---
title: "《Nature Methods》教你选择单细胞高变基因"
date: 2026-04-14
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537219&idx=1&sn=043692316d09cbfa24ececb3eb7166bf&chksm=9b3c2b13ac4ba205d8395dc2b34f438d63eccb373b0c39272d31f29984ca6f0d00eabebcf661#rd
albums: ["单细胞教程全收录"]
---

# 《Nature Methods》教你选择单细胞高变基因

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537219&idx=1&sn=043692316d09cbfa24ececb3eb7166bf&chksm=9b3c2b13ac4ba205d8395dc2b34f438d63eccb373b0c39272d31f29984ca6f0d00eabebcf661#rd
> 合集：单细胞教程全收录

**一、写在前面**

**Feature selection** （特征选择）是[scRNA-seq](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)分析中决定整合质量的关键前处理步骤。该研究于2025年发表于《 _Nature Methods》_ ，旨在系统评估不同特征选择方法对数据集整合（Integration）**与** 查询映射（Querying）性能的影响。在构建[大规模细胞图谱](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530984&idx=1&sn=41ea9b742095ea9f22e943fc7422a5f1&scene=21#wechat_redirect>)时，如何从数万个基因中剔除技术噪声（如[批次效应](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&scene=21#wechat_redirect>)）并保留核心生物学变异，是研究者面临的首要难题。作者通过对 20 多种方法在 10 个数据集上的基准测试，利用覆盖**批次校正、生物变异保持、映射质量、标签转移及未见群体检测** 这五个维度的指标，证明了高度可变特征（HVG）筛选在产生高质量集成中的核心地位。

基于此，本文先解读原文章再实操，为使用[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&scene=21#wechat_redirect>)或[Scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534702&idx=1&sn=f1531163f8f620b59cf63dfaa1c03e67&scene=21#wechat_redirect>)开展[多样本整合](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&scene=21#wechat_redirect>)及[单样本分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&scene=21#wechat_redirect>)的科研人员提供单细胞高变基因筛选的方法选择思路：**推荐优先采用[ Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&scene=21#wechat_redirect>)-vst（[R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530924&idx=2&sn=ba3b03a998e48de5cec08933b734d905&scene=21#wechat_redirect>)）或 [Scanpy-seurat_v3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533070&idx=1&sn=eb762b5b475695f418438d6628d8012f&scene=21#wechat_redirect>)（[Python语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&scene=21#wechat_redirect>)）方法筛选高可变基因，并在此基础上进行降维与[细胞分群](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504024&idx=1&sn=143c0ec4d94b8fca0a4a47d3dc24415b&scene=21#wechat_redirect>)；其中选取 2000 个高变基因即可获得理想的分群效果**。

如果你希望有人真的手把手教你学单细胞：

[R语言scRNA-seq数据分析全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535927&idx=2&sn=86947f0522de0d9785865bd24115b002&scene=21#wechat_redirect>)

[Python版scRNA-seq数据分析全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)指导、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469&token=1729645779&lang=zh_CN#wechat_redirect>)、自测数据个性化分析辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、文献解读**

文献标题：Feature selection methods affect the performance of scRNA-seq data integration and querying

DOI: 10.1038/s41592-025-02624-3

2.1 摘要

单细胞转录组学的可用性使得参考细胞图谱的构建成为可能，但其实用性取决于数据集整合的质量和新样本的定位能力。以往基准测试比较了集成方法，并建议特征选择能提升性能，但尚未探讨如何选择最佳特征。本文，作者对单细胞RNA测序整合的特征选择方法进行了基准测试，利用超越批量校正和生物变异保持的指标，评估查询映射、标签转移及未见群体的检测。作者通过证明高度可变的特征选择对产生高质量集成有效，进一步指导了所选特征数量、批次感知特征选择、谱系特定特征选择与整合以及特征选择与整合模型相互作用的影响。这些结果对于从事大规模组织图谱研究、使用图谱或整合自身数据以解决具体生物学问题的研究人员具有重要参考价值。

2.2 前言

如今，许多生物研究人员都能够使用转录组学技术。随着单细胞RNA测序数据集的数量不断增加，分析方法也不断得到改进，我们观察到研究趋势正在从探索性实验转向多样本数据分析。这一趋势表现为：越来越多的研究会设计专门的实验来探讨特定现象，或检测不同条件下的差异；同时，也有更多研究致力于系统地分析组织内部的细胞异质性。更多的样本数量确实有助于更深入地开展生物学研究，但这也带来了新的挑战 —— 如何[将这些样本有效地整合起来](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532349&idx=1&sn=59c0f14043906ff50c56dea3b16e9200&scene=21#wechat_redirect>)，以消除技术操作带来的差异，同时保留那些具有生物学意义的变异信息。对于那些旨在构建大规模人类组织图谱的研究项目而言，高质量的样本整合尤为关键。因为要全面反映组织中的细胞异质性，就需要收集来自不同地区、不同个体的样本，这些样本需要通过不同的方法从不同的器官组织中获取，并且还需要使用多种不同的技术手段对其进行分析。

许多计算科学家已经解决了整合问题，目前至少有250种单胞整合工具可用。研究评估了某些方法的表现，形成一套用于评估集成性能的既定指标。尽管这些方法已经得到了比较，但那些可能影响整合结果的前处理步骤在很大程度上被忽视了。其中一个受到了一定关注的步骤是特征选择。相关基准测试表明，使用变异程度较高的基因通常能够获得更好的整合效果；然而，这项研究仅考察了一种常用的特征选择方法。与其他分析步骤（如聚类分析）不同，目前尚未有人评估哪种特征选择方法才是最适合用于整合分析的。当考虑如何将整合后的结果作为参考来分析其他样本时，还会出现一些其他问题：选择某些特征确实可能使参考样本的整合效果更好，但同时也会导致所建立的整合模型忽略那些对于理解其他样本而言至关重要的生物变异因素。

这项研究评估了特征选择在整合scRNA-seq样本以及利用这些整合后的参考数据来分析查询样本时的影响。我们通过五类不同的评估指标，对20多种特征选择方法的性能进行了测试：这些指标包括去除批量效应、保留生物变异信息、提高查询样本与参考数据之间的映射质量、确保标签转移的准确性，以及检测未知基因群体的能力（扩展数据图1）。这套严谨的基准测试流程所获得的结果，对于希望整合自身数据集或构建参考图谱的研究人员而言，具有重要的参考价值（扩展数据图2）。这些结果将有助于提升整个研究领域的资源质量，并促进更深入的生物学研究。

![](../../images/8a217f81b02636b8.webp)

扩展数据图1

![](../../images/0e743dbafc178742.webp)

扩展数据图2

2.3 结果

2.3.1 指标选择对于可靠的基准测试至关重要

在这项研究中，作者收集了多种指标，这些指标涵盖了集成与查询映射的不同方面。虽然衡量各种因素非常重要，但其中许多指标的具体表现特征尚未得到充分研究。在作者的研究背景下，这一点尤为重要，因为需要使用这些指标来评估特征选择方法对系统性能的影响，而不是用来比较不同的整合方法。因此，作者专门设置了一个指标选择环节，以便对各种指标进行评估，并决定最终使用哪些指标来进行基准测试。这一环节的目的是选择那些能够有效衡量系统性能的指标，那些与技术因素关联度不高且不会造成重复计算的指标。

作者通过为每个数据集随机选择不同大小的特征集以及高变基因集（基于[scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505248&idx=2&sn=18995c7248ca6f13b61edfef24208ae1&scene=21#wechat_redirect>)软件实现的[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534661&idx=1&sn=16872e942170ace88f26deb0ea6c4b34&scene=21#wechat_redirect>)算法）来进行指标选择，执行整合与映射，计算指标得分，并比较结果（图1a）。通过随机基因集，作者计算了每个数据集与整合组合的得分范围。同时，作者还利用随机集计算了指标与数据集技术特征之间的相关性（例如特征数量、参考细胞数量、参考标签数量和批次、查询细胞数量、查询批次数量以及未见标签数量）。对于高变基因集，作者计算了指标得分与所选特征数量的相关性，因为随机特征集没有内在顺序（前100个特征并不比后100个特征更具信息量）。理想的指标应能准确测量其设计目标，在整个输出范围内返回与数据技术特征无关且与其他指标正交的得分。图1b总结了指标评估的结果。

![](../../images/8716ea4ae404a9c5.webp)

图1

基于这些结果，作者选择了一组用于评估特征选择方法的指标。作者发现，一些指标（例如批次平均轮廓系数batch average silhouette width（Batch ASW），以及 k-nearest neighbors（kNN）相关性）在很大范围的特征集合变化下几乎没有波动。然而，从应用角度看，这种稳定性可能是优势（比如评估方法鲁棒性），但也可能是劣势（比如无法区分不同特征选择策略的优劣）。这种现象并不总是容易解释。举例来说，细胞类型局部逆辛普森指数（cell-type local inverse Simpson’s index，cLISI）的自然取值范围是从0到数据集中标签的数量，随后被重新缩放到0到1之间，从而压缩了观测到的数值范围，使得即便是很小的差异也具有信息量。

在考察各指标与所选特征数量之间的相关性时，作者发现大多数指标与特征数量呈正相关，平均相关系数约为 0.5。少数指标（如local structure和kNN相关性）与特征数量之间表现出更强且更稳定的关联。相比之下，映射（mapping）类指标通常呈负相关。这种关系可能源于：较小的特征集会产生噪声更大的整合结果，使得不同细胞群体发生混合。在这种情况下，对查询数据的映射不需要非常精确——不需要精准定位到某一种细胞的位置，只要能映射到这个混合群体的范围内，就可以得到较高的映射分数。

由于这里涉及的数据集数量相对较少，且各种技术因素会在不同数据集之间相互关联（通常来说，数据集中的细胞数量越多，相应的批次和标签数量也就越多）。这种关联性导致无法区分是 “细胞多”、“批次多”， 还是 “标签多” 单独造成了指标分数的变化。因此这些技术因素对各项指标评分的影响较难被准确解读。作者观察到，更复杂的数据集通常会导致所有指标的得分降低（扩展数据图3）。例外的是Milo和Uncertainty指标。对于Milo而言，目前尚难判断其得分与技术因素之间的正相关性究竟是由于数据量增加的整体效应，还是由某些特定特征驱动的结果。对于Uncertainty指标，更可能的解释是其所使用的分类器模型校准不足，在面对更复杂的数据集时表现出更低的确定性（从而给出更高的得分）。Uncertainty指标的定义规则—— 它的分数高低直接对应模型分类结果的“不确定性程度”，而非分类的“准确性”。而这一现象与具体的技术因素无关。要准确评估技术性数据集特征的影响，需要更多的数据集，使每个因素能够被独立地变化，可能需要借助模拟研究来实现。

![](../../images/759102b7006f166f.webp)

扩展数据图3

特征选择方法评估指标的筛选原则——核心逻辑是避免指标内的高相关性导致结果偏倚，如果选择多个高度相关的指标，这些指标本质上是在重复衡量同一个维度的性能，会导致最终结果被这个维度“过度加权”，从而产生偏倚。同时依据指标的实际关联特性调整其分类归属，最终确定一套覆盖不同评估维度且相互独立的指标集合。整合（生物学）类[Integration (Bio)]中ARI、bARI、NMI、bNMI、cLISI 等多个指标高度相关 仅筛选其中一个子集纳入最终指标集，剔除冗余指标。分类类指标[Classification metrics]中所有指标的分数趋势都极为相似，相关性极强，选择代表性指标即可。由于指标间一致性太高，选一个或全选对最终结果影响很小。

次要考量因素是指标类型间的相关性会干扰结果解读。除了同一类别内的指标相关性，不同类别指标之间的相关性也会影响解读，这一点的核心诉求是：希望不同类型的指标能独立反映对应维度的性能，方便分别总结各维度的表现。如果两类本应衡量“对立/不同维度”的指标出现强相关性，就会混淆不同维度的信号，导致无法清晰判断模型在某一特定维度的优劣。

特殊指标的分类调整：依据实际相关性修正初始归类。部分指标的初始分类（根据原文献定义的用途）和实际表现（与其他指标的相关性）不匹配，作者据此调整了它们的归属，典型案例有两个：

案例 1：kBET 指标

初始分类：整合（批次）类 [Integration (Batch)]，本应衡量批次效应的消除效果。

实际问题：它同时与衡量 “生物变异保守性” 的指标高度相关。

处理结果：将其排除在研究之外，因为它会混淆“批次效应消除”和“生物特征保留”两类信号，无法明确区分指标反映的具体维度。

案例 2：graph connectivity（图连通性）指标

初始分类：原作者将其定义为批次校正指标。

实际表现：与整合（批次）类的其他指标负相关，反而与整合（生物）类指标正相关。

处理结果：保留该指标，但将其重新归类到整合（生物）类，确保后续分析中指标分类与实际评估维度一致。

最终成果：确定多维度、低冗余的指标集合：

基于上述相关性分析和分类调整，作者最终选定了一套覆盖5个核心维度的指标集，具体包括：

（1）Integration (Batch) 3类：batch principal-component regression (Batch PCR), cell-specific mixing score (CMS) 和 integration local inverse Simpson’s index (iLISI)

（2）Integration (Bio) 6类：isolated label ASW, isolated label F1 , bNMI, cLISI, local density factor difference (ldfDiff) 和 graph connectivity

（3）mapping 4类：Cell distance12, Label distance, mapping local inverse Simpson’s index (mLISI) 和 query local inverse Simpson’s index (qLISI)

（4）classification 3类： F1 (Macro), F1 (Micro) 和 F1 (Rarity)

（5）unseen population 3类：Milo, Unseen cell distance 和 Unseen label distance

2.3.2 利用基线来有效地对各项指标进行量化分析与总结

公平比较不同特征选择方法的评估指标分数，作者采用了基于基线方法的指标缩放策略，同时定义理论极值参考、计算分类汇总分数与加权总分数，最终实现指标的标准化解读。需要缩放的原因在于：①不同指标的有效取值范围不同（比如有的指标取值是0–1，有的是0–10，原始分数的绝对值不具备可比性）；②与数据集的交互差异（同一个指标在不同复杂度、不同类型的数据集上，分数分布规律不一样）。因此，必须对每个数据集的指标分数进行缩放，让所有指标在同一数据集上的取值范围一致，才能消除指标本身和数据集的固有差异，实现公平比较。作者借鉴了单细胞分析领域权威项目的思路，选定4类具有代表性的基线方法：

（1） 所有特征：使用数据集的全部特征进行整合，代表 “无特征筛选” 的基准表现；

（2） 2000个高度可变特征：基于[Scanpy-Cell Ranger](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521051&idx=1&sn=e2ab820001013bae6e35310e27897086&scene=21#wechat_redirect>) 的批次感知方法筛选，是领域内公认的最佳实践，筛选出了2,000个变化幅度较大的特征参数；这种方法是公认的、常用的、符合最佳实践标准的分析方法；

（3） 随机选取的500个特征值：随机选 5 组特征集，取分数平均值，提供 “随机筛选” 的对照基准；

（4） 200个稳定表达特征（scSEGIndex）：筛选稳定表达的基因，这类特征通常无法捕捉生物学或批次信号。 作为阴性对照，代表 “无效特征选择” 的基准；

所有基线方法都用scVI工具进行数据整合，保证了分析流程的一致性。这4类方法的多样性，足以覆盖单个指标在某一数据集上的全部有效分数范围，为后续缩放提供了可靠的参考依据（图2a）。

![](../../images/44e5eefac19de7dd.webp)

图2

作者以scIB胰腺数据集为例，详细说明了缩放流程，核心逻辑是以基线方法的分数极值作为锚点，将原始分数映射到相对区间：

（1）确定基线极值：对每个数据集的每个指标，计算 4 类基线方法得到的分数的 最小值（min） 和 最大值（max）。

（2）引入理论参考点：除了真实基线，还定义了两个理论方法作为补充：Good方法（理论上在所有指标类型上表现最优，用于模拟 “超越所有基线” 的情况）和Bad方法（理论上在所有指标类型上表现最差，用于模拟“劣于所有基线”的情况。

（3）执行缩放计算：将原始指标分数相对于基线的 min 和 max 进行缩放。缩放后分数的特点：

若方法表现 优于所有基线 → 缩放分数 > 1（对应 Good 方法的情况）。

若方法表现 介于基线之间 → 缩放分数在 0–1 之间。

若方法表现 劣于所有基线 → 缩放分数 < 0（对应 Bad 方法的情况）。

这种缩放方式的优势在于：超出基线范围的分数依然有明确的解读意义，能直观判断方法是否突破了现有基准的表现边界。

（4）汇总分数的计算：从单指标到整体评估。缩放完成后，作者通过两步计算实现从 “单指标分数” 到 “方法整体表现” 的量化。对同一类别的指标（如整合批次类、整合生物类、映射类等），计算其缩放分数的平均值，得到该类别的汇总分数。这一步能反映方法在某一特定评估维度的综合表现。加权总分数则计算所有类别汇总分数的 加权平均值，得到方法的最终整体分数。

（5）权重设计的原则：保证评估维度的均衡性。作者明确了权重分配的核心逻辑为赋予 “参考集整合” 和 “查询集映射” 两大核心任务 同等重要的权重。在每个核心任务内部，不同指标类型的权重也保持一致。同时强调，整体分数虽有参考价值，但后续分析仍会展示各类别的单独分数——因为不同应用场景下，对“批次消除”、“生物特征保留”、“映射精度”等维度的优先级需求不同，单独分数能满足更灵活的解读需求。

综合评分来看：Scanpy-Cell Ranger 的批次感知方法筛选2000个高度可变特征综合分数最高。

2.3.3 所选特征的数量对单细胞数据整合、映射等任务性能的影响

特征选择的方法和数量都会影响整合与映射的效果。理论上需要对每种特征选择方法都测试全范围的特征数量，但这样会带来巨大的计算负担，无法实现。折中方案是研究者仅针对常用特征选择方法开展测试，涵盖两类：①工具包内置方法如来自 Seurat 和 Scanpy 的经典算法；②简单基础方法如筛选高表达基因、高可变基因的方法。

特征数量对不同评估指标的影响规律如图3a。作者用标准化得分（z-score）衡量不同特征数量下的指标表现，并将指标分为不同类别，发现了截然不同的趋势：

（1）整合（批次）指标Integration (Batch)：小特征集（<500）得分最高，特征数增加后得分持续下降。小特征集容易构建 “噪声整合嵌入”—— 细胞在降维空间中混为一团，批次效应被掩盖，但细胞类型的区分度也会完全丧失，因此其他指标得分会降低。

（2）映射指标 Mapping：趋势与批次整合指标类似，但变化幅度更缓和，特征数≥500后得分趋于均值。映射效果受批次混合程度影响，但对细胞类型特异性的依赖度高于纯批次整合指标。

（3）分类指标 Classification + 未见种群指标 Unseen populations：得分先随特征数增加而上升，基因数目在2000达到峰值后趋于平稳。更多特征能提供更丰富的细胞类型特异性信息，提升[分类和未知细胞类型识别](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&scene=21#wechat_redirect>)的准确率；但特征数达到阈值后，新增特征的边际效益会降低。

（4）整合（生物学）指标 Integration (Bio)：得分随特征数一开始会有一定增加，但是达到2000以后随增加而下降。过多特征会引入冗余的生物学或技术噪声，干扰真实的生物学差异信号，降低整合后的生物学意义。

整体分数的趋势：和生物学相关类别（整合生物、分类、未知群体）的趋势一致，在 500–5000 个特征区间达到峰值 —— 这个区间是 “批次消除” 和 “生物特征保留” 的最优平衡点。

![](../../images/6f115a40d28e8693.webp)

图3

尽管在每一类指标中都可以观察到清晰的总体趋势，但仍然存在显著的变异。图3中的后续各子图展示了在不同数据集和方法之间计算得到的平均标准化数值。我们可以看到，不同方法在各个数据集之间总体上具有较好的一致性（图3c）。复杂方法Seurat-VST、scanpy-SeuratV3以及scanpy-Seurat在略高数量的特征时（约2000）达到峰值；而简单方法statistic-Variance和statistic-Mean在Integration(Batch)和Integration(Bio)类别中，在较少特征数量时达到峰值，但在分类（classification）和未见群体（unseen populations）类别中，则在较多特征数量时达到峰值（扩展数据图4）。这一模式表明，简单方法筛选的特征在参考集中能较好捕捉信号，但在查询集中的泛化能力弱，需要更多特征才能弥补信息缺口。

![](../../images/a1abf135a5861a79.webp)

扩展数据图4

当按数据集分组分析时，最优特征数量的差异更明显（图3b及扩展数据图4）。核心规律由数据集复杂度决定。细胞数量最少的两个数据集（splat和scIB pancreas）表现出不同的模式。对于模拟的splat数据集，只需要较少的特征即可捕获其中存在的变异；相比之下，scIB pancreas数据集的最高得分则与更多特征数量相关。这些差异反映了两个数据集本身的性质：splat模拟生成的数据复杂度低于真实数据，而scIB pancreas数据集包含来自多种技术的数据，对整合提出了更高的挑战。

大型真实数据集（胎儿肝脏fetal liver）数据集同样需要更多特征，才能在查询相关类别中获得较高的得分；在映射（mapping）和未见群体（unseen populations）类别中，当使用全部特征时获得了最高的平均得分。这一趋势表明，对于该数据集而言，从参考数据中选择的特征集合并不能很好地捕获查询数据中的信息。尽管这种趋势不那么显著，但在所有数据集中均可观察到：相较于Integration(Bio)类别，在分类和未见群体类别中，需要更多特征才能达到较高得分；然而，使用全部特征所带来的性能提升也存在上限，说明可获取的额外信号是有限的。额外信号达到饱和的特征数量尚不明确，并且很可能因数据集中所包含的生物学和技术多样性不同而有所差异。

基于上述分析，在后续评估中，作者对大多数方法统一使用2,000个特征，因为这一数量在不同数据集、方法和指标类别中都能稳定地产生较高得分。例外情况包括那些动态决定特征数量的方法（Anticor、DUBStepR、NBumi、Seurat-MVP和triku），以及单细胞投影非负矩阵分解方法（single-cell projective non-negative matrix factorization，scPNMF），其文档建议使用少于其他方法的特征数量，因此我们对这些方法使用200个特征。

2.3.4 高变异特征方法与监督方法表现良好

在确定了所使用的特征数量之后，作者对不同的特征选择方法进行了比较。结果显示能够在所有数据集上成功运行大多数方法。然而，NBumi在Reed乳腺数据集上未能在24小时内完成。scPNMF在Human Lung Cell Atlas（HLCA）、HLCA immune、HLCA epithelial、Human endoderm以及Reed乳腺数据集上要么内存消耗超过400GB，要么未能在24小时内完成。Anticor则在Human endoderm数据集上产生了一个未预期的错误。

图4a展示了各指标类别的总体结果，并按照scVI整合条件下跨数据集的平均总体得分进行排序（扩展数据图5a）。有多种方法获得了相似的平均总体得分。Wilcoxon方法是唯一使用细胞标签进行特征选择的有监督方法，其平均总体得分最高。但是，数据集间的性能波动大——说明有监督方法的效果依赖数据集特性，即便用相同特征基因评估，也未必适用于所有数据集，可能需要针对不同数据集调整选特征的数量。

Seurat-VST总排名最高，且这类方法的性能稳定性远优于Wilcoxon，不同数据集上的表现更一致。证明无监督的高变特征筛选是单细胞数据分析中普适性更强的策略。triku总分与高变特征方法相当，但存在 “重批次校正、轻生物变异保留” 的偏向性 —— 筛选的特征更利于消除批次效应，但对细胞类型等生物学特征的保留能力较弱。

![](../../images/982412605c03bba0.webp)

图4

作者通过[Jaccard指数](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504403&idx=5&sn=12e5a17af1cc976ce78876b51cd241ca&scene=21#wechat_redirect>)衡量不同方法所选特征的重叠度（对应图4b、4c），核心发现有两点：多数方法的特征重叠度低：绝大多数方法组合的平均Jaccard指数低于0.5——说明不同方法筛选特征的逻辑差异大，捕捉的数据集变异维度不同。例外情况：Seurat-VST与scanpy-SeuratV3，两者选出的特征完全相同。原因是由于它们是同一算法的不同编程语言实现（分别对应 R 和 Python），一致性验证了算法的可靠性。补充：两者的性能差异仅来自整合或指标计算过程中的随机性，与特征选择无关。

部分重叠的情况在scanpy-Seurat与Seurat-MVP。差异原因在于，虽基于同一思路，但scanpy版支持手动指定特征数量，Seurat版则通过阈值动态选特征；同时预处理步骤的不同也导致了特征重叠度和性能的差异。更少的特征足够完成参考集的整合与批次校正，但适量增加特征（到 2000）能提升方法在查询集上的泛化能力，对分类、未知群体识别这类任务更重要。

核心共识特征的存在：多数数据集上，有500–1000个特征被至少20种方法共同选中（对应图4c）。这些特征是数据集的核心信息载体，对有效整合和映射至关重要。对于差异的解释是：性能相近的方法间仍有大量特征不重叠，是因为基因表达存在冗余性 —— 多个基因可携带同一生物学过程的信息，不同方法只是选择了冗余集中的不同子集。

批次感知特征选择则发现效果不稳定，未展现出普适优势（图4e）。批次感知特征选择的核心逻辑是：先按批次分别筛选特征，再合并各批次的共有特征（通常选被多数批次选中的特征）。设计初衷是避免筛选出“仅在批次间变异、无生物学意义”的特征，理论上更精准。作者通过对比“批次感知版”与“标准版”scanpy方法的性能，得到以下结论：从整体分数看，批次感知版和标准版的差距很小。从细分场景看，效果随数据集、指标类型波动极大：正面案例：对HLCA（Immune）数据集，提升了 “未知群体检测” 的分数。负面案例：对 HLCA（Epithelial）、Human endoderm、scIB 胰腺数据集，反而导致 “未知群体检测” 分数显著下降。

![](../../images/a6fbd115b21ba0fb.webp)

扩展数据图5

2.3.5 谱系特异性特征选择与整合

在大规模单细胞数据整合项目中，一直存在一个关键问题，即两种整合策略的取舍：

（1）全组织整合：整合所有细胞类型的全部数据，优势是覆盖完整的细胞状态空间；

（2）谱系特异性整合：先按细胞谱系（如免疫细胞、上皮细胞）划分数据集，再分别整合，初衷是降低数据复杂度，筛选更具谱系针对性的特征。

这里作者以 HLCA（人类肺细胞图谱）数据集的3个版本（全组织+不同谱系子集）为对象，从多个维度对比两种策略的效果（图5）。

作者通过排名对比和Jaccard指数分析，得到两个关键结论：

（1）方法性能排名：无显著差异。谱系子集上各特征选择方法的排名趋势，和全组织数据集上的趋势基本一致；没有任何一种方法能在谱系子集上 “持续优于” 全组织数据集的表现。说明降低数据复杂度并没有给方法性能带来稳定增益。

（2）特征重叠度：优秀方法具有“自适应能力”。谱系子集与全组织数据集之间的特征重叠度，并没有高于不同数据集之间的重叠度。更重要的是：排名靠前的方法，特征重叠度反而更低。这一现象的解读是：优秀的特征选择方法能根据数据集的特性（全组织 / 谱系子集）自主筛选适配当前数据的特征，而非机械复用全组织的特征集——这正是方法鲁棒性的体现。额外发现：免疫细胞子集和上皮细胞子集之间的特征重叠度，低于各自与全组织数据集的重叠度——说明不同谱系的特征偏好差异显著。

（3）标记基因的选择比例（谱系特异性）：未提升标记基因富集。谱系特异性整合的核心预期是筛选的特征会更富集对应谱系的已知标记基因（Marker Gene）。但实验结果并不支持这一预期，标记基因选择比例普遍偏低。对HLCA的4个谱系（内皮、上皮、免疫、基质），所有方法选中的标记基因平均比例仅0.38（中位数0.39，第一四分位数仅0.04）——说明多数特征选择方法筛选的特征，和已知标记基因的重合度不高。比例低的原因可能是基因表达存在信息冗余（功能相关的基因可以携带相同的生物学信号，方法可能选择了冗余集中的非标记基因）；特征选择与标记基因检测的目标不同（特征选择的目标是“最大化整合/映射性能”，而标记基因检测的目标是 “区分细胞类型”，两者的筛选逻辑存在天然差异。

（4）未知群体检测能力：在全组织整合更具优势。由于谱系子集和全组织数据集的细胞、标签不同，直接对比指标分数不具备可比性。因此作者聚焦Milo分数（衡量未知群体检测能力）（图5d），针对单个未知标签做精细化分析，得到了最关键的结论，谱系子集的Milo分数显著更低。背后的逻辑可能由于全组织整合提供了更丰富的细胞状态多样性，让整合模型能学习到更完整的细胞空间特征。而谱系子集的细胞类型单一，模型的泛化能力受限，因此对新的未知细胞群体的识别能力更弱。

![](../../images/cab6bdbbe2656067.webp)

图5

2.3.6 特征选择方法与整合方法之间的交互作用

作者首先明确了本研究的核心定位：核心目标是评估特征选择方法的优劣，而非比较整合方法。加入scANVI和Symphony两种整合方法的原因有两个，一是评估“特征选择方法”与“整合方法”之间是否存在“交互效应”——即某类特征选择方法是否对特定整合工具更友好；二是探究“生物监督信息”的作用：scANVI 是 scVI 的半监督版本（[引入细胞标签信息](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497669&idx=3&sn=ac3408c7dd28425426d954f81d283252&scene=21#wechat_redirect>)），可以对比 “监督” vs “无监督” 整合对特征选择结果的影响。图6显示了每种整合方法的平均得分和排名，以及scANVI和Symphony与scVI的性能差异。

![](../../images/101dc7f71d896d45.png)

从方法排名的宏观视角看不同整合方法下，特征选择方法的排名没有出现明显变化。说明特征选择方法的优劣具有一定的 “普适性”，不会因整合工具的更换而发生颠覆性反转。存在一个轻微的趋势：在scVI上排名靠前的特征选择方法，在scANVI/Symphony上的排名会小幅下降；在scVI上排名靠后的方法，排名会小幅上升。作者给出了两种可能的解释：①特征选择 - 整合方法的交互作用，部分特征选择方法的优势依赖scVI的算法特性，换用其他整合工具后优势被削弱；②均值回归效应：整合过程和指标计算存在随机性，极端排名（极高/极低）有向平均水平回归的自然趋势。

![](../../images/30e9efb76132179a.webp)

扩展数据图8

分方法性能差异体现在scANVI提升生物维度，Symphony弱于基准（图6b）。scANVI半监督信息弥补特征局限，生物维度性能提升。相比 scVI，scANVI 在 Integration (Bio)（生物特征保留） 维度上，对部分特征选择方法（scanpy-Seurat (batch=false)、Seurat-MVP、Brennecke、DUBStepR、全特征）有显著性能提升。关键原因是scANVI引入了细胞标签的监督信息，这种生物学先验知识可以“弥补特征选择的局限性”。即便是筛选质量一般的特征集，监督信息也能引导模型更精准地捕捉生物特征。但是scANVI在Integration (Batch)（批次校正）维度的性能略有下降，但这种权衡是可接受的。因为mapping（映射）分数同步提升—— 说明 “保留更多生物信息” 并没有牺牲查询集向参考集的映射能力，反而有所增强。这对单细胞数据分析的核心目标（保留细胞类型差异）具有重要价值。

Symphony整体性能弱于scVI。除了mapping分数外，Symphony在所有其他指标类别的性能都低于scVI。最显著的短板在unseen population（未知群体检测）维度，对scVI上排名靠前的特征选择方法，Symphony的分数下降最明显。即使用相同的特征集，Symphony也无法识别出那些能被scVI/scANVI检测到的新细胞群体。背后的本质原因是Symphony的算法特性：它是基于 “参考映射” 的整合工具，模型的学习范围受限于参考集的细胞状态空间，对超出参考范围的未知群体天然不敏感；而scVI/scANVI 是无监督/半监督的生成模型，能学习更灵活的细胞状态分布，更适合发现新群体。

2.4 讨论

本文作者评估了24种特征选择方法的变体，在10个数据集上测试了1700个特征集，完成6000余次整合分析，生成14万+指标分数；同时通过严格的指标筛选流程，确定了2000个特征是跨数据集的最优参数。

最优方法是高变特征选择法（无监督）：基于方差稳定变换的方法（Seurat-VST/scanpy-SeuratV3）排名第一。这验证了单细胞数据分析的“通用最佳实践”——无监督高变特征筛选是普适性最强的策略。这类方法的优势在于稳定性强，跨数据集表现一致，无需依赖先验标签。表现较好的其他方法有Wilcoxon（标签指导的标记基因法），其性能优异，但数据集间波动大——原因是它是有监督方法，依赖细胞标签，而标签在整合前通常不可得，限制了其适用场景。triku方法排名靠前，但存在“重批次校正、轻生物特征保留”的偏向性——适合以批次消除为核心目标的研究，但需权衡生物学信息的损失。

整合方法的交互效应显示不同整合方法下，特征选择方法的排名没有颠覆性变化。仅存在“均值回归”的小幅波动——说明优秀特征选择方法的普适性。显示监督信息有增益。scANVI（半监督）vs scVI（无监督）：scANVI在所有指标类别都有小幅提升，尤其是生物特征保留维度——证明加入细胞标签的先验知识，能弥补特征选择的局限性，且不会牺牲映射性能，是更优的整合选择。Symphony（参考映射）vs scVI：Symphony除映射分数外，其余指标均低于scVI，未知群体检测能力显著不足——本质原因是其算法受限于参考集的细胞状态空间，适合“已知群体的精准映射”，但不适合“新群体发现”的研究目标。

谱系特异性整合的结论显示全组织整合更优。针对“谱系vs全组织整合”的开放问题，作者给出了阶段性结论：谱系子集的整合没有展现出优势——方法排名与全组织一致，特征重叠度低（优秀方法能自适应谱系特性），且Milo分数更低（未知群体检测能力弱）。全组织整合因覆盖更完整的细胞状态空间，更利于新群体发现——这是单细胞图谱构建的核心目标。研究局限：未探究“谱系特征能否提升全组织整合性能”，也未分离“特征选择”与“整合”的独立效应——这是未来研究的切入点。

最后作者也坦诚指出实验设计的不足。特征数量测试的局限性，仅对部分常用方法测试了不同特征数量，而非所有方法——原因是全量测试的计算成本过高；且受限于数据集数量，无法将“最优特征数”与数据集的具体技术属性（批次数、标签数）建立明确关联。方法层面局限性体现在研究期间有新的特征选择方法发表，未纳入评估，无法排除这些方法提升性能的可能。

****三、实操流程****
```
3.1 数据下载
```
```
下载地址：https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163973
```
```
之前我们在100个小时沉浸式学会scRNA-seq数据分析全程班中对这篇文章进行过完整的文章复现，感兴趣的小伙伴可以阅读scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性哦~
```
```
3.2 包加载
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library(Seurat)library(dplyr)library(harmony)library(ggsci)library(sceasy)library(png)library(ggplot2)library(patchwork)library(ggthemes)library(ggpubr)library(UpSetR)library(gridExtra) library(grid)      library(VennDiagram)
```

  *   *   *

```r
#定义后续要使用的配色color <- c(pal_d3()(7),pal_aaas()(7),pal_uchicago()(7),pal_jama()(7))color
```
```
##  [1] "#1F77B4FF" "#FF7F0EFF" "#2CA02CFF" "#D62728FF" "#9467BDFF" "#8C564BFF"##  [7] "#E377C2FF" "#3B4992FF" "#EE0000FF" "#008B45FF" "#631879FF" "#008280FF"## [13] "#BB0021FF" "#5F559BFF" "#800000FF" "#767676FF" "#FFA319FF" "#8A9045FF"## [19] "#155F83FF" "#C16622FF" "#8F3931FF" "#374E55FF" "#DF8F44FF" "#00A1D5FF"## [25] "#B24745FF" "#79AF97FF" "#6A6599FF" "#80796BFF"
```
```
3.3 Seurat整合分析流程
```
```
3.3.1 数据质控
```

  *   *   *   *   *

```r
# 原数据有6例样本，这里我们只选择其中NF1和NF2两例样本用于测试NF1_path <- "data/GSE163973_RAW/NF1_matrix/"NF2_path <- "data/GSE163973_RAW/NF2_matrix/"datadir <- c(NF1_path,NF2_path)datadir
```
```
## [1] "data/GSE163973_RAW/NF1_matrix/" "data/GSE163973_RAW/NF2_matrix/"
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
data <- list()for (i in 1:2) {  # 依次读取表达矩阵  scdata <- Read10X(data.dir = datadir[i])  sample_name <- strsplit(datadir[i],'\\/')[[1]][3]  %>% strsplit(.,'_') %>% .[[1]] %>% .[1]  print(paste0('--------',sample_name,'正在处理--------'))  scobj <- CreateSeuratObject(counts = scdata,                             project = sample_name,                             min.cells = 3,                             min.features = 200)  # 线粒体基因表达比例计算  scobj[["percent.mt"]] <- PercentageFeatureSet(scobj, pattern = "^MT-")  # 参考原文数据质控  scobj <- subset(scobj, subset = nFeature_RNA > 200 & nFeature_RNA < 6000 & percent.mt < 15)  scobj <- NormalizeData(scobj, normalization.method = "LogNormalize", scale.factor = 10000)  scobj <- FindVariableFeatures(scobj, selection.method = "vst", nfeatures = 2000)  data[[i]] <- scobj  names(data)[i] <- sample_name}
```

  *   *

```r
# 合并多个样本的seurat对象scobj <- merge(x=data[[1]], y = data[-1], add.cell.ids
```

3.3.2 降维分群

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 高变基因scobj <- FindVariableFeatures(scobj, selection.method = "vst", nfeatures = 2000)# scalescobj <- ScaleData(scobj)# PCA降维scobj <- RunPCA(scobj, features = VariableFeatures(object = scobj),reduction.name = "pca")# harmony去批次scobj <- RunHarmony(scobj,reduction = "pca",group.by.vars = "orig.ident",reduction.save = "harmony")# 邻近计算scobj <- FindNeighbors(scobj, reduction = "harmony", dims = 1:30)# 细胞分群scobj <- FindClusters(scobj, resolution = 0.5)# UMAP降维（tSNE也可以）scobj <- RunUMAP(scobj, reduction = "harmony", dims = 1:30,reduction.name = "umap")
```

  *

```
# saveRDS(data,"result/data.rds")
```

  *

```
# saveRDS(scobj,"result/scobj.rds")
```

3.3.3 细胞注释

接下来使用的marker基因全部来源于原文提供。

  *

```r
scobj <- readRDS("result/scobj.rds")
```

  *

```
table(scobj@meta.data$orig.ident)
```

  *   *   *   *   *   *   *   *

```
# 小提琴图展示数据质量VlnPlot(scobj,        # 指标：细胞表达基因数目、counts数目和线粒体基因表达比例        features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3,pt.size = 0,        # 指定颜色        cols=color,        # 分样本展示        group.by = "orig.ident")
```

![](../../images/f4c1c6fd475acb55.webp)

  *   *

```
# 分群情况DimPlot(scobj, reduction = "umap",cols=color)
```

![](../../images/87b5abfbb6af1cc7.webp)

  *   *

```
#C2/4 = EndothelialVlnPlot(scobj, features = c("CLDN5",'FLT1','SELE',"PECAM1"),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/18a74c634597ad9d.webp)

  *   *

```
#C0/1/6/7 = FibroblastsVlnPlot(scobj, features = c('COL1A1','COL1A2','COL3A1'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/421eb42c3e8bc31a.webp)

  *   *

```
#C5/8 = SMCVlnPlot(scobj, features = c('TAGLN','ACTA2','TPM2'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/5b9fd1a504885a19.webp)

  *   *

```
# C3/10/14 = KRTVlnPlot(scobj, features = c('KRT14','KRT1','KRT5','KRT10'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/169aa06a0d384d2d.webp)

  *   *

```
#C9 = IMMVlnPlot(scobj, features = c('LYZ','HLA-DRA','PTPRC'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/ce5d5ad739f30d44.webp)

  *   *

```
#C11 = LYMEVlnPlot(scobj, features = c('CCL21','LYVE1'),pt.size = 0,cols=color)
```

![](../../images/5b7305bb961076f2.webp)

  *   *

```
#C15 = MELAVlnPlot(scobj, features = c('TYRP1','PMEL'),pt.size = 0,cols=color)
```

![](../../images/026214f1e7309cc1.png)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 根据前面的基因表达在不同亚群的差异，我们就可以确定出每个数字分群对应的细胞类型是什么了，接下来我们做的工作是细胞标签的替换# 更改idents名称，并将cell annotation信息添加至metadataIdents(scobj) <- "seurat_clusters"#更改idents名称scobj <- RenameIdents(scobj,                      "0" = "FIB",                      "1" = "FIB",                      "2" = "ENDO",                      "3" = "KRT",                      "4" = "ENDO",                      "5" = "SMC",                      "6" = "FIB",                      "7" = "FIB",                      "8" = "SMC",                      "9" = "IMM",                      "10" = "KRT",                      "11" = "LYME",                      "12" = "Unknown",                      "13" = "Unknown",                      "14" = "KRT",                      "15" = "MELA",                      "16" = "Unknown")
```

  *

```
scobj@meta.data$celltype = Idents(scobj)
```

  *   *

```
#注释好的UMAP图DimPlot(scobj, reduction = "umap",cols=color)
```

![](../../images/4ef3b7a63194807a.webp)

  *

```
# saveRDS(scobj,"result/scobj_ann.rds")
```

  *   *   *   *

```r
scobj <- readRDS("result/scobj_ann.rds")# 保留有明确细胞身份的细胞类型进行降维展示sub<- subset(scobj,idents = "Unknown",invert=T)table(Idents(sub))
```
```
##
##  FIB ENDO  KRT  SMC  IMM  LYME MELA
##  6945 3234 2160  1747  530  408  139
```

  *

```
DimPlot(sub, reduction = "umap",cols=color[c(1:7,10)])
```

![](../../images/c9cd30acf02571b8.webp)

3.4 Seurat高变基因选择

Seurat高变基因的计算是通过FindVariableFeatures函数中selection.method参数控制的，可以选择的有“vst”、“mean.var.plot”和“dispersion”。

方法名| 核心思想| 主要步骤| 是否校正均值 - 方差关系| 统计尺度| 优点| 局限性| 典型使用场景
---|---|---|---|---|---|---|---
vst| 基于方差稳定化（Variance Stabilizing Transformation）| 1\. 用 loess 拟合 `log(variance) ~ log(mean)` 关系2\. 根据拟合曲线得到期望方差3\. 对基因表达进行标准化4\. 对标准化值（截断后）计算方差| 是（显式建模）| 标准化后的方差| 对测序深度和均值依赖建模充分，鲁棒性强，是当前默认方法| 计算量相对较大| 推荐默认方法，大多数 scRNA-seq 数据
mean.var.plot (mvp)| 在相同表达水平下比较离散度| 1\. 计算每个基因的平均表达和离散度2\. 按平均表达分成 `num.bin` 个 bin3\. 在每个 bin 内计算离散度 z-score| 是（分箱间接校正）| 离散度 z-score| 思路直观、历史使用广泛| 结果依赖 bin 数；对极端表达值敏感| 早期 Seurat 分析
dispersion (disp)| 直接选择最离散的基因| 1\. 计算每个基因的离散度2\. 直接按离散度排序并选取| 否| 原始离散度| 简单、计算最快| 强烈受均值影响，高表达基因容易被选中| 不推荐用于正式分析，仅作快速探索

3.4.1[ 默认vst方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526649&idx=3&sn=812284c1bebbee77c8d20ac606b2fb6a&scene=21#wechat_redirect>)

以上Seurat默认分析流程是我们基于Seurat默认的vst方法计算得到的2000个高变基因降维分群之后，同时利用细胞类型的marker基因完成了涉及样本的细胞类型的注释。总共是得到了7种有明确细胞身份的细胞类型，分别是成纤维细胞（FIB）、内皮细胞（ENDO）、角质细胞（KRT）、平滑肌细胞（SMC）、免疫细胞（IMM）、淋巴内皮细胞（LYME）和 黑色素细胞（MELA）。基于默认的vst方法得到的高变基因能够对降维分群起到过滤噪音、聚焦差异，让细胞群划分更清晰的作用。正如前文benchmarking所提到的seurat-vst优秀评分结果是一致的。那么基于这个数据，我们来看下vst得到的高变基因究竟是哪些？同时它和seurat其他高变基因计算方法以及scanpy计算的高变基因有哪些差异呢？我们进一步来探讨一下。

  *   *

```r
seurat_vst_hvg <- VariableFeatures(scobj)head(seurat_vst_hvg)
```
```
## [1] "CCL21" "LYZ"   "CXCL8" "CCL20" "KRT6A" "KRT2"
```

  *

```
length(seurat_vst_hvg)
```
```
## [1] 2000
```

3.4.2 mvp方法

（1）mvp方法降维分群

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
scobj <- readRDS("result/scobj_ann.rds")#高变基因scobj_mvp <- FindVariableFeatures(scobj, selection.method = "mean.var.plot", nfeatures = 2000)#scalescobj_mvp <- ScaleData(scobj_mvp)#PCA降维scobj_mvp <- RunPCA(scobj_mvp, features = VariableFeatures(object = scobj_mvp),reduction.name = "pca")#harmony去批次scobj_mvp <- RunHarmony(scobj_mvp,reduction = "pca",group.by.vars = "orig.ident",reduction.save = "harmony")#邻近计算：scobj_mvp <- FindNeighbors(scobj_mvp, reduction = "harmony", dims = 1:30)# 细胞分群scobj_mvp <- FindClusters(scobj_mvp, resolution = 0.5)#UMAP降维（tSNE也可以）scobj_mvp <- RunUMAP(scobj_mvp, reduction = "harmony", dims = 1:30,reduction.name = "umap")
```

  *

```
# saveRDS(scobj_mvp,"result/scobj_mvp.rds")
```

（2）mvp方法细胞注释

  *

```r
scobj_mvp <- readRDS("result/scobj_mvp.rds")
```

  *   *

```
# 分群情况DimPlot(scobj_mvp, reduction = "umap",cols=color)
```

![](../../images/2e7df0a02d333c98.webp)

  *   *

```r
seurat_mvp_hvg <- VariableFeatures(scobj_mvp)head(seurat_mvp_hvg)
```
```
## [1] "IGKC"    "DCD"     "IGHG4"   "IGHG1"   "SCGB2A2" "CCL21"
```

  *

```
length(seurat_mvp_hvg)
```
```
## [1] 957
```

  *

```
# 这里可以看到mvp方法的高变基因数目是不受到nfeatures参数控制的，会自动生成一定数目的高变基因
```

  *   *

```
#C2/5/7 = EndothelialVlnPlot(scobj_mvp, features = c("CLDN5",'FLT1','SELE',"PECAM1"),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/4e76c97c06777c59.webp)

  *   *

```
#C 0/1/6/8= FibroblastsVlnPlot(scobj_mvp, features = c('COL1A1','COL1A2','COL3A1'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/1a536ced6797db7c.webp)

  *   *

```
#C4/10 = SMCVlnPlot(scobj_mvp, features = c('TAGLN','ACTA2','TPM2'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/3e925ab2f9b70d49.webp)

  *   *

```
# C3/9 = KRTVlnPlot(scobj_mvp, features = c('KRT14','KRT1','KRT5','KRT10'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/48c1ee4dbab0b232.webp)

  *   *

```
#C11 = IMMVlnPlot(scobj_mvp, features = c('LYZ','HLA-DRA','PTPRC'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/c765f75f5d732a3f.webp)

  *   *

```
#C12 = LYMEVlnPlot(scobj_mvp, features = c('CCL21','LYVE1'),pt.size = 0,cols=color)
```

![](../../images/13125be2d80fa360.webp)

  *   *

```
#C16 = MELAVlnPlot(scobj_mvp, features = c('TYRP1','PMEL'),pt.size = 0,cols=color)
```

![](../../images/bbda20517c4e96f8.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 更改idents名称，并将cell annotation信息添加至metadataIdents(scobj_mvp) <- "seurat_clusters"#更改idents名称scobj_mvp <- RenameIdents(scobj_mvp,                      "0" = "FIB",                      "1" = "FIB",                      "2" = "ENDO",                      "3" = "KRT",                      "4" = "SMC",                      "5" = "ENDO",                      "6" = "FIB",                      "7" = "ENDO",                      "8" = "FIB",                      "9" = "KRT",                      "10" = "SMC",                      "11" = "IMM",                      "12" = "LYME",                      "13" = "Unknown",                      "14" = "Unknown",                      "15" = "Unknown",                      "16" = "MELA")
```

  *

```
scobj_mvp@meta.data$celltype = Idents(scobj_mvp)
```

  *   *

```
#注释好的UMAP图DimPlot(scobj_mvp, reduction = "umap",cols=color)
```

![](../../images/ae18ecdf730b7e0f.webp)

  *

```
# saveRDS(scobj_mvp,"result/scobj_mvp_ann.rds")
```

  *   *   *   *

```r
scobj_mvp <- readRDS("result/scobj_mvp_ann.rds")# 保留有明确细胞身份的细胞类型进行降维展示sub_mvp<- subset(scobj_mvp,idents = "Unknown",invert=T)table(Idents(sub_mvp))
```
```
##
##  FIB ENDO  KRT SMC  IMM  LYME MELA
## 6977  3288 2098 1756  523  412   97
```

  *

```
DimPlot(sub_mvp, reduction = "umap",cols=color[c(1:7,10)])
```

![](../../images/503c5b38d5d00441.webp)

3.4.3 disp方法

（1）disp方法降维分群

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
scobj <- readRDS("result/scobj_ann.rds")#高变基因scobj_disp <- FindVariableFeatures(scobj, selection.method = "dispersion", nfeatures = 2000)#scalescobj_disp <- ScaleData(scobj_disp)#PCA降维scobj_disp <- RunPCA(scobj_disp, features = VariableFeatures(object = scobj_disp),reduction.name = "pca")#harmony去批次scobj_disp <- RunHarmony(scobj_disp,reduction = "pca",group.by.vars = "orig.ident",reduction.save = "harmony")#邻近计算：scobj_disp <- FindNeighbors(scobj_disp, reduction = "harmony", dims = 1:30)# 细胞分群scobj_disp <- FindClusters(scobj_disp, resolution = 0.5)#UMAP降维（tSNE也可以）scobj_disp <- RunUMAP(scobj_disp, reduction = "harmony", dims = 1:30,reduction.name = "umap")
```

  *

```
# saveRDS(scobj_disp,"result/scobj_disp.rds")
```

（2）disp方法细胞注释

  *

```r
scobj_disp <- readRDS("result/scobj_disp.rds")
```

  *   *

```
# 分群情况，可以看到该方法细胞群相较于前两个方法明显杂乱了许多DimPlot(scobj_disp, reduction = "umap",cols=color)
```

![](../../images/e5e3ef05e390e5ce.webp)

  *   *

```r
seurat_disp_hvg <- VariableFeatures(scobj_disp)head(seurat_disp_hvg)
```
```
## [1] "IGKC"    "DCD"     "IGHG4"   "IGHG1"   "SCGB2A2" "COL1A1"
```

  *

```
length(seurat_disp_hvg)
```
```
## [1] 2000
```

  *

```
# disp下的nfeatures参数可以起到控制高变基因数目的作用
```

  *   *

```
#C2/4 = EndothelialVlnPlot(scobj_disp, features = c("CLDN5",'FLT1','SELE',"PECAM1"),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/21f8e16078eff2ea.webp)

  *   *

```
#C0/1/6/10/12 = FibroblastsVlnPlot(scobj_disp, features = c('COL1A1','COL1A2','COL3A1'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/ee5981401c0b44a3.webp)

  *   *

```
#C5/7 = SMCVlnPlot(scobj_disp, features = c('TAGLN','ACTA2','TPM2'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/65046ecc5a156c8f.webp)

  *   *

```
# C3/9 = KRTVlnPlot(scobj_disp, features = c('KRT14','KRT1','KRT5','KRT10'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/c5b5e76a25d1c7f4.webp)

  *   *

```
#C8 = IMMVlnPlot(scobj_disp, features = c('LYZ','HLA-DRA','PTPRC'),pt.size = 0,ncol = 2,cols=color)
```

![](../../images/899b5359bf1d4765.webp)

  *   *

```
#C11 = LYMEVlnPlot(scobj_disp, features = c('CCL21','LYVE1'),pt.size = 0,cols=color)
```

![](../../images/2e6ad9e7f738794d.webp)

  *   *

```
#C17 = MELAVlnPlot(scobj_disp, features = c('TYRP1','PMEL'),pt.size = 0,cols=color)
```

![](../../images/1f0eb339d9cb9281.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 更改idents名称，并将cell annotation信息添加至metadataIdents(scobj_disp) <- "seurat_clusters"#更改idents名称scobj_disp <- RenameIdents(scobj_disp,                      "0" = "FIB",                      "1" = "FIB",                      "2" = "ENDO",                      "3" = "KRT",                      "4" = "ENDO",                      "5" = "SMC",                      "6" = "FIB",                      "7" = "SMC",                      "8" = "IMM",                      "9" = "KRT",                      "10" = "FIB",                      "11" = "LYME",                      "12" = "FIB",                      "13" = "Unknown",                      "14" = "Unknown",                      "15" = "Unknown",                      "16" = "Unknown",                      "17" = "MELA")
```

  *

```
scobj_disp@meta.data$celltype = Idents(scobj_disp)
```

  *   *

```
#注释好的UMAP图DimPlot(scobj_disp, reduction = "umap",cols=color)
```

![](../../images/227edfa187422170.webp)

  *

```
# saveRDS(scobj_disp,"result/scobj_disp_ann.rds")
```

  *   *   *   *

```r
scobj_disp <- readRDS("result/scobj_disp_ann.rds")# 保留有明确细胞身份的细胞类型进行降维展示sub_disp<- subset(scobj_disp,idents = "Unknown",invert=T)table(Idents(sub_disp))
```
```
##
##  FIB ENDO KRT  SMC  IMM LYME MELA
##  6913 3202 2101 1759  513 400   98
```

  *

```
DimPlot(sub_disp, reduction = "umap",cols=color[c(1:7,10)])
```

![](../../images/0dfa3a1dbcd6f77c.webp)

3.5 Scanpy整合分析流程

Scanpy是基于python语言开发的单细胞分析软件，所以接下来的代码都是在python环境下运行的哦~ Python作为这部分内容的核心编程语言，它语法简洁、库资源丰富，计算高效，是数据科学、自动化开发等领域的首选，兼顾新手入门与资深者高效需求。因此，同学们在学习这个教程前，需要有一定得Python知识，可以参考[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520999&idx=2&sn=7f6aa90c2ffa786bd660aa40b109de49&scene=21#wechat_redirect>)进行快速学习。这里我们主要进行的包括了Scanpy数据质控、数据整合和细胞类型注释环节。想要了解更详细的Scanpy分析过程和下游可以拓展的分析内容，可以参考[Python版scRNA-seq分析全流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)。

3.5.1 数据质控

  *   *   *   *   *   *   *

```
# 加载python库import scanpy as sc                          # Scanpy 主库（对标 Seurat）import anndata as ad                         # AnnData 数据结构import pandas as pd                          # 表格处理import numpy as np                           # 数值计算import os                                    # 文件路径处理import scanpy.external as sce                # 辅助功能库
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 指定数据路径 NF1_path = "data/GSE163973_RAW/NF1_matrix/"  # NF1 样本路径NF2_path = "data/GSE163973_RAW/NF2_matrix/"  # NF2 样本路径datadir = [NF1_path, NF2_path]               # 样本路径列表adatas = []                                  # 用于存放每个样本的 AnnData 对象# 读取数据（Read10X + CreateSeuratObject） for path in datadir:    sample_name = os.path.basename(os.path.normpath(path)).split("_")[0]  # 提取样本名    print(f"-------- {sample_name} 正在处理 --------")                     # 打印进度信息    adata = sc.read_10x_mtx(               # 读取 10X counts 矩阵（对标 Read10X）        path,        var_names = "gene_symbols",         # 使用基因名作为 var_names        cache = False    )    adata.obs["orig.ident"] = sample_name   # 添加样本标签（对标 project / orig.ident）    sc.pp.filter_genes(adata, min_cells = 3)    # min.cells = 3    sc.pp.filter_cells(adata, min_genes = 200)  # min.features = 200    adatas.append(adata)                    # 保存当前样本对象#  线粒体基因比例 & 质控 for adata in adatas:    adata.var["mt"] = adata.var_names.str.startswith("MT-")  # 标记线粒体基因    sc.pp.calculate_qc_metrics(             # 计算 QC 指标        adata,        qc_vars = ["mt"],        percent_top = None,        log1p = False,        inplace = True    )    adata._inplace_subset_obs(               # 质控过滤（对标 subset）        (adata.obs["n_genes_by_counts"] > 200) &        (adata.obs["n_genes_by_counts"] < 6000) &        (adata.obs["pct_counts_mt"] < 15)    )    # 备份原始的counts矩阵    adata.layers["counts"] = adata.X.copy()# NormalizeData（LogNormalize） for adata in adatas:    sc.pp.normalize_total(adata, target_sum = 1e4)  # scale.factor = 10000    sc.pp.log1p(adata)                               # log1p 转换# 合并样本（merge）adata = ad.concat(                                 # 合并多个样本    adatas,    label = "orig.ident",    keys = [a.obs["orig.ident"][0] for a in adatas],    join="outer")
```

3.5.2 [降维分群](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485571&idx=1&sn=a0497f79fe83ff6b86705f6eb0e1cbf9&scene=21#wechat_redirect>)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 高变基因（FindVariableFeatures vst） sc.pp.highly_variable_genes(    adata,    layer="counts",    flavor = "seurat_v3",                           # 对标 vst 方法    n_top_genes = 2000,    subset = False)adata.layers["scaled"] = adata.X.toarray()# ScaleData sc.pp.scale(adata, max_value = 10, layer="scaled")                  # 对标 ScaleData# PCA（RunPCA） sc.tl.pca(    adata,    use_highly_variable = True,    svd_solver = "arpack",    layer="scaled")# Harmony 去批次（RunHarmony）sce.pp.harmony_integrate(adata, key = "orig.ident", basis = 'X_pca', adjusted_basis = 'X_pca_harmony')# FindNeighborssc.pp.neighbors(    adata,    use_rep = "X_pca_harmony",                           # 使用 Harmony 空间    n_neighbors = 20,    n_pcs = 30)# FindClusterssc.tl.leiden(    adata,    resolution = 0.5,    key_added = "leiden")# RunUMAPsc.tl.umap(adata)# 保存对象adata.write("result/scobj_scanpy_seurat_v3.h5ad")
```

3.5.3 细胞注释

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_seurat_v3.h5ad")sc.pl.violin(    adata,    keys = [        "n_genes_by_counts",                 # nFeature_RNA        "total_counts",                      # nCount_RNA        "pct_counts_mt"                      # percent.mt    ],    groupby = "orig.ident",                  # 按样本分组    jitter = 0,                              # 不抖动（等价 pt.size = 0）    multi_panel = True,                       # 多面板显示    save = "_qc.png")
```

![](../../images/382923eb4aae2ef1.webp)

  *   *   *   *   *   *   *

```
# UMAP 分群展示sc.pl.umap(    adata,    color = "leiden",                        # 聚类结果    legend_loc = "on data",     save = "_seurat_v3.png")
```

![](../../images/6900e35ce04e0b74.webp)

  *   *   *   *   *   *   *   *   *   *

```
# Marker 验证# Endothelial（C3 / C4 / C7）# Marker: CLDN5, FLT1, SELE, PECAM1sc.pl.violin(    adata,    keys = ["CLDN5", "FLT1", "SELE", "PECAM1"],    groupby = "leiden",    jitter = 0,    save = "_ENDO_seurat_v3.png")
```

![](../../images/efaceb2329513d59.webp)

  *   *   *   *   *   *   *   *   *

```
# Fibroblasts（C0 / C1 / C6 / C10）# Marker: COL1A1, COL1A2, COL3A1sc.pl.violin(    adata,    keys = ["COL1A1", "COL1A2", "COL3A1"],    groupby = "leiden",    jitter = 0,    save = "_FIB_seurat_v3.png")
```

![](../../images/ca390da6773ac7e9.webp)

  *   *   *   *   *   *   *   *   *

```
# Smooth Muscle Cells（C5 / C9）# Marker: TAGLN, ACTA2, TPM2sc.pl.violin(    adata,    keys = ["TAGLN", "ACTA2", "TPM2"],    groupby = "leiden",    jitter = 0,    save = "_SMC_seurat_v3.png")
```

![](../../images/c1edc346a63fd4a5.webp)

  *   *   *   *   *   *   *   *   *

```
# Keratinocytes（C2 / C11 / C15）# Marker: KRT14, KRT1, KRT5, KRT10sc.pl.violin(    adata,    keys = ["KRT14", "KRT1", "KRT5", "KRT10"],    groupby = "leiden",    jitter = 0,    save = "_KRT_seurat_v3.png")
```

![](../../images/c49f7580cdd3c865.webp)

  *   *   *   *   *   *   *   *   *

```
# Immune cells（C8）# Marker: LYZ, HLA-DRA, PTPRCsc.pl.violin(    adata,    keys = ["LYZ", "HLA-DRA", "PTPRC"],    groupby = "leiden",    jitter = 0,    save = "_IMM_seurat_v3.png")
```

![](../../images/356b95a053e3db7e.webp)

  *   *   *   *   *   *   *   *   *

```
# Lymphatic Endothelial Cells（C12）# Marker: CCL21, LYVE1sc.pl.violin(    adata,    keys = ["CCL21", "LYVE1"],    groupby = "leiden",    jitter = 0,    save = "_LYME_seurat_v3.png")
```

![](../../images/fe08638206123b5a.webp)

  *   *   *   *   *   *   *   *   *

```
# Melanocytes（C16）# Marker: TYRP1, PMELsc.pl.violin(    adata,    keys = ["TYRP1", "PMEL"],    groupby = "leiden",    jitter = 0,    save = "_MELA_seurat_v3.png")
```

![](../../images/3ecd9883586acfe8.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 细胞类型注释（RenameIdents 对标）cluster_to_celltype = {    "0": "FIB",    "1": "FIB",    "2": "KRT",    "3": "ENDO",    "4": "ENDO",    "5": "SMC",    "6": "FIB",    "7": "ENDO",    "8": "IMM",    "9": "SMC",    "10": "FIB",    "11": "KRT",    "12": "LYME",    "13": "Unknown",    "14": "Unknown",    "15": "KRT",    "16": "MELA",    "17": "Unknown"}adata.obs["celltype"] = adata.obs["leiden"].map(cluster_to_celltype)  # 写入 metadata# 保存对象（saveRDS 对标）adata.write("result/scobj_scanpy_seurat_v3_ann.h5ad")                       # 注释后细胞
```

  *   *   *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_seurat_v3_ann.h5ad") # 去除 Unknown 细胞adata_sub = adata[adata.obs["celltype"] != "Unknown"].copy()         # UMAP 分群展示sc.pl.umap(    adata_sub,    color = "celltype",                        # 聚类结果    legend_loc = "on data",    save = "_seurat_v3_ann.png")
```

![](../../images/a487f92bd337e90d.webp)

3.6 Scanpy高变基因选择

这部分我们使用Scanpy整合分析流程seurat_v3方法计算得到的2000个高变基因降维分群之后，同时利用细胞类型的marker基因完成了涉及样本的细胞类型的注释。同样得到了第四小节中Seurat的整合分析流程一致的7种有明确细胞身份的细胞类型。基于Scanpy中seurat_v3方法得到的高变基因同样能够对降维分群起到过滤噪音、聚焦差异，让细胞群划分更清晰的作用。Scanpy中除了seurat_v3方法可以计算高变基因之外，另外两种可供使用的方法为 seurat 和 cell_ranger。不同的方法通过sc.pp.highly_variable_genes函数的flavor参数控制。对比如下：

flavor| 期望输入矩阵| 核心统计计量| 是否分 bin| 是否用 batch_key| batch_key 的作用方式| 对应 Seurat 方法
---|---|---|---|---|---|---
seurat| log-normalized data| Dispersion（标准化离散度）| 是（按 mean 分 bin）| 否（Scanpy 中不支持）| 不适用| Seurat v2 `FindVariableFeatures(method="mean.var.plot")`
cell_ranger| log-normalized data| Dispersion（标准化离散度）| 是（按 mean 分 bin）| 否| 不适用| Cell Ranger HVG 方法 (Zheng et al. 2017)
seurat_v3| raw counts| Normalized variance (VST)| 否| 是| 先算每个 batch 的 HVG 排名；按 “中位排名” 排序，batch 覆盖数用于打破平局| Seurat v3+ `FindVariableFeatures(method = "vst")`
seurat_v3_paper| raw counts| Normalized variance (VST)| 否| 是| 先按 “成为 HVG 的 batch 数量” 排序；中位排名用于打破平局| Seurat `SelectIntegrationFeatures`

3.6.1 seurat_v3方法

  *   *   *

```
# 提取scanpy_seurat_v3计算得到的高变基因scanpy_seurat_v3_hvg =adata.var[adata.var['highly_variable']].copy()print(f"scanpy_seurat_v3提取到的高变基因数量：{len(scanpy_seurat_v3_hvg)}")
```

![](../../images/26cdfad048da9872.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 保存高变基因scanpy_seurat_v3_hvg.to_csv(    "result/scanpy_seurat_v3_hvg.txt",    sep="\t",  # 制表符分隔，符合单细胞分析常规格式    index=True,  # 不保存行索引    header=True   # 保留列名)# 保存细胞分群与barcode对应关系 # 1. 提取barcode和celltype，整理成DataFramecelltype_df = adata.obs[['celltype']].copy()# 重置索引，将barcode（行名）转为列celltype_df.reset_index(inplace=True)celltype_df.rename(columns={'index': 'barcode'}, inplace=True)# 2. 保存细胞分群表格到指定路径celltype_df.to_csv(    "result/scanpy_seurat_v3_celltype.txt",    sep="\t",    index=False,    header=True)
```

3.6.2 seurat方法

（1）降维分群

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_seurat_v3_ann.h5ad") # 高变基因（FindVariableFeatures vst） # 注意这里layer需要用标准化之后的，不能是原始的counts,否则会报错sc.pp.highly_variable_genes(    adata,    flavor = "seurat",                              n_top_genes = 2000,    subset = False)adata.layers["scaled"] = adata.X.toarray()# ScaleData sc.pp.scale(adata, max_value = 10, layer="scaled")                  # 对标 ScaleData# PCA（RunPCA） sc.tl.pca(    adata,    use_highly_variable = True,    svd_solver = "arpack",    layer="scaled")# Harmony 去批次（RunHarmony）sce.pp.harmony_integrate(adata, key = "orig.ident", basis = 'X_pca', adjusted_basis = 'X_pca_harmony')# FindNeighborssc.pp.neighbors(    adata,    use_rep = "X_pca_harmony",                           # 使用 Harmony 空间    n_neighbors = 20,    n_pcs = 30)# FindClusterssc.tl.leiden(    adata,    resolution = 0.5,    key_added = "leiden")# RunUMAPsc.tl.umap(adata)# 保存对象adata.write("result/scobj_scanpy_seurat.h5ad")
```

（2）细胞注释

  *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_seurat.h5ad")# UMAP 分群展示sc.pl.umap(    adata,    color = "leiden",                        # 聚类结果    legend_loc = "on data",     save = "_seurat.png")
```

![](../../images/80e8403ee7bd39d9.webp)

  *   *   *   *   *   *   *   *   *   *

```
# Marker 验证# Endothelial（C0 / C6）# Marker: CLDN5, FLT1, SELE, PECAM1sc.pl.violin(    adata,    keys = ["CLDN5", "FLT1", "SELE", "PECAM1"],    groupby = "leiden",    jitter = 0,    save = "_ENDO_seurat.png")
```

![](../../images/f3cf8228a0a55de3.webp)

  *   *   *   *   *   *   *   *   *

```
# Fibroblasts（C1 / C2 / C3 / C9）# Marker: COL1A1, COL1A2, COL3A1sc.pl.violin(    adata,    keys = ["COL1A1", "COL1A2", "COL3A1"],    groupby = "leiden",    jitter = 0,    save = "_FIB_seurat.png")
```

![](../../images/3e69f3c9d39e8126.webp)

  *   *   *   *   *   *   *   *   *

```
# Smooth Muscle Cells（C5 / C8）# Marker: TAGLN, ACTA2, TPM2sc.pl.violin(    adata,    keys = ["TAGLN", "ACTA2", "TPM2"],    groupby = "leiden",    jitter = 0,    save = "_SMC_seurat.png")
```

![](../../images/f7505347551fce42.webp)

  *   *   *   *   *   *   *   *   *

```
# Keratinocytes（C4 / C11 / C14）# Marker: KRT14, KRT1, KRT5, KRT10sc.pl.violin(    adata,    keys = ["KRT14", "KRT1", "KRT5", "KRT10"],    groupby = "leiden",    jitter = 0,    save = "_KRT_seurat.png")
```

![](../../images/0978f1423962299b.webp)

  *   *   *   *   *   *   *   *   *

```
# Immune cells（C7）# Marker: LYZ, HLA-DRA, PTPRCsc.pl.violin(    adata,    keys = ["LYZ", "HLA-DRA", "PTPRC"],    groupby = "leiden",    jitter = 0,    save = "_IMM_seurat.png")
```

![](../../images/58d7580a71110033.webp)

  *   *   *   *   *   *   *   *   *

```
# Lymphatic Endothelial Cells（C10）# Marker: CCL21, LYVE1sc.pl.violin(    adata,    keys = ["CCL21", "LYVE1"],    groupby = "leiden",    jitter = 0,    save = "_LYME_seurat.png")
```

![](../../images/1db374b9db5bae62.webp)

  *   *   *   *   *   *   *   *   *

```
# Melanocytes（C15）# Marker: TYRP1, PMELsc.pl.violin(    adata,    keys = ["TYRP1", "PMEL"],    groupby = "leiden",    jitter = 0,    save = "_MELA_seurat.png")
```

![](../../images/4380c0937fb39873.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 细胞类型注释（RenameIdents 对标）cluster_to_celltype = {    "0": "ENDO",    "1": "FIB",    "2": "FIB",    "3": "FIB",    "4": "KRT",    "5": "SMC",    "6": "ENDO",    "7": "IMM",    "8": "SMC",    "9": "FIB",    "10": "LYME",    "11": "KRT",    "12": "Unknown",    "13": "Unknown",    "14": "KRT",    "15": "MELA",    "16": "Unknown"}adata.obs["celltype"] = adata.obs["leiden"].map(cluster_to_celltype)  # 写入 metadata# 保存对象（saveRDS 对标）adata.write("result/scobj_scanpy_seurat_ann.h5ad")                       # 注释后细胞
```

  *   *   *

```
# 提取scanpy_seurat计算得到的高变基因scanpy_seurat_hvg =adata.var[adata.var['highly_variable']].copy()print(f"scanpy_seurat提取到的高变基因数量：{len(scanpy_seurat_hvg)}")
```

![](../../images/2acd0b46e03b1940.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 保存高变基因scanpy_seurat_hvg.to_csv(    "result/scanpy_seurat_hvg.txt",    sep="\t",  # 制表符分隔，符合单细胞分析常规格式    index=True,  # 不保存行索引    header=True   # 保留列名)# 保存细胞分群与barcode对应关系 # 1. 提取barcode和celltype，整理成DataFramecelltype_df = adata.obs[['celltype']].copy()# 重置索引，将barcode（行名）转为列celltype_df.reset_index(inplace=True)celltype_df.rename(columns={'index': 'barcode'}, inplace=True)# 2. 保存细胞分群表格到指定路径celltype_df.to_csv(    "result/scanpy_seurat_celltype.txt",    sep="\t",    index=False,    header=True)
```

  *   *   *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_seurat_ann.h5ad") # 去除 Unknown 细胞adata_sub = adata[adata.obs["celltype"] != "Unknown"].copy()         # UMAP 分群展示sc.pl.umap(    adata_sub,    color = "celltype",                        # 聚类结果    legend_loc = "on data",    save = "_seurat_ann.png")
```

![](../../images/8903fe5e28a25ba2.webp)

3.6.3 [cell_ranger方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521051&idx=1&sn=e2ab820001013bae6e35310e27897086&scene=21#wechat_redirect>)

（1）降维分群

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_seurat_v3_ann.h5ad") # 高变基因（FindVariableFeatures vst） sc.pp.highly_variable_genes(    adata,    flavor = "cell_ranger",                               n_top_genes = 2000,    subset = False)adata.layers["scaled"] = adata.X.toarray()# ScaleData sc.pp.scale(adata, max_value = 10, layer="scaled")                  # 对标 ScaleData# PCA（RunPCA） sc.tl.pca(    adata,    use_highly_variable = True,    svd_solver = "arpack",    layer="scaled")# Harmony 去批次（RunHarmony）sce.pp.harmony_integrate(adata, key = "orig.ident", basis = 'X_pca', adjusted_basis = 'X_pca_harmony')# FindNeighborssc.pp.neighbors(    adata,    use_rep = "X_pca_harmony",                           # 使用 Harmony 空间    n_neighbors = 20,    n_pcs = 30)# FindClusterssc.tl.leiden(    adata,    resolution = 0.5,    key_added = "leiden")# RunUMAPsc.tl.umap(adata)# 保存对象adata.write("result/scobj_scanpy_cell_ranger.h5ad")
```

（2）细胞注释

  *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_cell_ranger.h5ad")# UMAP 分群展示sc.pl.umap(    adata,    color = "leiden",                        # 聚类结果    legend_loc = "on data",     save = "_cell_ranger.png")
```

![](../../images/676e28cdc25130c1.webp)

  *   *   *   *   *   *   *   *   *   *

```
# Marker 验证# Endothelial（C1 / C6）# Marker: CLDN5, FLT1, SELE, PECAM1sc.pl.violin(    adata,    keys = ["CLDN5", "FLT1", "SELE", "PECAM1"],    groupby = "leiden",    jitter = 0,    save = "_ENDO_cell_ranger.png")
```

![](../../images/a212d9f3d2cf197e.webp)

  *   *   *   *   *   *   *   *   *

```
# Fibroblasts（C0 / C2 / C5 / C11）# Marker: COL1A1, COL1A2, COL3A1sc.pl.violin(    adata,    keys = ["COL1A1", "COL1A2", "COL3A1"],    groupby = "leiden",    jitter = 0,    save = "_FIB_cell_ranger.png")
```

![](../../images/2127a2d2f86e65f3.webp)

  *   *   *   *   *   *   *   *   *

```
# Smooth Muscle Cells（C4 / C8）# Marker: TAGLN, ACTA2, TPM2sc.pl.violin(    adata,    keys = ["TAGLN", "ACTA2", "TPM2"],    groupby = "leiden",    jitter = 0,    save = "_SMC_cell_ranger.png")
```

![](../../images/dcb389ad3576f2df.webp)

  *   *   *   *   *   *   *   *   *

```
# Keratinocytes（C3 / C7）# Marker: KRT14, KRT1, KRT5, KRT10sc.pl.violin(    adata,    keys = ["KRT14", "KRT1", "KRT5", "KRT10"],    groupby = "leiden",    jitter = 0,    save = "_KRT_cell_ranger.png")
```

![](../../images/f3380fe3b1fc4a3d.webp)

  *   *   *   *   *   *   *   *   *

```
# Immune cells（C9）# Marker: LYZ, HLA-DRA, PTPRCsc.pl.violin(    adata,    keys = ["LYZ", "HLA-DRA", "PTPRC"],    groupby = "leiden",    jitter = 0,    save = "_IMM_cell_ranger.png")
```

![](../../images/9136621d1a3e5bc7.webp)

  *   *   *   *   *   *   *   *   *

```
# Lymphatic Endothelial Cells（C10）# Marker: CCL21, LYVE1sc.pl.violin(    adata,    keys = ["CCL21", "LYVE1"],    groupby = "leiden",    jitter = 0,    save = "_LYME_cell_ranger.png")
```

![](../../images/ba890d95eb5670d2.webp)

  *   *   *   *   *   *   *   *   *

```
# Melanocytes（C14）# Marker: TYRP1, PMELsc.pl.violin(    adata,    keys = ["TYRP1", "PMEL"],    groupby = "leiden",    jitter = 0,    save = "_MELA_cell_ranger.png")
```

![](../../images/6ea5caf930158c6c.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 细胞类型注释（RenameIdents 对标）cluster_to_celltype = {    "0": "FIB",    "1": "ENDO",    "2": "FIB",    "3": "KRT",    "4": "SMC",    "5": "FIB",    "6": "ENDO",    "7": "KRT",    "8": "SMC",    "9": "IMM",    "10": "LYME",    "11": "FIB",    "12": "Unknown",    "13": "Unknown",    "14": "MELA",    "15": "Unknown"}adata.obs["celltype"] = adata.obs["leiden"].map(cluster_to_celltype)  # 写入 metadata# 保存对象（saveRDS 对标）adata.write("result/scobj_scanpy_cell_ranger_ann.h5ad")                       # 注释后细胞
```

  *   *   *

```
# 提取scanpy_cell_ranger计算得到的高变基因scanpy_cell_ranger_hvg =adata.var[adata.var['highly_variable']].copy()print(f"scanpy_cell_ranger提取到的高变基因数量：{len(scanpy_cell_ranger_hvg)}")
```

![](../../images/be9ceb7eb88f473c.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 保存高变基因scanpy_cell_ranger_hvg.to_csv(    "result/scanpy_cell_ranger_hvg.txt",    sep="\t",  # 制表符分隔，符合单细胞分析常规格式    index=True,  # 不保存行索引    header=True   # 保留列名)# 保存细胞分群与barcode对应关系 # 1. 提取barcode和celltype，整理成DataFramecelltype_df = adata.obs[['celltype']].copy()# 重置索引，将barcode（行名）转为列celltype_df.reset_index(inplace=True)celltype_df.rename(columns={'index': 'barcode'}, inplace=True)# 2. 保存细胞分群表格到指定路径celltype_df.to_csv(    "result/scanpy_cell_ranger_celltype.txt",    sep="\t",    index=False,    header=True)
```

  *   *   *   *   *   *   *   *   *   *

```
adata = sc.read("result/scobj_scanpy_cell_ranger_ann.h5ad") # 去除 Unknown 细胞adata_sub = adata[adata.obs["celltype"] != "Unknown"].copy()         # UMAP 分群展示sc.pl.umap(    adata_sub,    color = "celltype",                        # 聚类结果    legend_loc = "on data",    save = "_cell_ranger_ann.png")
```

![](../../images/79bdbabd00873f4d.webp)

3.7 Scanpy和Seurat对比

3.7.1 降维分群差异

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
scanpy_seurat_v3 <- readPNG("figures/umap_seurat_v3_ann.png")scanpy_seurat <- readPNG("figures/umap_seurat_ann.png")scanpy_cell_ranger <- readPNG("figures/umap_cell_ranger_ann.png")# 创建三个独立的 ggplot 图片对象p1 <- ggplot() +   background_image(scanpy_seurat_v3) +   theme_void() +  # 隐藏坐标轴，只显示图片  labs(title = "scanpy_seurat_v3")  # 可选：添加标题p2 <- ggplot() +   background_image(scanpy_seurat) +   theme_void() +  labs(title = "scanpy_seurat")p3 <- ggplot() +   background_image(scanpy_cell_ranger) +   theme_void() +  labs(title = "scanpy_cell_ranger")# 拼接三张图（并排展示，可调整布局）# 1行3列布局p1 | p2 | p3
```

![](../../images/05a4480a08be4044.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# seurat_vst降维结果p4 <- DimPlot(sub, reduction = "umap",cols=color[c(1:7,10)],label = T)+  # 绘图四周方框同时隐藏坐标轴刻度  theme_bw()+theme_few()+  theme(axis.text = element_blank(),         axis.ticks = element_blank())+  # 不设置图例  NoLegend()+  # 图片标题  labs(title = "seurat_vst")# seurat_mvp降维结果p5 <- DimPlot(sub_mvp, reduction = "umap",cols=color[c(1:7,10)],label = T)+theme_bw()+theme_few()+theme(axis.text = element_blank(), axis.ticks = element_blank())+NoLegend()+labs(title = "seurat_mvp")# seurat_disp降维结果p6 <- DimPlot(sub_disp, reduction = "umap",cols=color[c(1:7,10)],label = T)+theme_bw()+theme_few()+theme(axis.text = element_blank(), axis.ticks = element_blank())+NoLegend()+labs(title = "seurat_disp")# 三张图联合展示p4 | p5 | p6
```

![](../../images/32a9748d4717ed61.webp)

把seurat的结果和scanpy放在一起对比下：

![](../../images/f29afb3413e1f2ba.webp)

结合这张图，我们先比较一下Seurat内部三种高变基因方法的优劣程度。总体来看Seurat三种方法都可以做到比较好的细胞群的划分。都成功划分出了7种有明显生物学差异的细胞类型。但是仔细看一下的话，还是有一定差异的。相对来说Seurat-vst方法的聚类分群效果上，细胞群内部紧凑性以及群与群之间的界限是分的最清晰的。以Seurat-mvp方法为例，FIB和MELA群存在一定粘连，划分不够清晰。Seurat-disp则相对vst和mvp方法效果更差一些，零散细胞更多，群内部的紧凑性不如前两种方法。

Scanpy也呈现出类似的趋势，不同高变基因计算方法也都做到了比较好的细胞群的划分，分别成功鉴定出了关键的7种细胞亚群。但是就分群效果来看，与Seurat-vst对标的Scanpy-seurat_v3效果是最好的。能够做到群内部细胞之间分布紧密，不同群之间界限清晰。更为有助于我们后续的细胞类型确定。

3.7.2 [高变基因交集情况](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504403&idx=5&sn=12e5a17af1cc976ce78876b51cd241ca&scene=21#wechat_redirect>)

（1）高变基因数目统计

  *   *   *

```r
# 读取文件并提取基因ID（行名））gene_seurat_v3 <- rownames(read.table("result/scanpy_seurat_v3_hvg.txt", header = TRUE, row.names = 1, sep = "\t"))head(gene_seurat_v3)
```
```
## [1] "A2M"    "A2ML1"  "AADAC"  "AARD"   "ABCA12" "ABCC9"
```

  *   *

```r
gene_seurat <- rownames(read.table("result/scanpy_seurat_hvg.txt", header = TRUE, row.names = 1, sep = "\t"))head(gene_seurat)
```
```
## [1] "AARD"         "AATK"         "ABCA10"       "ABCC9"        "ABHD14A-ACY1"
## [6] "ABI3BP"
```

  *   *

```r
gene_cell_ranger <- rownames(read.table("result/scanpy_cell_ranger_hvg.txt", header = TRUE, row.names = 1, sep = "\t"))head(gene_cell_ranger)
```
```
## [1] "A2M"    "AARD"   "ABCA10" "ABCA6"  "ABCA8"  "ABCB1"
```

（2）venn图

  *   *   *   *   *   *   *   *   *   *   *

```r
gene_list <- list(  "seurat_vst"       = seurat_vst_hvg,    # 第1组  "seurat_mvp"       = seurat_mvp_hvg,    # 第2组  "seurat_disp"      = seurat_disp_hvg,   # 第3组  "scanpy_seurat_v3" = gene_seurat_v3,    # 第4组  "scanpy_seurat"    = gene_seurat,       # 第5组  "scanpy_cell_ranger" = gene_cell_ranger # 第6组)# 统计每组基因总数gene_total <- sapply(gene_list, length)cat("高变基因总数统计 ===\n")
```
```
## 高变基因总数统计 ===
```

  *   *   *

```
for (i in 1:length(gene_total)) {  cat(names(gene_total)[i], "：", gene_total[i], "个基因\n")}
```
```
## seurat_vst ： 2000 个基因
## seurat_mvp ： 957 个基因
## seurat_disp ： 2000 个基因
## scanpy_seurat_v3 ： 2000 个基因
## scanpy_seurat ： 2000 个基因
## scanpy_cell_ranger ： 2000 个基因
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 定义对比组别compare_groups <- c("seurat_mvp", "seurat_disp", "scanpy_seurat_v3",                     "scanpy_seurat", "scanpy_cell_ranger")for (group_name in compare_groups) {  set1 <- gene_list[["seurat_vst"]]  set2 <- gene_list[[group_name]]  # 计算基因交集数目  intersection <- intersect(set1, set2)  cat(paste0(    "seurat_vst vs ", group_name,    " 交集基因数: ", length(intersection), "\n"  ))  # 关键：新开一页  grid.newpage()  # 设置画布边距，避免字符被遮挡  pushViewport(viewport(x = 0.45, width = 0.9))  draw.pairwise.venn(    area1 = length(set1),    area2 = length(set2),    cross.area = length(intersection),    category = c("seurat_vst", group_name),    fill = c("#1f77b4", "#ff7f0e"),    alpha = 0.6,    lwd = 2,    fontface = "bold",    fontfamily = "sans",    cat.cex = 1.2,    cex = 1.5  )}
```
```
## seurat_vst vs seurat_mvp 交集基因数: 787
```

![](../../images/d5e7c049ceeeb123.webp)

```
## seurat_vst vs seurat_disp 交集基因数: 1113
```

![](../../images/fe2f34ad4d06850d.webp)

```
## seurat_vst vs scanpy_seurat_v3 交集基因数: 1728
```

![](../../images/4b74b2e6c1adab24.webp)

```
## seurat_vst vs scanpy_seurat 交集基因数: 1107
```

![](../../images/515cf20f7575421d.webp)

```
## seurat_vst vs scanpy_cell_ranger 交集基因数: 1253
```

![](../../images/b48f337895a03e80.webp)

（3）UpSet图（适合6个集合的交集可视化）

  *   *   *   *   *   *   *   *   *   *   *   *

```
# 正如预期，UpSet中Seurat-vst和Scanpy-seurat_v3交集是最多的，虽然可能和预期的有一定差异，不是完全一致，但是benchmarking也提到这个可能是由于有的基因之间存在表达冗余导致没有被选择进来upset(  fromList(gene_list),  nsets = 6,  number.angles = 30,  point.size = 3.5,  line.size = 2,  mainbar.y.label = "Intersection Size",  sets.x.label = "Gene Set Size",  text.scale = c(1.2, 1.2, 1, 1, 1.5, 1),  order.by = "freq")
```

![](../../images/a27c670d1e8148de.webp)

3.8 总结

综合以上，大家后续在使用Seurat或者是Scanpy进行多样本整合或者是单样本分析的时候，如果还纠结于高变基因如何选择的话，不妨先来看看我们这个测试教程。优先推荐大家使用Seurat-vst（R语言）或者是Scanpy-seurat_v3（Python语言）方法计算得到的高变基因进行降维分群。高变基因数目2000即可达到优秀的分群结果。

**三、参考**
```
[1] Zappia, L., Richter, S., Ramírez-Suástegui, C. et al. Feature selection methods affect the performance of scRNA-seq data integration and querying. Nat Methods 22, 834–844 (2025). https://doi.org/10.1038/s41592-025-02624-3
```
```
[2] https://github.com/satijalab/seurat
```
```
[3] https://github.com/scverse/scanpy
```

**四、资料领取**

更多编程教程可见：

[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)

[5.5小时掌握R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535038&idx=2&sn=717a8673a8bf82d5ac40af4441a07f65&scene=21#wechat_redirect>)

[生信python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520999&idx=2&sn=7f6aa90c2ffa786bd660aa40b109de49&scene=21#wechat_redirect>)

一切不给测试文件的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：

![](../../images/cf46f2591705aaed.png)

链接: https://pan.baidu.com/s/1TWhFvNuoux1uwPrBJUOQdg

提取码: 6kck

![](../../images/72b5a0e3fcb7f5a9.webp)![图片](../../images/cb4255ab8010219d.gif)

**欢迎致谢**

如果以上内容对你有帮助，欢迎在文章的Acknowledgement中加上这一段，联系客服微信可以发放奖励：
```
Since Biomamba and his wechat public account team produce bioinformatics tutorials and share code with annotation, we thank Biomamba for their guidance in bioinformatics and data analysis for the current study.
```

**欢迎在发文/毕业时向我们分享你的喜悦~**

**已致谢文章**

[ 鼻咽癌的Bulk RNA-Seq与scRNA-Seq联合分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510548&idx=1&sn=58048c46e837b1d56dffa282272c6d96&chksm=9b3cd344ac4b5a52369e91b4e61fa0a2c951b82cc21165b99f42ba2c2191d4add803bd73c928&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)

[13分+文章利用scRNA-Seq揭示地铁细颗粒物引起肺部炎症的分子机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511886&idx=1&sn=31c712d00377b0f0ed33703b5b4fbfd8&chksm=9b3cd61eac4b5f084fde14a2eb50356f2f40a66c608d38909f12a3d81f48cff029a09ce2ee8c&token=1453608870&lang=zh_CN&scene=21#wechat_redirect>)

[除了铁死亡，还有铜死亡？！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247518144&idx=1&sn=d036f1bb04b09eb73f53e2104d69404c&chksm=9b3cfe90ac4b77862f2f463b42132c7bfdb687a1b61d350dcf656117b1331271e179710fd4fa&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)

[IF14.3| scRNA-seq+脂质组多组学分析揭示宫内生长受限导致肝损伤的性别差异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520900&idx=1&sn=157134292ffc2e5df730c5ba8a357b61&chksm=9b3cebd4ac4b62c286543c30381e9b4fdb8b44b28d4fa902fb963bbd45b28e1d3f1bc98eb148&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)[银屑病和脂肪肝病中共同病理和免疫特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521069&idx=1&sn=4ef441a885cb2525ee3b5c81001feddf&chksm=9b3cea7dac4b636be9f10ffdf75e13531fccae62129944b21a457db2e08c3f2db1e1b553ac34&scene=21&cur_album_id=3425248581018714114#wechat_redirect>) [《Advanced Science》新型Arf1抑制剂促进癌症干细胞衰老并增强抗肿瘤免疫](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522233&idx=1&sn=287a380de741ff55f0ce78dc9c727985&chksm=9b3ceee9ac4b67ffd925abafeba2cb215a5984e6dc85f0d8607340a07ec9208f1d19eae0e04b&scene=21#wechat_redirect>)

[scRNA-seq揭示脓毒症预后水平预测的关键靶点！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522281&idx=1&sn=f95eb12fdc340b8da1123ec6253e6fac&chksm=9b3ceeb9ac4b67afa587e5fa3a2a8960e9bb28a1ad6dc48e49120a76154417a4c8be95af90b0&scene=21#wechat_redirect>)

[机器学习+生信多组学联合构建牙周炎"线粒体功能障碍与免疫微环境"关联网络](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527168&idx=1&sn=0791d2bf53a9a60015577f892b10d370&scene=21#wechat_redirect>)

[KIF18A在肝细胞癌转移中的双重角色](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528014&idx=1&sn=d285c9ebd415be328fc682d00e6182c0&scene=21#wechat_redirect>)

[bulk+scRNA-seq挖掘BCL2-MAPK14-TXN氧化应激诊断模型，鉴定脓毒症中氧化应激关键基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530000&idx=1&sn=e8ddca4e1b2e60839cdf2a7fe87b3dfe&chksm=9b3c0f40ac4b86562e0e307b9dbb8688159e72b3c19d9ceebf8a4bb2e21638896f005b497b11&scene=21&cur_album_id=3425248581018714114&search_click_id=#wechat_redirect>)

[致谢文章+1，中科院1区，scRNA-seq揭示麻黄-甘草配对治疗呼吸系统症状和多(I:C)诱发肺炎模型机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536407&idx=1&sn=4da88e13f112662a02fea89d1b7798e9&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/acba43cb3408c3d0.gif) 您点的每个赞和在看，我都认真当成了喜欢
