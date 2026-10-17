#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 Markdown 围栏不闭合: ``` 数量为奇数时在文末补齐; 并输出诊断"""
import glob
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FENCE = "`" * 3


def main():
    files = sorted(glob.glob(os.path.join(BASE, "posts", "*", "*.md")))
    fixed, clean = [], []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        n = text.count(FENCE)
        if n % 2 == 0:
            clean.append(f)
            continue
        # 找出所有围栏行
        lines = text.split("\n")
        fl = [i for i, l in enumerate(lines) if l.strip().startswith(FENCE)]
        print("不闭合: %s" % os.path.basename(f))
        for i in fl:
            print("   L%-5d %s" % (i + 1, lines[i][:70]))
        # 正文内孤立的 ``` 行(非配对)极罕见, 多为转换丢失; 文末补齐保证渲染
        if not text.endswith("\n"):
            text += "\n"
        text += FENCE + "\n"
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text)
        fixed.append(f)
    print("\n检查 %d 篇: 正常 %d, 修复 %d"
          % (len(files), len(clean), len(fixed)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
