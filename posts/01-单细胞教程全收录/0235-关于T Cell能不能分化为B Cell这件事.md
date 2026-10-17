---
title: "关于T Cell能不能分化为B Cell这件事"
date: 2025-07-13
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529864&idx=1&sn=825c0c6d9e29c224dc46e97f3c6d7f47&chksm=9b3c0cd8ac4b85ce3a0def6ace951bb94cc3d070e4b2745e056435d8299e09278fc8199fc96d#rd
albums: ["单细胞教程全收录"]
---

# 关于T Cell能不能分化为B Cell这件事

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529864&idx=1&sn=825c0c6d9e29c224dc46e97f3c6d7f47&chksm=9b3c0cd8ac4b85ce3a0def6ace951bb94cc3d070e4b2745e056435d8299e09278fc8199fc96d#rd
> 合集：单细胞教程全收录

一、不要神话拟时序分析

我们在分享[轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)时，总有同学问：我的分析结果中XX细胞和XX细胞的拟时间顺序不对/反了，寻求解决办法。其实这个问题很好理解，[《拟时序分析》概论](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&scene=21#wechat_redirect>)时我们其实解释过，通俗点说算法根本不知道谁前谁后，它只知道把表达相似的细胞排排坐。所以不要过度神话拟时序的分析结果，拟时间与实际生物学现象并不一定完全相关。甚至我也可以把T Cell和B Cell的拟时间手搓成连续的，但显然我并不能说T Cell分化成了B Cell：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 设置工作目录library(monocle)# seurat对象转换为cds对象方法sce.obj<- readRDS('data/sce.obj.rds')sce.obj <- subset(sce.obj,idents = c('Naive CD4 T' , 'Memory CD4 T', 'B' ,'CD8 T'))# 准备细胞*基因表达矩阵data <- GetAssayData(sce.obj, slot = "counts")
# 准备phenoData，描述细胞的各种元属性，相当于seurat_obj@meta.data，行-细胞，列-属性  pd <- new('AnnotatedDataFrame', data = sce.obj@meta.data)# 准备featureData，基因名，行-基因名fData <- data.frame(gene_short_name = row.names(data),                     row.names = row.names(data))fd <- new('AnnotatedDataFrame', data = fData)# 创建monocle2的celldataset(缩写为cds)对象mycds <- newCellDataSet(data,                        phenoData = pd,                        featureData = fd,                        expressionFamily = negbinomial.size())
mycds <- estimateSizeFactors(mycds)mycds <- estimateDispersions(mycds)
# 质控(可选) 去除死细胞、空液滴、碎细胞液滴、双液滴，提高计算准确度、降低运算时间mycds <- detectGenes(mycds, min_expr = 0.1)
mycds_expressed_genes <- row.names(subset(Biobase::fData(mycds),                                          num_cells_expressed >= 10))mycds <- mycds[mycds_expressed_genes,]disp_table <- dispersionTable(mycds)unsup_clustering_genes <- subset(disp_table, mean_expression >= 0.1)#展示轨迹图的方法plot_cell_trajectory(mycds, color_by = "celltype",size = 3)|  plot_cell_trajectory(mycds, color_by = "Pseudotime")#来看看拟时间吧
```

这样看来B Cell与T Cell的几种亚群就展示出了相互演化的拟时序关系，显然我们并不能说B Cell与T Cell能够相互转化。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpziaDLJV1CBklPMTI9MrJlDmmNQziaGqal2eSxUkuIiazujYYb6BkeSiaml0P3GOkzKbX2OQ9Rad77fkw/640?wx_fmt=png&from=appmsg)

二、说的正规点

说的正规点这种情况由以下原因造成：

1\. 细胞状态定义不准确

Monocle通过识别基因表达变化的连续性来构建轨迹，但其初始状态（root node）需手动指定([monocle3的拟时序分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&scene=21#wechat_redirect>)支持)。若选择的 root 细胞实际属于终末状态，则会导致拟时间方向颠倒。若将分化终点的细胞错误指定为起点，后续细胞的拟时间将呈现 “反向” 分化。

2\. 基因选择偏差

Monocle 依赖差异表达基因（DEGs）来推断轨迹。若选择的基因集偏向于特定方向（如终末分化标记），算法可能误判轨迹方向。

3\. 分支结构复杂

在存在多分支的分化轨迹中，Monocle 可能将某个分支的方向误判为主轴方向，导致部分细胞拟时间反转。

4\. 批次效应或技术噪声

未校正的批次效应可能干扰细胞间的相似性计算，使算法误判细胞的先后顺序。

5\. 算法参数不匹配

Monocle的DDRTree降维算法对参数敏感，如关键参数设置不当可能导致轨迹扭曲。

三、如何正确的矫正拟时序

1\. 正确的定义初始/终止的root

使用已知的早期/晚期标记基因（如干细胞标志物）筛选 root 细胞类群。

2\. 优化特征基因选择

在确定参与计算的基因集时不要简单的选择高变基因，可选择部分已知参与该样本演化的细胞类群

3\. 批次效应校正

使用limma或scran等进行批次校正，当然，最好你的实验设计时就避免批次效应产生。

4\. 考虑替代算法/工具

若Monocle持续出现方向性问题，可尝试其他轨迹推断工具：[一文学会四种scRNA-seq轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)

四、更多教程

如果你觉得当前教程有用，不妨看看：[生信基地122篇单细胞教程全索引](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528470&idx=1&sn=7f3ced59b2b97bed1ac9df560b11ddd6&scene=21#wechat_redirect>)[scRNA-seq，从小白到文献复现大神！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528482&idx=1&sn=7cc0715eace4f592a62bdaf157b25c01&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
