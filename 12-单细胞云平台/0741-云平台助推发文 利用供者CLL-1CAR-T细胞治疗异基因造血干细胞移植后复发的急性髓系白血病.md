---
title: "云平台助推发文| 利用供者CLL-1CAR-T细胞治疗异基因造血干细胞移植后复发的急性髓系白血病"
date: 2025-09-16
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531106&idx=2&sn=e1382bff779571f606544e7067c361a7&chksm=9b3c0332ac4b8a24e6766c82680d0fc1ec71c0d6becdb98144ed8efbf3cf14226b0c27aa26d0#rd
albums: ["单细胞云平台"]
---

# 云平台助推发文| 利用供者CLL-1CAR-T细胞治疗异基因造血干细胞移植后复发的急性髓系白血病

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531106&idx=2&sn=e1382bff779571f606544e7067c361a7&chksm=9b3c0332ac4b8a24e6766c82680d0fc1ec71c0d6becdb98144ed8efbf3cf14226b0c27aa26d0#rd
> 合集：单细胞云平台

#

**一、写在前面**

**急性髓系白血病（AML）** 是一种高度侵袭性的血液肿瘤，**异基因造血干细胞移植（allo-HSCT）后复发** 患者预后极差，吉西他滨等传统化疗方案疗效有限。**嵌合抗原受体T细胞（[ CAR-T](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506371&idx=1&sn=a9f44bdfd795a4d04615bc307cd23cf5&scene=21#wechat_redirect>)）疗法**作为新兴免疫治疗手段，已在B细胞肿瘤中取得突破，但针对AML的靶点开发仍面临挑战。**人类C型凝集素样分子1（CLL-1）作为AML特异性靶点** ，具有广阔潜力。这项研究探讨了**供体来源CLL-1CAR-T细胞** 在allo-HSCT后复发AML患者中的应用，共纳入了12名患者，分三组进行**剂量递增试验** ，并通过**[单细胞RNA测序（scRNA-seq）](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)** 分析CAR-T细胞动态。本文旨在评估**CLL-1CAR-T的疗效与安全性** ，揭示其在AML免疫治疗中的潜力。原文链接:https://pubmed.ncbi.nlm.nih.gov/39896798/
DOI: 10.3389/fimmu.2024.1491341
![image-20250831230715833](../../images/f809a3a1e4d4b6c5.webp)
本篇文献的部分分析是通过[SeekSoul Online](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115#wechat_redirect>)完成的![](../../images/b61e435b42a51244.png)。此外，我们也在上周推出了与云平台配套的免费教学课程[直播中，零代码学会单细胞画图、亚群分析、特征分析、拟时序分析、转录因子、细胞通讯、肿瘤异质性分析等](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531048&idx=2&sn=7643d21ed11c95b76b143edea305021d&scene=21#wechat_redirect>)。欢迎感兴趣的小伙伴联系我们参与作业打卡活动，即可免费获取3个月的云平台使用权限~B站课程视频：https://www.bilibili.com/video/BV1anpMznE18/云平台地址：https://seeksoul.online/t_static/Biomamba/Biomamba.html![](../../images/f1e435e05f985e01.webp)
如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21&token=167164344&lang=zh_CN#wechat_redirect>)**教学** 、生信热点**[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)** 、自测数据**个性化分析** 辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[**Biomamba_zhushou**]

**二、主要结果
**

1\. 患者特征这项临床研究最初招募了14名在异基因造血干细胞移植（allo-HSCT）后复发的急性髓系白血病（AML）患者，但其中2名患者因疾病进展过快，在CAR-T细胞输注前退出了研究。共有12名可评估的患者接受了治疗，患者信息如表1所示。这是一个经过多线治疗、病情复杂的极高危患者群体。患者的中位年龄为30.5岁，既往接受治疗的中位线数为5.5线。所有患者均在allo-HSCT后复发，其中2名患者甚至是在第二次移植后复发。接受治疗时，患者的中位肿瘤负荷为20.21%，部分患者还存在**中枢白血病（centralleukemia）** 、**髓外浸润（extramedullaryinfiltration）** 以及高危的细胞遗传学和分子特征。值得注意的是，其中2名患者在接受CAR-T治疗前，已经尝试过化疗联合**供者淋巴细胞输注（DLI）** 进行挽救治疗，但均未取得效果，凸显了这部分患者治疗的棘手程度。表1![www.frontiersin.org](../../images/f6420fea026e9b2a.webp)

2\. **临床疗效** 在疗效方面，所有12名接受治疗的患者均表现出肿瘤负荷的降低，显示了该疗法普遍的抗肿瘤活性。如图1所示，9名患者（75%）达到了完全缓解（CR），其中**7名患者（58.33%）** 更是达到了检测不到微小残留病的完全缓解（**MRD-CR** ），另外**2名患者（16.67%）** 达到了MRD阳性的完全缓解（**MRD+CR** ）。此外，还有2名患者获得部分缓解（PR），仅有1名患者无应答。在所有患者中，中位缓解持续时间为7.13个月。对于其中8名获得缓解的患者，CLL-1CAR-T细胞疗法成功地作为一项**“桥接”治疗（"bridging"therapy）** ，使他们能够继续接受后续的二次造血干细胞移植（HSCT）。在中位随访12个月后，部分患者因严重CRS、感染或原发病复发等原因死亡，这反映了尽管该疗法初步疗效显著，但这部分患者群体本身仍面临极高的治疗风险。![www.frontiersin.org](../../images/2c034ecf20770a4d.webp)

图1

3\. **安全性评估** 安全性方面，研究团队评估了CLL-1CAR-T细胞相关的副作用（表2）。该疗法的主要毒副作用与常规CAR-T疗法相似，但血液学毒性尤为突出。**细胞因子释放综合征（CytokineReleaseSyndrome,CRS）** 在**所有12名患者** 中均有发生，其中**5名患者** 达到了3级及以上的重度CRS，且重度CRS更多地出现在最高剂量组中。3名患者出现了相关的神经毒性（**CRES** ），其中1名患者达到了最严重的4级并最终导致死亡。然而，本研究中最值得关注且普遍发生的不良事件是严重的骨髓抑制。**所有患者** 都经历了严重的**全血细胞减少症（pancytopenia）** ，具体表现为**11名患者（91.67%）** 出现了4级**中性粒细胞减少症（neutropenia）** ，**7名患者（58.33%）** 出现了4级**血小板减少症（thrombocytopenia）** （图2A）。为应对这一严重的副作用，8名患者接受了减低强度的预处理方案后，成功进行了二次移植以恢复造血功能。其他常见的不良反应还包括低磷血症、低钙血症和肝酶升高等（表3）。表2

![www.frontiersin.org](../../images/6f916951b33d18a4.webp)

![www.frontiersin.org](../../images/54f1077925608682.webp)

图2

表3

![www.frontiersin.org](../../images/3205ac109b0003ea.webp)

4\. **CLL-1 CAR-T细胞在外周血中的扩增和持久性** 通过[流式细胞术](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529204&idx=1&sn=dc70f79b6460e9a134d8dbee531fc3c7&scene=21#wechat_redirect>)检测，研究人员发现在所有12名患者的外周血中都能检测到**CLL-1CAR-T细胞（CLL-1CAR-Tcells）** 的扩增，达到峰值扩增的中位时间为**9天** （范围为7-11天）（如图2B、C所示）。与CAR-T细胞扩增相对应，患者体内的**铁蛋白（ferritin）** 和多种**细胞因子（cytokines）** 水平也出现了不同程度的升高。值得注意的是，为了降低毒副作用并为后续的二次移植做准备，研究人员在移植前使用了鲁索替尼（Ruxolitinib）和类固醇等药物来终止CAR-T细胞的增殖。因此，在该研究的设计下，CAR-T细胞**在第三周后就检测不到了** ，其持久性被人为地缩短了。

5\. **CAR-T细胞中的scRNA-seq和聚类分析**

为了更深入地探究CAR-T细胞在体内的动态变化和功能特征，研究人员对一名经历重度CRS的4号患者，在CAR-T细胞输注前（即产品中）和体内扩增达到峰值时这两个时间点，进行了**[单细胞RNA测序（scRNA-seq）](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)** 。分析发现，CAR-T细胞的亚群构成发生了显著的动态变化：在输注前的产品中，细胞以**CD4+初始T细胞（CD4+Tn）** 为主；而在体内扩增达到峰值时，则转变为以**CD4+效应记忆T细胞（CD4+Tem）** 为主导（图3D）。与这种表型转变相对应的是功能上的增强，扩增峰值时的CD4+CAR-T细胞显著上调了与**细胞杀伤功能（cellkillingfunction）** 相关的基因（如NKG7,PRF1,GZMB）和**记忆T细胞功能（memoryTcellfunction）** 相关的基因（如GZMK），表明CAR-T细胞在进入患者体内后，其杀伤能力和记忆潜能都得到了强化（图3E）。值得注意的是，该名患者的CAR-T细胞无论是产品还是扩增后，均以**CD4+CAR-T细胞** 为主，功能富集分析也显示其与炎症反应通路相关，作者据此推测，高比例的CD4+CAR-T细胞可能与该患者经历的重度CRS有关。

![www.frontiersin.org](../../images/b436e7d0b328d7ab.webp)

图3

**三、随便聊聊**

这项临床研究证实，供体的CLL-1CAR-T细胞在allo-HSCT后复发AML患者中显示出**可接受的安全性和显著疗效** ，**58.33%患者达到MRD-CR** （微小残留病灶阴性的完全缓解），CAR-T细胞**峰值扩增时间为9天** 。scRNA-seq分析揭示**CD4+CAR-T细胞在峰值期上调杀伤和记忆相关基因** ，但**高比例CD4+细胞可能与严重CRS（细胞因子释放综合征）相关** ，提示调整CD4:CD8比例可缓解副作用。当然研究也有一定的局限性，即**样本量有限** ，**长期随访数据不足** ，且**重度粒细胞减少** 进一步优化管理（如供体干细胞桥接）。可在未来进一步探索**CLL-1CAR-T与其他疗法的联合应用** ，以提升持久缓解率，并通过更大规模试验验证其临床价值。该研究为**AML免疫治疗提供了新方向** ，推动精准医学发展。

**四、参考文献**

[1]: Zhang M, Zhang X, Wang J, Lu W, Xiao X, Lyu H, He X, Pu Y, Meng J, Lyu C, Cao X, Zhao M. Utilization of donor CLL-1 CAR-T cells for the treatment of relapsed of acute myeloid leukemia following allogeneic hematopoietic stem cell transplantation. Front Immunol. 2025 Jan 17;15:1491341. doi: 10.3389/fimmu.2024.1491341 . PMID: 39896798; PMCID: PMC11782272.

![图片](../../images/95968d673495ca4c.png)

**如何联系我们**

![图片](../../images/b36f05f29bee05ab.png)![图片](../../images/0667abfe3cfb054d.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/eff615a0a49ee4ca.webp)![图片](../../images/735cbbf3b51b2cbf.gif) 您点的每个赞和在看，我都认真当成了喜欢
