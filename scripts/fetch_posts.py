#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抓取每篇文章正文，转为 Markdown 落地到 posts/<合集>/。

特性:
  - 断点续传: 已存在的 .md 跳过
  - 风控规避: 随机 UA + 随机延迟 + 每 N 篇长休息 + 遇验证页自动退避
  - 异常分类: 删除/付费/验证/超时 分别记录到 failed.json
"""
import json
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from bs4 import BeautifulSoup
import html2text

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(BASE, "posts")
DATA = os.path.join(BASE, "data")
STATE = os.path.join(BASE, "raw", "posts_state.json")

UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
]

RISK_WORDS = ["环境异常", "去验证", "验证码", "访问过于频繁", "请在微信客户端打开"]


def safe(s, limit=80):
    s = re.sub(r'[\\/:*?"<>|#\n\r\t]', "", str(s)).strip()
    s = re.sub(r"\s+", " ", s)
    return s[:limit].strip() or "untitled"


def conv():
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False
    h.protect_links = True
    h.single_line_break = False
    h.baseurl = ""
    h.mark_code = True  # <pre> 输出 ``` 围栏, 否则只做缩进
    return h


def fetch_html(url, timeout=30, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", random.choice(UAS))
            req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
            req.add_header("Referer", "https://mp.weixin.qq.com/")
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", errors="ignore")
        except Exception as e:  # noqa: BLE001
            last = repr(e)
            time.sleep(3 + i * 3)
    return {"__error__": last}


def extract(html):
    """返回 (正文html, 状态) 状态: ok / deleted / risk / empty"""
    if isinstance(html, dict):
        return None, "error:" + str(html.get("__error__"))[:80]
    low = html[:6000]
    if any(w in html[:3000] for w in RISK_WORDS):
        return None, "risk"
    if "该内容已被发布者删除" in html or "此内容因违规无法查看" in html:
        return None, "deleted"
    m = re.search(r'id="js_content"(.*?)(?=<script|</body>)', html, re.S)
    if not m:
        if "js_content" not in html:
            return None, "no_content"
        m = re.search(r'id="js_content"(.*)', html, re.S)
    seg = m.group(1)
    cut = seg.find('<div class="js_pc_qr_code')
    if cut > 0:
        seg = seg[:cut]
    return seg, "ok"


def clean(seg):
    soup = BeautifulSoup(seg, "lxml")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    # 微信代码块: <pre><code><span>...</span><br/>...</code></pre>
    # 行内 span 是语法高亮, 不能拆; 真正的换行是 <br/>
    for pre in soup.find_all("pre"):
        for br in pre.find_all("br"):
            br.replace_with("\n")
        text = pre.get_text()
        pre.clear()
        tag = soup.new_tag("code")
        tag.string = text
        pre.append(tag)
    # 图片懒加载 -> 取真实地址
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("src") or ""
        if src:
            img["src"] = src
    body = soup.find("div", id="js_content") or soup
    return str(body)


def guess_lang(code):
    if re.search(r"(^|\n)\s*(library\(|require\()|<-", code):
        return "r"
    if re.search(r"(^|\n)\s*(import |def |from .+ import)", code):
        return "python"
    if re.search(r"(^|\n)\s*(conda |pip |cd |ls |mkdir |wget |curl )", code):
        return "bash"
    return ""


def fence(md):
    """html2text 新版把 <pre> 输出为 [code]...[/code] + 4空格缩进, 转为围栏"""
    def rep(m):
        body = m.group(1)
        lines = [l[4:] if l.startswith("    ") else l for l in body.split("\n")]
        code = "\n".join(lines).strip("\n")
        if not code.strip():
            return ""
        return "```%s\n%s\n```" % (guess_lang(code), code)
    return re.sub(r"\[code\]\n?(.*?)\n?\[/code\]", rep, md, flags=re.S)


def to_md(title, url, date, albums, seg):
    md = conv().handle(clean(seg))
    # 清理微信隐藏元素泄漏的 style 片段
    md = fence(md)
    md = re.sub(r'\s*style="[^"]*"\s*>', "", md)
    md = re.sub(r'^\s*>\s*$', "", md, flags=re.M)
    # 去掉纯空白行(微信空 section 产生) 与行尾空格
    md = "\n".join(l.rstrip() for l in md.split("\n"))
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"```\n{3,}", "```\n\n", md).strip()
    fm = [
        "---",
        "title: \"%s\"" % title.replace('"', "'"),
        "date: %s" % date,
        "source: %s" % url,
        "albums: [%s]" % ", ".join('"%s"' % a for a in albums),
        "---",
        "",
        "# %s" % title,
        "",
        "> 原文：%s" % url,
        "> 合集：%s" % " / ".join(albums),
        "",
        md,
        "",
    ]
    return "\n".join(fm)


def main():
    # argv[1] = 并发数(默认4), argv[2] = 限量(0=全部)
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    with open(os.path.join(DATA, "articles.json"), encoding="utf-8") as f:
        arts = json.load(f)
    with open(os.path.join(DATA, "albums.json"), encoding="utf-8") as f:
        albums = json.load(f)
    id2name = {a["album_id"]: a["name"] for a in albums}
    order = {a["album_id"]: a["index"] for a in albums}
    safe_album = {a["album_id"]: "%02d-%s" % (a["index"], safe(a["name"], 40))
                  for a in albums}

    os.makedirs(POSTS, exist_ok=True)
    os.makedirs(os.path.dirname(STATE), exist_ok=True)

    failed = {}
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            failed = json.load(f).get("failed", {})

    # 主归类: 取 order 最小(最靠前)的合集
    def primary(a):
        als = [x for x in a["albums"] if x["album_id"] in order]
        if not als:
            return None
        return min(als, key=lambda x: order[x["album_id"]])

    todo = []
    for i, a in enumerate(arts):
        p = primary(a)
        if not p:
            continue
        d = os.path.join(POSTS, safe_album[p["album_id"]])
        fn = os.path.join(d, "%04d-%s.md" % (i + 1, safe(a["title"], 60)))
        todo.append((fn, d, a, p))

    if limit:
        todo = todo[:limit]

    done = sum(1 for fn, _, _, _ in todo if os.path.exists(fn))
    print("待抓取 %d 篇, 已完成 %d 篇" % (len(todo), done))

    lock = threading.Lock()
    stat = {"ok": 0, "bad": 0, "skip": 0, "risk": 0}
    stop = threading.Event()

    def work(item):
        if stop.is_set():
            return None
        fn, d, a, p = item
        if os.path.exists(fn):
            with lock:
                stat["skip"] += 1
            return None
        os.makedirs(d, exist_ok=True)
        html = fetch_html(a["url"])
        seg, st = extract(html)
        with lock:
            cur = stat["ok"] + stat["bad"]
        if st != "ok":
            with lock:
                stat["bad"] += 1
                failed[a["msgid"]] = {"title": a["title"], "url": a["url"],
                                      "status": st}
                if st == "risk":
                    stat["risk"] += 1
                    r = stat["risk"]
            if st == "risk":
                print("  [!] 风控命中 #%d, 退避 45s | %s" % (r, a["title"][:28]))
                time.sleep(45)
                if r >= 6:
                    print("  !! 风控累计 6 次, 停止。稍后重跑即可续传。")
                    stop.set()
            return st
        names = [id2name.get(x["album_id"], "") for x in a["albums"]]
        md = to_md(a["title"], a["url"], a["date"], [x for x in names if x], seg)
        if len(md) < 200:
            with lock:
                stat["bad"] += 1
                failed[a["msgid"]] = {"title": a["title"], "url": a["url"],
                                      "status": "too_short"}
            return "too_short"
        with open(fn, "w", encoding="utf-8") as f:
            f.write(md)
        with lock:
            stat["ok"] += 1
            n = stat["ok"]
        if n % 25 == 0:
            print("  进度 ok=%d bad=%d risk=%d" % (n, stat["bad"], stat["risk"]))
            with lock:
                json.dump({"failed": failed, "ok": stat["ok"],
                           "bad": stat["bad"]},
                          open(STATE, "w", encoding="utf-8"),
                          ensure_ascii=False, indent=1)
        time.sleep(random.uniform(0.8, 1.8))
        return "ok"

    print("并发数 %d, 待处理 %d 篇" % (workers, len(todo)))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(work, it) for it in todo]
        try:
            for f in as_completed(futs):
                f.result()
        except KeyboardInterrupt:
            stop.set()
            print("  中断, 等待已提交任务收尾...")

    with open(STATE, "w", encoding="utf-8") as f:
        json.dump({"failed": failed, "ok": stat["ok"], "bad": stat["bad"]},
                  f, ensure_ascii=False, indent=1)
    print("\n完成: 成功 %d / 跳过 %d / 失败 %d (风控 %d)"
          % (stat["ok"], stat["skip"], stat["bad"], stat["risk"]))


if __name__ == "__main__":
    main()
