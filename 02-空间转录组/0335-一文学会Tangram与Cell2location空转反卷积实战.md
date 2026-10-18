---
title: "一文学会Tangram与Cell2location空转反卷积实战"
date: 2026-02-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534882&idx=2&sn=787ff8d8548c512dd64f5e5f131d176f&chksm=9b3c3072ac4bb964af9813b995ee3d63f265ba3ee57ec3b8e0ecc219f1993e77016d44a3dea4#rd
albums: ["空间转录组"]
---

# 一文学会Tangram与Cell2location空转反卷积实战

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534882&idx=2&sn=787ff8d8548c512dd64f5e5f131d176f&chksm=9b3c3072ac4bb964af9813b995ee3d63f265ba3ee57ec3b8e0ecc219f1993e77016d44a3dea4#rd
> 合集：空间转录组

![](../../images/399758fa7d6941c2.png)

空间转录组数据去卷积分析手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)由于主流的空间转录组并不能以真正的单细胞为分辨率检测细胞数据，因此需要通过空间转录组反卷积分析解析每个spot中细胞类型组成比例的过程，该分析的原理是基于单细胞参考数据集构建线性/概率模型，实现混合信号拆解，进而达到从混合表达信号中推断细胞类型空间分布模式的目的。工具简介：

1、[Tangram](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521196&idx=1&sn=f77395164cd2e2568daa2aae811b8861&scene=21#wechat_redirect>)是一种强大的深度学习工具，专门用于将[单细胞RNA测序](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)(scRNA-seq) 数据与[空间转录组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532178&idx=2&sn=45a5f43b44ae5eb3346bb67238caea5d&scene=21#wechat_redirect>)(ST)数据进行整合和对齐，实现细胞类型组成的反卷积（Deconvolution）。其核心目的是解决低分辨率空间技术（如Visium）中Spot信号混合的问题。

2、[Cell2location](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529485&idx=1&sn=4002de7cb87732889b144fbe85d92c9e&scene=21#wechat_redirect>)是一种基于贝叶斯模型（Bayesian Model）的计算方法，专门为空间转录组（Spatial Transcriptomics,ST）数据设计。解决空间转录组数据中Spot信号混合的问题。[Cell2location](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529485&idx=1&sn=4002de7cb87732889b144fbe85d92c9e&scene=21#wechat_redirect>)将每个Spot的总mRNA计数分解为构成该Spot的各种细胞类型的丰度（即，推断每个Spot中包含多少个某种特定类型的细胞）。

本教程基于Python完成，没有基础的小伙伴可见[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&scene=21#wechat_redirect>)，自学有困难的小伙伴可见：[Python实战-玩转空间转录组分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531284&idx=1&sn=cc785f60e85a3caa8117792de60e1393&scene=21#wechat_redirect>)本教程基于Linux中的[Jupyter](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531443&idx=3&sn=0930f54959a9bd13b99780d8f26a1155&scene=21#wechat_redirect>)环境演示，计算资源不足的同学可参考：
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[配置一个心仪的工作站(硬件+环境配置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519707&idx=1&sn=73dcab26f9b2ed75a954327317d07112&chksm=9b3cf48bac4b7d9df5b5a432fbe70d4f9c13bc8d739aa401732614f022223d1912642a7e4bea&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)

本教程**复现集锦** ：

![](../../images/4e4ab971b7ef2833.webp) **-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

tangram学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：‍

![](../../images/0a0902abad18d0dd.gif)

**教程目录** ：

**写在前面**

**一、Tangram介绍**

**1.1 Tangram：基于最优传输理论的空间反卷积方法**

**1.2 核心原理**

**1.3 工作流程**

**二、 代码实操 Ⅰ：Slide-seq**

**2.1 软件和数据准备**

**（1）GPU准备**

**（2）下载数据**

**2.2 加载空间数据**

**2.3 加载单细胞数据**

**2.4 准备映射**

**2.5映射**

**2.6下游分析**

****三、代码实操Ⅱ：10x Visium****

****3.1 软件和数据准备****

3.2 加载空间转录组和单细胞参考数据

3.3 预处理

3.4 数据对齐

3.5 映射结果检查

3.6 通过对齐单细胞数据获得新的空间数据

3.7 精确反卷积

3.8 通过比对单细胞数据进行反卷积

环境信息

****空间转录组教程全收录****

********欢迎致谢********

文末下载链接中包含的内容：

![](../../images/98a934dfd1538df6.jpg)

测试文件约**8.35GB** ，大家注意按需下载！

cell2location学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：

![](../../images/030e31c0d796f86f.gif)

**教程目录** ：

**一、写在前面**

**二、Cell2location：空间转录组数据细胞类型解卷积工具**

**2.1 Cell2location简介与核心目标**

**2.2 Cell2location的工作流程与技术原理**

**2.3**Cell2location的主要优势****

**2.4 结果可视化**

**三、代码实操**

**3.1 加载安装的库**

**3.2 加载单细胞转录组参考数据**

**3.3 数据质控**

**3.4 获取参考数据集**

**3.5 参考数据集质控**

3.6 参考细胞类型特征估计（Estimation of reference cell type signatures）------NB回归

3.7 模型训练（GPU可加速）

3.8 检查QC质量图表

3.9 加载训练好的 scRNA-seq 参考数据和回归模型

3.10 进行空间映射

3.11 可视化细胞类型丰度

3.12 下游分析

（1）通过聚类来区分不同组织区域

（2）非负矩阵分解 (NMF) 识别细胞区室 / 组织区域

（3）估计空间数据中每个基因的细胞类型特异性表达

**环境信息**

****空间转录组教程全收录****

********欢迎致谢********

文末下载链接中包含的内容

![](../../images/f95aa47a2351222e.jpg)

测试文件约**6.76GB** ，大家注意按需下载！

![](../../images/7d247e6c6ef19f87.png)

![图片](../../images/eab31beb8c0e41d2.png)

往期订阅

![图片](../../images/8b04fd62fd8f3d51.png)![图片](../../images/4064a50c19e8ad22.png)

生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[那就开放一个终身订阅吧~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)

2025已更新订阅内容：

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

[一文学会三种空转数据共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=1&sn=cd16d0151ef19c9a2dcfcba6ee09f431&scene=21#wechat_redirect>)![图片](../../images/697dd2eb5e60e8d8.png)
解锁前需阅读：**[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)**![](../../images/399758fa7d6941c2.png)

学习手册下载链接：

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

领取提取码请联系客服微信[Biomamba_zhushou]

本推送教程二维码：

https://pan.baidu.com/s/1j1xTPvFgLtTjjjO9z5s10g

整个订阅合集的百度云下载地址可见:

https://pan.baidu.com/s/1_Pjd4RjinDCWmwVtSfStFA

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/e43581b4f5118aad.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
