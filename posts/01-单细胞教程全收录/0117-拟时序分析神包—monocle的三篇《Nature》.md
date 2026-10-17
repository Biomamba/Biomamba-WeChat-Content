---
title: "拟时序分析神包—monocle的三篇《Nature》"
date: 2024-07-02
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519064&idx=1&sn=173948cb696c7d33b90cd21b28986777&chksm=9b3cf208ac4b7b1e328fdc445f9aecd6cfb836fdb33767876ba1aa35c55098a2a071dbe8e2f0#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# 拟时序分析神包—monocle的三篇《Nature》

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519064&idx=1&sn=173948cb696c7d33b90cd21b28986777&chksm=9b3cf208ac4b7b1e328fdc445f9aecd6cfb836fdb33767876ba1aa35c55098a2a071dbe8e2f0#rd
> 合集：单细胞教程全收录 / 文献速递

**写在前面**

一般获得单细胞测序数据，对细胞类型进行鉴定后，还要对其进行进阶分析如拟时序分析，即按照一个虚拟的时间，基于关键基因的表达模式对单个细胞进行排序，以得到细胞与细胞之间的转化和演替的顺序和轨迹；Monocle是常用的ScRNA-seq拟时序分析的经典工具，目前已更新至第3版本；当我们使用Monocle 3分析时，官网（https://cole-trapnell-lab.github.io/monocle-release/papers/）要求我们引用以下3篇文献，当然这3篇文章也是Monocle工具最好的学习资料，让我们一起来看看吧。

拟时序分析系列**教程** 可见：

B站连续播放比较方便：

https://www.bilibili.com/video/BV1br4y1x7Hf?p=1

**往期推送**

[《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)

[《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)

[《拟时序分析》3.monocle2实操：精简版拟时序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487398&idx=1&sn=6621eed90157d8da06ef778c40bd5554&chksm=9b3f76f6ac48ffe081ddfee3a323e0e31c1fda33731012de73168cf2ab30a226cf70c848f769&scene=21#wechat_redirect>)

[《拟时序分析》4.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)

[单细胞测序数据进阶分析—《拟时序分析》5.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)

[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)

[单细胞测序数据进阶分析—《拟时序分析》7.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)

[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)

[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494479&idx=1&sn=32f39c79c4c9fc07aa829eed49016da3&chksm=9b3c921fac4b1b091efcdd151500b69d19f71d5ca518122af697fc37e87acd915f3be5f63fb8&scene=21#wechat_redirect>)

**第一篇——Nature Biotechnology**

首先**第一篇文章** 的题目是：“The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells /单细胞拟时序分析揭示了细胞命运决定的动力学和调控因子”；这篇文章于2014年发表在Nature Biotechnology上，影响因子是46.9。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSuoW8icq0v1SHlcH5BFMCnxRUUd3haV02lH4TzNs8JichokLQTeoHBoDw/640?wx_fmt=png&from=appmsg)

文中，作者主要研究了骨骼肌成肌细胞分化过程中的单细胞转录组动力学。在高有丝分裂原的条件下分离原代人骨骼肌成肌细胞，细胞稳定后使用低血清培养24h以诱导分化；在分化后24h,48h和72h使用Fluidigm C1系统经微流控技术分别捕获74,77和49个细胞（Figure1a）。从捕获的每个细胞中提取RNA并构建单个mRNA-Seq文库，对每个文库进行不少于400万reads的深度测序。拿到测序数据后，作者首先证实了单个细胞的平均表达谱和相同时间获取的大量细胞的表达谱类似，且单个细胞表达谱中均能检测到中等表达基因（FPKM≥1），证明测序数据可信（Figure1b）；但令人惊讶地是，成熟肌细胞的标记物（ENO3和MYH3）在血清转换后的时间点都存在但表达量不同，许多其他基因也表现出类似的时间异质性（Figure1c）。作者推测其原因很有可能是细胞不同步分化所导致的，不同时间点成肌细胞，中间肌管细胞，成熟肌管细胞共同存在，其中MYH2作为成熟肌管细胞的标志，72h表达最高（Figure1d）。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSmySIQol8Y5ia5UY9RiaNVaPs6f7PIwODbpWVKCibicL69qiauE6grHlgnlg/640?wx_fmt=png&from=appmsg)

接下来作者开发了Monocle，可以根据细胞的分化进程而不是收集时间对细胞进行排序，从而提高了连续细胞对之间的转录相似性（Figure2a）。该算法首先将每个细胞作为一个点，将每个基因的表达作为一个维度，其次使用降维处理降低维度使数据更容易进行可视化，然后根据细胞的点来计算最小生成树（MST），以衡量每个点之间的距离;最后通过MST找到最长的路径，对应于转录相似细胞的最长序列，最终得到单个细胞分化过程的“轨迹”。Monocle分析将肌细胞分化处理为二维图像，并且分离出非分化细胞分支（Figure2b）。当把拟时作为横坐标进行基因表达的分析，作者展示了1061个基因的动态表达（Figure2c）。MEF2C和MYH2(分别是分化细胞的早期和晚期标志物)，通过免疫荧光和RNA-seq按照收集时间展示阳性细胞的比例；RNA-seq按照拟时展示阳性细胞的比例，作者发现细胞标志物的表达与拟时序分析动力学高度一致，验证了拟时序分析的准确性（Figure2d）。同时作者发现分化过程中拟时序分析的基因动态变化学与小鼠肌生成期间基因变化高度一致，例如CDK1,ID1和MYOG等关键基因的差异表达，因此Monocle分析揭示了肌成细胞控制分化关键基因表达的具体时间。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSKILkxDJSdWhRGl1ag5s9RPeK7VBAEHJkLgFC78dtlicdmXl5e32mtAw/640?wx_fmt=png&from=appmsg)

接下来作者将具有相同表达趋势的基因分组，他们很有可能具有相同的生物学功能和调节因子，当根据时间和方向对基因进行聚类，发现基因表达六种不同的趋势（Figure3），黑色为已知的致肌因子，红色为在肌肉分化中没有已知作用的因子。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSmYyO9pbcSGyrj4F6gH4ia9AaM6nlxNMeHco79J22LGib3XxxhJZLXqgA/640?wx_fmt=png&from=appmsg)

为了进一步确定驱动分化过程的因素，作者对于每个拟时间簇进行顺式调节因子分析，作者发现了很多之前肌肉发育研究没有注意到的转录因子，为了进一步验证这些基因的重要性功能，作者选择11个单细胞进行RNA干扰靶向抑制这些基因，发现靶向MZF1, ZIC1, XBP1和USF1等基因后，细胞发生了明显的分化动力学转变，使用shRNA敲低XBP1、USF1、ZIC1和MZF1能够增强肌管细胞的形成（Figure4a）。特别的是，一些因子的结合基序在启动子和增强子中高度富集，其基序与已知的肌肉调节基序一致（Figure4b）。例如在增强子中同时富集到USF1基序和MYOD基序。作者共确定了8个调节因子，并推测这些因子可能是通过与促生因子竞争调节元件来抑制分化（Figure4c）。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSS04j0Ja73sUb6GPyjiaHX8vuyDibIticr96SVonVRyR4WR8AAaetXeKLg/640?wx_fmt=png&from=appmsg)
**结束语：** 这篇文章作者向我们展示了如何使用Monocle进行肌细胞分化过程中的拟时序分析，并与小鼠肌肉发育过程中的基因表达变化进行了比较，验证了拟时序分析结果的准确性，同时，作者发现了之前研究没有被注意到的转录因子，揭示了他们在肌肉发育过程中的关键调控作用，看完这篇文章，你有没有进一步了解到Monocle呢？

**第二篇——Nature Methods**

接下里**第二篇文章** 的题目是：“Single-cell mRNA quantification and differential analysis with Census /使用Census算法进行单细胞mRNA 定量及差异分析”；这篇文章于2017年发表在Nature Methods上，影响因子是48.0。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSjIib0dKYzOvZG49iaIDoDjPL0DEgjzKugnFsWeicG3VHkMrnJicL5Tsk3A/640?wx_fmt=png&from=appmsg)
作者开发了通过单细胞分析工具包Monocle 2获得的Census算法，它能够不经Spike-in标准化而将RNA-seq表达数据转化为相对转录水平，与归一化得到的表达水平相比，相对转录水平的准确性明显提高，这篇文章中作者通过重新分析几种发育和疾病状态下的测序数据来验证Census算法的准确性。单细胞测序主要是通过外源RNA “Spike-in”或独特的分子标签（UMI）来指征相对转录水平，而Census算法无需添加“Spike-in”或UMI便能将相对表达量转化为转录水平。首先作者进行了Census算法的方案展示（Figure1a），从细胞裂解物中获取mRNA经逆转录获得约10%的cDNA来代表转录水平，大多数方案会使用mRNA的polyA尾来作为模板从而获得每个基因的cDNA全长（Figure1b），因此，每个细胞相对丰度分布模式下或测量到的所有可检测表达的基因应该存在于大约1个cDNA拷贝中。作者通过分析肺上皮细胞的发育过程来评估Census算法的准确性，获得了每个细胞转录本总数的估计值（Figure1c）。其结果与经“Spike-in”标准化后的数据高度相似，且基因的表达变化也高度相似（Figure1d,e）![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwS92JtPfzpNqHQDNOHnITamIOdI1LR7VmjwfgflDqo71TS0Mk9EGDBbA/640?wx_fmt=png&from=appmsg)
接下来作者评估了Census算法能否改善下游的差异分析，作者选择了Monocle，edgeR,DEseq2和SCDE等分析工具，获得差异基因的ROC曲线来评估准确度，相比于Read Counts和TPM，Census算法的准确度明显提高（Figure2a）。同时Census算法也提高了工具之间的一致性（Figure2b）。因此作者得出了当“Spike-in”或UMI不可用时，Census算法或许是最好的选择。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSdibc3J8CqdwZN8oss55aaU6iarias7uh35jX4n92TibGScrrWHnR5fsjtA/640?wx_fmt=png&from=appmsg)

大多数单细胞分析的研究旨在找出发育过程中的关键调节因子，Monocle算法进行的拟时序分析，可以用来展示分化过程中的基因表达水平，所以作者选择了最近一篇研究中的RNA-seq数据进行重新分析，轨迹开始的地方是具有高增殖活性（Ccnb2,Cdk1）的细胞，分化过程中逐渐转向AT1（Pdpn）和AT2（Sftpb）两个进化分支，AT1和AT2分别是I型和II型肺上皮细胞（Figure3a）。作者接下来进行了BEAM（分支表达分析建模）鉴定，分析出了分支依赖性变化的一些基因（Figure3b）。共鉴定出1,219个基因，包括肺上皮细胞标志性基因（Pdpn和Sftpb）等（Figure3c）。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwS9IVnG8agib8TTyDiaea0zdQnXqx81HkNMsa64SgpLAt4mhdlIGAeAuHQ/640?wx_fmt=png&from=appmsg)

分支不仅可能在发育过程中出现，而且也可能出现在突变、药物治疗或其他细胞扰动刺激后。因此作者也重新分析了骨髓来源的树突细胞（BMDC）对LPS刺激而产生转录反应的测序数据（Figure4a）。对野生型（WT）小鼠的BMDC和缺乏干扰素α（Ifnar1-/-）或Stat1（Stat1\--）受体的小鼠的BMDC进行了比较,发现不同小鼠的细胞出现在不同的分支上（Figure4b）。BEAM算法鉴定出870个关键调控基因，均与干扰素信号转导相关（Figure4c）。这些因子大都是分支依赖性的，说明BEAM算法能够区分关键调控基因和下游基因（Figure4d,e）。这些结果展示了Monocle 2和BEAM能够进行关键信号通路的调节分析。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSsFnauHDldhjfc18Wc7FcTSDk80FA6JZYBv1FqzfHYrC7ticM0IsMdaA/640?wx_fmt=png&from=appmsg)
单细胞RNA-seq实验中也渐渐有研究开始关注RNA的剪接变化，作者使用Census算法进行了成肌细胞中的异构体转录本检测，捕获了74个基因剪接变化的拟时序分析，图中所示的是TPM1选择性剪切的分析示意图（Figure5）。单细胞分析也可以揭示每个基因的两个等位基因进行协调调控的程度。作者进行了混合遗传背景(CAST/EiJ × C57BL/6J)着床前小鼠胚胎的单细胞测序数据分析，大多数的等位基因平衡为50%（Figure6a）。雌性胚胎中父系 X 染色体的失活表现在16个细胞阶段，表现出父系 X 染色体贡献的基因逐渐减少（Figure6b,c）。且单等位基因的预期表达率接近100% ，并且随着表达的增加而降低（Figure6d）。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSwn1TUeIX10wThCRKPA4oQNfiaLD1riahYicBic2orHyibu5TiaLpYHysy9Ew/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSbBcWNz0Q07KL6FR4E9icicznB7aoFwrvn3FKWyD8lFnxX0ib6hrEBCX8g/640?wx_fmt=png&from=appmsg)
**结束语：** 经过作者的分析展示，相信大家也很震惊Monocle以及Census算法能解决如此多的问题，并且具有有很高的准确性，在大家的课题中是否也存在类似的需要解决的问题呢，可以使用Monocle工具来进行大胆的尝试。

第三篇——Nature Methods

最后**第三篇文章** 的题目是：“Reversed graph embedding resolves complex single-cell trajectories /反向图嵌入解决了复杂的单细胞轨迹问题”；这篇文章于2017年发表在Nature Methods上，影响因子是48.0。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwS9Xpsv37WNU9z4C4LNDI6k0d6Y1Y3hKqaM1odAgheOYKn6jEUg6GibQw/640?wx_fmt=png&from=appmsg)这篇文章中作者提出了Monocle2能够通过反向嵌入图，一种完全无监督的算法，准确地重建复杂的单细胞轨迹而得到细胞多种的命运决策。Monocle 2首先使用“dpFeature”选择降维处理后的细胞簇的差异基因，接下来使用“DDRTree”，一种可扩展的RGE算法，在默认情况下展示单细胞的主树，其描述了生物进程中整体基因的变化（Figure1a），同时，Monocle 2可以自动识别描述细胞状态变化的分支点。为了评估Monocle 2的准确性，作者将其应用于成肌细胞的分化过程分析（Figure1b）。Monocle 2重建了一个分支点和两个结果的拟时序轨迹（Figure1c）。并且与丝裂原停止相关的 Ccnb2基因，在两个分支上表现出相似的动力学，但是许多肌肉收缩所需的基因仅在两个分支中的一个上被强烈激活。接下来作者将Monocle 2拟时序分析的新算法进行比较，包括 Monocle 1，Wishbone3， DPT和 SLICER13。与Monocle 2不同的是，这些算法不构建显式树，而是通过细胞间的距离来预测细胞的相关性，进而通过最近邻图(Wishbone和 SLICER)或最小生成树(Monocle 1)或分析计算(dPT)来近似。与其他算法相比，Monocle 2显示出更准确的排列（Figure1d）和更高的一致性（Figure1e）![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSQRia3EAEnIDQqhjAktGDj4doV9h5B0Fu6XxVo9Zzw8j1rsNNYhOofnw/640?wx_fmt=png&from=appmsg)

同时，作者也使用Monocle 2进行了流式分选的小鼠骨髓生成的不同阶段(即LSK，CMP，GMP 和 LKCD34 +)细胞的分析，并重建了一个具有两个主要分支和三种不同细胞命运的细胞轨迹。LSK细胞（骨髓干细胞）位于树的根部，而CMP（共同髓系祖细胞）, GMP（淋系/髓系定向分化祖细胞）,和 LKCD34+（CD34+干/组细胞）细胞位于分支末端（Figure2a）。而来自缺失Gfi1（造血系统中影响细胞分化的重要转录因子）或Irf8（骨髓细胞谱系定型和分化的必需因子）的小鼠骨髓细胞并没有产生类似WT小鼠骨髓分化轨迹的结构（Figure2b）。以上结果进一步说明了Monocle 2分析的准确性。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSlpTHpfmiaibAWtFIs4Rczk8TCicgRkLxKlZuIVBOOA0BJh2TWicYiaO99uA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwv73YnWh425ZUZ6ZXtwOwSLx8Tw5you0deBJAtxVfx6WZWYllHrqA7gsGIleACf6liar0FZ7lop6g/640?wx_fmt=png&from=appmsg)

**结束语：** 这篇文章，作者进行了Monocle 2与Monocle，Wishbone3， DPT及SLICER13等算法分析结果的比较，发现Monocle 2具有更高的准确性和一致性。同时Monocle 2对于其他研究中的测序数据分析也显示出与预期一致的结果。相信大家已经很了解Monocle 2的应用了，如果感兴趣的话可以找出原文进行更深入的学习。

看到这里，大家是否有学习monocle的冲动呢：

拟时序分析系列**教程** 可见：

B站连续播放比较方便：

https://www.bilibili.com/video/BV1br4y1x7Hf?p=1

**往期推送**

[《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)

[《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)

[《拟时序分析》3.monocle2实操：精简版拟时序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487398&idx=1&sn=6621eed90157d8da06ef778c40bd5554&chksm=9b3f76f6ac48ffe081ddfee3a323e0e31c1fda33731012de73168cf2ab30a226cf70c848f769&scene=21#wechat_redirect>)

[《拟时序分析》4.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)

[单细胞测序数据进阶分析—《拟时序分析》5.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)

[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)

[单细胞测序数据进阶分析—《拟时序分析》7.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)

[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)

[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494479&idx=1&sn=32f39c79c4c9fc07aa829eed49016da3&chksm=9b3c921fac4b1b091efcdd151500b69d19f71d5ca518122af697fc37e87acd915f3be5f63fb8&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=1&sn=d9517a0803ad75cb7be430806834e7b8&chksm=9b3ca7bdac4b2eaba1ad01ed04ab1fbcbafcf4f6ddfe9e4f76ed9229707f545fe7d9c9ffd6ae&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（别问在么，添加时直接说来意）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)您点的每个赞和在看，我都认真当成了喜欢
