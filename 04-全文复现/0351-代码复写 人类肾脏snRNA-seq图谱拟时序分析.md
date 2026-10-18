---
title: "代码复写| 人类肾脏snRNA-seq图谱拟时序分析"
date: 2024-01-05
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506960&idx=1&sn=9f5913231f9583411e47ccf0dcadedf6&chksm=9b3ca540ac4b2c56a60b5f71ab32e1eacd3194af4bfef819b2de60fc50781360876b45837bf7#rd
albums: ["全文复现"]
---

# 代码复写| 人类肾脏snRNA-seq图谱拟时序分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506960&idx=1&sn=9f5913231f9583411e47ccf0dcadedf6&chksm=9b3ca540ac4b2c56a60b5f71ab32e1eacd3194af4bfef819b2de60fc50781360876b45837bf7#rd
> 合集：全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是06号作品。本作品复写了题为"Single cell transcriptional and chromatin accessibility profiling redefine cellular heterogeneity in the adult human kidney"的论文，**文章链接** ：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8044133/**物种** ：人。**数据链接** ：https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE151302**复现图片集锦** ：

![](../../images/f6c378bc352f0a68.webp)

**文献思路** ：对5个健康成人肾脏标本进行了单核ATAC(snATAC-seq)和RNA(snRNA-seq)测序，以生成成对的、特定细胞类型的染色质可及性和成人肾脏的转录图谱。下述代码主要对部分snRNA-seq结果进行分析复现。

一、复写内容

##### (1) R包加载
```r
library(Seurat)
```
```
## Attaching SeuratObject
```
```r
library(ggplot2)
library(harmony)
```
```
## 载入需要的程辑包：Rcpp
```
```r
library(Rcpp)
library(DoubletFinder)
library(openxlsx)
library(here)
```
```
## here() starts at E:/生信/单细胞测序/Single cell transcriptional and chromatin accessibility profiling redefine cellular heterogeneity in the adult human kidney/寻因杯参数_王子彤
```
```r
library(dplyr)
```
```
##
## 载入程辑包：'dplyr'
```
```
## The following objects are masked from 'package:stats':
##
##     filter, lag
```
```
## The following objects are masked from 'package:base':
##
##     intersect, setdiff, setequal, union
```
```r
library(stringr)
library(tibble)
library(monocle)
```
```
## 载入需要的程辑包：Matrix
```
```
## 载入需要的程辑包：Biobase
```
```
## 载入需要的程辑包：BiocGenerics
```
```
##
## 载入程辑包：'BiocGenerics'
```
```
## The following objects are masked from 'package:dplyr':
##
##     combine, intersect, setdiff, union
```
```
## The following objects are masked from 'package:stats':
##
##     IQR, mad, sd, var, xtabs
```
```
## The following objects are masked from 'package:base':
##
##     anyDuplicated, append, as.data.frame, basename, cbind, colnames,
##     dirname, do.call, duplicated, eval, evalq, Filter, Find, get, grep,
##     grepl, intersect, is.unsorted, lapply, Map, mapply, match, mget,
##     order, paste, pmax, pmax.int, pmin, pmin.int, Position, rank,
##     rbind, Reduce, rownames, sapply, setdiff, sort, table, tapply,
##     union, unique, unsplit, which.max, which.min
```
```
## Welcome to Bioconductor
##
##     Vignettes contain introductory material; view with
##     'browseVignettes()'. To cite Bioconductor, see
##     'citation("Biobase")', and for packages 'citation("pkgname")'.
```
```
## 载入需要的程辑包：VGAM
```
```
## 载入需要的程辑包：stats4
```
```
## 载入需要的程辑包：splines
```
```
## 载入需要的程辑包：DDRTree
```
```
## 载入需要的程辑包：irlba
```

#### (2)读入数据
```
dir='GSE151302/'
samples=list.files( dir )
samples
```
```
## [1] "GSM4572192_Control1_filtered_feature_bc_matrix.h5"
## [2] "GSM4572193_Control2_filtered_feature_bc_matrix.h5"
## [3] "GSM4572194_Control3_filtered_feature_bc_matrix.h5"
## [4] "GSM4572195_Control4_filtered_feature_bc_matrix.h5"
## [5] "GSM4572196_Control5_filtered_feature_bc_matrix.h5"
```
```r
sceList = lapply(samples,function(pro){
  # pro=samples[1]
  sce=CreateSeuratObject( Read10X_h5(file.path(dir,pro)),
                          project = strsplit(pro,'_')[[1]][2],
                          min.cells = 5,
                          min.features = 300 )
  return(sce)
})
names(sceList) <-  str_split_fixed(samples,'_',3)[,2]

sce.all=merge(x=sceList[[1]],
              y=sceList[ -1 ],
              add.cell.ids = str_split(samples,'_',simplify = T)[,2])

as.data.frame(sce.all@assays$RNA@counts[1:10, 1:2])
```
```
##            Control1_AAACCTGAGGGTCTCC-1 Control1_AAACCTGAGTGTTAGA-1
## AL627309.1                           0                           0
## AL627309.2                           0                           0
## AL669831.5                           0                           0
## LINC00115                            0                           0
## FAM41C                               0                           0
## AL645608.7                           0                           0
## AL645608.1                           1                           0
## SAMD11                               0                           0
## NOC2L                                0                           0
## KLHL17                               0                           0
```
```
head(sce.all@meta.data, 10)
```
```
##                             orig.ident nCount_RNA nFeature_RNA
## Control1_AAACCTGAGGGTCTCC-1   Control1       3408         1860
## Control1_AAACCTGAGTGTTAGA-1   Control1       5339         2499
## Control1_AAACCTGCAAGCGCTC-1   Control1      10176         3578
## Control1_AAACCTGCACCAGATT-1   Control1       8909         3016
## Control1_AAACCTGCACGGCGTT-1   Control1        894          731
## Control1_AAACCTGCAGTCAGAG-1   Control1       2035         1314
## Control1_AAACCTGCATGGAATA-1   Control1      11821         3260
## Control1_AAACCTGGTATTCGTG-1   Control1      14906         4479
## Control1_AAACCTGGTTCGGGCT-1   Control1       8138         2709
## Control1_AAACCTGTCAGCACAT-1   Control1       1119          822
```
```
table(sce.all$orig.ident)
```
```
##
## Control1 Control2 Control3 Control4 Control5
##     6904     4229     6599     4494     4708
```

#### (3) 质控
```r
rnaAggr <- sce.all
rnaAggr <- PercentageFeatureSet(rnaAggr, pattern = "^MT-", col.name = "percent.mt") # 线粒体比例
rnaAggr <- PercentageFeatureSet(rnaAggr, pattern = "^RPL", col.name = "percent.rpl") # 核糖体蛋白L比例
rnaAggr <- PercentageFeatureSet(rnaAggr, pattern = "^RPS", col.name = "percent.rps") # 核糖体蛋白S比例

## 提取metadata
metadata <- rnaAggr@meta.data
metadata$orig.ident <- factor(metadata$orig.ident, levels = unique(metadata$orig.ident))
rnaAggr@meta.data <- metadata
orig.ident <- levels(unique(rnaAggr$orig.ident))

p1 <- VlnPlot(object = rnaAggr, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3, group.by = "orig.ident",pt.size=0)
p2 <- VlnPlot(object = rnaAggr, features = c("percent.rps", "percent.rpl"), ncol = 2, group.by = "orig.ident",pt.size=0)

p1/p2
```

![](../../images/c63dc3118c34d665.webp)
```
ggsave('plots/0_qc.png')
```
```
## Saving 7 x 5 in image
```
```r
rnaAggr <- subset(rnaAggr, subset = nFeature_RNA > 500 # use same filter params as aggr
                  & nFeature_RNA < 4000
                  & nCount_RNA < 16000
                  & percent.mt < 0.8
                  & percent.rps < 0.4
                  & percent.rpl < 0.4)
```

#### (4) 去除双细胞
```r
FindDoublets <- function(library_id, seurat_aggregate) {
  rnaAggr <- seurat_aggregate
  seurat_obj <- subset(rnaAggr, idents = library_id)
  seurat_obj <- NormalizeData(seurat_obj)
  seurat_obj <- ScaleData(seurat_obj)
  seurat_obj <- FindVariableFeatures(seurat_obj, selection.method = "vst", nfeatures = 2000)
  seurat_obj <- RunPCA(seurat_obj)
  # ElbowPlot(seurat_obj)
  seurat_obj <- FindNeighbors(seurat_obj, dims = 1:20)
  seurat_obj <- RunUMAP(seurat_obj, dims = 1:20)
  DimPlot(seurat_obj)

  ## pK Identification (no ground-truth) ---------------------------------------------------------------------------------------
  sweep.res.list_kidney <- paramSweep_v3(seurat_obj, PCs = 1:20, sct = F)
  sweep.stats_kidney <- summarizeSweep(sweep.res.list_kidney, GT = FALSE)
  bcmvn_kidney <- find.pK(sweep.stats_kidney)
  pK <- bcmvn_kidney %>% # select the pK that corresponds to max bcmvn to optimize doublet detection
    filter(BCmetric == max(BCmetric)) %>%
    select(pK)
  pK <- as.numeric(as.character(pK[[1]]))
  seurat_doublets <- doubletFinder_v3(seurat_obj, PCs = 1:20, pN = 0.25, pK = pK,
                               nExp = round(0.05*length(seurat_obj@active.ident)),
                               reuse.pANN = FALSE, sct = F)

  # create doublet groupings and visualize results
  DF.class <- names(seurat_doublets@meta.data) %>% str_subset("DF.classifications")
  pANN <- names(seurat_doublets@meta.data) %>% str_subset("pANN")

  p1 <- ggplot(bcmvn_kidney, aes(x=pK, y=BCmetric)) +
    geom_bar(stat = "identity") +
    ggtitle(paste0("pKmax=",pK)) +
    theme(axis.text.x = element_text(angle = 90, hjust = 1))
  p2 <- DimPlot(seurat_doublets, group.by = DF.class)
  p3 <- FeaturePlot(seurat_doublets, features = pANN)

  outFile <- paste0("doublets.",library_id,".pdf")
  # pdf(here("plots",outFile))
  pdf(paste0('plots/', outFile))
    print(p1) # need to use print() when drawing pdf in a function call
    print(p2)
    print(p3)
  dev.off()

  # create a df of barcodes and doublet designations
  df_doublet_barcodes <- as.data.frame(cbind(rownames(seurat_doublets@meta.data), seurat_doublets@meta.data[[DF.class]]))
  return(df_doublet_barcodes)
}

Idents(rnaAggr) <- "orig.ident"
list.doublet.bc <- lapply(orig.ident, function(x) {FindDoublets(x, seurat_aggregate = rnaAggr)})
saveRDS(list.doublet.bc,"temp/list.doublet.bc.rds")
```
```r
list.doublet.bc <- readRDS('temp/list.doublet.bc.rds')
doublet_id <- list.doublet.bc %>%
  bind_rows() %>%
  dplyr::rename("doublet_id" = "V2") %>%
  tibble::column_to_rownames(var = "V1") # this is the barcode column
table(doublet_id)
rnaAggr <- AddMetaData(rnaAggr,doublet_id)
Idents(rnaAggr) <- "doublet_id"
rnaAggr <- subset(rnaAggr,idents = "Singlet")
saveRDS(rnaAggr,"temp/rnaAggr_singlet.rds")
```

#### (4) 细胞聚类
```r
rnaAggr <- readRDS("temp/rnaAggr_singlet.rds")
rnaAggr <- SCTransform(rnaAggr, vars.to.regress = c("percent.mt","percent.rpl", "percent.rps","nCount_RNA"), verbose = TRUE)
rnaAggr <- RunPCA(rnaAggr, verbose = TRUE)
# ElbowPlot(rnaAggr, ndims = 50) # to determine number of dimensions for clustering
rnaAggr <- RunHarmony(rnaAggr, "orig.ident", plot_convergence = TRUE)
rnaAggr <- FindNeighbors(rnaAggr, dims = 1:24, verbose = TRUE, reduction = "harmony")
rnaAggr <- FindClusters(rnaAggr, verbose = TRUE, resolution = 0.7, reduction = "harmony")
rnaAggr <- RunUMAP(rnaAggr, dims = 1:24, verbose = TRUE, reduction = "harmony")
saveRDS(rnaAggr, 'temp/rnaAggr_UMAP.rds')
```

#### (5)细胞注释
```r
rnaAggr <- readRDS('temp/rnaAggr_UMAP.rds')
p1 <- DimPlot(rnaAggr, reduction = "umap",  label = TRUE) + ggtitle("snRNA Seurat Clustering with Harmony No Doublets")

celltype.markers <- c("CUBN","HAVCR1","SLC5A1","SLC5A2", # PT and PT-VCAM1+ markers
                      "CFH", # PEC
                      "SLC12A1", # TAL NKCC2
                      "SLC12A3","TRPM6", # DCT1 and DCT2 NCC
                      "SCNN1G","TRPV5", # DCT2/CNT ENaC
                      "CALB1", # CNT
                      "AQP2", # PC
                      "ATP6V0D2", # ICA and ICB
                      "SLC4A1","SLC26A7", # ICA
                      "SLC26A4", # ICB
                      "NPHS1","NPHS2", # PODO
                      "PECAM1","FLT1","EMCN", # ENDO
                      "CLDN5", # GEC
                      "ITGA8","PDGFRB", # MES
                      "ACTA2","CALD1", # FIB
                      "PTPRC") # WBC
p2 <- DotPlot(rnaAggr, features = celltype.markers) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
p1/p2

rnaAggr[["orig.clusters"]] <- Idents(object = rnaAggr) # stash cluster idents prior to annotation
new.cluster.ids <- c("DCT1","PT","PT","CNT","TAL",
                     "TAL","ICA","TAL","PC","PEC",
                     "ENDO","PT_VCAM1","DCT2","PODO","ICB",
                     "ENDO","MES","FIB","ENDO","LEUK")
names(new.cluster.ids) <- levels(rnaAggr)
rnaAggr <- RenameIdents(rnaAggr, new.cluster.ids)

# reorder the idents and save celltype annotations in celltype slot metadata
levels(rnaAggr) <- rev(c("PT","PT_VCAM1","PEC","TAL","DCT1",
                     "DCT2","CNT","PC","ICA","ICB",
                     "PODO","ENDO","MES","FIB","LEUK"))
rnaAggr@meta.data$celltype <- rnaAggr@active.ident

# reset celltype as primary ident before saving and plotting
Idents(rnaAggr) <- "celltype"

# redraw umap and dotplot with reordered idents
DefaultAssay(rnaAggr) <- "SCT"
p3 <- DimPlot(rnaAggr, reduction = "umap",  label = TRUE) + ggtitle("snRNA Annotated Celltypes")
celltype.markers2 <- c('CUBN', 'HAVCR1','CFH', 'SLC12A1', 'SLC12A3',"TRPV5",
                       'CALB1','AQP2','SLC26A7','NPHS2', 'EMCN','ITGA8',
                       'CALD1','PTPRC')
p4 <- DotPlot(rnaAggr, features = celltype.markers2,
              cols = c("lightyellow","royalblue")) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
p3/p4

# draw pdf plots for before and after annotation
dir.create("plots", showWarnings = FALSE)
pdf(here("plots","umap.rnaAggr.control.pdf"))
list(p1,p2,p3,p4)
dev.off()
```

#### (6) 保存数据
```
# save preprocessed rnAggr file
print("Saving aggregated snRNAseq object as rnaAggr.rds in:")
dir.create("cellranger_rna_prep", showWarnings = FALSE)
here("cellranger_rna_prep")
saveRDS(rnaAggr, file = here("cellranger_rna_prep","rnaAggr_control.rds"))
```

#### (7)绘图
```r
rnaAggr <- readRDS("cellranger_rna_prep/rnaAggr_control.rds")
Idents(rnaAggr) <- "celltype"

# 整体聚类注释
DimPlot(rnaAggr, reduction = "umap", label = TRUE) +
  ggtitle("snRNA Annotated Celltypes")
```

![](../../images/961123250906908e.webp)
```
ggsave('plots/fig1b.png')
```
```
## Saving 7 x 5 in image
```
```r
# 各聚类细胞基因表达量
celltype.markers <- c('CUBN', 'HAVCR1','CFH', 'SLC12A1', 'SLC12A3',"TRPV5",
                       'CALB1','AQP2','SLC26A7','NPHS2', 'EMCN','ITGA8',
                       'CALD1','PTPRC')
DotPlot(rnaAggr, features = celltype.markers,
              cols = c("lightyellow","royalblue")) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
```

![](../../images/5d3abfd2c4a0a0f9.webp)
```
ggsave('plots/fig1c.png')
```
```
## Saving 7 x 5 in image
```
```
# 各样本聚类
DimPlot(rnaAggr,reduction = "umap",split.by = "orig.ident")
```

![](../../images/33094e727c20092e.webp)
```
ggsave('plots/figs3a.png')
```
```
## Saving 7 x 5 in image
```
```
FeaturePlot(rnaAggr,features = "HNF4A",order=T, label = T)
```

![](../../images/3c93fa2a48648d26.webp)
```
ggsave('plots/fig3b5.png')
```
```
## Saving 7 x 5 in image
```
```
FeaturePlot(rnaAggr,features = "TFAP2B",order=T, label = T)
```

![](../../images/3659366fffb4a4b2.webp)
```
ggsave('plots/fig3b6.png')
```
```
## Saving 7 x 5 in image
```

#### (8)时序分析
```r
rnaAggr <- readRDS("cellranger_rna_prep/rnaAggr_control.rds")
# 构建cds对象
expr_matrix = as(as.matrix(rnaAggr@assays$RNA@counts), 'sparseMatrix') #大数据集使用稀疏矩阵，节省内存，加快运算
count_data <- GetAssayData(rnaAggr, assay = "RNA",slot = "counts")
gene_metadata <- as.data.frame(rownames(count_data))
colnames(gene_metadata) <- "gene_short_name"
rownames(gene_metadata) <- gene_metadata$gene_short_name
sample_sheet<-rnaAggr@meta.data#将实验信息赋值新变量

pd <- new("AnnotatedDataFrame", data = sample_sheet)
fd <- new("AnnotatedDataFrame", data = gene_metadata)
cds <- newCellDataSet(expr_matrix, phenoData = pd, featureData = fd,
                      lowerDetectionLimit = 0.5, expressionFamily = negbinomial.size())
# 过滤PT
valid_cells <- row.names(subset(pData(cds), celltype %in% c('PT', 'PT_VCAM1')))
cds <- cds[,valid_cells]

# 预处理
cds <- estimateSizeFactors(cds) # 标准化
cds <- estimateDispersions(cds) # 为后续差异分析做准备
## 筛选平均表达量 > 0.1的基因用于聚类
disp_table <- dispersionTable(cds)
unsup_clustering_genes <- subset(disp_table, mean_expression >= 0.1)
## 过滤小于100个细胞中表达的基因
cds <- detectGenes(cds, min_expr = 0.1) # 在fData(cds)中添加列num_cells_expressed
express_gene <- rownames(subset(fData(cds), num_cells_expressed >=100 ))
target_gene <- intersect(unsup_clustering_genes$gene_id, express_gene)
cds <- setOrderingFilter(cds, unsup_clustering_genes$gene_id)

# 降维
cds <- reduceDimension(cds, max_components = 2,
                       method = 'DDRTree')
cds <- orderCells(cds) # root_state设置根
save(cds, file = 'cellranger_rna_prep/cds.Rdata')
```
```r
# 绘图
load('cellranger_rna_prep/cds.Rdata')
p1 <- plot_cell_trajectory(cds, color_by = "Pseudotime")+
  scale_colour_gradientn(colours = c("purple", "red",'yellow'))
```
```
## Warning: `select_()` was deprecated in dplyr 0.7.0.
## i Please use `select()` instead.
## i The deprecated feature was likely used in the monocle package.
##   Please report the issue to the authors.
## This warning is displayed once every 8 hours.
## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
## generated.
```
```r
p2 <- plot_cell_trajectory(cds, color_by = "celltype")+
  scale_color_brewer(palette = 'Set1')
p1|p2
```

![](../../images/6da600b75a38e529.webp)
```
ggsave('plots/fig6a1.png')
```
```
## Saving 7 x 5 in image
```
```r
keygenes <- c('VCAM1', 'TPM1', 'SLC5A12', 'SLC4A4')
cds_subset <- cds[keygenes,]
plot_genes_in_pseudotime(cds_subset,color_by='celltype')
```

![](../../images/fc1f47eab524c6e8.webp)
```
ggsave('plots/fig6a2.png')
```
```
## Saving 7 x 5 in image
```

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：

https://pan.baidu.com/s/11bPVwXVXLLa2hgFH3IBd7g?pwd=6qq4

提取码：6qq4

![](../../images/1ef1104961ee28dd.jpg)

02

三、合作方介绍

****本次活动由**Biomamba生信基地** 组织主办、**北京寻因生物科技** 有限公司独家冠名、科研者之家、西柚云超算联合赞助，设立总价值约**50W** 的科研助力基金。
北京寻因生物科技有限公司：

北京寻因生物科技有限公司（简称寻因生物）成立于2018年，秉承“用技术温暖生命，预见未来”的企业愿景，致力于全球单细胞市场标准普世化发展，推动单细胞技术在早筛、临床、药研等应用方向的深耕落地，为全球科学家、技术公司及药企工业等客户提供可信赖的高品质单细胞技术服务及实验室建设解决方案。

科研者之家：

科研者之家（www.home-for-researchers）是目前国内最知名的科研工具箱平台，以“科研不停，神器不止”为理念，自2019年上线以来，多款工具火爆科研界，如AI写作助手、Figdraw在线绘图平台、生信零代码平台、AI润色、DLP一键改写降重、中文版Pubmed、课题思路助手等。截止目前，包括Nature，Advanced Materials等顶级期刊在内，科研者之家相关科研工具被论文引用已超2300次之多。

西柚云超算：

西柚云是一家专注于科研共享计算的云服务基建型公司。于2022年推出独立研发的大禹共享型计算系统，具有实例动态迁移（拒绝传统型共享服务器单节点卡顿）、开箱即用的生信环境、每个用户拥有[独立的实例和root权限](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)等特性。

03

四、往期作品回顾

[干细胞样CD4+ T细胞与自身免疫性血管炎](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506684&idx=1&sn=c27703a05d4fffae6a5e9e54b4fa7dfe&chksm=9b3ca3acac4b2abaa1e5d4f4a7e4d0730f2e5c4d72c7b3d3d29a653c3bae6590d90e31908dde&scene=21#wechat_redirect>)
[结直肠癌免疫图谱中的基因表达程序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506720&idx=2&sn=4760277df5a7b6f0d6d1698ac734aa3b&chksm=9b3ca270ac4b2b66b0330e822893fa233ba3bdfd45d857097fba6e86561196c1497c20db25b8&scene=21#wechat_redirect>)
[MLP模型鉴定免疫细胞发育和瘤内T细胞耗竭的单细胞染色质图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506754&idx=1&sn=3e3e9b4857bb0371b7c1113df792df2e&chksm=9b3ca212ac4b2b043baf0c72684d186a1c065ff7b3d865c308aff4f3483ab5923638fda8d1ff&scene=21#wechat_redirect>)
[T Cell单细胞参考图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506779&idx=1&sn=dc97a74cfac6caeabaa838160385c3b2&chksm=9b3ca20bac4b2b1da51998764b22ac3c08415298a47ded14283337386f18f9548749de70725e&scene=21#wechat_redirect>)
[小鼠纹状体单细胞基因变化图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506900&idx=1&sn=83774f3062e42ca0eee1df2cf19144f0&chksm=9b3ca284ac4b2b9221736162ac44280d6184c9f8b0cc13bbcc4c914c14b707fe13a850c6418e&scene=21#wechat_redirect>)

04

**本次活动最终解释权归主办方所有!********主办方拥有对作品的编辑、宣发权利!**

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
