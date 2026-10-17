---
title: "别痛苦了，scATAC已经能零代码分析啦"
date: 2025-06-18
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529409&idx=1&sn=6323b50872b8eebf67c995277e9e97a0&chksm=9b3c0a91ac4b83870688a3ee21d4aba245ca8825ebed8cf111fca375084cd2d3505c35e1d45b#rd
albums: ["单细胞云平台"]
---

# 别痛苦了，scATAC已经能零代码分析啦

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529409&idx=1&sn=6323b50872b8eebf67c995277e9e97a0&chksm=9b3c0a91ac4b83870688a3ee21d4aba245ca8825ebed8cf111fca375084cd2d3505c35e1d45b#rd
> 合集：单细胞云平台

**写在前面**

单细胞表观遗传及其它多模态已然成为scRNA的新趋势，我们也一致致力于给大家分享代码注释丰富、测试文件齐全的教程。此前我们分享了[4.6w字长文| SeekOne®-DD单细胞ATAC+RNA一胞双组学-学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528858&idx=1&sn=0620dd3681e73858eb47256d785d7437&scene=21#wechat_redirect>)。有同学表示学起来压力山大，想要一款能够界面化、适合零代码基础小白的一款软件。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxJ9mialIB0K4kCz3PGzSMv5n6YuQxcXgBKLiagm92c3RnV4oqUdb4jic8vV8vEaowfuEteo3rthMMicg/640?wx_fmt=png&from=appmsg)

当然是有的啦，云平台已经悄咪咪更新了很多新功能供大家选择下文我们也将演示scATAC的零代码基础分析流程：

软件包/云平台包名称| 云平台更新内容| 功能分类| 作用
---|---|---|---
signac| 细胞类型uMAP/tSNE降维图（ATAC、RNA、ATAC+RNA 三种降维结果）| 降维聚类| 将高维的单细胞 ATAC 和 RNA 数据投影到二维空间，直观展示细胞间的相似性与异质性，识别细胞亚群结构。
signac| 样本uMAP/tSNE降维图（ATAC、RNA、ATAC+RNA 三种降维结果）| 降维聚类| 通过整合多组学特征，揭示不同样本间的细胞组成差异。
signac+寻因AI| SingleR+AI注释| 细胞注释| 基于已知标记基因库和 AI 算法，自动识别单细胞类型（如 T 细胞、巨噬细胞），提高注释准确性与效率。
signac| peak鉴定| 可视化| 识别染色质开放区域（peak），并在基因组上定位，辅助调控元件发现与可视化。
GeneActivity| 基因活性分析|
| 通过 peak 与基因启动子 / 增强子的关联性，推断基因表达调控活性，弥补 ATAC 数据与 RNA 表达的直接关联缺口。
ATAC_diffEnrich| 差异peak分析| 差异分析| 比较不同细胞群体间染色质开放区域的差异，发现潜在的细胞特异性调控元件。
ATAC_diffEnrich| peak富集分析| 富集分析| 对差异 peak 进行功能注释（如 GO/KEGG 通路），解析调控元件参与的生物学过程。
ATAC_diffEnrich| 差异motif分析| motif分析| 识别差异 peak 中的转录因子结合基序（motif），预测潜在的上游调控因子。
ATAC_Peak2Gene| Peak2GeneLink关联分析| peak gene联合分析| 整合 ATAC 的 peak 数据与 RNA 表达，建立非编码调控元件（如增强子）与靶基因的功能性联系，解析基因表达调控网络。
ataCNV、epiAneufinder、CopyscAT| ATAC 数据CNV分析| 肿瘤细胞分析| 通过 ATAC-seq 数据中染色质可及性的拷贝数变异（CNV），识别肿瘤细胞克隆及其演化关系，辅助肿瘤异质性研究。

云平台现开放用户自行上传数据一键分析，5例/季度免费分析联系客服微信[Biomamba_yunying]开通权限。

云平台地址：

https://seeksoul.online/t_static/Biomamba/Biomamba.html

使用教程可见：

[一文学会零代码单细胞分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511007&idx=1&sn=e7be3d9775890e5717889714629cfaf5&chksm=9b3cd28fac4b5b9936428d5f74d8b581b5cddc18d0fc42e2a5d75604cce080588d50f1304a17&scene=21#wechat_redirect>)

[零代码单细胞视频教程](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_2095d655e3b&enterid=1715838775&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1#wechat_redirect>)

注，为了保证界面演示的完整性，图中的文字可能有些小，请点击拉大观看哦~

**一、激活流程**

在"我的项目"中大家可以看到一个名为"SeekARCDemoProject"的项目。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YJmKYO2JqCyZxT5b30xGw7wZ1zRkKHzUe4icTZpvMWZ0S8nsnPWIA9TQ/640?wx_fmt=png&from=appmsg)
启动激活流程，当状态栏变成绿色的"在线"时，就可以点击操作中的"查看"，进入下一步啦~![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YMS73vQ6GS5bNBDhmBEXUL9WFB6m01VYOYe28xD2iaEJPbapIDmyDNXg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YFfoM3KQlNqof9R5peuqLbUia8cgibgUMNBq3KkWfOscn0ia7wZdrITsXA/640?wx_fmt=png&from=appmsg)

**二、查看数据并质控过滤**

查看项目进入的首先就是质控页面![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YqEbCp6BNl1n8u1C0lKNXqkkYht9Clm2OoW28JicCy5FFqafGkuCwksg/640?wx_fmt=png&from=appmsg)
这是推荐的过滤参数：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YUoSd7ZF3nPTPzXTn7xHEkkktN8JDJ3Q7nbd9RIofGsRV4yOzicQJJXA/640?wx_fmt=png&from=appmsg)
点击过滤后系统会自动给出过滤前后的数据对比：![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YJTPiaA9icCxXyjwy13bBSLOHAFzqVoJmcicfdHcU3IngwO5XQVsictAIkQ/640?wx_fmt=jpeg&from=appmsg)

**三、多样本整合**

多样本的整合，我们同样给出了模板参数：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YkLDXbOZGvJqwlprjtu0zLolAibg7jTcZsia9ribD4o7RHfUVCGtfFZl8Q/640?wx_fmt=png&from=appmsg)
可以看出Harmony整合后样本基本不存在批次效应：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YW0dofKSTWyaA2libvxxMXHiaicENglzhEhCia1Jaicxicm28n7RIsNx29IHA/640?wx_fmt=png&from=appmsg)

**四、聚类分群**

默认聚类参数：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YRWhUyyk0q8ibicAtsl5PSUjsgAlYOT4ib8ZMz0PB2BLdicgxworlBNdgUA/640?wx_fmt=png&from=appmsg)
这里分别使用ATAC矩阵、WNN、RNA矩阵进行了降维分群(加权最近邻算法（Weighted Nearest Neighbor，WNN） 是 Seurat 中用于数据整合的核心方法之一，尤其适用于整合异质性较大的数据或多组学数据。WNN通过共享特征（如基因调控关系）建立跨模态的联系，使其与 scRNA-seq 的基因表达量形成对应，从而完成跨模态的降维分群。下文将以RNA矩阵的分群结果进行后续演示。

在分辨率为0.5，dims选择1:30的参数下，共获得0~11这12种cluster![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099Y5FVJ68y5tfQRWjU1xu1Qox2yMRN4nwV7loFiasAXPmPia2J2VeicpNayA/640?wx_fmt=png&from=appmsg)
到这里基础分析流程就完结啦，可以点击画布右上方的"汇总"即可把当前分析流程的结果整合到结果总览中，最终可以通过网页报告的形式查看所有的分析结果：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099Yun5mpmHbqpibRBVTxHsvyxIS2hLHgGzulHeR9icrgjKWjicUO6dH6HJiag/640?wx_fmt=png&from=appmsg)

**五、细胞注释**

细胞注释页面会给出对应分群策略下的降维图、气泡图、小提琴图、热图、细胞比例柱状图等信息，帮助你完成细胞类型的注释![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YnWkvlb8AeDbbVXYlrlQ0ksHb7RCYWjP9NGEwWUOjatz9I6ppt3Q5LA/640?wx_fmt=png&from=appmsg)
可视化内容展示：![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpwZ3Knayk7oxp5GkEup099Y9Jc94dOHegrz4MLzmJcamaq1v1EmmibS3OPFDficyWI4dFRk5P7xOtyw/640?wx_fmt=gif&from=appmsg)
给大家展示一个新功能，利用系统输出的marker结合singleR和AI，能够一键注释细胞类型。![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YkXwib2LPV9TWgkhIC2h0LEYrS4fttPBTQa4FKicCk1Mwk17Lzp7cQdsA/640?wx_fmt=gif&from=appmsg)
保存后的新注释在这里，我们以CellAnnotation注释进行后续分析：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YARX9lJsA7RAPjibndyCuF09yuFm5JK8fIPcXzXMTJKs8VSMezwfic9iaA/640?wx_fmt=png&from=appmsg)

**六、图片美化**

Seeksoulonline提供了发表级的画图工具，可以一站式完成小提琴图、降维图、FeaturePlot、DotPlot、分组统计图、热图的绘制与美化。比我们此前分享的[单细胞图片改造计划](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2707677276481814529#wechat_redirect>)可简单多了。大家可以看这个视频进行学习：[零代码分析单细胞测序数据| 图片美化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522176&idx=2&sn=11cc2a6687fb139508644504bbc2f374&scene=21#wechat_redirect>)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YibxCbfFUUt9gKPUhPbsWUn0aPNiclCfh1iaNCsxible3G5BW3iaricNtRYDA/640?wx_fmt=png&from=appmsg)

**七、基因集评分**

特征集分析也可以一站式完成，主要完成[单细胞基因集评分](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497831&idx=2&sn=82fa51c76a381fba0b444e9b6b23eb5f&scene=21#wechat_redirect>)工作。Seeksoul Online中内置了几百种特征基因集：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YCJCliam5PgDphapHUkVKicoyOJ0icy3xPQvFW5UBYozYkNU5oINgwC2DQ/640?wx_fmt=png&from=appmsg)
随便选一个基因集进行提交：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099Y2biaiamTOtQibGK5eOzWh3qcwmgubiajQNC5Z3uhPDCg2nzyefU8uKnEKQ/640?wx_fmt=png&from=appmsg)
秒出结果：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YOOfs8g8B3dWxTLE13vI8IIXovGh9RibMLibhDX3sZxvvlqKPLZYvkqOw/640?wx_fmt=png&from=appmsg)

**八、差异与富集分析**

[零代码单细胞| 差异分析与富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510401&idx=5&sn=8cde5a0101cdf1da4a24e614b05cedfa&scene=21#wechat_redirect>)也可以一站式完成![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099Y0IrdvISlsBL6Q2fdLdj7CicDDpw6gaLkVhgj2Z4mJr2ziaOqicic2h7eBg/640?wx_fmt=png&from=appmsg)可以按照如下演示创建你需要的差异分析![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YicpF7DN75FBQibtmKFXDN7UQABzqYvbIZIt4vicGgcU6VbY5Y6BxMsTtQ/640?wx_fmt=gif&from=appmsg)

**九、亚群分析**

通过提交细胞注释类别(参数)、具体需要亚群分析的细胞类群(值)。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YJ0uAJbE52DUviaZOicFNccJqR1VTaHzj2sUePj7wDnZwofiaWcppW1vOQ/640?wx_fmt=png&from=appmsg)完成后点击进入这个加号即可进入与大群一样的预处理流程：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YhwZpkfR1icNyy0crPS5k1HLoTo7mKpDKdgsV4G2VGKibsibSyvfqEtBgw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YKlqme7FLswpGIZcC6pntLubTQWo3EkuRLMNUJNU9pzgDQrxlLBL72A/640?wx_fmt=png&from=appmsg)

**十、高级分析**

高级分析现SeeksoulOnline已经内置了几十种高级分析，包含monocle3、cellphonedb、infercnv、scenic、monocle2、DiffEnrich、CytoTRACE、CellChat、scMetabolism、copyKAT、GSVA、Nichenet、scVelo、scoring、group_diffenrich、Augur、hdWGCNA、GeneActivity、ATAC_Peak2Gene共19种高级分析，大家可以逐个试一试，我们后面再出一篇推送来演示这些内容~![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YOu0VeBsLjb1qZ8RkkSxdVCLzNZtw8ibDeib6Jg3BgKswWfUv5El3gfqw/640?wx_fmt=png&from=appmsg)
还有炫酷的交互式分析，绝对值得大家好好探索一番：![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YgxVq6tgNgbIlVveH8NFjrAmJVJumxtGl9DibPd4SqA3IGmxaQhibkYuA/640?wx_fmt=gif&from=appmsg)

**十一、辅助信息与结题报告**

辅助信息上半部分页面包含了各分析流程用到工具的名称、版本、分析内容、参考链接，下半部分页面包含了注释信息。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YGPUCIgYZw1tFROPia7AMicIvawzYoCt9lmxNTJad3iabaM2SPyTYAAtCw/640?wx_fmt=png&from=appmsg)
结果总览中包含了活页的结题报告：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YDUWhX7XzDPoFGFYj5rGkMlJW91mfC2w3kCsKGJB0HAw83eMsGyzr4w/640?wx_fmt=png&from=appmsg)

感兴趣的同学可以看看我们此次操作的报告：报告目录：

  *   *   *   *   *   *   *   *   *   *   *   *

```
./└── report    ├── dist    │   └── src    │       ├── assets    │       ├── css    │       ├── file    │       ├── graph    │       ├── img    │       └── js    ├── report.html    └── report.pdf
```

报告的html文件是可交互的哦：![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpwZ3Knayk7oxp5GkEup099YRC9WDqY8j4KJnicIRvOvwGzbU82Rl7icziaXwy9cia1dkb8c5qPwHOAKCw/640?wx_fmt=gif&from=appmsg)

下载链接：

通过网盘分享的文件：SeekARCDemoProject_SeekARCDemoProcess_云分析标准报告

链接: https://pan.baidu.com/s/1VvBMqRX7Muh5qZMbP4j_qw?pwd=bfg8

提取码: bfg8

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwZ3Knayk7oxp5GkEup099Y5tLt1EP4uTl0OQlann6xw5rzzJUdxPXtHPyZ0HnLzsgaPQK5BXib29g/640?wx_fmt=jpeg)

**视频教程**

本系列视频我们将进行拆解动作，完整视频教程可见合集：

[SeekSoul® Online单细](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_1006a9b5456&enterid=1729128003&from_msgid=2247522176&from_itemidx=2&count=3&nolastread=1#wechat_redirect>)

[胞云平台](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_1006a9b5456&enterid=1729128003&from_msgid=2247522176&from_itemidx=2&count=3&nolastread=1#wechat_redirect>)

总是有小伙伴在学我们的单细胞**代码** 教程(**[两百篇单细胞知识帖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522475&idx=1&sn=84dd9a65348528be9aa2b8d2711d776c&scene=21#wechat_redirect>)**)时深感头疼，密密麻麻的代码、繁琐的流程、巨大的数据量，这些都是劝退大家的门槛。这对这一现象，**Biomamba** 联合**寻因生物** 发布了科研利器——**[SeekSoul Online单细胞云平台](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_69f8cb7b2da&enterid=1713928791&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1&token=1053256417&lang=zh_CN#wechat_redirect>)** 及对应的**《[ 2周教你学会单细胞生信全套分析](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_69f8cb7b2da&enterid=1713928791&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1&token=1053256417&lang=zh_CN#wechat_redirect>)》**课程，准备好**零代码** 发单细胞文章吧！

云平台访问链接：https://seeksoul.online/t_static/Biomamba/Biomamba.html

往期云平台使用视频教程可参考：[单细胞云平台教程全收录](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_69f8cb7b2da&enterid=1713928791&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1#wechat_redirect>)

体验反馈问卷链接：https://www.wjx.cn/vm/QIX0xRI.aspx#

各位同学需要**联系您的专属在线客服，获取demo数据后，进行操作学习。**

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzlCHzM8BicyYndroTyAQWjdHD5ZO0DJHw7ff3XHNoiaCNmD4eMp5j1yX70aqtS0Y0mFxE32WrlrdCw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcysqPg5ZJ3sWZ54d3okyxzNK7sicraXvicUxWeic24H8udwKpeYHncdJYoLJgt7Xm11TVY3NH4E9JQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
