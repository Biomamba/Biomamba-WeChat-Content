---
title: "Inferelator 3.0多快好省的基因网络推断工具"
date: 2025-07-30
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530020&idx=1&sn=0e8d4247b258a71f7dc6637ec5d16579&chksm=9b3c0f74ac4b8662b5c075470714dd062ffa46e1596ca90d344d71e6ed6518d9f6db3bc34777#rd
albums: ["文献速递"]
---

# Inferelator 3.0多快好省的基因网络推断工具

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530020&idx=1&sn=0e8d4247b258a71f7dc6637ec5d16579&chksm=9b3c0f74ac4b8662b5c075470714dd062ffa46e1596ca90d344d71e6ed6518d9f6db3bc34777#rd
> 合集：文献速递

**一、写在前面**

基因调控网络即转录因子与靶基因的调控关系，能够帮助人们重构并理解细胞生长及功能理解，此前已有一些优秀的调控网络推断工具通过测序技术与深度学习的发展，能够从基因组级别的数据中推断并重构基因网络调控过程(例如我们此前介绍的：[SCENIC单细胞转录因子预测|学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>))。随着测序技术的发展，现在已经超过上千种技术能够生成超过百万级别的单细胞测序，能够处理千万级别细胞的工具需要被提上日程啦。因此Claudia Skok Gibbs等人开发了Inferelator 3.0(Inferelator能够完成bulk RNA的GRN构建)，其能够显著整合来自不同细胞类型的的数据以学习并推断出调控网络。相比于其它工具，Inferelator 3.0能够处理更大的单细胞数据且通过"金标准"的 _Saccharomyces cerevisiae_ 学习并验证工具的性能。Inferelator 3.0也能够成功的从包含1.3 million的单细胞表达矩阵及染色质可及性数据中推断小鼠的E18脑组织不同神经元、胶质细胞的基因调控网络。本文于2022年发在经典期刊《Bioinformatics》上，原文与工具链接如下：https://pmc.ncbi.nlm.nih.gov/articles/PMC9048651 https://github.com/flatironinstitute/inferelator更多调控网络计算可参考：[一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)更多单细胞教程可参考：[生信基地122篇单细胞教程全索引](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528470&idx=1&sn=7f3ced59b2b97bed1ac9df560b11ddd6&scene=21#wechat_redirect>)如果自学单细胞有困难的话：[scRNA-seq，从小白到文献复现大神！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)

**二、背景知识**

基因调控控制着细胞生长、发育、条件性反射。转录调控的实质主要是转录因子(transcription factors, TFs)结合DNA的特定区域造成染色质重塑或直接影响RNA聚合酶的出现(Figure 1A)。在 _Saccharomyces cerevisiae_ 中大约3%的基因为TFs；在人类细胞中超过6%的基因被认为是TFs或其辅因子。TFs与靶基因之间的转录调控网络(Gene Regulatory Network, GRN)可以通过有向图来展示(Figure 1B)。GRN的推定对于解释疾病过程中的基因失调至关重要，更能够对工业中对生物体重编程以高效生成化合物与酶起到指导作用。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZjku158icaicdY8D51CM11VKKmEEgoRfqWcOgnGxdb5bIvIT7gssUMycA/640?wx_fmt=png&from=appmsg)

Figure 1

基因组规模的调控网络构建依赖于基因组级别的表达量(似乎是废话，但是测序通量提升前确实做不到)。面对基因组级别的数量，TFs与靶基因的庞大数量会干扰网络的构建，尤其是单细胞矩阵的稀疏特征会进一步干扰GRN的正确构建。设计一个专门的实验来捕获GRN的可识别性几乎是不可能的(一些类似于chromatin immunoprecipitation的技术也不能在基因组规模构建所有的GRN)。最佳的做法是以时间为变量收集大量的数据用于GRN推断，实际科研中很难获得这样的数据，所以更常见的做法是在已有的数据集中推断GRN。单细胞技术的介绍跳过，感兴趣的同学可以参考：[scRNA-Seq学习手册Seurat V5更新版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&chksm=9b3cf48fac4b7d99e65eba6d4c66c63e40b1d187fa1d9e6449d6cd07d5dec5127cff54886f93&scene=21#wechat_redirect>)、[scRNA-Seq学习手册Python版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&chksm=9b3caabdac4b23ab6e28425a4a5eb4d40ee3612e51f84f5d1e53ac91bef93f717e9e754398e3&scene=21#wechat_redirect>)最早发布的Inferelator已被验证能够在 _B.__subtilis_ 、人类Th17 cells 、小鼠淋巴细胞、 _S.__cerevisiae_ 、 _Oryza sativa_ 中完成GRN的构建。在Inferelator 3.0发布前，大多数的GRN推断工具只能预测五万个细胞的表达数据。Inferelator 3.0基于正则化回归及先验网络计算TF活性，并与利用实际的 _S.__cerevisiae_ 单细胞数据以及金标准数据为测试数据与[SCENIC](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)、CellOracle(能够整合scRNA与scATAC数据进行基于贝叶斯的GRN预测)对比，进行性能评估。在基于Python的 Inferelator 3.0中，可以调用Bayesian best-subset regression (BBSR)来大规模地(百万级细胞)完成GRN的构建。

**三、主要结果**

1、Inferelator 3.0
Inferelator 3.0在数据量少(<1w)或多(>1w)时采取不同的计算策略，应对小规模数据Inferelator 3.0直接引用个人电脑的python自带多线程策略进行计算，而大规模数据则利用Dask引擎(pySCENIC也是这种策略)被布置在高性能集群中进行计算 。
2、利用bulk RNA-Seq进行GRN推断作者利用Inferelator 3.0在 _B.__subtilis_ 、 _S.__cerevisiae_(这两个物种拥有大量的金标准数据)中进行了基于微阵列与bulk RNA-Seq数据的测试。Inferelator 3.0中内置了BBSR、StARS-LASSO模型(Figure 2A)，它们在上述数据集中的准确率与召回率(被预测正确的样本占总实际样本的比例，又称查全率)表现接近。而不利用先验网路信息的GRNBOOST2则明显表现较差(Figure 2B)，召回率和准确率都比较低。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZbZFdg9SeVQbWv8EibZWOeEkI0tAwnEic9RSPmsJqr8pp6EGsfevprQug/640?wx_fmt=png&from=appmsg)

Figure2

与基因表达矩阵一样，GRN的构建过程中也会出现明显的批次效应，其间网络推断的整合亦是一道难题。例如，两个不同数据集的PCA结果明显在降维图中占据着不同的空间(Figure S1A)。作者尝试用不同的方法去除批次效应，例如将两个数据集按照独立的学习任务处理，然后整合网络信息使得GRN信息统一(Figure 2C)。但最佳的做法是利用多任务学习方法—— Adaptive Multiple Sparse Regression (AMuSR) 在回归过程中整合网络信息。这一方法对基因表达的差异解释度高于BBSR与StARS-LASSO(Figure S1B)，且两个数据集共享的edges数也显著更高(Figure S1C)。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZmoLTmJ7qNDyAkYbeEeHllU8qYz0yKSMmCTI4txGCaROtoyDSMfp9uQ/640?wx_fmt=png&from=appmsg)

Figure S1

3、通过染色质数据与TF motifs构建先验网络
Inferelator 3.0通过基因表达量和先验的GRN生成推断网络，而先验GRN的一个重要来源就是数据库中的调控子、基因互作关系。即使一些数据库中拥有具有文献支撑的互作关系，但仍不能覆盖所有物种或细胞类型。在这种情况下，利用ATAC获得的染色质可及性和TFs结合DNA的偏好性可以识别理论上的互作关系。
为了生成这些先验网络，作者制作了inferelator的依赖包，该包能够通过TF motif的位置权重矩阵对TF与基因调控序列区域的结合能力进行打分，并构建先验稀疏矩阵 (Figure 3A)。与inferelator依赖包类似，CellOracle也能够提供类似功能，而二者在YEASTRACT文献记载的先验网络构建中，表现出了相似的Jaccard index(衡量有限样本集之间相似性和差异性的统计量。它的值越大，表示样本之间的相似度越高)(Figure 3B)。这一依赖先验信息的GRN构建在inferelator 3与CellOracle中均表现出良好的效果(Figure 3C)(area under the precision–recall,AUPR值越高效果越好)。需要注意的是motif文库不同的来源(Figure S2A)记录的不同位点(Figure S2B)会显著影响先验网络的输出(Figure S2C)。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZ6ibGasLtnPQSox8Vicdpa9dQMHOtX0AibX0zcNJA5oZMiclrpZjj0YoXLw/640?wx_fmt=png&from=appmsg)

Figure 3

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZ8V2wDPmB0DIUGsECKj0JLGG7CeRcoaMn9q7784XxCdKSgnXp2qibUYA/640?wx_fmt=png&from=appmsg)

Figure S2

4、利用单细胞表达数据进行网络推断单细胞欠采样(稀疏)、噪声大已经不是什么秘密，去噪也是单细胞软件设计的基操。作者将 _S.__cerevisiae_ 单细胞数据按照实验分组分为了十五个任务(Figure 4A)。作者利用基于YEASTRACT文献记载的先验网络构建调控网络，这个过程中每个任务使用部分基因进行训练，在通过未经训练的基因将各个任务运行结果整合到一起。最终，作者得到了BBSR、StARS-LASSO、AMuSR三种方法的结果(Figure S4B-D)。过程中作者发现按照测序深度对raw count进行standard Freeman–Tukey or log2 pseudocount transformation能够获得最佳的结果。随后，作者使用CellOracle与SCENIC与Inferelator 3.0中的AMuSR进行对比，AUPR值遥遥领先(Figure 4G)。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZQmf1ElLj9Y2IqxYnSG3anTq5QiaEspNbHVUicja3vib5n5etUUJz9BsjA/640?wx_fmt=png&from=appmsg)

Figure 4

5、大规模小鼠神经元单细胞网络推断
Inferelator 3.0能够把任务分布式的布置在多个计算节点中，因此能够快速处理超过10w个细胞的数据(Figure S5A，GENIE3出来挨打)。为了测试Inferelator 3应对大规模数据的处理能力作者使用基于10X Genomics的766402个单细胞数据以及7751个scATAC数据进行测试(Figure 5F)，数据集中占比较高的细胞类型与占比较低的细胞类型比例差距悬殊(Figure 5G)。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZFkVoog20eo0bk2ZcM4RhgA32Oxt48ApDJuPmPn0siahzx8LJ8oVhgWA/640?wx_fmt=png&from=appmsg)**Figure S5**

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZaSuJ1Lw93qbz2xicF0FJ1ZBvUxPZFvxf5ccpRZ5kUO3ZT7x0LDyNLOw/640?wx_fmt=png&from=appmsg)

Figure 5

利用AMuSR模型进行分布式计算后，结果共整合了包含20991个TF-靶基因调控egdes，从中选择最高置信度的预测，以最大限度地提高MCC(Figure 6B&C)。其中存在1090个网络节点存在于每一个任务的网络中(Figure 6C)，不同任务的相似细胞互相间也展示处了较高的Jaccard index(Figure 6D)。根据作者的先验知识，Egr1靶向103个基因(Figure 6E)，其中有20个基因能够被其他TFs调控(Figure 6F)；而Atf4能够靶向14个基因，这些都与先验知识相一致。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzdaeaMicibGTg23wvb3KlBrZA9LN8rUtIWiax498dUgyzFm2EmeJqU5vic5le5YicSPXDjeA0oh8djDQQ/640?wx_fmt=png&from=appmsg)

Figure 6

**四、最后聊聊**

不得不承认计算工具的开发要落后于湿实验测序平台一周期，好在各位大佬一直在给大家开发高效、好用的生信软件。在数据库冗余的今天，各个数据库整合分析产生的批次效应阻碍了数据的应用。而转录调控网络的出现能够很好的帮助大家解决批次效应(毕竟批次效应很难巧合的落在一堆互相能够调控的生物学"regulon"上)。作者开发的Inferelator 3.0与我们熟知的SCENIC相比有一个最大的好处：没有物种限制。此外Inferelator 3.0能够快速处理上百万个细胞的数据，即使相较于SCENIC中同为python平台算法的GRNBOOST2，计算速度也要明显快出很多(Figure S5A)。当然，Inferelator 3.0也有一些缺陷，不过这些似乎是整个行业的瓶颈：RNA半衰期会影响预测的准确性、TF与靶基因间的促进或抑制作用难以预测、TF-TF之间存在协同或竞争关系。但总体来说，Inferelator 3.0是一个值得尝试的好工具！

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528482&idx=1&sn=7cc0715eace4f592a62bdaf157b25c01&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
