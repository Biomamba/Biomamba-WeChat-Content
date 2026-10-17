#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 raw/albums/*.json 整理为按合集分类的 Markdown 索引 + 结构化 JSON。
输出:
  content/<NN>-<合集名>.md   每个合集一篇文章清单
  README.md                   总览索引
  data/albums.json            合集元数据
  data/articles.json          全部文章(去重, 带所属合集)
"""
import json
import os
import re
import time
from collections import OrderedDict
from urllib.parse import quote

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw", "albums")
CONTENT = os.path.join(BASE, "content")
DATA = os.path.join(BASE, "data")

# 合集展示顺序(按内容重要性排列)
ORDER = [
    "2168829347397156865",  # 单细胞教程全收录
    "2879312479804489730",  # 空间转录组
    "2959853503529910274",  # Bulk RNA-seq
    "2981710763847614469",  # 全文复现
    "3889788454284181504",  # 编程语言教程
    "2725521219349151745",  # 服务器
    "4512393426008801292",  # AIDD & CADD
    "4586640069750685707",  # AI时代
    "2453318094304673794",  # 答读者问
    "2802463431357661184",  # 文献速递
    "3567317259540447238",  # 基金申报
    "3403706694394970115",  # 单细胞云平台
    "3168648680917467142",  # 在线工具
    "4421772406013378566",  # 专题班
    "4470288526508818453",  # 单细胞全程班习题
    "4609993129990291458",  # 生信分析服务
    "3721493119318310916",  # 生信基地
    "3674593374767628288",  # 实验基地
    "2649634741759279105",  # 粉丝来稿
    "2697849917016670209",  # 漫谈胡侃
    "2672902529483309057",  # 求职/求学/招聘
    "2774482520754388994",  # 送周边
    "3722529418976378880",  # 千里姻缘一线牵
]


def safe_name(name):
    """把合集名转为安全的目录/文件名"""
    s = re.sub(r'[\\/:*?"<>|]', "", name)
    s = s.replace("&", "and").replace("｜", "").replace("|", "")
    s = re.sub(r"\s+", "", s)
    return s.strip()


def ts2date(ts):
    try:
        return time.strftime("%Y-%m-%d", time.localtime(int(ts)))
    except Exception:  # noqa: BLE001
        return ""


def https(u):
    if u.startswith("http://"):
        return "https://" + u[len("http://"):]
    return u


def main():
    os.makedirs(CONTENT, exist_ok=True)
    os.makedirs(DATA, exist_ok=True)

    albums = OrderedDict()
    for fn in sorted(os.listdir(RAW)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(RAW, fn), encoding="utf-8") as f:
            d = json.load(f)
        arts = d["articles"]
        # 按 pos_num 倒序 (合集内最新在前) -> 转为发布时间正序更符合教程阅读
        for a in arts:
            a["url"] = https(a.get("url", ""))
            a["date"] = ts2date(a.get("create_time", ""))
        try:
            arts.sort(key=lambda x: int(x.get("pos_num", 0)))
        except Exception:  # noqa: BLE001
            pass
        albums[d["album_id"]] = d

    ordered_ids = [i for i in ORDER if i in albums]
    ordered_ids += [i for i in albums if i not in ORDER]

    # ---------- 结构化数据 ----------
    art_map = OrderedDict()
    album_meta = []
    for idx, aid in enumerate(ordered_ids, 1):
        d = albums[aid]
        safe = safe_name(d["name"])
        rel = "content/%02d-%s.md" % (idx, safe)
        album_meta.append({
            "index": idx,
            "album_id": aid,
            "name": d["name"],
            "safe_name": safe,
            "file": rel,
            "expected_count": d["expected_count"],
            "fetched_count": d["fetched_count"],
            "complete": d["complete"],
        })
        for pos, a in enumerate(d["articles"], 1):
            key = a["msgid"] + "_" + a.get("itemidx", "1")
            rec = {
                "msgid": a["msgid"],
                "itemidx": a.get("itemidx", "1"),
                "title": a["title"],
                "url": a["url"],
                "date": a["date"],
                "cover": a.get("cover_img_1_1", ""),
                "albums": [{"album_id": aid, "name": d["name"], "pos": pos}],
            }
            if key in art_map:
                art_map[key]["albums"].append(
                    {"album_id": aid, "name": d["name"], "pos": pos})
            else:
                art_map[key] = rec

    with open(os.path.join(DATA, "albums.json"), "w", encoding="utf-8") as f:
        json.dump(album_meta, f, ensure_ascii=False, indent=1)
    with open(os.path.join(DATA, "articles.json"), "w", encoding="utf-8") as f:
        json.dump(list(art_map.values()), f, ensure_ascii=False, indent=1)

    # ---------- 直接扫描 posts/ 目录建立 存档路径映射 ----------
    # 文件名规则: posts/<NN-合集>/<全局序号4位>-<标题>.md, 序号 = articles.json 顺序
    import glob
    post_by_idx = {}
    posts_dir = os.path.join(BASE, "posts")
    if os.path.isdir(posts_dir):
        for p in glob.glob(os.path.join(posts_dir, "*", "*.md")):
            b = os.path.basename(p)
            m = re.match(r"(\d+)-", b)
            if m:
                rel = "posts/" + os.path.basename(os.path.dirname(p)) \
                    + "/" + b
                post_by_idx[int(m.group(1))] = rel.replace("\\", "/")
    arts_list = list(art_map.values())
    post_of = {}
    for i, a in enumerate(arts_list, 1):
        if i in post_by_idx:
            post_of[a["msgid"] + "_" + a.get("itemidx", "1")] = post_by_idx[i]

    # ---------- 每个合集一个 Markdown ----------
    for m in album_meta:
        aid = m["album_id"]
        d = albums[aid]
        lines = []
        lines.append("# %s" % d["name"])
        lines.append("")
        lines.append("> 合集 ID：`%s` ｜ 篇数：**%d** ｜ 抓取状态：%s"
                     % (aid, d["fetched_count"],
                        "完整" if d["complete"] else "不完整(可能分页受限)"))
        lines.append("")
        lines.append("[[返回总索引]](../README.md)")
        lines.append("")
        has_post = any((a["msgid"] + "_" + a.get("itemidx", "1")) in post_of
                       for a in d["articles"])
        if has_post:
            lines.append("> 跨合集文章统一归档在其**主合集**目录下，"
                         "故部分「本地存档」链接指向其他合集目录。")
            lines.append("")
            lines.append("| # | 标题 | 年份 | 原文 | 本地存档 |")
            lines.append("|---|---|---|---|---|")
        else:
            lines.append("| # | 标题 | 年份 | 原文 |")
            lines.append("|---|---|---|---|")
        for pos, a in enumerate(d["articles"], 1):
            title = a["title"].replace("|", "／").replace("\n", " ").strip()
            year = a["date"][:4] if a["date"] else ""
            row = "| %d | %s | %s | [链接](%s) " % (pos, title, year, a["url"])
            if has_post:
                p = post_of.get(a["msgid"] + "_" + a.get("itemidx", "1"))
                row += "| %s |" % ("[阅读](../%s)" % quote(p, safe="/")
                                   if p else "—")
            lines.append(row)
        lines.append("")
        p = os.path.join(BASE, m["file"])
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    # ---------- 总索引 README ----------
    total = sum(m["fetched_count"] for m in album_meta)
    uniq = len(art_map)
    r = []
    r.append("# Biomamba 生信基地 · 内容全索引")
    r.append("")
    r.append("> 按公众号**合集（专辑）**整理的内容导航。")
    r.append("> 原文版权归 Biomamba 生信基地所有，本仓库仅做索引与学习导航。")
    r.append("")
    r.append("- 合集数：**%d**" % len(album_meta))
    r.append("- 条目数：**%d**（跨合集去重后 **%d** 篇）" % (total, uniq))
    if post_of:
        r.append("- 正文存档：**%d** 篇（`posts/`，按合集分目录，含代码块）"
                 % len(post_of))
    r.append("- 官网：https://www.biomamba.cn")
    r.append("- 生成时间：%s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    r.append("")
    r.append("## 合集导航")
    r.append("")
    r.append("| # | 合集 | 篇数 | 索引页 |")
    r.append("|---|---|---:|---|")
    for m in album_meta:
        r.append("| %d | %s | %d | [%s](%s) |"
                 % (m["index"], m["name"], m["fetched_count"],
                    "%02d-%s.md" % (m["index"], m["safe_name"]),
                    m["file"].replace("\\", "/")))
    r.append("")
    r.append("## 数据文件")
    r.append("")
    r.append("- `data/albums.json` — 合集元数据")
    r.append("- `data/articles.json` — 全部文章（含所属合集、发布时间、链接）")
    r.append("- `scripts/fetch_albums.py` — 抓取脚本（可增量更新）")
    r.append("")
    with open(os.path.join(BASE, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(r))

    print("合集 %d 个, 条目 %d, 去重文章 %d 篇" % (len(album_meta), total, uniq))
    for m in album_meta:
        flag = "" if m["complete"] else "  <== 不完整"
        print("  %02d %-28s %4d 篇%s"
              % (m["index"], m["name"], m["fetched_count"], flag))


if __name__ == "__main__":
    main()
