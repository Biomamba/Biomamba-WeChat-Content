---
title: "一文搞定单细胞免疫组库分析(scTCR+scBCR)"
date: 2025-09-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531049&idx=2&sn=1eedafb06d5d15f110f064bba354501c&chksm=9b3c0379ac4b8a6f58cbfb547c76ad7f7989c8292b653b5bba4b31b05825e53d0610f4750b0f#rd
albums: ["单细胞教程全收录"]
---

# 一文搞定单细胞免疫组库分析(scTCR+scBCR)

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531049&idx=2&sn=1eedafb06d5d15f110f064bba354501c&chksm=9b3c0379ac4b8a6f58cbfb547c76ad7f7989c8292b653b5bba4b31b05825e53d0610f4750b0f#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

scTCR&scBCR学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)**有多种”Bulk”水平 免疫组库测序技术，涉及从给定组织中分析混合的BCR或TCR。Bulk’s免疫组库测序技术在很大程度上仅限于分析单链（例如,只有TRB或IgH），并不能捕获适应性免疫受体的二聚体性质。文库构建和测序策略也阻碍了真正的配对链测序数据获取。****通过单细胞技术，使成对链的适应性免疫受体在规模上的分析成为可能。各种高通量测序TCRs和BCRs的技术。 针对BCR和TCR的VDJ序列的异质性，在cDNA的基础上，进一步进行扩增子测序，通过分析BCR和TCR的不同序列，分析免疫环境中的克隆型多样性，解析有机体抵制病原微生物入侵的免疫机制。****与[ scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)类似，通过微流控系统将带有条形码和引物的凝胶珠与单个细胞包裹在油滴中；接下来在每个油滴内，凝胶珠溶解，细胞裂解释放 mRNA，通过逆转录产生带有 10X barcode 和 UMI 信息的 cDNA。破油后，cDNA 一分为二，后续同时进行基因表达和免疫组库的文库构建。其中 TCR 或者 BCR 的 V(D)J 序列通过设计在 C 区的巢式引物进行 PCR 富集。测序后即可一次性获得大量单细胞的基因表达和免疫组库数据。结合[scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)数据与BCR/TCR多样性数据，解析免疫细胞中更高维度的异质性。****本学习手册将从单细胞免疫组库概论、cellranger VDJ定量、scRepertoire数据实战带领大家一同完成单细胞免疫组库数据的分析流程。** 本教程可视化集锦![](../../images/5c4b40fb3854d71e.webp)**
**更多生信教程可见：[生信基地终身订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530199&idx=1&sn=59e5e523b7c25fd1410f2b7b71a2d284&scene=21#wechat_redirect>)
本教程基于Linux中的Rstudio环境演示，计算资源不足的同学可参考：[选择西柚云的11个理由](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529471&idx=2&sn=c191f2df999820bf7f1f96832d120d2d&scene=21#wechat_redirect>)
[趁开学前| 入手足够完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530226&idx=2&sn=0522eb4eae67efeea2b96404474af611&scene=21#wechat_redirect>)
[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21#wechat_redirect>)
**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：

![](../../images/dd2582a4482cfeae.webp)

‍

**教程目录** ：

**一、准备工作**

**1.1 编程基础**

1.2 硬件基础

1.3 生信基础

**二、免疫组库测序**

**2.1 TCR和BCR**

**2.2 结构组成**

**2.3 单细胞免疫组库测序**

**2.4 分析流程**

**三、 cellranger VDJ**

**3.1 scBCR数据的上游定量**

**（1）下载**

**（2）参考基因组准备**

**（3）测试数据下载**

（4）软件运行

**3.2 scTCR数据的上游定量**

**（1）TCR测试数据下载**

**（2）准备配置文件**

**（3）软件运行**

**四、 scRepertoire**

4.1 红斑性头痛/正常皮肤演示数据

4.2 数据实操

（1）基本克隆可视化

（2）可视化克隆动力学

（3）整体序列分布概要

（4）比较样本克隆多样性、差异与相似性

（5）合并克隆和单细胞对象

（6）整合后数据可视化

（7）量化克隆偏差

（8）基于scBCR-seq数据的分析

（9）版本信息

****参考********单细胞教程全收录********欢迎致谢****

文末下载链接中包含以下内容：

![](../../images/026c8b03b44f6063.webp)

测试文件约**9.31GB** ，大家注意按需下载！

![](../../images/7d247e6c6ef19f87.png)
![图片](../../images/eab31beb8c0e41d2.png)

往期订阅

![图片](../../images/8b04fd62fd8f3d51.png)![图片](../../images/4064a50c19e8ad22.png)

生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[那就开放一个终身订阅吧~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)

2025已更新订阅内容：

[《Cell》复现|中性粒细胞scRNA-seq图谱阐明抗肿瘤抗原呈递效力](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526776&idx=1&sn=99eb6a16c7bf345445b6ff4b61110138&scene=21#wechat_redirect>)

[代码复现|scRNA-seq绘制透明细胞肾癌的免疫微环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527498&idx=1&sn=c8282e9d4175bfb2e572278312073d81&scene=21#wechat_redirect>)

[改造单细胞DoHeatmap](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527762&idx=1&sn=ba7c8a4cb704e71fa86ebfe1f19bffea&scene=21#wechat_redirect>)

[Slingshot拟时序分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527850&idx=1&sn=f4e2ca5e2e5e71eeaf132375bb8270eb&scene=21#wechat_redirect>)

[《Cancer Cell》|时空单细胞揭示CRC的PD-1治疗免疫细胞动态](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528056&idx=1&sn=73c0da3ff7ff50bafbb9315fd5b60f15&scene=21#wechat_redirect>)

[scRNA-seq数据基础分析手册(2025最新修订)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)

[代码复现|吞噬作用增强肿瘤中巨噬细胞的氧化代谢和免疫抑制特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528289&idx=1&sn=b56f00f3d8a4b152e54f3acd40aef21d&scene=21#wechat_redirect>)[一文学会scRNA Velocity剪切速率分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528458&idx=1&sn=900357283922571c6294435be409a2f3&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)

# [一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)

[肿瘤异质性分析必备| 一文学会四种scRNA-seq拷贝数变异分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529921&idx=1&sn=93f8ad6655ee6d2b036cd557a6a74be6&scene=21#wechat_redirect>)[分子批量对接与亲和力热图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=1&sn=90de71a3b453e635920d309faedb36c7&scene=21#wechat_redirect>)[代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=1&sn=90de71a3b453e635920d309faedb36c7&scene=21#wechat_redirect>)[单细胞免疫组库测序(scTCR+scBCR)学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>)
![图片](../../images/697dd2eb5e60e8d8.png)解锁前需阅读：**[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)**![](../../images/399758fa7d6941c2.png)

订阅后解锁下方学习手册链接：

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

请联系[Biomamba_zhushou]获取文件提取码

本推送教程链接：

https://pan.baidu.com/s/1YZAE00XfLzyGtiUyA7cB9w

整个订阅合集的百度云下载地址可见:

https://pan.baidu.com/s/1yXzQi0zBqh4ZLR6Hznckiw?

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)
