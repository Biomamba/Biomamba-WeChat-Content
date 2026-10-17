---
title: "不会吧不会吧，Nature都能白嫖？"
date: 2023-03-21
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=2&sn=caeb8ed06ffd5239b58cebcd90843cf8&chksm=9b3c81dbac4b08cd9eec50978951a1b890ca08edec644ff75205a09ad1f067dff25d6ecb938e#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# 不会吧不会吧，Nature都能白嫖？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=2&sn=caeb8ed06ffd5239b58cebcd90843cf8&chksm=9b3c81dbac4b08cd9eec50978951a1b890ca08edec644ff75205a09ad1f067dff25d6ecb938e#rd
> 合集：单细胞教程全收录 / 文献速递

**写在前面**

本次介绍的是一篇今年3月发表在《NatureMedicine》上的单细胞数据集的meta分析文章，题为“Single-cell meta-analysis of SARS-CoV-2 entrygenes across tissues and demographics”,实时影响因子87.241**。**

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx5BrnoOJI40pRaXaNFtS7tT9VzL8iaIthXy6rqpPP5RAt6XrfDBKOdccVvYAUNBpOBySTKttRiaaDw/640?wx_fmt=png)

**一、背景介绍**

新型冠状病毒肺炎（COVID-19），由严重急性呼吸系统综合征冠状病毒2(SARS-CoV-2)感染引起。所有冠状病毒都以覆盖其表面的冠状“刺突”命名，称为刺突或“S”蛋白质。在体内，病毒的S蛋白锁定在一个细胞表面的受体上，可通过几种方式触发病毒进入细胞[1]，例如，直接与细胞融合或与细胞形成的囊融合，进而将病毒遗传物质释放至细胞中。研究显示[2]，血管紧张素转换酶2 (ACE2)和辅助蛋白酶(TMPRSS2和CTSL)是SARS-CoV-2进入细胞所必需的，它们的表达可能揭示了病毒的靶向性和对全身的影响。

**二、研究简介**

在该项研究中，作者通过对107项单细胞（scRNA-seq）和单核RNA测序(snRNA-seq)研究的综合分析，评估了ACE2和TMPRSS2、CTSL表达的细胞特异性。主要进行了31项肺部单细胞RNA测序研究的meta分析，这些数据来源于228名个体的377例鼻、气道和肺实质样本中的1,320,896个细胞。数据量庞大，研究样本包括公共数据和自测样本GSE153643（其实自测数据仅有两个样本）。其中，在GEO中检索筛选数据集的条件为:

●(1)提供非归一化计数数据

●(2)由10x Genomics Chromium平台生成

●(3)侧写人体样本。样本涵盖多类组织，包括原代组织、培养细胞系和化学或遗传干扰样本；后者包含两个10X样本（GSM4648564adipose_pooled腹部成形术中收集的皮下脂肪组织单细胞；GSM4648565 liver_pooled 肝脏切除术中肿瘤附近的健康肝组织细胞）

数据链接https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE153643 整体而言，该研究揭示了年龄、性别和吸烟的细胞类型特异性与ACE2、TMPRSS2和CTSL的表达水平之间的关联。基于基因组特征发现，男性、老年人和吸烟人群更易被SARS-CoV-2所感染。通过识别可被SARS-CoV-2感染的特定细胞类型，并将SARS-CoV-2进入因子与年龄或性别等关键协变量联系起来，有助于我们理解疾病结局中的COVID-19趋向性和异质性。

**三、研究框架**

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx5BrnoOJI40pRaXaNFtS7trxMAaeENogGrTMiaT817HdOnWXzpmcL32UvMtrAI9uVnxY5GticRG9ag/640?wx_fmt=png)

**四、研究结果**

**● 1、肺部、气道以及与COVID-19相关的其他组织的ACE2+ TMPRSS2+双阳性细胞。**通过列举92项人的scRNA-seq或snRNA-seq研究（包括7项肺和气道）中双阳性ACE2+TMPRSS2+ 细胞和ACE2+CTSL+ 细胞的比例，证明ACE2+TMPRSS2+ 上皮细胞在回肠、肝、肺、鼻粘膜、膀胱、睾丸、前列腺和肾脏中普遍存在；ACE2+ CTSL+双阳性细胞主要存在于胎盘、心脏、肺、肾和肠神经系统，富集于AT1和AT2细胞、肠上皮细胞、心室心肌细胞、心脏巨噬细胞、成纤维细胞等。由于ACE2的表达较低，作者通过荧光原位杂交和免疫荧光技术，在三个健康供体肺的气道和肺泡组织切片上进行了验证。结果显示，ACE2、CTSL和TMPRSS2通过荧光原位杂交显示在肺泡细胞中共表达，部分HTI -280+AT2细胞表达ACE2和TMPRSS2。**● 2、可能与病毒感染有关的其他蛋白酶的细胞类型特异性表达。**即便是没有TMPRSS2，SARS-CoV-2也会感染细胞，这表明其他蛋白酶也可能在病毒蛋白的蛋白水解切割中发挥作用。作者检测了ACE2与625个带注释的人类蛋白酶基因的共表达，最终得出，在所有已知的人类蛋白酶中，组织蛋白酶(CTSB、CTSC、CTSD、CTSL和CTSS)、蛋白酶体亚基(PSMB2、PSMB4和PSMB5)和补体蛋白酶(C1R、C2和CFI)在肺上皮细胞类型中常与ACE2共表达。

**● 3、肺和气道细胞中ACE2、TMPRSS2和CTSL的表达与年龄、性别和吸烟的相关性。**

作者对31项肺部单细胞RNA测序研究进行了荟萃分析，从228人的377个鼻腔、气道和肺实质样本中提取了1320,896个细胞，经研究发现，年龄、吸烟和性别在SARS-CoV-2进入细胞复制能力中均起着重要作用。具体而言，在男性、老年人和吸烟人群中，ACE2酶的表达量更高，这意味着新冠病毒更容易进入并感染这些细胞。在男性和老年人中TMPRSS2表达更多，同时除TMPRSS2以外的其他酶也可以使病毒感染人体。研究显示，ACE2、TMPRSS2和CTSL的表达水平随着男性的年龄增加而增加，包括在气道分泌细胞和肺泡2型细胞中的表达。

**● 4、气道、肺和肠道中ACE2+ TMPRSS2+双阳性细胞的免疫基因程序**

研究确定了与鼻上皮、肺和肠道中ACE2+TMPRSS2+双阳性细胞相关的组织和细胞程序。组织程序可在一种组织中不同细胞类型的双阳性细胞之间共享；细胞程序将双阳性细胞与其他相同类型的细胞区分开。组织程序与病毒感染和免疫应答的相关途径紧密联系，包括吞噬体构建、抗原加工和呈递以及细胞凋亡。来自多个组织的细胞程序，包括与TNF信号相关的基因，这增加了抗TNF治疗对ACE2、TMPRSS2表达影响的可能性。ACE2+阳性的上皮细胞的免疫样程序也通过scATAC-seq反映了对ACE2位点的调控。**● 5、小鼠模型中的保守表达模式。**SARS-CoV-2感染和治疗的进入临床研究前需要近似人类生理学的模型系统。表达人类ACE2 的hACE2小鼠模型已被确定为评价COVID-19治疗方法的重要模型。因此，作者研究SARS-CoV-2进入因子在人类和小鼠模型细胞类型中表达模式是否相似。健康小鼠气道上皮的多纤毛细胞主要表达Ace2+Tmprss2+和Ace2+Ctsl+，并在2-4月龄时增加，与人类气道的情况一致。此外，每天暴露于香烟烟雾2个月的小鼠全肺的scRNA-seq数据与人类气道上皮细胞的结果一致。烟雾暴露后，气道分泌细胞中Ace2+阳性的细胞数量和Ace2表达显著增加，而AT2细胞数量并未显著增加，指示人胎盘和小鼠胎盘发育的表达模式一致。

**五、讨论**

分析细胞类型特异性表达模式，有助于了解COVID-19的发病机制。该研究主要揭示了年龄、性别和吸烟与ACE2、TMPRSS2和CTSL表达水平的细胞类型特异性的相关性。由于气道上皮细胞RNA-seq信号的增加可能会掩盖AT2细胞ACE2表达量的降低，因此需要通过单细胞测序来分析不同上皮细胞的ACE2表达与吸烟的相关性，由此也体现出了单细胞检测在本篇研究中的优势。在该项研究中，作者纳入的样本数据来源于200多名捐赠者，拟合此模型需要聚合多个数据集，并通过一致的单元格类型注释进行协调，工作量不容小觑。但是客观而言，该研究使用的样本来源于多个地区，捐赠者的民族、遗传史、患病史等因素仍然可能混淆研究的关联性结果。为验证吸烟与年龄的相关性，该研究还构建了小鼠模型，结果显示人与小鼠胎盘发育的表达模式并无显著差异。但同样有报道显示[3]，在老龄小鼠中，ACE2表达量有所降低，可见小鼠模型的应用仍然存在一定的局限。除此之外，随着研究的深入，数据集数量增加，后续可以进一步分析协变量之间的非线性关系，整合遗传风险因素和流行病学因素，生成新的图谱，进而加深对疾病的了解。

**六、总结反思**

完成这种研究，对研究者自身而言有一定的要求，不仅仅包括明确且广泛的认知，良好的洞察力，同时也要求掌握相关的研究技能和技术。

**●** 1\. 首先要了解研究背景，找出现有研究的缺陷，明确仍然需要深入探究的问题，才能找准研究方向。

**●** 2\. 研究者要具备娴熟的数据分析和绘图能力，精美的数据图表是文章的重要加分项，能提升文章的档次。

**●** 3\. 完善的数据是绘图和分析的基础，因此掌握收集、分析数据的技巧和方法也同样重要。目前来看，公开数据和自测是单细胞测序数据的两大主要来源，不管数据的来源如何，一定都需要第二点技能的支持。

栉风沐雨科研路。学习优秀的文章，必然能从中获得启发，提升我们的思辨能力。通过不断的积累，砥砺前行，必能在科研之路上有所收获。

**七、参考文献**

[1] FungTS, Liu DX. Human Coronavirus: Host-Pathogen Interaction. Annu Rev Microbiol.2019 Sep 8;73:529-557. doi: 10.1146/annurev-micro-020518-115759. Epub 2019 Jun21. PMID: 31226023.[2] Walls AC, ParkYJ, Tortorici MA, Wall A, McGuire AT, Veesler D. Structure, Function, andAntigenicity of the SARS-CoV-2 Spike Glycoprotein. Cell. 2020 Apr16;181(2):281-292.e6. doi: 10.1016/j.cell.2020.02.058. Epub 2020 Mar 9. Erratumin: Cell. 2020 Dec 10;183(6):1735. PMID: 32155444; PMCID: PMC7102599.[3] Lou LL, Xie L,Hu Y, Chen LN, Liang P, Shi F, Liu CJ, Liu HM. [Association of age distributionwith the expression of angiotensin-converting enzyme 2 in lung tissues insevere acute respiratory syndrome coronavirus 2 infection: reflections from thestudy of RAS pathway expression in mice]. Zhongguo Dang Dai Er Ke Za Zhi. 2020Oct;22(10):1119-1124. Chinese. doi: 10.7499/j.issn.1008-8830.2005045. PMID:33059811; PMCID: PMC7568992.

封面文献doi：10.1038/s41591-020-01227-z

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器的**微信号** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
