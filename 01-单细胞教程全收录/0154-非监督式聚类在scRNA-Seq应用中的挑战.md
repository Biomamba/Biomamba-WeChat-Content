---
title: "非监督式聚类在scRNA-Seq应用中的挑战"
date: 2023-11-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505257&idx=1&sn=a524a42b966007defbb2529d300d4c28&chksm=9b3cac39ac4b252f9f88181b932fdc279507c2affc765b53dbccf73084f86f0de25ab1af39bc#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# 非监督式聚类在scRNA-Seq应用中的挑战

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505257&idx=1&sn=a524a42b966007defbb2529d300d4c28&chksm=9b3cac39ac4b252f9f88181b932fdc279507c2affc765b53dbccf73084f86f0de25ab1af39bc#rd
> 合集：单细胞教程全收录 / 文献速递

**写在前面**

本次介绍的是发表在《Nature Review Genetics》上题为"Challenges in unsupervised clustering of single- cell RNA- seq data"的文章。在**单细胞测序诞生之前** ，细胞身份的识别主要靠它们的大小、形状、位置、表面蛋白等。而单细胞测序多组学技术的出现改变了这一现状，通过监督式或非监督式的**聚类分群** ，可以依据所获细胞数据的特征将其划分为不同的细胞类型。为了能够获得数据导向、无偏的细胞转录组特征用于细胞类型鉴别，非监督式聚类在scRNA-Seq中被广泛应用。非监督式聚类是继质量控制、normalization、基因过滤、降维后的步骤，可以说是scRNA-Seq数据分析**向生物学意义迈进的第一步**(Fig. 1)。考虑到后续的一切进阶分析(细胞通讯、拟时序、RNA动力学分析、转录因子预测。。。)都是以细胞注释的结果为**基础** ，非监督式聚类无疑是scRNA-Seq数据分析的**重中之重** 。考虑到细胞生物学意义与聚类算法实现的复杂性，本文重点探讨了非监督室聚类在scRNA-Seq中应用的**现状(2019.05)与挑战** 。

![](../../images/15faad417ef0c0b7.webp)

**图1**

**主要内容**

目前也有多种cluster算法，最主流的方法为**k-means**(Fig. 3b)，这种方法的策略为先识别k cluster形状中心，再将每个细胞分配给"距离最近"的形状中心。例如Lloyd算法就是其中的一种，由于其随细胞/点增加时计算量呈现线性关系，也被广泛用于大数据集的计算中。值得注意的是，k-means倾向于将细胞划分为大小类似的细胞类群，这意味着一些**低丰度** 的细胞类群很有可能被较大的细胞类群所**覆盖** ，RaceID与SIMLR在调用k-means时考虑到了这一缺陷。另一个常用的分群算法为hierarchical clustering(层次聚类，Fig. 3c)，这类算法包含两种策略：一种不断将细胞个体整合为更大的类群；另一种则是不断拆分大的细胞类群。层次聚类的缺点是，随着数据量的上升，对于时间和内存的要求往往呈**指数式增长** ，例如CIDR、BackSPIN、pcaReduce等均采用层次聚类的策略。而层次聚类最大的优点便是有利于发现丰度较小的类群。第三类常见算法community-detection-based算法的逻辑是先基于数据构建k-nearest-neighbours graph，再依据后者寻找node(Fig.3 d-e)，例如**Seurat与Scanpy** 都在用的Louvain。

![](../../images/411bb7e38c3544fe.webp)

**图3**
**分离连续性细胞**
从计算的角度来对细胞进行分群正经是个难活，难就难在算法与生物学意义的匹配程度。区分**离散型** 的细胞显然较为简单，例如区分上皮细胞和免疫细胞，这两种细胞来源不同、表达矩阵迥异，自然也就大大降低了分群的难度。而一些较为**连续** 的细胞，例如受精卵发育为胚盘的过程中，由于细胞均处于连续分裂的状态，不同细胞个体之间的差异甚微。这时拟时序会是一个区分细胞状态的好办法。

![](../../images/bcee9457dfa17a46.webp)

Fig. 4

**技术挑战** 由于scRNA-Seq的特性，表达矩阵通常比普通的bulk RNA-Seq包含更多的**噪音与0值** 。对于通常占稀疏矩阵填充值半数以上的0值，通常由三种情况造成：**1** ，该转录本不表达，是真正的0值；**2** ，测序深度过低，表达的基因序列并没有被捕捉到；**3** ，在文库构建时，该基因的表达序列没有被成功扩增。这些均为后续的计算带来了复杂性，BEARscc可以通过对噪声模型的机器学习来消除0值的影响(这里Biomamba很疑惑，如何获得"完美"的0值噪声数据作为**训练集** 供算法学习呢)。另外，**批次效应** 同样会为分群计算带来难度，样本来源、测序lane通道、测序深度等因素均会导致批次效应的产生。不过批次效应一直都受到算法开发人员的重视，现在已经有很多种去批次的方法供大家选择([多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21#wechat_redirect>))。另外，由于细胞的形状大小、建库策略等因素，实际的单细胞测序数据中还会包含双液滴和空液滴，这同样会对聚类算法的执行带来挑战。

**生物学挑战** 除了技术挑战，生物学因素对分群带来的影响依旧不可忽视，其中典型案例便是**细胞周期** 带来的影响。处于转变中的细胞往往会影响分群效果，目前scLVM、cyclone等工具可以回归消除细胞周期效应并提供矫正后的转录数据。但在某些情况下，细胞周期具有对应的生物学意义，例如癌症组织中细胞周期往往处于活跃状态，因此不能对其细胞周期效应进行去除。换句话说，具体问题还是得**具体分析** 。另外，一些丰度较低的细胞类群难以在分群过程中被识别，固然可以通过提升建库时细胞的上样量以及样本数来解决，但显然不够经济。某些算法在识别**小类群细胞** 具有优势，例如上文提到过的RaceID与GiniClust。

**计算学挑战** 随着单细胞数据的规模日益增长，挑战与机遇并存，更高大的数据能够为各项研究提供强有力的数据支撑，但同样也对算法和硬件带来了更高的要求([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=2&sn=c2ba75edc0382855cfc914c3bb713e7e&chksm=9b3caa9bac4b238d0690d2aa5a236c18c8ad8f0d7a23421eb63b5236ff1201c9ec99e12efc8f&scene=21#wechat_redirect>))。对于分群降维的可视化也同样有助于对生物学的理解：一些线性转换的算法(例如PCA)，可以更精准的捕获细胞之间的相似性以及噪声；而非线性转换(例如UMAP与tSNE)则比较容易受到参数的影响，这也导致了**较低的可重复性**(所以经常有粉丝提问为什么自行跑出的降维图与我们演示课程中的不同)。许多分群方法均包含众多面向用户的参数可供选择，而这些参数通常也不能让分析人员达成共识，这也就造成分析结果掺入了人为的**主观因素**(不过大部分生信分析过程均包含这种因素)。此外，还有一个**先有鸡还是先有蛋** 的问题：对于各类算法的评估，需要依赖于质量较好的细胞注释数据(质量较好的细胞数据中细胞数却通常较少)，但注释完善的数据又依赖于较好的分群算法，因此不同算法之间的benchmark也值得斟酌。这些都是目前需要应对的挑战。
**生物学解释与注释**
即使你成功解决了上面我们提到过的挑战并拿到了分群后的数据，对于分群的生物学解释与注释仍是一个难题，因为你所获得的cluster当中仍有可能包含一种**或多种** 的细胞类型。而cluster的类型注释也包含较大的主观因素，且没有统一的标准与数据库。更多情况下，cluster的注释像是一种"**约定俗成** "。因此会出现来源于不同实验室的相同组织获得的注释信息一模一样的情况，互相参考、**过于同质化** 显然会阻碍学科发展。对于分群结果，通常需要结合参考文献、label transform([细胞类型注释，从入门到入土](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&chksm=9b3cb8d7ac4b31c19c843810c7fe4341515df8ba6fff86a0ebff9d830edfcd656a29d18011c9&scene=21#wechat_redirect>))、[SCENIC转录因子预测](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2933885075702972418&scene=173&from_msgid=2247500631&from_itemidx=1&count=3&nolastread=1#wechat_redirect>)、[基因富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21#wechat_redirect>)等操作来确定并矫正细胞类型。

**如何判定一个cluster为新细胞类型？** 这个目的往往是选择非监督式分群的原因，鉴定一个cluster为新细胞类型，就需要研究者证明这一个cluster与其余cluster或细胞类型具有不同的生物学特征，这些内容同样具有主观因素，并且难以标准化。例如，究竟在基因表达矩阵上有怎样的差异才能被定义为新细胞类型**？** 一个cluster包含多少细胞才能被定义为新细胞类型**？** 一个cluster是否需要经过试验验证才能被定义为新细胞类型**？** 这些问题都需要时间去回答，我想这也是scRNA-Seq领域文章层出不穷**临床转化** 却寥寥无几的原因。
最后
可以看出，这一领域的发展仍有很长一段路要走。面对组织、物种、算法的多样性，细胞分群的标准化仍亟待普及。当然，也随时有可能让现在变成"**未来已来** "。

参考：

Kiselev VY, Andrews TS, Hemberg M. Challenges in unsupervised clustering of single-cell RNA-seq data. Nat Rev Genet. 2019 May;20(5):273-282.

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息更新不及时，超过48h便不许回复读者消息，这里给大家留一下领取资料及免费服务器([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=2&sn=c2ba75edc0382855cfc914c3bb713e7e&chksm=9b3caa9bac4b238d0690d2aa5a236c18c8ad8f0d7a23421eb63b5236ff1201c9ec99e12efc8f&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
