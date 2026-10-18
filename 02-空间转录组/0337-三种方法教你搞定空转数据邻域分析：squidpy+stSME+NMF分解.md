---
title: "三种方法教你搞定空转数据邻域分析：squidpy+stSME+NMF分解"
date: 2026-06-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538803&idx=2&sn=54db98682dcff3feb04a5623c37546ce&chksm=9b3c2123ac4ba835ea136c12212da54b0bf9147192926e16b6027dfc1735e56a0c21aaf8d130#rd
albums: ["空间转录组"]
---

# 三种方法教你搞定空转数据邻域分析：squidpy+stSME+NMF分解

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538803&idx=2&sn=54db98682dcff3feb04a5623c37546ce&chksm=9b3c2123ac4ba835ea136c12212da54b0bf9147192926e16b6027dfc1735e56a0c21aaf8d130#rd
> 合集：空间转录组

![](../../images/399758fa7d6941c2.png)

空间转录组数据邻域分析手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)邻域分析是基于空间位置的细胞/spot邻域划分与表达谱分析，具有从“单细胞”到“细胞群落”的表型解析，揭示群体功能的核心价值，以及阐明细胞间通讯、微环境异质性、结构-功能关联的生物学意义，为肿瘤微环境解析、组织发育机制等研究提供空间维度证据。与传统分析相比，邻域分析可以将空间位置权重纳入基因表达解读，突破纯表达谱分析的局限。工具简介：

1、[squidpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505844&idx=2&sn=5756c0702d080d6e602c504e7d461013&scene=21#wechat_redirect>)的邻域分析的核心目标是在Visium空间转录组分析中，Spot的基因表达数据提供了分子信息，而高分辨率组织图像则提供了细胞形态和组织结构的视觉信息。我们可以从组织图像中计算每个Visium spot(Spot)的图像特征。这些特征将作为一个obs × 特征矩阵，与obs×基因表达矩阵一起存储在[AnnData](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528513&idx=1&sn=1ff1b8bee321f8f5bcac425ce96dc6ff&scene=21#wechat_redirect>)对象中，用于下游的联合分析。

2、stSME是通过spot图像的相似性来调整基因表达，使相似的组织区域在表达上更一致。

3、NMF分解是一种降维技术，它将一个输入矩阵V分解为两个非负矩阵W矩阵（Spot×成分）和H矩阵（成分×细胞类型）。具有识别共现模式、处理混合信号、跨区域共享信息和简化可视化的优势与生物学意义。

本教程基于Python完成，没有基础的小伙伴可见[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&scene=21#wechat_redirect>)，自学有困难的小伙伴可见：[Python实战-玩转空间转录组分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533721&idx=1&sn=9648ed4701224e5d2e4c704d7046d9de&scene=21#wechat_redirect>)
本教程基于Linux中的[Jupyter](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531443&idx=3&sn=0930f54959a9bd13b99780d8f26a1155&scene=21#wechat_redirect>)环境演示，计算资源不足的同学可参考：
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[配置一个心仪的工作站(硬件+环境配置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519707&idx=1&sn=73dcab26f9b2ed75a954327317d07112&chksm=9b3cf48bac4b7d9df5b5a432fbe70d4f9c13bc8d739aa401732614f022223d1912642a7e4bea&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)

本教程**复现集锦** ：

![](../../images/470bac0700dfe587.webp) **-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

Squidpy学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：‍

![](../../images/bae7212fa177e3b2.gif)

**教程目录** ：

**一、写在前面**

**二、 邻域分析**

**2.1 空间转录组图像特征提取：结合形态与分子信息**

**2.2 图像特征的价值：互补与融合**

**2.3 应用**

**三、 代码实操**

**3.1 加载所需库**

**3.2 读取数据**

**3.3 计算不同尺度的特征**

**3.4 数据聚合**

**3.5 数据基础分析**

**3.6 可视化聚类信息**

**3.7 邻域富集**

**（1）空间邻域富集分析：识别组织中 Spot 簇的共现模式**

（2）分析步骤

（3）配体 - 受体相互作用分析

环境信息

****空间转录组教程全收录****

********欢迎致谢********

文末下载链接中包含的内容：

![](../../images/a3d9c664db47c9a7.webp)

测试文件约**355.71MB** ，大家注意按需下载！

stSME聚类方法学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：

![](../../images/24ee50b1245d7bab.gif)

**教程目录** ：

**一、写在前面**

**二、SME 算法**

**2.1 背景**

**2.2 方法原理（SME = Spatial Morphology Expression）**

**（1）提取形态学特征**

**（2）计算形态学相似性**

**（3）基因表达调整（Morphological normalization）**

**（4）形态调整后的基因表达矩阵 (Morph)**

**2.3 特点与优势**

**三、代码实操**

**3.1 例1：小鼠大脑（冠状面）**

**（1）数据预处理**

**（2）运行stSME聚类**

**3.2 例2：小鼠大脑 (后矢状面)**

（1）数据预处理

（2）**运行stSME聚类**

**环境信息**

****空间转录组教程全收录****

********欢迎致谢********

********文末下载链接中包含的内容********

![](../../images/3450d418532683e4.webp)

******测试文件约 909.84MB，大家注意按需下载！ ******

******
******

******NMF分解学习手册 以html文件格式提供，可在浏览器中打开并翻阅学习：‍******

![](../../images/ebc1a4458ef7fc0c.gif)

******
******

********教程目录** ：******

******一、写在前面******

******二、非负矩阵分解 (NMF) 识别细胞区室 / 组织区域******

******三、代码实操******

******3.1 导入数据和库******

******3.2 使用Cell2location进行空间共定位******

******3.3 输出共定位结果******

******3.4 可视化共定位热图******

******环境信息******

******空间转录组教程全收录******

******欢迎致谢******

******文末下载链接中包含的内容******

![](../../images/6f3c44cf92532501.webp)

******测试文件约 8.54GB，大家注意按需下载！ ******

![](../../images/7d247e6c6ef19f87.png)

![图片](../../images/eab31beb8c0e41d2.png)

往期订阅

![图片](../../images/8b04fd62fd8f3d51.png)![图片](../../images/4064a50c19e8ad22.png)

生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[那就开放一个终身订阅吧~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)

2025已完结，内容如下：

[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)[《Cell》复现|中性粒细胞scRNA-seq图谱阐明抗肿瘤抗原呈递效力](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526776&idx=1&sn=99eb6a16c7bf345445b6ff4b61110138&scene=21#wechat_redirect>)

[代码复现|scRNA-seq绘制透明细胞肾癌的免疫微环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527498&idx=1&sn=c8282e9d4175bfb2e572278312073d81&scene=21#wechat_redirect>)

[改造单细胞DoHeatmap](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527762&idx=1&sn=ba7c8a4cb704e71fa86ebfe1f19bffea&scene=21#wechat_redirect>)

[Slingshot拟时序分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527850&idx=1&sn=f4e2ca5e2e5e71eeaf132375bb8270eb&scene=21#wechat_redirect>)

[《Cancer Cell》|时空单细胞揭示CRC的PD-1治疗免疫细胞动态](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528056&idx=1&sn=73c0da3ff7ff50bafbb9315fd5b60f15&scene=21#wechat_redirect>)

[scRNA-seq数据基础分析手册(2025最新修订)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)

[代码复现|吞噬作用增强肿瘤中巨噬细胞的氧化代谢和免疫抑制特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528289&idx=1&sn=b56f00f3d8a4b152e54f3acd40aef21d&scene=21#wechat_redirect>)[一文学会scRNA Velocity剪切速率分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528458&idx=1&sn=900357283922571c6294435be409a2f3&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)

# [一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq拷贝数变异分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529921&idx=1&sn=93f8ad6655ee6d2b036cd557a6a74be6&scene=21#wechat_redirect>)

# [分子批量对接与亲和力热图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=1&sn=90de71a3b453e635920d309faedb36c7&scene=21#wechat_redirect>)

# [代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&scene=21#wechat_redirect>)

# [单细胞免疫组库测序(scTCR+scBCR)学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>)[一文掌握WGBS分析流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531339&idx=1&sn=83d6e80e24494cc7080188d5c9e695e2&scene=21#wechat_redirect>)

# [《NC》代码复现|snATAC联合scRNA-seq揭示小鼠肾脏细胞分化程序与疾病靶点](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531908&idx=1&sn=2f094e390621a57853ba17f59f298ebe&scene=21#wechat_redirect>)

# [空间转录组数据基础分析手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532178&idx=1&sn=2cc8f5453765bd68b8ddacf2c2e3d5e7&scene=21#wechat_redirect>)

# [空间转录组|多样本整合分析手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532349&idx=1&sn=59c0f14043906ff50c56dea3b16e9200&scene=21#wechat_redirect>)

[一文学会三种空转数据共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=1&sn=cd16d0151ef19c9a2dcfcba6ee09f431&scene=21#wechat_redirect>)[一文搞定空转数据反卷积分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532458&idx=1&sn=f8ec547187374fe77c38fc1125709b3b&scene=21#wechat_redirect>)[三种方法教你搞定空转数据邻域分析：squidpy+stSME+NMF分解](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532641&idx=1&sn=c8422ab7c1cd70751fb3109a84cb64ea&chksm=9b3c3931ac4bb0275fe5fd89712535cce677a308ac5a2c4e85d6f2a8785a4c76359e6612553c&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)[空转细胞通讯分析学习手册：CellPhoneDB+Commot+stLearn](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532763&idx=1&sn=f6e4df9242f1341d2dc7e6154c33aa46&chksm=9b3c398bac4bb09d978dddd3f44c04c855ec89f6cd949fccbe497c515a62440f58dca31b4885&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)[空间转录组轨迹分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532806&idx=1&sn=7d7ecf4977cb2cc9ace0e4e31941a1ac&chksm=9b3c3856ac4bb140a5f0955158656f458951cfe9bdd0a68d8c8ff74bd1e3f7adcc4da76197f0&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)[空间转录组数据拷贝数变异分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532924&idx=1&sn=46b87151e30163e393cf2c1751360bac&chksm=9b3c382cac4bb13ad9aecd8783f1c6b0c576b1a25d04c3d15fa95a7e4fd5fdd8090cba7ce027&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)[《Nature Genetics》文献复写 | 结直肠癌免疫细胞的高清空转分析（Visium HD+Xenium）](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533068&idx=1&sn=52cbc8d161ec216b5d7a8238a49d47c6&chksm=9b3c3b5cac4bb24a1b5c8ee1304f896c2ccea583e81bda4f9fae26564bc7d77c09a58baef3de&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)[2025订阅资料已完结，请留下你的评价！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534421&idx=1&sn=2c80be7809a97981bab3f76fae55ac20&scene=21#wechat_redirect>)![图片](../../images/697dd2eb5e60e8d8.png)
更多订阅请阅读：**[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)**![图片](../../images/eab31beb8c0e41d2.png)

学习手册下载链接：

![图片](../../images/8b04fd62fd8f3d51.png)![](../../images/007e970626afa0b7.png)

链接:https://pan.baidu.com/s/1v_4WQmqqcu7m9BGJ-0z6Gg

提取码请联系客服微信获取：

![](../../images/fe8ecb8594a1f419.webp)![](../../images/7d247e6c6ef19f87.png)
