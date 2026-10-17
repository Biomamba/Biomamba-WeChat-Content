---
title: "酸了，六个样本的scRNA-Seq+差异分析=9分文章"
date: 2022-12-30
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496237&idx=1&sn=646cd85b62d08c1739a532242c8991ba&chksm=9b3c8b7dac4b026be9e65b64df8e830d1c2c882272165e64eec6eb258e4ed5342cf30f42dda5#rd
albums: ["单细胞教程全收录"]
---

# 酸了，六个样本的scRNA-Seq+差异分析=9分文章

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496237&idx=1&sn=646cd85b62d08c1739a532242c8991ba&chksm=9b3c8b7dac4b026be9e65b64df8e830d1c2c882272165e64eec6eb258e4ed5342cf30f42dda5#rd
> 合集：单细胞教程全收录

**写在前面**

今天看到一篇《**Diabetes** 》上题为"athogenesis Study Based on High-Throughput SingleCell Sequencing Analysis Reveals Novel Transcriptional Landscape and Heterogeneity of **Retinal Cells** in Type 2 Diabetic Mice"。这篇文章[1]是去年五月发表的，那么它对应的影响因子是2020年度的9.46，考虑到发表在《Diabetes》上，其实际的生物学价值可能要比这个影响因子高一些。抱着学习的心态点了进来，很遗憾的告诉大家，如果你想从学习单细胞的角度来看这篇文章，我觉得你可能会收获甚微。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzHfU2wJcHBlgJYxCicKhgrIZ3icshWUPC52WcysAOUF3K3rEWclKonVSunORaGcCbJzYz3iaDxaThiaQ/640?wx_fmt=png)

**具体内容**

Diabetic retinopathy (DR)为一种糖尿病的并发症这里不是我们讨论的重点，不作介绍。这个文章的含单细胞量确实很高，正文中共计6张Figure，其中5张都是单细胞相关的图片，给我的感觉就是其实这五张图片都可以放在Supplement里：

第一张图就是老几样——TSNE、marker展示(教程参考：[手把手教你做单细胞测序数据分析（三）——单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487976&idx=1&sn=8edd929256e609e4210a40df63fc1427&chksm=9b3f68b8ac48e1aefd3ff38dd5744c485cde5d7f28d79745b66863928d4614fafb2928b3f617&scene=21#wechat_redirect>))、细胞比例统计(教程参考: [沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&scene=21#wechat_redirect>))，都是些比较简单的图片，作者花了一段内容向大家介绍其中的细胞数量组成与具体比例。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzVicYucKZ2iaxn5IibNczIGnic0YUPe69hId8RNA3NszIwEHOzdkn6Sf3gg6cialYnva538BdNTJbfIyw/640?wx_fmt=png)

第二张图作者展示了一些之前经GWAS证明与DR相关的基因集，大致意思是告诉大家这些基因的表达在DR中是具有异质性的，而这便是这篇单细胞文章存在的意义。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzVicYucKZ2iaxn5IibNczIGnicThP8FFS6wH92Ced9bGOUzBawLicEib4RqpkrnapDn8cibFiaGItBC4bmYA/640?wx_fmt=png)
紧接着就来到了图三，作者使用cellphoneDB(**我个人更喜欢cellchat:**[**单细胞测序数据进阶分析—《细胞通讯》2.2CellChat多组别分析**](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485706&idx=1&sn=2d39360b41733b0be6f88d2922388507&chksm=9b3f705aac48f94cc478210f7f11d37294156517c489dedb333d8647ca287134a29944f39a3d&scene=21#wechat_redirect>))对两组数据进行了细胞通讯的计算，但显然作者对算到的通路都不太感兴趣，不知为何掏了Kdr与Vegfa这对配受体出来发起猛攻，并且对它们进行了相关性分析，发现这对配受体在RGC、Rods、Cones中的相关性分别为-0.26、-0.77、-0.20而另一对配受体Ephb1、Efnb3在RGCs中的相关性高达0.99。值得一提的是，如果这里做相关性分析，显然我会以每个细胞为单位进行相关性分析，而不是下图这样以样本为单位(**参考教程:**[**来个线性回归分析**](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484907&idx=1&sn=331048eabfe07dfab0db4916c8ba382e&chksm=9b3f7cbbac48f5adb4d6f23642533d904bbde6ad4a213ebd8fb20d2418cd9b28c4de6c89fc57&scene=21#wechat_redirect>))。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzVicYucKZ2iaxn5IibNczIGnicrShBj9uvNgpjP3Xqz8ibgdziafvEOiaa125Q07CLk2TCkMfiaWn4ynp2Lg/640?wx_fmt=png)
接下来的图四是差异分析了，对以下五种主要的细胞类型进行了组间差异分析(**参考教程:**[**手把手教你做单细胞测序数据分析 （六） 组间差异分析及可视化**](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488675&idx=1&sn=c1f4ac08b87baf625c7aafa8f073ed79&chksm=9b3f6df3ac48e4e53ef11776bda8a5f75f1d465e4e2d6cccd5e4e1aff5f26eaa34cdea3aabb8&scene=21#wechat_redirect>)**)** ，并将GO富集(**参考教程:**[**手把手教你做单细胞测序数据分析（七）—— 基因集富集分析**](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488717&idx=1&sn=6ba02599dda33eb6cff751c1d92055d9&chksm=9b3f6d9dac48e48ba334f031ce7874b4383a45be271acc9f0e6a714934ab7c7d945a513efdec&scene=21#wechat_redirect>))的结果放在了补充材料之中。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzVicYucKZ2iaxn5IibNczIGnicnBGhloOKdibtpib8Wot36DfFftV1WibKQ2hoAxC4oTQCBpuu0nv72x4CA/640?wx_fmt=png)
图五是图四的延续，用小提琴图具体的展示了一些差异基因的表达情况，真的**很难相信** 这是一张近十分文章正文中的完整Figure，而本文的单细胞内容也到此结束。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzVicYucKZ2iaxn5IibNczIGnicJSkHzAxibheLtZJx9aWnXCCqva1TMzU3e2Owx5uJe1T0LibHVVsYowjA/640?wx_fmt=png)
图六中作者使用腺病毒载体递送了上面的一个差异基因 RLBP1，并通过免疫荧光、WB、ELISA、视网膜扫描图证明了这一基因的表达量差异会引起一些炎症反应。好吧，我也不会做实验，没有评价的资格，**大家来瞅瞅** 这些实验大概属于怎样的水平。
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzVicYucKZ2iaxn5IibNczIGnicDTkic7WRMibdOdthnB3HxA45ehazw4zfeVgcS2JzDVaqxgA5GYgKI46g/640?wx_fmt=png)

**我的看法**

说实话我这人一直比较悲观，个人以为现在这种小样本的动物单细胞数据应当**不太容易** 发十分左右的文章，况且从单细胞数据分析的角度来说这篇文章确实不能算是优秀。但是这篇文章确实是DR领域**较早** 的scRNA-Seq作品(不是第一篇，有更早的[2])，作为开拓者之一确实值得《Diabetes》的青睐。所以目前若能抢先揭示一类疾病模型的scRNA-Seq图谱，仍有可能轻松发十分以上的文章。看来还是我太保守了，此前总说学完我们的教程([六万播放量的B站单细胞课程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489564&idx=1&sn=11de94de6ec045cb66b7dbdde644f6aa&chksm=9b3f614cac48e85a46e317c8e7d96dd67248dacaa1a82a3f98f1e540f99898d6710827b6bdac&scene=21#wechat_redirect>))可以发一篇3~5分的文章，看来实际情况要乐观的多，**祝各位都有光明的未来** ！

**参考文献** ：[1]: Niu T, Fang J, Shi X, Zhao M, Xing X, Wang Y, Zhu S, Liu K. Pathogenesis Study Based on High-Throughput Single-Cell Sequencing Analysis Reveals Novel Transcriptional Landscape and Heterogeneity of Retinal Cells in Type 2 Diabetic Mice. Diabetes. 2021 May;70(5):1185-1197.[2]: Van Hove I, De Groef L, Boeckx B, Modave E, Hu TT, Beets K, Etienne I, Van Bergen T, Lambrechts D, Moons L, Feyen JHM, Porcu M. Single-cell transcriptome analysis of the Akimba mouse retina reveals cell-type-specific insights into the pathobiology of diabetic retinopathy. Diabetologia. 2020 Oct;63(10):2235-2248.
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器的**微信号** ，方便各位随时交流、提建议（由助理接待）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
