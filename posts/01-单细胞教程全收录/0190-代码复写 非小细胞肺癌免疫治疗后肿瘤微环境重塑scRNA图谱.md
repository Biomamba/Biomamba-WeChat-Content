---
title: "代码复写| 非小细胞肺癌免疫治疗后肿瘤微环境重塑scRNA图谱"
date: 2024-01-20
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507757&idx=1&sn=1045b58a64b4602881e9853d2a908012&chksm=9b3ca67dac4b2f6b4d33f10e71da2a6287968512677e77017b3820bf9aedfcd60301bb14d401#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写| 非小细胞肺癌免疫治疗后肿瘤微环境重塑scRNA图谱

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507757&idx=1&sn=1045b58a64b4602881e9853d2a908012&chksm=9b3ca67dac4b2f6b4d33f10e71da2a6287968512677e77017b3820bf9aedfcd60301bb14d401#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是19号作品。本作品复写了题为"Tumor microenvironment remodeling after neoadjuvant immunotherapy in non-small cell lung cancer revealed by single-cell RNA sequencing"的论文.**文章链接** ：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985263/**数据原始链接：** 投稿人未提供**复现图片集锦** ：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialprgXAwdToS9hgicyoicSGaiaCV10Xv6hl3deUiahKUG306mq6vfMRoibD1Bw/640?wx_fmt=png&from=appmsg)

**文献简介** ：投稿人未提供

一、复写内容

rmd文件：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
---title: "Untitled"output: html_documentdate: "2023-12-19"---
```
{r setup, include=FALSE}knitr::opts_chunk$set(echo = TRUE)```
## all
```
{r packages}library(data.table)library(Seurat)library(dplyr)library(DoubletFinder)library(ggplot2)```
```
{r}#读取数据data <- fread("./GSE207422_NSCLC_scRNAseq_UMI_matrix.txt.gz", data.table = F)data[1:10, 1:10]```
```
{r}rownames(data) <- data$Genedata[1:10, 1:10]```
```
{r}data <- select(data, -Gene)data[1:10, 1:10]```
```
{r}#创建Seurat对象S <- CreateSeuratObject(counts = data)#saveRDS(S, file = "orig_data.rds")```
```
{r}#QC#计算线粒体相关基因百分比mito_genes <- rownames(S)[grep("^MT-", rownames(S))]head(mito_genes)S <- PercentageFeatureSet(S, features = mito_genes, col.name = "percent_mito")```
```
{r}#计算核糖体相关基因百分比ribo_genes <- rownames(S)[grep("^RP[SL]", rownames(S))]head(ribo_genes)S <- PercentageFeatureSet(S, features = ribo_genes, col.name = "percent_ribo")```
```
{r}#计算housekeeping基因表达量housekeeping_genes <- c("ACTB","GAPDH","MALAT1")hw_data <- data[housekeeping_genes, ]hw_data[1:3,1:5]housekeeping_UMI <- colSums(hw_data)sum(housekeeping_UMI <= 1)S <- AddMetaData(object = S, metadata = housekeeping_UMI, col.name = "housekeeping_UMI")```
```
{r}#过滤head(S@meta.data)dim(S)S <- subset(S, subset = nFeature_RNA >= 500 & percent_mito <= 20 & percent_ribo <= 50 & housekeeping_UMI >= 1)dim(S)```
```
{r}#降维聚类S <- NormalizeData(S)S <- FindVariableFeatures(S)S <- ScaleData(S)S <- RunPCA(S)ElbowPlot(S)S <- FindNeighbors(S, dims = 1:15, resuction = "pca")S <- FindClusters(S, resolution = 0.6)S <- RunUMAP(S, dims = 1:15)#saveRDS(S, file = "normaliza_data.rds")```
```
{r}#去除双细胞sweep.res.list_S <- paramSweep_v3(S, PCs = 1:15, sct = FALSE)head(sweep.res.list_S)sweep.stats_S <- summarizeSweep(sweep.res.list_S, GT = FALSE)bcmvn_S <- find.pK(sweep.stats_S) #可以看到最佳参数的点mpK<-as.numeric(as.vector(bcmvn_S$pK[which.max(bcmvn_S$BCmetric)])) #最佳参数annotations <- S@meta.data$seurat_clustershomotypic.prop <- modelHomotypic(annotations)  DoubletRate = 0.025nExp_poi <- round(DoubletRate*length(S$seurat_clusters))nExp_poi.adj <- round(nExp_poi*(1-homotypic.prop)) #计算双细胞比例S <- doubletFinder_v3(S, PCs = 1:10, pN = 0.25, pK = mpK, nExp = nExp_poi, reuse.pANN = FALSE, sct = F)S <- doubletFinder_v3(S, PCs = 1:10, pN = 0.25, pK = mpK, nExp = nExp_poi.adj, reuse.pANN = FALSE, sct = F)#saveRDS(S, file = "countdoublet_data.rds")```
```
{r}table(S$DF.classifications_0.25_0.28_2057)DimPlot(S, reduction = "umap", group.by ="DF.classifications_0.25_0.28_2057",cols =c("black", "red"))```
```
{r}S <- subset(S, subset = DF.classifications_0.25_0.28_2057 == 'Singlet')dim(S)```
```
{r}#CCA整合#S <- readRDS(file = "countdoublet_data.rds")S@meta.data$orig.ident <- substr(rownames(S@meta.data), 1, 11)table(S$orig.ident)DimPlot(S, group.by = "orig.ident")S_list <- SplitObject(S, split.by = "orig.ident")S_listS_list <- lapply(X = S_list, FUN = function(x) {  x <- NormalizeData(x)  x <- FindVariableFeatures(x, selection.method = "vst", nfeatures = 3000)})features <- SelectIntegrationFeatures(object.list = S_list)S_anchors <- FindIntegrationAnchors(object.list = S_list, anchor.features = features, dims = 1:20)S_combined <- IntegrateData(anchorset = S_anchors, dims = 1:20)DefaultAssay(S_combined) <- "integrated"S_combined <- ScaleData(S_combined)S_combined <- RunPCA(S_combined)ElbowPlot(S_combined)S_combined <- FindNeighbors(S_combined, reduction = "pca", dims = 1:20)S_combined <- FindClusters(S_combined, resolution = c(0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8))S_combined <- RunUMAP(S_combined, reduction = "pca", dims = 1:20)head(S_combined@meta.data)DimPlot(S_combined, group.by = "integrated_snn_res.0.2")#saveRDS(S_combined, file = "combined_data.rds")```
```
{r}#细胞注释DefaultAssay(S_combined) <- "RNA"DimPlot(S_combined, group.by = "integrated_snn_res.0.7", label = T)```
```
{r}#B cell:'CD79A', 'CD19', 'MS4A1', 'IGHM'    FeaturePlot(S_combined, features = c('CD79A', 'CD19', 'MS4A1', 'IGHM'), ncol = 2)``````{r}#Epithelium:'EPCAM', 'KRT19', 'KRT8', 'KRT7' FeaturePlot(S_combined, features = c('EPCAM', 'KRT19', 'KRT8', 'KRT7'), ncol = 2)```
```
{r}#Stromal cell:'COL1A2', 'DCN', 'COL6A2', 'VWF'  FeaturePlot(S_combined, features = c('COL1A2', 'DCN', 'COL6A2', 'VWF'), ncol = 2)```
```
{r}#Mast cell:'CPA3', 'MS4A2', 'KIT'  FeaturePlot(S_combined, features = c('CPA3', 'MS4A2', 'KIT'), ncol = 2)```
```
{r}#Myeloid cell:'LYZ', 'MARCO', 'C1QB'  FeaturePlot(S_combined, features = c('LYZ', 'MARCO', 'C1QB'), ncol = 2)```
```
{r}#Neutrophil:'FCGR3B', 'CXCR2', 'S100A8', 'S100A9'   FeaturePlot(S_combined, features = c('FCGR3B', 'CXCR2', 'S100A8', 'S100A9'), ncol = 2)```
```
{r}#NK cell:mature:'KLRD1', 'KLRF1', 'CD8A'   FeaturePlot(S_combined, features = c('KLRD1', 'KLRF1', 'CD8A'), ncol = 2)```
```
{r}#pDC:'CLEC4C', 'LILRA4', 'IL3RA' FeaturePlot(S_combined, features = c('CLEC4C', 'LILRA4', 'IL3RA'), ncol = 2)```
```
{r}#Plasma cell:'IGHG1', 'JCHAIN', 'MZB1' FeaturePlot(S_combined, features = c('IGHG1', 'JCHAIN', 'MZB1'), ncol = 2)```
```
{r}#T cell:'CD3E', 'TRBC2', 'TRAC', 'CD2' FeaturePlot(S_combined, features = c('CD3E', 'TRBC2', 'TRAC', 'CD2'), ncol = 2)```
```
{r}dim(S_combined)S_combined@meta.data$celltype <- NAhead(S_combined@meta.data)S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(3)] <- 'B cell'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(5, 13, 14, 19, 22)] <- 'Epithelium'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(18)] <- 'Stromal cell'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(20)] <- 'Mast cell'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(7, 8, 10, 17, 21)] <- 'Myeloid cell'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(6, 11)] <- 'Neutrophil'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(0, 1, 2, 4, 9, 15, 16, 24)] <- 'T/NK cell'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(23)] <- 'pDC'S_combined@meta.data$celltype[S_combined@meta.data$integrated_snn_res.0.7 %in% c(12)] <- 'Plasma cell'sum(table(S_combined$celltype))sum(table(S_combined$integrated_snn_res.0.6))```
```
{r}#标注样本信息S_combined@meta.data$group <- paste0('P', substr(S_combined@meta.data$orig.ident, 10, 11))head(S_combined@meta.data)S_combined@meta.data$RECIST[S_combined@meta.data$group %in% c('P01', 'P05', 'P08')] <- 'TN'S_combined@meta.data$RECIST[S_combined@meta.data$group %in% c('P03', 'P06', 'P11', 'P14')] <- 'MPR'S_combined@meta.data$RECIST[S_combined@meta.data$group %in% c('P02', 'P04', 'P07', 'P09', 'P10', 'P12', 'P13', 'P15')] <- 'NMPR'table(S_combined$RECIST)#saveRDS(S_combined, file = "celltype_data.rds")```
```
{r}#S_combined <- readRDS("./celltype_data.rds")DimPlot(S_combined, group.by = "celltype")```
```
{r}table(S_combined$orig.ident)```
```
{r}Idents(S_combined) <- S_combined$celltypeprop.table(table(Idents(S_combined)))table(Idents(S_combined), S_combined$group)Cellratio <- prop.table(table(Idents(S_combined), S_combined$group), margin = 2)Cellratio <- as.data.frame(Cellratio)```
```
{r}ggplot(Cellratio) +   geom_bar(aes(x = Var2, y = Freq, fill = Var1),stat = "identity",width = 0.7, size = 0.5, colour = '#222222')+   theme_classic() +  labs(y = 'Fraction', x = element_blank()) +  theme(panel.border = element_rect(fill = NA, color = "black", size = 0.5, linetype = "solid")) +  guides(fill = guide_legend(title = 'celltype'))```
```
{r}table(S_combined$celltype)``````{r}S_immune <- subset(S_combined, subset = celltype %in% c('T/NK cell', 'B cell', 'Myeloid cell', 'Neutrophil'))phe <- S_immune@meta.data```
```
{r}phe$patient =  paste(phe$group, phe$RECIST, sep = '_')tb <- table(phe$celltype, phe$patient)head(tb)```
```
{r}bar_data <- as.data.frame(tb)bar_per <- bar_data %>%  group_by(Var2) %>%  mutate(sum(Freq)) %>%  mutate(percent = Freq/`sum(Freq)`)head(bar_per)bar_per$Var2```
```
{r}group <- ifelse(str_detect(bar_per$Var2, "TN"), "TN", ifelse(str_detect(bar_per$Var2, "NMPR"), "NMPR", "MPR"))bar_per$group <- grouphead(bar_per)```
```
{r}bar_per$group = factor(bar_per$group, levels = c("TN", "MPR", "NMPR"))table(bar_per$Var1)```
```
{r}bar_per$Var1 = factor(bar_per$Var1, levels = c("T/NK cell", "B cell", "Myeloid cell", "Neutrophil"))head(bar_per)```
```
{r}library(gridExtra)p <- list()for(i in 1:4){  celltype_data <- bar_per[bar_per$Var1 == unique(bar_per$Var1)[i],]  p[[i]] <- ggplot(celltype_data, aes(x = group, y = percent, fill = group)) +    geom_boxplot(size = 0.5, fill = "white", outlier.fill = "white", outlier.color = "white", colour = c('#4169E1', '#FF7F50', '#3CB371')) +    geom_jitter(aes(fill = group), width = 0.2, shape = 21, size = 2) +    ggtitle(paste0(unique(bar_per$Var1)[i], " ")) +    theme_bw() +    theme(legend.position = "none",          axis.text.x = element_text(colour = "black", family = "Times", size = 14),          axis.text.y = element_text(family = "Times", size = 14, face = "plain"),          axis.title.y = element_text(family = "Times", size = 14, face = "plain"),          axis.title.x = element_text(family = "Times", size = 14, face = "plain"),          plot.title = element_text(family = "Times", size = 15, face = "bold", hjust = 0.5),          panel.grid.major = element_blank(),          panel.grid.minor = element_blank()) +    ylab("Fraction (%) of immune cells") + xlab(" ")  p[[i]] <- p[[i]] + theme(axis.title.y = element_blank())}p <- grid.arrange(grobs = p, ncol = 4, left = "Fraction (%) of immune cells")p```

## TNK cell```{r}library(harmony)library(pheatmap)library(ggplot2)library(gplots)library(ComplexHeatmap)library(ggplot2)library(dplyr)library(monocle)
#S_combined <- readRDS(file = "celltype_data.rds")table(S_combined@meta.data$celltype)TNK <- subset(S_combined, subset = celltype == "T/NK cell")dim(TNK)TNK <- NormalizeData(TNK, normalization.method = "LogNormalize")TNK <- FindVariableFeatures(TNK)TNK <- ScaleData(TNK)TNK <- RunPCA(TNK)TNK <- RunHarmony(TNK, "orig.ident")TNK <- FindNeighbors(TNK, reduction = "harmony", dims = 1:20)TNK <- FindClusters(TNK, resolution = c(0.2, 0.3, 0.4, 0.5, 0.6))TNK <- RunUMAP(TNK, reduction = "harmony", dims = 1:20)head(TNK@meta.data)DimPlot(TNK, group.by = "RNA_snn_res.0.6", label = T)#saveRDS(TNK, file = "TNK_data.rds")```
```
{r}markers <- c('CD8A', 'CD8B', 'CD4',             'FCGR3A', 'KLRD1',             'FOXP3', 'IL2RA', 'IKZF2',              'TCF7', 'SELL', 'LEF1', 'CCR7',             'LAG3', 'TIGIT', 'PDCD1', 'HAVCR2', 'CTLA4', 'LAYN', 'ENTPD1',             'GZMA', 'GZMB', 'GZMK', 'GNLY', 'IFNG', 'PRF1', 'NKG7',             'CD28', 'ICOS', 'CD40LG', 'TNFRSF4', 'TNFRSF9', 'TNFRSF18',             'ZNF683', 'ITGAE',             'CCL3', 'CCL5', 'CXCL13', 'IL21',             'EOMES', 'MAF', 'TOX2', 'ID2', 'TBX21', 'HOPX',             'MKI67', 'STMN1')
Idents(TNK) <- TNK$RNA_snn_res.0.6p <- DotPlot(TNK, features = markers, assay='RNA') + coord_flip()ggsave(filename = "./TNK-dotplot.png", plot = p, width = 8, height = 10)
TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(0)] <- 'CD4_CCR7'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(1)] <- 'CD8_GZMK'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(2)] <- 'CD8_HAVCR2'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(3)] <- 'Treg_CTLA4'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(4)] <- 'CD4_MAF'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(5)] <- 'CD8_IL7R'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(6)] <- 'NK_FCGR3A'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(7)] <- 'T_MKI67'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(8)] <- 'CD8_GZMB'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(9)] <- 'CD8_STMN1'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(10)] <- 'NK_KLRD1'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(11)] <- 'CD4_IL7R'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(12)] <- 'Treg_SELL'TNK@meta.data$celltype[TNK@meta.data$RNA_snn_res.0.6 %in% c(13)] <- 'CD4_CXCL13'#saveRDS(TNK, file = "TNK_celltype.rds")DimPlot(TNK, group.by = "celltype", label = T)```
```
{r}pbmc_tmp <- TNKave_exp <- AverageExpression(pbmc_tmp, group.by = 'celltype', assay='RNA', features = markers)df <- ave_exp$RNA
plot_df <- t(scale(t(df)))Heatmap(plot_df,cluster_columns = F,cluster_rows = F,name = "Z-Score",        border=T,col = viridis::viridis(200))```
```
{r}phe_TNK <- TNK@meta.dataphe_TNK$patient =  paste(phe_TNK$group, phe_TNK$RECIST, sep = '_')tb_TNK <- table(phe_TNK$celltype, phe_TNK$patient)head(tb_TNK)bar_data_TNK <- as.data.frame(tb_TNK)bar_per_TNK <- bar_data_TNK %>%  group_by(Var2) %>%  mutate(sum(Freq)) %>%  mutate(percent = Freq/`sum(Freq)`)head(bar_per_TNK)bar_per_TNK$Var2group <- ifelse(str_detect(bar_per_TNK$Var2, "TN"), "TN", ifelse(str_detect(bar_per_TNK$Var2, "NMPR"), "NMPR", "MPR"))bar_per_TNK$group <- grouphead(bar_per_TNK)bar_per_TNK$group = factor(bar_per_TNK$group, levels = c("TN", "MPR", "NMPR"))table(bar_per_TNK$Var1)bar_per_TNK$Var1 = factor(bar_per_TNK$Var1, levels = c("NK_FCGR3A", "NK_KLRD1", "CD8_IL7R", "CD8_GZMK", "CD8_GZMB", "CD8_HAVCR2", "CD8_STMN1", "T_MKI67", "CD4_IL7R", "CD4_CCR7", "CD4_MAF", "CD4_CXCL13", "Treg_SELL", "Treg_CTLA4"))head(bar_per_TNK)```
```
{r}ggplot(bar_per_TNK, aes(x = Var1, y = percent, fill = group, colour = group)) +  geom_boxplot(width = 0.6, outlier.shape = NA) +  geom_jitter(shape = 21, size = 2, position = position_jitterdodge(0.2)) +  scale_fill_manual(values = c("white", "white", "white")) +  scale_color_manual(values = c('#4169E1', '#FF7F50', '#3CB371'),                     labels = c("TN(n=3)", "MPR(n=4)", "NMPR(n=8)")) +  theme_bw() +  theme(legend.position = "bottom",        legend.direction = 'horizontal',        legend.justification = "left",        legend.box.just = "left",        legend.title = element_blank(),        axis.text.x = element_text(colour = "black",angle=45,  hjust = 1, family = "Times", size = 12),        axis.text.y = element_text(family = "Times", size = 14, face = "plain"),        axis.title.y = element_text(family = "Times", size = 14, face = "plain"),        axis.title.x = element_text(family = "Times", size = 14, face = "plain"),        plot.title = element_text(family = "Times", size = 15, face = "bold", hjust = 0.5),        panel.grid.major = element_blank(),        panel.grid.minor = element_blank()) +  labs(y = "Fraction (%) of immune cells", x = element_blank())+  guides(fill = FALSE)```
```
{r}cd8 = TNK[, TNK$celltype %in% c('CD8_GZMB', 'CD8_GZMK', 'CD8_HAVCR2')]Mono_object <- cd8Mono_matrix <- as(as.matrix(GetAssayData(Mono_object, slot = "counts")), 'sparseMatrix')gene_anno <- data.frame(gene_id = rownames(Mono_matrix), gene_short_name = rownames(Mono_matrix))rownames(gene_anno) <- rownames(Mono_matrix)cell_anno <- Mono_object@meta.data
fd <- new("AnnotatedDataFrame", data = gene_anno)pd <- new("AnnotatedDataFrame", data = cell_anno)Mono.cds <- newCellDataSet(Mono_matrix, phenoData = pd, featureData = fd)Mono.cds <- estimateSizeFactors(Mono.cds)Mono.cds <- estimateDispersions(Mono.cds)Mono.cds <- detectGenes(Mono.cds, min_expr = 0.1) #计算每个基因在多少细胞中表达Mono.cds <- reduceDimension(Mono.cds, reduction_method = "DDRTree", max_components = 2, norm_method = 'log')Mono.cds <- orderCells(Mono.cds) head(pData(Mono.cds))```
```
{r}plot_cell_trajectory(Mono.cds,color_by="celltype", size=1,show_backbone=TRUE)```

## B cell```{r}library(harmony)```
```
{r}#S_combined <- readRDS(file = "celltype_data.rds")table(S_combined@meta.data$celltype)B <- subset(S_combined, subset = celltype == "B cell")dim(B)```
```
{r}B <- NormalizeData(B, normalization.method = "LogNormalize")B <- FindVariableFeatures(B)B <- ScaleData(B)B <- RunPCA(B)B <- RunHarmony(B, "orig.ident")B <- FindNeighbors(B, reduction = "harmony", dims = 1:20)B <- FindClusters(B, resolution = c(0.2, 0.3, 0.4, 0.5, 0.6))B <- RunUMAP(B, reduction = "harmony", dims = 1:20)head(B@meta.data)DimPlot(B, group.by = "RNA_snn_res.0.2")#saveRDS(B, file = "B_data.rds")```
```
{r}#B <- readRDS("B_data.rds")markers <- c('LRMP', 'SYNE2', 'SERPINA9', 'HMCES', 'RGS13',             'HSPH1', 'KDM6B', 'EGR3', 'NFKBID', 'CD83',             'FCRL5', 'KCTD12', 'ITGAX', 'CCR1', 'FCRL4',             'IL4R', 'YBX3', 'TCL1A', 'IGHD',              'IER5', 'DNAJB1', 'HLA-DRB3', 'HSPA1B', 'HSPA1A',             'CD1C', 'JCHAIN', 'TENT5C', 'FCRL3', 'IGHM',             'SCIMP', 'FOSB', 'AL365357.1', 'ITGB1', 'HLA-DRB5'             )
DotPlot(B, features = markers, group.by = "RNA_snn_res.0.2") + coord_flip()ggsave(filename = "./B-dotplot.png", width = 8, height = 10)```
```
{r}B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(0, 5, 6, 7)] <- 'B0_MS4A1'B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(1)] <- 'B4_FCRL4'B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(2)] <- 'B3_IGHD'B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(3)] <- 'B5_CD83'B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(4)] <- 'B2_HSPA1A'B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(8)] <- 'B1_IGHM'B@meta.data$celltype[B@meta.data$RNA_snn_res.0.2 %in% c(9)] <- 'B6_RGS13'DimPlot(B, group.by = "celltype", label = T)#saveRDS(B, file = "B_celltype.rds")```
```
{r}phe_B <- B@meta.dataphe_B$patient =  paste(phe_B$group, phe_B$RECIST, sep = '_')tb_B <- table(phe_B$celltype, phe_B$patient)head(tb_B)bar_data <- as.data.frame(tb_B)bar_per_B <- bar_data %>%  group_by(Var2) %>%  mutate(sum(Freq)) %>%  mutate(percent = Freq/`sum(Freq)`)head(bar_per_B)bar_per_B$Var2group <- ifelse(str_detect(bar_per_B$Var2, "TN"), "TN", ifelse(str_detect(bar_per_B$Var2, "NMPR"), "NMPR", "MPR"))bar_per_B$group <- grouphead(bar_per_B)bar_per_B$group = factor(bar_per_B$group, levels = c("TN", "MPR", "NMPR"))table(bar_per_B$Var1)bar_per_B$Var1 = factor(bar_per_B$Var1, levels = c("B3_IGHD", "B0_MS4A1", "B1_IGHM", "B2_HSPA1A", "B4_FCRL4", "B5_CD83", "B6_RGS13"))head(bar_per_B)```
```
{r}ggplot(bar_per_B, aes(x = Var1, y = percent, fill = group, colour = group)) +  geom_boxplot(width = 0.6, outlier.shape = NA) +  geom_jitter(shape = 21, size = 2, position = position_jitterdodge(0.2)) +  scale_fill_manual(values = c("white", "white", "white")) +  scale_color_manual(values = c('#4169E1', '#FF7F50', '#3CB371'),                     labels = c("TN(n=3)", "MPR(n=4)", "NMPR(n=8)")) +  theme_bw() +  theme(legend.position = "bottom",        legend.direction = 'horizontal',        legend.justification = "left",        legend.box.just = "left",        legend.title = element_blank(),        axis.text.x = element_text(colour = "black",angle=45,  hjust = 1, family = "Times", size = 12),        axis.text.y = element_text(family = "Times", size = 14, face = "plain"),        axis.title.y = element_text(family = "Times", size = 14, face = "plain"),        axis.title.x = element_text(family = "Times", size = 14, face = "plain"),        plot.title = element_text(family = "Times", size = 15, face = "bold", hjust = 0.5),        panel.grid.major = element_blank(),        panel.grid.minor = element_blank()) +  labs(y = "Fraction (%) of immune cells", x = element_blank())+  guides(fill = FALSE)```
```
{r}VlnPlot(B, features = c('FCRL4', 'FCRL5', 'BHLHE40', 'CCR1', 'STAT1', 'GBP4', 'CD86', 'ITGAX'), ncol = 4, group.by = "celltype", pt.size = 0)```
```
{r}#B <- readRDS("B_celltype.rds")table(B@meta.data$celltype)B4 <- subset(B, subset = celltype == 'B4_FCRL4')dim(B4)B4_count <- as.matrix(B4@assays$RNA@data)B4_meta <- data.frame(Cell = rownames(B4@meta.data), celltype = 'B4_FCRL4')
#TNK <- readRDS("TNK_celltype.rds")table(TNK@meta.data$celltype)CD4 <- subset(TNK, subset = celltype %in% c('CD4_MAF', 'CD4_CXCL13'))dim(CD4)cd4_count <- as.matrix(CD4@assays$RNA@data)cd4_meta <- data.frame(Cell = rownames(CD4@meta.data), celltype = 'Tfh')
CD8 <- subset(TNK, subset = celltype %in% c('CD8_IL7R', 'CD8_GZMK', 'CD8_GZMB', 'CD8_HAVCR2', 'CD8_STMN1'))dim(CD8)cd8_count <- as.matrix(CD8@assays$RNA@data)cd8_meta <- data.frame(Cell = rownames(CD8@meta.data), celltype = 'CD8 T')
count <- cbind(B4_count, cd4_count, cd8_count)meta <- rbind(B4_meta, cd4_meta, cd8_meta)
write.table(count, './B4_Tfh_CD8T_count.txt', sep = '\t', quote = F, row.names = T)write.table(meta, './B4_Tfh_CD8T_meta.txt', sep = '\t', quote = F, row.names = F)```
## cellphonedb分析在python中运行```{r}library(Seurat)library(dplyr)library(psych)library(qgraph)library(igraph)library(tidyverse)library(ktplots)library(SingleCellExperiment)library(reticulate)count <- read.table("./B4_Tfh_CD8T_count.txt", sep = '\t')head(count)meta <- read.table("./B4_Tfh_CD8T_meta.txt", sep = '\t', header = T)head(meta)meta <- as.matrix(meta)
sce <- SingleCellExperiment(assays = list(counts = count), colData = meta)pvals <- read.delim("./cellphonedb_result/statistical_analysis_pvalues_pbmc.txt", check.names = F)means <- read.delim("./cellphonedb_result/statistical_analysis_means_pbmc.txt", check.names = F)
head(meta)plot_cpdb(cell_type1 = 'B4_FCRL4', cell_type2 = 'CD8 T',scdata = sce,          idents = 'celltype',           means = means, pvals = pvals) +  small_axis(fontsize = 3) + small_grid() + small_guide() + small_legend(fontsize = 2) ```
```

Python部分：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
import cellphonedbcpdb_file_path = './cellphonedb.zip'test_meta_file_path = './B4_Tfh_CD8T_meta.txt'test_counts_file_path = './B4_Tfh_CD8T_count.txt'from cellphonedb.src.core.methods import cpdb_statistical_analysis_methoddeconvoluted, means, pvalues, significant_means = cpdb_statistical_analysis_method.call( cpdb_file_path = cpdb_file_path, meta_file_path = test_meta_file_path, counts_file_path = test_counts_file_path, counts_data = 'hgnc_symbol', iterations = 100, threshold = 0.1, threads = 6, output_suffix = "pbmc", output_path = "./cellphonedb_result")
```

输出图片：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpyBKPhUicWEJ3ltiaXwvic3lUad2ToUn4gictFMxqvv5rE4bMg2W9fZpbJg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpApy98KYYVkpqQk0seA8VPdV7pp701qjfutMGlhSAHmoaibtXibicFPE3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpIicrYaDwsD5HCD7UCC0pXDaYIXKGRToPP4q90HicRccyPHKK4m66xNiaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpzqiazpibsZj4Ztl83gt9O2T6wewol6MfoBG7XAUb73aPHJeIBmxon3hw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialptTSH2B2zhT42xoCxcxYDFEgtQ404UR2n7kFruP1egx3WBbNU0VyZPw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialprtq92vVNiaw842aEvmZhgSDvKmL3GSXZWAiaGuKwtLicickWdLjTZUrRLg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpfUk3pKcVcialgkrPibwgX5IKrAHUH8heX5TnNURzXErvGxMQ9iaibp2XmQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpfiaEyQ7nsotscr2AoRibVRHBrN29E9JgAx7hzgBgGY1H8Bf8S7icpshPg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialplR4ut0giazSMWiclGviaUL71jAS322uXQFh7Thkyn4Wya5y84ZwBzEbWQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialp6gM3rhQWGZvu6bFpVXVWGxnzx3SaoYk8oSqKp7nnY8xgNLnoYUfEicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialp1wCqG2mJxSn0Nefz2DIpkxBRs4mLNlK9dlkZ5lfloojESicdCexw0iaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpqSR5VN993OeupuDtH18MGjS3f3PASnzX90kTSLAOUrrWEuLrNRS2Zw/640?wx_fmt=png&from=appmsg)

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/17I_4PoJ7hU4Y-1mL7o-iEg?pwd=bkn4

提取码：bkn4

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzJ5VTn1WwhdFfsDcVSPialpTlfWE0njRgIcUxNRZ8I8tvjQMClFzalD5tQdhEXVsntQMfxiasiaDFsg/640?wx_fmt=jpeg&from=appmsg)

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
[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506960&idx=1&sn=9f5913231f9583411e47ccf0dcadedf6&chksm=9b3ca540ac4b2c56a60b5f71ab32e1eacd3194af4bfef819b2de60fc50781360876b45837bf7&scene=21#wechat_redirect>)[人类肾脏snRNA-seq图谱拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506960&idx=1&sn=9f5913231f9583411e47ccf0dcadedf6&chksm=9b3ca540ac4b2c56a60b5f71ab32e1eacd3194af4bfef819b2de60fc50781360876b45837bf7&scene=21#wechat_redirect>)
[CellRank的教程重现](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507012&idx=1&sn=fb01cca63326fd6e8c682434a53fc2ea&chksm=9b3ca514ac4b2c02115ae5dea368190ce74997ac16a07fdc29f76cef815600b1e5b813c71163&scene=21#wechat_redirect>)
[胶质瘤相关巨噬细胞scRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507096&idx=1&sn=98e42a5768074d2766f2ce64214ac391&chksm=9b3ca5c8ac4b2cdebe68a8519a087e41a4c88a7e465c5ddc107f633a5fbf3fcc8bbff6aa8821&scene=21#wechat_redirect>)
[肝癌单细胞分群marker](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507136&idx=2&sn=16f8afe29fb59b9a8e9cac265098709c&chksm=9b3ca590ac4b2c86c9554bf20edd587f5d758636f55cf9e390220249d3338b1fde7717fb3c6e&scene=21#wechat_redirect>)
[scRNA揭示T1D骨髓与骨质减少的关系](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507144&idx=1&sn=ed6e95f16601e6196cea7179b88db250&chksm=9b3ca598ac4b2c8ecfd1025246eb79c6aa8bf5703f8698d23f1d1f673121e3bf8168a32dba07&scene=21#wechat_redirect>)
[微环境中肿瘤免疫屏障决定了免疫治疗的效果](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507337&idx=1&sn=e23d849663a6cfcad19bacdaeeb85b5f&chksm=9b3ca4d9ac4b2dcf8ce4d9720bf7588a30e932adea4297862927ebfe20c29f8961436f761b8c&scene=21#wechat_redirect>)[肝脏发育、成熟的单细胞图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507353&idx=1&sn=f2922ce2337c31a781a690ea59c5abde&chksm=9b3ca4c9ac4b2ddfc267838fe6d794027643e89fe054a5ca4d48e51976ea825af7fed285e26b&scene=21#wechat_redirect>)
[胰腺导管腺癌的内异质性和恶性进展scRNA-seq图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507450&idx=1&sn=ee9b7d482ad9a88c6da18341c7ec5254&chksm=9b3ca4aaac4b2dbc83fc6cc4c084636fb397e56d0057dfb5b546acf402661ab64d241f985073&scene=21#wechat_redirect>)
[人类肾脏scRNA-seq图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=2&sn=dec30ee34e483c3695613b3e41488a78&chksm=9b3ca77dac4b2e6b1734f1fd3d0134468b2ca8bc9f9118edc6e114a37f7ceea7dc4fa41b4556&scene=21#wechat_redirect>)
[小鼠与人类的空间表观单细胞图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=1&sn=94c2a38b98957a9526d510798f791419&chksm=9b3ca77dac4b2e6b40d37e73f54791d55a919f50992bf62ac557ecbac919fb6415dca468dba4&scene=21#wechat_redirect>)
[疟疾中免疫细胞亚群的调控响应](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507659&idx=2&sn=a6860bb0eb8d3854a37acd0342777956&chksm=9b3ca79bac4b2e8dc0c3aa83c000894a53e2b316388495703e58d42ab205dd093bf578807b74&scene=21#wechat_redirect>)
[儿童白血病的单细胞数据读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=2&sn=8d45c680ad78f52043d4ce4cbbf3c67a&chksm=9b3ca7bdac4b2eab2405773b5d71ff1f5495250ef813b24429e1b920c1b96a4ee391507d011b&scene=21#wechat_redirect>)[小鼠脑动脉瘤模型的scRNA-Seq分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507717&idx=2&sn=1d99c171cbfedc11f11fc827b643c89d&chksm=9b3ca655ac4b2f4360790bde80bc1452e9e314c6a0ae2dc6f9d19edbcc580e81ace3080dbb5f&scene=21#wechat_redirect>)

04

**本次活动最终解释权归主办方所有!********主办方拥有对作品的编辑、宣发权利!**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
