---
title: "《Nature methods》：基于单细胞多组学检测DNA甲基化和组蛋白修饰重构表观基因组维持的动态过程"
date: 2026-09-26
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542445&idx=1&sn=19321604b1584835ac4a97a311a14f60&chksm=9b3c5ffdac4bd6ebfea8c74baff8dc10e198ac9bacbf563cae196191c36bc9c25b80b95c487c#rd
albums: ["文献速递"]
---

# 《Nature methods》：基于单细胞多组学检测DNA甲基化和组蛋白修饰重构表观基因组维持的动态过程

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542445&idx=1&sn=19321604b1584835ac4a97a311a14f60&chksm=9b3c5ffdac4bd6ebfea8c74baff8dc10e198ac9bacbf563cae196191c36bc9c25b80b95c487c#rd
> 合集：文献速递

* * *

**一、写在前面**

**文章 DNA methylome profiling of circulating tumor cells in lung cancer at single base-pair resolution（IF=32.1）**发布于2021年**《** Nature methods》。

[DNA甲基化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541876&idx=1&sn=454053fc7add53addcb84f5c48aa75ec&scene=21#wechat_redirect>)（5 - 甲基胞嘧啶；5mC）和组蛋白修饰是两种主要的、可遗传的表观遗传标记。开创性的工作已经通过亚硫酸氢盐测序（scBS-seq）建立了[单细胞5mC](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541876&idx=1&sn=454053fc7add53addcb84f5c48aa75ec&scene=21#wechat_redirect>)分析方法。此外，还有几种方法能够进行单细胞组蛋白修饰分析，通过特定的抗体分别将蛋白A-微囊藻核酸酶（scChIC）或蛋白A-Tn5转座酶（scCUT & TAG）连接到修饰的核小体上。组蛋白修饰和DNA甲基化以多种方式相互作用，例如招募DNMTs结合到H3K36me3，或者UHRF1结合到H3K9me3；然而，目前还没有技术能够在单细胞中捕捉到这些[相互作用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)。为填补这一空白，作者开发了单细胞Epi2-seq（scEpi2 - seq），该方法能够在单细胞中同时读取组蛋白修饰和DNA[甲基化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538223&idx=1&sn=2be2cf61a27b9a5def3b5f0bad4d152b&scene=21#wechat_redirect>)，能够为表观遗传相互作用的动态过程提供了宝贵的见解。 更多单细胞甲基化分析教程可见：[![图片](../../images/4e57987612836970.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541876&idx=1&sn=454053fc7add53addcb84f5c48aa75ec&scene=21#wechat_redirect>) 如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21&token=827157490&lang=zh_CN&poc_token=HLe6Q2mjR5L5stXqZGOdzOvf2Vk8eTYi05UUYRRy#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469&token=827157490&lang=zh_CN#wechat_redirect>)、自测数据个性化分析辅导、[实验科研服务](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=1&sn=578993fdfa060d38c80e2df6fc200c39&scene=21#wechat_redirect>)和[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=2&sn=1d329f22e35586dc794ce30aa6bd0ce4&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、主要内容**

**一：单细胞Epi2 - seq检测[ 单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)中的组蛋白修饰和CpG甲基化。**

基于sortChIC技术，单细胞Epi2 - seq利用TET辅助的吡啶硼烷测序（TAPS）实现单细胞中DNA甲基化和组蛋白修饰的多组学读取（Fig.1a）。在分离和通透化后，通过抗体将pA - MNase融合蛋白连接到特定的组蛋白修饰上。单细胞通过流式细胞分选（FACS）被分选到384孔板中。接下来，通过添加必需的辅因子Ca²⁺启动MNase消化。产生的片段经过修复和A尾化处理。然后，将含有单细胞条形码、唯一分子标识符（UMI）、T7启动子和Illumina接头的接头连接到这些片段上。从384孔板中收集材料并进行TAPS处理。与基于亚硫酸氢盐的方法不同，TAPS将甲基化胞嘧啶（5mC）转化为尿嘧啶，同时保持条形码化的单细胞接头完整。文库制备包括体外转录（IVT）、逆转录和PCR。在进行双端测序后，可以从每条读取中提取多条信息。通过比对基因组位置可以确定修饰组蛋白的位置，而C到T的碱基转换则可以识别甲基化胞嘧啶。此外，还可以从测序读取的起始位置之间的距离推断出核小体的间距（Fig.1a）。

之后作者根据每个细胞的唯一读取数量和平均甲基化水平筛选出高质量的细胞，结果有60.2% - 77.9%的细胞通过了质量控制（扩展数据图2a）。在剩余的细胞（n = 1981）中，检测到每个单细胞中有超过50000个CpG位点（扩展数据图2b）。接下来，通过计算每个细胞的峰值区域读取比例（FRiP）来量化单细胞组蛋白测量的特异性（通过MACS3识别）（扩展数据图2c）。平均FRiP值根据抗体的不同在0.72 - 0.88之间（扩展数据图2c）。且空白阴性对照孔中检测到的读取数量少得多（扩展数据图2d），这突显了单细胞Epi2 - seq数据染色质模态的高灵敏度和特异性。作者的测量结果与之前发表的数据（包括sortChIC和ENCODE ChIP - seq）的伪批量比较显示出高度相关性（扩展数据图2h，i）。[单细胞轨迹](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)显示，正如预期的那样，组蛋白修饰通常不会重叠（Fig.1b和扩展数据图2j）。这种现象在更高分辨率（200bp）下更容易观察到（扩展数据图2f），并且定量分析进一步支持了这种互斥模式。因此，跨细胞和修饰的数据产生了接近全基因组范围的CpG覆盖（约80%；扩展数据图2e）。这些分布也在K562细胞中高表达的PRAME基因位点上观察到（300kb；扩展数据图2j），该基因的转录区域显示出高水平的H3K36me3，而周围基因组则被抑制标记H3K27me3和H3K9me3修饰。从读取比对位置中提取MNase切割位点之间的距离。单细胞[热图](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2685207236771872770#wechat_redirect>)（Fig.1c）和按组蛋白标记聚合的数据（Fig.1d）揭示了与核小体间距相关的预期振荡模式。这些振荡在距离大于1kb时对于H3K36me3消失，而对于H3K27me3和H3K9me3则持续存在，这可能与转录过程中核小体动态的增加有关。

与[染色质](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522998&idx=1&sn=843d378d3b679951ad3c8e5da7c32d87&scene=21#wechat_redirect>)分析类似，作者还展示了2号染色体大区域的单细胞甲基化轨迹，观察到H3K36me3的甲基化水平较高，而H3K27me3和H3K9me3的甲基化水平较低（Fig.1d和扩展数据图3d）。以切割位点为中心绘制平均甲基化水平也显示，H3K27me3和H3K9me3的5mC水平（8% - 10%）远低于H3K36me3（50%）（Fig.1e，f）。这与经WGBS数据的分析（扩展数据图3a，d）一致，也与之前关于基因体中甲基化水平更高的报告相符。

![图片](../../images/fa2856bd85501eba.webp)

Fig.1

二：细胞周期依赖的DNA甲基化动态主要由DNA复制驱动

为了研究细胞周期进展过程中表观遗传标记之间的相互作用，作者利用了RPE - 1 hTERT细胞中的FUCCI细胞周期报告系统。在分选过程中，记录每个单细胞的FUCCI报告器的强度，可精准测定各细胞所处周期阶段，为了可视化细胞周期中CpG的动态变化，作者绘制了单细胞的平均CpG甲基化水平以及FUCCI标记的荧光强度（S/G2期标记mAG-Geminin为X轴，G1期标记Cdt1-mKO为Y轴；扩展数据图5d）。初步观察发现细胞周期中存在轻微波动，但异常细胞可能掩盖了真实模式。通过滚动窗口平滑处理，所有组蛋白修饰区域的CpG甲基化均在S期出现短暂下降（Fig.2a）。为了提高与基因组复制时间相关的[分辨率](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528207&idx=1&sn=13aafaa75639311cfd0940c34dc25dbe&scene=21#wechat_redirect>)，作者将单细胞Epi2 - seq数据与同一细胞系的单细胞EdU-seq数据（scEdU - seq）进行了整合（Fig.2b和方法）。通过这种整合，能够从两个时间分辨轴来评估CpG甲基化和组蛋白甲基化：从FUCCI报告器提取的细胞周期进展以及从scEdU - seq实验推断出的DNA复制时间（Fig.2c）。结果显示，组蛋白标记的基因组分布与复制时间密切相关。H3K36me3和H3K9me3分别富集于早期和晚期复制区域，而H3K27me3则广泛分布于中期复制时间域（Fig.2c）。且在晚期复制区域，无论是标记有H3K27me3还是H3K9me3的区域，维持性甲基化都延续到G1期（Fig.2c）。当两种模态沿着基因组可视化时，复制偶联的甲基化丢失与复制时间之间的关联也很明显（Fig.2d）。总的来说，作者的数据表明，观察到的细胞周期依赖的DNA甲基化动态主要是由DNA复制驱动的。

![图片](../../images/a472e6e75bd6e863.webp)

Fig.2

三：核小体占据直接影响DNA复制后的DNA甲基化维持

为了评估核小体占据与甲基化维持之间的相互作用，作者利用了scEpi2-seq数据的单分子特性，首先，评估了在整个细胞周期进程中，DNA甲基化与MNase切割位点距离的关系（Fig.3a）。作者观察到，S期（x轴）DNA甲基化的降低与距切割位点的距离（y轴）相关。之后选择三个代表性距离来探究DNA[甲基化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538223&idx=1&sn=2be2cf61a27b9a5def3b5f0bad4d152b&scene=21#wechat_redirect>)维持与核小体占据之间的相关性。90 bp和270 bp的距离分别对应于距切割位点第一个和第二个核小体的中点，而180 bp的距离则反映了连接DNA区域。进一步分析表明，在被核小体覆盖的区域，甲基化水平的降低更为显著，尤其是在H3K27me3和H3K9me3修饰区域（Fig.3b）。当研究绝对甲基化水平与切割位点距离的关系时，这种效应更加明显（Fig.3c）。作者观察到，在核小体缺失区域（180 bp，绿线），甲基化水平在整个细胞周期进程中波动较小，并且与被核小体覆盖的区域表现不同。这表明，基因组中被核小体结合的区域在DNA复制后表现出不同的DNA甲基化恢复动力学。这些动态在CpG甲基化标准化后也清晰可见（Fig.3d；每个染色质标记的CpG甲基化进行z-score标准化）。与这一观察结果一致，包裹在核小体上的DNA的CpG甲基化水平变化高达12%，而连接区域的甲基化水平变化仅为4%（Fig.3e）。此外，这些动态在H3K27me3和H3K9me3之间具有高度可重复性。对于H3K36me3，总体下降幅度要小得多，并且与核小体占据的相关性也不那么明显。表明RNA聚合酶II转录过程中组蛋白的高周转率使得DNA复制后CpG甲基化水平能够更快地恢复。总而言之，这些发现表明，除了复制时间之外，核小体占据率对DNA甲基化的维持也具有重要影响。

![图片](../../images/52d44f70fd9f6c81.webp)

Fig.3

四：对小鼠肠道细胞进行分析揭示了H3K27me3区域内细胞类型特异性的DNA甲基化差异

在探索相对均一的细胞中特定染色质区域的CpG甲基化后，作者开始评估scEpi2-seq在复杂组织中的功能。鉴于DNA去甲基化在肠道分化过程中的关键作用以及PRC2依赖性抑制在肠道干细胞维持中的作用。作者对从小鼠小肠中分离的单细胞进行了H3K27me3靶向scEpi2-seq测序，从三只小鼠的小肠近端、远端和中部区域分离细胞（Fig.4a）。经过质量控制后，保留3,123 个小鼠肠道细胞，分别使用 Signac32 和 MethSCAn33 对 H3K27me3 模式和 CpG 甲基化进行降维和聚类分析。作者在 H3K27me3 和 CpG 甲基化数据中都观察到几个簇，这些簇分布在近端和中部区域的细胞与远端区域的细胞之间（Fig.4b）。为了确定这些簇中的细胞类型，作者对 H3K27me3 信号进行了标记基因检测。结果揭示了三种细胞类型：吸收细胞（例如，Pou2f3、Tcf4、Ephb3、Foxa1 和 Foxa2）、分泌细胞（例如，Nptx1、Nkx2-2 和 Fev）和[免疫](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536091&idx=1&sn=9c5c8e70ee8855be14ef34489c364ba5&scene=21#wechat_redirect>)细胞（例如，Ikzf3、Pax5 和 Pou2f2）。吸收细胞和分泌细胞存在于所有前后轴区域，而免疫细胞则富集在远端区域（Fig.4b，c）。这与小肠远端淋巴滤泡（称为派尔集合淋巴结）数量增加的现象一致。

为了获得更高的细胞类型分辨率，作者对每个聚类（吸收细胞、分泌细胞和免疫细胞）分别再次进行了降维和聚类分析。作者发现吸收细胞聚类分为两个非常相似的肠上皮细胞亚群（Fig.4d）。利用这些细分的细胞类型，作者研究了H3K27me3和CpG甲基化水平（Fig.4e，f）。结果显示肠上皮细胞的H3K27me3水平最低，其CpG甲基化水平也最低。分泌细胞中杯状细胞的H3K27me3水平与EECs相似，但CpG甲基化水平更高。对于免疫细胞，发现B细胞的H3K27me3水平低于T细胞或髓系细胞，但其CpG甲基化水平最高。接下来，作者使用MethSCAn在小鼠肠道数据中识别了DMRs。这些数据表明，尽管H3K27me3在这些区域的修饰水平相似，但上皮细胞和造血细胞谱系之间的CpG甲基化水平却存在显著差异（Fig.4h-j）。

![图片](../../images/6e5dd2da362c0f5b.webp)

Fig.4

**三、总结讨论**

单细胞Epi2 - seq是一种新的单细胞多组学技术，能够同时检测单细胞中的DNA甲基化（5mC）和组蛋白修饰。该技术结合了sortChIC和TAPS转化，克服了亚硫酸氢盐处理的局限性，实现了高特异性和高分辨率的多组学测量。通过在RPE - 1 hTERT细胞和小鼠小肠组织中的应用，研究发现细胞周期依赖的DNA甲基化动态主要由DNA复制驱动，且维持性甲基化在晚期复制区域延续至G1期。此外，在小鼠小肠中，H3K27me3和5mC的联合分析揭示了不同细胞系之间的独特[表观遗传](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535047&idx=3&sn=fcdfbd0cb62e0cf05c6999b6d52e23bb&scene=21#wechat_redirect>)特征和分化轨迹，表明染色质状态可能影响细胞命运决定。

![图片](../../images/2b97050f06208e7a.webp)

**欢迎交流**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家一起讨论。![图片](../../images/e43581b4f5118aad.webp)![图片](../../images/4ccf87cacd1143af.gif)您点的每个赞和在看，我都认真当成了喜欢
