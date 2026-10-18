---
title: "代码复写《Developmental Cell》|利用scRNA-seq对新生儿~成人肝脏发育和成熟的时间分析"
date: 2025-01-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526426&idx=1&sn=7191649a25332d1b8bf2bd9c797d06a7&chksm=9b3c114aac4b985cd9d16e134892c140111b32493063036363b39119ef7aad205a3c12bba867#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写《Developmental Cell》|利用scRNA-seq对新生儿~成人肝脏发育和成熟的时间分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526426&idx=1&sn=7191649a25332d1b8bf2bd9c797d06a7&chksm=9b3c114aac4b985cd9d16e134892c140111b32493063036363b39119ef7aad205a3c12bba867#rd
> 合集：单细胞教程全收录 / 全文复现

****

![](../../images/399758fa7d6941c2.png)

学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png) 本次教程中，我们复写了题为"Temporal analyses of postnatal liver development and maturation by single-cell transcriptomics"的文章(DOI: 10.1016/j.devcel.2022.01.004)。本研究提供了详细的图谱，通过单细胞分辨率的逐步变化，以说明新生儿肝脏如何发育成主要代谢器官。通过拟时序分析揭示了肝细胞和liver sinusoid endothelial cells （LSEC ）在代谢区构建中的渐进和协同发育和功能成熟的过程。主要发现包括：(1）在 D7 鉴定出一组巨噬细胞，其表现出巨噬细胞和内皮细胞的混合表型。(2) 分析预测了出生后的肝脏生物钟受 Bhlhe40 （Dec1） 等因素的调节，还推断了几个关键代谢途径适应新生儿生命剧烈环境变化的动态变化。(3) Dcn+ macrophage (Dcn+ Mac) 和 Treg 细胞之间的 CXCL12-GRK6-CXCR4 信号传导可能促进 Treg 细胞的募集和活性
本教程基于Linux中的Rstudio环境演示，计算资源不足的同学可参考：
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[配置一个心仪的工作站(硬件+环境配置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519707&idx=1&sn=73dcab26f9b2ed75a954327317d07112&chksm=9b3cf48bac4b7d9df5b5a432fbe70d4f9c13bc8d739aa401732614f022223d1912642a7e4bea&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)

本教程**复现集锦** ：

![](../../images/1fe10ae568464c51.webp)

**-Biomamba**

![](../../images/7d247e6c6ef19f87.png)

![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

学习手册以html文件格式提供，可在浏览器中打开并翻阅学习

![](../../images/cf128d973b63555f.gif)

**教程目录** ：

**一、文献解读**

1.0复现集锦1.1背景介绍1.2主要内容1.3总结讨论

**二、准备工作**

2.1硬件准备
2.2单细胞基础

**三、数据下载、处理和可视化**

1.‍数据下载‍2.读取数据（h5数据）3.Seurat标准流程4.拆分出肝细胞并按照时间点拆分细胞进行分析5.Monocle2拟时序分析6.不同时间点免疫细胞比例7.细胞通讯分析

**四、参考**

文末下载链接中包含的内容：

![](../../images/d24fe444bdee1921.webp)

测试文件约**2.4GB** ，大家注意按需下载！

![](../../images/7d247e6c6ef19f87.png)

解锁前需阅读：[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)![](../../images/f08cdfe212eb6283.png)

文末还可解锁以下内容

![](../../images/2cc9da4d1e6321da.png)![](../../images/556752da2b520ff6.png)

龙年订阅合集持续更新中，联系客服微信[**Biomamba_yunying**]可以119￥获取全部资料(包括今年后面更新的内容)。当然，付费不是目的，以下资料都可以通过**转发领取**(更推荐这种方式)。

[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)
[单细胞Figure 1常见图表](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509260&idx=1&sn=9ff90a428c3f22d43a31ec864e2d8a94&chksm=9b3cdc5cac4b554a2f7cb2a6368f7df9a9a3f6e406eb070663f53d81841a76e188c0b50727de&scene=21#wechat_redirect>)
[快速上手Seurat V5](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0&scene=21#wechat_redirect>)
[机器学习基础手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&chksm=9b3cd139ac4b582f23dd0ca65dcc66bed80b4240da76ee5abfbb61ec1bf62674ebfd2c50a45e&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)
[Bulk RNASeq| 转录组实战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510793&idx=1&sn=bfa69e8f261932d9bea74443fab732f0&chksm=9b3cd259ac4b5b4fd4b3bb80d0210a3396cda777b32ab49be1a45339453db314bb2a17fc438d&scene=21#wechat_redirect>)[scRNA-Seq双细胞过滤手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&chksm=9b3cd716ac4b5e00122eac47f55085198040a4a0e97c56895bbc39f3a9f1a1eb4eba27048a8f&scene=21#wechat_redirect>)
[CellChat空转细胞通讯合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512011&idx=1&sn=fbd41832c5995d79fead016931d3bfbd&chksm=9b3cd69bac4b5f8d16e7d8b8eeb5490e4938daf68902b06a8d60e25f150ec4ec459796f3aaac&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V5更新版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&chksm=9b3cf48fac4b7d99e65eba6d4c66c63e40b1d187fa1d9e6449d6cd07d5dec5127cff54886f93&scene=21#wechat_redirect>)
[SCENIC转录因子调控网络图](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520750&idx=1&sn=496bead1531a7eddd5c286030d350745&chksm=9b3ce8beac4b61a8589a1f8a66bd0571e09c0646655b6d805348bf6f4a0c7b52851615c22868&scene=21#wechat_redirect>)
[scATAC分析学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&chksm=9b3cec34ac4b6522977cb002919634af5334eec170b32f4961826dafb42f44f611144b159b2b&scene=21#wechat_redirect>)
[单细胞拷贝数变异学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522733&idx=1&sn=4e3a0707fd8f83b5ad9377bc91ee8e53&scene=21#wechat_redirect>)
[microRNA-靶标相互作用及疾病和药物关联分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247523676&idx=1&sn=6dad381e38df9ad63b90ed5935b73bf0&scene=21#wechat_redirect>)[《NC》代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性和间充质成纤维细胞增加](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247525649&idx=1&sn=6145f50422ef8680be2a7ffd6c66f5f3&scene=21#wechat_redirect>)
[《Nature Communications》| scRNA-seq揭示头颈癌早期转移过程中潜在的免疫逃避机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526011&idx=1&sn=e601b8dedfad86ee6d9ce5b6d6ca8511&scene=21#wechat_redirect>)

![](../../images/3536da08710707f3.png)![](../../images/399758fa7d6941c2.png)

订阅后获取学习手册下载链接：

![](../../images/fbfc4b8be383f432.png)
