---
title: "快速上手Seurat V5"
date: 2024-04-08
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0#rd
albums: ["单细胞教程全收录"]
---

# 快速上手Seurat V5

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

写在前面

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)Seurat包可以说是单细胞从业者的必修课，其主要的功能包括数据质控、归一化、降维、聚类、细胞亚群的识别和可视化(包括绘制热图、散点图、UMAP 和 t-SNE 等)，能够帮助用户快速、直观的分析单细胞数据。正因为Seurat的强大,我们此前的单细胞教程([二十万+播放量的单细胞教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505219&idx=1&sn=d92cc2048e0568669d32e74c8df76484&chksm=9b3cac13ac4b2505bd4f9e36f38eee4e0fce3aea0e191b18f5cc678995c2ccc883e391132784&scene=21#wechat_redirect>))也是基于其V3、V4版本制作。但现在Seurat的V5版本已经成为了CRAN的默认版本，我们此前也介绍过V5版本的文章([Seurat V5的《Nature Biotechnology》](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505826&idx=1&sn=5b9e4aeb41fc2f2943aeac9e22d4d038&chksm=9b3caef2ac4b27e4d57e75a508f00b5605ab99a7b51024110f54778683e14ed8bbcd743f0588&scene=21#wechat_redirect>))，这里我们整理了Seurat V5与V4的主要不同以及使用注意事项。有自学能力的同学可以参考：https://satijalab.org/seurat/更多学习资料可见：
[2023订阅资料已完结~](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508123&idx=1&sn=5211090a5013a94695d899d844cfe23e&chksm=9b3cd9cbac4b50dd65bbae0f76519bc670acb429b5ae3016d02e0474b19ed9bd2e1035a36b32&scene=21#wechat_redirect>)
[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>) **-Biomamba**

![](../../images/7d247e6c6ef19f87.png)

![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)一如既往地，我们整理好了测试文件和代码的html文件，供大家翻阅学习：

![](../../images/e65ebc0499f26091.gif)

目录及分析输出图片示例：

![](../../images/1b95a03a8088e29a.webp)

![](../../images/7d247e6c6ef19f87.png)

解锁前需阅读：[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)![](../../images/399758fa7d6941c2.png)

订阅后获取学习手册下载链接：

![](../../images/fbfc4b8be383f432.png)
