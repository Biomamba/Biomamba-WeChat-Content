---
title: "用Excel他不香么？"
date: 2021-02-19
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484071&idx=1&sn=58d09c6198e3ee0ad6a87281b2686f7b&chksm=9b3f7bf7ac48f2e1977a75fb8e9dd3c15253bab9f5c5859b0cd8339d87b388277c47d4e0fa29#rd
albums: ["答读者问", "漫谈胡侃"]
---

# 用Excel他不香么？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484071&idx=1&sn=58d09c6198e3ee0ad6a87281b2686f7b&chksm=9b3f7bf7ac48f2e1977a75fb8e9dd3c15253bab9f5c5859b0cd8339d87b388277c47d4e0fa29#rd
> 合集：答读者问 / 漫谈胡侃

最近有粉丝求助，希望能够按照其要求对文件进行拆分，具体要求如下：A014行的中位值7.92，分别输出文件的A014行大于中位数的列与小于中位数的列。讲道理，中位数都求出来了，这种操作在Excel中进行排序岂不是最简单的方式。既然希望通过R实现，那就写一手吧。

数据如下：

![](../../images/8a93b4c8c71e8488.webp)
代码也很简单，仅仅几行：

  *   *   *   *   *   *   *   *   *   *   *

```r
setwd("工作路径")#设置工作路径yourdata <- read.table("test.txt",sep = "\t",header = T,row.names = 1)mediannumber <- fivenum(yourdata[row.names(yourdata)=="A014",])[[3]]#还是先求个中位数吧big <- yourdata[,yourdata[row.names(yourdata)=="A014",]>mediannumber]#取出对应的列small <- yourdata[,yourdata[row.names(yourdata)=="A014",]<mediannumber]#同上write.csv(big,"big.csv")write.csv(small,"small.csv")#write。table有时会造成行首的平移-
```
