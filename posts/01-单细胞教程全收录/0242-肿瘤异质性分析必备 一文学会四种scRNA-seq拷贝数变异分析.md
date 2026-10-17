---
title: "肿瘤异质性分析必备| 一文学会四种scRNA-seq拷贝数变异分析"
date: 2025-08-14
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530392&idx=2&sn=d894648d098f6964f5ab5a617df50563&chksm=9b3c0ec8ac4b87de34b0a1aed105c28fe263f1885c6be3b5dd626efcb87c43d3a0a5605a01c4#rd
albums: ["单细胞教程全收录"]
---

# 肿瘤异质性分析必备| 一文学会四种scRNA-seq拷贝数变异分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530392&idx=2&sn=d894648d098f6964f5ab5a617df50563&chksm=9b3c0ec8ac4b87de34b0a1aed105c28fe263f1885c6be3b5dd626efcb87c43d3a0a5605a01c4#rd
> 合集：单细胞教程全收录

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

scRNA-seq拷贝数变异分析

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)**拷贝数变异（Copy number alterations，以下简称CNA；infercnv包也习惯描述为 Copy Number Variation，CNV）是一种重要的基因组变异，在癌症的发生和发展过程中起着至关重要的作用。确定肿瘤细胞中CNA的特征对早期肿瘤检测、划分肿瘤异质性、了解肿瘤进展模式和揭示耐药机制具有重要意义。随着单细胞RNA测序（scRNA-seq）的蓬勃发展，研究人员开发出了多种计算方法来从scRNA-seq研究中推断CNA。目前从scRNA-seq数据中推断CNA的计算方法大致可分为两类。一类是基于表达的，即直接从基因表达推断CNA。这类工具包括inferCNV、copykat和SCEVAN。这些工具的工作原理是，CNA扩增（AMPs）或缺失（DELs）将分别导致受影响基因组区域内基因的上调或下调。InferCNV利用基因窗口的校正移动平均数；copykat采用综合贝叶斯分割方法；SCEVAN采用多通道分割算法。第二类将基因表达与等位基因信息相结合，相关工具有Numbat和CaSpER等。**自学有困难的同学不妨看看：[scRNA-seq，从小白到文献复现大神！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)**更多生信教程可见：[生信基地终身订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)**
本教程基于Linux中的Rstudio环境演示，计算资源不足的同学可参考：[选择西柚云的11个理由](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529471&idx=2&sn=c191f2df999820bf7f1f96832d120d2d&scene=21#wechat_redirect>)
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21#wechat_redirect>)

本教程可视化集锦![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwy0hBvqfSTsLLNTrk36j0ggAovnSdYd3E7DgicdibY4TzgNPOic6FLLAStxjJHTQsiciaZ3QCZtY90pLw/640?wx_fmt=jpeg&from=appmsg) **-Biomamba**
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

所见即所得

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpwy0hBvqfSTsLLNTrk36j0gC12BcO8p0qflUJeZjYG84FgegiaVgSmAdLRYHXGzmL2MpsTc6KwAJbA/640?wx_fmt=gif&from=appmsg)

‍

**教程目录** ：

**一、写在前面**

**二、可视化集锦**

**三、绪论**

**3.1 定义**

**3.2 主要研究成果**

**（1）区分肿瘤细胞与正常细胞**

**（2） 推断的拷贝数变异（CNA）谱的准确性**

**（3） 亚克隆结构推断准确性的评估**

（4）计算效率

**3.3 小结**

**四、infercnv**

4.1 简介

4.2 安装

4.3 输入文件

4.4 infercnv workflow

4.5 infercnv实战

（1）数据概况

（2）infercnv流程

（3）热图优化

（4）小提琴图

****五、copykat****

5.1 copykat介绍

（1）简介

（2）copykat工作流程描述

（3）性能评估

（4）实体肿瘤中肿瘤细胞和正常细胞的分类

（5）应用于其他scRNA-seq技术

（6）推断乳腺肿瘤的克隆亚结构

（7）小结

5.2 copykat流程（1）安装（2）counts矩阵预处理（3）常用参数（4）copykat（5）整理数据（6）绘制热图5.3 copykat实战（1）数据概况（2）copykat（3）整理数据（4）热图绘制（5）探究一下拷贝数变异与原来亚群之间的关系（6）CNA score小提琴图

**六****、SCEVAN******

****6.1 安装R包****

****6.2 加载R包********6.3 单样本分析********（1）加载数据********（2）执行分析********（3）结果查看********6.4 多样本分析********（1）加载数据 （2）执行分析（3）结果查看********6.5 联合Seurat对象********（1）创建****Seurat对象**** （2）将拷贝数变异结果加入****Seurat对象**** （3）降维分群（4）可视化****

****七****、numbat********

********7.1****安装R包************

****7.2****加载R包************7.3 数据下载********7.4 等位基因数据准备********（1）运行参数解释 （2）示例脚本（3）可能出现的报错（4）执行分析********7.5 运行numbat********（1）运行参数解释********（2）运行****numbat************7.6 结果解读********（1）拷贝数景观和单细胞系统发育 （2）在系统发育上完善亚克隆（3）共识拷贝数区段（4）pseudobulks水平拷贝数变异（5）进化树********八、环境版本信息********
********九、参考********十、单细胞教程全收录********十一、欢迎致谢****

文末下载链接中包含以下内容：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwsZLxicFFC4gUXuoBfB0icOB1sWmh7riaudYqCbTADNMkJUoHXmDDWlFdxibWQWY1knm36ictcAiawKvfQ/640?wx_fmt=png&from=appmsg)

测试文件约**55.57GB** ，大家注意按需下载！

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)**
****解锁前需阅 读：**[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)****![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

订阅后获取下方学习手册链接：

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

请联系[Biomamba_zhushou]获取文件提取码

本推送教程二维码：

https://pan.baidu.com/s/1wGR2oZT3bw7wkbOdUI6hnA?

整个订阅合集的百度云下载地址可见:

https://pan.baidu.com/s/1yXzQi0zBqh4ZLR6Hznckiw?

**-Biomamba**
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
