---
title: "iTalk：躺在预印刊的细胞通讯工具"
date: 2025-06-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529428&idx=2&sn=f4a21753d435a90985049b55ddde43cf&chksm=9b3c0a84ac4b8392fbb0008dd8e06ff92212e13d60e555dd6066a2c9ba4d7591091bd4710f49#rd
albums: ["文献速递"]
---

# iTalk：躺在预印刊的细胞通讯工具

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529428&idx=2&sn=f4a21753d435a90985049b55ddde43cf&chksm=9b3c0a84ac4b8392fbb0008dd8e06ff92212e13d60e555dd6066a2c9ba4d7591091bd4710f49#rd
> 合集：文献速递

**一、写在前面**

这次介绍的是一个基于R语言的细胞通讯分析工具——iTALK，这是笔者目前用起来觉得对用户最友好的工具，奇怪的是截至推送发稿，这篇文章仍然仅发表在预印刊上，未被其它期刊正式接收(距离其2019年1月发表在预印刊上，已经过去了六年半)。感兴趣的同学可以看一下原文：https://www.biorxiv.org/content/10.1101/507871v1 完整教程可见：[scRNA-Seq细胞通讯之《iTalk学习手册》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528921&idx=1&sn=7584797c68f0e979112b6dd2e4e30f14&scene=21#wechat_redirect>) 更多单细胞教程可见：

[一文学会四种scRNA-seq细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)

[scRNA-seq数据分析小白全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529379&idx=1&sn=10283cee636a7bc706f145edc791fe7c&scene=21#wechat_redirect>)

**二、细胞通讯与iTalk**

肿瘤细胞与肿瘤微环境（TME）中其他细胞之间的相互作用在肿瘤进展、转移以及耐药性中扮演着至关重要的角色。作者介绍了 iTALK，一种基于计算的方法，用于表征和展示多细胞肿瘤生态系统中的细胞间通讯信号，利用单细胞 RNA 测序数据。iTALK 原则上可以用来解剖细胞间通讯的复杂性、多样性和动态变化，涵盖广泛的细胞过程。
肿瘤微环境（TME）已成为调节肿瘤进展、免疫逃逸以及抗肿瘤治疗耐药机制的重要因素。TME 包含多种细胞类型，例如肿瘤细胞、多种类异质的免疫细胞，以及非免疫的基质成分。肿瘤细胞与这些非肿瘤成分之间进行动态的协调和相互作用，彼此间的相互信号被认为提供了指导和促进肿瘤细胞生长与迁移的关键信号。通过这种细胞间通讯，肿瘤细胞能够在其他 TME 细胞（如肿瘤相关成纤维细胞、巨噬细胞和 T 细胞）中引发显著的表型变化，并对 TME 进行重编程，从而逃避免疫监视以促进其生存。因此，更好地理解细胞间通讯信号可能有助于识别新的调节治疗策略，从而更好地造福患者。然而，由于缺乏有效的数据分析和可视化的生物信息学工具，这一研究进展受到限制。作者介绍了 iTALK（识别和展示细胞间信号网络的变化；https://github.com/Coolgenome/iTALK），这是一个开源的 R 包，旨在从单细胞 RNA 测序数据（scRNA-seq）中分析和可视化配体-受体介导的细胞间相互作用信号（见图 1 和在线方法）。作者展示了 iTALK 可以成功应用于 scRNA-seq 数据，捕捉到高度丰富的配体-受体基因（或转录本）对，识别细胞间相互作用的增减变化，并追踪纵向样本中细胞间通讯信号的动态变化。值得注意的是，作者精心编制的 iTALK 配体-受体数据库会自动为配体-受体基因添加功能注释，且结果可以通过作者高效的数据可视化工具以不同格式进行展示，该工具是 iTALK 的一部分。这种方法适用于从数百个到数万个细胞的数据集，并且不受限于测序平台。值得一提的是，除了研究 TME，iTALK 还可以应用于涉及细胞间通讯的广泛生物医学研究领域。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxb5BookcM4fB9lFicSD2hw6gRkNVibvu1RmUjlJiatic3ibEjw1bVOricDialpfmmcQUuJpw8Btbm8BSicng/640?wx_fmt=png&from=appmsg)**图 1.iTALK的生物信息学工作流程及其输出图示格式。iTALK以单细胞RNA测序的细胞-基因表达矩阵作为输入。根据研究设计对数据矩阵进行处理。已知的配体和受体基因被筛选、配对并通过内置的配体-受体数据库进行功能注释。最终，输出结果可以通过数据可视化工具（该工具作为iTALK的一部分实现）以不同格式进行可视化。**

配体-受体结合是邻近细胞和远离细胞之间信号转导的主要形式之一。为了表征配体-受体介导的细胞间相互作用，作者首先基于之前的研究手动整理了一个独特的配体-受体基因对列表，并将其作为 iTALK 的内置数据库。这一数据库收录了 2,648 对非冗余的已知互动配体-受体对，并根据配体的主要功能将其进一步分类为四类：细胞因子/趋化因子、免疫检查点基因、成长因子和其他（见图 1 和在线方法）。该数据库将定期更新，用户也可以选择输入自己的基因列表或自定义基因类别。由于不同的细胞类型可能对同一配体具有不同的受体，并且可能诱导不同的反应，反之亦然，iTALK 在分析数据时将每一对不同的配体-受体视为独立事件。而且，由于功能上的异质性，同一配体-受体结合在不同类型/表型的细胞中可能会引发独特的细胞反应，与其遗传身份无关。因此，单细胞 RNA 测序数据是确定哪种细胞类型/表型表达哪种配体或受体，并帮助更准确地绘制细胞间通讯网络的理想平台。

**三、iTalk介绍**

iTALK 以单细胞 RNA 测序（scRNA-seq）数据中的细胞-基因表达矩阵作为输入。表达数据可以是原始数据或经过标准化的数据。数据矩阵将根据研究设计进行解析和处理。对于在单一时间点或单一组/队列中收集的数据集，iTALK 可以通过生成排序基因列表来识别高度表达的配体-受体对，然后使用 iTALK 数据库进行配体和受体的搜索和配对。对于在多个时间点进行纵向收集的数据集，或包含多个遗传学/组织学不同的亚组或队列的数据集，iTALK 可以通过查找和排序差异表达的配体和/或受体，识别组间的显著变化，即互动的增加或减少（见图 1）。iTALK 结合了常用的算法进行批次效应修正和差异基因表达分析（见在线方法），同时允许用户根据数据的特点选择最适合的方法。iTALK 还是一种高效的数据可视化工具。iTALK 的输出可以以多种格式进行可视化，包括网络图、circos 图、误差条形图，同时数值也可以以表格形式导出（见图 1-2）。网络图通过分别标记网络中每两种不同细胞类型之间检测到的配体-受体相互作用的前向（从信号细胞到靶细胞）和后向信号数量来进行展示。它还测量每种细胞类型内的自分泌信号。网络图的节点按细胞类型进行颜色编码，边按比例缩放并标记信号细胞和靶细胞之间的相互作用数量（见图 2a）。Circos 图显示每对配体-受体基因的名称，并展示每个相互作用的方向。用户可以选择在 circos 图中显示哪些细胞类型、基因类别和相互作用数量（见图 2b-c）。Circos 图的外环显示细胞类型，内环显示每个相互作用的配体-受体对的详细信息，两者均使用颜色编码。Circos 图内部的线条和箭头按比例缩放，以分别指示配体和受体的相对信号强度，同时使用不同颜色和类型的线条来描绘图 2 中所示的各种可能的变化。它可以展示在单一时间点或组/队列场景中高表达的配体-受体信号（见图 2b-c），或展示两个或多个时间点或亚组/队列之间变化最大（增加或减少）的配体-受体相互作用（见图 2d-e）。对于大多数配体-受体介导的相互作用，配体似乎只有在与其受体结合时才能发挥作用。因此，作者预计当受体表达缺失（或减少）时，无论其配体的表达水平如何，相互作用都会丧失（或减少），反之亦然。误差条形图用于展示多个时间点中特定感兴趣的配体-受体对的动态变化（见图 2f）。所有带有注释信息的 iTALK 数值也可以以表格形式导出（见图 1），用户可以通过排序/筛选来选择某些相互作用以进行进一步的下游分析或自定义绘图。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxb5BookcM4fB9lFicSD2hw60eiav8Z1dldCgHdzRpGicLu5AZJZa1Jjucf8weFY7hcB9WZdMibhcQYSg/640?wx_fmt=png&from=appmsg)**图2. iTALK输出结果的不同格式可视化。a.网络图展示了不同细胞类型之间以及同一细胞类型内检测到的配体-受体相互作用数量；b-c.Circos图展示了单一时间点、组或队列中前20个高表达的配体-受体相互作用；d. Circos图展示了包括两个亚组或队列的研究；e. 用于纵向研究，展示了细胞相互作用的显著变化；f.误差条形图展示了特定配体-受体对在多个时间点的动态变化。**
作者已成功将iTALK应用于内部生成和公开下载的多个单细胞RNA测序（scRNA-seq）数据集。这种方法可以应用于从数百到数十万个细胞的数据集，并且不受测序平台的限制。除了研究肿瘤微环境（TME）外，作者预计iTALK还可以应用于涉及细胞间通讯的广泛生物医学研究领域，以帮助剖析复杂的细胞间信号网络。
**数据库与注释** 内置数据库是根据之前的成果3-10手动整理的。将基因列表合并并去除重复项，以创建一个非冗余的配体-受体列表。该数据库总共包含2648个独特的配体-受体相互作用对。作者根据配体的已知功能，将它们进一步分为四类：细胞因子/趋化因子（n=320）、免疫检查点（n=31）、生长因子（n=227）和其他（n=2070）。作者预计将定期更新数据库，以确保其时效性。除了内置数据库外，用户还可以选择输入自己的配体-受体基因列表。用户还可以根据需要自定义基因类别。输入数据格式、数据解析、过滤、去除批次效应。输入数据应为细胞基因表达矩阵，并为每个细胞注释细胞类型或表型。原始数据应根据质量控制指标进行过滤。默认标准是过滤出在少于3个细胞中检测到的基因，以及细胞中计数非零的基因少于200个的细胞。如果细胞中超过15%的计数来自线粒体基因组，则这些低质量细胞也将被丢弃。对于可能存在批次效应的测序数据，可以使用scde11和monocle12（已集成到iTALK中）来消除它们。**识别显著的相互作用** 作者集成了多种算法来识别显著的相互作用（差异表达的配体和受体），包括常用的R包：DESeq214、scde11、monocle12、DEsingle15、edgeR16和MAST17。用户可以灵活选择最适合其数据集的方法。所有这些方法都要求输入数据为原始数据，不进行任何过滤或标准化。考虑到单细胞测序数据有时可能包含数千或数万个细胞，作者还提供了Wilcoxon方法，以加快数据处理速度。Wilcoxon方法的输入数据可以是原始数据或处理过的数据。在找到高表达或差异表达的基因后，这些基因将与作者的配体-受体数据库进行匹配和配对，以识别显著的配体-受体相互作用。为了识别信号传递相互作用的变化，会评估配体和受体的表达水平。作者定义“交互作用的增加”为：如果配体（或受体）基因上调，并且其配对基因上调或保持不变，则认为交互作用增强。作者定义“交互作用的丧失”为：如果配体（或受体）基因下调，不论其配对基因的表达水平如何，均视为交互作用丧失。图示。网络图、Circos图和误差条形图均采用了颜色编码，用户可以选择自己喜欢的颜色（例如，用于细胞类型、基因类别、变化强度和方向等）。此外，用户可以选择显示的细胞类型数量（如肿瘤细胞、T细胞、NK细胞、巨噬细胞、成纤维细胞等）或基因类别（如细胞因子/趋化因子、免疫检查点、生长因子及其他），以及Circos图和网络图中显示的相互作用数量（前30、50、100或全部）。网络图是基于R包igraph18生成的；Circos图是基于包circlize19绘制的；误差条形图则是基于ggplot220创建的。**示例数据集** 作者的示例数据集由内部生成。这些数据通过Seurat13进行了过滤和标准化。细胞类型的定义基于已知的标记物。简而言之，B细胞通过CD79A、CD79B和MS4A1进行识别；T细胞通过CD3D/E进行识别；CD8 T细胞通过CD3D/E和CD8A进行识别；NK细胞通过CD45、NKG7和GZMA进行分类；单核细胞则通过CD68、CD163和S100A8/9进行识别。作者应用了Wilcoxon方法来寻找不同组之间的显著相互作用。**代码可用性** 代码和内置数据库可以在GitHub上公开获取，网址为https://github.com/Coolgenome/iTALK

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
