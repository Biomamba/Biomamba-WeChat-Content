---
title: "单细胞基因集评分之AUCell"
date: 2022-09-01
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&chksm=9b3c99e1ac4b10f7ca158561e96fec76a49ff32b8412cb146ed3fb7aa9260c75172b4eb16f9a#rd
albums: ["单细胞教程全收录"]
---

# 单细胞基因集评分之AUCell

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&chksm=9b3c99e1ac4b10f7ca158561e96fec76a49ff32b8412cb146ed3fb7aa9260c75172b4eb16f9a#rd
> 合集：单细胞教程全收录

# **一、写在前面：**

![](../../images/90fab1387787746b.gif)

此前已经给大家简单介绍过了五种单细胞基因集打分方法，包含`AddModuleScore`、`ssGSEA`、`GSVA`、`PercentageFeatureSet`、`AUCell`：[**一文搞定单细胞基因集评分**](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490658&idx=1&sn=3460a09ef4ad2916aabfaa13e195c7b1&chksm=9b3f6532ac48ec249e974aa5bfcca2f5d441e64bbd353fe9dd45a50b47599663bf0334def7d4&scene=21#wechat_redirect>)。但最近在做SCENIC(用于单细胞转录因子调控网络预测)的教程，其中用到了AUCell这一R包/算法来计算**regulon** 的活性，本以为AUCell是其他的哪位大佬开发的，没想到是作者在设计SCENIC时顺手写的基因集打分方法，看来硬生信和软生信之间的鸿沟是真实存在的，AUCell值得我们用单独的版面来介绍。

考虑节省时间我们先将**图文** 教程更新出来，不知诸位是否需要**视频** 教程（真的还蛮花时间的），老规矩，上票:

# **
**

# **二、教程：**

![](../../images/90fab1387787746b.gif) 1.0 AUCell简介AUCell可以在单细胞测序数据种鉴定/识别激活的基因集，主要实现方式是通过曲线下面积(Area Under the Curve, AUC)去计算每个细胞中是否存在富集的关键基因集(signature)。输出的**AUC scores** 类似于GSVA score，可以用于反应**signature** 的相对表达量。值得一提的是，由于GSVA score的计算方式基于排序和AUC，因此计算过程并不受基因表达量的**单位** 以及**normalization** 的影响；并且AUC scores是以**每一个细胞为单位** 进行计算的，因此处理大数据内存吃紧时，对每个子集计算AUC score再合并也无妨。

## 2.0. 分析前准备

### 2.0.1 版本信息

大家软件装不上时第一件事就应该检查环境的版本信息：
```
sessionInfo()
```

```
R version 4.2.1 (2022-06-23 ucrt)Platform: x86_64-w64-mingw32/x64 (64-bit)Running under: Windows 10 x64 (build 19044)Matrix products: defaultlocale:[1] LC_COLLATE=Chinese (Simplified)_China.utf8 [2] LC_CTYPE=Chinese (Simplified)_China.utf8   [3] LC_MONETARY=Chinese (Simplified)_China.utf8[4] LC_NUMERIC=C                               [5] LC_TIME=Chinese (Simplified)_China.utf8    attached base packages:[1] stats4    stats     graphics  grDevices utils     datasets  methods   base     other attached packages: [1] rbokeh_0.5.2         shiny_1.7.2          RColorBrewer_1.1-3   [4] NMF_0.24.0           cluster_2.1.3        rngtools_1.5.2       [7] pkgmaker_0.32.2      registry_0.5-1       DT_0.24             [10] Rtsne_0.16           dplyr_1.0.9          BiocParallel_1.30.3 [13] GSEABase_1.58.0      graph_1.74.0         annotate_1.74.0     [16] XML_3.99-0.10        AnnotationDbi_1.58.0 IRanges_2.30.0      [19] S4Vectors_0.34.0     Biobase_2.56.0       BiocGenerics_0.42.0 [22] AUCell_1.18.1        Matrix_1.4-1         data.table_1.14.2   loaded via a namespace (and not attached):  [1] plyr_1.8.7                  lazyeval_0.2.2               [3] splines_4.2.1               crosstalk_1.2.0              [5] GenomeInfoDb_1.32.3         ggplot2_3.3.6                [7] gridBase_0.4-7              pryr_0.1.5                   [9] digest_0.6.29               foreach_1.5.2               [11] htmltools_0.5.3             fansi_1.0.3                 [13] magrittr_2.0.3              memoise_2.0.1               [15] doParallel_1.0.17           mixtools_1.2.0              [17] tzdb_0.3.0                  limma_3.52.2                [19] Biostrings_2.64.0           readr_2.1.2                 [21] matrixStats_0.62.0          R.utils_2.12.0              [23] colorspace_2.0-3            blob_1.2.3                  [25] usdata_0.2.0                xfun_0.32                   [27] crayon_1.5.1                RCurl_1.98-1.8              [29] jsonlite_1.8.0              hexbin_1.28.2               [31] GEOquery_2.64.2             survival_3.3-1              [33] iterators_1.0.14            glue_1.6.2                  [35] gtable_0.3.0                zlibbioc_1.42.0             [37] XVector_0.36.0              DelayedArray_0.22.0         [39] kernlab_0.9-31              maps_3.4.0                  [41] scales_1.2.1                DBI_1.1.3                   [43] Rcpp_1.0.9                  xtable_1.8-4                [45] bit_4.0.4                   htmlwidgets_1.5.4           [47] httr_1.4.4                  ellipsis_0.3.2              [49] pkgconfig_2.0.3             R.methodsS3_1.8.2           [51] sass_0.4.2                  utf8_1.2.2                  [53] crul_1.2.0                  tidyselect_1.1.2            [55] rlang_1.0.4                 reshape2_1.4.4              [57] later_1.3.0                 munsell_0.5.0               [59] tools_4.2.1                 cachem_1.0.6                [61] cli_3.3.0                   generics_0.1.3              [63] RSQLite_2.2.16              evaluate_0.16               [65] stringr_1.4.1               fastmap_1.1.0               [67] yaml_2.3.5                  knitr_1.39                  [69] bit64_4.0.5                 airports_0.1.0              [71] cherryblossom_0.1.0         purrr_0.3.4                 [73] KEGGREST_1.36.3             nlme_3.1-157                [75] sparseMatrixStats_1.8.0     mime_0.12                   [77] R.oo_1.25.0                 xml2_1.3.3                  [79] compiler_4.2.1              curl_4.3.2                  [81] png_0.1-7                   tibble_3.1.8                [83] bslib_0.4.0                 stringi_1.7.8               [85] gistr_0.9.0                 lattice_0.20-45             [87] vctrs_0.4.1                 pillar_1.8.1                [89] lifecycle_1.0.1             BiocManager_1.30.18         [91] jquerylib_0.1.4             bitops_1.0-7                [93] httpuv_1.6.5                GenomicRanges_1.48.0        [95] R6_2.5.1                    promises_1.2.0.1            [97] codetools_0.2-18            MASS_7.3-57                 [99] assertthat_0.2.1            SummarizedExperiment_1.26.1[101] withr_2.5.0                 httpcode_0.3.0             [103] openintro_2.3.0             GenomeInfoDbData_1.2.8     [105] parallel_4.2.1              hms_1.1.2                  [107] grid_4.2.1                  tidyr_1.2.0                [109] rmarkdown_2.15              DelayedMatrixStats_1.18.0  [111] segmented_1.6-0             MatrixGenerics_1.8.1
```

### 2.0.2 安装

```
if (!requireNamespace("BiocManager", quietly=TRUE))    install.packages("BiocManager")# To support paralell execution:BiocManager::install(c("doMC", "doRNG","doSNOW"))# For the main example:BiocManager::install(c("mixtools", "SummarizedExperiment"))# For the examples in the follow-up section of the tutorial:BiocManager::install(c("DT", "plotly", "NMF", "d3heatmap", "shiny", "rbokeh",                       "dynamicTreeCut","R2HTML","Rtsne", "zoo"))BiocManager::install('AUCell')
```

### 2.0.3 获取帮助文档

大部分的包都可以这样调用帮助文档

```
#在浏览器中查看browseVignettes(package="AUCell") #命令行中查看vignette(package="AUCell") # listvignette("AUCell") # zoom中打开
```

### 2.0.4

作者贴心的给了一个Rmarkdown的模板，大家可以这样调用，使用AUCell的时候就不用重复写报告啦

```r
vignetteFile <- paste(file.path(system.file('doc', package='AUCell')), "AUCell.Rmd", sep="/")# Copy to edit as markdownfile.copy(vignetteFile, ".")# Alternative: extract R codeStangle(vignetteFile)
```

## 2.1. 最简单的用法

```r
library(AUCell)#给定一个基因集geneSets <- list(geneSet1=c("gene1", "gene2", "gene3"))#计算富集分数：cells_AUC <- AUCell_run(exprMatrix, geneSets,                        aucMaxRank=nrow(cells_rankings)*0.05)#这一步其实就可以得到AUC score#可选：通过设定阈值将AUC score转换为二元矩阵(判断基因集是否激活，用于在SCENIC中判断regulon是否激活)par(mfrow=c(3,3))set.seed(123)cells_assignment <- AUCell_exploreThresholds(cells_AUC,                                              plotHist=TRUE,                                              nCores=1, assign=TRUE)
```

## 2.2. 测试数据

### 2.2.1 表达矩阵

数据来源为GSE60361，该数据集中包含3005个细胞，物种为mouse，组织来源为**cortex** 和**hippocampus** 。

```r
#下载数据：if (!requireNamespace("GEOquery", quietly = TRUE)) BiocManager::install("GEOquery")geoFile <- "GSE60361_C1-3005-Expression.txt.gz"# download.file("https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60361/suppl/GSE60361_C1-3005-Expression.txt.gz", destfile = geoFile)library(data.table)exprMatrix <- fread(geoFile, sep="\t")exprMatrix[1:5,1:5]#第一列是基因名，需要将其转换为行名
```
```
##     cell_id 1772071015_C02 1772071017_G12 1772071017_A05 1772071014_B06
## 1:  Tspan12              0              0              0              3
## 2:    Tshz1              3              1              0              2
## 3:   Fnbp1l              3              1              6              4
## 4: Adamts15              0              0              0              0
## 5:   Cldn12              1              1              1              0
```

Hide
```r
geneNames <- unname(unlist(exprMatrix[,1, with=FALSE]))geneNames[1:5]
```
```
## [1] "Tspan12"  "Tshz1"    "Fnbp1l"   "Adamts15" "Cldn12"
```

```r
exprMatrix <- as.matrix(exprMatrix[,-1, with=FALSE])rownames(exprMatrix) <- geneNamesexprMatrix <- exprMatrix[unique(rownames(exprMatrix)),]dim(exprMatrix)
```
```
## [1] 19970  3005
```

```
exprMatrix[1:5,1:4]
```
```
##          1772071015_C02 1772071017_G12 1772071017_A05 1772071014_B06
## Tspan12               0              0              0              3
## Tshz1                 3              1              0              2
## Fnbp1l                3              1              6              4
## Adamts15              0              0              0              0
## Cldn12                1              1              1              0
```

```r
#将矩阵转换为稀疏矩阵library(Matrix)exprMatrix <- as(exprMatrix, "dgCMatrix")#保存成RdatamouseBrainExprMatrix <- exprMatrixsave(mouseBrainExprMatrix, file="exprMatrix_MouseBrain.RData")
```

这里为了加速演示过程并节省计算资源，做一个抽样，随机抽取表达矩阵中的5000个基因
```r
set.seed(333)#设定随机数一定程度上保证结果的可重复性load('exprMatrix_MouseBrain.RData')exprMatrix <- mouseBrainExprMatrix[sample(rownames(mouseBrainExprMatrix), 5000),]dim(exprMatrix)
```
```
## [1] 5000 3005
```

### 2.2.2 测试基因集
```r
library(AUCell)library(GSEABase)gmtFile <- paste(file.path(system.file('examples',                                       package='AUCell')),                  "geneSignatures.gmt", sep="/")geneSets <- getGmt(gmtFile)
```

这个数据的结构大概是这样:

![](../../images/96e578482440e0e0.webp)

```
rownames(exprMatrix)[1:5]
```
```
## [1] "Gm5833"   "Gm16119"  "Arhgap44" "Snord99"  "Ccl5"
```

```r
#取出表达矩阵中包含的geneSets <- subsetGeneSets(geneSets, rownames(exprMatrix))#查看每个基因集中包含在表达矩阵中的基因数量nGenes(geneSets)
```
```
##       Astrocyte_Cahoy          Neuron_Cahoy Oligodendrocyte_Cahoy
##                   526                   404                   469
##        Astrocyte_Lein           Neuron_Lein       Microglia_lavin
##                     7                    15                   159
```

```r
#把每个基因集包含的基因数量加在基因集名称后面：geneSets <- setGeneSetNames(geneSets, newNames=paste(names(geneSets), " (", nGenes(geneSets) ,"g)", sep=""))names(geneSets)
```
```
## [1] "Astrocyte_Cahoy (526g)"       "Neuron_Cahoy (404g)"
## [3] "Oligodendrocyte_Cahoy (469g)" "Astrocyte_Lein (7g)"
## [5] "Neuron_Lein (15g)"            "Microglia_lavin (159g)"
```

为了确定上述基因集结果的真实性，这里掺入一些**随机抽取** 的**模拟** 基因集

```r
set.seed(321)extraGeneSets <- c(  GeneSet(sample(rownames(exprMatrix), 50), setName="Random (50g)"),  GeneSet(sample(rownames(exprMatrix), 500), setName="Random (500g)"))#统计count大于0的基因：countsPerGene <- apply(exprMatrix, 1, function(x) sum(x>0))gene4use <- sample(names(countsPerGene)[which(countsPerGene>quantile(countsPerGene, probs=.95))], 100)#从表达量前5%的函数中随机抽取一百个基因#构建基因集：extraGeneSets <- c(extraGeneSets,                   GeneSet(gene4use, setName="HK-like (100g)"))#这些基因的表达量比较高，这里可以初步命名为house-keeping like Gene#合并测试基因集与模拟基因集geneSets <- GeneSetCollection(c(geneSets,extraGeneSets))names(geneSets)
```
```
## [1] "Astrocyte_Cahoy (526g)"       "Neuron_Cahoy (404g)"
## [3] "Oligodendrocyte_Cahoy (469g)" "Astrocyte_Lein (7g)"
## [5] "Neuron_Lein (15g)"            "Microglia_lavin (159g)"
## [7] "Random (50g)"                 "Random (500g)"
## [9] "HK-like (100g)"
```

## 2.3 AUCell流程

与`GSVA`不同的是，`GSVA`需要输入完整的表达矩阵(样本数、基因数以及表达矩阵的单位都会影响GSVA score的计算)。但是由于AUCell有一步`rank`的过程，因此输入矩阵的完整性要求没有那么严格。

### 2.3.1 一步法计算基因集的富集分数(AUC)

```
if(!require(BiocParallel))BiocManager::install('BiocParallel')
```
```
## 载入需要的程辑包：BiocParallel
```

```
BPPARAM=BiocParallel::MulticoreParam(5)#开5个核并行计算
```
```
## Warning in BiocParallel::MulticoreParam(5): MulticoreParam() not supported on
## Windows, use SnowParam()
```

```r
cells_AUC <- AUCell_run(exprMatrix, geneSets)#1.16.0版本的AUCell没有AUCell_run这个函数，推荐在R4.2.1目录下安装AUCell的1.18.1版本#AUCell score的矩阵存在:cells_AUC@assays@data$AUC[1:4,1:4]
```
```
##                               cells
## gene sets                      1772071015_C02 1772071017_G12 1772071017_A05
##   Astrocyte_Cahoy (526g)            0.1463133      0.1372851      0.1588755
##   Neuron_Cahoy (404g)               0.2775261      0.2978313      0.2960964
##   Oligodendrocyte_Cahoy (469g)      0.1507791      0.1219598      0.1357430
##   Astrocyte_Lein (7g)               0.1509872      0.1399535      0.2166086
##                               cells
## gene sets                      1772071014_B06
##   Astrocyte_Cahoy (526g)            0.1650442
##   Neuron_Cahoy (404g)               0.3202570
##   Oligodendrocyte_Cahoy (469g)      0.1296386
##   Astrocyte_Lein (7g)               0.2485482
```

```
save(cells_AUC, file="cells_AUC.RData")#画个热图看一下：suppressMessages(if(!require(pheatmap))install.packages('pheatmap'))pheatmap(cells_AUC@assays@data$AUC,show_colnames = F)#没错，确实是连续性数值，因为AUCell score是一个积分，所以也不会像GSVA那样有负值啦。
```

![](../../images/9c230ef38626310c.webp)

### 2.3.2 拆解计算步骤

`AUCell_run`等同于下面的`AUCell_buildRankings`**+**`AUCell_calcAUC`，拆分出来有利于大家理解AUCell的计算过程

```
plotGeneCount(as.matrix(exprMatrix))#可以先看一下每个细胞中表达的基因数量,这组细胞表达基因数量中位数不足一千个
```
```
## Quantiles for the number of genes detected by cell:
## (Non-detected genes are shuffled at the end of the ranking. Keep it in mind when choosing the threshold for calculating the AUC).
```

![](../../images/5660673fbfa69706.webp)
```
##     min      1%      5%     10%     50%    100%
##  193.00  271.08  364.20  447.40  921.00 2056.00
```

```r
cells_rankings <- AUCell_buildRankings(exprMatrix, plotStats=FALSE, splitByBlocks=TRUE)#把每一个细胞的基因从表达量由高向低排列cells_rankings#由于这步ranking，大家合并不同的数据集时需要保证数据集里每个细胞检测到的基因数量相近
```
```
## Ranking for 5000 genes (rows) and 3005 cells (columns).
##
## Top-left corner of the ranking:
##           cells
## genes      1772071015_C02 1772071017_G12 1772071017_A05 1772071014_B06
##   Gm5833             4904           3305           4028           3895
##   Gm16119            2327           1596           1794           2610
##   Arhgap44            182           2937            330            296
##   Snord99            4021           2865           4514           4628
##   Ccl5               3794           4095           3332           3794
##   Sox18              4807           3052           3126           3365
##           cells
## genes      1772067065_H06
##   Gm5833             3028
##   Gm16119            2588
##   Arhgap44            157
##   Snord99            2932
##   Ccl5               2774
##   Sox18              4918
```

```r
cells_AUC <- AUCell_calcAUC(geneSets, cells_rankings)
```
```
## Warning in .AUCell_calcAUC(geneSets = geneSets, rankings = rankings, nCores =
## nCores, : Using only the first 250 genes (aucMaxRank) to calculate the AUC.
```

```r
#为了应对大数据的计算以及去噪，只有每个细胞表达量最高的前5%的基因参与计算#这一比例可以通过'aucMaxRank'参数调整，比如：cells_AUC <- AUCell_calcAUC(geneSets, cells_rankings,                   aucMaxRank = ceiling(0.05 * nrow(cells_rankings)))
```
```
## Warning in .AUCell_calcAUC(geneSets = geneSets, rankings = rankings, nCores =
## nCores, : Using only the first 250 genes (aucMaxRank) to calculate the AUC.
```

按照我个人的理解，AUCell的过程类似于对每个细胞的基因排序后进行GSEA分析(GSEA的教程可以[点这里](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484175&idx=1&sn=3e45ad62b045a541874e5ae7ca03f849&chksm=9b3f7a5fac48f349f8893500825d2c6b4ff581fbb0816c1074d88a0dbbb4a612c1e1bb3740bb&scene=21#wechat_redirect>))，然后把基因的排序作为一个**连续值** ，**求积分** 。`AUC`一定程度上反应了signature基因表达的比例，并且可以代表它们相对于细胞内其他基因的相对表达值。换句话说，我们可以使用AUC来探索数据集中存在的细胞种群。AUC也会考虑到每个细胞中高度表达的基因在基因集中的比例。从基因集中表达很多基因的细胞将比表达较少的细胞拥有更高的AUC值，也就是说AUC的值在不同的基因集之间也是可以相互比较的。由于AUC一定程度上代表了signature中表达基因的比例，因此细胞间的相对AUC来根据基因集的表达来探索数据集中存在的细胞群体(根据SCENIC的文献报道利用AUCell score进行细胞分群的效果甚至要比大多数去除批次效用的方法都好)。但是由于AUCell score并不是一个绝对表达值，以及考虑到细胞大小、选择的基因集的大小(越大的基因集AUCell score越大，并且越容易呈现正态分布)和表达情况、单细胞测序矩阵的稀疏性，通过AUCell score来判断一个基因集的表达是激活还是沉默需要进一步的探索。这个问题实质上需要解决如何将AUCell score这一连续性矩阵转换为二项分布的矩阵。这时可以用`AUCell_exploreThresholds()`自动绘制直方图，并自动计算数个阈值，可以用来考虑一个基因集是on或off“(在`$aucThr`中返回)。对应的阈值用匹配颜色的竖条表示，较粗的竖线表示软件默认选择的阈值($aucThr$selected)，这一阈值能够最大限度的减少假阳性。

```r
if (!requireNamespace("mixtools", quietly=TRUE))BiocManager::install("mixtools") set.seed(123)par(mfrow=c(3,3)) cells_assignment <- AUCell_exploreThresholds(cells_AUC, plotHist=TRUE, assign=TRUE)#计算阈值并绘制柱状图
```

![](../../images/ad9730e282b2e952.webp)

```
#返回的数据结构包含软件选择的最佳阈值，其他阈值的返回结果(阈值参数与当前阈值下"on"的细胞数量)，软件返回的commentcells_assignment$`Astrocyte_Cahoy (526g)`$aucThr
```
```
## $selected
##      L_k2
## 0.2384452
##
## $thresholds
##            threshold nCells
## Global_k1 0.18579694    375
## L_k2      0.23844518    220
## R_k3      0.09762972   2629
##
## $comment
## [1] ""
```

```r
warningMsg <- sapply(cells_assignment, function(x) x$aucThr$comment)#把comment循环取出warningMsg[which(warningMsg!="")]#查看非空的comment
```
```
##                                                                                                                  Random (500g)
## "The AUC might follow a normal distribution (random gene-set?).  The global distribution overlaps the partial distributions. "
```

```
#之间混入的随机选取的基因集被发现了，判定为正态分布的矩阵#同样的代码我们可以得到每个geneset的最佳阈值：sapply(cells_assignment, function(x) x$aucThr$selected)
```
```
##              Astrocyte_Cahoy (526g).L_k2
##                               0.23844518
##          Neuron_Cahoy (404g).minimumDens
##                               0.14918986
## Oligodendrocyte_Cahoy (469g).minimumDens
##                               0.23828191
##          Astrocyte_Lein (7g).minimumDens
##                               0.03079067
##            Neuron_Lein (15g).minimumDens
##                               0.18279180
##              Microglia_lavin (159g).L_k2
##                               0.13368241
##                   Random (50g).Global_k1
##                               0.01883846
##            Random (500g).outlierOfGlobal
##                               0.15682484
##                      HK-like (100g).L_k2
##                               0.69133962
```

```
#在默认最佳阈值下获得的处于"on"状态下的细胞barcode名称(这里只展示前五个)suppressMessages(library(dplyr))sapply(cells_assignment, function(x) x$assignment %>% .[1:5])
```
```
##      Astrocyte_Cahoy (526g) Neuron_Cahoy (404g) Oligodendrocyte_Cahoy (469g)
## [1,] "1772071015_A01"       "1772071015_C02"    "1772067069_B02"
## [2,] "1772066080_D10"       "1772071017_G12"    "1772071041_A02"
## [3,] "1772066099_C03"       "1772071017_A05"    "1772066077_G03"
## [4,] "1772071036_B05"       "1772071014_B06"    "1772066070_D08"
## [5,] "1772067060_G06"       "1772067065_H06"    "1772067076_A07"
##      Astrocyte_Lein (7g) Neuron_Lein (15g) Microglia_lavin (159g)
## [1,] "1772071015_C02"    "1772071015_C02"  "1772062116_E04"
## [2,] "1772071017_G12"    "1772071017_G12"  "1772060225_F12"
## [3,] "1772071017_A05"    "1772071017_A05"  "1772062118_B06"
## [4,] "1772071014_B06"    "1772071014_B06"  "1772066077_B04"
## [5,] "1772067065_H06"    "1772067065_H06"  "1772058171_F04"
##      Random (50g)     Random (500g) HK-like (100g)
## [1,] "1772071017_A05" NA            NA
## [2,] "1772071014_E04" NA            NA
## [3,] "1772071017_F09" NA            NA
## [4,] "1772071017_A09" NA            NA
## [5,] "1772067094_C05" NA            NA
```

```
#在默认最佳阈值下获得的处于"on"状态下的细胞数量sapply(cells_assignment, function(x) x$assignment %>% length)
```
```
##       Astrocyte_Cahoy (526g)          Neuron_Cahoy (404g)
##                          220                         1777
## Oligodendrocyte_Cahoy (469g)          Astrocyte_Lein (7g)
##                          741                         2633
##            Neuron_Lein (15g)       Microglia_lavin (159g)
##                         1794                           35
##                 Random (50g)                Random (500g)
##                          657                            0
##               HK-like (100g)
##                            0
```

```r
#画出对应geneset处于on状态下的细胞geneSetName <- rownames(cells_AUC)[grep("Oligodendrocyte_Cahoy", rownames(cells_AUC))]par(mfrow=c(1,1)) AUCell_plotHist(cells_AUC[geneSetName,], aucThr=cells_assignment$`Oligodendrocyte_Cahoy (469g)`$aucThr$selected)abline(v=cells_assignment$`Oligodendrocyte_Cahoy (469g)`$aucThr$selected)
```

![](../../images/38169f78b1c22a0a.webp)

```r
#解放劳动力，还是得靠写循环展示出所有geneset的情况par(mfrow=c(3,3)) for(i in 1:length(cells_assignment)){  temp.name <- gsub(' (.*)','',names(cells_assignment)[i])  temp.cellname <- rownames(cells_AUC)[grep(temp.name, rownames(cells_AUC))]  AUCell_plotHist(cells_AUC[temp.cellname,], aucThr=cells_assignment[[i]]$aucThr$selected)  abline(v=cells_assignment[[i]]$aucThr$selected)}
```

![](../../images/815a787a0f3d9d2a.webp)![](../../images/68047827c8fc34f1.webp)

### 2.3.3 进一步分析
```r
cellsAssigned <- lapply(cells_assignment, function(x) x$assignment)#去除assignment，即'on'的barcodeassignmentTable <- reshape2::melt(cellsAssigned, value.name="cell")#转换成长格式的tablecolnames(assignmentTable)[2] <- "geneSet"head(assignmentTable)
```
```
##             cell                geneSet
## 1 1772071015_A01 Astrocyte_Cahoy (526g)
## 2 1772066080_D10 Astrocyte_Cahoy (526g)
## 3 1772066099_C03 Astrocyte_Cahoy (526g)
## 4 1772071036_B05 Astrocyte_Cahoy (526g)
## 5 1772067060_G06 Astrocyte_Cahoy (526g)
## 6 1772058148_A03 Astrocyte_Cahoy (526g)
```

```r
assignmentMat <- table(assignmentTable[,"geneSet"], assignmentTable[,"cell"])assignmentMat[1:4,1:4]#统计，table到的就是1(on)，不存在的就是0(off),也就是说geneset从这一步变成了二项分布的矩阵
```
```
##
##                          1772058148_A01 1772058148_A03 1772058148_A04
##   Astrocyte_Cahoy (526g)              0              1              0
##   Astrocyte_Lein (7g)                 1              1              1
##   Microglia_lavin (159g)              0              0              0
##   Neuron_Cahoy (404g)                 0              0              0
##
##                          1772058148_A05
##   Astrocyte_Cahoy (526g)              0
##   Astrocyte_Lein (7g)                 1
##   Microglia_lavin (159g)              1
##   Neuron_Cahoy (404g)                 0
```

可以通过热图的形式展示这个二元的矩阵
```
set.seed(123)suppressMessages(library(NMF))aheatmap(assignmentMat, scale="none", color="black", legend=FALSE)
```

![](../../images/6e28ce8551b9de9b.webp)

### 2.3.4 实测一下AUCell score对单细胞分群的帮助

读取原始表达矩阵并进行`tsne`分析

```r
mouseBrainExprMatrix[1:4,1:4]#表达矩阵sumByGene <- apply(mouseBrainExprMatrix, 1, sum)#对每个基因的count求和exprMatSubset <- mouseBrainExprMatrix[which(sumByGene>0),]#从矩阵中删除不表达的基因logMatrix <- log2(exprMatSubset+1)logMatrix <- as.matrix(logMatrix)library(Rtsne)set.seed(123)cellsTsne <- Rtsne(t(logMatrix))#运行TSNErownames(cellsTsne$Y) <- colnames(logMatrix)colnames(cellsTsne$Y) <- c("tsne1", "tsne2")save(cellsTsne, file="cellsTsne.RData")
```

```r
load('cellsTsne.RData')cellsTsne <- cellsTsne$Yplot(cellsTsne, pch=16, cex=.3)
```

![](../../images/c8037a97048a9095.webp)

```r
library(DT)datatable(assignmentTable, options = list(pageLength = 10), filter="top")
```

|
|

---|---|---

|
|

1| 1772071015_A01| Astrocyte_Cahoy (526g)
2| 1772066080_D10| Astrocyte_Cahoy (526g)
3| 1772066099_C03| Astrocyte_Cahoy (526g)
4| 1772071036_B05| Astrocyte_Cahoy (526g)
5| 1772067060_G06| Astrocyte_Cahoy (526g)
6| 1772058148_A03| Astrocyte_Cahoy (526g)
7| 1772060240_H04| Astrocyte_Cahoy (526g)
8| 1772063063_B11| Astrocyte_Cahoy (526g)
9| 1772060225_B12| Astrocyte_Cahoy (526g)
10| 1772063074_E01| Astrocyte_Cahoy (526g)

  *

```
assignmentTable[1:4,]
```
```
##             cell                geneSet
## 1 1772071015_A01 Astrocyte_Cahoy (526g)
## 2 1772066080_D10 Astrocyte_Cahoy (526g)
## 3 1772066099_C03 Astrocyte_Cahoy (526g)
## 4 1772071036_B05 Astrocyte_Cahoy (526g)
```

在TSNE图中原位把AUCell score画出来看看，类似于Seurat::FeaturePlot()
```r
selectedThresholds <- getThresholdSelected(cells_assignment)#好吧，原来有直接获得selectedThr的方法，不需要写循环selectedThresholds[1:5]
```
```
##       Astrocyte_Cahoy (526g)          Neuron_Cahoy (404g)
##                   0.23844518                   0.14918986
## Oligodendrocyte_Cahoy (469g)          Astrocyte_Lein (7g)
##                   0.23828191                   0.03079067
##            Neuron_Lein (15g)
##                   0.18279180
```

```r
par(mfrow=c(2,3)) # Splits the plot into two rows and three columnsfor(geneSetName in names(selectedThresholds)){  #处于off状态下的物种颜色：  colorPal_Neg <- grDevices::colorRampPalette(c("black","blue", "skyblue"))(5)  #处于on状态下的物种颜色：  colorPal_Pos <- grDevices::colorRampPalette(c("pink", "magenta", "red"))(5)    # 将细胞按照on和off拆开  passThreshold <- getAUC(cells_AUC)[geneSetName,] >  selectedThresholds[geneSetName]  if(sum(passThreshold) >0 )  {    aucSplit <- split(getAUC(cells_AUC)[geneSetName,], passThreshold)        # Assign cell color    cellColor <- c(setNames(colorPal_Neg[cut(aucSplit[[1]], breaks=5)], names(aucSplit[[1]])),     setNames(colorPal_Pos[cut(aucSplit[[2]], breaks=5)], names(aucSplit[[2]])))        plot(cellsTsne, main=geneSetName,    sub="Pink/red cells pass the threshold",    col=cellColor[rownames(cellsTsne)], pch=16)     #这里的绘图方式其实也给我们DIY featurePlot提供了思路  }}
```

![](../../images/73fa4cb2731f2d69.webp)

```
#还有一个更简单的方法：par(mfrow=c(2,3))
```

![](../../images/383f326482fc8577.webp)

```
AUCell_plotTSNE(tSNE=cellsTsne, exprMat=exprMatrix, cellsAUC=cells_AUC[1:2,], thresholds=selectedThresholds[1:2])
```

![](../../images/bf2d00c02d7ed435.webp)

```
#AUCell_plotTSNE三联分布展示了AUCell score的分布柱状图、TSNE原位展示通过阈值筛选的点、TSNE原位展示AUCell score
```

作者这里还给了一个自动创建shinyApp的函数，再次让我叹为观止，我来好好学一学，下次给大家写个类似的

```r
library(shiny); library(rbokeh)exprMat <- log2(mouseBrainExprMatrix+1) # (back to the full matrix)# Create app aucellApp <- AUCell_createViewerApp(auc=cells_AUC, thresholds=selectedThresholds,                                     tSNE=cellsTsne, exprMat=exprMat)# Run (the exact commands depend on the R settings, see Shiny's doc for help)options(shiny.host="0.0.0.0") savedSelections <- runApp(aucellApp) # Other common settings:# host = getOption("shiny.host", "127.0.0.1") # shinyApp(ui=aucellApp$ui, server=aucellApp$server)# Optional: Visualize extra information about the cells (categorical variable)cellInfoFile <- paste(file.path(system.file('examples', package='AUCell')),                       "mouseBrain_cellLabels.tsv", sep="/")cellInfo <- read.table(cellInfoFile, row.names=1, header=TRUE, sep="\t")head(cellInfo)Another example for interactive plot (e.g. to save as html, no need to keep the server running):    geneSetName <- "Astrocyte_Cahoy (555g)"library(rbokeh)tSNE.df <- data.frame(cellsTsne, cell=rownames(cellsTsne))figure() %>%  ly_points(tsne1, tsne2, data=tSNE.df, size=1, legend = FALSE,            hover=cell, color=getAUC(cells_AUC)[geneSetName,rownames(tSNE.df)]) %>%  set_palette(continuous_color = pal_gradient(c("lightgrey", "pink", "red")))
```

## 2.4 为什么选择AUCell?

其实这个问题上文也解释过，最简单的评价基因集表达量的方法是算平均值，但是平均值容易受到基因表达量、测序文库大小的影响(这也就无法考虑到批次效应等非生物学问题)。而AUCell是对每个细胞的矩阵rank后做富集打分，可以回避这些问题，并且对每个细胞独立分析的策略可以回避normalization的方式(即`raw counts`, `TPM`, `UMI counts`等均可以作为输入数据)

做个简单的对比
这是基因集均值的展示:

```r
logMat <- log2(exprMatrix+2)meanByGs <- t(sapply(geneSets, function(gs) colMeans(logMat[geneIds(gs),])))rownames(meanByGs) <- names(geneSets)colorPal <- grDevices::colorRampPalette(c("white", "red"))(5)par(mfrow=c(3,3))for(geneSetName in names(geneSets)){  cellColor <- setNames(colorPal[cut(meanByGs[geneSetName,], breaks=5)], names(meanByGs[geneSetName,]))  plot(cellsTsne, main=geneSetName, axes=FALSE, xlab="", ylab="",  sub="Expression mean",  col=cellColor[rownames(cellsTsne)], pch=16)}
```

![](../../images/01e890ca17096106.webp)

这是AUCell score的展示:
```
par(mfrow=c(3,3))AUCell_plotTSNE(tSNE=cellsTsne, exprMat=exprMatrix, plots = "AUC",cellsAUC=cells_AUC[1:9,], thresholds=selectedThresholds)
```

![](../../images/7ee91733731edb94.webp)

还有一个点是，这类基因集打分的软件大都是打个分即完事，而不仅AUCell自己创立了一套判断`on/off`的方法，可以帮助大家判断基因集是否被激活；还会为基因集的治疗做出评估，例如上面随机抽样的基因集就被**AUCell** 发现符合正态分布，不适用于`on/off`的评价体系。

#

#

# **最后、单细胞教程全收录：**

![](../../images/90fab1387787746b.gif)

单细胞数据分析系列教程：

B站视频，先看一遍视频再去看推送操作，建议至少看三遍：https://www.bilibili.com/video/BV1S44y1b76Z/以下的资料都可以在这里订阅：[2022资料合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491618&idx=1&sn=ebd55322b512225ed1834bd307fc0baa&chksm=9b3c9972ac4b1064bf1ec24f5c547cec831625db80da2f77e55ea56f8a326ca0cb715a0bff3d&scene=21#wechat_redirect>)

单细胞测序基础数据分析保姆级教程，代码部分整理在往期推送之中：[手把手教你做单细胞测序数据分析（一）——绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484077&idx=1&sn=e329bf865493d46308985f4c111370ae&chksm=9b3f7bfdac48f2eb7e903510338bd772c6be34ccbcb681806d288e62a05eee28fa209d2f33b9&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析（二）——各类输入文件读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484086&idx=1&sn=7346a09ba350d6fb7c806dcb7509a1ef&chksm=9b3f7be6ac48f2f02cb948140381ad2a0e3818cc0eefc53cb7a1ad7459aacdc1e90a1ce0af8b&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析（三）——单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487976&idx=1&sn=8edd929256e609e4210a40df63fc1427&chksm=9b3f68b8ac48e1aefd3ff38dd5744c485cde5d7f28d79745b66863928d4614fafb2928b3f617&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析（四）——多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488539&idx=1&sn=73c538e31907b8d82437cc063b2a2a15&chksm=9b3f6d4bac48e45dcc737ee5a7529f58803fdbaa9ef49aca3c76af0f2e7e374247266b0d16cb&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析（五）——细胞类型注释](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488597&idx=1&sn=6123d348db245774d4a0db4134a839d4&chksm=9b3f6d05ac48e4132f92ca6c32dab29d2a4e1eb00d1db3b6e10eba7ffc7154e8554a70938583&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析（六）——组间差异分析及可视化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488675&idx=1&sn=c1f4ac08b87baf625c7aafa8f073ed79&chksm=9b3f6df3ac48e4e53ef11776bda8a5f75f1d465e4e2d6cccd5e4e1aff5f26eaa34cdea3aabb8&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析（七）——基因集富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488717&idx=1&sn=6ba02599dda33eb6cff751c1d92055d9&chksm=9b3f6d9dac48e48ba334f031ce7874b4383a45be271acc9f0e6a714934ab7c7d945a513efdec&scene=21#wechat_redirect>)

上游fastq文件处理：
[单细胞分析的最上游——处理Fastq文件：cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484923&idx=1&sn=b5876af14fbee68d1e9db4b0f70cd1c8&chksm=9b3f7cabac48f5bdb3aac7d20201d89121a83720b41a10017564fedbb8c4a13df0da92daffd7&scene=21#wechat_redirect>)
[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484937&idx=1&sn=4fe1fa518202bdaf462bb93a2614ed32&chksm=9b3f7f59ac48f64fafaf34bac2c80f06d3a86b6a84ccf12566c7eac25bb71c7edd3d74004cf7&scene=21#wechat_redirect>)[有奖提问,这个smart-Seq2数据实战的比对率为何如此低？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488441&idx=1&sn=dac4efc4a8901a4abb133f9e5c80831e&chksm=9b3f6ae9ac48e3fff5a7112a0127726441ccb9dc2c3369d4a0fe98a2120df991954ff0567732&scene=21#wechat_redirect>)

细胞通讯B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1Ab4y1W7qx?p=1**往期推送**[ 单细胞测序数据进阶分析—《细胞通讯》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485403&idx=1&sn=e148e2d09556a85333cd9c212a880aaa&chksm=9b3f7e8bac48f79d6288977f3a67ebed5813dfe92e4a227a2e304eb68321771b3511fdaf5ba5&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《细胞通讯》2.1CellChat基础分析教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485680&idx=1&sn=8168685ab9bbf772dce24e8673994033&chksm=9b3f71a0ac48f8b6554aa6f30a81f7e622fd8bf2f6a83701839290b7dd8f1c90343592603413&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《细胞通讯》2.2CellChat多组别分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485706&idx=1&sn=2d39360b41733b0be6f88d2922388507&chksm=9b3f705aac48f94cc478210f7f11d37294156517c489dedb333d8647ca287134a29944f39a3d&scene=21#wechat_redirect>)
[给你们申请到了免费的128GB云服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485734&idx=1&sn=32c75f6d07b49084e518af6d18099e8b&chksm=9b3f7076ac48f9600593b319d2e0b36bf5a62399a9835caa5783ad36fbdec6004e04cb656db9&scene=21#wechat_redirect>)
拟时序分析B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1br4y1x7Hf?p=1**往期推送**[ 单细胞测序数据进阶分析—《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》3.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487400&idx=1&sn=223a96a245c408c31e2c3c16afac88fc&chksm=9b3f76f8ac48ffee769dc76870e15bbd0275647dcfb9bf21bf499b7eaee86121b254e4b2da54&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》4.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)

其他单细胞相关技术贴也在这里：[细胞的数量由誰决定？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484056&idx=1&sn=4967a054f5241ff3a1bd4a6fe9a502b1&chksm=9b3f7bc8ac48f2deca3141461be035deb8658be184d78597af28f8ba2092d12f020768275248&scene=21#wechat_redirect>)[单细胞中应该如何做GSVA？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&chksm=9b3f7c4dac48f55bf1d11337406ab0e1295e8e1731dbac0715eedc99d11beff7f380e42dd49b&scene=21#wechat_redirect>)[答读者问（三）：单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)[答读者问（四）：如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)[答读者问（六）：Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484376&idx=2&sn=9fda8a5261e86f889a58d607163ce0fd&chksm=9b3f7a88ac48f39ea9c19e256a513c9ae80c6f6dc1724b7783884e23981e2061c78fa67071c9&scene=21#wechat_redirect>)[答读者问（八）：为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)
[答读者问（十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)
[答读者问（十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析：Loupe Browser](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a&scene=21#wechat_redirect>)
[什么？不做单细胞也能分析细胞类群和免疫浸润？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485798&idx=1&sn=c849bc7a0093af92fc99e13b55842bb2&chksm=9b3f7036ac48f92048d726b38f2dd978d0b0cce779c1a4090aa4da5cb2df3ad30a5c5dbed27e&scene=21#wechat_redirect>)
[答读者问 （十三）查看Seurat对象时的ERROR：type='text'](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)
[各类单细胞对象（数据格式）转换大全（一）](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485925&idx=1&sn=14e08440200f0f5cb4dcc2dc615efeb8&chksm=9b3f70b5ac48f9a37a43cc2a8b2a5e485a3f84b4ef87949dfe99056bc6301b110e80800f6bb1&scene=21#wechat_redirect>)[批量整理好GEO中下载的单细胞数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486045&idx=1&sn=0b6874bcffc8abafb505cabce4c4fc0e&chksm=9b3f730dac48fa1b140ef01c07a7749e69df4fa7d2056deeed0673c668b6246724cd85741125&scene=21#wechat_redirect>)
[答读者问 （十四）Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)
[答读者问 （十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)
[答读者问 （十六）做单细胞测序到底需要多少内存](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487923&idx=1&sn=15043c6d729b0d5493ab875b0e54a259&chksm=9b3f68e3ac48e1f5dae514a01c857f9a56a90e2977dd7862db28d06fe55888cd9bb4afbb14e0&scene=21#wechat_redirect>)[答读者问 （十七）调用的线程越多就算的越快嘛?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488995&idx=1&sn=7140e0d037671542fb37dff3a3c94b28&chksm=9b3f6cb3ac48e5a5f54a02be9e6af9f5a4cf8da1de1770f9035130c84dedf059a024964fc15a&scene=21#wechat_redirect>)
[答读者问（十八）、一个我至少被问过30遍的monocle报错](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25&scene=21#wechat_redirect>)
[一文搞定单细胞基因集评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490658&idx=1&sn=3460a09ef4ad2916aabfaa13e195c7b1&chksm=9b3f6532ac48ec249e974aa5bfcca2f5d441e64bbd353fe9dd45a50b47599663bf0334def7d4&scene=21#wechat_redirect>)[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&scene=21#wechat_redirect>)[没有barcode文件的单细胞数据要怎么读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490952&idx=1&sn=364a3941e59e45234795c906a42fc9ab&chksm=9b3f64d8ac48edcec70384cf5c6a91224d0f7841ce3a7cfcade6513500c13673a6695d6f0299&scene=21#wechat_redirect>)

单细胞文献阅读：[Biomamba助推的第二篇文章!发表了！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489823&idx=1&sn=6a5dddd53870395316d2b2e904c6ce72&chksm=9b3f604fac48e959e97e4b0317643efdcf117da7f8b75f1edbcd64dd8e2f07149e6031a94dd4&scene=21#wechat_redirect>)文献阅读（三）、单细胞测序解析糖尿病肾病中肾小球的动态变化
[文献阅读（四）、](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484204&idx=1&sn=ee2119c172e6e917998f3781ed20f550&chksm=9b3f7a7cac48f36a97e3bd13660c34f8001032a87a17e98cccb835de3583bbf2d928128a277e&scene=21#wechat_redirect>)单细胞测序技术解析健康人与T2D患者的胰岛差异[文献阅读（六）、](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484204&idx=1&sn=ee2119c172e6e917998f3781ed20f550&chksm=9b3f7a7cac48f36a97e3bd13660c34f8001032a87a17e98cccb835de3583bbf2d928128a277e&scene=21#wechat_redirect>)小鼠全肾单细胞测序开篇之作[文献阅读（七）、](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484204&idx=1&sn=ee2119c172e6e917998f3781ed20f550&chksm=9b3f7a7cac48f36a97e3bd13660c34f8001032a87a17e98cccb835de3583bbf2d928128a277e&scene=21#wechat_redirect>)一篇不花钱就能白嫖的文章[文献阅读（八）、不会吧不会吧，Nature都能白嫖？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484204&idx=1&sn=ee2119c172e6e917998f3781ed20f550&chksm=9b3f7a7cac48f36a97e3bd13660c34f8001032a87a17e98cccb835de3583bbf2d928128a277e&scene=21#wechat_redirect>)[文献阅读（十一）、高氧下小鼠肺发育损伤的ScRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485097&idx=1&sn=6e3e63fff6f26332b6a8b393608686d9&chksm=9b3f7ff9ac48f6efc5477c57f3ab38e6c7dbd48b503a731cb08ac5f430fdab98d0d7e21da11a&scene=21#wechat_redirect>)[文献阅读（十二）、IgAN & STRT-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485376&idx=1&sn=02e228d0993d8a653c8bb1d531021cdb&chksm=9b3f7e90ac48f78686d6d5953aeb192db4f28bf577dbebd76d9fabbe797f135b7fb08fb42867&scene=21#wechat_redirect>)
[文献阅读（十三）、老树开新花——EGFR、肿瘤、免疫+scRNA-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486192&idx=1&sn=6b40bb3bb1ef590a477514a4400f4642&chksm=9b3f73a0ac48fab6044850ae09b4e340f08b1b19e2c180ae1c25808104886fc544311d167396&scene=21#wechat_redirect>)
[文献阅读（十五）、癌前基质细胞驱动BRCA1肿瘤发生](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486417&idx=1&sn=5dfa5b46e7626a1d3e327cb4fc3df3d5&chksm=9b3f7281ac48fb9721b5ac0b8fd323a44018ba9d3ff3a872be2c36f141c2e02f9761df95708e&scene=21#wechat_redirect>)[文献阅读（十八）、紧跟生信"钱"沿,胰腺癌&免疫多模态图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489045&idx=1&sn=29feb00f094a9a7e20418b22aa54dd8c&chksm=9b3f6f45ac48e653d4223838eb1d96e65e5ee51ac3f7782841d9b33013bdb67b5e22e9599fac&scene=21#wechat_redirect>)
[文献阅读（十九）、原发头颈癌和肿瘤转移微生态](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489511&idx=1&sn=76ec706ebd97e3edd08687f5cf3b6816&chksm=9b3f6eb7ac48e7a10bb81aec5332ecc0544a683f576ea680c8baa621e504816bf65c7d331bdf&scene=21#wechat_redirect>)
[文献阅读（二十一）、肾脏疾病&代谢&核受体ESRRA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490575&idx=1&sn=b931a1d50ddcfc4e34999763139695a0&chksm=9b3f655fac48ec49eb2fb01ce8acb15e230091ab3c29ce1471747850be5dae54dbe97fd103b0&scene=21#wechat_redirect>)[文献阅读（二十二）、PD-1&急性髓细胞性白血病&T Cell](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490929&idx=1&sn=82bf93ccbd9dd906caad8ec709c86153&chksm=9b3f6421ac48ed37117794e7c5b878fa78760627e8bced9c37a2c7c67fd8afd58d0cf0add17e&scene=21#wechat_redirect>)

单细胞注释复写[单细胞注释复写(一):Human Fetal Kidney](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447&scene=21#wechat_redirect>)[单细胞注释复写（二）: human colorectal](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491642&idx=1&sn=2246fb702277ddc690f056fc8854142e&chksm=9b3c996aac4b107c059a403978eca7be1ae7987659626272c58430910ad75892ad470517aefb&scene=21#wechat_redirect>)

非技术帖：[关于单细胞的事 谈谈后面的计划](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484798&idx=1&sn=120eada9b02ea2f81f93cd4cfa5eb964&chksm=9b3f7c2eac48f538e2f95166dbe576b029dcb3ad7d321a4d9f346c9a51416d777f4cffb9aa84&scene=21#wechat_redirect>)[趁机预告一波](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485614&idx=1&sn=f63ab5d759bdcb933f334be6333f9493&chksm=9b3f71feac48f8e8cece92812e0c26d7c03130359451a89ce7db22b7022506371269e1fc2af0&scene=21#wechat_redirect>)[有关提高"Biomamba 生信基地"运行效率事宜](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486435&idx=1&sn=c61124eb7c0fd6cc0eaefb639b551092&chksm=9b3f72b3ac48fba5c0091fd843c98d504d4aefe0ba01a2fed966f897f58d8924ace8df07955e&scene=21#wechat_redirect>)
[生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489314&idx=1&sn=fe66765836fe0d7b3450b30117415ce8&chksm=9b3f6e72ac48e7642725b22bafbece9c37277f56e3958be57d9702240c3b63dbeb1aedf61cf9&scene=21#wechat_redirect>)

![](../../images/56869e2cc75aa830.png)

如何联系我们

![](../../images/7c0febec2249cfa6.gif)公众号后台中消息更新不及时，超过48h后便不允许回复读者消息，这里给大家留一下领取资料、免费服务器的**微信号** ，方便大家随时交流、提建议（由助理接待）。此外呼声一直很高的交流群也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490936&idx=1&sn=850dfc45b10a6bd538c81cfbf1d7af37&chksm=9b3f6428ac48ed3e4199dbfdec2fce4324d3226af19e335b8e5c0143cf8f0881667e36074d83&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](../../images/fdb4c49c78e6216c.webp)
