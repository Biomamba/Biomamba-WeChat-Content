---
title: "Cell metabolism| 单细胞测序技术解析健康人与T2D患者的胰岛差异"
date: 2023-03-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=1&sn=b7f8df758bc4d95b88969378c6dfbeee&chksm=9b3c8ea1ac4b07b7c6a0b5023ebf6c8ecd7d34741ab076baa0b564535d1d753bbf9dc5be5290#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# Cell metabolism| 单细胞测序技术解析健康人与T2D患者的胰岛差异

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=1&sn=b7f8df758bc4d95b88969378c6dfbeee&chksm=9b3c8ea1ac4b07b7c6a0b5023ebf6c8ecd7d34741ab076baa0b564535d1d753bbf9dc5be5290#rd
> 合集：单细胞教程全收录 / 文献速递

**文献信息**

●Single-Cell Transcriptome Profiling of Human Pancreatic Islets in Health and Type 2 Diabetes●Cell Metabolism● IF:31.373

**Introduction**

关于糖尿病的推文我已写了数篇，关于糖尿病的背景不做赘述。作为一个维持体内代谢的重要器官，胰腺中的外分泌细胞及腺泡细胞可以产生消化酶并分泌到肠道之中。在胰腺中大量分布的胰岛主要由α细胞（30~45%，分泌glucagon，GCG）、β细胞（50~60%，分泌insulin，INS）、γ/PP（pancreatic poly-peptide）、δ细胞（与PP细胞的合不足10%，分泌somatostatin，SST）、ε细胞（不足1%，分泌ghrelin，GHRL）组成，占据了胰腺2%的质量。而T2D发病的根本原因便是外周组织的胰岛素抵抗性上升从而导致β细胞的质量及功能降低。为了更精确的找到健康者与T2D患者的胰岛差异，本文利用单细胞测序技术对两组胰岛进行了细胞类型之间的分析。

**Methods**

本文的method是一个值得关注的点，为了多维度、全方位的展示两组胰岛的差别，作者设计了一系列的实验与分析方法以精确解析数据。

**● Single-Cell RNA-Seq of Pancreatic Islets**

作者使用flfluo rescence-activated cell sorting（FACS）将胰岛分选至384孔板中，以Smart-seq2的方式建库测序。这里我个人觉得有些浪费，因为与之前提到过的10X不同，Smart-seq2的测序对象为RNA全长而10X获得的仅是3'端的序列。因此Smart-seq2可用于转录本的结构分析而不仅局限于组成分析，但本文并没有做这一部分的分析，因此实质上与10X的分析项目无异。

**● RNA-Seq**

为了评估RNA-Seq与单细胞测序之间由技术引起的系统误差，作者对样本进行了Bulk RNA-Seq。

**●** 此外，本文还做了Single-Molecule mRNA Flurescence In Situ Hybridzation及测序后的各项分析工作。

**Results**

首先，作者对样本捐献者的基本信息做了统计，数据如下表所示。从列表及后续分析中我们可以发现作者充分的考虑到了性别的因素，但是却忽略了年龄因素，因此本文后续的一切分析可能会受到这一因素的干扰。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzIaxTSH2LlNaDIv6AOppoBghDlicbjlVYG86JAAu824F88YGCFHeyJeI3mlGEKTopTBNO3kzolWCg/640?wx_fmt=png)

****●** 1、测序前准备：**为了确定健康样本的胰岛确实具有正常的功能，作者首先对胰岛进行了葡萄糖刺激。可以发现，各样本在经过葡萄糖刺激后胰岛素分泌水平均有所上升，且除了H4样本外均有显著性差异。确定了胰岛功能后作者对这些胰岛建库测序，测序结果显示，共得到了3386个细胞，质控后对剩下的2209个细胞进行了进一步分析。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzIaxTSH2LlNaDIv6AOppoBu0Nl2GialBbboKibwcTxr97ZQxNg5HEG59ILsiaiaAmbmoaK3CB3VXyrJw/640?wx_fmt=png)

******●**** 2、细胞类型确认：**

首先还是使用单细胞测序细胞聚类的老方法，本文使用t-SNE聚类方法将胰岛细胞聚为以下几类。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzIaxTSH2LlNaDIv6AOppoBMNOXADszJhuibMrVB5Ashktibr6h6IoDmbCmgXic2HnEpKr6p4o1yO6sg/640?wx_fmt=png)

做了以上降维分析后作者通过下图中的 _PRSS1_ 、 _KRT19_ 两种基因的表达分布情况鉴定出外分泌腺泡及导管细胞。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzIaxTSH2LlNaDIv6AOppoBOESyCLKSKS9G3dYmiaxXrH8jWGq9jyG9kIKHgO9jcjV2g6rzVJ5Vrbg/640?wx_fmt=png)

通过对下图中各基因RPKM的计算，作者注释出了pancreatic stellate、endothelial cells、mast cells、antigen-pressing MHC class II cells等细胞类型。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzIaxTSH2LlNaDIv6AOppoBVxjl48pYPEN8peuZHYlYhpXlElNoBhaAEqiboBItFE0azcAqN3HuVbA/640?wx_fmt=png)

******●**** 3、细胞类组成及表达差异：**这一部分数据值得深思，此前我曾经提过，虽然单细胞测序是一种高分辨率、高通量的技术，能够充分考虑到细胞间的异质性，但是在单细胞悬液的制备以及建库的过程中，对于细胞来说均是一种应激反应，在这些处理的过程中是否会让细胞进入一种应激的表达模式，以及不同种的细胞数量是否会收到这些处理的影响，这些问题均是未知数。因此作者便设计了这一部分的实验以评估系统误差带来的影响。作者主要是对提取的胰岛针对GCG与INS使用免疫组化染色技术检测了胰岛提取过程中对各细胞类型的影响，免疫组化结果如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx4GAum51xXv95YM9Ge9S1Y8WqN14jn9DAkxic1rCGUNm6sradaicsp4U4LoVibhrIibibebFDSMyJQNow/640?wx_fmt=png)

此外，作者还针对GCG，INS和SST利用FACS技术进行了统计，结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx4GAum51xXv95YM9Ge9S1YSqX93dcIf35og3N8aicdib5jiaiaeus0MU6GQBzfrgSMyCt8RTia51d5Nzw/640?wx_fmt=png)

这一组实验的结果显示 _α_ -细胞在单细胞测序数据中更多而β细胞却更少，这表明在单细胞的建库过程中 _β_ 细胞的存活率更低，这证明单细胞测序与FACS确实会在操作过程中引入系统误差。此外，为了证明单细胞测序在转录组水平上是否存在系统误差，作者拿单细胞测序与胰岛的Bulk RNA-Seq进行了RPKM的相关性分析，spearman系数在0.86~0.92之间，可以认为Sc-RNAseq与bulk RNA-seq均能为转录本的分析提供可信的图谱。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx4GAum51xXv95YM9Ge9S1YaSVXdycVUBqDLfib89znDickzZyEuUhu1QxsgBAkZIfuCTuh5TpT4ccQ/640?wx_fmt=png)

******●**** 4、内分泌细胞的基因表达情况：**下图为各细胞类型的平均RPKM值，可以发现，内分泌细胞的平均值大约为5500而外分泌细胞的平均值大约为7000。虽然内分泌细胞的平均表达量更少，但是其中各种激素占据了绝大多数。 _INS_ 、 _PPY_ 和 _SST_ 的转录组占据了α、β、δ细胞约50%的转录本。在α与ε细胞中， _GCG_ 与 _GHRL_ 占据了大约20%的转录本。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx4GAum51xXv95YM9Ge9S1YZNo91iaicSdET2FoL1M3HaQGTWBSrI0oLQIML0jt9sib9YcauAa76h27Q/640?wx_fmt=png)

为了进一步探寻α、β、γ、δ、腺泡、导管这六种细胞的基因表达模式差异，作者做了以下热图。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx4GAum51xXv95YM9Ge9S1YBFTnDBbocbkfficFuKaSCbghWbeJE020UfWibMoext2TNeKf1cCAj4Ew/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx4GAum51xXv95YM9Ge9S1YNibpH1vCchN1UWzj87JOJgRl7nVQPJcJgYFJyH06KRBDlB34tJ65Llg/640?wx_fmt=png)

显然上述热图要素过多，因此作者挑选了一些特定的基因作为各cluster的marker gene，其表达量如下图所示。图中可以发现， _GCG_ 、 _LOXL4_ 、 _DPP4_ 、 _GC_ 与 _FAP_ 可以作为α细胞的高质量marker gene。INS、IAPP、ADCARP1、PDX1、MAFA、NK6-1与MEG3可以作为β细胞的高质量marker gene。为了验证marker基因，作者使用RNA原位杂交技术进行了鉴定，结果如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBM0WrX5ueDvz7hJ8jiaOzdvRWSZOWHzX8m5icZkHCq3vVLyDgiaWYhyBGQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBOD6UicbW1TEscYxN7IU7N1DpwPwM4JyibkoZTqY7F0GzCDPg2gbfzn9Q/640?wx_fmt=png)

******●************5********、对γ、δ、ε转录本的剖析** 因为这一部分细胞的数量占内分泌细胞的比例较少因此作者将这一部分细胞单独罗列，值得一提的是，分析中发现δ细胞中高表达许多特有的受体（如 _UNC5B_ ,  _GABRB3_ ,_GABRG2_ ,  _CASR_ ,  _FFAR4/GPR120_ ,and  _KCNJ2_ 等），最重要的是还从其中发现了瘦素受体（一个与肥胖密切相关的激素受体）。
在γ细胞类群之中鉴定出的marker gene为 _SERTM1_ ,  _SPOCK1_ ,  _ABCC9_ , and  _SLITRK6_ 。此外，在2209个细胞之中，仅存在7个ε细胞，其中 _GHRL_ 与 _HRLOS_ 可以作为marker gene， _NPY1R_ ,  _OPRK1_ ,  _PTGER4_ , and  _ASGR1_ 等受体、 _PCSK6_ 酶也在 ε细胞中特异性表达。******●**** 6、转录因子：**作者对scRNA-seq中的转录因子序列进行了研究，结果如下图所示，发现 _MAFA_ 仅在β细胞中表达、 _IRX2_ 仅在α细胞中表达。此外，还有一些转录因子仅在特定的细胞类群中表达，如ARX在α与γ细胞中高表达，且在小鼠的胰岛胚胎中高表达ARX基因会引起α与γ细胞数量的增加。HHEX在δ与导管细胞中表达，MAFB在α、β、δ中高表达。接下来都是一些报菜名的操作，就不一一赘述了。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBE2dicHUFvibQg8fKrw80EFeRlUDFicdQr3kKvAIf8MwS2osMU8OS8mpGQ/640?wx_fmt=png)

**●****7****、细胞亚群及状态的鉴定：** 为了进行更高分辨率的剖析，作者对每一种细胞移除了样本偏差后进行了聚类，大部分细胞分散的比较集中，但有12个α细胞被分离开来。这些细胞 _GCG_ 的表达量与α细胞无明显差异，但 _C10orf10_ ,  _PEMT_ ,  _PLCE1_ ,  _ARRDC4_ ,  _CRYBA2_ ,  _LOXL4_ 等α细胞的marker基因、及一些与增殖相关的基因如 _TOP2A_ ,  _MKI67_ ,  _CENPF_ ,  _BIRC5_ , and  _CDK1_ 在这12个细胞中表达量下调。此外，在腺泡细胞与导管细胞中也发现了少量细胞表达与增殖相关的的基因，表面这些细胞可能与胰腺的更新与修复相关。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBxYyTqR60OXalNRJkNtic1loBicHyxEZ4IsGr5WMFKbY1T8XoicdJT5k0Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBicTrfrlwlcDh92ucIKlj7XJhRMucazpUY1gzv8uLKabcnD5HPI6Q12w/640?wx_fmt=png)

对β细胞的解析中如下图所示，我们可以发现β细胞一共可以被分为五个亚群，这五种细胞表达 _INS_ 的水平相当，cluster1与5表达 _RBP4_ （这一基因在肝脏与脂肪细胞中表达，是一种脂肪因子），RBP4在外周组织浓度的增加与肥胖与T2D及胰岛素抵抗的水平具有相关关系。这部分细胞还表达 _FFAR4_ 基因，该基因的激动剂可以诱导小鼠胰岛释放 _INS_ 。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBNK6Gic592h9tbbuL1Sdeuo3Hhg5Rva7xczKFM2QfJic9nbiaXXzmJCcJQ/640?wx_fmt=png)

最后，作者对腺泡细胞的聚类中发现了两个亚群，其中cluster1的高表达基因中包含许多炎症相关的基因，如促炎的趋化因子（ _CD74_ ,  _HLA-DMA_ ,  _HLA-DRA_ , and  _HLA-DRB1_ ）、MHC II类分子、细胞因子（ _IL17C_ and  _IL18_ ）及与免疫相关的转录因子（ _STAT1_ ,  _NFKBIA_ ,  _NFKBIZ_ ,  _HIF1A_ ,  _SOX4_ , and  _ONECUT2_ ）。而cluster2高表达的基因主要功能为编码分泌的消化酶及其调节的转录因子。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBiap6d8DKodyutpzCKgQpZPFcnfOhcZ4BQj4ibCSRGbjRMiayrKqg76d4g/640?wx_fmt=png)

******●**** 8、在肥胖进程中基因表达的变化：**为了找到与肥胖进程相关的基因，作者对五个健康男性的每种cluster基因表达情况与BMI之间进行了相关性分析，结果如下图所示。 _PCSK1_ inhib-itor (_PCSK1N_)在所有细胞中的表达与BMI都呈现强烈的负相关关系。 _PCSK1_ 能够使 _INS_ 、 _SST_ 、脑啡肽等激素的前提转换为活性模式。而 _PCSK1N_ 高表达的转基因小鼠也会呈现出肥胖的表型。 _SCG5_ 在所有细胞类型中的与BMI也呈现负相关关系，其是 _PCSK2_ 的分子伴侣，可以帮助 _GCG_ 、 _IAPP_ 的前体转换为活性形式，表面α与β细胞的功能损失可能与 _GCG_ 、 _IAPP_ 的产生缺陷相关。 _CAKM2_ 在内分泌细胞中的表达水平与BMI呈负相关的关系，其编码钙调节蛋白并与β细胞的胰岛素释放相关。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBrYLMuoxvtHuKWTMQ7Od9Eo2kibGiaQeDx14rpvWa73pWpjKs2rslMa3Q/640?wx_fmt=png)

为了探寻Bulk RNA-Seq中的基因表达量与BMI之间的关系，作者也做了相关性分析，与Bulk RNA-Seq的结果对比发现，ScRNA发现的相关性基因有所不同。（之前作者以二者RPKM的数值就认为两种数据集之间无显著差异的方式我就不是很认可，两种数据集的差异必然是很大的 ）

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBGK2nhrP9wFRQ7NsHDcfd7j50voJt7mCU1KeU4nPyiaCn4Tgc5qn3ricw/640?wx_fmt=png)

******●**** 9、T2D导致的基因变化：**由下图的差异基因表达图可以看出T2D的上调差异基因占比很高且，INS表达量与β细胞的质量都会随T2D的进程而减少。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBdY3pmvaAJjhyFXiaGicRKvSELlqk5wrneIVCTbcfZRpVImDDFt1Uib9ug/640?wx_fmt=png)

具体的差异表达信息如下图所示，在T2D患者的β细胞中下调水平最显著的为FXYD2基因，其编码了Na/K-ATPase的γ亚基，缺少了这一基因会导致小鼠的葡萄糖耐量增加，并伴随着胰腺的增生及血浆中INS水平的增加，**这一基因的高表达会引起肾脏细胞的分裂率下降** 。另一方面，T2D中也存在一些上调的基因，如GPD2与LEPROTL1，前者与NADH转运有关而后者与瘦素相关。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IByiat4TIsBGfuD068ziaweWdUlvcnpyAuXe5fEdyjibExglRubMnuTj31Q/640?wx_fmt=png)

作者使用基因集为对象进行了差异分析后得到下图，从这个图中可以发现关于线粒体内能量代谢、蛋白质合成的基因集在T2D患者中表达量下调。关于细胞凋亡、糖尿病肾病及细胞因子的通路表达量上升。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpybvLIviaEC4LTeJUNfOM8IBDrP8VDJuwXH26pmBwyPqr4CNzvCVgCChkgrd8gBiaCJubxUbkSiaFQ5w/640?wx_fmt=png)

**谈谈个人想法**

总的来说，这篇文章中应用到的技术多样、工作量可观、逻辑合理，对于问题的描述也十分清晰，总体上阐明了健康人与T2D患者在胰腺中的差异，对于后人的研究具有参考价值。

参考文献doi: 10.1016/j.cmet.2016.08.020

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器的**微信号** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
