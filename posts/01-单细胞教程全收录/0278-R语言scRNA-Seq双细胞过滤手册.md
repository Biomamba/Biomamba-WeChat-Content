---
title: "R语言scRNA-Seq双细胞过滤手册"
date: 2026-05-18
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537859&idx=3&sn=84cc128e093fac63a5a97421dfe8be53&chksm=9b3c2d93ac4ba4859ab08e62421ff663b45cf0ddfa809f918b9d40cbd9c2b2b8b9f0779f05e9#rd
albums: ["单细胞教程全收录"]
---

# R语言scRNA-Seq双细胞过滤手册

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537859&idx=3&sn=84cc128e093fac63a5a97421dfe8be53&chksm=9b3c2d93ac4ba4859ab08e62421ff663b45cf0ddfa809f918b9d40cbd9c2b2b8b9f0779f05e9#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

双细胞过滤学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)无论是哪个平台的单细胞测序技术(微流控、微室、微滴等)，在建库过程中都会或多或少的形成一定比例的**双细胞**(doublets)，即**两个或多个** 细胞混进了一个单细胞建库体系中从而被带上了**相同的barcode** 。这样的情况会导致这种”单细胞”常常会包含多个(homotypic doublets)、甚至多种细胞(heterotypic doublets)混合而成的表达矩阵，从而造成对数据分析的干扰。为了避免这一现象，反应体系以及实验流程的优化是”湿实验”部分需要解决的问题(例如：cell hashing、species mixture、demuxlet、MULTI-seq等平台或技术)。但是这通常会带来更复杂的实验步骤和更高的实验时间与花费，而且实验的优化并不能解决已包含doublets数据的问题。因此**在数据分析与处理** 方面，同样需要优化流程。简单的过滤很多时候并不能完成doublets的过滤，目前有诸多计算工具能够帮助用户完成doublets、正常细胞、空液滴的判定。本次学习手册，我们先从**绪论** 说起，带大家一同比较doubletCells, Scrublet, cxds, bcds, hybrid, Solo, DoubletDetection, DoubletFinder等工具在**双细胞预测表现中的优劣**(benchmarking)，再进行DoubletFinder与cxds工具的**实操流程讲解** 。不熟悉分析过程的同学可以先行学习：[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)另外本手册涉及到的包比较占内存，硬件跟不上的同学可以参考：[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=2&sn=4708fac31ac8f4e347847e4b7f2a4fed&scene=21#wechat_redirect>)
分析图片集锦![](../../images/f2a3c1abed72280c.webp)

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

学习手册可直接用浏览器打开：

![](../../images/83f4dfcd705a76a6.webp)

下载的资料内容：

![](../../images/121409c1843b5794.png)
![](../../images/7d247e6c6ef19f87.png)
解锁前需阅读：[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)![](../../images/f08cdfe212eb6283.png)

文末还可解锁以下内容

![](../../images/2cc9da4d1e6321da.png)![](../../images/556752da2b520ff6.png)

龙年订阅合集已完结，联系客服微信[Biomamba_zhushou]可以以￥119获取全部资料(包括今年后面更新的内容)。当然，付费不是目的，以下资料都可以通过**转发领取**(更推荐这种方式)。

[龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)
[单细胞Figure 1常见图表](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509260&idx=1&sn=9ff90a428c3f22d43a31ec864e2d8a94&chksm=9b3cdc5cac4b554a2f7cb2a6368f7df9a9a3f6e406eb070663f53d81841a76e188c0b50727de&scene=21#wechat_redirect>)
[快速上手Seurat V5](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0&scene=21#wechat_redirect>)
[机器学习基础手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&chksm=9b3cd139ac4b582f23dd0ca65dcc66bed80b4240da76ee5abfbb61ec1bf62674ebfd2c50a45e&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)
[Bulk RNASeq| 转录组实战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510793&idx=1&sn=bfa69e8f261932d9bea74443fab732f0&chksm=9b3cd259ac4b5b4fd4b3bb80d0210a3396cda777b32ab49be1a45339453db314bb2a17fc438d&scene=21#wechat_redirect>)

[scRNA-Seq双细胞过滤手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&chksm=9b3cd716ac4b5e00122eac47f55085198040a4a0e97c56895bbc39f3a9f1a1eb4eba27048a8f&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[CellChat空转细胞通讯合辑](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512011&idx=1&sn=fbd41832c5995d79fead016931d3bfbd&chksm=9b3cd69bac4b5f8d16e7d8b8eeb5490e4938daf68902b06a8d60e25f150ec4ec459796f3aaac&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[scRNA-Seq学习手册Seurat V5更新版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&chksm=9b3cf48fac4b7d99e65eba6d4c66c63e40b1d187fa1d9e6449d6cd07d5dec5127cff54886f93&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[SCENIC转录因子调控网络图](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520750&idx=1&sn=496bead1531a7eddd5c286030d350745&chksm=9b3ce8beac4b61a8589a1f8a66bd0571e09c0646655b6d805348bf6f4a0c7b52851615c22868&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[scATAC分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&chksm=9b3cec34ac4b6522977cb002919634af5334eec170b32f4961826dafb42f44f611144b159b2b&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[单细胞拷贝数变异学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522733&idx=1&sn=4e3a0707fd8f83b5ad9377bc91ee8e53&chksm=9b3ce0fdac4b69ebf301818e3cccb668f443f66807d2a97edc463721d48392b52e10a262dfa7&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[microRNA-靶标相互作用及疾病和药物关联分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247523676&idx=1&sn=6dad381e38df9ad63b90ed5935b73bf0&chksm=9b3ce40cac4b6d1af13dc1d8188d1134fae12213f536abcce8c683b6fa8e68b6a48c5b417215&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《NC》代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性和间充质成纤维细胞增加](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247525649&idx=1&sn=6145f50422ef8680be2a7ffd6c66f5f3&chksm=9b3c1c41ac4b955748b6735bb43b27fb222f3795c4ae49bb8a453f78765fc472ff43f9e7fc89&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《Nature Communications》| scRNA-seq揭示头颈癌早期转移过程中潜在的免疫逃避机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526011&idx=1&sn=e601b8dedfad86ee6d9ce5b6d6ca8511&chksm=9b3c1f2bac4b963d523438200ea92f352bd84ab5fbb40a4b2220e7f1af77778f27aa1f728e47&scene=21&cur_album_id=3348420850777358342#wechat_redirect>)

[代码复写《Developmental Cell》|利用scRNA-seq对新生儿~成人肝脏发育和成熟的时间分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526426&idx=1&sn=7191649a25332d1b8bf2bd9c797d06a7&chksm=9b3c114aac4b985cd9d16e134892c140111b32493063036363b39119ef7aad205a3c12bba867&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[龙年订阅资料已完结~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526649&idx=1&sn=9f822b11a117b2435982d8a22e9f4545&chksm=9b3c11a9ac4b98bf4467e02c806db8b4c8cd9c74897a1d47e1c96ddbe111e6ef487f17d5ce7e&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

![](../../images/3536da08710707f3.png)![](../../images/399758fa7d6941c2.png)

学习手册下载链接：

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)本推送教程、测试文件下载链接：

https://pan.baidu.com/s/1_UCwVhC-grl9rg_zk1_xIQ

提取码请联系客服微信获取：

![](../../images/fe8ecb8594a1f419.webp)![](../../images/7d247e6c6ef19f87.png)![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532717&idx=2&sn=eb98e578098b9f432ea6ecbdc3c0d74b&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/acba43cb3408c3d0.webp) 您点的每个赞和在看，我都认真当成了喜欢
