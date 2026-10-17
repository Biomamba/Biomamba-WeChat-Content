---
title: "5w单细胞在Monocle2拟时序中占据多少内存？"
date: 2025-03-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528216&idx=1&sn=a12e276a7dac4df56d24b5a92dd78a24&chksm=9b3c1648ac4b9f5e08379a1d5a5d8aa80f93373da2e6d057b219d732168707ac830002267c03#rd
albums: ["单细胞教程全收录"]
---

# 5w单细胞在Monocle2拟时序中占据多少内存？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528216&idx=1&sn=a12e276a7dac4df56d24b5a92dd78a24&chksm=9b3c1648ac4b9f5e08379a1d5a5d8aa80f93373da2e6d057b219d732168707ac830002267c03#rd
> 合集：单细胞教程全收录

一、写在前面![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn5RYeZyo5amnOAgOiaRia5pTmJkLwBXH0J3icajPObPVuj8C5TeYLc8fI9KZickXDnsa1EvhSibltJv7VQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

总有小伙伴购买服务器([足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526504&idx=2&sn=417d07347cebe0a1bd403f6c3e7d9b29&scene=21#wechat_redirect>))时不知道哪个版本的配置适合自己，这里我们对Monocle拟时序运行进行了内存和时间占用的压力测试。往期测试可见：[服务器压力测试](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3771935244480249861#wechat_redirect>)

简单从测试结果来看，目前monocle2最多能计算[4.5w，5w)细胞，占用内存峰值接近200GB。考虑到系统本身以及环境中的其它变量，推荐大家至少准备256GB内存为宜。若采取并行计算等操作，占据的内存数量会更多！

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZwp3Dtlm9DbNfoPZXPJiawHafChibEPRadsSLVQDTuafRlHhsDTIyDMag/640?wx_fmt=png&from=appmsg)

本教程基于Linux中的Rstudio环境（[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526504&idx=2&sn=417d07347cebe0a1bd403f6c3e7d9b29&scene=21#wechat_redirect>)）演示，计算资源不足的同学可参考：
[生信分析为什么要使用服务器？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491007&idx=1&sn=8619c2bad23791b3252a1c4cb1831931&chksm=9b3f64efac48edf9c02f84959aeee9b12480736fce70c5ddb8b41d79cfc22ce590ea2cb60fba&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[配置一个心仪的工作站(硬件+环境配置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519707&idx=1&sn=73dcab26f9b2ed75a954327317d07112&chksm=9b3cf48bac4b7d9df5b5a432fbe70d4f9c13bc8d739aa401732614f022223d1912642a7e4bea&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)
[
](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

更多内容可咨询客服微信[**Biomamba_yunying**]

[
](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)

**二、测试过程**![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn5RYeZyo5amnOAgOiaRia5pTmJkLwBXH0J3icajPObPVuj8C5TeYLc8fI9KZickXDnsa1EvhSibltJv7VQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

1、准备工作

本期测试的数据来源于数据集GSE139107。前期的数据处理可以参考我们之前推送的DimPlot优化内容[改造单细胞降维图|1.DimPlot的探索](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496162&idx=1&sn=598c2920f7cc0697ee5a1fa6cadaee04&scene=21#wechat_redirect>)

  *   *   *   *   *   *

```r
library(Seurat)library(monocle)library(peakRAM)setwd("/home/cwj/project/11_monocle/")obj <- readRDS("./iri.intergrate.rds")obj
```
```
## An object of class Seurat
## 29133 features across 126578 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_8w <- subset(obj,downsample=4500) obj_8w
```
```
## An object of class Seurat
## 29133 features across 78295 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_6w <- subset(obj,downsample=3000) obj_6w
```
```
## An object of class Seurat
## 29133 features across 58646 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_5w <- subset(obj,downsample=2500) obj_5w
```
```
## An object of class Seurat
## 29133 features across 50223 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_4w <- subset(obj,downsample=1900)obj_4w
```

```
## An object of class Seurat
## 29133 features across 39944 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_3w <- subset(obj,downsample=1400)obj_3w
```
```
## An object of class Seurat
## 29133 features across 30662 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_2w <- subset(obj,downsample=900)obj_2w
```
```
## An object of class Seurat
## 29133 features across 20895 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

  *   *

```r
obj_1w <-  subset(obj,downsample=400)obj_1w
```
```
## An object of class Seurat
## 29133 features across 10152 samples within 2 assays
## Active assay: RNA (27133 features, 0 variable features)
##  2 layers present: counts, data
##  1 other assay present: integrated
##  3 dimensional reductions calculated: pca, umap, tsne
```

2、时间和内存测试

monocle是单细胞轨迹分析中常用的软件之一，往期推送中我们也详细的介绍过monocle的使用教程[拟时序分析| 3.monocle2实操：完整版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497730&idx=2&sn=930dc0e276219d70c937e943119388ff&chksm=9b3c8152ac4b08446d457cef3ede4a4a17c0ebacaec0c36efe7d7c8706fb4a3d62222d702ee5&scene=21&cur_album_id=2820794880947159043#wechat_redirect>)。同时对于monocle常见报错也进行了在线答疑[解决monocle2的orderCells报错的两种方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&token=333450324&lang=zh_CN&scene=21#wechat_redirect>)。大家可以先跟随我们的往期教程熟悉一下monocle完整的运行流程。接下来我们正式进入到monocle的时间和内存测试内容。

运行代码：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
for ( obj in c(obj_1w,obj_2w,obj_3w,obj_4w,obj_5w,obj_6w,obj_8w)){  # print(obj)  print(    peakRAM({      # 创建celldateset对象      counts <- GetAssayData(obj, layer = "counts")      gene_metadata <- data.frame(gene_short_name = rownames(counts))      rownames(gene_metadata) <- rownames(counts)      pd <- new("AnnotatedDataFrame", data = obj@meta.data)      fd <- new("AnnotatedDataFrame", data = gene_metadata)      cds <- newCellDataSet(counts, phenoData = pd, featureData = fd)      # 评估size factor和离散度      cds <- estimateSizeFactors(cds)      cds <- estimateDispersions(cds)      # 统计每个基因在多少个细胞中表达      cds <- detectGenes(cds, min_expr = 0.1)  #增加了num_cells_expressed,num_genes_expressed列      # 选择定义细胞轨迹进展的基因，这里使用monocle计算得到的高变基因      disp_table <- dispersionTable(cds)      # 选择用于聚类的基因      disp.genes <- subset(disp_table, mean_expression >= 0.1, dispersion_empirical >= 1 * dispersion_fit)$gene_id      cds <- setOrderingFilter(cds, disp.genes[1:2000]) #增加use_for_ordering列      plot_ordering_genes(cds)      # 降维      cds <- reduceDimension(cds, max_components = 2, reduction_method = 'DDRTree')      cds <- orderCells(cds)      plot_cell_trajectory(cds, color_by = "Pseudotime")     })  )}
```

结果：

细胞数为1万时的时间和内存消耗：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZFQX6rzK2MWRyJqxpqvdc7wnMQdMrS0CtlVhh81ZcGbmGKynMTlvISQ/640?wx_fmt=jpeg&from=appmsg)

细胞数为2万时的时间和内存消耗：![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZiaEp8icvrIM0mTNiar18NCs5pYNSS4WqH05R94KI1wzRmInvLLeQStcWw/640?wx_fmt=jpeg&from=appmsg)细胞数为3万时的时间和内存消耗：![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZesKL7fYl8ia2mZd3IIbTBhwd8LHbv12uFPibia0E6Nu0pc4m2NrQK5TFg/640?wx_fmt=jpeg&from=appmsg)

细胞数为4万时的时间和内存消耗：
![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZI4Qf5Qeia7TibKdKDeeziau8HicrIQlmzVdp9QeI4obLfs1asFjBJqdGRg/640?wx_fmt=jpeg&from=appmsg)细胞数为4万时的时间和内存消耗：![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZstdRYlibQqtxscBOvcplFCvQ6Mb0MlwicF14kjrx9c8l0Sh9qTKubZZg/640?wx_fmt=jpeg&from=appmsg)
**三、遇到点小问题**![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn5RYeZyo5amnOAgOiaRia5pTmJkLwBXH0J3icajPObPVuj8C5TeYLc8fI9KZickXDnsa1EvhSibltJv7VQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) 上文可以看到我们只展示了细胞数为1w、2w、3w、4w和4.5w时候的时间和内存结果，那么其他的测试结果为什么没有展示出来呢？这是因为我们在测试过程中遇到了以下的一些问题，导致细胞数达到某些数量级的时候是无法利用monocle来进行轨迹推断的。以下是我们遇到的问题展示和部分解决方法，大家可以做个参考。问题1

  *   *   *   *

```
# 报错出现的提示`nei()` was deprecated in igraph 2.1.0 and is now defunct；# 解决方法：修改源码trace("project2MST",edit = T, where = asNamespace("monocle")) 后 修改nei()为.nei()
```

问题2

  *   *   *   *

```r
# 报错出现的提示：Error in if (class(projection) != "matrix") projection <- as.matrix(projection) # 解决方法：修改源码trace("project2MST",edit = T, where = asNamespace("monocle")) 删除 “ if (class(projection) != "matrix") ”这部分的代码
```

问题3

  *   *   *   *   *   *   *   *

```
# 报错出现的提示：orderCells(cds)：Error in sequence.default(n..1, from = seq.int(s.1, length(df), s.1),:'from' contains NAs "# 出现场景：# 这个问题会出现在>= 5w细胞的时候，提示矩阵中包含有NA，但是检查后发现矩阵中无NA # ！！！github上面有人同样遇到这个问题无法解决 https://github.com/cole-trapnell-lab/monocle-release/issues/518。# 第一种方法尝试解决：# 检查是否存在NA值# 确实结果中不存在NA
```

  *   *   *   *   *

```r
for ( obj in c(obj_1w,obj_2w,obj_3w,obj_4w,obj_5w,obj_6w,obj_8w)){  counts <- GetAssayData(obj, layer = "counts")  print(sum(is.na(counts)))  print(sum(is.na(obj@meta.data)))}
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZtuxAHzic3xAqS3xJ7PMYvthuzZ82oQy3Im2xZRbuKcTGLaWTlzFVEQQ/640?wx_fmt=jpeg&from=appmsg)问题4

  *   *   *   *

```
# 报错出现的提示：estimateDispersions(cds) ：Error in h(simpleError(msg, call)) :   error in evaluating the argument 'x' in selecting a method for function 'print': error in evaluating the argument 'x' in selecting a method for function 'rowMeans': unable to aggregate TsparseMatrix with 'i' and 'j' slots of length exceeding 2^31-1# 出现场景：10w 及以上的细胞会提示矩阵过大而无法继续运算
```

**
****四、总结数据**![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn5RYeZyo5amnOAgOiaRia5pTmJkLwBXH0J3icajPObPVuj8C5TeYLc8fI9KZickXDnsa1EvhSibltJv7VQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
sum <- data.frame(matrix(NA, nrow = 5, ncol = 2))colnames(sum) <- c("time","peak_mem")row.names(sum) <- c("1w","2w","3w","4w","4.5w")sum["1w",] <- c(9,18979)sum["2w",] <- c(28,59923)sum["3w",] <- c(55,106038)sum["4w",] <- c(90,129860)sum["4.5w",] <- c(116,167045)sum$Category <- rownames(sum)sum$Category <- factor(sum$Category, levels=sum$Category)ggplot(sum, aes(x = Category , y = time, fill= Category)) + geom_bar(stat = "identity")+labs(x = "Category", y = "Time(min)", title = "Monocle Time Compare") +  theme_minimal() +   theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 12),        axis.text.y = element_text(size = 12),         axis.title = element_text(size = 14, face = "bold"),         plot.title = element_text(size = 16, face = "bold", hjust = 0.5),        legend.title = element_text(size = 12, face = "bold"),        legend.text = element_text(size = 10))
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZXYnCWZ1y3cSJXgWsofpUutdDLr4Z8ju1kFicXfH7DINomclzVPYsib5A/640?wx_fmt=png&from=appmsg)

  *   *   *   *   *   *   *   *   *

```
ggplot(sum, aes(x = Category, y = peak_mem, fill= Category)) + geom_bar(stat = "identity")+labs(x = "Category", y = "peak_mem(MB)", title = "Monocle Peak Mem Compare") +  theme_minimal() +   theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 12),         axis.text.y = element_text(size = 12),         axis.title = element_text(size = 14, face = "bold"),        plot.title = element_text(size = 16, face = "bold", hjust = 0.5),        legend.title = element_text(size = 12, face = "bold"),        legend.text = element_text(size = 10))
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpz1ibfuzV67bSCvhLN1QELbZ5A4u3brdD1PAiaO8Kia97YtBbNVnRM53Ol7nal8tNjfHezlq23J0l2BQ/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取资料、[免费两周学习版上](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号** ，方便各位随时交流（别问在么，添加时直接说来意）。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyZBGOXDqRYHpgiczxr9PX8gliblp8giaPGsr7w6IeoU6lExTAeEjx48Ke4LEJQfbdiarzXwUGvoRFvyA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢**
**
