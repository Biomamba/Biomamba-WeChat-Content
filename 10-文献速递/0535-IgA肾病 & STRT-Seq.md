---
title: "IgA肾病 & STRT-Seq"
date: 2023-04-13
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498665&idx=2&sn=c32affcb095e485f30ee80838c6876ab&chksm=9b3c82f9ac4b0bef42405982960035b9d48a92453da8639d9dd3ac59779be6e7ea7b294c7275#rd
albums: ["文献速递"]
---

# IgA肾病 & STRT-Seq

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498665&idx=2&sn=c32affcb095e485f30ee80838c6876ab&chksm=9b3c82f9ac4b0bef42405982960035b9d48a92453da8639d9dd3ac59779be6e7ea7b294c7275#rd
> 合集：文献速递

****Biomamba荐语****

不必多说这篇文章是北京大学汤富酬（单细胞鼻祖）教授课题组的作品，学习价值应当较高。

**doi:**

10.1016/j.celrep.2020.108525

**链接：**

https://www.sciencedirect.com/science/article/pii/S221112472031514X?via%3Dihub

**Summary**

●**1 lgAN**

IgA nephropathy (IgAN)是肾衰的原因之一，其发生机制尚未完全解析清楚（套话）

●**2 主要发现**

**1、** Jchain作为免疫球蛋白的连接成分，在IgAN患者的系膜细胞处高表达，并引起IgAN在这一部位的沉积，引起后续的并发症。

**2、** 作者通过细胞通讯发现IgAN的整个过程可能是由系膜细胞为中心引发。

**3、** 差异分析解释肾脏浸润的Mac与CD8 T Cell起到了促增生、促炎的作用。

**4、** 经拟时序分析发现了收集管夹层细胞在IgAN中发生了一种转变，使其具有部分CD-PC的特性，这种变化参与了纤维化。（这其实并不是新发现，早前在慢性肾病中就已经发现了这种现象）

**Introduction**

●**1 lgAN** IgAN是一个公认的自身免疫性疾病，主要的并发症为肾小球肾炎，大约30~40%的病人最终会发展成终末期肾病。其最主要的诱因是IgAN在肾小球系膜部位的沉积：

![](../../images/5012c551e58ff6bb.webp)

但奇怪的是，系膜细胞并不能表达任何IgA的受体，因此，IgAN真正的发病原因仍不得而知，这是这一领域亟待解决的问题。

●**2****测序技术**

目前来说，主流的单细胞测序平台有两种，一种是基于液滴捕获（droplet based），这类测序捕获细胞数多但测序深度低；另一种是以SMAT-Seq为代表的技术，一般是经过流式或磁珠分选后进行建库，能对特定的细胞种类进行深度测序，因而捕获细胞数量少，但测序深度极高。

![](../../images/41ba2265a7dc54ee.webp)

**Methods
**

●**1 样本信息**

通过肾组织活检收取了13个病人的肾脏穿刺样本。

在来自患者肾脏摘除的样本中选取宏观观测正常的组织用于对照。

抽取了六个患者与六个健康人的外周血。

这些受试对象的主要临床信息如下：

![](../../images/473d75cd3a433675.webp)

●**2 操作流程** 下面这张图形摘要很好地展示了这篇文章的主要流程，具体的取材、制样过程不多赘述，感兴趣的同学可以去看看原文。大家知晓作者通过磁力分选，利用CD14、EPCAM等标志物分离得到单核/巨噬细胞、并分离肾小球组织用于STRT-Seq即可。

![](../../images/771c99624cda938c.webp)

●**3 分析流程** 首选STRT-Seq与我们之前所介绍的10X Genomics存在一些差异的，具体表现为前者每个细胞的测序深度更高、获得的基因(1000~12000)与分子数量（4000~600000）更多。与一般分析流程不同的是，作者将两组的细胞分别进行分群注释后利用scran包进行去批次整合（主流做法是先整合去批次，再进行分群注释）。在第一轮注释结束后，仍剩下两类细胞未能得到有效注释，因此作者利用了此前的一个snRNA-Seq的数据帮助注释（具体原理和过程可以参考这个：[手把手教你做单细胞测序数据分析（五）、细胞类型注释——从入门到入土](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484198&idx=1&sn=35d70e1f86d212ed3d253d933e98f711&chksm=9b3f7a76ac48f3604ff794f9d0528f4c9152baf066485335c02bc7dc13c51dee0b36429dd886&scene=21#wechat_redirect>)）。
在细胞通讯的分析之中，作者先在linux中利用cellphonedb进行了细胞互作的计算，后接R语言的igraph进行可视化（有些托大，其实可以通过cellchat、italk等R包一站式搞定，Biomamba后续的课程会出）。富集分析用的是DAVID，一个在线工具，不是很推荐，更新速度要比clusterprofiler慢很多（[手把手教你做单细胞测序数据分析（七）—— 基因集富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484738&idx=1&sn=96a7e1d3c7fd249f3a7e4d77e7ea0613&chksm=9b3f7c12ac48f5045fbc2b1cf0ff7d9f0cf5147e170802428a5a17475ad7e8c45faa00e983c4&scene=21#wechat_redirect>)）。

**Results
**

●**1 分群**

经基本的reads、count质控后，测得的八千多个细胞最终只剩下了3620个

![](../../images/bccb58ea2f797367.webp)

两组分开分群的方式确实有一些怪异，并且有些marker表达的特异性并不高，此前我在其他文章的阅读过程中发现过不错的marker展示（小鼠）：

![](../../images/87606095ac0391d1.webp)

![](../../images/66015ee1c769c658.webp)

●**2 J chain** 首先作者对两组间的系膜细胞进行了差异分析，从下面的火山图中我们可以较为明显的看到，JCHAIN在IgAN组中高表达，并且这一结果是可以通过免疫荧光被重复出来的。

![](../../images/216830cc6cb68a9c.webp)

![](../../images/2a07b2e5eaa94b81.webp)

我们来了解一下J chain，有免疫背景的同学可能比较熟悉一些，IgA的完整结构如下图所示，一个IgA分子由两个Y型免疫球蛋白组成，而这两个Y连接的部分，正是这个J chain。换句话说，正是系膜细胞高表达JCHAIN，才给此处IgA的沉积带来了可能性。

![](../../images/54ac15ee767488a0.webp)

●**3 富集分析** 差异基因的富集分析在两组间也有明显不同：在normal中被富集的通路主要与肾脏发育、分化相关，而在IgAN中被富集的通路主要体现在免疫应答和纤维化：

![](../../images/2f05fe982220c6d7.webp)

●**4 细胞通讯** 在笔者的概念里，任何一个疾病的发生均是多因素共同作用的结果，基本发生过程中必然存在着细胞与细胞之间的互作。这里对两组分别进行了细胞通讯的预测，并发现由normal（下图左）到IgAN（下图中）的过程中，系膜细胞与其余细胞的互作均上升，而CD-IC与其他细胞的互作均下降（下图右）。
![](../../images/ce201e45a75053c4.webp)●**5 免疫** 作为一种自身免疫类的疾病，IgAN的免疫微环境是最值得关注的，这里作者通过GSEA分析发现巨噬细胞的NOTCH通路、及与糖、氨基酸、脂类代谢的通路在IgAN中被显著富集；并且无论是肾脏浸润的巨噬细胞还是外周血中的巨噬细胞（终于提到外周血了）均在IgAN组表现出了激活的现象，因此作者认为巨噬细胞内的代谢通路改变重新编辑了IgAN的免疫微环境（我个人认为这一点有些牵强。。。）。![](../../images/a6febd0210b48386.webp)![](../../images/a088e7459df44383.webp)●**6 分群CD-IC的转变** 作为一种自身免疫类的疾病，IgAN的免疫微环境是最值得关注的，此前作者已经发现了CD-IC在IgAN组中与其他细胞的互作全线下降，引起了作者的关注。通过CD-IC、CD-PC这两种细胞marker的展示，作者发现CD-IC中存在着一种特殊的类型——可以高表达CD-IC与CD-PC两种细胞的marker。这在之前的CKD研究中也已经被证实过了。![](../../images/7e797dc5f6f8ada6.webp)

经拟时序分析后，作者发现这些CD-IC能够被分为3类IC1、IC2与纯正的CD-IC：![](../../images/3ff77057e0f08fa3.webp)

其中IC1与IC2便是上述提到能够表达CD-PC特征Gene的类群：![](../../images/7f87370bf45d175a.webp)

这两类细胞能够高表达WNT、FGF信号通路的基因，这是一些与先维护和EMT相关的基因。
![](../../images/cf5c8623eeb39d7f.webp)

**Discussion
**

作者的讨论我就不重复了，这里主要表达一下我对这篇文章的看法：

**B站同步播出**

https://www.bilibili.com/video/BV1ja411t7JL/

![](../../images/56869e2cc75aa830.png)

如何联系我们

![](../../images/7c0febec2249cfa6.gif)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器的**微信号** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](../../images/fdb4c49c78e6216c.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
