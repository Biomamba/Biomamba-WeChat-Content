#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抓取 Biomamba 生信基地公众号全部合集(album)及其文章列表。
数据源: 微信 appmsgalbum JSON 接口
输出: raw/albums/<album_id>.json  (原始分页合并结果)
"""
import json
import os
import random
import time
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE, "raw", "albums")
os.makedirs(OUT_DIR, exist_ok=True)

BIZ = "MzAwMzIzOTk5OQ=="

# 从索引页解析出的合集清单: (album_id, 合集名)
ALBUMS = [
    ("2168829347397156865", "单细胞教程全收录"),
    ("2879312479804489730", "空间转录组"),
    ("2959853503529910274", "Bulk RNA-seq"),
    ("4512393426008801292", "AIDD & CADD"),
    ("4586640069750685707", "AI时代，不用就会被淘汰"),
    ("3889788454284181504", "编程语言教程"),
    ("2725521219349151745", "服务器"),
    ("3168648680917467142", "在线工具"),
    ("3403706694394970115", "单细胞云平台"),
    ("3721493119318310916", "生信基地"),
    ("4609993129990291458", "生信分析服务/个性化分析"),
    ("3674593374767628288", "实验基地"),
    ("2453318094304673794", "答读者问"),
    ("2649634741759279105", "粉丝来稿"),
    ("3567317259540447238", "基金申报"),
    ("2802463431357661184", "文献速递"),
    ("2697849917016670209", "漫谈胡侃"),
    ("2672902529483309057", "求职/求学/招聘"),
    ("3722529418976378880", "千里姻缘一线牵"),
    ("2774482520754388994", "送周边"),
    ("2981710763847614469", "全文复现"),
    ("4421772406013378566", "专题班/R语言scRNA-seq分析系列"),
    ("4470288526508818453", "单细胞全程班理论习题检测"),
]

UAS = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.20(0x18001426) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002832) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 12; SM-G9910 Build/SP1A.210812.016; wv) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 "
    "MicroMessenger/8.0.32.2300(0x28002051) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN",
]


def fetch(album_id, begin_msgid=None, begin_itemidx=None, retries=3):
    params = {
        "__biz": BIZ,
        "action": "getalbum",
        "album_id": album_id,
        "f": "json",
        "count": "10",
    }
    if begin_msgid is not None:
        params["begin_msgid"] = str(begin_msgid)
        params["begin_itemidx"] = str(begin_itemidx)
    url = "https://mp.weixin.qq.com/mp/appmsgalbum?" + urllib.parse.urlencode(params)

    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", random.choice(UAS))
            req.add_header("Referer", "https://mp.weixin.qq.com/")
            req.add_header("Accept", "application/json, text/plain, */*")
            req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
            with urllib.request.urlopen(req, timeout=25) as resp:
                raw = resp.read().decode("utf-8", errors="ignore")
            data = json.loads(raw)
            if data.get("base_resp", {}).get("ret") == 0:
                return data
            last_err = "ret=%s" % data.get("base_resp", {}).get("ret")
        except Exception as e:  # noqa: BLE001
            last_err = repr(e)
        time.sleep(2 + attempt * 2)
    print("    ! 请求失败: %s (album=%s)" % (last_err, album_id))
    return None


def grab_album(album_id, name):
    out_path = os.path.join(OUT_DIR, "%s.json" % album_id)
    if os.path.exists(out_path):
        with open(out_path, encoding="utf-8") as f:
            cached = json.load(f)
        if cached.get("complete"):
            print("  = 跳过(已完成): %s [%s] 共 %d 篇"
                  % (name, album_id, len(cached["articles"])))
            return cached

    all_arts = {}
    base_info = None
    begin_msgid = None
    begin_itemidx = None
    page = 0
    while True:
        page += 1
        data = fetch(album_id, begin_msgid, begin_itemidx)
        if not data:
            break
        resp = data.get("getalbum_resp") or {}
        if base_info is None:
            base_info = resp.get("base_info", {})
        arts = resp.get("article_list") or []
        # 微信接口在仅剩 1 条时会返回单个对象而非数组
        if isinstance(arts, dict):
            arts = [arts]
        arts = [a for a in arts if isinstance(a, dict) and a.get("msgid")]
        if not arts:
            break
        for a in arts:
            all_arts[a["msgid"] + "_" + a.get("itemidx", "1")] = a
        flag = resp.get("continue_flag")
        print("    页%02d 累计 %d/%s" % (page, len(all_arts),
                                       (base_info or {}).get("article_count", "?")))
        if not flag:
            break
        last = arts[-1]
        begin_msgid = last.get("msgid")
        begin_itemidx = last.get("itemidx", "1")
        time.sleep(random.uniform(0.9, 1.8))
    result = {
        "album_id": album_id,
        "name": name,
        "base_info": base_info or {},
        "expected_count": int((base_info or {}).get("article_count", 0) or 0),
        "fetched_count": len(all_arts),
        "complete": bool(base_info) and len(all_arts) >= int(
            (base_info or {}).get("article_count", 0) or 0),
        "articles": list(all_arts.values()),
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print("  -> %s [%s] 抓取 %d 篇 / 应有 %s 篇  complete=%s"
          % (name, album_id, len(all_arts),
             (base_info or {}).get("article_count", "?"), result["complete"]))
    return result


def main():
    print("开始抓取 %d 个合集 ..." % len(ALBUMS))
    summary = []
    for aid, name in ALBUMS:
        print("[%s] %s" % (aid, name))
        r = grab_album(aid, name)
        summary.append({
            "album_id": r["album_id"],
            "name": r["name"],
            "expected_count": r["expected_count"],
            "fetched_count": r["fetched_count"],
            "complete": r["complete"],
        })
        time.sleep(random.uniform(1.0, 2.0))
    with open(os.path.join(BASE, "raw", "albums_summary.json"), "w",
              encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    tot = sum(s["fetched_count"] for s in summary)
    print("\n完成: %d 个合集, 累计 %d 篇文章条目" % (len(summary), tot))


if __name__ == "__main__":
    main()
