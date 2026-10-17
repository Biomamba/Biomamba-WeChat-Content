---
title: "SCENIC单细胞转录因子预测|5.step1+step2构建共表达网络与regulon"
date: 2023-07-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501692&idx=1&sn=3f7e263a93942ad03faa1ba5f8694ec4&chksm=9b3cbe2cac4b373af9db74a50ffb08a9b8a3b958fc6385c937385f0f7323bc935cdb0fe5275c#rd
albums: ["单细胞教程全收录"]
---

# SCENIC单细胞转录因子预测|5.step1+step2构建共表达网络与regulon

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501692&idx=1&sn=3f7e263a93942ad03faa1ba5f8694ec4&chksm=9b3cbe2cac4b373af9db74a50ffb08a9b8a3b958fc6385c937385f0f7323bc935cdb0fe5275c#rd
> 合集：单细胞教程全收录

**写在前面** SCENIC封装的过好([4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>))，可能不利于大家理解每一步的含义，所以我们做一下分解动作。这个过程可能**有些枯燥** ，但对于大家理解程序的执行过程、了解输出结果的含义非常有帮助。
```r
org <- "mgi" # or hgnc, or dmel
dbDir <- 'cisTarget_databases/mouse/mouse.mm9/' # RcisTarget databases location
myDatasetTitle <- "SCENIC example on Mouse brain" # choose a name for your analysis
data(defaultDbNames)
dbs <- defaultDbNames[[org]]
scenicOptions <- initializeScenic(org=org, dbDir=dbDir, dbs=dbs, datasetTitle=myDatasetTitle, nCores=10)
scenicOptions@inputDatasetInfo$cellInfo <- "int/cellInfo.Rds"
scenicOptions@inputDatasetInfo$colVars <- "int/colVars.Rds"
saveRDS(scenicOptions, file="int/scenicOptions.Rds") #这样存起来方便调用
```

`
`

学习手册与测试文件不断更新，可在这里获取([SCENIC.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>))或联系客服微信Biomamba领取。
学习手册：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyu18ShpajyL1fUdXxZSg5wFP3HiaQpNaQ9NbUA3ialKSzu8hQFRUHSgqENUdpDNSl2WAowteMuqe7A/640?wx_fmt=png)

当然更推荐大家去作者的Github学习：https://github.com/aertslab/SCENIC[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497382&idx=1&sn=95586ea6dc381f8b8941cbd50f914c34&chksm=9b3c8ff6ac4b06e0a44df58181c3c85ea856fbc1b02e819640f7d9963fb598a4c4abb84f000f&scene=21#wechat_redirect>)
**视频教程**

B站同步播出：

https://www.bilibili.com/video/BV1Mg4y1c7wU?p=5

https://www.bilibili.com/video/BV1Mg4y1c7wU?p=6
**图文教程**

## 4.1 step.1 共表达网络(**Co-expression network**)计算

通过表达矩阵推断潜在的转录因子作用靶点(`GENIE3`/`GRNBoost`). 需要将过滤后的矩阵、转录因子对应关系作为输入数据,由`runSCENIC_1_coexNetwork2modules()`输出共表达模式.

`GENIE3`, `GRNBoost`, `WGCNA`等都可以用来构建基因共表达网络，这里作者推荐使用`GENIE3`,**GENIE3** 终于不是这个作者写的包了:Inferring Regulatory Networks from Expression Data Using Tree-Based Methods，这里作者推荐的理由是`GENIE3`可以识别数据集中部分存在的非线性关系，并且可以有效应对网络推断中的DREAM5 challenge(Reprogramming of regulatory network using expression uncovers sex-specific gene regulation in Drosophila),缺点就是会占用计算资源和计算时间(3-5k个细胞可能会算几天)。所以为了解决这个问题，作者又写了个包`GRNboost`用于大型数据的计算。
当然你也可以选择从数据中随机提取一些细胞出来参与计算，但这样需要确保抽出的样本能够替代总体，所以这个方法我并不推荐。

### 4.1.1 基因表达矩阵过滤

为了加快计算速度，并且去除数据噪声，`GENIE3/GRNBoost`执行前需要进行一步过滤，去除表达量过低(统计count数，默认删除低于`3 X 0.1 X 数据集细胞数量`的基因，即细胞数为200，删除count低于6的基因)或表达比例过低的基因(统计表达该基因的细胞数，默认删除表达比例不足`1%`的基因)。这里为了防止一些在特定细胞类型中表达的基因被误删，这里的`1%`推荐设置的比数据中最小的细胞群比例更小。在初步过滤后，矩阵中能够被**RcisTarget databases** 收录的基因被保留用于下游计算。

```r
genesKept <- geneFiltering(exprMat, scenicOptions=scenicOptions,
                           minCountsPerGene=3*.01*ncol(exprMat),
                           minSamples=ncol(exprMat)*.01)#获得能经过“质检”的基因
```
```
## Maximum value in the expression matrix: 421
```
```
## Ratio of detected vs non-detected: 0.24
```
```
## Number of counts (in the dataset units) per gene:
```
```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
##     0.0    17.0    48.0   146.8   137.0  5868.0
```
```
## Number of cells in which each gene is detected:
```
```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
##    0.00   10.00   25.00   39.01   60.00  180.00
```
```
##
## Number of genes left after applying the following filters (sequential):
```
```
##  771 genes with counts per gene > 6
```
```
##  770 genes detected in more than 2 cells
```
```
## Using the column 'features' as feature index for the ranking database.
```
```
##  770 genes available in RcisTarget database
```
```
## Gene list saved in int/1.1_genesKept.Rds
```

```r
exprMat_filtered <- exprMat[genesKept,]#取出过滤后的矩阵
dim(exprMat_filtered)
```
```
## [1] 770 200
```

### 4.1.2 计算转录因子与靶基因的相关性

默认是`Spearman correlation`，并且正相关与负相关都会被考虑

```
runCorrelation(exprMat_filtered, scenicOptions)
```

### 4.1.3 `GENIE3`

`GRNBoost`需要在Python中运行，可以通过`exportsForGRNBoost`输出`GRNBoost`所需数据。
`GENIE3`的输出数据即上面已被过滤过的`exprMat_filtered`、`RcisTarget`中提供的转录因子与靶基因的对应关系以及`scenicOptions`中存放的其它已设定参数。
由于`GENIE3`采取的是随机森林算法(`Random Forest approach`)，所以即使是相同的数据和程序，运行多次得到的结果也可能是不同的，`ntrees`参数越高、结果的变化程度就越低，这里为了保证结果具有可重复性，应当用`set.seed()`函数设置随机数种子。
`runGenie3`在大家运行真实的数据集时，这一步可能会花费数小时甚至数天，因此我不是很推荐在Rstudio-server中运行这一步，我的建议是通过`nohup`把命令提交到`Linux`后台运行。

```r
mymethod <- 'R'
library(reticulate)
if(mymethod=='R'){
  # R语言版：
  runGenie3(exprMat_filtered_log, scenicOptions)
}else{
  # 调用python参与计算：
  arb.algo = import('arboreto.algo')
  tf_names = getDbTfs(scenicOptions)
  tf_names = Seurat::CaseMatch(
    search = tf_names,
    match = rownames(exprMat_filtered))
  adj = arb.algo$grnboost2(
    as.data.frame(t(as.matrix(exprMat_filtered))),
    tf_names=tf_names, seed=2023L
    )
  colnames(adj) = c('TF','Target','weight')
saveRDS(adj,file=getIntName(scenicOptions,
                            'genie3ll'))
  }
```
```
## Using 8 TFs as potential regulators...
```
```
## Warning in runGenie3(exprMat_filtered_log, scenicOptions): Only 8 (0%) of the 1721 TFs in the database were found in the dataset. Do they use the same gene IDs?
```
```
## Running GENIE3 part 1
```
```
## Running GENIE3 part 10
```
```
## Running GENIE3 part 2
```
```
## Running GENIE3 part 3
```
```
## Running GENIE3 part 4
```
```
## Running GENIE3 part 5
```
```
## Running GENIE3 part 6
```
```
## Running GENIE3 part 7
```
```
## Running GENIE3 part 8
```
```
## Running GENIE3 part 9
```
```
## Finished running GENIE3.
```

## 4.2. step.2 构建基因调控网络(Gene regulatory network, GRN):

`scenicOptions`的默认参数可以如是调整

```r
library(SCENIC)
scenicOptions <- readRDS("int/scenicOptions.Rds")#读取初始化设置
scenicOptions@settings$verbose <- TRUE#运行过程中是否保留进度条
scenicOptions@settings$nCores <- 10#并行计算时调用的线程
scenicOptions@settings$seed <- 123#涉及随机数种子便于重复结果

scenicOptions@settings$dbs <- scenicOptions@settings$dbs["10kb"] #这里是做示例运行时取子集用于加速，正式运行时应删除
```

###

### 4.2.1 获取共表达网络：
```r
scenicOptions <- runSCENIC_1_coexNetwork2modules(scenicOptions)
```
```
## 02:19    Creating TF modules
```
```
## Number of links between TFs and targets (weight>=0.001): 6139
```
```
##            [,1]
## nTFs          8
## nTargets    770
## nGeneSets    47
## nLinks    17299
```

### 4.2.2 通过`RcisTarget`获得regulons信息(TF motif analysis)

```r
#这一步大家无需运行，我们下面要做拆解
scenicOptions <- runSCENIC_2_createRegulons(scenicOptions, coexMethod=c("top5perTarget")) #coexMethod参数用于加速运行，正式运行时应删除
```

```r
scenicOptions <- readRDS("int/scenicOptions.Rds")#读取初始化信息
minGenes=20
coexMethod=NULL#正式运行数据时coexMethod不应选择'top5perTarget'
```

上面的`runSCENIC_2_createRegulons`与下面的`runSCENIC_3_scoreCells`封装了很多步功能，因此我们需要重点关注加以拆解，从而了解整个流程的步骤与原理，并能够更好的解读分析结果：

```
vignette("detailedStep_2_createRegulons", package="SCENIC")#这行可以获得runSCENIC_2_createRegulons的详细信息:
```

这一步是为了通过DNA motif的富集分析从而鉴别TF直接的靶点(regulons)，其实上面的共表达分析已经能够初步为基因调控网络提供信息，但是**Biomamba** 在此前的很多推送都强调过，相关性分析并不能代表最终的因果，因此共表达矩阵中可能存在着间接作用的基因(例如直接作用靶基因的下游基因)。那么为了找到真正的regulons，这里利用`RcisTarget`数据库收录的信息进行顺势调控元件分析(cis-regulatory motif analysis)

(1)加载共表达模块`RcisTarget`数据库

```r
nCores <- getSettings(scenicOptions, "nCores")
nCores
```
```
## [1] 8
```

```r
tfModules_asDF <- loadInt(scenicOptions, "tfModules_asDF")
head(tfModules_asDF)
```
```
##    Target   TF method corr
## 1    Dlx5 Dlx1 w0.001    1
## 2    Gad2 Dlx1 w0.001    1
## 3    Gad1 Dlx1 w0.001    1
## 4   Bmper Dlx1 w0.001    1
## 5   Gria4 Dlx1 w0.001    1
## 6 St8sia4 Dlx1 w0.001    1
```

```r
if(!is.null(coexMethod)) tfModules_asDF <- tfModules_asDF[which(tfModules_asDF$method %in% coexMethod),]#选择coexMethod
if(nrow(tfModules_asDF)==0) stop("The co-expression modules are empty.")#如果不存在共表达模块，则会报错
```

为RcisTarget::addMotifAnnotation()设置并行线程数

```r
if("BiocParallel" %in% installed.packages()) library(BiocParallel); register(MulticoreParam(nCores), default=TRUE) #设定并行参数
msg <- paste0(format(Sys.time(), "%H:%M"), "\tStep 2. Identifying regulons")#保存程序运行进度信息
if(getSettings(scenicOptions, "verbose")) message(msg)#若设置需要更新进度，则输出程序运行进度信息
```
```
## 02:19    Step 2. Identifying regulons
```

检查物种并加载数据库
```r
if(is.na(getDatasetInfo(scenicOptions, "org"))) stop('Please provide an organism (scenicOptions@inputDatasetInfo$org).')#检查物种名是否正常
library(AUCell)#加载AUCell用于打分
library(RcisTarget)
motifAnnot <- getDbAnnotations(scenicOptions)#按照初始化参数载入数据库
motifAnnot[1:4,1:4]#收录了数据库中的大量信息
```
```
##               motif     TF directAnnotation inferred_Orthology
## 1:   bergman__Abd-B  Hoxa9            FALSE              FALSE
## 2:    bergman__Aef1 Zfp128            FALSE               TRUE
## 3:     bergman__Cf2 Zfp853            FALSE               TRUE
## 4: bergman__EcR_usp  Nr1h2            FALSE               TRUE
```

```r
if(is.null(names(getSettings(scenicOptions, "dbs"))))
{
  names(scenicOptions@settings$"dbs") <- scenicOptions@settings$"dbs"
  tmp <- sapply(strsplit(getSettings(scenicOptions, "dbs"),"-", fixed=T), function(x) x[grep("bp|kb",x)])
  if(all(lengths(tmp)>0)) names(scenicOptions@settings$"dbs") <- tmp
}

loadAttempt <- sapply(getDatabases(scenicOptions), dbLoadingAttempt)
if(any(!loadAttempt)) stop("It is not possible to load the following databses: \n",
                           paste(dbs[which(!loadAttempt)], collapse="\n"))

genesInDb <- unique(unlist(lapply(getDatabases(scenicOptions), function(x)
  names(feather::feather_metadata(x)[["types"]]))))#获取数据库中包含的gene symbol
genesInDb[1:10]
```
```
##  [1] "features"      "0610007C21Rik" "0610007L01Rik" "0610007P08Rik"
##  [5] "0610007P14Rik" "0610007P22Rik" "0610008F07Rik" "0610009B14Rik"
##  [9] "0610009B22Rik" "0610009D07Rik"
```

(2)过滤共表达矩阵
这里选出与TF表达成正相关关系的共表达模块(可能有激活关系)，并将TF加入该模块中，保留至少包含20个基因的共表达模块。同理可以选出与TF表达成正相关关系的共表达模块(可能存在抑制关系)，但在测试数据中这类模块数量较少。

移除**RcisTarget数据库** 中没有收录的基因
```r
#将TF和Target都转换成字符串
tfModules_asDF$TF <- as.character(tfModules_asDF$TF)
tfModules_asDF$Target <- as.character(tfModules_asDF$Target)
allTFs <- getDbTfs(scenicOptions)##获取数据库中收录的转录因子
allTFs[1:10]
```
```
##  [1] "1700009N14Rik"  "1700080O16Rik"  "1810024B03Rik"  "2010315B03Rik"
##  [5] "2310011J03Rik"  "2410141K09Rik"  "2610044O15Rik8" "2810403A07Rik"
##  [9] "3300002I08Rik"  "3830417A13Rik"
```

```r
tfModules_asDF <- tfModules_asDF[which(tfModules_asDF$TF %in% allTFs),]
geneInDb <- tfModules_asDF$Target %in% genesInDb#获取共表达木块中的基因是否数据库中收录的布尔值
geneInDb[1:10]
```
```
##  [1] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE
```

```r
missingGene <- sort(unique(tfModules_asDF[which(!geneInDb),"Target"]))#共表达模块中存在的，但数据库中没有收录的基因，这里不存在这类基因
missingGene
```
```
## character(0)
```

```r
if(length(missingGene)>0)
  warning(paste0("Genes in co-expression modules not available in RcisTargetDatabases: ",
                 paste(missingGene, collapse=", ")))#若missingGene存在则数据warning信息
tfModules_asDF <- tfModules_asDF[which(geneInDb),]#保留包含在数据库中的基因共表达模块
```

取出正向的共表达模块并处理
```r
tfModules_Selected <- tfModules_asDF[which(tfModules_asDF$corr==1),]#tfModules_asDF$corr，是个三元矩阵
# Add a column with the geneSet name (TF_method)
tfModules_Selected <- cbind(tfModules_Selected, geneSetName=paste(tfModules_Selected$TF, tfModules_Selected$method, sep="_"))
head(tfModules_Selected)
```
```
##    Target   TF method corr geneSetName
## 1    Dlx5 Dlx1 w0.001    1 Dlx1_w0.001
## 2    Gad2 Dlx1 w0.001    1 Dlx1_w0.001
## 3    Gad1 Dlx1 w0.001    1 Dlx1_w0.001
## 4   Bmper Dlx1 w0.001    1 Dlx1_w0.001
## 5   Gria4 Dlx1 w0.001    1 Dlx1_w0.001
## 6 St8sia4 Dlx1 w0.001    1 Dlx1_w0.001
```

```r
tfModules_Selected$geneSetName <- factor(as.character(tfModules_Selected$geneSetName))
allGenes <- unique(tfModules_Selected$Target)
```

利用不同的`methods`拆分并加入TF

```r
tfModules <- split(tfModules_Selected$Target, tfModules_Selected$geneSetName)

# Add TF to the gene set (used in the following steps, careful if editing)
tfModules <- setNames(lapply(names(tfModules), function(gsn) {
  tf <- strsplit(gsn, "_")[[1]][1]#_前的字符即为TF名称
  unique(c(tf, tfModules[[gsn]]))
}), names(tfModules))
```

保留基因数量大于`minGenes`的模块

```r
tfModules <- tfModules[which(lengths(tfModules)>=minGenes)]
saveRDS(tfModules, file=getIntName(scenicOptions, "tfModules_forEnrichment"))
print(getIntName(scenicOptions, "tfModules_forEnrichment"))
```
```
## [1] "int/2.1_tfModules_forMotifEnrichmet.Rds"
```

```r
#所以这里保存的就是转录因子及其对应模块包含的基因，其实就相当于做基因集评分时的geneset
if(getSettings(scenicOptions, "verbose")) {
  tfModulesSummary <- t(sapply(strsplit(names(tfModules), "_"), function(x) x[1:2]))
  message("tfModulesSummary:")
  print(sort(table(tfModulesSummary[,2])))#输出每种算法下包含的TF
}
```
```
## tfModulesSummary:
```
```
##
##        top3sd        top1sd         top50 top5perTarget        w0.001
##             5             8             8             8             8
##        w0.005
##             8
```

接下来将用到`RcisTarget`,通过Motif富集分析在共表达网络种识别直接作用靶基因，套娃真的套不动了，更详细的教程可以参考：
```
vignette("RcisTarget")#这里我就不运行了
```
```
## Warning: vignette 'RcisTarget' not found
```

  1. Run `RcisTarget` (Motif enrichment) 简单来说，就是根据`RcisTarget`中的**motif-TF** 数据库找到**TF** 对应的**motif**(在TSS附近检索，与基因组上其它基因做对比)，并对来源于同一个TF的motif进行富集分析。

(1).找出高表达的motif: 这一步SCENIC会利用一个包含TSS周围(上游的500bp或上下游10kb，设置一个窗口进行扫描评分)motif评分的数据库。Normalized Enrichment Score (NES, 先求出motif的AUCell score，再对其进行normalization) > 3.0 (这样能够保证假阳性率在3%到9%)的motif会被认为是改TF模块中显著富集的motif (并不是基因集中的所有基因都拥有相同富集的motif，所以保留motif分值高者即可，高NES意味着这个motif可以覆盖大量的输入基因)，并通过`addMotifAnnotation()`存在motifEnrichment$TFinDB中(显著的以**标记)。
得到的结果中对于motif的注释有高可信度(一般是被直接记载)与低可信度(一般是由motif的相似度预测得来, 例如**sufix _extended**就代表这是一种低可信度的motif)。

```r
#通过RcisTarget计算富集的motif
msg <- paste0(format(Sys.time(), "%H:%M"), "\tRcisTarget: Calculating AUC")
if(getSettings(scenicOptions, "verbose")) message(msg)#输出进度
```
```
## 02:20    RcisTarget: Calculating AUC
```

```r
motifs_AUC <- lapply(getDatabases(scenicOptions), function(rnkName) {
  ranking <- importRankings(rnkName, columns=allGenes)
  message("Scoring database: ", ranking@description)
  RcisTarget::calcAUC(tfModules, ranking, aucMaxRank=0.03*getNumColsInDB(ranking), nCores=nCores, verbose=FALSE)})
```
```
## Using the column 'features' as feature index for the ranking database.
```
```
## Scoring database:  [Source file: mm9-tss-centered-10kb-7species.mc9nr.feather]
```

```
saveRDS(motifs_AUC, file=getIntName(scenicOptions, "motifs_AUC"))#int/2.2_motifs_AUC.Rds里存的是motif的AUCell值
```

```r
#以NES>3过滤，并注释motif的置信度
# motifs_AUC <- loadInt(scenicOptions, "motifs_AUC") #上一步保存的int/2.2_motifs_AUC.Rds
msg <- paste0(format(Sys.time(), "%H:%M"), "\tRcisTarget: Adding motif annotation")
message(msg)#报进度
```
```
## 02:20    RcisTarget: Adding motif annotation
```

```r
motifEnrichment <- lapply(motifs_AUC, function(aucOutput)
{
  # Extract the TF of the gene-set name (i.e. MITF_w001):
  tf <- sapply(setNames(strsplit(rownames(aucOutput), "_"), rownames(aucOutput)), function(x) x[[1]])

  # Calculate NES and add motif annotation (provide tf in 'highlightTFs'):
  addMotifAnnotation(aucOutput, #AUCell score
                     nesThreshold=3, #NES的阈值，这里是3
                     digits=3, #保留三位小数
                     motifAnnot=motifAnnot,#加入数据库中的注释
                     motifAnnot_highConfCat=c("directAnnotation", "inferredBy_Orthology"),
                     motifAnnot_lowConfCat=c("inferredBy_MotifSimilarity",
                                               "inferredBy_MotifSimilarity_n_Orthology"),
                     highlightTFs=tf#将结果返回在motifEnrichment$tf中
                     )
})
```
```
## Using BiocParallel...
```

```r
#合并各tf的列表，并加入一列'motifDb'
motifEnrichment <- do.call(rbind, lapply(names(motifEnrichment), function(dbName){
  cbind(motifDb=dbName, motifEnrichment[[dbName]])
}))
head(motifEnrichment)#这是个长格式的数据，head也很难看出门道
```
```
##    motifDb     geneSet                                      motif  NES   AUC
## 1:    10kb Dlx1_top1sd                               cisbp__M1205 5.24 0.133
## 2:    10kb Dlx1_top1sd      taipale_cyt_meth__HOXB1_STAATTAN_eDBD 4.96 0.128
## 3:    10kb Dlx1_top1sd                       transfac_pro__M01388 4.72 0.124
## 4:    10kb Dlx1_top1sd taipale_cyt_meth__HOXB1_GTAATTAN_eDBD_meth 4.52 0.121
## 5:    10kb Dlx1_top1sd       taipale_cyt_meth__PDX1_YTAATTAN_eDBD 4.52 0.121
## 6:    10kb Dlx1_top1sd                             stark__RATTAMY 4.47 0.120
##    highlightedTFs TFinDB                                         TF_highConf
## 1:           Dlx1
## 2:           Dlx1                             Hoxb1 (inferredBy_Orthology).
## 3:           Dlx1                                  Dlx5 (directAnnotation).
## 4:           Dlx1                             Hoxb1 (inferredBy_Orthology).
## 5:           Dlx1                              Pdx1 (inferredBy_Orthology).
## 6:           Dlx1        Hoxa4; Hoxb4; Hoxc4; Hoxd4 (inferredBy_Orthology).
##                                                                                                                                                                                                                                                                                             TF_lowConf
## 1:                                                                                 Evx1; Hoxa2; Hoxa3; Hoxd3; Pdx1; Vax1; Vax2 (inferredBy_MotifSimilarity). Emx1; Emx2; Evx2; Gsx1; Gsx2; Hoxa6; Hoxa7; Hoxb2; Hoxb6; Hoxb7; Hoxc6; Lbx1; Lhx2; Lhx9; Noto (inferredBy_MotifSimilarity_n_Orthology).
## 2:                                                                                                                                           Hoxa1; Hoxd3; Meox2 (inferredBy_MotifSimilarity). Hoxa5; Hoxb5; Hoxb7; Hoxc5; Hoxd1; Hoxd4; Lhx4; Meox1; Prop1 (inferredBy_MotifSimilarity_n_Orthology).
## 3:                                                                                                                                                                                                 Hoxd3 (inferredBy_MotifSimilarity). Nkx1-1; Nkx1-2; Vsx1 (inferredBy_MotifSimilarity_n_Orthology).
## 4:                                                                      Hoxa2; Pdx1 (inferredBy_MotifSimilarity). Emx1; Evx1; Evx2; Gm28308; Hoxa1; Hoxa5; Hoxb2; Hoxb5; Hoxd1; Hoxd4; Lhx4; Meox1; Meox2; Mnx1; Nkx1-1; Nkx1-2; Phox2a; Phox2b; Vax1; Vax2 (inferredBy_MotifSimilarity_n_Orthology).
## 5: Emx2; Evx1; Gsx2; Hoxa2; Hoxa3; Hoxa5; Hoxb3; Hoxd3; Vax1; Vax2 (inferredBy_MotifSimilarity). Emx1; En1; Evx2; Gm28308; Gsx1; Hoxa6; Hoxa7; Hoxb2; Hoxb5; Hoxb6; Hoxb7; Hoxc4; Hoxc5; Hoxc6; Hoxd4; Lhx2; Lhx6; Lhx8; Lhx9; Lmx1a; Mnx1; Rax; Vsx1; Vsx2 (inferredBy_MotifSimilarity_n_Orthology).
## 6:
```

```r
saveRDS(motifEnrichment, file=getIntName(scenicOptions, "motifEnrichment_full"))#int/2.3_motifEnrichment.Rds中存放的既是motif富集信息
msg <- paste0("Number of motifs in the initial enrichment: ", nrow(motifEnrichment))
if(getSettings(scenicOptions, "verbose")) message(msg)#报告motif总数
```
```
## Number of motifs in the initial enrichment: 6605
```

```r
# motifEnrichment <- loadInt(scenicOptions, "motifEnrichment_full")#除了readrds，还可以这样读回来

#保留能与现存TF对应的motif
motifEnrichment_selfMotifs <- motifEnrichment[which(motifEnrichment$TFinDB != ""),, drop=FALSE]
msg <- paste0("Number of motifs annotated to the corresponding TF: ", nrow(motifEnrichment_selfMotifs))
if(getSettings(scenicOptions, "verbose")) message(msg)
```
```
## Number of motifs annotated to the corresponding TF: 696
```

```
if(nrow(motifEnrichment_selfMotifs)==0)
  stop("None of the co-expression modules present enrichment of the TF motif: There are no regulons.")
```

  2. 构建**regulon** `RcisTarget`利用类似于GSEA的原理通过`addSignificantGenes()`为每个motif找到高匹配度的基因，将motif、TF、靶基因构建为一个regulon, 这一步的运行速度与基因集的大小有关，不受细胞数量影响。

```r
#Prune targets
msg <- paste0(format(Sys.time(), "%H:%M"), "\tRcisTarget: Prunning targets")#汇报能够注释到对应TF的motif数量
if(getSettings(scenicOptions, "verbose")) message(msg)
```
```
## 02:20    RcisTarget: Prunning targets
```

```r
dbNames <- getDatabases(scenicOptions)
dbNames#这里是测试流程，所以只用到了TSS周围"10kb"的数据文件"mm9-tss-centered-10kb-7species.mc9nr.feather"
```
```
##                                                                                10kb
## "cisTarget_databases/mouse/mouse.mm9//mm9-tss-centered-10kb-7species.mc9nr.feather"
```

```r
motifEnrichment_selfMotifs_wGenes <- lapply(names(dbNames), function(motifDbName){
  ranking <- importRankings(dbNames[motifDbName], columns=allGenes)
  addSignificantGenes(resultsTable=motifEnrichment_selfMotifs[motifEnrichment_selfMotifs$motifDb==motifDbName,],
                      geneSets=tfModules,#从tfmodule中找匹配基因
                      rankings=ranking,
                      maxRank=5000, method="aprox", nCores=nCores)
})
```
```
## Using the column 'features' as feature index for the ranking database.
```
```
## [1] 22058
```

```r
suppressPackageStartupMessages(library(data.table))
motifEnrichment_selfMotifs_wGenes <- rbindlist(motifEnrichment_selfMotifs_wGenes)#将list中的元素纵向合并
saveRDS(motifEnrichment_selfMotifs_wGenes, file=getIntName(scenicOptions, "motifEnrichment_selfMotifs_wGenes"))
#那么"int/2.4_motifEnrichment_selfMotifs_wGenes.Rds"中存的就是motif与其对应的富集靶基因
if(getSettings(scenicOptions, "verbose"))
{
  # TODO messages/print
  message(format(Sys.time(), "%H:%M"), "\tNumber of motifs that support the regulons: ", nrow(motifEnrichment_selfMotifs_wGenes))
  motifEnrichment_selfMotifs_wGenes[order(motifEnrichment_selfMotifs_wGenes$NES,decreasing=TRUE),][1:5,(1:ncol(motifEnrichment_selfMotifs_wGenes)-1), with=F]
}
```
```
## 02:26    Number of motifs that support the regulons: 696
```
```
##    motifDb    geneSet                                        motif  NES   AUC
## 1:    10kb Tef_top1sd taipale_cyt_meth__TEF_NRTTAYGTAAYN_eDBD_meth 9.60 0.219
## 2:    10kb Tef_top1sd                taipale__TEF_DBD_NRTTACRTAAYN 9.40 0.216
## 3:    10kb Tef_top1sd                         transfac_pro__M07688 9.17 0.212
## 4:    10kb Tef_top1sd                                 cisbp__M5909 9.01 0.209
## 5:    10kb Tef_top1sd                         transfac_pro__M07439 8.85 0.206
##    highlightedTFs TFinDB                            TF_highConf
## 1:            Tef     **           Tef (inferredBy_Orthology).
## 2:            Tef     **           Tef (inferredBy_Orthology).
## 3:            Tef     ** Dbp; Hlf; Tef (inferredBy_Orthology).
## 4:            Tef     **           Tef (inferredBy_Orthology).
## 5:            Tef     **               Tef (directAnnotation).
##                                                                                                                          TF_lowConf
## 1:        Atf2; Cebpb; Dbp; Hlf; Nfil3 (inferredBy_MotifSimilarity). Cebpd; Cebpe; Cebpg (inferredBy_MotifSimilarity_n_Orthology).
## 2: Atf2; Cebpa; Cebpb; Dbp; Hlf; Nfil3 (inferredBy_MotifSimilarity). Cebpd; Cebpe; Cebpg (inferredBy_MotifSimilarity_n_Orthology).
## 3:                                                                         Atf2; Cebpa; Cebpb; Nfil3 (inferredBy_MotifSimilarity).
## 4: Atf2; Cebpa; Cebpb; Dbp; Hlf; Nfil3 (inferredBy_MotifSimilarity). Cebpd; Cebpe; Cebpg (inferredBy_MotifSimilarity_n_Orthology).
## 5:              Atf2; Cebpa; Cebpb; Dbp; Hlf (inferredBy_MotifSimilarity). Crebl2; Nfil3 (inferredBy_MotifSimilarity_n_Orthology).
##    nEnrGenes rankAtMax
## 1:        65       920
## 2:        73      1156
## 3:        79      1274
## 4:        68       904
## 5:        80      1249
```
```
#Save motif enrichment results as text and HTML (optional):
```

motif富集基因结果输出(即初步保存regulon相关信息)
```r
# motifEnrichment_selfMotifs_wGenes <- loadInt(scenicOptions, "motifEnrichment_selfMotifs_wGenes")#可以这样读入上一步数据

#以文本文件输出
if(!file.exists("output")) dir.create("output")#output文件夹在这一步生成
write.table(motifEnrichment_selfMotifs_wGenes, file=getOutName(scenicOptions, "s2_motifEnrichment"),
            sep="\t", quote=FALSE, row.names=FALSE)#以文本格式存在"output/Step2_MotifEnrichment.tsv"中

#以HTML文件输出
if("DT" %in% installed.packages() && nrow(motifEnrichment_selfMotifs_wGenes)>0)
{
  nvm <- tryCatch({
    colsToShow <- c("motifDb", "logo", "NES", "geneSet", "TF_highConf", "TF_lowConf")
    motifEnrichment_2html <- viewMotifs(motifEnrichment_selfMotifs_wGenes, colsToShow=colsToShow, options=list(pageLength=100))

    fileName <- getOutName(scenicOptions, "s2_motifEnrichmentHtml")#存于"output/Step2_MotifEnrichment_preview.html"中

    dirName <- dirname(fileName)
    fileName <- basename(fileName)
    suppressWarnings(DT::saveWidget(motifEnrichment_2html, fileName))#需要通过DT编译组件
    file.rename(fileName, file.path(dirName, fileName))
    if(getSettings(scenicOptions, "verbose")) message("Preview of motif enrichment saved as: ", file.path(dirName, fileName))
  }, error = function(e) print(e$message))
}
```
```
## Preview of motif enrichment saved as: output/Step2_MotifEnrichment_preview.html
```

```r
motifEnrichment.asIncidList <- apply(motifEnrichment_selfMotifs_wGenes, 1, function(oneMotifRow) {
  genes <- strsplit(oneMotifRow["enrichedGenes"], ";")[[1]]
  oneMotifRow <- data.frame(rbind(oneMotifRow), stringsAsFactors=FALSE)
  data.frame(oneMotifRow[rep(1, length(genes)),c("NES", "motif", "highlightedTFs", "TFinDB")], genes, stringsAsFactors = FALSE)
})
class(motifEnrichment.asIncidList)
```
```
## [1] "list"
```

```r
motifEnrichment.asIncidList <- rbindlist(motifEnrichment.asIncidList)#转换为数据框的结构，rbind会使其变成与类似于长格式的数据
head(motifEnrichment.asIncidList)
```
```
##     NES                                    motif highlightedTFs TFinDB
## 1: 4.34 taipale_cyt_meth__HOXA5_NYAATTAN_FL_meth           Dlx1      *
## 2: 4.34 taipale_cyt_meth__HOXA5_NYAATTAN_FL_meth           Dlx1      *
## 3: 4.34 taipale_cyt_meth__HOXA5_NYAATTAN_FL_meth           Dlx1      *
## 4: 4.34 taipale_cyt_meth__HOXA5_NYAATTAN_FL_meth           Dlx1      *
## 5: 4.34 taipale_cyt_meth__HOXA5_NYAATTAN_FL_meth           Dlx1      *
## 6: 4.34 taipale_cyt_meth__HOXA5_NYAATTAN_FL_meth           Dlx1      *
##        genes
## 1: Adcyap1r1
## 2:   Cntnap2
## 3:    Crabp1
## 4:      Dlx1
## 5:     Frem1
## 6:      Fzd1
```

```r
colnames(motifEnrichment.asIncidList) <- c("NES", "motif", "TF", "annot", "gene")
motifEnrichment.asIncidList <- data.frame(motifEnrichment.asIncidList, stringsAsFactors = FALSE)
```

按照TF整理靶基因,并且保留motif富集信息

```r
regulonTargetsInfo <- lapply(split(motifEnrichment.asIncidList, motifEnrichment.asIncidList$TF),#按照tf拆分表格，依次做如下处理
                             function(tfTargets){
  print(unique(tfTargets$TF))#输出当前正在处理的TF
  tfTable <- as.data.frame(do.call(rbind, lapply(split(tfTargets, tfTargets$gene), function(enrOneGene){#按照基因拆分表格，依次做如下处理
    highConfAnnot <- "**" %in% enrOneGene$annot#取出高置信度的motif
    enrOneGeneByAnnot <- enrOneGene
    if(highConfAnnot) enrOneGeneByAnnot <- enrOneGeneByAnnot[which(enrOneGene$annot == "**"),]#取出包含高置信度的基因
    bestMotif <- which.max(enrOneGeneByAnnot$NES)#取出每个基因当中富集分数NES最高的
    cbind(TF=unique(enrOneGene$TF), gene=unique(enrOneGene$gene), nMotifs=nrow(enrOneGene),
          bestMotif=as.character(enrOneGeneByAnnot[bestMotif,"motif"]), NES=as.numeric(enrOneGeneByAnnot[bestMotif,"NES"]),
          highConfAnnot=highConfAnnot)#将以上数据合并
  })), stringsAsFactors=FALSE)
  tfTable[order(tfTable$NES, decreasing = TRUE),]
})
```
```
## [1] "Dlx1"
## [1] "Dlx5"
## [1] "Irf1"
## [1] "Sox10"
## [1] "Sox8"
## [1] "Sox9"
## [1] "Stat6"
## [1] "Tef"
```

```r
regulonTargetsInfo <- rbindlist(regulonTargetsInfo)#将循环的list转换为数据框
colnames(regulonTargetsInfo) <- c("TF", "gene", "nMotifs", "bestMotif", "NES", "highConfAnnot")
head(regulonTargetsInfo)#即将每个module中的最佳motif取出，与靶基因、motif形成一个regulon
```
```
##      TF   gene nMotifs                                  bestMotif  NES
## 1: Dlx1  Scml4      24             hocomoco__GBX2_HUMAN.H11MO.0.D  4.2
## 2: Dlx1  Arl4c      24 taipale_cyt_meth__HOXA5_NYAATTAN_eDBD_meth 4.16
## 3: Dlx1   Ddr2      15 taipale_cyt_meth__HOXA5_NYAATTAN_eDBD_meth 4.16
## 4: Dlx1  Fstl4      18 taipale_cyt_meth__HOXA5_NYAATTAN_eDBD_meth 4.16
## 5: Dlx1 Gm5607       9 taipale_cyt_meth__HOXA5_NYAATTAN_eDBD_meth 4.16
## 6: Dlx1   Ldhb      23 taipale_cyt_meth__HOXA5_NYAATTAN_eDBD_meth 4.16
##    highConfAnnot
## 1:         FALSE
## 2:         FALSE
## 3:         FALSE
## 4:         FALSE
## 5:         FALSE
## 6:         FALSE
```

```r
#下面这步可选，目的是加入GENIE3 score(并不是用来构建regulons的)，如果你在上面运行的是GRNBOOST而非GENIE3，则可忽略这一步

linkList <- loadInt(scenicOptions, "genie3ll", ifNotExists="null")
if(!is.null(linkList) & ("weight" %in% colnames(linkList)))
{
  if(is.data.table(linkList)) linkList <- as.data.frame(linkList)

    uniquePairs <- nrow(unique(linkList[,c("TF", "Target")]))
    if(uniquePairs == nrow(linkList)) {
      linkList <- linkList[which(linkList$weight>=getSettings(scenicOptions, "modules/weightThreshold")),]
      rownames(linkList) <- paste(linkList$TF, linkList$Target,sep="__")
      regulonTargetsInfo <- cbind(regulonTargetsInfo, Genie3Weight=linkList[paste(regulonTargetsInfo$TF, regulonTargetsInfo$gene,sep="__"),"weight"])
    }else {
      warning("There are duplicated regulator-target (gene id/name) pairs in the co-expression link list.",
              "\nThe co-expression weight was not added to the regulonTargetsInfo table.")
    }
}else warning("It was not possible to add the weight to the regulonTargetsInfo table.")

saveRDS(regulonTargetsInfo, file=getIntName(scenicOptions, "regulonTargetsInfo"))#即最终的regulon信息被存在"int/2.5_regulonTargetsInfo.Rds"

write.table(regulonTargetsInfo, file=getOutName(scenicOptions, "s2_regulonTargetsInfo"),
            sep="\t", col.names=TRUE, row.names=FALSE, quote=FALSE)#以文本格式输出最终的regulon信息于"output/Step2_regulonTargetsInfo.tsv"
```

根据motif注释划分regulons

```r
regulonTargetsInfo_splitByAnnot <- split(regulonTargetsInfo, regulonTargetsInfo$highConfAnnot)#按照注释的置信度划分
regulons <- NULL
if(!is.null(regulonTargetsInfo_splitByAnnot[["TRUE"]]))
{
  regulons <- lapply(split(regulonTargetsInfo_splitByAnnot[["TRUE"]], regulonTargetsInfo_splitByAnnot[["TRUE"]][,"TF"]), function(x) sort(as.character(unlist(x[,"gene"]))))
}#执行度搞的保留TF名称
regulons_extended <- NULL
if(!is.null(regulonTargetsInfo_splitByAnnot[["FALSE"]]))
{
  regulons_extended <- lapply(split(regulonTargetsInfo_splitByAnnot[["FALSE"]],regulonTargetsInfo_splitByAnnot[["FALSE"]][,"TF"]), function(x) unname(unlist(x[,"gene"])))
  regulons_extended <- setNames(lapply(names(regulons_extended), function(tf) sort(unique(c(regulons[[tf]], unlist(regulons_extended[[tf]]))))), names(regulons_extended))
  names(regulons_extended) <- paste(names(regulons_extended), "_extended", sep="")
}#置信度低的重命名为TF名称_extended
regulons <- c(regulons, regulons_extended)
saveRDS(regulons, file=getIntName(scenicOptions, "regulons"))#将regulons信息(TF与其对应基因)以geneset的形式存在"int/2.6_regulons_asGeneSet.Rds"

incidList <- reshape2::melt(regulons)#转换为长格式数据
head(incidList)
```
```
##       value   L1
## 1    Ablim1 Dlx1
## 2      Ache Dlx1
## 3    Adarb2 Dlx1
## 4 Adcyap1r1 Dlx1
## 5  AI854703 Dlx1
## 6       Alk Dlx1
```

```r
incidMat <- table(incidList[,2], incidList[,1])
saveRDS(incidMat, file=getIntName(scenicOptions, "regulons_incidMat"))

if(getSettings(scenicOptions, "verbose"))
{
  # Number of regulons and summary of sizes:
  length(regulons)
  summary(lengths(regulons))
}
```
```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
##    41.0   105.2   128.5   162.0   165.2   448.0
```

```r
scenicOptions@status$current <- 2
#如果程序中断了，可以这样查看运行阶段，返回的数字为已运行完的step：
scenicOptions@status$current
```
```
## [1] 2
```

``

[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497842&idx=1&sn=5d109d3cfc74c64c4499fce90febeabb&chksm=9b3c8122ac4b0834157220d5c21f1f88dfa7a4eeb5ff44454df126b75648e41a8621833fb8e2&scene=21#wechat_redirect>)
**往期回顾**

[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)

[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)

[SCENIC单细胞转录因子预测|3.软件安装与数据准备](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de&scene=21#wechat_redirect>)

[SCENIC单细胞转录因子预测|4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)

**参考**

[1]Aibar S, González-Blas CB, Moerman T, Huynh-Thu VA, Imrichova H, Hulselmans G, Rambow F, Marine JC, Geurts P, Aerts J, van den Oord J, Atak ZK, Wouters J, Aerts S. SCENIC: single-cell regulatory network inference and clustering. Nat Methods. 2017 Nov;14(11):1083-1086. doi: 10.1038/nmeth.4463. Epub 2017 Oct 9.

[2]https://github.com/aertslab/SCENIC

**单细胞系列教程目录**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=other&wxfrom=5&wx_lazy=1) 单细胞数据分析系列教程：B站视频，先看一遍视频再去看推送操作，建议至少看三遍：https://www.bilibili.com/video/BV1S44y1b76Z/本公众号单细胞相关资料都可以在这里订阅：[scRNA-Seq学习手册2023_R语言版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500516&idx=1&sn=3c0b9de505fcd232054e38b451fa1742&chksm=9b3cbbb4ac4b32a26b61f3a1f7941fff5852d3e6e744ec680aafd0b84ec976a33bf982fb5f79&scene=21#wechat_redirect>)

单细胞测序基础数据分析保姆级教程，代码部分整理在往期推送之中：[手把手教你做单细胞测序数据分析|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&chksm=9b3cb950ac4b30467a082527547b91aec15b7d1f40d44e362894aedeb6a99e014518fa5e4743&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|2.各类数据结构与读取方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499795&idx=2&sn=68e6298eb43633c71939c146d90230ff&chksm=9b3cb943ac4b3055e09739d77e037d679f3d9ec68780d1aa8c592f806fcc8d2322eaee78752d&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|3.单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|4.多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|5.细胞类型注释，从入门到入土](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&chksm=9b3cb8d7ac4b31c19c843810c7fe4341515df8ba6fff86a0ebff9d830edfcd656a29d18011c9&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|6组间差异分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=2&sn=d8c4ebf8f63d12bd2ac8e2607864f322&chksm=9b3cb8beac4b31a824e228b486f0d8dd21a8f4113a0a0bcbaf1b20eaade3a83c9c7c1184010b&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|7基因集富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21#wechat_redirect>)
[Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&scene=21#wechat_redirect>)

单细胞图片改造计划：[改造单细胞降维图| 1.DimPlot的探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496162&idx=1&sn=598c2920f7cc0697ee5a1fa6cadaee04&chksm=9b3c88b2ac4b01a415feeebbbec6c4891319439dc8dcdafd33cca7a1222e5adc723ae9d3a73d&scene=21#wechat_redirect>)
[改造单细胞降维图| 2.ggplot2中的DIY](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496239&idx=1&sn=1fe6fd4a7fb88ecc0456b4f5710cb5d6&chksm=9b3c8b7fac4b0269e0abeab951ad6ae0ddd1464dd9d1867280eeb9755fda5ba8f5237d88a7a6&scene=21#wechat_redirect>)
[改造单细胞降维图| 3.3D降维图与动图绘制](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496343&idx=1&sn=8ac1c511e1197e231c628649167bc26f&chksm=9b3c8bc7ac4b02d134495e000f349cdbd75458b429297f858dfd58d1b428d8256b7e5c5075b4&scene=21#wechat_redirect>)

SCENIC转录因子分析：[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|3.软件安装与数据准备](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)

上游fastq文件处理：
[单细胞分析的最上游——处理Fastq文件：cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484923&idx=1&sn=b5876af14fbee68d1e9db4b0f70cd1c8&chksm=9b3f7cabac48f5bdb3aac7d20201d89121a83720b41a10017564fedbb8c4a13df0da92daffd7&scene=21#wechat_redirect>)
[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484937&idx=1&sn=4fe1fa518202bdaf462bb93a2614ed32&chksm=9b3f7f59ac48f64fafaf34bac2c80f06d3a86b6a84ccf12566c7eac25bb71c7edd3d74004cf7&scene=21#wechat_redirect>)[有奖提问,这个smart-Seq2数据实战的比对率为何如此低？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488441&idx=1&sn=dac4efc4a8901a4abb133f9e5c80831e&chksm=9b3f6ae9ac48e3fff5a7112a0127726441ccb9dc2c3369d4a0fe98a2120df991954ff0567732&scene=21#wechat_redirect>)

细胞通讯B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1Ab4y1W7qx?p=1**往期推送**[《细胞通讯》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501282&idx=2&sn=cd37ea80e0b92f5bfbc98ea286e363da&chksm=9b3cbcb2ac4b35a4258d21fe003374795619fc2356376ebbe4ff640233f4b4c6e3e3ead41370&scene=21#wechat_redirect>)[《细胞通讯》2.1CellChat基础分析教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=2&sn=fb3e252d95ee8b50cd446e71335b1aa0&chksm=9b3cbca0ac4b35b621b4f51d2c3a130f00461faeeff067396222c2fc2eeb53f3544664d7d9bc&scene=21#wechat_redirect>)
[《细胞通讯》2.2CellChat多组别分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501523&idx=2&sn=6fa803f256c2e0b945f93ae7d8245f50&chksm=9b3cbf83ac4b3695b587e9817840f419104c8680f5ef08ee39aa149b79852f48b179f68e3397&scene=21#wechat_redirect>)

拟时序分析B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1br4y1x7Hf?p=1**往期推送**[《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)[《拟时序分析》3.monocle2实操：精简版拟时序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487398&idx=1&sn=6621eed90157d8da06ef778c40bd5554&chksm=9b3f76f6ac48ffe081ddfee3a323e0e31c1fda33731012de73168cf2ab30a226cf70c848f769&scene=21#wechat_redirect>)
[《拟时序分析》4.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》7.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
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
[一文搞定单细胞基因集评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493493&idx=1&sn=2cd725b2f04377f218955bafbcbb877d&chksm=9b3c9e25ac4b17330a9b9ff77302ab95a9dc5dc7e6fe7298f28d682112ee066c7d4bc1947982&scene=21#wechat_redirect>)[答读者问（二十）四个单细胞样本只给了一套文件怎么读](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494879&idx=1&sn=c2287ab3684792747dfac53d6704462b&chksm=9b3c958fac4b1c994a4b075c4f8475816e121966fa8c52cb0a2ce8c14987988ab9bdb49bdf69&scene=21#wechat_redirect>)
[人类单细胞测序数据中有哪些以"**-"开头的基因](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495019&idx=1&sn=f52ac22ca1ea47ecddaa3503bdc2c0b6&chksm=9b3c943bac4b1d2d521f7155ce8f499389dade23828017572a84cdce71e5d08d37d74e08512b&scene=21#wechat_redirect>)
[为什么总把分辨率调的很高](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495765&idx=1&sn=2ec5e3e26491e28c92e25c40630bffae&chksm=9b3c8905ac4b0013a23f9cda2cccd67cdf3c4a941bac161e3a15a12ab98cd4e5eca8aeedbe96&scene=21#wechat_redirect>)
[Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495938&idx=1&sn=2258390c97ec14f3cd336defede59cdb&chksm=9b3c8852ac4b01448fd3b84463d5ab6b697495db6ad57746e7f60e32f491547a3e35290c66ee&scene=21#wechat_redirect>)
[答读者问| 22.object 'CsparseMatrix_validate' not found](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496273&idx=1&sn=fd5a92dd7fdc349b1624784ca74b1220&chksm=9b3c8b01ac4b0217cf06d89bfea49c3fa0c9b580957338c0cc8f55ede3e8f65d6d7162ae27e3&scene=21#wechat_redirect>)
[单细胞数据在R中的读取及存储速度太慢怎么办？这个神包来帮你！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=1&sn=11bdf3c7f9042fc03f9ed237a9b9677b&chksm=9b3cb8beac4b31a8bf1d9fb862553ed32ac9a56f4a6e0f2d38c9478132f87327d8c6b6940573&scene=21#wechat_redirect>)
[单细胞分群分辨率选择困难症](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501241&idx=1&sn=9e15d23f721ad7f4ae1335ce5362031b&chksm=9b3cbce9ac4b35ff43434c0384afbbf5689f5b62a677e55e8a635d4812da57593d85a73cf48b&scene=21#wechat_redirect>)

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
[《Nature》：MYB调控衰竭性T细胞对检查点抑制的响应](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498939&idx=2&sn=b63958fb8f28af052036f4ffc05e2fc2&chksm=9b3c85ebac4b0cfdf3fda8f7236c50db168de20ff4795db7af9d6a0b45304e3f6fb3ba888694&scene=21#wechat_redirect>)[单细胞都能活检测序了？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500846&idx=1&sn=d5e9782c0318e411771e746950f5b5f5&chksm=9b3cbd7eac4b3468ea93a5d6a28cfd05409660a532cc8df72ed9b58f30a76b0a8b6cec79934a&scene=21#wechat_redirect>)
[文献阅读(二十九)、单细胞测序做到什么程度能毕业|硕士篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493808&idx=1&sn=52c7d330ffdda47c3409d36fe9cbbcd8&chksm=9b3c91e0ac4b18f6edf59d171a0d982b1e3f842148046d8eed19343484feaa84dbd5b7682a11&scene=21#wechat_redirect>)
[文献阅读(三十)、单细胞测序做到什么程度能毕业|博士篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494017&idx=1&sn=a2dc4e2eef2bcdb40f5074b665dfa45f&chksm=9b3c90d1ac4b19c79ac5128f96d27789241357c9745bb0389ff5f79f96ab825d3e1c9b29e3af&scene=21#wechat_redirect>)[2022年了，都有哪些器官/组织有scRNA-Seq数据|小鼠篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494796&idx=1&sn=92c91a65719bdf39658814eb691a780f&chksm=9b3c95dcac4b1cca5547440a5881e650da3ea430bad3e6017cbd2891606b2ec40e3ec343bc0e&scene=21#wechat_redirect>)
[2022年了，都有哪些器官/组织有scRNA-Seq数据|人类篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494806&idx=1&sn=1d15ad9cb4d350a164d3b941bc715233&chksm=9b3c95c6ac4b1cd054cedbd3e8c8f57ee88cc59a6ebda2fd11ba8fea79f5e9e8c65d21ff338c&scene=21#wechat_redirect>)
[2023年了, 都哪些物种有scRNA-Seq数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496958&idx=1&sn=f34c69e2114d99fa25e2524411c028a2&chksm=9b3c8daeac4b04b80a5629433d5eec4d25b8ba7d2a74fa31cd499b98c36601ddfe436e2196eb&scene=21#wechat_redirect>)[终于读到一篇用monocle3做拟时序的文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496064&idx=1&sn=0be38306f9cd8c6b819d58cc2e779b87&chksm=9b3c88d0ac4b01c6773b6c4f1a063788509baa27c57e2098b16b8ebe38cc625a87b9d89272c7&scene=21#wechat_redirect>)
[单细胞转录组+亚细胞空间代谢组=25分文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496126&idx=1&sn=8cb6040a38eb844bb215c0d395196e3a&chksm=9b3c88eeac4b01f8dcb8f4c7a19c5a58841d5fe1623f0a4c585c6dcc281cbbdd2830a1150f6a&scene=21#wechat_redirect>)
[酸了，六个样本的scRNA-Seq+差异分析=9分文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496237&idx=1&sn=646cd85b62d08c1739a532242c8991ba&chksm=9b3c8b7dac4b026be9e65b64df8e830d1c2c882272165e64eec6eb258e4ed5342cf30f42dda5&scene=21#wechat_redirect>)[自测scRNA-Seq+scWGBS=3分三区文章？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498939&idx=1&sn=1b33d219c795f2de8ff66a5c330a3d24&chksm=9b3c85ebac4b0cfd050a7c0abe11dead991a988aa5b790eac6fd57de2f76a85ef2191d8b9ca6&scene=21#wechat_redirect>)
[百万级单细胞多组学数据集成](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499336&idx=1&sn=864c535b38ce630487fccc602d893a80&chksm=9b3c8718ac4b0e0e8a0e2560a83546167a82616d99503606e3ac0ef29e90b01cc762e95d64e6&scene=21#wechat_redirect>)[空间转录组与单细胞转录组整合分析工具大比拼](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500243&idx=1&sn=b0e513e85a202ec7ca4041a700a7ae10&chksm=9b3cb883ac4b3195cffd0398d880468b12dd068f9a9fd96b7d0f8aed8961be34293e6ff4a2bb&scene=21#wechat_redirect>)

单细胞注释复写[单细胞注释复写(一):Human Fetal Kidney](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447&scene=21#wechat_redirect>)[单细胞注释复写(二): human colorectal](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491642&idx=1&sn=2246fb702277ddc690f056fc8854142e&chksm=9b3c996aac4b107c059a403978eca7be1ae7987659626272c58430910ad75892ad470517aefb&scene=21#wechat_redirect>)
[单细胞复写|3.急性心肌梗塞(AMI)外周血scRNA-Seq分析实战(链接重置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501145&idx=2&sn=12c2e8d104ad343fc13acb8cda266e6c&chksm=9b3cbc09ac4b351f4ed708a0ed577a21f48ccb0d4173aed94a027b4170147ab85931ee51d1e5&scene=21#wechat_redirect>)

硬件准备：
[生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501099&idx=1&sn=78446147184292fad3417495926b3096&chksm=9b3cbc7bac4b356dcf0460781f9bf16df4ede481f8cc57282c7384b9d2baccaa820d64c89bab&scene=21#wechat_redirect>)
[有root权限的共享服务器,注册即送200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500273&idx=1&sn=f600f10077f6298ea957e459b5f8a375&chksm=9b3cb8a1ac4b31b702838076dbceb077e9c8980d9cffe5c4ab10ebbeceaf5fe3e658003e66c4&scene=21#wechat_redirect>)
[独享服务器，满足你对生信分析的所有幻想](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500111&idx=1&sn=1dfc668263614efb82e0659af5fcd438&chksm=9b3cb81fac4b3109a8e19a09cc68122b1943dcd45c653627e77dfa47d476280079ea6a8dd63d&scene=21#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、服务器([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501099&idx=1&sn=78446147184292fad3417495926b3096&chksm=9b3cbc7bac4b356dcf0460781f9bf16df4ede481f8cc57282c7384b9d2baccaa820d64c89bab&scene=21#wechat_redirect>))的**微信号[Biomamba_kefu]** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
