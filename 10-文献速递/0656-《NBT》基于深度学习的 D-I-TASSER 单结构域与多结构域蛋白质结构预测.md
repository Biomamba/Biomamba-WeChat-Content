---
title: "《NBT》基于深度学习的 D-I-TASSER 单结构域与多结构域蛋白质结构预测"
date: 2026-05-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538221&idx=1&sn=41d35930366504bc913a05ad9c3dac06&chksm=9b3c2f7dac4ba66bcd32af67329d3e8ee773c077c129a8678f05f22f466b681abd51928b2b1f#rd
albums: ["文献速递"]
---

# 《NBT》基于深度学习的 D-I-TASSER 单结构域与多结构域蛋白质结构预测

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538221&idx=1&sn=41d35930366504bc913a05ad9c3dac06&chksm=9b3c2f7dac4ba66bcd32af67329d3e8ee773c077c129a8678f05f22f466b681abd51928b2b1f#rd
> 合集：文献速递

* * *

**一、写在前面**

![](../../images/c851a7230e69b698.webp)

**文章《Deep-learning-based single-domain and multidomain protein structure prediction with D-I-TASSER》 （IF=41.7）**发布于2025年杂志《**nature biotechnology 》。**

**[深度学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507794&idx=1&sn=c70dd03a962adb3f3b92ffed47e978bb&scene=21#wechat_redirect>) 技术**在**[蛋白质结构预测](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>) 领域**取得的巨大成功，让传统基于力场的折叠模拟的必要性和实用性受到了挑战。这篇文章中作者提出了一种混合方法——**基于深度学习的迭代组装优化（ D-I-TASSER）**，**它通过将多源深度学习势能与迭代片段组装模拟相结合，构建原子级别的蛋白质结构模型。**

D-I-TASSER 引入了一种结构域分割与组装协议，用于大分子多结构域蛋白质结构的自动化建模。**基准测试以及蛋白质结构预测关键评估（ CASP15）实验**表明，无论是在单结构域还是多结构域蛋白质上，D-I-TASSER 的表现都优于 [AlphaFold2](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>) 和 [AlphaFold3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)。

**大规模折叠实验** 进一步显示，D-I-TASSER 能够折叠人类蛋白质组中 81% 的蛋白质结构域和 73% 的全链序列，其结果与 AlphaFold2 最近发布的模型具有高度的互补性。这都说明了D-I-TASSER**可以****将深度学习与经典基于物理的折叠模拟相结，可用于实现高精度的蛋白质结构与功能预测，并适用于全基因组范围的应用** 。

我们之前也分享受关于蛋白质结构与功能预测的相关教程：[正刊都在用的AI驱动蛋白质从头设计流程：RFdiffusion+ProteinMPNN+AlphaFold3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)[Ai驱动结合蛋白设计：Bindcraft全流程教学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537769&idx=1&sn=5dbfe76b35fd2f7593e55bff48c6fa73&scene=21#wechat_redirect>)
如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21#wechat_redirect>)**指导** 、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)、自测数据**个性化分析** 辅导、[实验科研服务](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=1&sn=578993fdfa060d38c80e2df6fc200c39&scene=21#wechat_redirect>)和[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[**Biomamba_zhushou**]。

**二、主要内容**

1\. **D-I-TASSER 专为混合深度学习与基于片段组装的蛋白质结构建模而设计，重点关注非同源及多结构域蛋白质**

D-I-TASSER 首先通过**迭代搜索基因组和宏基因组序列数据库** 来构建深度多序列比对（MSAs），并通过快速的深度学习引导预测过程选择最佳 MSA（Fig.1a）。随后，该流程利用DeepPotential、AttentionPotential和[AlphaFold2](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)创建空间结构约束，它们分别由深度残差[卷积](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532458&idx=1&sn=f8ec547187374fe77c38fc1125709b3b&scene=21#wechat_redirect>)网络、自注意力转换和端到端神经网络驱动。

接着，在全局优化的[深度学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507794&idx=1&sn=c70dd03a962adb3f3b92ffed47e978bb&scene=21#wechat_redirect>)和基于知识的力场指导下，通过**Replica Exchange Monte Carlo** （REMC）模拟，利用 LOMETS3 从多个 threading 比对中组装模板片段，从而构建全长模型。为了应对多结构域结构建模的复杂性，D-I-TASSER 整合了一个新的结构域划分与组装模块。在该模块中，结构域边界分割、结构域级别的 MSAs、threading 比对和空间约束均以迭代模式创建，而多结构域结构模型则是在混合结构域级别和结构域间空间约束的指导下，通过全链 I-TASSER 组装模拟生成的（Fig.1b）。

![](../../images/5318bc6985a41cbe.webp)![](../../images/db64dbbb3cff11b0.webp)

**Fig.1**

2\. D-I-TASSER **在单结构域蛋白质上的基准测试**

**单结构域蛋白质的结构建模是计算蛋白质结构预测的基础。** 为了检验流程的性能，作者首先在一组包含 500 个非冗余“高难度”结构域的数据集上测试了 D-I-TASSER。这些结构域收集自蛋白质结构分类（SCOPe）、蛋白质数据库（PDB）以及 CASP 8–14 实验。在排除与查询序列序列一致性 >30% 的同源结构后，LOMETS3 无法从 PDB 中检测到显著的模板

首先作者通过**三种方法的直接对比** 展示了 I-TASSER 算法的优越性（Fig.2a-b），之后，作者将 D-I-TASSER 与前沿的 AlphaFold2 方法（v.2.3）进行了进一步比较，结果显示 D-I-TASSER 模型的平均 TM 得分（0.870）比 AlphaFold2高出 5.0%（Fig.2c）。且作者发现，两者的差异主要来源于**高难度结构域** 。作者的基准比较主要针对 AlphaFold2.3。尽管如此，他们在所有 500 个测试结构域上还运行了 AlphaFold 的各个版本（包括 AlphaFold2.0、AlphaFold2.1、AlphaFold2.2、AlphaFold2.3 和 AlphaFold3），观察到它们之间的差异极小（Fig.2d）。

在此基础上，作者举了一个例子来验证他的算法，经典版本的 I-TASSER 通过多重片段组装模拟显著优化了模板质量，但模型仍然具有错误的折叠（Fig.2e）。**但****在深度学习约束的指导下， D-I-TASSER 组装出了一个 TM 得分高达 0.986 的优异模型**（Fig.2f）。这种改进主要归因于**空间约束的高精度** ，其相对于天然结构的距离图预测的平均绝对误差非常低（Fig.2g）。之后作者还展示了从模板结构开始的 D-I-TASSER 模拟的**折叠轨迹** 。在 D-I-TASSER 新设计的深度学习势能的指导下，预测距离相对于诱饵模型的平均绝对误差迅速降低（Fig.2h）。除此之外，作者还严谨地用另外的一个例子进行了相同的验证（Fig.2i-m）。

**以上****数据表明，像 D-I-TASSER 这样基于物理的方法，通过 REMC 模拟对构象组装进行建模并探索更广阔的构象空间，在建模无序结构方面可能比像 AlphaFold2 这样纯粹基于深度学习的方法具有潜在优势。**

![](../../images/33178098882ae721.webp)

**Fig.2**

3\. D-I-TASSER 在多结构域蛋白质上的表现

**为了检验 D-I-TASSER 在多结构域结构预测方面的能力，**作者从 PDB 收集了一组包含 230 个非冗余蛋白质的数据集，这些蛋白质包含 2 到 7 个结构域，总共覆盖 557 个独立结构域。作者展示了D-I-TASSER 与 AlphaFold2 在全长链和结构域级别结构预测上的性能比较（Fig.3a-b）。列出了 D-I-TASSER 和 AlphaFold2 在包含不同数量结构域的蛋白质上的 TM 得分比较（Fig.3c）。AlphaFold2 创建了一个质量较差的全长链模型且TM 得分较低，仅为 0.425（Fig.3d），且结构域间和结构域内距离图预测都很差（Fig.3e）。相比之下，D-I-TASSER 检测到的全长链 MSA 的 neff 略高,特别是，**结构域分割过程** 使得 DeepMSA2 能够分别为结构域 1 和结构域 2 检测到 688 条和 15 条额外的同源序列，这有助于深度学习模型推导出更可靠的进化信息（Fig.3f-i）。

![](../../images/df9f34fb69c3d610.webp)

**Fig.3**

4\. **D-I-TASSER 在 CASP15 盲测中的表现**

D-I-TASSER参加了 2022 年举办的**CASP15 蛋白质三级结构预测实验**。CASP15 实验发布了 77 个蛋白质目标，包括 55 个单结构域和 22 个多结构域目标。这些目标可以进一步分为 62 个基于模板的建模（TBM）结构域和 50 个自由建模（FM）结构域。首先作者列出了 D-I-TASSER（命名为“UB-TBM”）与另外 44 个参加了 CASP15“常规建模”和“结构域间建模”部分的服务器组的比较，这两个部分分别对应单结构域和多结构域结构（Fig.4a-b）。同时还进一步展示了 D-I-TASSER 与 AlphaFold2 和 Wallner 模型在 112 个结构域级别和 22 个多结构域目标上的直接比较，其中 Wallner 组是 CASP15 的另一个强预测组，主要基于使用 AlphaFold2 的大量采样（Fig.4c-d）。最后展示了 D-I-TASSER 与不同版本的 AlphaFold 程序在 50 个缺乏同源模板的 FM 结构域和 20 个多结构域目标上的比较。虽然 AlphaFold 各版本之间的性能差异很小，但 D-I-TASSER 取得了显著更高的 TM 得分（Fig.4e-f）。

![](../../images/8263732607b8dfc2.webp)![](../../images/2070fc744e84a482.webp)

**Fig.4**

5\. 人类蛋白质组的结构与功能建模

由于大多数人类蛋白质的实验结构未知，作 _者_ _设计了一个估计 TM 得分（eTM score）来定量评估 D-I-TASSER 模型的质量_，eTM 得分是根据五个因素的线性组合估算得出的：LOMETS 穿线比对的显著性、预测接触和距离图的满足率、D-I-TASSER 模拟的结构收敛性以及 AlphaFold2 排名第一的模型的预测 LDDT（pLDDT）得分。，eTM 得分与真实 TM 得分的皮尔逊相关系数（PCC）为 **0.79** （Fig.5a）**。作者****展示了 D-I-TASSER 对结构域级别和全长链人类蛋白质模型的 eTM 得分分布**（Fig.5b）**。** 之后，作者绘制了位于每条染色体上的全长链模型的 eTM 得分（外圈）、目标类型（容易或困难；中圈）和 neff 值（内圈）（Fig.5c）。作者展示了 AlphaFold2 的 pLDDT 与 D-I-TASSER 的 eTM 得分在两个程序都预测的 19,488 种蛋白质上的直接比较（Fig.5d-e）。

![](../../images/ff276f1452daa88d.webp)

**Fig.5**

6\. 人类蛋白质组的功能注释

**遵循 “序列到结构再到功能”的范式**，作者进一步应用成熟的 COFACTOR 协议，基于 D-I-TASSER 预测的模型对人类基因组的生物学功能进行注释。虽然蛋白质功能通常是多方面的，但作者主要关注三个主要方面：[配体](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)结合位点（LBS）、酶学委员会分类（EC）和基因本体（GO），其中 GO 进一步细分为分子功能（MF）、生物过程（BP）和细胞组分（CC）三个子方面。首先展示了基于染色体的 D-I-TASSER/COFACTOR 功能模型列表，其中为每条染色体选择了前三个功能（Fig.6a）。之后还展示了一个乙酰辅酶 A（CoA）乙酰转移酶（UniProt ID: Q9BWD1）自动 LBS 预测的说明性例子，其 D-I-TASSER 模型与实验解析结构的 TM 得分高达 **0.99** 。该目标被预测与 CoA 分子结合，预测的 CoA 姿态与从实验结构 1wl4 计算的天然姿态之间的均方根偏差（RMSD）为 **0.74 Å** ，表明结合位置预测非常准确。在实验结构中与 CoA 分子结合距离小于 4 Å 的 23 个残基中，COFACTOR 正确预测了 **22** 个配体结合残基（Fig.6b-c）。

![](../../images/95b12bdda1c3fb7a.webp)

**Fig.6**

**三、总结与展望**

**3\. 总结讨论**

**这篇文章中作者开发了****D-I-TASSER****，** 它是一个混合蛋白质结构预测流程，它创新性地将深度学习的空间约束与基于物理的迭代组装模拟相结合，并引入了专门的结构域分割与重组模块。这一设计使其在预测高难度的非同源蛋白和复杂的多结构域蛋白时展现出显著优势。在CASP15盲测及多个基准测试中，D-I-TASSER的预测精度均超越了AlphaFold2，尤其是在多结构域蛋白的建模上，其性能提升幅度巨大。

作为一项大规模应用，D-I-TASSER成功预测了约95%的人类蛋白质组结构，其结果与AlphaFold2数据库形成了高度互补，能够准确预测数千个AlphaFold2难以可靠建模的蛋白质。尽管在处理缺乏同源序列的孤儿蛋白和蛋白质复合物方面仍面临挑战，但D-I-TASSER的成功证明了将深度学习与物理模拟深度融合的策略，为解决结构生物学中的剩余难题开辟了富有前景的新路径**。**

![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
