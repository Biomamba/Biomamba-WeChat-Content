---
title: "scRNA-Seq学习手册(基于Seurat V5)"
date: 2026-08-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&chksm=9b3c26bbac4bafad95197f607f819302567eb4f79327634c054a1715c4689e0886d326e7bda8#rd
albums: ["单细胞教程全收录"]
---

# scRNA-Seq学习手册(基于Seurat V5)

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&chksm=9b3c26bbac4bafad95197f607f819302567eb4f79327634c054a1715c4689e0886d326e7bda8#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)这里我们重置了我们在B站上播放量已逾**三十万** 的单细胞课程代码(1~7节近五个小时的基础视频课：https://www.bilibili.com/video/BV1S44y1b76Z)，并通过Rmarkdown的形式编译成了一个**学习手册**(HTML文件，用浏览器打开，在**文末获取**)，其中包含了课程涉及到的视频、代码、测试文件和输出结果(学有余力的同学推荐自行去官网整理：https://satijalab.org/seurat/)。为了避免Seurat V5可能带来的bug，本次教程使用最新版的Seurat V5进行修订与编译([快速上手Seurat V5](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0&scene=21#wechat_redirect>))，希望该手册可以帮助大家完成单细胞基础分析的**一站式学习** ，更习惯使用V4的同学可以参考：[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)。![](../../images/ad2c12a8a9f75c21.webp)

更多单细胞教程可见：[少走点单细胞的弯路](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510768&idx=1&sn=cead60ac55bf28910f5cf220d723fe05&chksm=9b3cd3a0ac4b5ab68b1a11e981eea4a23aae26cd2bf48f886f834b0893c73cca31072b224a39&scene=21#wechat_redirect>)

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)![](../../images/f8154c26e0e90f06.gif)

文末下载链接中包含的内容：

![](../../images/f42d88d7561e6fee.webp)
![](../../images/7d247e6c6ef19f87.png)
解锁前需阅读：[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)
![](../../images/f08cdfe212eb6283.png)

文末还可解锁以下内容

![](../../images/2cc9da4d1e6321da.png)![](../../images/556752da2b520ff6.png)

龙年订阅合集持续更新中，联系客服微信[Biomamba_yunying]可以119￥获取全部资料(包括今年后面更新的内容)。当然，付费不是目的，以下资料都可以通过**转发领取**(更推荐这种方式)。

[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)
[单细胞Figure 1常见图表](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509260&idx=1&sn=9ff90a428c3f22d43a31ec864e2d8a94&chksm=9b3cdc5cac4b554a2f7cb2a6368f7df9a9a3f6e406eb070663f53d81841a76e188c0b50727de&scene=21#wechat_redirect>)
[快速上手Seurat V5](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0&scene=21#wechat_redirect>)
[机器学习基础手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&chksm=9b3cd139ac4b582f23dd0ca65dcc66bed80b4240da76ee5abfbb61ec1bf62674ebfd2c50a45e&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)
[Bulk RNASeq| 转录组实战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510793&idx=1&sn=bfa69e8f261932d9bea74443fab732f0&chksm=9b3cd259ac4b5b4fd4b3bb80d0210a3396cda777b32ab49be1a45339453db314bb2a17fc438d&scene=21#wechat_redirect>)[scRNA-Seq双细胞过滤手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&chksm=9b3cd716ac4b5e00122eac47f55085198040a4a0e97c56895bbc39f3a9f1a1eb4eba27048a8f&scene=21#wechat_redirect>)
[CellChat空转细胞通讯合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512011&idx=1&sn=fbd41832c5995d79fead016931d3bfbd&chksm=9b3cd69bac4b5f8d16e7d8b8eeb5490e4938daf68902b06a8d60e25f150ec4ec459796f3aaac&scene=21#wechat_redirect>)

![](../../images/3536da08710707f3.png)![](../../images/399758fa7d6941c2.png)

订阅后获取学习手册下载链接：

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)提取码请联系客服微信[Biomamba_zhushou]

https://pan.baidu.com/s/1GpjTmwLFO_BFwJq3-IGQzg

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)
