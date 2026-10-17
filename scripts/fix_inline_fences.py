#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 ``` 后直接粘连正文的行: 非语言标记的拆成两行"""
import glob
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = {
    "r", "R", "python", "Python", "bash", "sh", "shell", "zsh", "console",
    "javascript", "js", "typescript", "ts", "sql", "json", "perl", "html",
    "css", "java", "c", "cpp", "matlab", "julia", "text", "txt", "markdown",
    "md", "yaml", "yml", "diff", "xml", "",
}


def main():
    files = sorted(glob.glob(os.path.join(BASE, "posts", "*", "*.md")))
    changed = 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        out = []
        mod = False
        for line in text.split("\n"):
            if line.startswith("```") and len(line) > 3:
                rest = line[3:]
                tag = rest.strip().rstrip("{}").strip()
                if tag not in LANGS:
                    out.append("```")
                    out.append(rest)
                    mod = True
                    continue
            out.append(line)
        if mod:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write("\n".join(out))
            changed += 1
            print("修复:", os.path.basename(f))
    # 复查闭合
    fence = "`" * 3
    odd = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        if t.count(fence) % 2:
            odd.append(os.path.basename(f))
    print("拆行修复 %d 篇; 仍不闭合 %d 篇: %s"
          % (changed, len(odd), ", ".join(odd[:5]) if odd else "无"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
