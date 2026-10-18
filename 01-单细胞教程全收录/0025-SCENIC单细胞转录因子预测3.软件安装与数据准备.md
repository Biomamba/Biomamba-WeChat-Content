---
title: "SCENIC单细胞转录因子预测|3.软件安装与数据准备"
date: 2023-06-17
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de#rd
albums: ["单细胞教程全收录"]
---

# SCENIC单细胞转录因子预测|3.软件安装与数据准备

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de#rd
> 合集：单细胞教程全收录

**写在前面** SCENIC全称Single Cell rEgulatory Network Inference and Clustering，就像字面意思那样，其功能为单细胞调控网络的推断与聚类。本次内容我们先与大家一起做好准备工作，完成软件安装、数据库文件与输入文件的准备工作。测试数据和学习手册可在之前的推送中获取：[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)最近下载的同学比较多，网络拥挤时建议在订阅链接中获取资料，百度云链接会更稳定一些，没有波峰波谷影响：[2023年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497382&idx=1&sn=95586ea6dc381f8b8941cbd50f914c34&chksm=9b3c8ff6ac4b06e0a44df58181c3c85ea856fbc1b02e819640f7d9963fb598a4c4abb84f000f&scene=21#wechat_redirect>)
**视频教程**

B站同步播出：

https://www.bilibili.com/video/BV1Mg4y1c7wU?p=3

**图文教程**

# 一、SCENIC

`SCENIC`全称Single Cell rEgulatory Network Inference and Clustering，就像字面意思那样，功能是单细胞调控网络的推断与聚类(不过**rEgulatory** 首字母取E真是。。。)，主要用于计算单细胞测序中的基因调控网络及与细胞类型间的联系
能翻的读者可以翻出去看看官方教程，#这个工作也是被发表在了《Natrue method》上：Aibar, S., González-Blas, C., Moerman, T. et al. SCENIC: single-cell regulatory network inference and clustering. Nat Methods 14, 1083–1086 (2017).
该软件包拥有`R`与`python`两个版本，按照作者的推荐，除非你对`R`和可视化有很深的执念（比如我这种不太懂`python`和`Nextflow` ），否则的话还是推荐各位使用`python`的版本，毕竟Python的计算能力更强,占用的硬件资源也更少（但可视化的功能基本等于没有）。

## 1.1 构建基因调控网络(GRN)

计算转录因子(TF)靶基因的共表达情况,保留共表达的靶基因矩阵，并构建TF的共表达模型，由`GENIE3/GRNBoost`实现。
通过DNA-motif分析选择TF潜在直接结合的靶点(regulon)，由`RcisTarget`实现

## 1.2 通过**regulon** 判定细胞状态

计算每个细胞的GRN活性，由`AUCell`实现，AUCell完整教程已更：[单细胞基因集评分之AUCell](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&chksm=9b3c99e1ac4b10f7ca158561e96fec76a49ff32b8412cb146ed3fb7aa9260c75172b4eb16f9a&scene=21#wechat_redirect>)。通过一定的阈值将`AUCell score`的连续性矩阵转换为二元矩阵(on/off)，根据矩阵可进一步解释生物学意义。

# 二、准备步骤

## 2.1 安装

### 2.1.1 装包

`SCENIC`的workflow主要依赖三个R包的支持：
1、`GENIE3`：用于共表达网络的计算(也可以用`GRNBoost2`替代)
2、`RcisTarget`：转录因子结合motif的计算
3、`AUCell`：识别单细胞测序数据中的激活基因集(gene-network)
安装下面的包可能会花费大量的时间，可能要解决很多环境依赖问题、包的版本问题，当然，我在服务器中也已经给大家布置好了，可以申请免费的用一用[有root权限的共享服务器,注册即送200￥](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499707&idx=1&sn=1b1bb35069f6a86e50bc0866a22502b7&chksm=9b3c86ebac4b0ffd55d3cd9d8247eab6110481f1bf53e7fede84c0db29366910df8bd79dcc41&scene=21#wechat_redirect>)

```r
#安装是个永恒的难题，我在window中BiocManager==1.30.16,R==4.0.6以及本篇的sessionInfo环境下安装是没有问题的
#在Linux中如果你对conda比较熟悉那么也很好安装
if (!requireNamespace("BiocManager", quietly = TRUE))install.packages("BiocManager")
BiocManager::version()
#当你的bioconductor版本大于4.0时
if(!require(SCENIC))BiocManager::install(c("AUCell", "RcisTarget"),ask = F,update = F);BiocManager::install(c("GENIE3"),ask = F,update = F)#这三个包显然是必须安装的

### 可选的包：
#AUCell依赖包
if(!require(SCENIC))BiocManager::install(c("zoo", "mixtools", "rbokeh"),ask = F,update = F)
###t-SNEs计算依赖包:
if(!require(SCENIC))BiocManager::install(c("DT", "NMF", "ComplexHeatmap", "R2HTML", "Rtsne"),ask = F,update = F)

# #这几个包用于并行计算，很遗憾，Windows下并不支持，所以做大量数据计算时最好转战linux：
if(!require(SCENIC))BiocManager::install(c("doMC", "doRNG"),ask = F,update = F)
#可视化输出

# To export/visualize in http://scope.aertslab.org
if (!requireNamespace("devtools", quietly = TRUE))install.packages("devtools")
if(!require(SCopeLoomR))devtools::install_github("aertslab/SCopeLoomR", build_vignettes = TRUE)#SCopeLoomR用于获取测试数据

if (!requireNamespace("arrow", quietly = TRUE)) BiocManager::install('arrow')
#这个包不装上在runSCENIC_2_createRegulons那一步会报错，提示'dbs'不存在
library(SCENIC)#这就安装好了，试试能不能正常加载

if(!require(SCENIC))devtools::install_github("aertslab/SCENIC")
packageVersion("SCENIC")#这里我安装的是1.3.1
library(SCENIC)

#bioconductor版本小于4.0或你的R（3.6）的版本也比较老，你可能得试试下面的方法进行安装
devtools::install_github("aertslab/SCENIC@v1.1.2")
devtools::install_github("aertslab/AUCell")
devtools::install_github("aertslab/RcisTarget")
devtools::install_github("aertslab/GENIE3")
```

### 2.1.2 官方手册

```r
vignetteFile <- file.path(system.file('doc', package='SCENIC'), "SCENIC_Running.Rmd")
file.copy(vignetteFile, "SCENIC_myRun.Rmd")
# or:
vignetteFile <- "https://raw.githubusercontent.com/aertslab/SCENIC/master/vignettes/SCENIC_Running.Rmd"
download.file(vignetteFile, "SCENIC_myRun.Rmd")
```

## 2.2 `sessionInfo`

如果有安装失败的情况，第一件事是检查报错提示信息，第二件事就是检查环境是否与我一致

```
sessionInfo()
```
```
## R version 4.2.1 (2022-06-23)
## Platform: x86_64-pc-linux-gnu (64-bit)
## Running under: Ubuntu 20.04.4 LTS
##
## Matrix products: default
## BLAS:   /usr/lib/x86_64-linux-gnu/blas/libblas.so.3.9.0
## LAPACK: /usr/lib/x86_64-linux-gnu/lapack/liblapack.so.3.9.0
##
## locale:
##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C
##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8
##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8
##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C
##  [9] LC_ADDRESS=C               LC_TELEPHONE=C
## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C
##
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base
##
## loaded via a namespace (and not attached):
##  [1] bslib_0.4.1         jquerylib_0.1.4     pillar_1.8.1
##  [4] compiler_4.2.1      tools_4.2.1         digest_0.6.30
##  [7] jsonlite_1.8.3      evaluate_0.15       lifecycle_1.0.3
## [10] tibble_3.1.8        gtable_0.3.1        pkgconfig_2.0.3
## [13] rlang_1.0.6         cli_3.4.1           DBI_1.1.3
## [16] rstudioapi_0.13     yaml_2.3.6          xfun_0.31
## [19] fastmap_1.1.0       stringr_1.5.0       dplyr_1.0.10
## [22] knitr_1.39          sass_0.4.4          generics_0.1.3
## [25] vctrs_0.5.1         airports_0.1.0      hms_1.1.2
## [28] grid_4.2.1          tidyselect_1.2.0    glue_1.6.2
## [31] R6_2.5.1            fansi_1.0.3         rmarkdown_2.14
## [34] openintro_2.3.0     usdata_0.2.0        ggplot2_3.3.6
## [37] readr_2.1.2         tzdb_0.3.0          magrittr_2.0.3
## [40] scales_1.2.1        htmltools_0.5.3     ellipsis_0.3.2
## [43] assertthat_0.2.1    colorspace_2.0-3    utf8_1.2.2
## [46] stringi_1.7.8       munsell_0.5.0       cachem_1.0.6
## [49] cherryblossom_0.1.0
```

## 2.3 测试数据

### 2.3.1 从测试数据中提取表达矩阵与注释信息

输入数据的表达矩阵为**gene-summarized counts** ，不同于其他进阶分析的是，输入的数据最好是**raw counts** 或**normalized counts** 。计算后的**TPM** 或**FPKM/RPKM** 之类也是允许的, 但是这些可能会导致人为的**共变量** 引入，避免节外生枝，我还是推荐用raw count。但总的来说， **raw (logged) UMI counts** , **normalized UMI counts** , 和**TPM** 都能产生值得信赖的效果
form`loom`

```r
loomPath <- system.file(package="SCENIC", "examples/mouseBrain_toy.loom")
library(SCopeLoomR)
```
```
##
## Attaching package: 'SCopeLoomR'
```
```
## The following object is masked from 'package:base':
##
##     flush
```

```r
loom <- open_loom(loomPath)#获取loom文件
exprMat <- get_dgem(loom)#取出表达信息
class(exprMat)
```
```
## [1] "matrix" "array"
```

```
exprMat[1:4,1:4]
```
```
##          1772066100_D04 1772063062_G01 1772060224_F07 1772071035_G09
## Arhgap18              0              0              0              0
## Apln                  0              0              0              0
## Cnn3                  0              0              0              0
## Eya1                  0              0              0              4
```

```r
cellInfo <- get_cell_annotation(loom)#获得注释信息
cellInfo[1:4,1:3]
```
```
##                        CellType nGene nUMI
## 1772066100_D04     interneurons   170  509
## 1772063062_G01 oligodendrocytes   152  443
## 1772060224_F07        microglia   218  737
## 1772071035_G09    pyramidal CA1   265 1068
```

```
close_loom(loom)
```

上面我们说了如何从`loom`中读取表达矩阵与注释信息，而Python版的SCENIC是推荐使用loom作为输入数据的,这里教大家如何利用表达矩阵和注释信息创建`loom`文件(to `loom`)

```
dir.create("data")
```
```
## Warning in dir.create("data"): 'data' already exists
```

```r
loom <- build_loom("data/mouseBrain.loom", dgem=exprMat)
```
```
## [1] "Adding global attributes..."
## [1] "Adding matrix..."
##
  |
  |                                                                      |   0%
  |
  |======================================================================| 100%[1] "Adding column attributes..."
## [1] "Adding default metrics nUMI..."
## [1] "Adding default metrics nGene..."
```
```
## Warning in doTryCatch(return(expr), name, parentenv, handler): No default
## embedding set for the loom. You'll not be able to visualize it in SCope.
```
```
## [1] "Adding row attributes..."
## [1] "Adding columns graphs..."
## [1] "Adding row graphs..."
## [1] "Adding layers..."
```

```r
loom <- SCENIC::add_cell_annotation(loom, cellInfo)
```
```
## Warning in SCENIC::add_cell_annotation(loom, cellInfo): Columns 'nGene' and
## 'nUMI' will not be added as annotations to the loom file.
```

```
close_loom(loom)
```

`seurat`对象怎么取类推就好啦

```r
singleCellMatrix <- Seurat::Read10X(data.dir="filtered_gene_bc_matrices/hg19/")
exprMat <- as.matrix(scRNAsub@assays$RNA@counts)
cellInfo <- as.data.frame(scRNAsub@meta.data)
```

`SingleCellExperiment`也是一个单细胞数据分析的利器，以后有机会我们也出个教程

```r
library(SingleCellExperiment)
## Get data from sce object:
exprMat <- counts(sce)
cellInfo <- colData(sce)
```

**GEO** ，说实话我还真没这样从GEO下载过数据

```r
#这次的数据来自于GSE60361
# dir.create("SCENIC_MouseBrain"); setwd("SCENIC_MouseBrain") # if needed
# (This may take a few minutes)
if (!requireNamespace("GEOquery", quietly = TRUE)) BiocManager::install("GEOquery");library(GEOquery)
geoFile <- getGEOSuppFiles("GSE60361", makeDirectory=F)
gzFile <- grep("Expression", basename(rownames(geoFile)), value=TRUE)
gzFile#压缩文件名
txtFile <- gsub(".gz", "", gzFile)
txtFile#解压缩后的文件名
gunzip(gzFile, destname=txtFile, remove=TRUE)#解压缩

library(data.table)
geoData <- fread(txtFile, sep="\t")
geoData[1:4,1:4]
geneNames <- unname(unlist(geoData[,1, with=FALSE]))
geneNames[1:5]
exprMatrix <- as.matrix(geoData[,-1, with=FALSE])
exprMatrix[1:4,1:4]
rm(geoData)
dim(exprMatrix)
rownames(exprMatrix) <- geneNames
exprMatrix <- exprMatrix[unique(rownames(exprMatrix)),]
exprMatrix[1:5,1:4]

file.remove(txtFile)#不留下垃圾
```

如果你无法正常运行上面的命令

```
#可以尝试在R语言里download.file
download.file('https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60361/suppl/GSE60361_C1-3005-Expression.txt.gz','Expression.txt.gz')
download.file('https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60361/suppl/GSE60361_spikes_annotation_and_abundance.xlsx','GSE60361_spikes_annotation_and_abundance.xlsx')
#但是我个人感觉linux里的wget更稳定
system('wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60361/suppl/GSE60361_C1-3005-Expression.txt.gz > GSE60361_C1-3005-Expression.txt.gz')
#但是我个人感觉linux里的wget更稳定
system('wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE60nnn/GSE60361/suppl/GSE60361_spikes_annotation_and_abundance.xlsx > GSE60361_spikes_annotation_and_abundance.xlsx')
```

从`AUCell`中读取注释信息

```r
cellLabels <- paste(file.path(system.file('examples', package='AUCell')), "mouseBrain_cellLabels.tsv", sep="/")
cellLabels <- read.table(cellLabels, row.names=1, header=TRUE, sep="\t")
cellInfo <- as.data.frame(cellLabels)
colnames(cellInfo) <- "CellType"
saveRDS(cellInfo,'int/cellInfo.rds')
```

### 2.3.2 保存输入数据

```r
saveRDS(cellInfo, file="int/cellInfo.Rds")
# Color to assign to the variables (same format as for NMF::aheatmap)
colVars <- list(CellType=c("microglia"="forestgreen",
                           "endothelial-mural"="darkorange",
                           "astrocytes_ependymal"="magenta4",
                           "oligodendrocytes"="hotpink",
                           "interneurons"="red3",
                           "pyramidal CA1"="skyblue",
                           "pyramidal SS"="darkblue"))
colVars$CellType <- colVars$CellType[intersect(names(colVars$CellType), cellInfo$CellType)]
saveRDS(colVars, file="int/colVars.Rds")
plot.new(); legend(0,1, fill=colVars$CellType, legend=names(colVars$CellType))#查看保存了哪些细胞类型
```

![](../../images/a5b380600f6ad267.jpg)

## 2.4 **RcisTarget** 数据库

### 2.4.1 文件获取

SCENIC的运行需要依赖**RcisTarget** 数据库的内置数据用于`motif rankings`(score the motifs in the promoter of the genes)，这个内置数据集比较难下载(可能会收到长城的影响，大家可以选择可选上网)，如果不下载完全，运行`initializeScenic`时可能会报错或崩溃，运行`runGenie3()`时会导致R直接崩溃闪退，我们已经给大家下载好且生成了md5值供大家下载，可在往期推送中获取：
[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)

以上文件下载后请记得进行`md5`校验，教程可参考我们的`Linux`课程：[Linux| 22. (解)压缩与md5值校验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499888&idx=1&sn=9b27a668e5b050952ee44a01074bac23&chksm=9b3cb920ac4b3036743dcad804419044ec2da5e8ec8cf7bd9b294be1095cdc25d2ce992fbd2e&token=280235370&lang=zh_CN&scene=21#wechat_redirect>)

对自己网络有信心的可以按下面的网址自己试试: 懂linux的也可以这么下：https://resources.aertslab.org/cistarget/help.html 下完最好检查一下md5：

https://resources.aertslab.org/cistarget/databases/sha256sum.txt

**cisTarget** 数据库文件(目前构建好的物种有 _drosophila melanogaster/_ ,  _homo sapiens/_ ,  _mus_musculus/_)。
虽然目前支持的物种只有三个，但是可以参考这个方法构建自己所需物种的cisTarget database，这样就约等于SCENIC可以支持所有物种。

```r
#地址
#human：
dbFiles <- c("https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg19/refseq_r45/mc9nr/gene_based/hg19-500bp-upstream-7species.mc9nr.feather",
             "https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg19/refseq_r45/mc9nr/gene_based/hg19-tss-centered-10kb-7species.mc9nr.feather")

#mouse：
dbFiles <- c("https://resources.aertslab.org/cistarget/databases/mus_musculus/mm9/refseq_r45/mc9nr/gene_based/mm9-500bp-upstream-7species.mc9nr.feather",
             "https://resources.aertslab.org/cistarget/databases/mus_musculus/mm9/refseq_r45/mc9nr/gene_based/mm9-tss-centered-10kb-7species.mc9nr.feather")

#fly：
dbFiles <- c("https://resources.aertslab.org/cistarget/databases/drosophila_melanogaster/dm6/flybase_r6.02/mc8nr/gene_based/dm6-5kb-upstream-full-tx-11species.mc8nr.feather")

#下载

dir.create("cisTarget_databases"); setwd("cisTarget_databases")
for(featherURL in dbFiles)
{
  download.file(featherURL, destfile=basename(featherURL)) # saved in current dir
}
```

### 2.4.2 **RcisTarget** 数据库文件初始化

这一步相当于给上面下好的文件构建索引并设置一些默认参数

```r
### Initialize settings
library(SCENIC)
scenicOptions <- initializeScenic(org="mgi",#mouse填'mgi', human填'hgnc',fly填'dmel')
dbDir="cisTarget_databases/mouse/mouse.mm9/", nCores=8)#这里可以设置并行计算
```
```
## Motif databases selected:
##   mm9-500bp-upstream-7species.mc9nr.feather
##   mm9-tss-centered-10kb-7species.mc9nr.feather
```
```
## Using the column 'features' as feature index for the ranking database.
## Using the column 'features' as feature index for the ranking database.
```

```r
scenicOptions@inputDatasetInfo$cellInfo <- "int/cellInfo.Rds"
saveRDS(scenicOptions, file="int/scenicOptions.Rds")
```

[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497842&idx=1&sn=5d109d3cfc74c64c4499fce90febeabb&chksm=9b3c8122ac4b0834157220d5c21f1f88dfa7a4eeb5ff44454df126b75648e41a8621833fb8e2&scene=21#wechat_redirect>)

**往期回顾**

[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)

[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)

**参考**

[1]Aibar S, González-Blas CB, Moerman T, Huynh-Thu VA, Imrichova H, Hulselmans G, Rambow F, Marine JC, Geurts P, Aerts J, van den Oord J, Atak ZK, Wouters J, Aerts S. SCENIC: single-cell regulatory network inference and clustering. Nat Methods. 2017 Nov;14(11):1083-1086. doi: 10.1038/nmeth.4463. Epub 2017 Oct 9.

[2]https://github.com/aertslab/SCENIC

[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497842&idx=1&sn=5d109d3cfc74c64c4499fce90febeabb&chksm=9b3c8122ac4b0834157220d5c21f1f88dfa7a4eeb5ff44454df126b75648e41a8621833fb8e2&scene=21#wechat_redirect>)

**单细胞系列教程目录**

![](../../images/90fab1387787746b.gif) 单细胞数据分析系列教程：B站视频，先看一遍视频再去看推送操作，建议至少看三遍：https://www.bilibili.com/video/BV1S44y1b76Z/以下的资料都可以在这里订阅：[单细胞数据基础分析学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492295&idx=1&sn=d4e81588c0ac2906849c8bc44d079209&chksm=9b3c9b97ac4b1281ab462f866538f096ba2473a3d1426a27d8d97ccc636bfd081e1ba8934dfd&scene=21#wechat_redirect>)

单细胞测序基础数据分析保姆级教程，代码部分整理在往期推送之中：[手把手教你做单细胞测序数据分析|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&chksm=9b3cb950ac4b30467a082527547b91aec15b7d1f40d44e362894aedeb6a99e014518fa5e4743&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|2.各类数据结构与读取方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499795&idx=2&sn=68e6298eb43633c71939c146d90230ff&chksm=9b3cb943ac4b3055e09739d77e037d679f3d9ec68780d1aa8c592f806fcc8d2322eaee78752d&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|3.单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|4.多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|5.细胞类型注释，从入门到入土](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&chksm=9b3cb8d7ac4b31c19c843810c7fe4341515df8ba6fff86a0ebff9d830edfcd656a29d18011c9&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|6组间差异分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=2&sn=d8c4ebf8f63d12bd2ac8e2607864f322&chksm=9b3cb8beac4b31a824e228b486f0d8dd21a8f4113a0a0bcbaf1b20eaade3a83c9c7c1184010b&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|7基因集富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21#wechat_redirect>)
[Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&scene=21#wechat_redirect>)

SCENIC单细胞转录因子预测：[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)

单细胞图片改造计划：[改造单细胞降维图| 1.DimPlot的探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496162&idx=1&sn=598c2920f7cc0697ee5a1fa6cadaee04&chksm=9b3c88b2ac4b01a415feeebbbec6c4891319439dc8dcdafd33cca7a1222e5adc723ae9d3a73d&scene=21#wechat_redirect>)
[改造单细胞降维图| 2.ggplot2中的DIY](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496239&idx=1&sn=1fe6fd4a7fb88ecc0456b4f5710cb5d6&chksm=9b3c8b7fac4b0269e0abeab951ad6ae0ddd1464dd9d1867280eeb9755fda5ba8f5237d88a7a6&scene=21#wechat_redirect>)
[改造单细胞降维图| 3.3D降维图与动图绘制](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496343&idx=1&sn=8ac1c511e1197e231c628649167bc26f&chksm=9b3c8bc7ac4b02d134495e000f349cdbd75458b429297f858dfd58d1b428d8256b7e5c5075b4&scene=21#wechat_redirect>)

上游fastq文件处理：
[单细胞分析的最上游——处理Fastq文件：cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484923&idx=1&sn=b5876af14fbee68d1e9db4b0f70cd1c8&chksm=9b3f7cabac48f5bdb3aac7d20201d89121a83720b41a10017564fedbb8c4a13df0da92daffd7&scene=21#wechat_redirect>)
[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484937&idx=1&sn=4fe1fa518202bdaf462bb93a2614ed32&chksm=9b3f7f59ac48f64fafaf34bac2c80f06d3a86b6a84ccf12566c7eac25bb71c7edd3d74004cf7&scene=21#wechat_redirect>)[有奖提问,这个smart-Seq2数据实战的比对率为何如此低？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488441&idx=1&sn=dac4efc4a8901a4abb133f9e5c80831e&chksm=9b3f6ae9ac48e3fff5a7112a0127726441ccb9dc2c3369d4a0fe98a2120df991954ff0567732&scene=21#wechat_redirect>)

细胞通讯B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1Ab4y1W7qx?p=1**往期推送**[单细胞测序数据进阶分析—《细胞通讯》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485403&idx=1&sn=e148e2d09556a85333cd9c212a880aaa&chksm=9b3f7e8bac48f79d6288977f3a67ebed5813dfe92e4a227a2e304eb68321771b3511fdaf5ba5&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《细胞通讯》2.1CellChat基础分析教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485680&idx=1&sn=8168685ab9bbf772dce24e8673994033&chksm=9b3f71a0ac48f8b6554aa6f30a81f7e622fd8bf2f6a83701839290b7dd8f1c90343592603413&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《细胞通讯》2.2CellChat多组别分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485706&idx=1&sn=2d39360b41733b0be6f88d2922388507&chksm=9b3f705aac48f94cc478210f7f11d37294156517c489dedb333d8647ca287134a29944f39a3d&scene=21#wechat_redirect>)
[给你们申请到了免费的128GB云服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485734&idx=1&sn=32c75f6d07b49084e518af6d18099e8b&chksm=9b3f7076ac48f9600593b319d2e0b36bf5a62399a9835caa5783ad36fbdec6004e04cb656db9&scene=21#wechat_redirect>)
拟时序分析B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1br4y1x7Hf?p=1**往期推送**[单细胞测序数据进阶分析—《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》3.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487400&idx=1&sn=223a96a245c408c31e2c3c16afac88fc&chksm=9b3f76f8ac48ffee769dc76870e15bbd0275647dcfb9bf21bf499b7eaee86121b254e4b2da54&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》4.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)
[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494479&idx=1&sn=32f39c79c4c9fc07aa829eed49016da3&chksm=9b3c921fac4b1b091efcdd151500b69d19f71d5ca518122af697fc37e87acd915f3be5f63fb8&scene=21#wechat_redirect>)

其他单细胞相关技术贴也在这里：[细胞的数量由誰决定？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484056&idx=1&sn=4967a054f5241ff3a1bd4a6fe9a502b1&chksm=9b3f7bc8ac48f2deca3141461be035deb8658be184d78597af28f8ba2092d12f020768275248&scene=21#wechat_redirect>)[单细胞中应该如何做GSVA？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&chksm=9b3f7c4dac48f55bf1d11337406ab0e1295e8e1731dbac0715eedc99d11beff7f380e42dd49b&scene=21#wechat_redirect>)[答读者问（三）：单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)[答读者问（四）：如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)[答读者问（八）：为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)
[答读者问（十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)
[答读者问（十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析：Loupe Browser](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a&scene=21#wechat_redirect>)
[什么？不做单细胞也能分析细胞类群和免疫浸润？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485798&idx=1&sn=c849bc7a0093af92fc99e13b55842bb2&chksm=9b3f7036ac48f92048d726b38f2dd978d0b0cce779c1a4090aa4da5cb2df3ad30a5c5dbed27e&scene=21#wechat_redirect>)
[答读者问 （十三）查看Seurat对象时的ERROR：type='text'](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)
[各类单细胞对象（数据格式）转换大全（一）](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485925&idx=1&sn=14e08440200f0f5cb4dcc2dc615efeb8&chksm=9b3f70b5ac48f9a37a43cc2a8b2a5e485a3f84b4ef87949dfe99056bc6301b110e80800f6bb1&scene=21#wechat_redirect>)[批量整理好GEO中下载的单细胞数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486045&idx=1&sn=0b6874bcffc8abafb505cabce4c4fc0e&chksm=9b3f730dac48fa1b140ef01c07a7749e69df4fa7d2056deeed0673c668b6246724cd85741125&scene=21#wechat_redirect>)[答读者问 （十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)
[答读者问 （十六）做单细胞测序到底需要多少内存](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487923&idx=1&sn=15043c6d729b0d5493ab875b0e54a259&chksm=9b3f68e3ac48e1f5dae514a01c857f9a56a90e2977dd7862db28d06fe55888cd9bb4afbb14e0&scene=21#wechat_redirect>)[答读者问 （十七）调用的线程越多就算的越快嘛?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488995&idx=1&sn=7140e0d037671542fb37dff3a3c94b28&chksm=9b3f6cb3ac48e5a5f54a02be9e6af9f5a4cf8da1de1770f9035130c84dedf059a024964fc15a&scene=21#wechat_redirect>)
[答读者问（十八）、一个我至少被问过30遍的monocle报错](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25&scene=21#wechat_redirect>)[没有barcode文件的单细胞数据要怎么读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490952&idx=1&sn=364a3941e59e45234795c906a42fc9ab&chksm=9b3f64d8ac48edcec70384cf5c6a91224d0f7841ce3a7cfcade6513500c13673a6695d6f0299&scene=21#wechat_redirect>)
[单细胞基因集评分之AUCell](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&chksm=9b3c99e1ac4b10f7ca158561e96fec76a49ff32b8412cb146ed3fb7aa9260c75172b4eb16f9a&scene=21#wechat_redirect>)
[粉丝来稿|1. Seurat4相较于Seurat3的几点改动](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494516&idx=1&sn=cb2d4e6b182428ce7b98e7fff2e8729a&chksm=9b3c9224ac4b1b32c4fe99758960305c4845395cfe03851d70a0407043ee36250e55d20106fc&scene=21#wechat_redirect>)
[如何加快Seurat的计算速度](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494116&idx=1&sn=f3dc577cbb464779062aada313191a05&chksm=9b3c90b4ac4b19a27a17f958e3437337d5b10b6ba7153e4dd43dedcb4df812d8c6b4d86fe970&scene=21#wechat_redirect>)
[一文搞定单细胞基因集评分](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497831&idx=2&sn=82fa51c76a381fba0b444e9b6b23eb5f&chksm=9b3c8137ac4b0821dfb62e9b365ea3c32abbbd80df42df63181c37ad9ed991c0183c2c7981d8&payreadticket=HCkRKr7R3-O3p5-0VkAwOOfgIXR8STjX9HoZYYWKS3jgJtptsG2Mu4KWI6Pz6cAuCOxiFPM&scene=21#wechat_redirect>)[答读者问（二十）四个单细胞样本只给了一套文件怎么读](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494879&idx=1&sn=c2287ab3684792747dfac53d6704462b&chksm=9b3c958fac4b1c994a4b075c4f8475816e121966fa8c52cb0a2ce8c14987988ab9bdb49bdf69&scene=21#wechat_redirect>)
[人类单细胞测序数据中有哪些以"**-"开头的基因](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495019&idx=1&sn=f52ac22ca1ea47ecddaa3503bdc2c0b6&chksm=9b3c943bac4b1d2d521f7155ce8f499389dade23828017572a84cdce71e5d08d37d74e08512b&scene=21#wechat_redirect>)
[为什么总把分辨率调的很高](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495765&idx=1&sn=2ec5e3e26491e28c92e25c40630bffae&chksm=9b3c8905ac4b0013a23f9cda2cccd67cdf3c4a941bac161e3a15a12ab98cd4e5eca8aeedbe96&scene=21#wechat_redirect>)
[Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495938&idx=1&sn=2258390c97ec14f3cd336defede59cdb&chksm=9b3c8852ac4b01448fd3b84463d5ab6b697495db6ad57746e7f60e32f491547a3e35290c66ee&scene=21#wechat_redirect>)
[答读者问| 22.object 'CsparseMatrix_validate' not found](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496273&idx=1&sn=fd5a92dd7fdc349b1624784ca74b1220&chksm=9b3c8b01ac4b0217cf06d89bfea49c3fa0c9b580957338c0cc8f55ede3e8f65d6d7162ae27e3&scene=21#wechat_redirect>)
[单细胞数据在R中的读取及存储速度太慢怎么办？这个神包来帮你！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=1&sn=11bdf3c7f9042fc03f9ed237a9b9677b&chksm=9b3cb8beac4b31a8bf1d9fb862553ed32ac9a56f4a6e0f2d38c9478132f87327d8c6b6940573&scene=21#wechat_redirect>)
[一文搞定单细胞/空间转录组的WGCNA分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499737&idx=1&sn=b3f6174e1908494692d82ac154ce3218&chksm=9b3c8689ac4b0f9fbb0c8ba42172c702ca978683c4de28f9f56bd8e7764fe114ba9a1b9c7dac&scene=21#wechat_redirect>)

单细胞文献阅读：[测序技术的发展与应用](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495792&idx=2&sn=1aecc80b68f65f8a44a899df524038c0&chksm=9b3c8920ac4b0036b23268331b457a335b22b4fa3aed1db287ab79e7a4613df8d195bd11421a&scene=21#wechat_redirect>)
[一些生物信息学的基本概念](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485069&idx=1&sn=ef5cec9d4eab8807a3929baa5bc203eb&chksm=9b3f7fddac48f6cbfa64b2de8a627dd7c24e102046075840d56930dac3167eda3b6c8e21edae&scene=21#wechat_redirect>)
[Biomamba助推的第二篇文章!发表了！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489823&idx=1&sn=6a5dddd53870395316d2b2e904c6ce72&chksm=9b3f604fac48e959e97e4b0317643efdcf117da7f8b75f1edbcd64dd8e2f07149e6031a94dd4&scene=21#wechat_redirect>)[又来了！Biomamba生信基地助推的第四篇文章!](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492532&idx=1&sn=cddb4691f23defc80b60da231790c53c&chksm=9b3c9ae4ac4b13f2334cc7f6b16eec1d8223800f6ecef71a93cfba21698ac5f4505dbd64f300&scene=21#wechat_redirect>)
[单细胞测序解析糖尿病肾病中肾小球的动态变化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497682&idx=2&sn=7ef49191c5e334bb291ccdaa8ea444ae&chksm=9b3c8e82ac4b079425433938c831d528eddb9237efaca49acbc210e9cd715d057541589dc290&scene=21#wechat_redirect>)
[Cell metabolism| 单细胞测序技术解析健康人与T2D患者的胰岛差异](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=1&sn=b7f8df758bc4d95b88969378c6dfbeee&chksm=9b3c8ea1ac4b07b7c6a0b5023ebf6c8ecd7d34741ab076baa0b564535d1d753bbf9dc5be5290&scene=21#wechat_redirect>)
[Science| 小鼠全肾单细胞测序开篇之作](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=2&sn=554d6a4e1b28b2e5303695fae5942a34&chksm=9b3c8ea1ac4b07b72323ce25cd49474a9228ec1aaa56243f57dca3f2f668dc42ab9cd58dca21&scene=21#wechat_redirect>)
[一篇不花钱就能白嫖的文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497840&idx=2&sn=1dacbfb190e11d2ff104e32f238cf8c4&chksm=9b3c8120ac4b08367bfe3a0dd8d55f21f5d13528826de3144a9a85ce9b1c9f4c710de703edae&scene=21#wechat_redirect>)
[不会吧不会吧，Nature都能白嫖？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=2&sn=caeb8ed06ffd5239b58cebcd90843cf8&chksm=9b3c81dbac4b08cd9eec50978951a1b890ca08edec644ff75205a09ad1f067dff25d6ecb938e&scene=21#wechat_redirect>)
[高氧下小鼠肺发育损伤的ScRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498513&idx=2&sn=79845edf56a3023c59c73403d7b6494b&chksm=9b3c8241ac4b0b57793402686edc8c35aaa3b0959d3096b5122207fbb70ab809d1df5faee0d7&scene=21#wechat_redirect>)
[IgAN & STRT-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485376&idx=1&sn=02e228d0993d8a653c8bb1d531021cdb&chksm=9b3f7e90ac48f78686d6d5953aeb192db4f28bf577dbebd76d9fabbe797f135b7fb08fb42867&scene=21#wechat_redirect>)
[老树开新花—EGFR、肿瘤、免疫+scRNA-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498596&idx=2&sn=8f63f5856cdf90e15f1d19b4cfe6a39e&chksm=9b3c8234ac4b0b221a5d2c417558f0e63f742459c0a3f8c1cbb4cdf74ce25ddcaf0e48f4a7ce&scene=21#wechat_redirect>)
[癌前基质细胞驱动BRCA1肿瘤发生](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498597&idx=2&sn=9f5fee38d0821052c9c6b3753c2b3bed&chksm=9b3c8235ac4b0b238c4902ad7b3944b285baaa0a7ec6f5c7d08a596fdf89735dc7a7afab91f0&scene=21#wechat_redirect>)
[紧跟生信"钱"沿,胰腺癌&免疫多模态图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498668&idx=2&sn=50cb239885bed65d3d3702c813d8e354&chksm=9b3c82fcac4b0beabece692f6e2d89c5fe4adf3a268e2944d8f0df4393cc554de5432086d6c1&scene=21#wechat_redirect>)
[原发头颈癌和肿瘤转移微生态](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498644&idx=2&sn=6293493263eeb2b4bf3f82cf526dea36&chksm=9b3c82c4ac4b0bd2a9f48b1326bbfbf2b8270ab79e5877f9bca21aa7883f60fb9cb235df2c36&scene=21#wechat_redirect>)
[《Cell Metabolism》：肾脏疾病&代谢&核受体ESRRA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498860&idx=2&sn=156afeec25201c7baa880af8daac8c60&chksm=9b3c853cac4b0c2a2ca09f44fd487c6d8d9701cb447f318c89f83a53e1a7b712d6f10ff17c43&scene=21#wechat_redirect>)
[《Nature communication》：PD-1&急性髓细胞性白血病&T Cell](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498862&idx=2&sn=1ba36b54428198104c5168d84aba6c51&chksm=9b3c853eac4b0c2874eee3d90b5a989fdc2b366c40805b5041a6f1a588e99b45be14469bdd56&scene=21#wechat_redirect>)
[单细胞测序揭示鼻咽癌微环境的基质动力学和肿瘤特异性特征](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498926&idx=2&sn=3bbd43812d2dfcbbd9230c8cb50df36b&chksm=9b3c85feac4b0ce8225b6f77eec91ac9c8150bff171ac6874363b2617ccfe6042400777415c3&scene=21#wechat_redirect>)
[《Nature》：MYB调控衰竭性T细胞对检查点抑制的响应](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498939&idx=2&sn=b63958fb8f28af052036f4ffc05e2fc2&chksm=9b3c85ebac4b0cfdf3fda8f7236c50db168de20ff4795db7af9d6a0b45304e3f6fb3ba888694&scene=21#wechat_redirect>)[单细胞都能活检测序了？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493604&idx=1&sn=d0f8738e26a4b1c870d329b6a4a7b689&chksm=9b3c9eb4ac4b17a2d0b04d72c350c20f575701de7179f77fcd3567f4b1533cf35df4157f67e1&scene=21#wechat_redirect>)[文献阅读(二十九)、单细胞测序做到什么程度能毕业|硕士篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493808&idx=1&sn=52c7d330ffdda47c3409d36fe9cbbcd8&chksm=9b3c91e0ac4b18f6edf59d171a0d982b1e3f842148046d8eed19343484feaa84dbd5b7682a11&scene=21#wechat_redirect>)
[文献阅读(三十)、单细胞测序做到什么程度能毕业|博士篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494017&idx=1&sn=a2dc4e2eef2bcdb40f5074b665dfa45f&chksm=9b3c90d1ac4b19c79ac5128f96d27789241357c9745bb0389ff5f79f96ab825d3e1c9b29e3af&scene=21#wechat_redirect>)[2022年了，都有哪些器官/组织有scRNA-Seq数据|小鼠篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494796&idx=1&sn=92c91a65719bdf39658814eb691a780f&chksm=9b3c95dcac4b1cca5547440a5881e650da3ea430bad3e6017cbd2891606b2ec40e3ec343bc0e&scene=21#wechat_redirect>)
[2022年了，都有哪些器官/组织有scRNA-Seq数据|人类篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494806&idx=1&sn=1d15ad9cb4d350a164d3b941bc715233&chksm=9b3c95c6ac4b1cd054cedbd3e8c8f57ee88cc59a6ebda2fd11ba8fea79f5e9e8c65d21ff338c&scene=21#wechat_redirect>)
[2023年了, 都哪些物种有scRNA-Seq数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496958&idx=1&sn=f34c69e2114d99fa25e2524411c028a2&chksm=9b3c8daeac4b04b80a5629433d5eec4d25b8ba7d2a74fa31cd499b98c36601ddfe436e2196eb&scene=21#wechat_redirect>)[终于读到一篇用monocle3做拟时序的文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500192&idx=2&sn=b30f8f489695be29df65dc8b60858264&chksm=9b3cb8f0ac4b31e6561aba7bbaf7305e3bf1ca07acbd21aa16cd50ad6a0909f2fa4bff2d295b&scene=21#wechat_redirect>)
[单细胞转录组+亚细胞空间代谢组=25分文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496126&idx=1&sn=8cb6040a38eb844bb215c0d395196e3a&chksm=9b3c88eeac4b01f8dcb8f4c7a19c5a58841d5fe1623f0a4c585c6dcc281cbbdd2830a1150f6a&scene=21#wechat_redirect>)
[酸了，六个样本的scRNA-Seq+差异分析=9分文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496237&idx=1&sn=646cd85b62d08c1739a532242c8991ba&chksm=9b3c8b7dac4b026be9e65b64df8e830d1c2c882272165e64eec6eb258e4ed5342cf30f42dda5&scene=21#wechat_redirect>)[自测scRNA-Seq+scWGBS=3分三区文章？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498939&idx=1&sn=1b33d219c795f2de8ff66a5c330a3d24&chksm=9b3c85ebac4b0cfd050a7c0abe11dead991a988aa5b790eac6fd57de2f76a85ef2191d8b9ca6&scene=21#wechat_redirect>)
[百万级单细胞多组学数据集成](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499336&idx=1&sn=864c535b38ce630487fccc602d893a80&chksm=9b3c8718ac4b0e0e8a0e2560a83546167a82616d99503606e3ac0ef29e90b01cc762e95d64e6&scene=21#wechat_redirect>)[空间转录组与单细胞转录组整合分析工具大比拼](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500243&idx=1&sn=b0e513e85a202ec7ca4041a700a7ae10&chksm=9b3cb883ac4b3195cffd0398d880468b12dd068f9a9fd96b7d0f8aed8961be34293e6ff4a2bb&scene=21#wechat_redirect>)

单细胞注释复写[单细胞注释复写(一):Human Fetal Kidney](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447&scene=21#wechat_redirect>)[单细胞注释复写(二): human colorectal](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491642&idx=1&sn=2246fb702277ddc690f056fc8854142e&chksm=9b3c996aac4b107c059a403978eca7be1ae7987659626272c58430910ad75892ad470517aefb&scene=21#wechat_redirect>)

非技术帖：[生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489314&idx=1&sn=fe66765836fe0d7b3450b30117415ce8&chksm=9b3f6e72ac48e7642725b22bafbece9c37277f56e3958be57d9702240c3b63dbeb1aedf61cf9&scene=21#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)

![](../../images/56869e2cc75aa830.png)

如何联系我们

![](../../images/7c0febec2249cfa6.gif)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务([有root权限的共享服务器,注册即送200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499707&idx=1&sn=1b1bb35069f6a86e50bc0866a22502b7&chksm=9b3c86ebac4b0ffd55d3cd9d8247eab6110481f1bf53e7fede84c0db29366910df8bd79dcc41&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)
![](../../images/fdb4c49c78e6216c.webp)![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
