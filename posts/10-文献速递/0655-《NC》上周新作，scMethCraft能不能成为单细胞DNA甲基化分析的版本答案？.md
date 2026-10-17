---
title: "《NC》上周新作，scMethCraft能不能成为单细胞DNA甲基化分析的版本答案？"
date: 2026-05-19
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538066&idx=1&sn=65cfc72d44539598b994922f8e33d0a9&chksm=9b3c2cc2ac4ba5d4478182089c23a674c7d8e19f520c0e6870e1c5b46456aa3e1c3d5b4d17d6#rd
albums: ["文献速递"]
---

# 《NC》上周新作，scMethCraft能不能成为单细胞DNA甲基化分析的版本答案？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538066&idx=1&sn=65cfc72d44539598b994922f8e33d0a9&chksm=9b3c2cc2ac4ba5d4478182089c23a674c7d8e19f520c0e6870e1c5b46456aa3e1c3d5b4d17d6#rd
> 合集：文献速递

**一、写在前面**

5月16号新鲜online的《NC》，题为"Dissecting epigenetic heterogeneity in single-cell DNA methylomes with a unified framework"，由南开大学和[北京寻因生物](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247524500&idx=1&sn=bb3b9a15785d2a8095eb59eb7a417f14&scene=21#wechat_redirect>)共同发表。还没正式出版，大家可以看看抢先版。 不知道scMethCraft会不会像[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535877&idx=1&sn=e988a2172618fd6f609575294db9a44f&scene=21#wechat_redirect>)、[Scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)这些包一样成为版本答案呢。

[scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535927&idx=2&sn=86947f0522de0d9785865bd24115b002&scene=21#wechat_redirect>)现在卷的没边，考虑转移阵地的话，单细胞DNA甲基化（scDNAm）测序为剖析表观遗传异质性和基因调控机制新见解。然而，现有的分析方法大都是从scRNA-seq框架改编的，并不能说明scDNAm数据的独特特征。为了能够以单细胞分辨率系统地探索DNA甲基化衍生的表观遗传变异，该文章提出了scMethCraft，一个多功能的分析工具包。scMethCraft通过混合神经网络集成了多视角的基因组序列特征和甲基化区域的位置信息，并迭代量化细胞间关联，实现scDNAm数据准确建模。scMethCraft支持一系列下游分析，包括细胞嵌入，多源数据整合、细胞类型注释、表观遗传信号增强和差异甲基化区域的鉴定。scMethCraft能够与互补分析工作流程的整合，包括生物学功能富集、组织特异性表达分析和分区遗传性评估。当然，你如果对单细胞甲基化分析思路感兴趣的话，不妨免费领个学习"蓝皮书"![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/buxFNhaTGwk9kpj3P9micT3jZOE1bcpnicibG6weVXhoxPicfDAsHmIgQpBwPSz4SqM9yhJQtiad7cNO5W8SO9W8MCKZtzeHlPNdzn0Cw6kPz5GU/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/buxFNhaTGwn7tXBmGpXQaicmWm1IzIWWmvpCZhTgqs0tuPHm0yXmcAw92JicHD6pqW9wVS2pzlsoibHCfZ2xyPamU4TUOt0NfKBaKza9wGzy4s/640?wx_fmt=jpeg&from=appmsg)

参考文献：Tang S, Li S, Zhang G, Lyu A, Li H, Chen S. Dissecting epigenetic heterogeneity in single-cell DNA methylomes with a unified framework. Nat Commun. 2026 May 15.

**二、背景知识**

1、单细胞甲基化分析现状

在哺乳动物基因组中，DNA甲基化主要发生在CpG位点。尽管许多现有的方法以单CpG位点分辨率分析scDNAm数据，但仍存在scDNAm数据[稀疏性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529675&idx=1&sn=4d16321d68430f9a1c2d20fb77234d24&scene=21#wechat_redirect>)和噪声、通量的限制。与单CpG位点分析相比，在分析scDNAm数据时，初始步骤包括通过基因组分箱聚集来自多个甲基化位点的信号，从而减少数据量，提高信噪比，和提高可解释性。

甲基化与转录组数据最大的差别是，如果基因组区域内没有读数，则该区域的平均甲基化水平则为NA。而scRNA-seq或[scATAC-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&scene=21#wechat_redirect>)数据未观察到的计数通常被视为零。这意味着scDNAm矩阵的值分布不同于其他组学数据。基因组分箱表示平均甲基化水平范围，即连续地在0和1之间，这与[scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535927&idx=2&sn=86947f0522de0d9785865bd24115b002&scene=21#wechat_redirect>)或[scATAC-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536784&idx=1&sn=35754d32e7acbb0208a05917c7a1590b&scene=21#wechat_redirect>)数据中观察到的reads数的整数分布也不同。更重要的是，DNA甲基化数据与其他单细胞组学相比在数值尺度和生物学意义上存在根本差异。在[scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537658&idx=2&sn=f3adf25c6d116aa2fcc4ef6f9cc9bc2e&scene=21#wechat_redirect>)或[scATAC-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534015&idx=1&sn=04da5c98bee2ac3497b6fe412e0efd41&scene=21#wechat_redirect>)数据中，较高的reads计数通常对应于较强的生物信号，例如较高的基因表达或染色质可及性。但甲基化水平更高往往会抑制基因表达。

2、scMethCraft能够做到什么？

针对以上问题，scMethCraft提供了一个完整的分析scDNAm矩阵的分析流程。能直接对具有NA值的scDNAm矩阵进行操作，并通过混合神经网络架构整合DNA序列和基因组位置信息。通过引入迭代更新的细胞间相似性模块，scMethCraft提高了建模精度并降低了预测偏差，为scDNAm数据实现了有效的降维和稳健的细胞聚类。助于整合来自不同来源的scDNAm数据集，减轻批次对下游分析的影响，同时为跨数据集细胞类型注释提供可靠的基础。此外，scMethCraft在通过合并细胞间相似性信息对scDNAm矩阵进行去噪的同时估算NA值。scMethCraft能够识别差异甲基化区域（DMR），通过细胞类型特异性DMR模式，能够识别基因调控程序，组织特异性表达富集，疾病风险的遗传性。

三、详细结果

1、scMethCraft模型

在scMethCraft模型的基本框架中（图1a），首先将scDNAm细胞-区域矩阵𝐗∈𝑅𝑝×𝑛作为输入，其中𝑝表示基因组区域的数量（默认bin大小为10 kbp），𝑛表示细胞的数量。

对于每个基因组区域，scMethCraft检索对应基因组索引，提取DNA序列，并获得序列编码。其次，对于每个给定的基因组区域，引入序列特征提取模块来建模相应的序列并预测所有细胞的甲基化水平。最后，scMethCraft提供了一个增强的scDNAm矩阵∈ ×𝐗𝐞𝐧𝐡𝐚𝐧𝐜𝐞𝐝，并且可以从该模型𝑅𝑝中𝑛导出细胞间相似性矩阵𝐒𝐧𝐨𝐫𝐦∈𝑅𝑛×𝑛和细胞嵌入𝐇值∈𝑅 50 ×𝑛，用于下游分析。

scMethCraft的序列特征提取模块利用混合神经网络(卷积神经网络（CNN）和全连接神经网络（FCNN）)有效地捕获DNA序列特征（图1b）。此外，引入Kolmogorov-Arnold网络（KAN）来融合CNN和FCNN模块生成的特征嵌入，并将位置信息合并到最终的特征嵌入中。该混合神经网络为每个区域生成50维特征嵌入，随后将其带入具有加载矩阵的密集线性层，以预测给定基因组区域的不同细胞中的DNA甲基化水平（方法）。作为一个全面的scDNAm数据分析工具包，scMethCraft提供了广泛的适用性，如降维、可视化、细胞聚类、批量集成、细胞类型注释、数据增强、和DMR的识别（图1d）。

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnVBSodaH8CyiaRgFt8p4L7Lt9WkeBciciaj08sltPm4jXn4Nr4OOahumaFATRRtOK4LODriaIVDUYqHj7ER3eH7haIUiaKJ5dDty64/640?wx_fmt=png&from=appmsg)

图1

2、scMethCraft解析潜在空间中细胞群体之间的表观遗传异质性

为评估scMethCraft对全基因组scDNA数据的降维能力。作者收集了11个数据集，其特征在于不同的方案、供体和不同的细胞数量，并附有详细注释的主要细胞类型和亚群分类。以MethSCAn、EpiScanpy、SnapATAC作为基准。作者对scMethCraft生成的细胞嵌入向量进行了无监督聚类，并使用Louvain算法和二进制搜索策略为基线方法。计算完成后，通过五个指标评估聚类性能，包括调整后的兰德指数（ARI）、调整后的互信息（AMI）、归一化互信息（NMI）、同质性得分（Homo）和Fowlkes-Mallow指数（FMI）。

与基线参考方法相比，scMethCraft表现出显著的性能改进。在11个数据集上，scMethCraft始终获得高AMI评分（图2a）、scMethCraft的AMI评分平均为0.77，比MethSCAn提3.12%，比SnapATAC2提5.38%（图2b）。 scMethCraft在所有五个评估指标和11个数据集上展示了整体最先进的性能。单侧配对Wilcoxon符号秩检验的统计分析证实scMethCraft一致且显著优于基线方法，P值小于0.0 5（图2 d）。

在可视化与定性评估中，即使与表现较好的基线方法（EpiScanpy和MethSCAn）相比，scMethCraft在分离主要细胞类型、捕捉细胞群体间的细微差异方面也展现出了明显优势。以脑组织（ACC数据集）为例，OPC、ODC和MGC同属神经胶质细胞，表现出高度相似性，EpiScanpy（图2e）和MethSCAn（图2f）很难将其准确聚类；相比之下，scMethCraft有效地区分了这三种细胞类型（图2g）。同样，LAMP5基因座的尾神经节隆起衍生抑制性神经元（包括Lamp5和Lamp5-Lhx6亚型）在基线方法中未被明显区分，而scMethCraft成功捕捉到了这些细微差别，并在AMI上实现了高达10%的改善。在M1C数据集中，面对Vip、Sncg、Lamp5和Lamp5-Lhx6这四种高度异质的细胞类型，只有scMethCraft准确捕获了其潜在异质性，实现了生物学上有意义的精确聚类，AMI改善了约20%（图2h-j，补充图3-5）。

除了在脑组织中的卓越表现，为了验证模型在解析不同组织系统表观遗传异质性上的广泛适用性，作者还引入了由[寻因生物（SeekGene）](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536784&idx=1&sn=35754d32e7acbb0208a05917c7a1590b&scene=21#wechat_redirect>)提供的外周血单核细胞（PBMC）数据集。该数据集具备寻因独有的“[高通量一胞双组”（单细胞DNA甲基化 + 转录组）技术特性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534762&idx=1&sn=08d8c49dbc901dc56c22ab2d77db3b88&scene=21#wechat_redirect>)。作者首先利用转录组完成了高置信度的细胞注释，并通过单细胞 Barcode 将真实标签精准映射至甲基化维度，以此作为客观的评估基准。结果表明，即便面对高度复杂的免疫系统，scMethCraft在仅输入甲基化数据的情况下，依然展现出优异的细胞分群能力。它能有效提取甲基化特征，准确区分各类免疫细胞亚型，高效捕捉细微的表观遗传差异，将高度复杂的细胞间异质性清晰地剥离与展现。这一结果不仅充分印证了scMethCraft算法强大的降维与异质性解析能力，也凸显了[寻因“一胞双组”技术](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534762&idx=1&sn=08d8c49dbc901dc56c22ab2d77db3b88&scene=21#wechat_redirect>)在为前沿算法提供高质量基准测试及复杂样本表观图谱深度解析中的核心应用优势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnkDZHZBkCgNoXibQxACcvHGahmMOLKvX6I7Z2qGhvC6d3kglqlAHibRRUQcicxQJPZLfXAYwWxKYFKUwe3RRqLHp5GYxQlNbIQ6c/640?wx_fmt=png&from=appmsg)

scMethCraft 与主流基线方法甲基化数据降维聚类效果对比

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlRlibU1wMs0NwXvyUgEWLEKibDTo0w1d88icib9wEnylxDSAPdS9AqLoj1T2H9mQMzobUbibAiaAeoXWWx0nr8QnKqV67m13RjXnUvA/640?wx_fmt=png&from=appmsg)

寻因生物一胞双组数据分群注释结果展示（PBMC）

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmOhgHL0unHJUibkbPR9vE6juWTVXChoHtCOqIll7D6CdqCLoyb8BGPLa8qLRQichpSsEEZWzFt9N6OQDR1rsPssbaATPGF8aayg/640?wx_fmt=png&from=appmsg)

图2

3、scMethCraft支持多来源数据去批次整合

学过我们[scRNA-seq多样本整合](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&scene=21#wechat_redirect>)再熟悉不过，多来源样本的数据整合需要处理很令人头疼的[批次效应](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495992&idx=1&sn=db352382575954d0d62938ca4e61043e&scene=21#wechat_redirect>)，不同来源、组织、供体或批次的scDNA m数据集通常表现出系统性差异。

例如，我们将EpiScanpy的分析流程应用于从不同大脑区域和供体收集的MTG和Pro数据集。批次之间出现明显的批次效应，导致聚类结果主要反映了批次间的差异，而不是真实的生物学变异（图3a,b）。如图3c所示，来自MTG数据集的L2/3 -IT细胞被分配到簇3和9，而来自Pro数据集的L2/3-IT细胞被分组到簇2、8和10），突出了批次效应对scDNAm数据的下游分析的混杂影响。

因此，scMethCraft引入了对细胞相似性矩阵的校正，以促进跨批次信息整合并实现有效和准确的批次效应校正（补充图7）。在组合的MTG-Pro数据集上，scMethCraft有效地整合了来自不同批次的细胞，同时保留了生物学方差并避免了过度校正（Fig.3 d,e）。如图3f所示，整合的L2/3-IT细胞主要分为四个簇。在这些簇中，两个数据集的三个簇（簇2、4和5）由一个大的细胞簇组成。即在去批次中不但能准确区分同一细胞类型，也不会掩盖细胞亚群(Fig.3g)。

作者进一步将六个人类scDNAm数据集配对，以生成三个集成数据集：MTG-Pro、A46 -ACC和A5 A7-M1C。这些用于全面评估scMethCraft的批次整合性能。根据先前的研究，我们评估了批次校正指标和生物方差守恒指标。所有指标均使用主要类型和亚型评估。图3h总结了scMethCraft在三个数据集上的批次校正度量的平均性能，而图3 i显示了平均生物方差保守性得分。scMethCraft在所有批次整合指标上都取得了显著的改进。将所有六个数据集合并为混合数据集后，与EpiScanpy相比，scMethCraft改进了所有批次整合指标（图3 j），可视化显示批次效应显著减轻（图3 k,l和补充图11）。这些结果表明scMethCraft即使在复杂的多批次情况下也保持准确，从而促进来自不同来源的scDNAm数据联合分析，使研究人员能够专注于具有生物学意义的甲基化模式差异，而不是技术差异或批次效应。

4、scMethCraft自动细胞类型注释

与我们学习单细胞时用到的[Transferlabel、singleR](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&scene=21#wechat_redirect>)等工具类似，甲基化组学的分析也可以利用已注释好的数据集将标签传递给新的数据集。scMethCraft提供了一种简单、无需预训练和批量效应鲁棒的细胞类型注释策略。具体地，scMethCraft有效地利用学习的自适应相似性矩阵来识别给定细胞的最近邻居，推断每个查询细胞的最可能的细胞类型，从而实现准确的跨批次注释而不需要额外的模型训练。

作者使用六个人脑scDNAm数据集从多个角度系统地评估了跨批次细胞类型注释性能。在每次评估中，指定一个批次作为参考，其余五个批次作为查询集，并使用宏F1值进行定量评估。鉴于目前缺乏专门针对scDNAm数据设计的自动化注释方法，作者使用已经广泛应用于其他单细胞组学数据的细胞类型注释经典分类器作为基线方法，包括支持向量机（SVM）和K=5和K=10的k -最近邻（KNN），在EpiScanpy生成的嵌入向量上进行训练。

对于主要类型的注释，所有方法都取得了良好的性能然而，当使用A5 -A7数据集作为参考时，某些主要细胞类型（例如MGC）的注释由于它们在参考中的相对低丰度而变得困难。即使是替代方案中表现最好的基线模型SVM，如图3 m所示，SVM错误地将大多数MGC分配给L2/3 -IT或Pvalb细胞，并将丰富的OPC细胞错误地分类为ODC。相反，scMethCraft受益于其迭代优化的相似性表示，实现了OPC和MGC的近乎完美的注释，导致注释准确性的显著提高（图3n）。scMethCraft表现出实质性更优的性能，在所有六个评估中实现了最高的准确度（图3 o）。总之，scMethCraft在不同水平的注释粒度下在批次中实现了高注释准确度，使得能够从DNA甲基化的角度稳健地鉴定细胞身份。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkDPicqkehTmvU4TYQWNHrtZNlppsBbsBnUl4uiar6STrWQM7u7xbQNISXy5o1yPLcDkDPiapqm9HmkC1yP3BUjRFNia7E3YvoiaKsM/640?wx_fmt=png&from=appmsg)

图3

5、scMethCraft有效地插补并增强scDNAm信号

scDNAm矩阵通常包含噪声和相当大比例的NA值，这显著阻碍了DNA甲基化模式的表征和下游分析的实施。scMethCraft利用序列信息和细胞-细胞相似性来模拟scDNAm分布，对矩阵进行降噪，并估算NA条目，从而实现有效的数据增强。

作者首先评估了scMethCraft对scDNAm矩阵进行估算和降噪的能力。对于每种主要细胞类型，我们通过对属于相同细胞类型的细胞的甲基化水平取平均值来构建元细胞，然后使用每个单细胞及其相应元细胞之间的斯皮尔曼相关性来评估数据重建保真度。以ACC数据集为例（图4a,B），原始数据显示出与所有细胞类型的元细胞的低相关性，突出了噪音的不利影响。相比之下，scMethCraft大大改善了个体细胞与其相应元细胞之间的斯皮尔曼相关性，表明对潜在甲基化分布的真实地重建。我们进一步关注原始矩阵中最初注释为NA的区域，在计算与元细胞的相关系数时，只考虑这些区域，表示为scMethCraft（NA），以评估是否可以真实地重建单细胞甲基化谱中的缺失值，尽管这些条目在训练过程中没有被直接观察或使用，但它们仍然保持与元细胞的高度相关性（图4a），证明了scMethCraft基于学习的序列特征和细胞间相似性推断准确甲基化水平的能力。

为了直观地可视化原始scDNAm矩阵，可以通过scMethCraft有效地估算生成原始矩阵的热图（图4B）和scMethCraft增强矩阵（图4c）。显然，原始数据显示出大量的NA值和技术噪声（NA值在热图中显示为白色），导致不同细胞类型之间的图案模糊。不同细胞类型的DNA甲基化模式变得清晰可辨。相比之下，scMethCraft在多个数据集上的表现始终优于这些基线方法，强调了其数据增强能力的鲁棒性和普遍性（图4d）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlyu13Ca5Mqia2FK6p5o2r81bQkr2x9ibLFXtBhicxNdsicyriaetpUiaedXbUj54KbLq4jgkYggOJQ9icobgTTA6x64IiawV79Y6XvwyM/640?wx_fmt=png&from=appmsg)

图4

此外，作者验证了scMethCraft进行的数据增强是否与已知的生物学先验一致。在图3中，ACC数据集的所有细胞被分为三类：非神经元细胞、抑制性/非端脑神经元和端脑兴奋性神经元。在CellMarker数据库中，STMN 2被标记为兴奋性神经元的标记基因。鉴于基因表达通常与甲基化水平呈负相关，作者查询了与STMN 2基因重叠区域的平均甲基化水平，并根据甲基化水平对UMAP进行着色。原始数据中的DNA甲基化模式是无序的（图4f）；如图4g所示，STMN 2显示出更明显的甲基化模式，其特征在于端脑兴奋性神经元中的低甲基化和其他两类中的高甲基化。类似的观察结果在MAP 2和SATB 2基因（神经元的另一个标记物）的增强数据中得到进一步验证（补充图8）。

最后，我们进行了额外的掩蔽实验，以评估scMethCraft是否可以在极端缺失的情况下正确重建细胞类型特异性区域，同时保留其预期的细胞类型特异性。即使当与已知标记基因重叠的区域中的甲基化值在特定细胞类型中完全掩蔽时，scMethCraft也成功重建了与已知细胞类型身份一致的甲基化模式，保持细胞类型和潜在细胞异质性之间的相对差异。同时，通过比较插补前后每种细胞类型的平均甲基化水平，我们观察到scMethCraft并没有过分强调任何特定细胞类型中的特定甲基化模式。即scMethCraft通过高质量的去噪和插补增强了scDNAm矩阵，从而提高了细胞群体特异性DNA甲基化模式的可检测性。

6、scMethCraft通过识别候选的差异甲基化区域揭示了细胞类型特异性的生物学意义

从scDNAm数据中识别DMR为表征表观遗传变异提供了一种有用的方法。DMR为个体、组织和细胞类型之间的表观遗传差异提供了关键见解，从而能够全面表征表观基因组景观。作者利用scMethCraft进行DMR分析，以突出显示表现出细胞类型特异性甲基化模式的候选区域这些分析旨在提供对细胞类型特异性甲基化模式的探索性见解。

作者评估了scMethCraft和EpiScanpy的低DMR鉴定性能。以ACC数据集和ODC为例，EpiScanpy鉴定了142个ODC特异性低DMR（图5a），而scMethCraft鉴定了771个这样的区域（图5 b）。为了评价通过不同方法鉴定的低DMR是否捕获细胞类型特异性基因调控模式，作者找到了转录位点与这些低水平的基因重叠的基因，使用UCSC Genome Browser提供的基因组注释的DMR。为了定性评估这些基因与ODC的相关性，作者根据CellMarker和GeneCards数据库中的广泛搜索将它们分为三组：（1）在Cellmareker被明确注释的ODC基因（2）GeneCards中未被注释为ODC基因，但收录为ODC相关基因，其在GeneCards数据库中未被注释为ODC标记，但已被报道与神经细胞、脑发育或脑相关疾病密切相关;和（3）其他基因。作者生成了一个单词云，在这些基因中，8个基因被确认为ODC标记基因，19个基因被归类为ODC相关基因，根据查阅的数据库，只有8个基因缺乏与ODC相关的有力证据。尽管在所查阅的两个数据库中CHD7基因未被注释为标记基因或与ODC相关，但现有的研究已经证实CHD7可能是人类中枢神经系统髓鞘形成所需的功能，并且对ODC的成熟至关重要。此外，尽管其具体功能仍不清楚，人类蛋白质图谱数据库显示，CUEDC 1在ODC中表现出高表达。这些潜在相关基因的鉴定表明，scMethCraft可以捕获具有生物学意义的甲基化模式，并可能有助于探索基因从表观遗传学的角度来研究调控机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwl9v4ianTWsGuZszNwStGq5ZVr9ibgGPSLdXEjcMFQtqUIvoic4j9hFoQsVqwP8qXxXwb9UrPkpo0MkmnUicq177YIDic0U9jEjFBMk/640?wx_fmt=png&from=appmsg)

图5

7、scMethCraft的设计原则对单细胞组学数据建模的启示

scMethCraft设计原则从序列和细胞两个角度对scDNAm数据进行建模，有效地从甲基化矩阵表征细胞间关系。作为混合神经网络模型，scMethCraft集成了多个组件。作者研究了以下四个关键模块的scDNAm数据建模的有效性：特征提取子网络（即独热模块），k -mer特征提取子网络（即k -mer模块），位置特征提取子网络（即位置模块），相似度加权模块（即相似度模块），通过依次去除这些成分，构建了模型的四个消融变体。 scMethCraft采用两个优化器分别最小化序列特征提取模块和相似性加权模块的损失函数。首先，系统评估了不同组件对模型收敛性的影响；每个模型训练了100个epoch，记录了每个epoch的总损失。我们作者首先评估了序列特征提取模块的总损失。scMethCraft w/o one -hot在100个epoch后保持了明显更高的总损失，这表明one -hot编码捕获了最具信息量的序列特征该观察结果与来自scBasset一致，scBasset证明了独热编码基因组序列对于学习调控特征的有效性。

然而，scMethCraft对独热模块进行了重新设计，以适应区域水平的分箱、缺失值、连续的甲基化水平信号，这些是scDNAm数据所特有的，并且与scBasset基于scATAC-seq开发的有根本性差异。作者还评估了与相似性模块相关的总损失。每个单独的模块为表征细胞间相似性提供了不同的数据基础，完整的scMethCraft模型在整个训练过程中实现了最低的损失（图6 b)。

其次，我们还评估了scMethCraft及其四个消融变体的聚类性能，这间接反映了模型捕获细胞异质性信号的能力。三个基准数据集上每种方法的细胞聚类性能如图6c所示。没有独热模块的变体获得了最低的总得分，没有相似性模块的变体获得了第二低的得分，平均得分为0.76.缺少k聚体和位置模块的变体分别排名第三和第四（图6d）。

作者验证了相似性加权模块是否有效地捕获了细胞间的相似性信息，如细胞间相似性矩阵所示（图6e），与其他区域相比，沿着主对角线的区域表现出明显更高的值，这表明相同类型的细胞在矩阵内倾向于具有更高的相似性值。为了获得更精细的细胞亚型信息，作者将细胞按照亚型进行分类。图6f表明，即使对于具有细微差异的类型，scMethCraft的相似性加权模块仍然能够捕获这些细胞类型之间的生物异质性和相似性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkR9dYIdHJUcoiauCRAfKlaLA1YdTIgfYpMfOdAicstKImhKdNkh36dJ0TfiaJGqYqagdmRwubaib7LDujNv06HnPyX5gSKib2PNXnA/640?wx_fmt=png&from=appmsg)

图6

**四、最后聊聊**

相较于scRNA-seq分析生态的成熟，单细胞DNA尤其是单细胞甲基化数据的分析仍有较大的空白有待填补。scMethCraft在降维、可视化、细胞聚类、批量集成、细胞类型注释、数据增强、和DMR的识别方面展现出了此前基于scRNA与scATAC迁移开发的包具有较大的性能提升。不知道会不会成为单细胞甲基化数据分析的版本答案。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=7)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=8)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=9) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpw5vseibw4AJeLibc53LNsLYc2iaBU5PHFRGicesPwlJAYZjqVMGdYRGTxHe9oMUGVo6aIpmwQiabcvpzQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=11) 您点的每个赞和在看，我都认真当成了喜欢
