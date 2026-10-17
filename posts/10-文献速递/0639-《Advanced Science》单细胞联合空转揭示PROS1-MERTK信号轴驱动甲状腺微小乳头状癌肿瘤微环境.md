---
title: "《Advanced Science》单细胞联合空转揭示PROS1-MERTK信号轴驱动甲状腺微小乳头状癌肿瘤微环境"
date: 2026-01-31
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534794&idx=1&sn=0ea1a78976f1479f7f157dc818d213a9&chksm=9b3c319aac4bb88c985b17688859a129aefe2074a7ce6b9a41fbe48d193e37c0b20824cec9e1#rd
albums: ["文献速递"]
---

# 《Advanced Science》单细胞联合空转揭示PROS1-MERTK信号轴驱动甲状腺微小乳头状癌肿瘤微环境

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534794&idx=1&sn=0ea1a78976f1479f7f157dc818d213a9&chksm=9b3c319aac4bb88c985b17688859a129aefe2074a7ce6b9a41fbe48d193e37c0b20824cec9e1#rd
> 合集：文献速递

* * *

**一、写在前面**

**文章** PROS1-MERTK Axis Drives Tumor Microenvironment Crosstalk and Progression in Papillary Thyroid Microcarcinoma

文章影响因子: 中国医科大学附属肿瘤医院《Advanced science 》中科院分区(2025版) 1区 IF：14.1

DOI: 10.1002/advs.202413474

链接：https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202413474

本文图片集锦：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyN00o5T0LevX01eJ1e05knk3YpTfWdb2BIIc4biaDv6lFBiaTzsPicfrf8g07PB8ozWySctbfSCxTibg/640?wx_fmt=jpeg&from=appmsg)

近年来，随着高分辨率超声的广泛应用，甲状腺乳头状微癌（Papillary Thyroid Microcarcinoma, PTMC，定义为最大直径≤1cm的PTC）的检出率显著上升，构成了甲状腺癌发病率增长的主要部分。尽管大多数PTMC表现为惰性生长，预后良好，但仍有部分病例会在短期内出现肿瘤增大、淋巴结转移（LNM）和甲状腺外扩展（ETE）等侵袭性行为。这种临床异质性导致了针对PTMC“过度诊断与过度治疗”的反思，并使主动监测（AS）成为低风险PTMC的一种管理策略。然而，如何准确识别出具有进展风险、需要早期干预的PTMC患者，仍是当前临床面临的核心挑战。

肿瘤的发生发展并非仅由癌细胞自身驱动，其所在的肿瘤微环境（TME）扮演着关键角色。TME是一个由恶性细胞、基质细胞（如成纤维细胞、内皮细胞）和免疫细胞共同构成的复杂生态系统。大量证据表明，TME中的细胞间相互作用与PTC的进展密切相关。例如，Kucuk等人的研究发现，肥大细胞、中性粒细胞和浆细胞等特定免疫细胞的浸润与PTMC的侵袭特性相关；Zhang等人的研究则证实免疫浸润评分是PTC发生中央区淋巴结转移的独立风险因素。然而，肿瘤细胞如何主动调控微环境中其他细胞的状态，以及微环境又如何反过来影响PTMC的进展，其具体机制尚不完全明确。

在众多的信号通路中，除经典的MAPK/ERK和PI3K/AKT通路外，TAM受体酪氨酸激酶家族（包括TYRO3, AXL, MERTK）及其配体（PROS1和GAS6）在多种癌症中被证实参与调控肿瘤细胞的生存、侵袭、转移及免疫逃逸。尽管有研究提示AXL和PROS1在PTC中可能具有促癌功能，但TAM信号通路，特别是PROS1-MERTK这一对配体-受体在PTMC微环境中的具体作用、细胞来源以及其驱动肿瘤进展的完整机制，仍然是一个未被充分探索的关键领域。

因此，本研究旨在深入探究PTMC肿瘤微环境中细胞间的通讯网络，重点揭示PROS1-MERTK信号轴在驱动PTMC进展中的核心作用，以期为PTMC的风险分层和靶向治疗提供新的理论依据和生物标志物。

**本文相关的单细胞分析教程可见：****[这可能是全网最全的scRNA-seq分析教程！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)**

如果需要[数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)**指导** 、生信热点**[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)** 、自测/数据库数据**个性化 分析**辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531145&idx=1&sn=5cbe98083cb0fd67f2b0c18ea3c5fe74&scene=21#wechat_redirect>)，欢迎联系客服微信[**Biomamba_zhushou**]

**二、主要内容**

2.1. 通过单细胞转录谱定义 PTC的细胞生态系统

本研究对来自 15 名患者的 19 份手术组织标本进行了[单细胞RNA测序](<https://mp.weixin.qq.com/s?__biz=Mzk0ODQwNTU5NQ==&mid=2247485774&idx=2&sn=44f273ec0559b80cacf0243ac5dc0965&scene=21#wechat_redirect>)，分析的样本包括 4 个瘤旁（正常）组织、4 个非进展性 PTMC（来自接受 5 年主动监测且无临床进展的患者）、5 个进行性 PTMC 和 6 个进展性 PTC 组织。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXSja6XF4dmNno5Nma9oD6y0BP8HnjQmAOM33ic9IsaibrNjfBXukic7mxg/640?wx_fmt=png&from=appmsg)

Normal thyroid tissue：正常甲状腺组织，作为对照。

PTMC without progression：未进展的甲状腺微小乳头状癌（Papillary Thyroid Microcarcinoma），指肿瘤较小（≤1cm）且未出现侵袭或转移。

PTMC with progression：已进展的甲状腺微小乳头状癌，可能指肿瘤表现出侵袭性行为。

Macrocarcinoma PTC：大型乳头状甲状腺癌（通常指 >1cm），更具临床显著性。

将组织解离成单个细胞，然后对每个细胞的全部RNA（遗传信息表达产物）进行测序。它可以精确地揭示细胞群体的异质性，发现新的细胞亚型，并分析每个细胞在癌症状态下的基因活动。

保留了细胞在原始组织中的空间位置信息，直接在组织切片上测量基因表达。可以看出发炎区域、肿瘤边界、癌细胞如何与周围的免疫细胞相互作用等。

在排除低质量细胞后，[主成分分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&scene=21#wechat_redirect>)将正常、I 期、II 期和 III 期组织的 28 377、28 284、40 788 和 49 080 个细胞分别分为 32 个不同的聚类。平均而言，每个细胞包含≈3000 个基因和 10000 个UMI（图 1B，图 S1A-F）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXzRicBBekysaXVRsJRYuib52tAVV8HeP5sSu7A6gYkFYjJSh6odibDKQXQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXqDgI0j5TDAfwuslxBmmibCCcunSpCJYgia52zeWCuGP2V6rCAk56KOVg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXwZInzrtufkGPECOuFYU1FIabUqAX1GX6IBy0nxxMiacpjiak5sX6Oiatw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXujweIA6J8l0Qhv6aiacic2SxnJsUCO1ibtKemonzhC75o4Q6dDBEMbEeA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXOlmQibh3XzvMod9JZchdric2goREAicKeN3B0x18gJxtE0mXrFajPuViag/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXHYU1377aibZSnbb4VgfeQkuy6z7cbhLhcC3S9Yub45C5epADGDpGSuQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXAzb60J2SYnNkB0VAUQh9xSzqF9RiaAcguSwNdRhVOfKicJoTOe6YPiaag/640?wx_fmt=png&from=appmsg)

[单细胞测序数据](<https://mp.weixin.qq.com/s?__biz=Mzk0ODQwNTU5NQ==&mid=2247485809&idx=6&sn=c0cd5e07a0803a282fc036cca935798b&scene=21#wechat_redirect>)的质量控制。A)、B)、C) 分别为质量控制前的线粒体含量、基因数量和计数分布。D)、E)、F) 对应质量控制后的线粒体含量、基因数量及计数分布。G) 条形图展示各样本中32个细胞簇的占比情况。H) 10x Visium捕获芯片中肿瘤（及毗邻）组织切片的H&E染色与不同细胞簇的空间分布图谱。I) 通过单细胞测序鉴定的3个甲状腺细胞簇在其他组织切片中的空间映射。J) 热图展示各甲状腺细胞簇（列）显著富集的50条标志性通路（行）。

图 1C 中的热图显示了每个簇的差异基因表达谱。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXtzbiaiaxDYKCCwaGljCH6d4wfCKLEHF83YicRBLNdSNhZwt8wvNEichzyw/640?wx_fmt=png&from=appmsg)

这是一张**基因表达热图 （heatmap）**，常用于生物信息学中展示基因在不同样本 / 细胞群中的表达模式差异：

**维度与颜色：** 横轴：通常代表不同的分组（如单细胞分析中的 “细胞簇”“样本”“实验条件” 等）；纵轴：代表不同的**基因** ；颜色：黄色（亮色）表示基因在对应分组中**高表达** ，紫色（暗色）表示**低表达** ，颜色深浅的梯度反映表达量的连续变化。
**生物学意义（结合单细胞** / 转录组研究背景）：
这类热图常用来展示 “标志性基因” 的表达谱 —— 比如区分不同[细胞类型](<https://mp.weixin.qq.com/s?__biz=Mzk0ODQwNTU5NQ==&mid=2247484867&idx=1&sn=1ff30ecb761f954efea5325d9eb9a6a3&scene=21#wechat_redirect>)、细胞功能状态（如增殖、分化），或不同样本（如疾病 / 正常组织）的分子特征。通过观察颜色模式，可识别 “哪些基因在哪些分组中特异性高表达”，进而推断细胞的身份、功能，或样本的分子亚型差异。

根据原型细胞类型特异性标记基因的表达，将细胞分为 6 种原代细胞类型：甲状腺细胞（EPCAM）、成纤维细胞（ACTA2）、髓系细胞（LYZ）、内皮细胞（PECAM1）、T 细胞和 NK 细胞（CD3D）和 B 细胞（MS4A1;图 1D-F）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXJXBwWkP5hgoSiaL6JpyXBdBCiaXMkUQqyibPfvCek4928QsNlJWa8ZNtw/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXiaIjTBuKh0WyrJsZzZokmCvdlicofpSiaOP6Zj70C6ZhDLatUW6vibSNfw/640?wx_fmt=png&from=appmsg)**

**图 D（左图）：细胞分群的整体视图**

这是一张 **t-SNE****降维图** （把复杂的基因表达高维数据压缩到二维，方便观察细胞聚类），不同颜色代表不同**细胞类型** （图例标注了 B 细胞、内皮细胞、上皮细胞、成纤维细胞、髓系细胞、T/NK 细胞）。图中能直观看到，细胞依据基因表达特征，被分成了这 6 类不同的原代细胞群体。

**图 E（中间多幅小图）：细胞类型的 “标记基因验证”**

每张小图对应一个**细胞类型 特异性标记基因**（如  _EPCAM_ 对应上皮细胞、 _CD3D_ 对应T/NK 细胞、 _ACTA2_ 对应成纤维细胞等），展示该基因在 t-SNE 图上的表达分布（颜色越深，基因表达越高）。

比如： _EPCAM_ 高表达的区域，对应图 D 里的 “上皮细胞” 群体； _CD3D_ 高表达的区域，对应 “T/NK 细胞” 群体。以此**验证细胞分群的准确性** —— 即 “分出来的细胞群，是否真的表达该类型的标志性基因”。

**图 F（右图）：不同细胞类型的“基因表达量化”**

这是一张**点图** ，整合了 “细胞类型”“标记基因”“表达量”“表达比例” 4 类信息：

**纵轴：不同 细胞类型（B 细胞、内皮细胞、上皮细胞等）；****
****横轴：各细胞类型的 标志性基因（如  _MS4A1_ 是 B 细胞标记、 _PECAM1_ 是内皮细胞标记等）；****
****颜色：代表 基因的**平均表达量** （蓝色越深，该细胞类型中基因平均表达越高）；****点的大小：代表**表达比例** （点越大，该细胞类型中 “表达这个基因的细胞占比” 越高）。**

比如：B 细胞那一行， _MS4A1_ 对应的点 “颜色深且大”，说明 B 细胞中  _MS4A1_ 不仅平均表达量高，而且大部分 B 细胞都表达这个基因，符合 “ _MS4A1_ 是 B 细胞标记” 的特征；再看 T/NK细胞那一行， _CD3D_ 对应的点 “颜色深且大”，也验证了 _CD3D_ 是 T/NK 细胞的标志性基因。

整体来看，这些图从 “细胞分群→标记基因验证→基因表达量化”，逐步确认了单细胞数据中不同细胞类型的身份，以及它们的基因表达特征。

这些[细胞类型的比例](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&scene=21#wechat_redirect>)因患者样本而异（图 S1G）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXNv1YaRY4PuJR3sibic5iarWVxAicf54o6TQJHmhSYqvgY50P9jia15SLYrA/640?wx_fmt=png&from=appmsg)

疾病进展与 T 细胞和 NK 细胞的逐渐下降以及成纤维细胞的增加有关（图 1G）。此外，与正常或 I 期样品相比，II 期和 III 期 B 细胞的比例有所下降（图 1G）。在上皮细胞中观察到最明显的变化（图 1G）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXsMkuwzYbzRVnBDynra9O0gAG2icmicovmKRbn9tMa2pCib38x3zJiaxrgQ/640?wx_fmt=png&from=appmsg)

图 1H 中的热图说明了来自正常组织和肿瘤组织的细胞簇中癌症标志基因的差异富集。来自正常组织的上皮细胞高度富集氧化磷酸化，而肿瘤上皮细胞在细胞衰老、铁死亡、抗原加工和呈递、癌症途径和 ECM 受体相互作用方面表现出富集（图 1H）。 来自正常组织的内皮细胞富集自身免疫性甲状腺疾病、同种异体移植物排斥反应、细胞粘附分子以及抗原加工和呈递，而肿瘤内皮细胞在 MAPK 信号通路、癌症通路和 ECM 受体相互作用中表现出显著[富集](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510401&idx=5&sn=8cde5a0101cdf1da4a24e614b05cedfa&scene=21#wechat_redirect>)（图 1H）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX2FSaLkxUn1MwNwWgialdaXFJZE4iaj4h8BZOU0XZhVjCibzPwRT1DRuGg/640?wx_fmt=png&from=appmsg)

### 第一部分：上皮细胞（Epithelial Cells）的变化

上皮细胞是甲状腺癌的**癌细胞来源** ，所以它们的变化最直接地反映了癌变过程。

细胞类型| 富集的通路| 生物学意义解读
---|---|---
**正常上皮细胞**| **氧化磷酸化 (Oxidative Phosphorylation)**|  这是细胞能量工厂（线粒体）**高效产生能量** 的核心过程。这说明正常甲状腺细胞正在进行**正常的、高效的代谢活动** ，以维持其生理功能（如生产甲状腺激素）。
**肿瘤上皮细胞**| **细胞衰老 (Cellular Senescence)**|  癌细胞虽然无限增殖，但它们也会诱导一部分细胞进入衰老状态。衰老细胞会分泌一系列因子（SASP），**反而会刺激周围的肿瘤细胞生长、并破坏微环境** ，促进癌症进展。
**肿瘤上皮细胞**| **铁死亡 (Ferroptosis)**|  这是一种铁依赖性的细胞死亡方式。肿瘤细胞可能通过调节铁死亡来**抵抗死亡、适应应激环境** ，或者其相关基因的变化本身就是癌变的一个特征。
**肿瘤上皮细胞**| **抗原加工和呈递 (Antigen Processing and Presentation)**|  这通常是一种免疫功能。肿瘤细胞表面呈现抗原，本应被免疫系统识别并杀死。但有时这种功能可能**失灵或被利用** ，导致免疫逃逸。
**肿瘤上皮细胞**| **癌症通路 (Pathways in Cancer)**|  这直接表明，在这些细胞中，与癌症发生发展相关的经典信号通路（如MAPK, PI3K-AKT等）被全面激活了。
**肿瘤上皮细胞**| **ECM-受体相互作用 (ECM-Receptor Interaction)**|  ECM（细胞外基质）是细胞周围的支撑网络。肿瘤细胞通过改变与ECM的相互作用，可以获得**迁移、侵袭和转移** 的能力。

**小结：** 肿瘤上皮细胞失去了正常细胞的特征（高效能量代谢），转而获得了多种"超能力"：**激活促癌信号、与周围环境互动以利侵袭、以及操纵细胞死亡和免疫识别机制来生存和进化。**

* * *

###  第二部分：内皮细胞（Endothelial Cells）的变化

内皮细胞构成血管，是肿瘤微环境中**供应养分和氧气** 的关键角色。它们的变化显示了肿瘤如何"驯化"其周围的微环境来为自己服务。

细胞类型| 富集的通路| 生物学意义解读
---|---|---
**正常内皮细胞**| **自身免疫性甲状腺疾病 (Autoimmune Thyroid Disease)**|  这说明正常甲状腺组织中的血管处于一个**免疫活跃** 的环境中，可能经常有免疫细胞穿梭，以监视和应对潜在威胁（如自身免疫攻击）。
**正常内皮细胞**| **同种异体移植物排斥 (Allograft Rejection)**|  同样是**免疫相关** 功能，反映了正常组织血管具有招募和激活免疫细胞的能力，这是**健康免疫监视** 的一部分。
**正常内皮细胞**| **细胞粘附分子 (Cell Adhesion Molecules)**|  这有助于**免疫细胞粘附并穿过血管壁** （渗出），进入组织执行功能。
**正常内皮细胞**| **抗原加工和呈递**|  正常内皮细胞也具有一定的抗原呈递能力，可以与免疫系统沟通。
**肿瘤内皮细胞**| **MAPK信号通路 (MAPK Signaling Pathway)**|  这是一个强大的**促生长和增殖** 信号通路。肿瘤内皮细胞激活MAPK，意味着它们被肿瘤信号"刺激"了，可能正在**异常地、快速地构建新的血管（血管生成）** 来为肿瘤供血。
**肿瘤内皮细胞**| **癌症通路 (Pathways in Cancer)**|  肿瘤环境中的血管细胞本身也"癌化"了，其行为被肿瘤信号通路所主导。
**肿瘤内皮细胞**| **ECM-受体相互作用**|  和肿瘤细胞一样，内皮细胞与ECM的相互作用也发生改变，以支持**不规则、扭曲的新生血管的形成** ，这是肿瘤血管的典型特征。

**小结：** 肿瘤微环境中的内皮细胞发生了功能"转变"：从**免疫支持型** 转变为**肿瘤支持型** 。它们不再专注于协助免疫监视，而是被肿瘤"教唆"去疯狂地、畸形地生成新血管，并为肿瘤的生长和转移提供通路。

### 总结与全局意义

这段话通过对两种最关键细胞（癌细胞本身和血管细胞）的功能分析，描绘了一幅完整的**肿瘤生态演化图** ：

  1. **肿瘤细胞自身"黑化"** ：从正常的"能量生产者"变成了拥有多种促癌技能的"破坏者"。

  2. **微环境被"腐蚀"** ：原本负责免疫和供血的"基础设施"（内皮细胞）被肿瘤劫持，转而为其生长和扩散提供服务。

  3. **揭示了治疗靶点** ：这些显著富集的通路（如MAPK、ECM相互作用、抗原呈递）本身就是潜在的**治疗靶点** 。文章后续发现的**PROS1-MERTK轴** ，很可能正是驱动这些功能变化的上游关键开关。

因此，这段话不仅是描述一个现象，更是从**功能层面** 深刻揭示了PTMC进展的生物学本质。

其实这里还可以补一个分析：[肿瘤异质性分析必备| 一文学会四种scRNA-seq拷贝数变异分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531103&idx=2&sn=cad11d768e252d2489d124e68b71c7b0&scene=21#wechat_redirect>)

为了进一步研究 PTC 进展过程中肿瘤微环境的变化，对接受单细胞治疗的同一患者从三个进展阶段的 PTC 组织进行了[空间转录组测序](<https://mp.weixin.qq.com/s?__biz=Mzk0ODQwNTU5NQ==&mid=2247484558&idx=3&sn=b6dfff9e4f452a3f429e823bec306578&scene=21#wechat_redirect>)。进行苏木精和曙红（H&E）染色（图 1I，图 S1H），

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX8R4LtX4Qhh2poKfL3st0x04NsTN8hdybN6HfQRX0l6efQPKVSWAgiaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXiat3ylichebTBAOzfic5TRn5TNlzos9xcdNpbx3KjKPM4725UugusgLWg/640?wx_fmt=png&from=appmsg)

将[10x Visium](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522444&idx=2&sn=3ab5deb0b2a6db78ba2997bacbf869b9&scene=21#wechat_redirect>)从所有 6 个标本中捕获的斑点分成 15 个簇，与 H&E 图像对齐。这些簇在标本中表现出显著的异质性。在 I、II 和 III 期，观察到肿瘤与邻近组织之间有明显的边界。I 期和 II 期肿瘤区域表现出相对均匀的一致性，而 III 期肿瘤区域明显分为两类不同的类别，表明晚期 PTC 肿瘤存在显著的异质性（图 1J-l，图 S1H）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXMTKFd3ib1MN05SHqYp65FMdEqROgBfoUicEaCAOR3Q1vib02upZAETSDQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX0rMLxufPXqzhbrq3G1NSIEwuBzLWYBnt2pjgcJJYQBK8ybRzDSVNWQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXiat3ylichebTBAOzfic5TRn5TNlzos9xcdNpbx3KjKPM4725UugusgLWg/640?wx_fmt=png&from=appmsg)

2.2. PTC 中癌细胞状态的鉴定和表征

使用修拉对上皮细胞群进行基于图形的聚类，确定了八个簇（C0-C7）（图 2A）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXGrblNRj9FibhYQokRIGX3fe675OyubbNDqibibphNSxnPkbdaw6ianibayA/640?wx_fmt=png&from=appmsg)

来自正常组织的大多数上皮细胞集中在簇 C1 中，而癌细胞表现出患者特异性的表达模式（图 2B，C）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXaib2plR4ts9jnUUH7GWGQSlLsVCEYEugnHbbFNbJ4ibY7JazJiakfULXQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXDvIwd6dY2xEhqJ1kJxn04HYpQP5QvAo2ZpmPcB370jicYkHoUqBeibeQ/640?wx_fmt=png&from=appmsg)

甲状腺分化评分（TDS）显示，簇 C1表现出最高程度的分化（图 2D），与其在正常组织中的优势一致（图 2E）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXFXbFqBzgKUTd5yvrTNcMDwAQbuiaEQD5DEzroEDUVkicZRk8QN879JvA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXxBCEr48D8iaEabC6YTJ1nj8jfgVZ7zkqvFDpz3dMGZxDsia9WolRvdnA/640?wx_fmt=png&from=appmsg)

随着疾病的进展，C1 细胞的比例显著下降，从正常组织的平均 74%下降到 I 期的 14%、II 期的 6%和 III 期的 2%，表明这是一个去分化过程（图 2E）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXxBCEr48D8iaEabC6YTJ1nj8jfgVZ7zkqvFDpz3dMGZxDsia9WolRvdnA/640?wx_fmt=png&from=appmsg)

相比之下，簇 C0、C2、C3、C6 和 C7 在肿瘤组织中表现出显著增加的比例，特别是在 III 期样本中，一小部分起源于 II 期（图 2D，E）。主要来源于肿瘤组织的 C3、C6 和 C7 被指定为肿瘤相关上皮细胞。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXK2mCnLskXvpiaxnvnMre5KHia1NCtFW7Sl62l9DS3WibNuvlWAR6XKaEw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXRFpgZPBuen7UIgtRcticHyq30x309tn7LiaJiaSEaiblWznMXP7Xc6ea0w/640?wx_fmt=png&from=appmsg)

[空间转录组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531916&idx=4&sn=e1714c7c1c1a33fa47ffa0b2d5015670&scene=21#wechat_redirect>)结果证实了这些发现，因为与相邻的非癌性区域相比，将 C3、C6 和 C7 映射到空间切片上显示出肿瘤区域的显著分布。C3 分布最大，C6 和 C7 更局部化。随着 PTC 的进展，C6 和 C7 的比例逐渐增加，尤其是 C7，在 III.期丰度明显增加。值得注意的是，III 期切片的左下角主要由间质组织和一些局部卫星病灶组成，显示出这些病灶与 C7 肿瘤细胞的显着共定位，表明 C7 和 PTC 进展之间密切相关（图2F，图 S1I）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXhrdmycDsOsHXEFDoZiaC5AWWC9Anp6Hd92q0rrcSwWz2QkxXD50pbGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXzJI5OxdDnGR2ibvauPTqTsICHkRHP1X8ibLf0RfTq7oFhBiaAaJdokicgw/640?wx_fmt=png&from=appmsg)

[伪时间轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)证实，簇 C3、C6 和 C7 主要代表晚期伪时间阶段的细胞，而 C1 主要由早期细胞组成，表明从正常上皮细胞逐渐转变为高度恶性肿瘤细胞（图 2G）。每个子集群中的顶级 DEG 通过热图可视化（图 2H）

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXNTZ0YiaB0P77pcWmwLvibe3oDO1vHic2FicqlYUUs5zJ4icuWb33mPqCC3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXPjBANRSL4tEDJcTKAJ2TDEeusVl5ZNI4E1aSzFU7VggjHMeFLVDLCg/640?wx_fmt=png&from=appmsg)

基于 KEGG 的功能[富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&scene=21#wechat_redirect>)显示，C1中的 DEGs 主要与正常的代谢途径相关，而肿瘤来源的上皮细胞中的 DEGs 富集在各种癌症相关途径和参与外部相互作用的功能中（图 S2A-H）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX0juyQFdLdkP6ibgwbI6qZbEREpw58cKdDKcvKN8SbN9NsljMYN2HyvQ/640?wx_fmt=png&from=appmsg)

[GSVA ](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&scene=21#wechat_redirect>)进一步证实了肿瘤来源上皮细胞中血管生成、Hedgehog 信号传导、Kras 信号传导、炎症（包括炎症反应和 IL6JAK-STAT3 信号传导）、Wnt-β连环蛋白信号传导和蛋白质分泌的上调（图 2I，图 S1J）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXQnrvlpVJCajLbRkPyoic2VnwbDx2WUZUStnGd2Wa4ickXfYMKEIkiab4g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXC9aeyp3GBiaVB1VibShVicJfvsa4DBqYElzfpPnuVia8feI24Pa9yGZU3Q/640?wx_fmt=png&from=appmsg)

这些结果表明，肿瘤来源的上皮细胞表现出更活跃的生物学过程和与肿瘤微环境更强的[相互作用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)。相比之下，C1 在与脂质代谢（包括脂肪酸代谢、胆汁酸代谢和脂肪生成）、氧化应激和未折叠蛋白质反应相关的代谢途径中表现出高活性（图 S1J），与甲状腺细胞中甲状腺激素产生的生物学功能一致。相反，脂肪酸代谢在 C6 和 C7 中下调（图 S1J），进一步证实了它们的去分化。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX9xlTaecVXxtJQcfrSgja3XVctlicrOaTIgl0Cqxgt0SX73jYRxnQOZg/640?wx_fmt=png&from=appmsg)

在 II 期和 III 期样品中观察到类似的通路，具有明显的差异，例如 II 期炎症反应的显着上调，III 期糖酵解和 NOTCH 信号通路的显着上调（图 2I）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXQnrvlpVJCajLbRkPyoic2VnwbDx2WUZUStnGd2Wa4ickXfYMKEIkiab4g/640?wx_fmt=png&from=appmsg)

2.3．PROS1-MERTK 介导的成纤维细胞-肿瘤上皮[细胞通讯](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)在 PTMC 中随着进展的增强

考虑到肿瘤来源上皮细胞的活跃细胞活性，将[ scRNA-Seq 数据](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528512&idx=1&sn=d316bffcbe59e676cd22248936f07b69&scene=21#wechat_redirect>)与[配体-受体](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510401&idx=8&sn=bebffda99e0c1763147c3315cfe62676&scene=21#wechat_redirect>)相互作用数据库相结合，构建微环境的细胞间信号通路图谱。

比较 I 期与正常组织、II.期和 I 期、III.期和 II.期的信号通路。与正常对照相比，I 期上皮细胞，成纤维细胞和内皮细胞之间相互作用的数量和强度普遍增加（图 3A，B）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX1QxrTcf1wMsCIHjDNpl2ib2SwQicc0fbw3hjGQBVTBbNibVEklhrD1Fxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXFuN5FSmnm1Klgat0gYHCbbMiaBoTz4U16qTJvWIAQRV6JYYofGSiaSxA/640?wx_fmt=png&from=appmsg)

然而，成纤维细胞和内皮细胞之间的相互作用在 II 期（图 3A，C）和 III 期（图 3A，D）减少。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX1QxrTcf1wMsCIHjDNpl2ib2SwQicc0fbw3hjGQBVTBbNibVEklhrD1Fxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXhRNl7KE8SVYc4dutOH87icxFqMFkTKlCDbgsm3mqh6Om4jJnRgdujFQ/640?wx_fmt=png&from=appmsg)

对每个信号通路的信息流进行量化，确定了 PROS1，INF-II 和 POSTN 信号网络，具有正常I 期>II 期≥III 期（图 3E，F;图 S2I-N）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXJsBy68tl4A7ha1xp2ISG9lGrxS6f8U7GqjxRQGy006YcU8mq25L28g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXXV1G1CQwicBQtFcDTsPM4jicEhmg6DHtbBBfjPR2hzNdl0lYxKribT9ibA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXTDlskvepg5oDStDuicuz0rvibeXPYll7plPG4F5O62J1A8EULXcjOSAg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX7CdibhIImlT6Z5W3eKdqHevNoyTQQXJ7zvJX453vgspiawHvSBZ0GW1A/640?wx_fmt=png&from=appmsg)

对[ scRNA-Seq 数据](<https://mp.weixin.qq.com/s?__biz=Mzk0ODQwNTU5NQ==&mid=2247485531&idx=1&sn=d72136317b1a085a45f513c9f9d75cab&scene=21#wechat_redirect>)的分析表明，TAM 信号配体 PROS1 在 II 期和 III 期的肿瘤相关上皮细胞、CAF 和内皮细胞中特异性表达（图 3F，图 S2O）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXEjibYeyYd4UiadGkvqKXddBaob6IYp0rwPyEEibCq1q4AUT2nzsDrh8KA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX6hDotfW97S7kVvxiaCiaaLj04KbVC1ghAv0rYV8ibuTepIbGgS8JhYBVQ/640?wx_fmt=png&from=appmsg)

上皮细胞和成纤维细胞之间的相互作用比其他细胞类型更强（图 3E）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXECjR3picUB69sFspeWtj6NVLPJBmZBMUYCAaaCBNicvyOHrOJ5n8JeXA/640?wx_fmt=png&from=appmsg)

此外，GAS6 在髓系细胞、成纤维细胞、内皮细胞、甲状腺上皮细胞和肿瘤细胞（图 3F）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXQqFpCSsL8YlRozicicreX5zNq2nTrhbjb4x9EA3WibqUOaswNicNhC6kww/640?wx_fmt=png&from=appmsg)

TYRO3 表达很少被检测到，而AXL 在髓系细胞、肿瘤上皮细胞和 CAF 中表达。MERTK主要在 II 期和 III 期组织的骨髓细胞和肿瘤上皮细胞中表达（图 3F，图 S2O）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX0OdpRktkhwy3kFYFAypteGVicc8qHQrTJnibGBpRGvFia6ltpc68ZMu1g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX0TjxVZmc7zicy7NLXtOhSgZeygTicfcEELfvHE6Kx7NKwHhMuOEKlcow/640?wx_fmt=png&from=appmsg)

此外，在肿瘤相关巨噬细胞中检测到 MERTK 表达，在 II 期和III 期组织中观察到显著上调（图 S2P）。如 KEGG 和 GO 分析所示，肿瘤相关巨噬细胞中的高 MERTK 表达与多种癌症相关途径相关（图 S2Q）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXNC1ThnBLPbSPzrsicQSk9UpDoydM5vicmyMhMIbCJvGwgqYXVwnKQLicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXexY6zEkwSKSCibibjm6iaaLosGsnjoawO895ywCNUQe8xELeFPlZGIZGA/640?wx_fmt=png&from=appmsg)

对单个 TAM受体介导的信号通路的检查表明，GAS6-AXL 通路在正常组织和肿瘤组织中都很普遍，尽管具有不同的[细胞间通讯](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529343&idx=2&sn=905ed3c49959e3527adbaaf2800e29a7&scene=21#wechat_redirect>)模式（图 S2I）。在正常组织中，GAS6 信号传导涉及甲状腺细胞、成纤维细胞和内皮细胞，其中髓系细胞是唯一的受体（图 S2I，J）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX9sEVIqEPicmOwicTssDk9icvKtHdGzyTqImysglq4pwicibQc3ZmD22yyAg/640?wx_fmt=png&from=appmsg)

在肿瘤组织中，GAS6-AXL 介导的通讯更为复杂，涉及髓系细胞、成纤维细胞、内皮细胞，偶尔还涉及甲状腺细胞（图 S2I）。PROS1-AXL 通讯是肿瘤特异性的，在正常组织中不存在（图 S2J）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXyVpKaHhD8cfoqicBroUBZztDba3VgicPf8HGOfUuOhLLfZNS4ky6KjyA/640?wx_fmt=png&from=appmsg)

在 II 和 III 阶段，成纤维细胞充当 PROS1 信号的发送者和接收者（图 3E，图 S2J）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX6emK5K8JbrX9vwllAoZbNwRlyhgI7d9OVKFa1krE7JjuwDF5OHgHWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXn34TV3wyzqNRKTQSZREGawUDibZS2z8oEaaiakQdw7oJjpXr6ATxyvPA/640?wx_fmt=png&from=appmsg)

PROS1 和 MERTK 在 H&E 病理切片上的空间表达和分布与[单细胞分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529901&idx=1&sn=3e9cb1075a3b0b4c253ca19addf8b387&scene=21#wechat_redirect>)一致，显示它们在肿瘤区域的主要分布，并且随着 PTC 的进展而表达增加（图 3G，图S2R）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXxkhXat78R9KJ90AR0ib0ZLZ4rqnZhPJT0rQjSzIf2ibdzFoKlFuLhlYg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXibCY0ibjfEjjVUJYlVu6zSubaU7OOonOa63bm4Ve3DOcGzS0icbuqkmcA/640?wx_fmt=png&from=appmsg)

在 IFN-II 信号通路网络中，IFNG是 T 和 NK 细胞在 II 期和 III 期组织中产生的一种特异性信号分子，促进 T 和 NK 细胞、髓系细胞、成纤维细胞、甲状腺细胞和内皮细胞之间的通讯（图 S2K，L）。相比之下，POSTN 充当自分泌信号，主要由 II 期和 III 期组织中的 CAF产生（图 S2M，N）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXZ6GeWRC6Dv0qdv97zYLaqJHuYaXUw0M4JnU95xrVbljibQRDdTFQicGw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX8hEeQlibSia3DKr9Dl9xnJqI3tq8ctNsJPy9GSgAnQpnemqlnefI56vQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX2wFibicu78hrjFwkibHqxjVmlyfjW6lFflVnrHA00Bz5IThP7Bxd6DJng/640?wx_fmt=png&from=appmsg)

2.4. PTMC 中产脂 CAF 释放 PROS1 并伴有进展

POSTN 和 INF-II 信号仅由成纤维细胞、T 细胞和 NK 细胞产生，而PROS1 的表达则源于上皮细胞、成纤维细胞和内皮细胞。考虑到肿瘤细胞在微环境中的关键作用以及成纤维细胞对PROS1 信号传导的主导贡献，对成纤维细胞群进行了进一步的[主成分分析PCA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&scene=21#wechat_redirect>)。成纤维细胞根据表达变化最大的基因分为四个亚群：血管平滑肌细胞 （VSMC）、癌症相关肌成纤维细胞 （myo-CAF）、炎症 CAF （infla-CAFs） 和脂肪生成 CAF （adi-CAF）。这些亚群在四种样本类型的浸润比例上表现出显着的异质性（图 4A-C，图 S3A，B）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXeIgfict0Y9WcXJ7JvQichZxfhhedVetg2GjLxco96SLD33icXltlv8uYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXJvbnGK4NtsyFtxJFCXVvOo2ANnvR4s8sDvmcOYKPXF35WtoawUiaWVQ/640?wx_fmt=png&from=appmsg)

在肿瘤样本中，myo-CAFs 所占比例最高.随着肿瘤分期的推进而减少。Adi-CAF 在 II 期和 III 期显着富集，而infla-CAF 主要存在于肿瘤中，在所有阶段保持一致的比例。差异基因表达的热图分析显示成纤维细胞亚群之间存在显著的转录谱变异（图 4D）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXyWgUZnmYQy5CzZ97akuo8T7p8LCn87E8MC7HyiacspURndmS9J8VSRg/640?wx_fmt=png&from=appmsg)

[GSVA 分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&scene=21#wechat_redirect>)进一步表明，与 E2F 靶标，MYC 靶标 V1 和 V2，myo-CAF 中的 DNA 修复以及VSMC 中与 G2M 检查点，肌发生和胆固醇稳态相关的通路的上调（图 4E）。相比之下，adi-CAF 和infla-CAF 显示出与肿瘤进展相关的通路的上调，包括 Hedgehog，PI3K / Akt / mTOR，Wnt / β-Catenin 和 TGF-β信号通路（图 4E）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXnSuDWFiaf8nuOyS2W2bLvSWdDaBlwSPvpXEnq7akbtWRVIH6v1AZxtg/640?wx_fmt=png&from=appmsg)

值得注意的是，adi-CAFs高度表达 PROS1（图 4F，图 S3C），

III 期 adi-CAF 被确定为 PROS1 表达的主要来源（图 4G，图 S3D）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXkEuWuWWQZCI0hia8mwWULqH1sicsgKqXYhmFbEWcbHr826HGNcqrdFyA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXDibsibWMZ8OrfJAYn7tFGmWbZE0CPPeCNY5Lib7ZCKp3ESRf9vcIde6mw/640?wx_fmt=png&from=appmsg)

[伪时间轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)显示，adi-CAFs 的伪时间得分最高，而 VSMC 和 myo-CAFs 处于早期伪时间阶段，表明 adi-CAFs 可能对肿瘤刺激做出反应而与 VSMCs 或 myo-CAFs 分化（图 4H，I，图 S3E，F）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXibN4mL0Zs6W6rCzCYg9ibGIYv29BbXZ0j2WaCeYnmfs6qHYdPmaJKTOA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXIcLpl1zynylqdCXDbiaAzdg9dYKhicXQtxqYnlYhVVscGCu3gQPafnXA/640?wx_fmt=png&from=appmsg)

[空间转录组学分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531858&idx=3&sn=d910f0bab1834b08a073b2b7b79b3947&scene=21#wechat_redirect>)表明，VSMCs 亚群未能映射到空间切片上，这可能是由于其比例低。其余[成纤维细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&scene=21#wechat_redirect>)亚群表现出显着的空间异质性（图 4J，图 S3G-I）。

Adi-CAF 主要位于肿瘤周围的间质区域，浸润水平随着肿瘤的进展而增加。 在 I 期，infla-CAFs 和 myoCAFs 均呈从肿瘤外围向中心浸润的趋势，但随着肿瘤进展，这种趋势逐渐减弱，到III 期，肌 CAFs 浸润几乎不存在。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXK8SEXvsfc2oh7JDosf83vcr9hQIDxCJia8lib0lBXOpKjZJ198lRVWzw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXhMVPJRjZp6VlL1iaep9rt5jSkxy4nxUOXFSOc2dkI2MALRfqfU0OImQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXa1GBhKHOwcNoQGQ98x0yBU0S204hI9s6g6xyibqn6dhbVEJGkUKyyzg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXXmHdfUkU5E0F27kVWX7vyf0kDXmyIrz1jPpI9kEoGibNPzicOsDMPFIw/640?wx_fmt=png&from=appmsg)

2.5. PTC 中 TAM 受体介导的细胞间通讯

接下来大部分都是实验验证了，没错，实验我们也能教：[手把手教你做实验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532039&idx=2&sn=1e7a1ae6097fe217182f1ff305325512&scene=21#wechat_redirect>)

为了验证TAM 受体（MERTK 和 AXL）及其配体（GAS6 和 PROS1）在不同肿瘤阶段的表达模式，进行了多次[免疫荧光](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532039&idx=2&sn=1e7a1ae6097fe217182f1ff305325512&scene=21#wechat_redirect>)测定（图 5A，图 S4A）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXfSAqc0d4UDmnYLViapgdNrB8VSzKykibTxukOnd2eWiaQltShw69zFycg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXAibVicK8poZHiaavTWVibCOPkImSS4h4LxBQQgGQdQSkU5YiaHFmHxqvP6g/640?wx_fmt=png&from=appmsg)

GAS6 信号在非进行性 PTMC 组织中最为突出，在侵袭性 PTMC 和进行性 PTC 之间没有观察到显着差异（图 S4A）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXbbMlXEzmtG6NnGK04wLt7dMqCyAeibayjpQTWvq4ShdFlQ5hGH66dmw/640?wx_fmt=png&from=appmsg)

PROS1 和 MERTK 信号在侵袭性 PTMC 和进行性 PTC 中均显着升高，其中 MERTK 显示出特别高的表达（图 5A）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX4Qepr6l1Wfsx3FfgEMYvAPr2GXb4f5VM907oicJAnjEZ4LDkRYMXMxA/640?wx_fmt=png&from=appmsg)

在进行性 PTC（II 期和 III 期）中，几乎所有肿瘤细胞都表现出强烈的 MERTK 表达，而 AXL 表达在正常组织和肿瘤组织之间保持不变（图 S4A）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXbbMlXEzmtG6NnGK04wLt7dMqCyAeibayjpQTWvq4ShdFlQ5hGH66dmw/640?wx_fmt=png&from=appmsg)

免疫荧光测定与单细胞测序数据一致，显示 ACTA2+ 成纤维细胞和 PROS1 在正常组织或非进行性 PTMC 中没有共定位，但在侵袭性 PTMC 和进行性 PTC 中，共定位很明显（图 5B）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXNAiagYVvr1tOeWxxRPwIIn5ZH6H8CJMLhib8y2trYCQB6l26GAGoJUww/640?wx_fmt=png&from=appmsg)

对来自正常组织、I 期、II 期和 III 期标本的 50 个样本的免疫组织化学证实，II 期和 III 期的 MERTK 表达显着升高。与正常组织相比，PROS1 在肿瘤中的表达显着更高（图 5C，图 S4B）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXlekkudcia2F8ic5y0Fe4jMnBOywKrzy3gfAAbCNbeNE85k0PM54SYq5Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXAfHKtsuWOKWOvquZQ0bKYlUzlGUvfo0fhdwAC34bvu6BlOXvJOEu6w/640?wx_fmt=png&from=appmsg)

我们对 50 个非进展性 PTMC（I 期）和 100 个临床进展的 PTMC（II 期、III 期）之间的 MERTK 表达进行了免疫反应评分分析。结果显示，与临床进展的 PTMC 相比，非进展性 PTMC 的免疫反应评分显著降低（图 S4B）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXAfHKtsuWOKWOvquZQ0bKYlUzlGUvfo0fhdwAC34bvu6BlOXvJOEu6w/640?wx_fmt=png&from=appmsg)

与 I 期 CAF 和 NF 相比，原代成纤维细胞培养显示 PROS1 在 II 期和 III 期 CAF 中显着过表达（图 5D）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXu5yYv032lKJzenLBXZxEiciaLKfuIxJkrHcWqIQyVUjXVzV8eCADs3VQ/640?wx_fmt=png&from=appmsg)

类似地，相对于正常甲状腺滤泡上皮细胞，原代 PTC 细胞培养物在 PTC 细胞中表现出显着的 PROS1 过表达（图 5D）。与 I 期和正常甲状腺滤泡上皮细胞相比，II 期和 III 期 PTC 细胞中的 MERTK 表达也显着更高（图 5D）。相比之下，AXL 和 TYRO3 表达在正常组织和肿瘤组织之间没有显着差异（图 5D，图 S4C）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXbhibKSqibwBKY7hcN0IOlaqejQmauy3nJlfYVQnkAjSZhIb7FgmQkfDQ/640?wx_fmt=png&from=appmsg)

点印迹测定显示，与 I 期 CAF 或 NF 相比，II 期和 III 期 CAF 中的 PROS1 释放增加（图 5E），NF和 CAF 之间的 GAS6 分泌没有显着差异（图 S4D）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXg9kpKton756R78DziaOfN0paI5uhrUNBuhrYY5PtTcs1Op3SRMkWIfA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXibKRML4jMJIib3BgSam32iaXdKVu0kaZsKOfWBuLqQddb7qMvID5X9OYw/640?wx_fmt=png&from=appmsg)

[单细胞数据](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&scene=21#wechat_redirect>)进一步支持甲状腺细胞中 MERTK 的上调，特别是在与肿瘤进展相关的簇 2、3、6 和 7 中（图 5F，图 S4E）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXeIecZnLSib8icwB0sTNNXQvKop5HSGbWE5pJr1dsbP1O62sEZjkISUaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXMuz2BSkJGpdqiaF4FWbibNic1FVWrnXliakmicE7tH3iaSlEuD92QxMHiaEAQ/640?wx_fmt=png&from=appmsg)

TCGA [Bulk RNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529986&idx=2&sn=301d44caa8d63cba8243d13579775cf5&scene=21#wechat_redirect>)数据（568 个样本）证实，与邻近组织相比，肿瘤中 PROS1 和 MERTK 显着上调（图 5G，图S4F）。对 TCGA 队列的亚组分析显示，高 PROS1 表达与较高的 T 分期和 LNM 呈正相关，导致预后较差（图 5H-J）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX5LsibtyHwsicexI0s1EZtBmUT7vp5yabIuWZcTah3y4kAJwACGzbXuaA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXpo8XChd2PnO8pVh2YJWIGhDZicdDiapmzGeOiaCRCxhUpdwMJVelDI4gg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXWK1EBNVNPxHq6icmic3Ruic8WPzFJ7PG62icmsx3FkmKhr3KrEXQsxQAdg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnX7hr5ueuKw4lV3vhIfqkhZr4BmzyzGvibAuXKhFQKplClnib220PhJcwg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXw7F5P8p2icSVgNSBpViasa5oGLZMIesQl27KhZKZpp0dECv2HqiaFB1Qg/640?wx_fmt=png&from=appmsg)

2.6. PROS1-MERTK 通过旁分泌和自分泌途径促进 PTC 进展

细胞功能测定证实了 PROS1-MERTK 配体-受体相互作用在 PTC 中的作用。结果表明，PROS1 过表达 CAF 的上清液显著增强了 sh-PROS1、TPC1 和 K1 细胞的迁移、侵袭和增殖。在 shPROS1、TPC1 或 K1 细胞中用 PROS1 中和抗体和 MERTK 敲低处理可降低这些效应（图 6A-C）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXLIlOD5DQ7zSHicb7fmOwAEv1FZ5Wpw9GpeYhiadDAG0QCUNHicY79uF9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXx7rwUEjhafPicxr5WCb7E5ichNs73liaibPW3OhTz2HEBmqFrEnm4XuKdg/640?wx_fmt=png&from=appmsg)

小鼠模型中的皮下植入表明，与 NC 组相比，注射 sh-PROS1 K1 细胞和 PROS1 过表达 CAF 的 1：1 混合物的肿瘤表现出明显更大的体积。然而，sh-PROS1 K1 细胞中的 MERTK 敲低减少了 PROS1 过表达 CAF 诱导的肿瘤生长（图 6D）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXUvdic9dJLas9FWdBJoBQxEQajYWVXNjJyz6DXJ8YbdicYcuUy1FDeZzQ/640?wx_fmt=png&from=appmsg)

为了探索PROS1-MERTK 相互作用的潜在自分泌效应，PROS1 在 PTC 细胞中过表达。结果表明，PROS1 过表达促进了迁移、侵袭和增殖，而抗 PROS1 处理或 MERTK 敲低减轻了 PROS1 诱导的 PTC 细胞迁移和侵袭（图 S5A-C）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXsRbRNV6KOibt5Z4qico2NOeqicib4yXUqS5PQlx0hu0Pe7Bvgx9SRfkRPA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXWHMhEyCn4Z4QuWrvyicX4INKdrR8voicZnDdcoWxBxExbPMdSnCUPO7w/640?wx_fmt=png&from=appmsg)

体内皮下植入还表明，注射 PROS1 过表达 K1 细胞的肿瘤明显大于 NC 组，K1 细胞中的 MERTK 敲低减少了 PROS1 过表达驱动的肿瘤生长（图 S5D）。这些结果表明，PROS1-MERTK 相互作用通过旁分泌和自分泌机制促进 PTC 中的肿瘤进展。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXZEbibDJH001qZKo1OGMgael4f04iapxWqGatOpiaPD3vZwUmrgCySHb3Q/640?wx_fmt=png&from=appmsg)

2.7. NFYB、FOXP2 转录激活 PROS1 并通过 MERTK /WNT/TGF-β 途径促进 PTC 进展

鉴定adi-CAF 中 PROS1 的上游调节因子，进行[基因共表达分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)，并利用 [SCENIC 分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530488&idx=1&sn=e0c57d42b1ecb73e8b7b9f6caecbb81d&scene=21#wechat_redirect>)对每个细胞共表达和富集 TF 顺式调节基序的基因模块活性进行评分。注释的靶基因分为高置信度和低置信度注释。FOXP2 和 NFYB 被鉴定为PROS1 的高置信度转录调节因子。

tSNE 和 TF 富集热图表明，adi-CAF 过表达 FOXP2 和 NFYB，与PROS1 表达一致（图 7A，B）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXMzy5luEfHeNAp9vmRP0JXp96IbsWZ4Fu3mXl9mI3EfojxNgBibibQcHw/640?wx_fmt=png&from=appmsg)

敲低 CAF 中的 FOXP2 和 NFYB 显著降低PROS1 mRNA 和蛋白质表达（图 7C）。双荧光素酶报告基因测定证实 FOXP2 和 NFYB 与PROS1 启动子结合（图 7D，E）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXxqHJ7BKo0EkXoKjicIG7fXuTm6xgalTgq3KA08AJuRpZNB0GmgVfehA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXNHicndbjtntSoXMCWFicpib3whNJE61kDwgT1rdia3nhHl8GYXzRkpzwsw/640?wx_fmt=png&from=appmsg)

这些结果表明，FOXP2 和 NFYB 在 CAF 中转录激活 PROS1。

为探究MERTK 的潜在下游机制，对 21 份单细胞转录样本中MERTK 高表达和低表达的肿瘤细胞数据进行 GSEA 分析。结果显示 WNT/β-Catenin 和TGF-β信号通路显著激活（图 7F）。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXAOryaL3Ph9j5UqicWHf9RCatnZhBiaPhzlfxpP0bib29FPla6AKHTnictg/640?wx_fmt=png&from=appmsg)

蛋白质印迹分析进一步证实，PROS1 通过旁分泌或自分泌途径影响 MERTK 下游信号传导（图 7G，H）。来自过表达 PROS1 的 CAF 的条件培养基显著上调甲状腺癌细胞中 β-catenin、C-myc、CCND1 和p-SMAD2 的表达。

然而，K1 或 TPC1 细胞中的 PROS1中和抗体或 MERTK 敲低抑制了这些蛋白质的表达（图 7G）。使用激活剂（CHIR-99021 和 SRI-011381）激活 WNT 或 TGFβ通路挽救了PROS1 中和或 MERTK 敲低的影响（图 7G）。 此外，PTC 细胞中的 PROS1 过表达增强了β-catenin、C-myc、CCND1和 p-SMAD2 的表达，而抗 PROS1 或 sh-MERTK 降低了它们的表达（图 7H）。

WNT 或 TGF-β 通路激活剂（CHIR-99021 和SRI-011381）有效挽救了 PROS1 中和抗体或 MERTK 敲低诱导的作用（图 7H）。这些结果表明，PROS1 通过MERTK/WNT/TGF-β 途径促进 PTC 进展。

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXmvT6gwrib3S77YEIqpNADIpO8DicjRKy8nfk15Oqy4FDMPucJJOScibrQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GQbSTiaXLprMNDaE69iaNHqDOvFFDhvJnXJphNnLIaQ9Y812eibHBReFulT6Ks3ibmSZAdibc9uDrO5Wu5iakxpzMRBA/640?wx_fmt=png&from=appmsg)

如果需要[数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)**指导** 、生信热点**[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)** 、自测/数据库数据**个性化分析** 辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531145&idx=1&sn=5cbe98083cb0fd67f2b0c18ea3c5fe74&scene=21#wechat_redirect>)，欢迎联系客服微信[**Biomamba_zhushou**]

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24) 您点的每个赞和在看，我都认真当成了喜欢
