---
title: "Ai驱动结合蛋白设计：Bindcraft全流程教学"
date: 2026-06-30
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538886&idx=3&sn=6945c1ad968781b1b17a3a327287da56&chksm=9b3c2196ac4ba8803d6e10d505a96bd837956045d0a282198cc50e10e8bb6ded359426c11a75#rd
albums: ["AIDD & CADD"]
---

# Ai驱动结合蛋白设计：Bindcraft全流程教学

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538886&idx=3&sn=6945c1ad968781b1b17a3a327287da56&chksm=9b3c2196ac4ba8803d6e10d505a96bd837956045d0a282198cc50e10e8bb6ded359426c11a75#rd
> 合集：AIDD & CADD

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Bindcraft：用户友好的binder从头设计流程

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)蛋白质主要依赖蛋白质-蛋白质相互作用（PPI）来执行复杂的生物学功能。因此，设计能够特异性靶向PPI的蛋白质结合剂具有极高的治疗与生物技术价值。然而，传统的实验方法以及早期基于物理的计算工具（如 Rosetta）往往费时费力、成功率较低（低于0.1%），且依赖于海量的结构采样。近年来，结合[RFdiffusion和ProteinMPNN](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)的[深度学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507794&idx=1&sn=c70dd03a962adb3f3b92ffed47e978bb&scene=21#wechat_redirect>)方法大幅提升了设计的成功率，但仍存在一定的局限性：还是需要一定程度的高通量实验支持，且软件操作较为繁琐，要求用户具备一定的Linux系统使用经验。为此，洛桑联邦理工学院（EPFL）的团队开发了一款高度自动化的蛋白设计软件BindCraft（Nature 2025）。该软件利用AlphaFold2网络的反向传播机制 ，能够针对极具挑战性的治疗靶点，高效生成并精准识别出高亲和力结合剂。BindCraft不仅显著提升了按需设计结合剂的效率，其高度封装的特性也极大降低了使用门槛，为用户带来了更为便捷的操作体验。
本教程将重点介绍以下内容：Bindcraft的核心原理与设计实例、Bindcraft的安装与部署，Bindcraft的使用方法。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_77@2x.png)此教程还配备[专属镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)，领取该教程之后可免费领取镜像。

往期我们也出了Ai驱动结合蛋白质设计的教程，感兴趣的小伙伴可以点击[正刊都在用的AI驱动蛋白质从头设计流程：RFdiffusion+ProteinMPNN+AlphaFold3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)学习哦~

优惠订阅资料或参与课程请联系客服微信[Biomamba_zhushou]![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)**更多生信教程可见：[为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)**
**-Biomamba**
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png)

Bindcraft核心原理

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![截屏2026-03-11 11.04.14](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwn4xiadS1zCrBguNsaWGHZhFJEjyhBWEZxqvqicBKbeHYDzI1C77zibtmSBKUHlpkmVdWibIpoyyu5L17yKFMB7KZqYqzpoJ0LRNgI/640?wx_fmt=png&from=appmsg)

BindCraft的设计管线可以清晰地分为三个主要阶段：

**第一阶段：基于动态诱导契合的初始结构生成 **流程首先借助**ColabDesign** 框架下的AlphaFold2多聚体模型，通过反向传播机制“幻觉”产出结合剂序列。这一步巧妙在于，它并非在静态骨架上盲目设计，而是每次迭代都会重新预测复合物结构 ，允许靶标和结合剂的主侧链发生适度形变，从而通过动态的**诱导契合** 贴合靶标位点。

**第二阶段：聚焦真实表达率的序列重构** 为了解决**纯粹由AF2生成的蛋白质** 在体外实验中往往**表达量极低** 的问题，流程引入了针对可溶性优化的**MPNNsol** 网络 。在这一阶段，系统会精准锁定并**保护第一步生成的互作界面** 不变，专门对结合剂的核心与表面序列进行重新设计，从而大幅提升目标蛋白在真实环境中的折叠稳定性和表达能力。

**第三阶段：跨模型正交验证与严苛过滤** 最后一步是剔除“假阳性”的质控环节。经过优化的序列会被跨模型送入 AF2 单体模型中进行重新预测，以消除多聚体模型可能带来的评估偏倚。最终，系统会综合 AF2 的置信度得分与经典的 Rosetta 物理能量评分体系 ，精准剔除物理上不合理的设计，输出最终可以直接用于实验筛选的高成功率候选序列。

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png)

所见即所得

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

以html格式提供学习手册，可在浏览器中打开并翻阅学习：‍

![](https://mmbiz.qpic.cn/mmbiz_gif/buxFNhaTGwnJJRBrwYTU5A76u7tCj343GOIowu2pC2smekgRRchAwFkTknMes86QreWPxSI1K9Hoxkias9X62wX8sriaS2yTdSPFD7eFSXpcs/640?wx_fmt=gif&from=appmsg)

Bindcraft全流程教程目录：

一、准备工作

1.1 编程基础

1.2 硬件基础

二、理论基础

2.1 Bindcraft核心原理

2.2 Bindcraft设计实例

2.2.1 靶向细胞表面受体的结合剂

2.2.2 靶向未被探索的结合位点

2.2.3 掩盖至敏表面

2.2.4 AAV重定向用于基因递送

三、安装部署Bindcraft

3.1 常规安装（对网络有要求）

3.1.1 安装驱动和cuda

3.2 改进部署方法

四、Bindcraft的使用方法

4.1 Bindcraft的使用

4.2 Bindcraft的使用

4.2.1 基本设定参数

4.2.2 Bindcraft高级设置参数

4.2.3 Bindcraft过滤参数

文末下载链接中包含以下内容：

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmIfQBGswicJn25eBCBcMF5zX0PsePKdCMSMklMbVIWaJNTTKLlJNQdgsDPqlKXFmpIdxdib89QtOesIPlvW5wLJ6ibfjRMLRyQsY/640?wx_fmt=png&from=appmsg)测试文件，总大小6.66GB![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

往期推送

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Biomamba 生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)

2025年我们零差评完成订阅任务（[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)），2026已更新订阅内容：

[单细胞Figure1的常见图表(Python版)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534718&idx=1&sn=f1492239574ad489be9a1aa0c84af87a&scene=21#wechat_redirect>)

[告别R依赖！一文搞定Python单细胞基础分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534702&idx=1&sn=f1531163f8f620b59cf63dfaa1c03e67&scene=21#wechat_redirect>)

[风靡一时的scTenifoldKnk单细胞虚拟基因敲除,准不准?](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535112&idx=1&sn=95a6b88cd49fb2bbb7aa091a00e09e2c&scene=21#wechat_redirect>)

[scRNA拟时序分析三大Python包： palantir、PAGA、RNAvelocity](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535114&idx=1&sn=95b6364b67d7ae9f03ba8455863ddabe&scene=21#wechat_redirect>)

[正刊都在用的AI驱动蛋白质从头设计流程：RFdiffusion+ProteinMPNN+AlphaFold3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)

[CellphoneDB搞定细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=1&sn=c3eb2d3abad1952b3b7fa88099c607b7&scene=21#wechat_redirect>)

[scRNA-seq肿瘤细胞药物敏感性预测分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536705&idx=1&sn=7fbfeba5dee45f6c3311bd31082a428c&scene=21#wechat_redirect>)

[fastXXX、rapidXXX系列加速你的单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536940&idx=1&sn=57eea9f64dfeff9231977ab5028c3dcd&scene=21#wechat_redirect>)

[转录因子、基因共表达网络分析手册：pySCENIC在脑、黑色素瘤中的应用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537055&idx=1&sn=170371b86b42d47373bf7f0500031f19&scene=21#wechat_redirect>)

[让你的scRNA数据变得更干净~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537531&idx=1&sn=e5f08c08b352287ddfda069a20019afb&scene=21#wechat_redirect>)

[保姆级视频教程| 空间转录组分析手册(基于Seurat)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537631&idx=1&sn=b702b29384fd4f4878cc0b4d0fcf51e7&scene=21#wechat_redirect>)

[拷贝数变异分析的python实现及R语言对比](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537733&idx=1&sn=b938e687d0acf2d906139314e137b903&scene=21#wechat_redirect>)

[Ai驱动结合蛋白设计：Bindcraft全流程教学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537769&idx=1&sn=5dbfe76b35fd2f7593e55bff48c6fa73&scene=21#wechat_redirect>)

**![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwFyPvvyMoyrCDjicmgGcjLom5Yy4JXTXgcSvQIht80m1loPpSwgUPS52jZwKrYqDsXVgSRqwibJYkg/640?wx_fmt=png&from=appmsg)****
**

持续更新中~

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

解锁前需阅读：**[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)**![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

学习手册领取：

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

本推送教程、测试文件下载链接：

https://pan.baidu.com/s/1DBBUnOQRyfD9jbDEwBqf_Q

提取码请联系客服微信获取：

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
