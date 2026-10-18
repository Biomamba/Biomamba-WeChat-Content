---
title: "单细胞水平解析循环肿瘤细胞(CTCss)的多种基因组变异并预测新抗原"
date: 2026-09-27
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542450&idx=1&sn=6885ae2f91844dd77824ff9f9a763acd&chksm=9b3c5fe2ac4bd6f443f0a7036cf22f93b5156e378c7f82148d2f965dba06e3c2ffccda49198e#rd
albums: ["文献速递"]
---

# 单细胞水平解析循环肿瘤细胞(CTCss)的多种基因组变异并预测新抗原

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542450&idx=1&sn=6885ae2f91844dd77824ff9f9a763acd&chksm=9b3c5fe2ac4bd6f443f0a7036cf22f93b5156e378c7f82148d2f965dba06e3c2ffccda49198e#rd
> 合集：文献速递

* * *

**一、写在前面**

**文章** Identification of multiple genomic alterations and prediction of neoantigens from circulating tumor cells at the singlecell level**（IF=17）** 发布于2025年**《 Nature Communications》。**

1.循环肿瘤细胞(CTCs)与癌症进展和不良预后有关，准确检测CTCs中的基因组改变对于提高癌症诊断和治疗至关重要。

2.该文章开发了统一染色体构象捕获(Uni-C)，这是一种在[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)水平上分析3D染色质结构和基因组变化的方法。

3.使用Uni-C分析了胰腺癌患者来源的异种移植瘤(PDX)和自发性肿瘤小鼠模型的CTCs。

在PDX模型中，集成来自7个CTC的数据捕获了88.7%的SNPs和Indels，以及75.0%的存在于肿瘤组织中的结构变体。表明在CTC中检测到的变异反映了肿瘤基因组的特征。

文章还观察到有丝分裂和间期CTCs之间的染色质构象差异，暗示了细胞活力的潜在标记物。

在自发肿瘤模型中，发现了CTC的基因突变并预测新的抗原，从而推进了癌症的早期发现和治疗策略。

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)、自测数据个性化分析辅导、[实验科研服务](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=1&sn=578993fdfa060d38c80e2df6fc200c39&scene=21#wechat_redirect>)和[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=2&sn=1d329f22e35586dc794ce30aa6bd0ce4&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、主要内容**

**1.Uni-C概述**

首先使用乙二醇双琥珀酰亚胺琥珀酸酯(EGS)和甲醛对细胞进行双重交联，然后进行细胞裂解，染色质的碎裂是使用4碱基的切割器限制性内切酶，然后在相同的反应混合物中进行末端修复和邻近连接。然后用玻璃毛细管将单个细胞核转移到碱性裂解缓冲液中，为随后的单核扩增奠定基础。单核扩增使用了热稳定的phi29DNA聚合酶，以及dNTPs和α-硫醇修饰的ddNTPs的混合物，以及抗外核酸酶的随机引物。在扩增过程中加入α-硫醇修饰的ddNTPs有效地终止了延伸，从而将扩增产物的大小控制在2kb以下。此外，使用快速、耐热的phi29聚合酶将扩增时间减少到大约2小时。然后对扩增产物进行大小选择，然后准备文库进行高通量测序，以便于下游分析。获得的测序数据提供了两种关键类型的信息：染色质三维相互作用数据和全基因组测序数据

![](../../images/b37048b2b67d217c.webp)

2.UNI-C可以在[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)水平上有效地识别SNP和INDELs

经评估了Uni-C测序数据集的基因组覆盖率86.4%，测序深度14.6倍。

将在至少两个细胞中检测到的变体定义为候选SNPs/Indels，并将那些只在一个细胞中发现的SNPs/Indels归类为低置信度SNPs/Indels。

在过滤过程后，Uni-C对识别高置信突变体，鉴定SNPs/Indels的真阳性率上有明显提升，假阳性率有明显下降。且观察到碱基转变模式主要是从胞嘧啶(C)到胸腺嘧啶(T)的转变。

![](../../images/df9fcecc8a1356c9.webp)

3.单个肿瘤细胞中结构变异和ecDNA的检测

只考虑那些在至少两个细胞中观察到的结构变体作为候选结构变体，从而降低假阳性率，以验证Uni-C在单个肿瘤细胞中检测基因组结构变异的能力。

成功地识别了各种染色体内和染色体间的结构变异，并根据CNV数据进行了分类，强调了Uni-C在单细胞水平上捕获真正的基因组结构变异的可靠性。

经过筛选，发现至少结合四个细胞即可能够检测到在批量数据集中发现的79.2%的结构变体，以此评价Uni-C的敏感性。

表明将Uni-C的CNV数据与染色质相互作用信息相结合，可以准确地表征单细胞中焦点扩增的类型和拷贝数。

![](../../images/2e0dfe4cc01da30c.webp)

![](../../images/54398160df293a43.webp)

4.单克隆性细胞系UNI-C准确性的评估

分离单个MC38细胞以评价Uni-C在单细胞水平检测SNPs和Indels的准确性。通过8个Uni-C文库与PTA相比较。在过滤后，Uni-C确定了507,286个高置信度变体，每个细胞的平均真阳性率从36.8%增加到80.7%，平均假阴性率为1.9%，且Uni-C始终实现了略高于PTA的基因组覆盖率。这些结果表明，Uni-C的性能与PTA相当，在基因组覆盖率和单细胞水平的单核苷酸变异检测方面有一定的改进

![](../../images/a6c5aacbd2780458.webp)

![](../../images/5d899fe0e3b38190.webp)

5.研究CTCs的基因组改变

为了评估Uni-C在CTCs中的潜在临床应用，

以两个自发致瘤的KPC小鼠模型，胰腺癌患者来源的异种移植(PDX)小鼠，抗CD45磁珠从外周血中收集CTCs进行负浓缩三种来源，构建了19个Uni-C单细胞库，调查CTC的基因组变化，鉴定SNP和Indels。

Uni-C确定了12个结构变体。在CTC中，检测到75.0%的肿瘤组织结构变异，每个CTC平均识别约59.8%。且结合至少三个细胞能够检测到74.8%的肿瘤组织中存在的结构变异，统计差异最小。

![](../../images/fefcbe786bf31915.webp)

6.癌基因在癌组织中的局域扩增研究

在两个KPC小鼠的CTCs中没有发现显著的结构变异，且有一个细胞显示了显著的NF38基因的局部扩增。经GWIFA证实这种扩增是在Formoect DNA中进行的。

利用Uni-C数据集的分裂读数将扩增区域重构为完整的环状ecDNA结构，标志着ecDNA在单细胞水平上的三维分子结构的分辨率。

PanT24小鼠的七个CTC的分析中，在所有[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)和肿瘤组织中都观察到了MYC基因区域的局部扩增，GWIFA分析表明，MYC扩增区可能易位到该染色体。经使用8号和16号染色体的着丝粒探针以及MYC探针进行了荧光原位杂交(FISH)，证实，MYC基因确实以HSRs的形式在染色体内扩增，并定位于16号染色体

![](../../images/18818c9f482f513b.webp)

7.细胞周期各时相CTCs染色质结构的分析

一个CTCs中染色质相互作用矩阵显示染色体的长臂和短臂之间存在显著的相互作用，表明两个姐妹染色单体之间存在潜在的空间相互作用。其没有拓扑相关结构域(TADS)或其他高阶染色质构象可见，表明该特定细胞处于有丝分裂相。该CTC在B-B区显示出更强的相互作用，表明基因转录活性受到抑制。有丝分裂中的染色体缺乏间期细胞中交替的A/B室模式，大部分区域定位于B室，进一步表明有丝分裂细胞中转录活性降低。

相反，其他CTCs在[染色质相互作用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522998&idx=1&sn=843d378d3b679951ad3c8e5da7c32d87&scene=21#wechat_redirect>)矩阵中显示了明确的染色质高阶结构

基于染色质相互作用数据模拟了单细胞有丝分裂和间期的空间染色质结构。有丝分裂细胞中的染色体看起来更紧密，有清晰的轮廓和凝聚。相反，间期细胞的细胞核组织不太明确，不同染色质区域之间没有明显的边界，每个染色体的结构更宽松

![](../../images/5cb1ba446f4fe57d.webp)

8.CTCs基因突变的检测及新抗原的预测

PDX模型的CTC中，识别出的变异大多数是错义突变，单核苷酸变体(SNV)类型主要包括从T到C和C到T的转换。肿瘤增殖和凋亡相关基因，包括MUC家族基因MUC3A、MUC6、MUC16和MUC442，43显示出高突变负荷，这可能为未来的治疗策略提供信息。

KPC小鼠的CTCs的基因组变异显示频繁的MUC4突变，关键胰腺癌驱动基因(BRCA1、BRCA2、KRAS、TP53)44、45和错配修复(MMR)基因(MLH1、MSH6、PMS2)46的突变，以及MMR相关基因的突变。

使用pVACtools47预测了潜在的新抗原，证实两个小鼠品系都有22个新抗原的表达，并为其中10个新抗原合成了多肽。其中五个多肽通过分选小鼠脾中分离的γ+T细胞来刺激干扰素CD8的分泌，新抗原肽和CQ的联合治疗导致肿瘤体积和重量减少，表明有治疗应用的潜力。

![](../../images/9d626c32230f3836.webp)

![](../../images/c58492fb96d980a5.webp)

![](../../images/6414d4d5fd17eb71.webp)

**三、总结与展望**

1.主要内容

介绍胰腺癌诊疗困境与CTCs在液体活检中的重要地位，引出新型[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)多组学技术Uni-C。阐述Uni-C可同时解析多种基因组变异及染色质三维构象，强调其在胰腺癌PDX和自发肿瘤小鼠模型CTCs分析中的成果，包括变异检测、细胞周期判断及新抗原预测。

2.创新与意义

（一）技术创新

详细说明Uni-C在[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)水平实现ecDNA完整结构重建与拷贝数定量、用染色质构象差异判断CTCs细胞周期状态，以及整合三维基因组信息揭示结构变异功能影响这三大创新点。

（二）临床意义

阐述基于CTCs预测免疫原性新抗原并诱导T细胞应答、联合氯喹抑制肿瘤生长，以及PDX模型中CTCs替代组织活检的潜力，强调其对癌症早期诊断、治疗策略优化和预后监测的重要意义。

3.局限与未来方向

（一）当前局限

分析Uni-C技术在样本获取、检测成本、检测通量等方面可能存在的局限，以及在临床应用中面临的技术标准化、结果解读等挑战。

（二）未来方向

展望未来在技术优化、临床转化拓展，以及与其他技术联合应用方面的发展方向，如提升检测灵敏度与特异性、扩大临床样本验证范围、结合人工智能分析数据等。

![图片](../../images/2b97050f06208e7a.webp)

**欢迎交流**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家一起讨论。![图片](../../images/e43581b4f5118aad.webp)![图片](../../images/4ccf87cacd1143af.gif)您点的每个赞和在看，我都认真当成了喜欢
