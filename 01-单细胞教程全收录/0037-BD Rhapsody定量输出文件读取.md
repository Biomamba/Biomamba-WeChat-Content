---
title: "BD Rhapsody定量输出文件读取"
date: 2024-07-13
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519706&idx=1&sn=9d084bd8edf6ab4d9184672e5a4a2722&chksm=9b3cf48aac4b7d9c16ef85de7a5f33e65552bbba5d11d2170237063cf754fe9ff376647d3bd7#rd
albums: ["单细胞教程全收录"]
---

# BD Rhapsody定量输出文件读取

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519706&idx=1&sn=9d084bd8edf6ab4d9184672e5a4a2722&chksm=9b3cf48aac4b7d9c16ef85de7a5f33e65552bbba5d11d2170237063cf754fe9ff376647d3bd7#rd
> 合集：单细胞教程全收录

![](../../images/1acba08ed67b8404.webp)

演示过程

![](../../images/ed620ac26d383667.gif)

此前我们做了[BD Rhapsody平台单细胞转录组定量流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506542&idx=1&sn=99cf7af7fc0d56b0d6fe7ea3596df2b6&chksm=9b3ca33eac4b2a28e6682a7cf0b2091a387a06ecf89ee10737cf2194286ec0bba472ef1c2b90&scene=21#wechat_redirect>)，有些同学表示不知道如何读取`cwl-runner`输出的表达矩阵，这里我们来演示一下：

测试数据与教程的下载地址：

![](../../images/454a3448c6081735.jpg)

![](../../images/52e8c499bd1978f8.png)

输出文件夹下会有一个以`_Expression_Data.st`结尾的文件，即为我们需要的表达矩阵。
```r
# 读取数据：
expr <- read.table('Sample_f1_Expression_Data.st',header = T)
# 查看数据结构：
head(expr)
```
```
##   Cell_Index   Gene RSEC_Reads Raw_Molecules RSEC_Adjusted_Molecules
## 1      45133    A2M          1             1                       1
## 2      45133 A4GALT          3             1                       1
## 3      45133   AAAS          8             3                       3
## 4      45133   AACS         17             5                       4
## 5      45133  AAED1          3             2                       2
## 6      45133  AAGAB         38             8                       8
```

这几列数据对应的含义是：
`Cell_Index`: 细胞索引 - 用于标识每个细胞的唯一编号。
`Gene`: 基因 - 表示该行数据对应的基因名称。
`RSEC_Reads`: RSEC读数 - 该基因在对应细胞中的RSEC（Robust Single-cell Effective Count）读取数。
`Raw_Molecules`: 原始分子数 - 该基因在对应细胞中的原始分子计数。
`RSEC_Adjusted_Molecules`: RSEC调整后的分子数 - 基于RSEC方法调整后的分子计数。

那么对应的，我们只需要以`Cell_Index`作为列名，`Gene`作为行名，`RSEC_Adjusted_Molecules`作为填充值构建稀疏矩阵即可。
```r
library(Seurat)
```
```
## Warning: 程辑包'Seurat'是用R版本4.3.3 来建造的
```
```
## 载入需要的程辑包：SeuratObject
```
```
## Warning: 程辑包'SeuratObject'是用R版本4.3.3 来建造的
```
```
## 载入需要的程辑包：sp
```
```
## Warning: 程辑包'sp'是用R版本4.3.3 来建造的
```
```
##
## 载入程辑包：'SeuratObject'
```
```
## The following object is masked from 'package:base':
##
##     intersect
```
```r
library(Matrix)
```
```
## Warning: 程辑包'Matrix'是用R版本4.3.3 来建造的
```
```r
# 将长格式的数据框转换为稀疏矩阵
sparse_matrix <- sparseMatrix(
  i = as.numeric(factor(expr$Gene)),
  j = as.numeric(factor(expr$Cell_Index)),
  x = expr$RSEC_Adjusted_Molecules
)

# 将行和列名称设置为基因名称和细胞索引
rownames(sparse_matrix) <- levels(factor(expr$Gene))
colnames(sparse_matrix) <- levels(factor(expr$Cell_Index))

# 创建Seurat对象
scRNA <- CreateSeuratObject(counts = sparse_matrix)
```
```
## Warning: Feature names cannot have underscores ('_'), replacing with dashes
## ('-')
```
```
# 检查Seurat对象
scRNA
```
```
## An object of class Seurat
## 29406 features across 8870 samples within 1 assay
## Active assay: RNA (29406 features, 0 variable features)
##  1 layer present: counts
```

检查一下行名和列名对不对，`Seurat`对象应该是一个行名为基因名，列名是细胞`barcode`的对象：
```
# 没问题：
colnames(scRNA)[1:5]
```
```
## [1] "48"  "118" "190" "290" "411"
```
```
rownames(scRNA)[1:5]
```
```
## [1] "7SK"      "A1BG"     "A1BG-AS1" "A1CF"     "A2M"
```

继续往下做基础分析看看：
```r
scRNA[["percent.mt"]] <- PercentageFeatureSet(scRNA, pattern = "^MT-") #通过线粒体的序列数来对数据进行计算
head(scRNA@meta.data, 5)  #QC的数据存在meta.data里，可以用这个来查看前5行
```
```
##        orig.ident nCount_RNA nFeature_RNA percent.mt
## 48  SeuratProject       1519          594  10.730744
## 118 SeuratProject       1430          577  10.909091
## 190 SeuratProject       2056          927  22.422179
## 290 SeuratProject        922          461   9.544469
## 411 SeuratProject      26151         5310   8.607701
```
```
VlnPlot(scRNA, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)
```
```
## Warning: Default search for "data" layer in "RNA" assay yielded no results;
## utilizing "counts" layer instead.
```

![](../../images/ffc57e9ea02ad1e5.webp)
```r
#用小提琴图来展示QC的结果，展示了每个barcode中基因的数目、UMI数目以及线粒体基因含量的分布情况
plot1 <- FeatureScatter(scRNA, feature1 = "nCount_RNA", feature2 = "percent.mt")
plot2 <- FeatureScatter(scRNA, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")

CombinePlots(plots = list(plot1, plot2)) #高变基因，判断趋势及占比
```
```
## Warning: CombinePlots is being deprecated. Plots should now be combined using
## the patchwork system.
```

![](../../images/32ca40cc616e5cad.webp)
```r
scRNA <- subset(scRNA, subset = nFeature_RNA > 200 & nFeature_RNA < 5000 & percent.mt < 20)
#质控，选子集，RNA数量在200与2500之间的，多的可能是低质量细胞或空drouplets，gene count多的可能是doublets or multiplets
scRNA <- NormalizeData(scRNA, normalization.method = "LogNormalize", scale.factor = 10000)
```
```
## Normalizing layer: counts
```
```r
#用LogNormalize法对数据进行标准化（乘10000再取对数）数据存在scRNA[["RNA"]]@data.里
#默认的方法也完成了log1p的操作，得到的结果就类似于TPM的对数
scRNA <- FindVariableFeatures(scRNA, selection.method = "vst", nfeatures = 2000)
```
```
## Finding variable features for layer counts
```
```r
# 筛选高变基因（输出2000个），用于下游的PCA及分群
top10 <- head(VariableFeatures(scRNA), 10) #输出差异最大的十个基因
plot1 <- VariableFeaturePlot(scRNA)
plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)
```
```
## When using repel, set xnudge and ynudge to 0 for optimal results
```
```
CombinePlots(plots = list(plot1, plot2))  #输出差异基因散点图（有无标签）
```
```
## Warning: CombinePlots is being deprecated. Plots should now be combined using
## the patchwork system.
```
```
## Warning in scale_x_log10(): log-10 transformation introduced infinite values.
## log-10 transformation introduced infinite values.
```

![](../../images/90e2afb572e782d0.png)
```r
scRNA <- ScaleData(scRNA, features =  rownames(scRNA)) #将数据进行标准化，为后续的PCA分析做准备，数据存在scRNA[["RNA"]]@scale.data
```
```
## Centering and scaling data matrix
```
```r
##for PCA DoHeatmap
#scRNA <- ScaleData(scRNA)#only4VariableFeatures
scRNA <- ScaleData(scRNA, vars.to.regress = "percent.mt") #剔除不想要的变量（如线粒体的比例）
```
```
## Regressing out percent.mt
## Centering and scaling data matrix
```
```
## Warning: Different features in new layer data than already exists for
## scale.data
```
```r
#scRNA[["RNA"]]@scale.data
scRNA <- RunPCA(scRNA, features = VariableFeatures(object = scRNA)) #PCA降维分析
```
```
## PC_ 1
## Positive:  CD177, PIM2, RAB11FIP1, TP53INP2, PGLYRP1, IFIT2, COL18A1, TRBC2, CD3E, GNLY
##     TRAC, CD2, HSPA6, SPOCK2, GZMH, CEACAM1, NKG7, GZMA, PRF1, FGFBP2
##     IL32, CAMP, IL2RB, PI3, PTP4A3, CTSW, GZMB, NUAK2, CD7, KLRD1
## Negative:  MS4A7, MSR1, C1QC, C1QA, LGMN, A2M, CD163, GPNMB, TMEM176B, PLD3
##     C1QB, CTSL, MS4A4A, HLA-DPA1, HLA-DRB6, LIPA, APOE, SLCO2B1, FPR3, HLA-DRB1
##     DAB2, APOC1, HLA-DRA, TMEM176A, HLA-DMB, GPX1, CAPG, HLA-DPB1, CD68, SIGLEC1
## PC_ 2
## Positive:  IER3, VIM, CD14, LYZ, FCGRT, FTL, CXCL16, CD74, MS4A7, ASAH1
##     HLA-DRA, FCGR3A, MS4A6A, MSR1, C1QA, C1QC, CD163, IFI6, MS4A4A, HLA-DMB
##     CD83, C1QB, HLA-DPA1, CCL3, HLA-DPB1, FPR3, SLCO2B1, APOC1, CXCL2, APOE
## Negative:  PERP, KRT19, KRT6A, JUP, TACSTD2, SFN, CLDN4, MGST1, S100A16, HSPB1
##     CALML3, NQO1, TM4SF1, CLDN1, KRT5, GSTP1, CLDN7, CDKN2A, PLS3, UCHL1
##     KRT8, SDC1, AKR1B10, AKR1C2, MAL2, KLF5, KRT13, GPX2, EPCAM, AKR1C1
## PC_ 3
## Positive:  SPRR3, TACSTD2, SPRR1B, KRT6A, TMPRSS11E, SPRR1A, CLDN4, CLDN7, LCN2, ELF3
##     TMPRSS11D, PERP, PRSS8, SPRR2A, KRT16, KRT13, KRT80, PITX1, CTD-2319I12.1, SPRR2D
##     MAL2, S100A14, SERPINB2, KRT19, CSTA, CD24P4, ANXA1, KRT6B, PRSS22, A2ML1
## Negative:  SPARC, BGN, IGFBP7, CALD1, COL4A2, IGFBP4, COL1A2, LAMB1, FSTL1, FN1
##     COL5A2, MGP, THY1, MMP2, COL3A1, COL6A2, COL1A1, LAMA4, LHFP, PTRF
##     LUM, NID1, DCN, COL4A1, MYL9, COL6A1, C1R, CRIP2, COL6A3, PRSS23
## PC_ 4
## Positive:  FAM46C, MZB1, DERL3, CD79A, FCRL5, ITM2C, IGHG1, SSR4, SLAMF7, DUSP5
##     POU2AF1, CCL5, TRBC2, NKG7, IGHGP, CD3E, CPNE5, IGKC, SPAG4, RAB30
##     XBP1, IGHG4, GNLY, ANKRD36BP2, IGHG3, RPS5, TNFRSF17, SEC11C, IL32, IGHG2
## Negative:  IER3, FTL, SPRR3, TIMP2, SPRR1B, IL1RN, SPRR2A, TMPRSS11E, SLPI, TMPRSS11D
##     RAB11FIP1, KRT80, LCN2, SPRR1A, FCGRT, CXCL16, SPRR2D, PRSS8, EMP1, PI3
##     CTD-2319I12.1, CXCL1, PRSS22, CEACAM6, A2ML1, CSTA, CEACAM5, TP53INP2, ASAH1, IFIT2
## PC_ 5
## Positive:  UCHL1, AKR1C2, AKR1C1, AKR1B10, GSTM3, NTRK2, ADH7, ALDH3A1, TP63, KRT8
##     CKS1B, GPX2, SPARCL1, PKP1, CLCA2, NQO1, MIR205HG, AKR1C3, TOP2A, TPX2
##     SERPINB5, SOX2, BIRC5, EPCAM, CCNB2, FOXM1, STMN1, TMEM97, UGDH, MYC
## Negative:  SPRR1B, SPRR3, TMPRSS11E, SPRR2A, KRT80, SPRR2D, SPRR1A, HOPX, TMPRSS11D, LCN2
##     NDRG2, CTD-2319I12.1, PRSS8, PRSS22, KRT78, KLK10, A2ML1, MALL, CEACAM6, CEACAM5
##     KLK11, SLPI, PDZK1IP1, EPS8L1, SERPINB2, NCCRP1, C1orf116, KLK12, PRSS27, FUT3
```
```
print(scRNA[["pca"]], dims = 1:5, nfeatures = 5) #打印PCA部分结果
```
```
## PC_ 1
## Positive:  CD177, PIM2, RAB11FIP1, TP53INP2, PGLYRP1
## Negative:  MS4A7, MSR1, C1QC, C1QA, LGMN
## PC_ 2
## Positive:  IER3, VIM, CD14, LYZ, FCGRT
## Negative:  PERP, KRT19, KRT6A, JUP, TACSTD2
## PC_ 3
## Positive:  SPRR3, TACSTD2, SPRR1B, KRT6A, TMPRSS11E
## Negative:  SPARC, BGN, IGFBP7, CALD1, COL4A2
## PC_ 4
## Positive:  FAM46C, MZB1, DERL3, CD79A, FCRL5
## Negative:  IER3, FTL, SPRR3, TIMP2, SPRR1B
## PC_ 5
## Positive:  UCHL1, AKR1C2, AKR1C1, AKR1B10, GSTM3
## Negative:  SPRR1B, SPRR3, TMPRSS11E, SPRR2A, KRT80
```
```
VizDimLoadings(scRNA, dims = 1:2, reduction = "pca")
```

![](../../images/9cf9fa08a1da827d.webp)
```
DimHeatmap(scRNA, dims = 1, cells = 500, balanced = TRUE) #三种PCA展示方式
```

![](../../images/ad49fda897a2ae02.webp)
```
DimHeatmap(scRNA, dims = 1:15, cells = 500, balanced = TRUE) #展示15种PCA
```

![](../../images/0b96beec6f6e46f4.webp)
```r
#筛选合适的维度：
scRNA <- JackStraw(scRNA, num.replicate = 100) #重复计算次数
scRNA <- ScoreJackStraw(scRNA, dims = 1:20) #计算维度这一步花的时间比较久

JackStrawPlot(scRNA, dims = 1:15) #画出1到15个维度
```
```
## Warning: Removed 21000 rows containing missing values or values outside the scale range
## (`geom_point()`).
```

![](../../images/e37fcbabe9207447.webp)
```
#JackStrawPlot相当于高级PCA，为挑选合适维度进行下游可视化提供依据

ElbowPlot(scRNA) #利用ElbowPlot来评价PC，PCA切记为了结果好看而降低PC数
```

![](../../images/d228d9c62b7a3eed.png)
```r
scRNA <- FindNeighbors(scRNA, dims = 1:10)
```
```
## Computing nearest neighbor graph
```
```
## Computing SNN
```
```r
scRNA <- FindClusters(scRNA, resolution = 0.5)
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 6917
## Number of edges: 225890
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.8872
## Number of communities: 14
## Elapsed time: 0 seconds
```
```
#细胞分群，resolution分辨率在细胞数在3000附近时一般设为0.4-1.2，resolution越大得到的类群越多
head(Idents(scRNA), 5) #看前五个分类群ID
```
```
##  48 118 290 480 560
##   0   5   1   1   0
## Levels: 0 1 2 3 4 5 6 7 8 9 10 11 12 13
```
```r
#非线性降维方法：UMAP、tSNE
scRNA <- RunUMAP(scRNA, dims = 1:10) #运行UMAP算法
```
```
## Warning: The default method for RunUMAP has changed from calling Python UMAP via reticulate to the R-native UWOT using the cosine metric
## To use Python UMAP via reticulate, set umap.method to 'umap-learn' and metric to 'correlation'
## This message will be shown once per session
```
```
## 15:19:45 UMAP embedding parameters a = 0.9922 b = 1.112
```
```
## 15:19:45 Read 6917 rows and found 10 numeric columns
```
```
## 15:19:45 Using Annoy for neighbor search, n_neighbors = 30
```
```
## 15:19:45 Building Annoy index with metric = cosine, n_trees = 50
```
```
## 0%   10   20   30   40   50   60   70   80   90   100%
```
```
## [----|----|----|----|----|----|----|----|----|----|
```
```
## **************************************************|
## 15:19:46 Writing NN index file to temp file C:\Users\ADMINI~1\AppData\Local\Temp\RtmpyE7FkX\file26507696de1
## 15:19:46 Searching Annoy index using 1 thread, search_k = 3000
## 15:19:47 Annoy recall = 100%
## 15:19:47 Commencing smooth kNN distance calibration using 1 thread with target n_neighbors = 30
## 15:19:48 Initializing from normalized Laplacian + noise (using RSpectra)
## 15:19:48 Commencing optimization for 500 epochs, with 299704 positive edges
## 15:19:58 Optimization finished
```
```r
#sce.all <- RunUMAP(sce.all, dims = 1:30, min.dist = 0.01, n.neighbors = 4L)
#可以调整亚群之间的距离
scRNA <- RunTSNE(scRNA, dims = 1:10) #运行TSNE算法，TSNE算法运行时间较UMAP更久
DimPlot(scRNA, reduction = "umap", label = TRUE)
```

![](../../images/0526c377d66a0f0f.webp)
```r
#显示分类群的标号

scRNA.markers <- FindAllMarkers(scRNA, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)
```
```
## Calculating cluster 0
## Calculating cluster 1
## Calculating cluster 2
## Calculating cluster 3
## Calculating cluster 4
## Calculating cluster 5
## Calculating cluster 6
## Calculating cluster 7
## Calculating cluster 8
## Calculating cluster 9
## Calculating cluster 10
## Calculating cluster 11
## Calculating cluster 12
## Calculating cluster 13
```
```r
#寻找每一个分类群与其他所有细胞之间的标记基因，并只显示positive结果
library(dplyr)
```
```
## Warning: 程辑包'dplyr'是用R版本4.3.3 来建造的
```
```
##
## 载入程辑包：'dplyr'
##
## The following objects are masked from 'package:stats':
##
##     filter, lag
##
## The following objects are masked from 'package:base':
##
##     intersect, setdiff, setequal, union
```
```r
# 筛选Top3 gene
top3gene <- scRNA.markers %>% group_by(cluster) %>% top_n(n = 3, wt = avg_log2FC)
```
```
# 查看marker
VlnPlot(scRNA, features = unique(top3gene$gene),pt.size = 0,stack = T)
```

![](../../images/742bebf63a205cc9.webp) 接下来的分析探索就请大家自己完成啦，大家可以参考原数据集： https://ngdc.cncb.ac.cn/gsa-human/browse/HRA001033

本教程用到的R语言环境：
```
sessionInfo()
```
```
## R version 4.3.0 (2023-04-21 ucrt)
## Platform: x86_64-w64-mingw32/x64 (64-bit)
## Running under: Windows 11 x64 (build 22621)
##
## Matrix products: default
##
##
## locale:
## [1] LC_COLLATE=Chinese (Simplified)_China.utf8
## [2] LC_CTYPE=Chinese (Simplified)_China.utf8
## [3] LC_MONETARY=Chinese (Simplified)_China.utf8
## [4] LC_NUMERIC=C
## [5] LC_TIME=Chinese (Simplified)_China.utf8
##
## time zone: Asia/Shanghai
## tzcode source: internal
##
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base
##
## other attached packages:
## [1] dplyr_1.1.4        Matrix_1.6-5       Seurat_5.0.3       SeuratObject_5.0.1
## [5] sp_2.1-3
##
## loaded via a namespace (and not attached):
##   [1] RColorBrewer_1.1-3     rstudioapi_0.16.0      jsonlite_1.8.8
##   [4] magrittr_2.0.3         spatstat.utils_3.0-4   ggbeeswarm_0.7.2
##   [7] farver_2.1.1           rmarkdown_2.27         vctrs_0.6.5
##  [10] ROCR_1.0-11            spatstat.explore_3.2-6 htmltools_0.5.8.1
##  [13] sass_0.4.9             sctransform_0.4.1      parallelly_1.37.1
##  [16] KernSmooth_2.23-20     bslib_0.7.0            htmlwidgets_1.6.4
##  [19] ica_1.0-3              plyr_1.8.9             plotly_4.10.4
##  [22] zoo_1.8-12             cachem_1.0.8           igraph_2.0.3
##  [25] mime_0.12              lifecycle_1.0.4        pkgconfig_2.0.3
##  [28] R6_2.5.1               fastmap_1.1.1          fitdistrplus_1.1-11
##  [31] future_1.33.1          shiny_1.8.1.1          digest_0.6.35
##  [34] colorspace_2.1-0       patchwork_1.2.0        tensor_1.5
##  [37] RSpectra_0.16-1        irlba_2.3.5.1          labeling_0.4.3
##  [40] progressr_0.14.0       fansi_1.0.6            spatstat.sparse_3.0-3
##  [43] httr_1.4.7             polyclip_1.10-6        abind_1.4-5
##  [46] compiler_4.3.0         withr_3.0.0            fastDummies_1.7.3
##  [49] highr_0.11             MASS_7.3-58.4          tools_4.3.0
##  [52] vipor_0.4.7            lmtest_0.9-40          beeswarm_0.4.0
##  [55] httpuv_1.6.14          future.apply_1.11.1    goftest_1.2-3
##  [58] glue_1.7.0             nlme_3.1-162           promises_1.2.1
##  [61] grid_4.3.0             Rtsne_0.17             cluster_2.1.4
##  [64] reshape2_1.4.4         generics_0.1.3         gtable_0.3.4
##  [67] spatstat.data_3.0-4    tidyr_1.3.1            data.table_1.15.2
##  [70] utf8_1.2.4             spatstat.geom_3.2-9    RcppAnnoy_0.0.22
##  [73] ggrepel_0.9.5          RANN_2.6.1             pillar_1.9.0
##  [76] stringr_1.5.1          spam_2.10-0            RcppHNSW_0.6.0
##  [79] limma_3.58.1           later_1.3.2            splines_4.3.0
##  [82] lattice_0.21-8         survival_3.5-5         deldir_2.0-4
##  [85] tidyselect_1.2.1       miniUI_0.1.1.1         pbapply_1.7-2
##  [88] knitr_1.47             gridExtra_2.3          scattermore_1.2
##  [91] xfun_0.45              statmod_1.5.0          matrixStats_1.2.0
##  [94] stringi_1.8.3          lazyeval_0.2.2         yaml_2.3.8
##  [97] evaluate_0.24.0        codetools_0.2-19       tibble_3.2.1
## [100] cli_3.6.2              uwot_0.1.16            xtable_1.8-4
## [103] reticulate_1.35.0      munsell_0.5.0          jquerylib_0.1.4
## [106] Rcpp_1.0.12            globals_0.16.3         spatstat.random_3.2-3
## [109] png_0.1-8              ggrastr_1.0.2          parallel_4.3.0
## [112] ggplot2_3.5.0          presto_1.0.0           dotCall64_1.1-1
## [115] listenv_0.9.1          viridisLite_0.4.2      scales_1.3.0
## [118] ggridges_0.5.6         leiden_0.4.3.1         purrr_1.0.2
## [121] rlang_1.1.3            cowplot_1.1.3
```

**单细胞系列教程目录**

![](../../images/73d94b6f8a663b6d.gif) 单细胞数据分析系列教程：B站视频，先看一遍视频再去看推送操作，建议至少看三遍：https://www.bilibili.com/video/BV1S44y1b76Z/本公众号单细胞相关资料都可以在这里订阅：[scRNA-Seq学习手册2023_R语言版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500516&idx=1&sn=3c0b9de505fcd232054e38b451fa1742&chksm=9b3cbbb4ac4b32a26b61f3a1f7941fff5852d3e6e744ec680aafd0b84ec976a33bf982fb5f79&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Python版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&chksm=9b3caabdac4b23ab6e28425a4a5eb4d40ee3612e51f84f5d1e53ac91bef93f717e9e754398e3&scene=21#wechat_redirect>)

单细胞测序基础数据分析保姆级教程，代码部分整理在往期推送之中：[手把手教你做单细胞测序数据分析|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&chksm=9b3cb950ac4b30467a082527547b91aec15b7d1f40d44e362894aedeb6a99e014518fa5e4743&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|2.各类数据结构与读取方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499795&idx=2&sn=68e6298eb43633c71939c146d90230ff&chksm=9b3cb943ac4b3055e09739d77e037d679f3d9ec68780d1aa8c592f806fcc8d2322eaee78752d&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|3.单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|4.多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|5.细胞类型注释，从入门到入土](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&chksm=9b3cb8d7ac4b31c19c843810c7fe4341515df8ba6fff86a0ebff9d830edfcd656a29d18011c9&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|6组间差异分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=2&sn=d8c4ebf8f63d12bd2ac8e2607864f322&chksm=9b3cb8beac4b31a824e228b486f0d8dd21a8f4113a0a0bcbaf1b20eaade3a83c9c7c1184010b&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|7基因集富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21#wechat_redirect>)
[Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&scene=21#wechat_redirect>)

单细胞图片改造计划：[改造单细胞降维图| 1.DimPlot的探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496162&idx=1&sn=598c2920f7cc0697ee5a1fa6cadaee04&chksm=9b3c88b2ac4b01a415feeebbbec6c4891319439dc8dcdafd33cca7a1222e5adc723ae9d3a73d&scene=21#wechat_redirect>)
[改造单细胞降维图| 2.ggplot2中的DIY](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496239&idx=1&sn=1fe6fd4a7fb88ecc0456b4f5710cb5d6&chksm=9b3c8b7fac4b0269e0abeab951ad6ae0ddd1464dd9d1867280eeb9755fda5ba8f5237d88a7a6&scene=21#wechat_redirect>)
[改造单细胞降维图| 3.3D降维图与动图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498080&idx=2&sn=a9bcf65e3ae34ba201e8d49ee33c0728&chksm=9b3c8030ac4b0926c3f059a9a5d23f1bcdbcaf8e5a562eba2b7e3bec3396c44573269bd08e7b&scene=21&cur_album_id=2707677276481814529#wechat_redirect>)
[改造单细胞降维图| 4.一些造好的轮子](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498191&idx=1&sn=952312a6b26232d460bf787cc276543f&chksm=9b3c809fac4b098972c8c1dd83b9f954a38fe5b5f6bc7e295f3f3a7ba6c4c3d32951679ac24d&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&chksm=9b3ca933ac4b2025f922a325ec6893e93613f130ff1d4fd609e2d7274f7f1fdb5134092e28ad&scene=21#wechat_redirect>)
[改造单细胞FeaturePlot](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504616&idx=1&sn=f7b4a0e6b25d224380cd803e3463a3e4&chksm=9b3cabb8ac4b22aeb65e0d6ec32a1f8674dcf907da078ccb3b61e06c4aa035864ebec092f571&scene=21#wechat_redirect>)
[VlnPlot用法及ggplot复现](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504768&idx=1&sn=4fc5eb47037d3a80178e32975488d70b&chksm=9b3caad0ac4b23c61147cfb0f46ecd846568f37ce89c963eb5f069d3e89a8ba285897726bb3d&scene=21#wechat_redirect>)
[VlnPlot的ggplot改造](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=1&sn=b795a3e36ae092d8f87abb5a87187828&chksm=9b3caa9bac4b238dd33e905c33924b58aa4ff14e83abbf08046fba7fe765ecb0204163cb6acf&scene=21#wechat_redirect>)

SCENIC转录因子分析：[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|3.软件安装与数据准备](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|5.step1+step2构建共表达网络与regulon](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501692&idx=1&sn=3f7e263a93942ad03faa1ba5f8694ec4&chksm=9b3cbe2cac4b373af9db74a50ffb08a9b8a3b958fc6385c937385f0f7323bc935cdb0fe5275c&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|6.Step3 利用AUCell对Regulon评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501989&idx=1&sn=2700bf779d7d261a4d751d1635fdce2c&chksm=9b3cb1f5ac4b38e3014476242fe956cf510cc45b9f4cef86070af8094fd5f884f9d5c3a3363f&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|7.Step4 二元矩阵的计算与可视化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503995&idx=1&sn=26c7e9ec56af434e62b02853cfe667d6&chksm=9b3ca92bac4b203d7986645ab5a3fb574f44185c7ced8bd47957fa237d436a95bfa2579d052a&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|8.Step5 regulon聚类、分群、降维](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504024&idx=1&sn=143c0ec4d94b8fca0a4a47d3dc24415b&chksm=9b3ca9c8ac4b20de70a87acb2d3f810b0e1497071b1c6f14f1882a6d844fff016e9ba5581eb3&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|9.下游探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505276&idx=1&sn=949c753feb85d5877121433caaa33013&chksm=9b3cac2cac4b253affb587a937d3f5e0576851a4f4e1570cb7510a594d155873961bbd91758d&scene=21#wechat_redirect>)

上游fastq文件处理：
[单细胞分析的最上游——处理Fastq文件：cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501751&idx=2&sn=a79512f54db7456ea577de40f1a2d286&chksm=9b3cbee7ac4b37f1ce313d5eeb9a9ac9940640ab599ac5ab5d438fa86a8007796b768e4e68c2&scene=21#wechat_redirect>)
[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501812&idx=2&sn=7feb4d89ebc45ca7d64ad2dd5cd3c832&chksm=9b3cbea4ac4b37b2d2609172d58251076a6ab6a7043600613f0fb2ae0bea427de542b4dcf91e&scene=21#wechat_redirect>)[Cellranger报错：Unable to distinguish between [SC5P-R2, SC3Pv2] ...](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504739&idx=2&sn=e4e6ad0559b9b6a703d6ab37c2a8fdb0&chksm=9b3caa33ac4b23257424184bda44dd600ad98bc0dfdfa90ab0e3ebaf208e598b0b710fbafa4b&scene=21#wechat_redirect>)
[BD Rhapsody平台单细胞转录组定量流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506542&idx=1&sn=99cf7af7fc0d56b0d6fe7ea3596df2b6&chksm=9b3ca33eac4b2a28e6682a7cf0b2091a387a06ecf89ee10737cf2194286ec0bba472ef1c2b90&scene=21#wechat_redirect>)

细胞通讯B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1Ab4y1W7qx?p=1**往期推送**[《细胞通讯》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501282&idx=2&sn=cd37ea80e0b92f5bfbc98ea286e363da&chksm=9b3cbcb2ac4b35a4258d21fe003374795619fc2356376ebbe4ff640233f4b4c6e3e3ead41370&scene=21#wechat_redirect>)[《细胞通讯》2.1CellChat基础分析教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=2&sn=fb3e252d95ee8b50cd446e71335b1aa0&chksm=9b3cbca0ac4b35b621b4f51d2c3a130f00461faeeff067396222c2fc2eeb53f3544664d7d9bc&scene=21#wechat_redirect>)
[《细胞通讯》2.2CellChat多组别分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501523&idx=2&sn=6fa803f256c2e0b945f93ae7d8245f50&chksm=9b3cbf83ac4b3695b587e9817840f419104c8680f5ef08ee39aa149b79852f48b179f68e3397&scene=21#wechat_redirect>)
[《细胞通讯》CellChat学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501735&idx=2&sn=35fc792961507f4ae1cbae3a2882fba6&chksm=9b3cbef7ac4b37e1417d4108c8bd378c68c3907431ddfc52ad37c916e85649bb450d761a8e19&scene=21#wechat_redirect>)[CellChat空转细胞通讯合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512011&idx=1&sn=fbd41832c5995d79fead016931d3bfbd&chksm=9b3cd69bac4b5f8d16e7d8b8eeb5490e4938daf68902b06a8d60e25f150ec4ec459796f3aaac&scene=21#wechat_redirect>)
[SeekSpace细胞通讯分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511890&idx=1&sn=3457b875cd00b4433f50a39a45e1cb8a&chksm=9b3cd602ac4b5f144ad982dfbdf583b56d1bfb768e4e5f2cc9e5424af6e014e752835fadc8a6&scene=21#wechat_redirect>)

拟时序分析B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1br4y1x7Hf?p=1**往期推送**[《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)[《拟时序分析》3.monocle2实操：精简版拟时序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487398&idx=1&sn=6621eed90157d8da06ef778c40bd5554&chksm=9b3f76f6ac48ffe081ddfee3a323e0e31c1fda33731012de73168cf2ab30a226cf70c848f769&scene=21#wechat_redirect>)
[《拟时序分析》4.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》7.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)
[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494479&idx=1&sn=32f39c79c4c9fc07aa829eed49016da3&chksm=9b3c921fac4b1b091efcdd151500b69d19f71d5ca518122af697fc37e87acd915f3be5f63fb8&scene=21#wechat_redirect>)

scFAST系列[scFAST分析| 01.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503875&idx=1&sn=2b5ca0c57e17e51abb52adfe199c5736&chksm=9b3ca953ac4b20450f643b94bcfc95aa2b04ded197ce93e455a281901d7ccba099b48cfd03d9&scene=21#wechat_redirect>)
[scFAST分析| 02.单细胞分析准备工作](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504023&idx=1&sn=4091a22e853242b4aae7a7d3b4008f5c&chksm=9b3ca9c7ac4b20d1bb0389fad5fe85a3c4cf49179747fe97dffaab1087b7d2793668d9f63aa4&scene=21#wechat_redirect>)
[scFAST分析| 03.fast模块](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504044&idx=1&sn=d37991280217dcc29280efa344f856bb&chksm=9b3ca9fcac4b20eab124ccd4ba6ad3f5eee640df314e7d8fec0225035f06178e3a51dbe2033f&scene=21#wechat_redirect>)
[scFAST分析| 04.Seurat分析及可视化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504435&idx=1&sn=c6a6f7ca00684601f3cda49e53be5339&chksm=9b3cab63ac4b2275d993bbaa64c71652685065fa377be57319fc6a5c47eb958b3644c7459cd5&scene=21#wechat_redirect>)
[scFAST分析| 05.mut模块](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504878&idx=1&sn=2c5d9fc694eaf3e264c38b0691cd3a43&chksm=9b3caabeac4b23a87d201009137572c02ba1ea0dd747bcd8b8c02878b45917b6e235551c41cb&scene=21#wechat_redirect>)
[一文学会scFAST-seq数据分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505213&idx=1&sn=5f4ed0587dd96149d127a98d36f721f0&chksm=9b3cac6dac4b257bbc00c4647382d27883139bf06ab3071947bf1cccde8d1d501006dabab5f1&scene=21#wechat_redirect>)

其他单细胞相关技术贴也在这里：[单细胞必修课——Seurat流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512220&idx=1&sn=c71bc3f1ef007eb29be8b3b4ec10f0af&chksm=9b3cc9ccac4b40da749d2388dc2d885239a1e4f6ea0989f36b031c7253ce103b061e2605ad8c&scene=21#wechat_redirect>)
[scRNA-Seq双细胞过滤手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&chksm=9b3cd716ac4b5e00122eac47f55085198040a4a0e97c56895bbc39f3a9f1a1eb4eba27048a8f&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)[快速上手Seurat V5](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0&scene=21#wechat_redirect>)
[单细胞Figure 1常见图表](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509260&idx=1&sn=9ff90a428c3f22d43a31ec864e2d8a94&chksm=9b3cdc5cac4b554a2f7cb2a6368f7df9a9a3f6e406eb070663f53d81841a76e188c0b50727de&scene=21#wechat_redirect>)[细胞的数量由誰决定？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484056&idx=1&sn=4967a054f5241ff3a1bd4a6fe9a502b1&chksm=9b3f7bc8ac48f2deca3141461be035deb8658be184d78597af28f8ba2092d12f020768275248&scene=21#wechat_redirect>)[单细胞中应该如何做GSVA？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&chksm=9b3f7c4dac48f55bf1d11337406ab0e1295e8e1731dbac0715eedc99d11beff7f380e42dd49b&scene=21#wechat_redirect>)[答读者问（三）：单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)[答读者问（四）：如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)[答读者问（八）：为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)
[答读者问（十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)
[答读者问（十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析：Loupe Browser](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a&scene=21#wechat_redirect>)
[什么？不做单细胞也能分析细胞类群和免疫浸润？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485798&idx=1&sn=c849bc7a0093af92fc99e13b55842bb2&chksm=9b3f7036ac48f92048d726b38f2dd978d0b0cce779c1a4090aa4da5cb2df3ad30a5c5dbed27e&scene=21#wechat_redirect>)
[答读者问 （十三）查看Seurat对象时的ERROR：type='text'](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)
[各类单细胞对象（数据格式）转换大全（一）](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485925&idx=1&sn=14e08440200f0f5cb4dcc2dc615efeb8&chksm=9b3f70b5ac48f9a37a43cc2a8b2a5e485a3f84b4ef87949dfe99056bc6301b110e80800f6bb1&scene=21#wechat_redirect>)[单细胞对象(数据格式)转换大全|2. h5ad转Seuratobj](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496786&idx=1&sn=408a81e4824c33eaefe6e9e7f0143c7e&chksm=9b3c8d02ac4b0414bc1d11762b870248743bd9aaaef9d15480fd99a36322d47b448b229345be&scene=21#wechat_redirect>)
[批量整理好GEO中下载的单细胞数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486045&idx=1&sn=0b6874bcffc8abafb505cabce4c4fc0e&chksm=9b3f730dac48fa1b140ef01c07a7749e69df4fa7d2056deeed0673c668b6246724cd85741125&scene=21#wechat_redirect>)[答读者问 （十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)
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
[一文搞定空间转录组与单细胞测序的整合分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507210&idx=1&sn=f32037ffefd60b0d1bcca7bf9c3e0823&chksm=9b3ca45aac4b2d4cf0c68299db3a2891130d89d9e0fe2a9ecb34b394736550bcf7d7c51090cc&scene=21#wechat_redirect>)
[一文掌握十个单细胞数据库](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507979&idx=1&sn=e94225b592733f2e22b4b09245027365&chksm=9b3cd95bac4b504df8dc25d9c5cfddf56d3b47e7cc6f33a7ef369bc916c60abb6b49277b79f7&scene=21#wechat_redirect>)
[如何将已经构建好的Seurat空转对象转存为原始文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508133&idx=1&sn=297b8fb9cc8f33a1d19167dba1104e97&chksm=9b3cd9f5ac4b50e36df53e3e18bb2990d9635d88a725f1e54fc5eb5967ac9f0934b79cbb8b34&scene=21#wechat_redirect>)
[一文学会零代码单细胞分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511007&idx=1&sn=e7be3d9775890e5717889714629cfaf5&chksm=9b3cd28fac4b5b9936428d5f74d8b581b5cddc18d0fc42e2a5d75604cce080588d50f1304a17&scene=21#wechat_redirect>)
[SeekSpace| 会单细胞就会空间转录组](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511779&idx=1&sn=23868525d86a9ed7867a3837ed18612c&chksm=9b3cd7b3ac4b5ea502950d0278d68da978f6011b2597c3ec90fb77e79320883fb4a5be2d5399&scene=21#wechat_redirect>)
[10xGenomics官方可视化工具——Loupe Browser](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519698&idx=1&sn=0135ef1763fc146252835f2bd7f728ec&chksm=9b3cf482ac4b7d949d0936f11b487d5da4fd8f235bb86f63e960e23785885b9db0d14897b63d&scene=21#wechat_redirect>)

单细胞文献阅读：[13分+文章利用scRNA-Seq揭示地铁细颗粒物引起肺部炎症的分子机制](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511886&idx=1&sn=31c712d00377b0f0ed33703b5b4fbfd8&chksm=9b3cd61eac4b5f084fde14a2eb50356f2f40a66c608d38909f12a3d81f48cff029a09ce2ee8c&scene=21#wechat_redirect>)
[除了铁死亡，还有铜死亡？！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247518144&idx=1&sn=d036f1bb04b09eb73f53e2104d69404c&chksm=9b3cfe90ac4b77862f2f463b42132c7bfdb687a1b61d350dcf656117b1331271e179710fd4fa&scene=21#wechat_redirect>)
[拟时序分析神包—monocle的三篇《Nature》](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519064&idx=1&sn=173948cb696c7d33b90cd21b28986777&chksm=9b3cf208ac4b7b1e328fdc445f9aecd6cfb836fdb33767876ba1aa35c55098a2a071dbe8e2f0&scene=21#wechat_redirect>)
[测序技术的发展与应用](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495792&idx=2&sn=1aecc80b68f65f8a44a899df524038c0&chksm=9b3c8920ac4b0036b23268331b457a335b22b4fa3aed1db287ab79e7a4613df8d195bd11421a&scene=21#wechat_redirect>)[Biomamba助推的第二篇文章!发表了！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489823&idx=1&sn=6a5dddd53870395316d2b2e904c6ce72&chksm=9b3f604fac48e959e97e4b0317643efdcf117da7f8b75f1edbcd64dd8e2f07149e6031a94dd4&scene=21#wechat_redirect>)[又来了！Biomamba生信基地助推的第四篇文章!](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492532&idx=1&sn=cddb4691f23defc80b60da231790c53c&chksm=9b3c9ae4ac4b13f2334cc7f6b16eec1d8223800f6ecef71a93cfba21698ac5f4505dbd64f300&scene=21#wechat_redirect>)
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
[<IF=27.4> IgG4相关性疾病中颌下腺和血液中的细胞和分子改变](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503081&idx=1&sn=29890957ab75f050d466ca659292b529&chksm=9b3cb5b9ac4b3cafe279783c49cf7928819c5caeffbc34e52ae0c79f5e701ce8a25dd6f0c913&scene=21#wechat_redirect>)
[微生物组研究技术——微生物也能做单细胞](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488278&idx=1&sn=3662cde0f439a7e7cad7fb0d50082c05&chksm=9b3f6a46ac48e350318b38f1bfe252dd4c315ad058dc4b9aa02fadf2be2291fd0dac50f24cc6&scene=21#wechat_redirect>)
[scRNA-Seq+WGCNA+铁死亡：IF=9.69](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503498&idx=1&sn=fcf38bd6fd1dbaf80e203926bb63d5c4&chksm=9b3cb7daac4b3ecca9f2dd590fc581f5b1ae67a7f89be6f76eb438a017b5c335d8a01830b6a5&scene=21#wechat_redirect>)
[《Nature》: 单细胞解析大脑感知流感过程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503508&idx=1&sn=72781ff97ecae1c32815fe2c4d71b24e&chksm=9b3cb7c4ac4b3ed2b46c8c22f4ce8f93e3f93004ee76542bdd92039d301cec4a10077bb973db&scene=21#wechat_redirect>)
[两万字长文|当前单细胞 RNA-seq 分析的最佳实践](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503544&idx=1&sn=d563497cc912950d07c2284709f3aede&chksm=9b3cb7e8ac4b3efe66fa4e743f9d6c245a7dd6ea370cd0ee397e92761a2d680cac5c6dd4ea87&scene=21#wechat_redirect>)
[数百万级单细胞数据时代的多组学分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503603&idx=1&sn=c146eec4528f418226f0103030cb803c&chksm=9b3cb7a3ac4b3eb5bd8be7e41c8c440c80e8223fb10634bfc6d523fe389e3aa0bc14e5ea87d5&scene=21#wechat_redirect>)
[《Nature Methods》: NiCheNet, 能够考虑到胞内转录调控的细胞通讯软件](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503617&idx=1&sn=18389ffe1d201b1c0592ebc923aac851&chksm=9b3cb651ac4b3f4777cb0a6282ad99cd2aad711050d1590f20f970d843f05fb42f8cc02833e2&scene=21#wechat_redirect>)
[基于scRNA-Seq&空间转录组的AKI研究](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503664&idx=1&sn=39519d9cfa54e2d5b757f6c249ccbc86&chksm=9b3cb660ac4b3f768c8cfb708d8355c426b2d4ad39538acd5584aa9741ccdf1076b7112492df&scene=21#wechat_redirect>)
[自测蛋白质组+Bulk RNA-Seq & 挖掘scRNA-Seq=13.6分JASN](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504408&idx=1&sn=da427a6687b06a82d9dd58ae9f9aa474&chksm=9b3cab48ac4b225e8272d0475ae9295c1ea96172419aa604526f1b8a898748cb3897508d95a0&scene=21#wechat_redirect>)
[非监督式聚类在scRNA-Seq应用中的挑战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505257&idx=1&sn=a524a42b966007defbb2529d300d4c28&chksm=9b3cac39ac4b252f9f88181b932fdc279507c2affc765b53dbccf73084f86f0de25ab1af39bc&scene=21#wechat_redirect>)
[Seurat V5的《Nature Biotechnology》](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505826&idx=1&sn=5b9e4aeb41fc2f2943aeac9e22d4d038&chksm=9b3caef2ac4b27e4d57e75a508f00b5605ab99a7b51024110f54778683e14ed8bbcd743f0588&scene=21#wechat_redirect>)
[当空转遇上单细胞~](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505721&idx=1&sn=19d02b3858ebcf483d9e071b8ba00092&chksm=9b3cae69ac4b277f5b90fd75819ac8435226ad6daaf744f367d49ceb8099408e097d48656e2f&scene=21#wechat_redirect>)
[人类肾脏参考组织图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506567&idx=1&sn=e895c0d5a6dde49be76429e9961e61bf&chksm=9b3ca3d7ac4b2ac15dc4e2665e5d624b92bf85d8c94ac70c26e476444451c40a5286c853628f&scene=21#wechat_redirect>)
[有免疫特征的基质细胞，有没有可能是双细胞？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506493&idx=1&sn=ed65c6b0738a1fb8492da0b4ecdc9c63&chksm=9b3ca36dac4b2a7b4ca45f169526c6ed51777e20811d50c2892e683eee405c25607a42cc7a66&scene=21#wechat_redirect>)
[CAR-T治疗急性髓细胞性白血病的scRNA-Seq图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506371&idx=1&sn=a9f44bdfd795a4d04615bc307cd23cf5&chksm=9b3ca093ac4b29853f7f068e3969384ed07cd2cf4d64a55c423cd74bce83b914c96844a4cb3d&scene=21#wechat_redirect>)
[临床样本+单细胞+空转=IF4.8？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508744&idx=1&sn=1bc02443acab6d1720fe64e0334ce57a&chksm=9b3cda58ac4b534e3bf7ed2ab225d104d9976c5dc21b8443f88d3a555c5db67449b622ac91b4&scene=21#wechat_redirect>)
[鼻咽癌的Bulk RNA-Seq与scRNA-Seq联合分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510548&idx=1&sn=58048c46e837b1d56dffa282272c6d96&chksm=9b3cd344ac4b5a52369e91b4e61fa0a2c951b82cc21165b99f42ba2c2191d4add803bd73c928&scene=21#wechat_redirect>)
[GPTCelltype：玩GPT4玩出Nature](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510790&idx=1&sn=b56acf349e417f4ce1a09485256a5f87&chksm=9b3cd256ac4b5b400af5a809c5f595c8e1442513d277501c5bca1c80ce85f18a06a1d8994a9c&scene=21#wechat_redirect>)

单细胞注释复写[单细胞注释复写(一):Human Fetal Kidney](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447&scene=21#wechat_redirect>)[单细胞注释复写(二): human colorectal](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491642&idx=1&sn=2246fb702277ddc690f056fc8854142e&chksm=9b3c996aac4b107c059a403978eca7be1ae7987659626272c58430910ad75892ad470517aefb&scene=21#wechat_redirect>)
[单细胞复写|3.急性心肌梗塞(AMI)外周血scRNA-Seq分析实战(链接重置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501145&idx=2&sn=12c2e8d104ad343fc13acb8cda266e6c&chksm=9b3cbc09ac4b351f4ed708a0ed577a21f48ccb0d4173aed94a027b4170147ab85931ee51d1e5&scene=21#wechat_redirect>)
[单细胞复写|4. GSE157783数据集复现及差异分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503585&idx=1&sn=0035977a80621f09d0774d3c9b0a86cd&chksm=9b3cb7b1ac4b3ea76685ed44abcfb031c698835d9b9b42b269496f6104cd8c9d45467de7eddd&scene=21#wechat_redirect>)
[CellRank的教程重现](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507012&idx=1&sn=fb01cca63326fd6e8c682434a53fc2ea&chksm=9b3ca514ac4b2c02115ae5dea368190ce74997ac16a07fdc29f76cef815600b1e5b813c71163&scene=21#wechat_redirect>)
[人类肾脏scRNA-seq图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=2&sn=dec30ee34e483c3695613b3e41488a78&chksm=9b3ca77dac4b2e6b1734f1fd3d0134468b2ca8bc9f9118edc6e114a37f7ceea7dc4fa41b4556&scene=21#wechat_redirect>)
[小鼠纹状体单细胞基因变化图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506900&idx=1&sn=83774f3062e42ca0eee1df2cf19144f0&chksm=9b3ca284ac4b2b9221736162ac44280d6184c9f8b0cc13bbcc4c914c14b707fe13a850c6418e&scene=21#wechat_redirect>)
[T Cell单细胞参考图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506779&idx=1&sn=dc97a74cfac6caeabaa838160385c3b2&chksm=9b3ca20bac4b2b1da51998764b22ac3c08415298a47ded14283337386f18f9548749de70725e&scene=21#wechat_redirect>)
[MLP模型鉴定免疫细胞发育和瘤内T细胞耗竭的单细胞染色质图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506754&idx=1&sn=3e3e9b4857bb0371b7c1113df792df2e&chksm=9b3ca212ac4b2b043baf0c72684d186a1c065ff7b3d865c308aff4f3483ab5923638fda8d1ff&scene=21#wechat_redirect>)
[干细胞样CD4+ T细胞与自身免疫性血管炎](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506684&idx=1&sn=c27703a05d4fffae6a5e9e54b4fa7dfe&chksm=9b3ca3acac4b2abaa1e5d4f4a7e4d0730f2e5c4d72c7b3d3d29a653c3bae6590d90e31908dde&scene=21#wechat_redirect>)
[小鼠与人类的空间表观单细胞图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=1&sn=94c2a38b98957a9526d510798f791419&chksm=9b3ca77dac4b2e6b40d37e73f54791d55a919f50992bf62ac557ecbac919fb6415dca468dba4&scene=21#wechat_redirect>)
[人类肾脏scRNA-seq图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=2&sn=dec30ee34e483c3695613b3e41488a78&chksm=9b3ca77dac4b2e6b1734f1fd3d0134468b2ca8bc9f9118edc6e114a37f7ceea7dc4fa41b4556&scene=21#wechat_redirect>)
[胰腺导管腺癌的内异质性和恶性进展scRNA-seq图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507450&idx=1&sn=ee9b7d482ad9a88c6da18341c7ec5254&chksm=9b3ca4aaac4b2dbc83fc6cc4c084636fb397e56d0057dfb5b546acf402661ab64d241f985073&scene=21#wechat_redirect>)
[肝脏发育、成熟的单细胞图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507353&idx=1&sn=f2922ce2337c31a781a690ea59c5abde&chksm=9b3ca4c9ac4b2ddfc267838fe6d794027643e89fe054a5ca4d48e51976ea825af7fed285e26b&scene=21#wechat_redirect>)
[微环境中肿瘤免疫屏障决定了免疫治疗的效果](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507337&idx=1&sn=e23d849663a6cfcad19bacdaeeb85b5f&chksm=9b3ca4d9ac4b2dcf8ce4d9720bf7588a30e932adea4297862927ebfe20c29f8961436f761b8c&scene=21#wechat_redirect>)
[scRNA揭示T1D骨髓与骨质减少的关系](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507144&idx=1&sn=ed6e95f16601e6196cea7179b88db250&chksm=9b3ca598ac4b2c8ecfd1025246eb79c6aa8bf5703f8698d23f1d1f673121e3bf8168a32dba07&scene=21#wechat_redirect>)
[肝癌单细胞分群marker](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507136&idx=2&sn=16f8afe29fb59b9a8e9cac265098709c&chksm=9b3ca590ac4b2c86c9554bf20edd587f5d758636f55cf9e390220249d3338b1fde7717fb3c6e&scene=21#wechat_redirect>)
[胶质瘤相关巨噬细胞scRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507096&idx=1&sn=98e42a5768074d2766f2ce64214ac391&chksm=9b3ca5c8ac4b2cdebe68a8519a087e41a4c88a7e465c5ddc107f633a5fbf3fcc8bbff6aa8821&scene=21#wechat_redirect>)
[人类乳腺癌scRNA-seq数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507792&idx=2&sn=52dc1c2e5a23910ca0d8330ea917b60d&chksm=9b3ca600ac4b2f16a04624c74f2bcd3d24d300a835053a6f76ac4e1421b90c34b2ea01f1e7c8&scene=21#wechat_redirect>)
[肢端黑色素瘤细胞scRNA-seq图谱&免疫治疗](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507783&idx=1&sn=6ca5dc13a6aefbe78cce3f938fe04e40&chksm=9b3ca617ac4b2f01fb6e4677668f052f6361282ff394745394d363b54ea4c1eb58d2f30da30a&scene=21#wechat_redirect>)
[皮质神经注释复写](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507783&idx=2&sn=d1e28f5f4bddb3a3e4f1a85db1feac7f&chksm=9b3ca617ac4b2f01b40ae6adbe48e9371e50f9df543638e8c3e8e57bf9312b5daf731041ee16&scene=21#wechat_redirect>)
[非小细胞肺癌免疫治疗后肿瘤微环境重塑scRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507757&idx=1&sn=1045b58a64b4602881e9853d2a908012&chksm=9b3ca67dac4b2f6b4d33f10e71da2a6287968512677e77017b3820bf9aedfcd60301bb14d401&scene=21#wechat_redirect>)
[小鼠脑动脉瘤模型的scRNA-Seq分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507717&idx=2&sn=1d99c171cbfedc11f11fc827b643c89d&chksm=9b3ca655ac4b2f4360790bde80bc1452e9e314c6a0ae2dc6f9d19edbcc580e81ace3080dbb5f&scene=21#wechat_redirect>)
[儿童白血病的单细胞数据读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=2&sn=8d45c680ad78f52043d4ce4cbbf3c67a&chksm=9b3ca7bdac4b2eab2405773b5d71ff1f5495250ef813b24429e1b920c1b96a4ee391507d011b&scene=21#wechat_redirect>)
[疟疾中免疫细胞亚群的调控响应](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507659&idx=2&sn=a6860bb0eb8d3854a37acd0342777956&chksm=9b3ca79bac4b2e8dc0c3aa83c000894a53e2b316388495703e58d42ab205dd093bf578807b74&scene=21#wechat_redirect>)

硬件准备：
[生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=2&sn=c2ba75edc0382855cfc914c3bb713e7e&chksm=9b3caa9bac4b238d0690d2aa5a236c18c8ad8f0d7a23421eb63b5236ff1201c9ec99e12efc8f&scene=21#wechat_redirect>)[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502932&idx=1&sn=401d384d47616029375224b2d0a3c933&chksm=9b3cb504ac4b3c1299aac5c9f0747ccc36777390d2a939e1ed4af37c2836c1f7e8b4af612989&scene=21#wechat_redirect>)
![](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![](../../images/3b8e21da777157f9.webp)![](../../images/7a5130b05d387a24.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=1&sn=d9517a0803ad75cb7be430806834e7b8&chksm=9b3ca7bdac4b2eaba1ad01ed04ab1fbcbafcf4f6ddfe9e4f76ed9229707f545fe7d9c9ffd6ae&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（别问在么，添加时直接说来意）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/acba43cb3408c3d0.gif)您点的每个赞和在看，我都认真当成了喜欢
