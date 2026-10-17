---
title: "sc联合bulk RNA-Seq揭示预测免疫治疗反应的泛癌干细胞特征"
date: 2026-01-03
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533717&idx=1&sn=655c7290a42905cee5346fc3c5025496&chksm=9b3c3dc5ac4bb4d37332c6f9bcd8f80154283f678ead02aaa9f8709d7aac344a1f7195587e4a#rd
albums: ["文献速递"]
---

# sc联合bulk RNA-Seq揭示预测免疫治疗反应的泛癌干细胞特征

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533717&idx=1&sn=655c7290a42905cee5346fc3c5025496&chksm=9b3c3dc5ac4bb4d37332c6f9bcd8f80154283f678ead02aaa9f8709d7aac344a1f7195587e4a#rd
> 合集：文献速递

**
**

* * *

**一、写在前面**

**文章** Integrated analysis of single-cell and bulk RNA sequencing data reveals a pan-cancer stemness signature predicting immunotherapy response**（IF= 10.4）**发布于2022年**《 Genome Med》期刊。**

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprOB1QLibT97V1pursWjwXSFRu50iapAaNWBzVBk3sYnNj7TwTdymxiaicshhsiarA2twoTaNzdqr9iae0pA/640?wx_fmt=png&from=appmsg)
这篇文章我们关注一下方法部分，特别是 Stem.Sig 构建的逻辑和流程。这篇文章构建了干性特征并打分的方法，那我们是不是可以去用其他算法去打分呢？比如[细胞衰老](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247525650&idx=8&sn=9bf5f11fd891caf2caafe41c0d48e688&scene=21#wechat_redirect>)、[T 细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=7&sn=801a250297aa2871f840a57e23ca4b86&scene=21#wechat_redirect>)状态、[通路](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504403&idx=7&sn=99c35dd1d7cf7ad20adf0898fa916c73&scene=21#wechat_redirect>)打分、或者其他自定义打分呢？这可为ICI生物标志物的挖掘提供更多维度的思路。

免疫检查点抑制剂 (ICI) 开创了癌症治疗的新时代，为患者带来了前所未有的临床益处。然而，只有相对较少的患者对其有反应，这凸显了生物标志物研究的必要性，以优化患者选择和联合策略，以应对免疫耐药性。

传统的生物标志物研究主要集中于对完整肿瘤组织的全外显子组测序 (WES) 或 RNA 测序 (RNA-Seq) 进行分析，这些分析仅反映了大量不同细胞的平均遗传图谱。从这些研究中得出的现有 ICI 生物标志物显示出有限的预测值。[单细胞 RNA 测序 (scRNA-Seq)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>) 的发展使我们能够以单细胞分辨率剖析基因表达，并识别出具有更好性能的新型生物标志物。

[癌症干细胞 (CSC)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522233&idx=1&sn=287a380de741ff55f0ce78dc9c727985&scene=21#wechat_redirect>) 是一种自我更新细胞，可促进[肿瘤](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529921&idx=1&sn=93f8ad6655ee6d2b036cd557a6a74be6&scene=21#wechat_redirect>)发生、发展和转移。越来越多的证据表明，干细胞特性与癌症免疫逃避和抵抗之间存在显著关联。先前的一项研究表明，在 21 种实体癌类型中，高干细胞特性与免疫细胞排斥相关，但缺乏直接的临床证据来验证干细胞特性与 ICI 结果之间的负相关性。

DOI: 10.1186/s13073-022-01050-w

数据：https://doi.org/10.6084/m9.figshare.17654633

代码：https://doi.org/10.6084/m9.figshare.17654633

如果需要[数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)**指导** 、生信热点**[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)** 、自测/数据库数据**个性化分析** 辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[**Biomamba_zhushou**]。

**二、主要内容**

**一、癌症干细胞与ICI耐药性相关**

![13073_2022_1050_Fig1_HTML](https://mmbiz.qpic.cn/mmbiz_jpg/GQbSTiaXLprNg4jFrETSAuHf7cJWN8tUTvQbodlcGPsYy0MjicjjpaCUqMT6aMgAibCfnjljeAsQoP43CralX7EGA/640?wx_fmt=other&from=appmsg)

A 、C SKCM 或 BCC 恶性细胞的 tSNE 图。顶部 [tSNE 图](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508520&idx=1&sn=5964c7ac7cfad903cbc43794b3129a67&scene=21#wechat_redirect>)描绘了 CytoTRACE 评分在恶性细胞中的分布。深绿色表示分数较低 (低干性)，而深红色表示分数较高 (高干性)

B 、D SKCM队列中按反应表型 (NR vs. TN) 或 BCC 队列中按反应表型 (NR vs. R) 的 CytoTRACE 评分的雨云图

结论性结果：干性高的癌细胞在 NR 亚组中富集，癌细胞干性与 ICI 之间的存在负关联。

二、通过泛癌症scRNA分析开发Stem.Sig

![13073_2022_1050_Fig2_HTML](https://mmbiz.qpic.cn/mmbiz_jpg/GQbSTiaXLprOB1QLibT97V1pursWjwXSFRMSdI08SGgAGAGv9t8rXPXbDeOFzFuJUN5qolD4IEMx9PhEVfQmdO3Q/640?wx_fmt=other&from=appmsg)

A、 Circos 图描绘了 Stem.Sig 的发展

B、 Stem.Sig 中基因的通路富集分析

结论性结果：我们研究了 Stem.Sig 中过度表达的生物学功能，主要包括涉及缺氧、[糖酵解](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529679&idx=1&sn=f1348e4b4fe5658740e5786a012c4caa&scene=21#wechat_redirect>)、泛素化、EPH-ephrin 信号传导、WNT 信号传导和核苷酸切除修复 (NER) 的过程。

三、使用泛癌症TCGA队列分析Stem.Sig与免疫抑制之间的潜在联系

![13073_2022_1050_Fig3_HTML-1](https://mmbiz.qpic.cn/mmbiz_jpg/GQbSTiaXLprOB1QLibT97V1pursWjwXSFR8PibkiczaTREOYnlneDkMfw5ArgWpcyzesx8QicwEtxdrTCALOPmREEmw/640?wx_fmt=other&from=appmsg)

A、 Circos 图描绘了 Stem.Sig 与多种癌症类型中免疫相关基因表达水平之间的相关性。从 circos 图的内部到外部，带有黑色箭头的纵轴表示不同的癌症类型，由图 B 的 y 轴注释

B 、热图描绘了 Stem.Sig 与多种癌症类型中免疫细胞浸润之间的相关性

C、 热图描绘了 Stem.Sig 与 Top 10 Hallmark 通路之间的相关性

D、 每种癌症类型的中位 Stem.Sig 与中位 TMB 的相关性

E 、每种癌症类型的中位 Stem.Sig 与中位 ITH 的相关性

结论性结果：Stem.Sig 与抗肿瘤免疫呈负相关。无论 TMB 水平如何，低 Stem.Sig 的肿瘤表现出明显优于高 Stem.Sig 的肿瘤的抗肿瘤免疫力。

四、通过Stem.Sig预测免疫治疗结果

![13073_2022_1050_Fig4_HTML](https://mmbiz.qpic.cn/mmbiz_jpg/GQbSTiaXLprOB1QLibT97V1pursWjwXSFRErdym5tYlc3oPvlGNXXZnAUOiagIR2laTREPDtTn83Uh6x9UGZJVK5A/640?wx_fmt=other&from=appmsg)

A 、使用[机器学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&scene=21#wechat_redirect>)过程构建的 Stem.Sig 模型的训练、验证和测试流程图

B 、多个 ROC 图比较，描绘了验证集中不同机器学习算法的性能

C 、ROC 图描绘了验证和测试队列中最终 Stem.Sig 模型的性能

D 、Kaplan-Meier 曲线比较验证和测试集中高风险和低风险患者的 OS

五、Stem.Sig与其他预测基因特征比较

![13073_2022_1050_Fig5_HTML](https://mmbiz.qpic.cn/mmbiz_jpg/GQbSTiaXLprOB1QLibT97V1pursWjwXSFRTcE7IVoBOicAS8EgMHAledaxUUuAgg75FW4demCHZtL1aiciaQHpsJG0A/640?wx_fmt=other&from=appmsg)

A、 Circos 图描绘了测试集中泛癌症特征的表现

B、 热图比较了 Stem.Sig 与其他泛癌症特征的预测值。不同特征行按其在测试集中的 AUC 排序。从上到下，Stem.Sig 排名第一，而 Cytotoxic.Sig 排名最后

C、 条形图描绘了 SKCM 队列中 Stem.Sig 和其他黑色素瘤特异性特征的 AUC 值

六、利用CRISPR筛选数据探索Stem.Sig中的潜在治疗靶点

![13073_2022_1050_Fig6_HTML](https://mmbiz.qpic.cn/mmbiz_jpg/GQbSTiaXLprOB1QLibT97V1pursWjwXSFRibms9Ij9MXibkEd9X231AJfKzdao1S7KucNxiczWMZxwNM5gHIWOIygBg/640?wx_fmt=other&from=appmsg)

A 、根据基因敲除对抗肿瘤免疫的影响对 17 个 CRISPR 数据集的基因排名。负 (正) z 分数表示敲除特定基因后免疫反应更好 (更差)。基因根据其平均z分数进行排序。排名靠前的基因与免疫抗性相关。热图中的空白方块表示相应队列中基因数据的缺失值

B 、雷达图比较了 Stem.Sig 和其他预测特征中排名靠前的基因的百分比

C 、热图描绘了不同 CRISPR 数据集中排名靠前的 3% 基因中 20 个 Stem.Sig 基因的 z 分数

结论性结果：Stem.Sig 中排名前 3% 的基因有 20 个，这些与干细胞相关的基因的免疫抗性特性可能与 ICB 协同作为潜在的治疗靶点。

**三、结论与方法**

1.结论

我们提供了第一个确凿的临床证据，表明癌症干细胞特性与免疫疗法耐药性有关。通过对[单细胞转录组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)数据进行全癌分析，我们开发了一种[基因表达](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)特征 Stem.Sig，它在预测多个队列的 ICI 结果方面优于其他已建立的特征。对 Stem.Sig 的进一步探索还揭示了一些潜在的治疗靶点。我们的研究为免疫疗法中的患者选择提供了一种有希望的解决方案，并揭示了通过靶向[癌症干细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522233&idx=1&sn=287a380de741ff55f0ce78dc9c727985&scene=21#wechat_redirect>)特性来增强抗肿瘤免疫力来解决 ICI 耐药性的方法。

2.方法

①Stem.Sig 开发策略：

我们对泛癌症 scRNA数据集中恶性细胞的基因表达水平和 CytoTRACE 评分进行了 Spearman 相关性分析。

与 CytoTRACE 评分正相关的基因 (Spearman R > 0 和 FDR < 1e-05) 被视为 Gx。

在恶性细胞中差异上调的基因被视为 Gy。

为了获得与干性正相关的上调肿瘤特异性基因，将 Gx 和 Gy 相交以产生每个数据集的 Gn。

例如，G1 由来自第一个 [scRNA-Seq 数据](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)集中 Gx 和 Gy 交集的基因组成。计算了 G1–G34 中每个基因的 Spearman R 几何平均值。

最后，将 Spearman R 几何平均值 > 0.4 (中度至强相关性) 的基因汇总为 Stem.Sig。

②[scRNA-Seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>) ICI 队列

③泛癌症 scRNA-Seq 数据集 - TISCH

④泛癌症[转录组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507210&idx=1&sn=f32037ffefd60b0d1bcca7bf9c3e0823&scene=21#wechat_redirect>)数据 - UCSC Xena

⑤ICI RNA-Seq 队列

⑥CRISPR/Cas9 筛选研究的数据队列

⑦scRNA-Seq 数据分析-CytoTRACE

⑧免疫相关基因集、MCP-counter

⑨ComBat 方法消除不同 ICI RNA-Seq 队列的批次效应

⑩[机器学习 ](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&scene=21#wechat_redirect>)(ML) 算法，包括支持向量机 (SVM)、朴素贝叶斯 (NB)、随机森林 (RF)、k 最近邻 (KNN)、AdaBoost 分类树 (AdaBoost)、增强逻辑回归 (LogiBoost) 和 cancerclass

⑪ICI 反应特征

六种泛癌症特征 (INFG.Sig、T.cell.inflamed.Sig、PDL1.Sig、LRRC15.CAF.Sig、NLRP3.Sig 和 Cytotoxic.Sig)

七种黑色素瘤特异性特征 (CRMA.Sig、IMPRES.Sig、IPRES.Sig、TcellExc.Sig、ImmmunCells.Sig、IMS.Sig 和 TRS.Sig)

⑫AUC 为 0.9–1.0 被认为是优秀的，0.8–0.9 非常好，0.7–0.8 好，0.6–0.7 足够，0.5–0.6 差，小于 0.5 被认为没有用。

**四、引用**

Zhang Z, Wang ZX, Chen YX, et al. Integrated analysis of single-cell and bulk RNA sequencing data reveals a pan-cancer stemness signature predicting immunotherapy response. Genome Med. 2022;14(1):45. Published 2022 Apr 29.

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=24)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=25)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=26) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=28) 您点的每个赞和在看，我都认真当成了喜欢
