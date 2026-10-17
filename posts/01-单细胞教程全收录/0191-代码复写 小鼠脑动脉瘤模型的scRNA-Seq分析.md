---
title: "代码复写| 小鼠脑动脉瘤模型的scRNA-Seq分析"
date: 2024-01-19
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507717&idx=2&sn=1d99c171cbfedc11f11fc827b643c89d&chksm=9b3ca655ac4b2f4360790bde80bc1452e9e314c6a0ae2dc6f9d19edbcc580e81ace3080dbb5f#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写| 小鼠脑动脉瘤模型的scRNA-Seq分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507717&idx=2&sn=1d99c171cbfedc11f11fc827b643c89d&chksm=9b3ca655ac4b2f4360790bde80bc1452e9e314c6a0ae2dc6f9d19edbcc580e81ace3080dbb5f#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是18号作品。本作品复写了题为"文章标题: Single-Cell Transcriptome Analysis of the Circle of Willis in a Mouse Cerebral Aneurysm Model"的论文.**文章链接** ：https://www.ahajournals.org/doi/10.1161/STROKEAHA.122.038776**数据原始链接：** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE193533**复现图片集锦** ：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUM1SdpgAHyImM0kD3KHAuAKIQiao0ZpxEKEPJJxQm2hM5jxVMC7EP32hw/640?wx_fmt=png&from=appmsg)

**文献简介** ：发表日期和杂志：2022 年发表在STROKE上研究对象：成年雄性小鼠研究问题：确定Circle of Willis（CoW）血管细胞与脑动脉瘤（CAs）相关的转录特征。研究方法：使用单细胞RNA 测序技术对健康小鼠和脑动脉瘤（CAs ）小鼠的CoW 血管细胞进行了全面的谱系异质性和转录组学改变分析。实验设计：对照组：采用假手术的方式处理成年雄性小鼠。实验组：使用弹性蛋白酶模型在成年雄性小鼠中诱导脑动脉瘤。然后对动脉瘤诱导后 14 天获得的 Willis 样本进行单细胞 RNA 测序。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMyW5c6WkTaw4LWMDsxZGZF0GxBx8CbZP3aPAFL5Xu0ico6fD7PfzYrUQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMuoJgGEEkEqMNK4y3A0pfrS8snRaGnqB4u8l6gJmngq7N8kHWalN2Ow/640?wx_fmt=png&from=appmsg)

对来自假手术组、形成脑动脉瘤的动物以及患有破裂动脉瘤的动物所采集的Willis环动脉的单细胞悬浮液进行了单细胞RNA 测序。

一、复写内容

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
```
{r setup, include=FALSE}knitr::opts_chunk$set(echo = TRUE)```加载相关R包```{r}library(dplyr)  library(ggplot2)library(ggpubr)library(hdf5r)library(Seurat)library(harmony)library(tidyverse)library(sctransform)library(clustree)library(circlize)library(RColorBrewer)```设置工作目录```{r}setwd("E:\\单细胞测序\\单细胞原始复现数据\\mmuIA_GSE193533")```设置数据路径与样本名称```{r}assays <- dir("E:\\单细胞测序\\单细胞原始复现数据\\mmuIA_GSE193533\\data")
dir <- paste0("data/",assays)
samples_name = c('formed', 'ruptured', 'sham')```导入数据```{r}data_formed <- Read10X_h5(dir[1])  data_ruptured <- Read10X_h5(dir[2])data_sham <- Read10X_h5(dir[3])```创建seurat对象,根据文章最终得到的细胞和基因数量,试出min.cell为8,min.features为300```{r}formed_seurat <- CreateSeuratObject(data_formed,project = "data_formed",min.cells = 8, min.features = 300)formed_seurat[["percent.mt"]] <- PercentageFeatureSet(formed_seurat, pattern = "mt")
ruptured_seurat <- CreateSeuratObject(data_ruptured,project = "data_ruptured",min.cells = 8, min.features = 300)ruptured_seurat[["percent.mt"]] <- PercentageFeatureSet(ruptured_seurat, pattern = "mt")

sham_seurat <- CreateSeuratObject(data_sham ,project = "data_sham",min.cells = 8, min.features = 300)sham_seurat[["percent.mt"]] <- PercentageFeatureSet(sham_seurat, pattern = "mt")```过滤nFeature_RNA大于300且不小于5000的细胞和线粒体不小于15的细胞```{r}formed_seurat <- subset(formed_seurat,                         subset = nFeature_RNA > 300 &                           nFeature_RNA < 5000 &                           percent.mt < 15 &                          nCount_RNA < 23000)
ruptured_seurat <- subset(ruptured_seurat,                           subset = nFeature_RNA > 300 &                             nFeature_RNA < 5000 &                             percent.mt < 15 &                            nCount_RNA < 23000)
sham_seurat <- subset(sham_seurat,                       subset = nFeature_RNA > 300 &                         nFeature_RNA < 5000 &                         percent.mt < 15 &                        nCount_RNA < 23000)```nFeature_RNA数据框```{r}formed_seurat_nFeature <- cbind(formed_seurat[["nFeature_RNA"]],rep("formed", ncol(formed_seurat)))colnames(formed_seurat_nFeature) <- c("nFeature_RNA","treatment")
ruptured_seurat_nFeature <- cbind(ruptured_seurat[["nFeature_RNA"]],rep("ruptured", ncol(ruptured_seurat)))colnames(ruptured_seurat_nFeature) <- c("nFeature_RNA","treatment")
sham_seurat_nFeature <- cbind(sham_seurat[["nFeature_RNA"]],rep("sham", ncol(sham_seurat)))colnames(sham_seurat_nFeature) <- c("nFeature_RNA","treatment")
nFeature_RNA <- rbind(sham_seurat_nFeature,formed_seurat_nFeature)
nFeature_RNA <- rbind(nFeature_RNA,ruptured_seurat_nFeature)```nCount_RNA数据框```{r}formed_seurat_nCount <- cbind(formed_seurat[["nCount_RNA"]],rep("formed", ncol(formed_seurat)))colnames(formed_seurat_nCount) <- c("nCount_RNA","treatment")
ruptured_seurat_nCount <- cbind(ruptured_seurat[["nCount_RNA"]],rep("ruptured", ncol(ruptured_seurat)))colnames(ruptured_seurat_nCount) <- c("nCount_RNA","treatment")
sham_seurat_nCount <- cbind(sham_seurat[["nCount_RNA"]],rep("sham", ncol(sham_seurat)))colnames(sham_seurat_nCount) <- c("nCount_RNA","treatment")
nCount_RNA <- rbind(sham_seurat_nCount,formed_seurat_nCount)
nCount_RNA <- rbind(nCount_RNA,ruptured_seurat_nCount)```percent.mt数据框```{r}formed_seurat_mt <- cbind(formed_seurat[["percent.mt"]],rep("formed", ncol(formed_seurat)))colnames(formed_seurat_mt) <- c("percent.mt","treatment")
ruptured_seurat_mt <- cbind(ruptured_seurat[["percent.mt"]],rep("ruptured", ncol(ruptured_seurat)))colnames(ruptured_seurat_mt) <- c("percent.mt","treatment")
sham_seurat_mt <- cbind(sham_seurat[["percent.mt"]],rep("sham", ncol(sham_seurat)))colnames(sham_seurat_mt) <- c("percent.mt","treatment")
percent.mt <- rbind(sham_seurat_mt,formed_seurat_mt)
percent.mt <- rbind(percent.mt,ruptured_seurat_mt)```nCount_RNA箱线图```{r}kruskal_test1 <- kruskal.test(nCount_RNA ~ treatment, data = nCount_RNA)#p-value < 2.2e-16##===================p1 <- ggboxplot(nCount_RNA, x = "treatment", y = "nCount_RNA",width = 0.5,                color = "treatment",                add = "jitter")p1 + annotate("text", x = 1, y = 0, label = paste("Kruskal-Wallis, p < 2.2e-16"), vjust = -0.5) + #使用获得的p值    labs(x = "treatment", y = "nCount_RNA") +   stat_compare_means(comparisons = list(c("sham","formed"),c("sham","ruptured"),c("formed","ruptured")))```nFeature_RNA箱线图```{r}kruskal_test2 <- kruskal.test(nFeature_RNA ~ treatment, data = nFeature_RNA)#p-value < 2.2e-16##===================p2 <- ggboxplot(nFeature_RNA, x = "treatment", y = "nFeature_RNA",width = 0.5,                color = "treatment",                add = "jitter")p2 + annotate("text", x = 1, y = 0, label = paste("Kruskal-Wallis, p < 2.2e-16"), vjust = -0.5) + #使用获得的p值    labs(x = "treatment", y = "nFeature_RNA") +   stat_compare_means(comparisons = list(c("sham","formed"),c("sham","ruptured"),c("formed","ruptured")))```percent.mt箱线图```{r}kruskal_test3 <- kruskal.test(percent.mt ~ treatment, data = percent.mt)#p-value < 2.2e-16##===================p3 <- ggboxplot(percent.mt, x = "treatment", y = "percent.mt",width = 0.5,                color = "treatment",                add = "jitter")p3 + annotate("text", x = 1, y = 0, label = paste("Kruskal-Wallis, p < 2.2e-16"), vjust = -0.5) + #使用获得的p值    labs(x = "treatment", y = "percent.mt") +   stat_compare_means(comparisons = list(c("sham","formed"),c("sham","ruptured"),c("formed","ruptured")))
```
nCount_RNA<23000   13763 samples and 16124 features```{r}data <- merge(formed_seurat, y = c(ruptured_seurat, sham_seurat),               add.cell.ids = c("formed", "ruptured","sham"), project = " Mouse")```SCT函数进行标准化```{r}ifnb.list <- SplitObject(data)if (!requireNamespace("glmGamPoi", quietly = TRUE)) {  ifnb.list <- lapply(X = ifnb.list, FUN = SCTransform, vars.to.regress = "percent.mt", verbose = FALSE)}else{  ifnb.list <- lapply(X = ifnb.list, FUN = SCTransform, vars.to.regress = "percent.mt", verbose = FALSE, method = "glmGamPoi")}```
寻找4000个高变基因```{r}ifnb.list1 <- lapply(ifnb.list, FUN = FindVariableFeatures,selection.method = "vst", nfeatures = 4000)```整合数据用SCT集成```{r}features <- SelectIntegrationFeatures(object.list = ifnb.list1, nfeatures = 4000) #从每个数据集中选择一组特征,以便在整合时使用相似的基因集ifnb.list1 <- PrepSCTIntegration(object.list = ifnb.list1, anchor.features = features) #准备单细胞数据集以进行SCT整合integrated.anchors <- FindIntegrationAnchors(object.list = ifnb.list1, normalization.method = "SCT",                                             anchor.features = features) #寻找用于整合的锚点,即在不同数据集之间共享的特征all.integrated <- IntegrateData(anchorset = integrated.anchors, normalization.method = "SCT") #将数据集整合到一个共享的表达矩阵中,以便后续的降维和聚类分析
all.integrated <- RunPCA(all.integrated, features = VariableFeatures(object = all.integrated)) #对整合的数据运行主成分分析(PCA),以减少数据的维度all.integrated <- RunUMAP(all.integrated, reduction = "pca", dims = 1:15) #PCA的基础上运行UMAP算法,选取前15个主成分,将数据映射到二维空间
all.integrated <- FindNeighbors(all.integrated, dims = 1:15) #在降维的空间中找到每个点的邻居,为后续的聚类分析做准备```
利用clustree函数寻找分多少个群合适```{r}all.integrated <- FindClusters(  object = all.integrated,  resolution = c(seq(0,1.6,0.2),0.3) # 文章res等于0.3,便添加一个0.3上去)```
```
{r}clustree(all.integrated@meta.data, prefix = "integrated_snn_res.")# 选取res=0.3```
```
{r}all.integrated <- FindClusters(all.integrated, resolution = 0.3)```画出聚类图```{r}DimPlot(all.integrated, label = T, repel = T, label.size = 7)# 调了label大小,共16个cluster```
```
{r}FeaturePlot(all.integrated, features = c("Hbb-bt","Hbb-bs","Hba-a2","Hba-a1"), pt.size = 0.2,ncol = 2)# 可视化CoW 细胞中红细胞选择性标记基因的表达```根据查阅相关文献,探索每个聚类的标记基因,使用标记基因注释细胞类型```{r}all.integrated1 <- RenameIdents(all.integrated,                                `0` = "VSMC",                               `1` = "Mo/MΦ",                                `2` = "VSMC",                               `3` = "Mo/MΦ",                                `4` = "VSMC",                                `5` = "Neutrophils",                                `6` = "Fibroblast",                                `7` = "VSMC", # 存在红细胞大量分布                               `8` = "Endothelium",                                `9` = "Mo/MΦ",                               `10` = "T lymphocyte",                                `11` = "Pericyte",                                `12` = "Mast cells",                                `13` = "Mo/MΦ",                               `14` = "B lymphocyte",                               `15` = "Dendritic cells")```
```
{r}DimPlot(all.integrated1, label = TRUE)```查看每个样本中细胞个数```{r}table(Idents(all.integrated), all.integrated$orig.ident)```#*****************************************************************Circos plot```{r}df <- data.frame(table(Idents(all.integrated), all.integrated$orig.ident))df$Var2 <- gsub("^.*_","",df$Var2)df1 <- cbind(df$Var2,df)df1 <- df1[,-3]# 创建一个向量，包含0到16的数字  numbers <- 0:16  # 使用rep函数将"yellow"重复16次（因为0:16共有17个数字）  yellow_values <- rep("yellow", 17)  # 将numbers向量和yellow_values向量进行匹配，得到新的向量，其中每个数字对应的值都是"yellow"  result <- setNames(yellow_values, numbers)grid.col <- c(formed = "red", ruptured = "green", sham = "grey", result)```
```
{r}par(cex = 1.5, mar = c(0, 0, 0, 0)) #调节标签大小chordDiagram(df1, grid.col = grid.col, link.border = "grey")```#*****************************************************************Dotplot(聚类点图)```{r}features= c("Myh11","Tagln", "Acta2","Cd68","C1qa","C1qb","Lcn2","Dcn","Col1a1",            "Lum","Cdh5", "Pecam1","Esam","Cd3g","Cd28","Rgs5","Rgs16","Kcnj8",            "Ly6d","Cd209a", "Ccr7", "Mcpt4","Cma1","Tpsb2")```
```
{r}DotPlot(all.integrated, features = unique(features)) + RotatedAxis()```#*****************************************************************饼图```{r}#Neutrophils (中性粒细胞)#T lymphocyte (T淋巴细胞)#B lymphocyte (B淋巴细胞)#Dendritic cells(树突状细胞)sham <- df[which(df$Var2 == "sham"),]formed <- df[which(df$Var2 == "formed"),]ruptured <- df[which(df$Var2 == "ruptured"),]```聚类命名```{r}names <- c("VSMC", "Mo/MΦ", "Fibroblast", "Endothelium", "lmmune cells")```颜色设置```{r}cols <- c("#ED1C24", "#22B14C", "#FFC90E", "#3f48CC", "#3f90CC")```饼状图函数```{r}picture <- function(sample,names){piepercent=c()sum = sum(sample[sample$Var1 %in% c(0,1,2,3,4,5,6,7,8,9,10,13,14,15), "Freq"])piepercent[1] = sum(sample[sample$Var1 %in% c(0, 2, 4, 7), "Freq"])/sumpiepercent[2] = sum(sample[sample$Var1 %in% c(1, 3, 9, 13), "Freq"])/sumpiepercent[3] = sum(sample[sample$Var1 %in% 6, "Freq"])/sum       piepercent[4] = sum(sample[sample$Var1 %in% 8, "Freq"])/sum       piepercent[5] = sum(sample[sample$Var1 %in% c(5,10,14,15), "Freq"])/sum        piepercent = round(as.numeric(piepercent)*100)info<-data.frame(piepercent,names)}```Sham饼图```{r}sham_info <- picture(sham,names)pie(sham_info$piepercent, #扇形数值大小    labels = sham_info$names, #各扇形面积标签    radius = 0.9,#饼图半径    main = "sham",#标题    clockwise = FALSE, #饼图各个切片是否按顺时针做出分割    col = cols)#自定义颜色# 添加颜色样本标注legend("topright", names, cex = 0.8, fill = cols)```Formed饼图```{r}Formed_info <- picture(formed,names)pie(Formed_info$piepercent, #扇形数值大小    labels = Formed_info$names, #各扇形面积标签    radius = 0.9,#饼图半径    main = "Formed",#标题    clockwise = FALSE, #饼图各个切片是否按顺时针做出分割    col = cols)#自定义颜色# 添加颜色样本标注legend("topright", names, cex = 0.8, fill = cols)```Ruptured饼图```{r}Ruptured_info <- picture(ruptured,names)pie(Ruptured_info$piepercent, #扇形数值大小    labels = Ruptured_info$names, #各扇形面积标签    radius = 0.9,#饼图半径    main = "Ruptured",#标题    clockwise = FALSE, #饼图各个切片是否按顺时针做出分割    col = cols)#自定义颜色# 添加颜色样本标注legend("topright", names, cex = 0.8, fill = cols)```导出每组样本中各类细胞含量```{r}result_of_merge <- merge(sham_info, Formed_info, by = "names")  all_cell <- merge(result_of_merge, Ruptured_info, by = "names")colnames(all_cell) <- c("names","sham","Formed","Ruptured")write.csv(all_cell,file = "D:\\基因与转录组学\\all_cell.csv",row.names = F)```#*****************************************************************条形图```{r}prop.table(table(Idents(all.integrated), all.integrated$orig.ident))# 计算每组样本在每一cluster中的占比bar.chart<-as.data.frame(prop.table(table(Idents(all.integrated), all.integrated$orig.ident)))
colnames(bar.chart)<-c("cluster","sample","proportion")bar.chart$sample <- gsub("^.*_","",bar.chart$sample)
ggplot(bar.chart,aes(cluster,proportion,fill=sample))+    geom_bar(stat="identity",position="fill")+    ggtitle("")+    theme_bw()+    theme(axis.ticks.length=unit(0.5,'cm'))+    guides(fill=guide_legend(title=NULL))```
```

‍

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUM4L5dcHMF3tudAuLY96VMBeuI2cqPhNnwkvX4Mznv4CcYSL2p079zUA/640?wx_fmt=png&from=appmsg)

对应附件中Figure S1的B 图 (过滤后nFeature_RNA在三组样本间的含量图)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMAVbwOTmM66hcrO4ibBkNsracMVqsgndsq93RvOhQksyYiatswtZzy2uw/640?wx_fmt=png&from=appmsg)

对应附件中Figure S1的C图 (过滤后nCount_RNA在三组样本间的含量图)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMpepVjYZpuGib0ibBdicibiaJZvaUw6H1z7GtJyj8Shvib8Wptveun2Snd0hQ/640?wx_fmt=png&from=appmsg)

对应附件中Figure S1的D图 (过滤后percent.m在三组样本间的含量图)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMd1WgZ9LSUk9k1whZicay3hASaiah7K1DicY3GCssIRQFy8MtDtgic0AEeg/640?wx_fmt=png&from=appmsg)

(clustree聚类可视化)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMgR2tN9P6A9Cc4HFP2jfo3e8XJE0NbrEnbxMsNOtsgbza0MyGfk27yg/640?wx_fmt=png&from=appmsg)

对应正文中Figure 1的B图

(合并的CoW细胞的UMAP 图)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMjicJSEuKpHzIMporUuQF1tFrkQiaEfuzcYbyPYBQ6EOeB5B58UREPJWQ/640?wx_fmt=png&from=appmsg)

对应附件中Figure S2的B图

（可视化CoW 细胞中红细胞选择性标记基因的表达）

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUM5EuzoCDcIQxmJPiaO1c5pzBnxpGkFkuyIFkh4HGVOk3RtdcwBEGR2JQ/640?wx_fmt=png&from=appmsg)

(标记基因注释细胞类型)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMfqALibtqp5chxwEWalqBlnHicib9DVDNaMW4nSpJZF53hIXGMcag9qaAw/640?wx_fmt=png&from=appmsg)

对应正文中Figure 1的D图

（Circos plot）

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMWic06obic4rqhbO4GjicZuqJoqzj4nxsP0ffuTkh3Hx4IN4pYNhIxH35Q/640?wx_fmt=png&from=appmsg)

对应正文中Figure 1的F图

（气泡图）

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMRLaFPEUU87cEcFIxk656iaqBdc36YsZo8EP0icvVuibsWB1s89WKo6kGQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMvibicm6tD2K16Vfmb5oCILaXguEsvNoibqsXleDu67ZLUeM9Rc5xwsBxA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMfE4fbpPTng92YZu67wXnaWctmZFM3fmJAfMQZ64Qz1TXGtaxtfrJOg/640?wx_fmt=png&from=appmsg)

对应正文中Figure 2的B图

（不同条件下Cow细胞中每种细胞类型的比例）

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMYl3znibxXhbmSsHNCRdQyOl7HxzmnicPeviayWn5ia0fmQYk0XeaF7GoGQ/640?wx_fmt=png&from=appmsg)

对应正文中Figure 2的C图

（不同条件下的细胞群体百分比）

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/1QW_u7-sUfPNq21CYZr4Tjw?pwd=lv4a

提取码：lv4a

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwxdbamLWBib7PmbMTA9diaUMGTs1CYqOndc4I5aSV94umJkdmxHicFCrQicaN9Yto3rhnZKHKRaHD6icg/640?wx_fmt=jpeg&from=appmsg)

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
[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507096&idx=1&sn=98e42a5768074d2766f2ce64214ac391&chksm=9b3ca5c8ac4b2cdebe68a8519a087e41a4c88a7e465c5ddc107f633a5fbf3fcc8bbff6aa8821&scene=21#wechat_redirect>)

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
