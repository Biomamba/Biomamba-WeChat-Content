---
title: "自测蛋白质组+Bulk RNA-Seq & 挖掘scRNA-Seq=13.6分JASN"
date: 2023-10-31
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504408&idx=1&sn=da427a6687b06a82d9dd58ae9f9aa474&chksm=9b3cab48ac4b225e8272d0475ae9295c1ea96172419aa604526f1b8a898748cb3897508d95a0#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# 自测蛋白质组+Bulk RNA-Seq & 挖掘scRNA-Seq=13.6分JASN

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504408&idx=1&sn=da427a6687b06a82d9dd58ae9f9aa474&chksm=9b3cab48ac4b225e8272d0475ae9295c1ea96172419aa604526f1b8a898748cb3897508d95a0#rd
> 合集：单细胞教程全收录 / 文献速递

**写在前面**

今天介绍的是发表于《JOURNAL OF THE AMERICAN SOCIETY OF NEPHROLOGY》上题为"Unbiased Human Kidney Tissue Proteomics Identifies Matrix Metalloproteinase 7 as a Kidney Disease Biomarker"的一篇文章[1]。

糖尿病肾病是(diabetic kidney disease, DKD)是终末期肾病(end stage kidney disease, ESKD)的主要原因之一，此前大量的转录水平研究对人类肾脏进行了相关研究，但无偏的蛋白质水平图谱仍待进一步揭示。这里作者收集了23例DKD及10例健康对照临床样本，通过SomaScan平台[2]对肾脏的1305个蛋白质进行了定量并配对测定了Bulk RNA。此外，作者还收集了**11,030** 例血液样本用于验证，最终发现了Matrix Metalloproteinase 7(MM7)在与DKD进程的两个重要标志——eGFR、肾脏纤维化程度呈现出较高的关联性，可作为DKD及肾衰的生物标志之一。

![](../../images/727106c72c796239.webp)

**结果速递**

本文的研究结果行云流水、丝毫没有多余的内容，作者首先测定了反应肾脏功能的eGFR，并依据HE、PAS等染色切片邀请病理学家在不知道样本信息的情况下(相当于**单盲**)进行的DKD进程、纤维化的相关评分；发现eGFR与纤维化程度不仅在组间呈现出明显差异(已包含基线校准)，且存在显著的负相关关系(Figure 1)。而对通过SomaScan平台获得的蛋白质含量矩阵进行**层次聚类** ，也可将样本划分为主要包含健康对照与主要包含DKD的两类(Figure 1B)。在进一步的相关性分析中(线性回归模型，通过协变量进行矫正)，与**纤维化相关** 的蛋白质共有**152种** ，与**eGFR相关** 的蛋白质有**14种** ，它们的包含关系可见Figure 1C。综合考虑这些蛋白与eGFR及纤维化程度的相关性，MMP7的DKD风险系数在所有蛋白质种最高(Figure 1D)，且该蛋白与MMP7具有较高的相关性(Figure 1E)。

![](../../images/e3a694bfc00b7f0a.webp)

**Figure 1**

接下来，作者对蛋白质表达图谱进行了WGCNA分析([WGCNA教程合辑可点击跳转](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2891860532658733056&scene=173&from_msgid=2247499737&from_itemidx=1&count=3&nolastread=1#wechat_redirect>))并获得了8个蛋白质共表达模块(Figure 3A&B)。这些模块中包含MM7的**棕色模块** 与纤维化的聚类分值最近(Figure 3C)且关联程度最高(Figure 3E)。富集分析显示棕色模块富集于defense response、regulation of immune system process(Figure 3F)等通路。

![](../../images/473724192c6afa29.webp)

**Figure3**

接下来作者统计了配对样本中**蛋白质与RNA的相关性** 。不难发现，无论是全体样本还是代表性样本，蛋白质与对应RNA的R值均为0.46，这表明着基因的表达与翻译间仍存在着复杂的调控。在这一背景下，MMP7就显得有些突出：**R=0.64** 。不出所料，MMP7的RNA水平也与eGFR呈现出**负相关**(Figure 4D)的关系而与纤维化程度呈现**正相关** 的关系(Figure 4E)。而MMP7的RNA含量也在DKD组与健康对照间呈现出极显著的差异(Figure 4F)。

**![](../../images/efc6cbb1d431a0e3.webp)**

**Figure 4**

为了证明MMP7发生差异表达的细胞特异性(上文描述的蛋白质组与RNA-Seq均是Bulk水平)。作者挖掘了NIDDK与KPMP公布的DKD及Living Donor的肾脏scRNA-Seq数据(Figure 5A)，发现MMP7主要在PEC、ATL/TAL等细胞中表达(Figure 5B-C)。并且这一基因在PT、CNT、PC细胞的DKD组样本中呈现出明显的**上调趋势**(Figure 5D-G)

![](../../images/398011e25c806f28.webp)

**Figure 5**

不满足于以上结果，作者对另外的**186个人类肾脏** 样本开展了验证，MMP7的RNA水平依旧是与纤维化呈正比而蛋白质水平(Figure 6A)与eGFR(Figure 6B)呈反比(这里不是很懂为什么一个用RNA分析、一个用蛋白质分析)。另外，在354例糖尿病及11190例非糖尿病人均的血浆样本中，糖尿病患者(Figure 6D)的MMP7蛋白水平与对照组相比和eGFR间的负相关程度**更加强烈**(Figure 6C)。

![](../../images/e349c9848f743bcb.webp)

**最后聊聊**

其实本文的分析思路与分析方法真的非常**简单** ，本文的富集分析甚至是用**在线工具** DAVID[3]完成的，且scRNA-Seq的部分也由原作者提供了**注释后** 的工程文件。但简单不是缺点，**直截了当** 的阐明学术观点往往更能够取悦读者。并且作者的确提供了第一例DKD与健康人均对比的蛋白质组学图谱(原创性果然是第一生产力)。围绕着MMP7这一单个的基因，作者通过蛋白质组学、Bulk RNA-Seq、scRNA-Seq等**多组学** 、**多来源临床样本**(肾脏、血浆)分别验证其与DKD之间的风险关系，的确为DKD提供了置信度较高的生物标志物，为该领域做出了一定的贡献。

参考:

[1]:Hirohama D, Abedini A, Moon S, Surapaneni A, Dillon ST, Vassalotti A, Liu H, Doke T, Martinez V, Md Dom Z, Karihaloo A, Palmer MB, Coresh J, Grams ME, Niewczas MA, Susztak K. Unbiased Human Kidney Tissue Proteomics Identifies Matrix Metalloproteinase 7 as a Kidney Disease Biomarker. J Am Soc Nephrol. 2023 Apr 5.

[2]:Kobayashi H, Looker HC, Satake E, et al. Results of untargeted analysis using the SOMAscan proteomics platform indicates novel associations of circulating proteins with risk of progression to kidney failure in diabetes. Kidney Int. 2022;102(2):370–381.

[3]:https://david.ncifcrf.gov/

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503225&idx=1&sn=d07afe8ff1787f6226c2d64cc72508f9&chksm=9b3cb429ac4b3d3f06513c5b7e3a5e03b6dc347c3e4edff0544225b57e7f98e8425dff5242f3&scene=21#wechat_redirect>))的**微信号[Biomamba_kefu]** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅，**备注来意会优先通过**)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
