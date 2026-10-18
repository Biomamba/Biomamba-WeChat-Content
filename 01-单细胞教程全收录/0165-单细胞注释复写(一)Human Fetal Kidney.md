---
title: "单细胞注释复写(一):Human Fetal Kidney"
date: 2022-08-01
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 单细胞注释复写(一):Human Fetal Kidney

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447#rd
> 合集：单细胞教程全收录 / 全文复现

# **写在前面：**

![](../../images/90fab1387787746b.gif) 我反复的谈过，细胞类型注释才是单细胞测序中最难的环节，这主要是不同单细胞测序项目中的**取样形式** 、**建库方法** 、**测序平台** 、**分析工具** 、**函数参数** 等多方面造成的。拿笔者的第一个单细胞数据集来说，光是调整过滤参数、分辨率、寻找marker加以注释就花了一个月的时间，属实是既枯燥又乏味，为了给大家提供方便，以后会不定期带领大家复现一些已发表数据集中的细胞类型注释过程，有需要的同学可以持续关注，若有感兴趣的物种、组织器官也可以在文末客服处登记；当然，如果您有好的注释结果，也欢迎以Rmarkdown与工程文件的形式来稿，可以为大家提供稿费。注释后的数据：
https://pan.baidu.com/s/13XG4ITR34TzP5EL6FEWl9w?pwd=lisf

![](../../images/037f0533bbcabb83.png)

大家拿到这个数据后，可以用上图中的rds文件参考这个教程(文中的方法三与方法四)对自己手中合适的数据加以注释：[手把手教你做单细胞测序数据分析（五）——‍细胞类型注释](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488597&idx=1&sn=6123d348db245774d4a0db4134a839d4&chksm=9b3f6d05ac48e4132f92ca6c32dab29d2a4e1eb00d1db3b6e10eba7ffc7154e8554a70938583&scene=21#wechat_redirect>)

# **复现过程：**

![](../../images/90fab1387787746b.gif)

**
**

**一、基本信息**

**
**

**1\. 原文标题**

Phiclust: a clusterability measure for single-cell transcriptomics reveals phenotypic subpopulations.

#

**2.****文章链接**

https://pubmed.ncbi.nlm.nih.gov/35012604/

**3\. 物****种**

human fetal

**4.** **GSE编号链接**

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE114530

**5\. 取样方式**

10X-based scRNA-seq data human fetal kidneys at 5 different ages

**6\. 细胞类型**

肾脏组织(fetal kidneys)

**7\. metadata**

细胞类型由Biomamba生信基地团队参考原文图表注释

![](../../images/90fab1387787746b.gif)

**二、数据处****理**

**
**

******s****tep0：加载R包**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
rm(list = ls())options(stringsAsFactors = F)
set.seed(220625)
suppressPackageStartupMessages(library(Seurat))suppressPackageStartupMessages(library(dplyr))suppressPackageStartupMessages(library(ggplot2))suppressPackageStartupMessages(library(ggpubr))suppressPackageStartupMessages(library(monocle))suppressPackageStartupMessages(library(cowplot))suppressPackageStartupMessages(library(stringr))suppressPackageStartupMessages(library(harmony))
```

**step1：处理并加载数****据**

**
**

**1\. 批量整理数据**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
rm(list = ls())options(stringsAsFactors = F)

## 对下载后的压缩文件进行解压，在**Windows**中右键解压即可fs=list.files('./GSE114530_RAW/','^GSM')fslibrary(tidyverse)samples=str_split(fs,'_',simplify = T)[,3]sampleslapply(unique(samples),function(x){  y=fs[grepl(x,fs)]  folder=paste0("GSE114530_RAW/", str_split(y[1],'_',simplify = T)[,3])  dir.create(folder,recursive = T)  file.copy(paste0("GSE114530_RAW/",y[1]),file.path(folder,"barcodes.tsv.gz"))  file.copy(paste0("GSE114530_RAW/",y[2]),file.path(folder,"features.tsv.gz"))  file.copy(paste0("GSE114530_RAW/",y[3]),file.path(folder,"matrix.mtx.gz"))})
```

**2\. 批量读取数据，创建seurat对****象**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
samples <- list.files('./GSE114530_RAW/')samples# [1] "w16"  "wk09" "wk11" "wk13" "wk18"

sce_list <- lapply(samples,function(x){  y = file.path('./GSE114530_RAW',x)  print(y)  sce = CreateSeuratObject(Read10X(y),project = x, min.cells = 3,                            min.features = 200)})

sce_merge <- merge(sce_list[[1]],sce_list[-1],add.cell.ids = samples,merge.data = T)

table(sce_merge$orig.ident)# w16 wk09 wk11 wk13 wk18 # 8479  150 6262 8060 5545

head(sce_merge@meta.data,5)#                        orig.ident nCount_RNA nFeature_RNA# w16_AAACCTGAGAATCTCC-1        w16       3376         1408# w16_AAACCTGAGAGCCTAG-1        w16       2540         1087# w16_AAACCTGAGAGGACGG-1        w16       3334         1540# w16_AAACCTGAGCGATAGC-1        w16       3166         1329# w16_AAACCTGAGCGGCTTC-1        w16       2681         1201
```

**3\. 保存数据**

  *   *

```
save(sce_merge,file = 'sce_merge.RData')
```

**step2：数据质控**

**
**

**1\. 设置环境**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
rm(list = ls())options(stringsAsFactors = F)set.seed(220625)

dir.create("GSE114530_results")setwd("GSE114530_results")

dir.create("1_QC")setwd("1_QC")sce_all <- sce_mergedim(sce_all)# [1] 21802 28496
```

**2\. 计算各类基因占比**

**
**

**(1) 线粒体**

  *   *   *   *   *   *   *   *

```
mt.gene = rownames(sce_all)[grep("^MT-", rownames(sce_all))] mt.gene# [1] "MT-ND1"  "MT-ND2"  "MT-CO1"  "MT-CO2"  "MT-ATP8" "MT-ATP6" "MT-CO3"  "MT-ND3"  "MT-ND4L" "MT-ND4"  "MT-ND5"  "MT-ND6"  "MT-CYB"

sce_all = PercentageFeatureSet(sce_all,"^MT-", col.name = "percent.mt")fivenum(sce_all@meta.data$percent.mt)# [1]  0.000000  1.601241  2.234210  3.218346 66.568915
```

**(2) 核糖体**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
ribo.gene = rownames(sce_all)[grep("^Rp[sl]", rownames(sce_all),ignore.case = T)] ribo.gene# [1] "RPL22"          "RPL11"          "RPS6KA1"        "RPS8"           "RPL5"           "RPS27"          "RPS6KC1"        "RPS7"           "RPS27A"        # [10] "RPL31"          "RPL37A"         "RPL32"          "RPL15"          "RPSA"           "RPL14"          "RPL29"          "RPL24"          "RPL22L1"       # [19] "RPL39L"         "RPL35A"         "RPL9"           "RPL34-AS1"      "RPL34"          "RPS3A"          "RPL37"          "RPS23"          "RPS14"         # [28] "RPL26L1"        "RPS18"          "RPS10-NUDT3"    "RPS10"          "RPL10A"         "RPL7L1"         "RPS12"          "RPS6KA2"        "RPS6KA3"       # [37] "RPS4X"          "RPS6KA6"        "RPL36A"         "RPL39"          "RPL10"          "RPS20"          "RPL7"           "RPL30"          "RPL8"          # [46] "RPS6"           "RPL35"          "RPL12"          "RPL7A"          "RPLP2"          "RPL27A"         "RPS13"          "RPS6KA4"        "RPS6KB2"       # [55] "RPS3"           "RPS25"          "RPS24"          "RPS26"          "RPL41"          "RPL6"           "RPLP0"          "RPL21"          "RPS29"         # [64] "RPL36AL"        "RPS6KL1"        "RPS6KA5"        "RPS27L"         "RPL4"           "RPLP1"          "RPS17"          "RPL3L"          "RPS2"          # [73] "RPS15A"         "RPL13"          "RPL26"          "RPL23A"         "RPL23"          "RPL19"          "RPL27"          "RPS6KB1"        "RPL38"         # [82] "RPL17-C18orf32" "RPL17"          "RPS21"          "RPS15"          "RPL36"          "RPS28"          "RPL18A"         "RPS16"          "RPS19"         # [91] "RPL18"          "RPL13A"         "RPS11"          "RPS9"           "RPL28"          "RPS5"           "RPS4Y1"         "RPS4Y2"         "RPL3"          # [100] "RPS19BP1"

sce_all = PercentageFeatureSet(sce_all,"^RP[SL]",col.name = "percent.ribo")fivenum(sce_all@meta.data$percent.ribo)# [1]  0.1960784 10.2933381 19.8131278 25.7350902 55.1646369
```

**(3) 红细胞基因**

  *   *   *   *   *   *   *   *   *

```
hb.gene = rownames(sce_all)[grep("^Hb[^(p)]", rownames(sce_all),ignore.case = T)]hb.gene# [1] "HBEGF" "HBS1L" "HBB"   "HBD"   "HBG1"  "HBG2"  "HBE1"  "HBZ"   "HBM"   "HBA2"  "HBA1"  "HBQ1"

sce_all = PercentageFeatureSet(sce_all, "^HB[^(P)]", col.name = "percent.hb")fivenum(sce_all@meta.data$percent.hb)# [1]  0.00000000  0.00000000  0.00000000  0.01611604 94.00321543
```

**3\. 可视化**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
feats = c("nCount_RNA","nFeature_RNA")p1 = VlnPlot(sce_all,features = feats,pt.size = 0,group.by = "orig.ident")&NoLegend()&labs(x = '') #&geom_hline(yintercept = 2500)ggsave("vlnplot1.pdf",width = 6,height = 5,dpi = 500) ggsave("vlnplot1.png",width = 6,height = 5,dpi = 500)

feats = c("percent.mt")p1 = VlnPlot(sce_all,features = feats,pt.size = 0,group.by = "orig.ident") + scale_y_continuous(breaks = seq(0,100,10)) + NoLegend() + labs(x = '')ggsave("percentmt.pdf",width = 3,height = 5,dpi = 500) ggsave("percentmt.png",width = 3,height = 5,dpi = 500)

#### (2) percent.mt\ribo\hbfeats = c("percent.ribo","percent.hb","percent.mt")p2 = VlnPlot(sce_all,features = feats,pt.size = 0,group.by = "orig.ident")&scale_y_continuous(breaks = seq(0,100,10))&NoLegend()&labs(x = '') ggsave("vlnplot2.pdf",width = 9,height = 5,dpi = 500)ggsave("vlnplot2.png",width = 9,height = 5,dpi = 500)

#### (3) feature-feature relationshipp3 = FeatureScatter(sce_all,feature1 = "nCount_RNA",feature2 = "nFeature_RNA",group.by = "orig.ident")ggsave("scatter.pdf",width = 5.5,height = 4.6,dpi = 500)ggsave("scatter.png",width = 5.5,height = 4.6,dpi = 500)
```

![](../../images/4f609c4fa090f361.webp)

![](../../images/df214e6ed2896fcf.webp)

![](../../images/fe823ed42c60c781.webp)

**4\. 质控过滤：基因200-6000，线粒体基因占比 <9%**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
select_c = WhichCells(sce_all,expression = nFeature_RNA > 200 & nFeature_RNA < 6000 & percent.mt < 9)length(select_c)# [1] 27210

sce_filt = subset(sce_all,cells = select_c)

dim(sce_filt)# [1] 21802 27210table(sce_filt$orig.ident)# w16 wk09 wk11 wk13 wk18 # 8152  141 5917 7765 5235

summary(sce_filt$nCount_RNA)# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. # 219    2274    3244    3895    4856   32314  summary(sce_filt$nFeature_RNA)# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. # 201    1222    1586    1714    2118    5964    a = as.data.frame(table(sce_filt$orig.ident))summary(a$Freq)# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. # 141    5235    5917    5442    7765    8152
```

**5\. 过滤后可视化**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
## gene and UMIfeats = c("nCount_RNA","nFeature_RNA")p1 = VlnPlot(sce_filt,features = feats,pt.size = 0,group.by = "orig.ident")&NoLegend()&labs(x = '') ggsave("vlnplot1_filtered.pdf",width = 6,height = 5,dpi = 500)ggsave("vlnplot1_filtered.png",width = 6,height = 5,dpi = 500)

feats = c("percent.mt")p1 = VlnPlot(sce_filt,features = feats,pt.size = 0,group.by = "orig.ident") + scale_y_continuous(breaks = seq(0,100,2)) + NoLegend() + labs(x = '') ggsave("percentmt_filtered.pdf",width = 3,height = 5,dpi = 500) ggsave("percentmt_filtered.png",width = 3,height = 5,dpi = 500)

## percent.mt\ribo\hbfeats = c("percent.ribo","percent.hb","percent.mt")p2 = VlnPlot(sce_filt,features = feats,pt.size = 0,group.by = "orig.ident")&NoLegend()&labs(x = '') ggsave("vlnplot2_filtered.pdf",width = 9,height = 5,dpi = 500)ggsave("vlnplot2_filtered.png",width = 9,height = 5,dpi = 500)

## feature-feature relationshipp3 = FeatureScatter(sce_filt,feature1 = "nCount_RNA",feature2 = "nFeature_RNA",group.by = "orig.ident")ggsave("scatter_filtered.pdf",width = 5.5,height = 4.6,dpi = 500)ggsave("scatter_filtered.png",width = 5.5,height = 4.6,dpi = 500)

## 保存数据save(sce_filt,file = "sce_filt.RData")
```

![](../../images/412a1bd0b0f97a06.webp)

![](../../images/8e6d4091c45184a1.webp)

![](../../images/8e2afeaedb0c434a.webp)

**step3：数据整合、降维、聚类分群**

**
**

**1\. 设置环境**

  *   *   *   *   *   *   *   *   *   *   *

```
setwd("../")dir.create("2_int")setwd("2_int")

#load("../GSE114530_results/1_QC/sce_filt.RData")sce_filt# An object of class Seurat # 21802 features across 27210 samples within 1 assay # Active assay: RNA (21802 features, 0 variable features)
```

**2\. 数据预处理 + harmony整合**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
sce.all.filt = NormalizeData(sce_filt)sce.all.filt = FindVariableFeatures(sce.all.filt,selection.method = "vst",nfeatures = 2000, verbose = FALSE)sce.all.filt = ScaleData(sce.all.filt)

sce.all.filt

sce.all.filt = RunPCA(sce.all.filt, npcs = 50)

ElbowPlot(sce.all.filt,50)ggsave2('elbowplot.pdf',width = 6.5,height = 5,dpi = 500)ggsave2('elbowplot.png',width = 6.5,height = 5,dpi = 500)

sce_ha = sce.all.filtpc.num = 1:30

sce_har = RunHarmony(sce_ha,group.by.vars = "orig.ident",project.dim = F,plot_convergence = T)
```

![](../../images/1465ab53abb16b92.webp)

**3\. 分群**

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
sce.har <- sce_harsce.har@active.assaysce.har = FindNeighbors(sce.har, dims = pc.num,reduction = "harmony")## resolution selectionsce.har = FindClusters(sce.har, graph.name = "RNA_snn", resolution = 1.5, algorithm = 1)

table(sce.har@active.ident)#  0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30# 2322 2315 1697 1645 1620 1539 1260 1143 1131 1048  994  905  838  820  813  794  717  706  647  564  560  542  470  347  337  294  288  268  208  160 89#   31   32 #   71   58
```

**4\. 降维及可视化**

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
sce.har = RunUMAP(sce.har, dims = pc.num,reduction = "harmony")save(sce.har,file = "sce_har_tu.RData")

DimPlot(sce.har,label = T,repel = T) + NoLegend()ggsave('umap.pdf',width = 6,height = 6,dpi = 500)ggsave('umap.png',width = 6,height = 6,dpi = 500)

DimPlot(sce.har,label = F,group.by = 'orig.ident')ggsave('umap_indi.pdf',width = 7,height = 6,dpi = 500)ggsave('umap_indi.png',width = 7,height = 6,dpi = 500)
```

![](../../images/9c794af734d9ef29.webp)

![](../../images/e3525a04e45b3830.webp)

**step4：细胞注释**

**
**

**1\. 基因检查**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
rm(list = ls())setwd("../")dir.create("3_markers")setwd("3_markers")load("../2_int/sce_har_tu.RData")

# 这里用的是原文提供的基因genes_to_check = c('SIX2', # NPCa                   'CITED1','GDNF','HES1', # NPCb                   'MEOX1','CRABP2', # NPCc                   'EYA1','LEF1', # NPCd                   'LHX1','JAG1','WNT4','CCND1', # PTA                   'SFRP2','DLL1','LHX1', # RVCSBa                   'CDH6','FOXC2','MAFB','CLDN1','WT1', # RVCSBb                   'HNF1A','CDH6','AMN','CLDN2','ANPEP','SLC34A1', # SSBpr                   'SLC3A1','LRP2','SLC13A1', # SSBpr low                   'IRX1','IRX2','SIM2','SOX9','POU3F3','HNF1B', # SSBm/d                   'PAPPA2','MAL', # SSBm/d low                   'MAL','CLCN5','SLC12A3','POU3F3','SLC12A1','UMOD', # DTLH                   'MAFB','FOXC2','OLFM3', # SSBpod                   'CLIC5','PTPRO','NPHS1','NPHS2', # Podocyte                   'ALDH1A1','TACSTD2','CDH1','SOX9','POU3F3','RET','KRT8','KRT18','MMP7','AQP2','CALB1','GATA2', # CnT                   'FOXD1','GDNF', # IPCs                   'PDGFRA', # IC                   'FGF7','TPM2','ACTA2', # ICa                   'DCN','DES','SERPINE2','COL3A1', # ICb                   'PDGFRB','ACTA2', # mesangial cell                   'KDR','TEK', # Endo                   'CD37','CD48',# immune                   'MKI67','TOP2A')

DefaultAssay(sce.har) = "RNA"DotPlot(sce.har,features = unique(genes_to_check),group.by = 'RNA_snn_res.1.5') + coord_flip()ggsave("har_gene_show.pdf",width = 14,height = 12,dpi = 500)ggsave("har_gene_show.png",width = 14,height = 12,dpi = 500)

# allmarkers <- FindAllMarkers(sce.har,logfc.threshold = 0.5,min.pct = 0.1,only.pos = T)# write.csv(allmarkers,'allmarkers.csv')

# top10 <- allmarkers %>% group_by(cluster) %>% top_n(10,wt = avg_log2FC)# write.csv(top10,'top10.csv')
```

![](../../images/20081cf80eaf3071.webp)

**2\. 注释**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
sce <- sce.harcelltype = data.frame(ClusterID = 0:32,celltype = 'NA')celltype[celltype$ClusterID %in% c(0,1,4,10,20,31),2] = "Pod"celltype[celltype$ClusterID %in% c(2),2] = "SSBpod"celltype[celltype$ClusterID %in% c(3),2] = 'NPCa'celltype[celltype$ClusterID %in% c(5,22,25,32),2] = 'ICb'celltype[celltype$ClusterID %in% c(6,28),2] = 'SSBm/d'celltype[celltype$ClusterID %in% c(7),2] = 'ICa' celltype[celltype$ClusterID %in% c(8),2] = "CnT" celltype[celltype$ClusterID %in% c(9,24),2] = 'ErPrT'celltype[celltype$ClusterID %in% c(18),2] = 'SSBpr'celltype[celltype$ClusterID %in% c(11,15),2] = "NPCd" celltype[celltype$ClusterID %in% c(12),2] = "NPCc"celltype[celltype$ClusterID %in% c(13),2] = 'Unknown' celltype[celltype$ClusterID %in% c(14),2] = "RVCSBa" celltype[celltype$ClusterID %in% c(16),2] = 'NPCb'celltype[celltype$ClusterID %in% c(17),2] = "End" celltype[celltype$ClusterID %in% c(19),2] = "PTA"celltype[celltype$ClusterID %in% c(23),2] = "DTLH"celltype[celltype$ClusterID %in% c(26),2] = 'Leu' celltype[celltype$ClusterID %in% c(21),2] = 'IPC' celltype[celltype$ClusterID %in% c(27),2] = "RVCSBb" celltype[celltype$ClusterID %in% c(29),2] = 'Mes'celltype[celltype$ClusterID %in% c(30),2] = "UBCD"

head(celltype)celltype table(celltype$celltype)sce.har$celltype = "NA"for(i in 1:nrow(celltype)){  sce.har@meta.data[which(sce.har@meta.data$RNA_snn_res.1.5 == celltype$ClusterID[i]),'celltype'] <- celltype$celltype[i]}table(sce.har@meta.data$celltype)# CnT    DTLH     End   ErPrT     ICa     ICb     IPC     Leu     Mes    NPCa    NPCb    NPCc    NPCd     Pod     PTA  RVCSBa  RVCSBb  SSBm/d  SSBpod # 1131     347     706    1385    1143    2361     542     288     160    1645     717     838    1699    7882     564     813     268    1468    1697 # SSBpr    UBCD Unknown # 647      89     820

Idents(sce.har) = sce.har$celltypeIdents(sce.har) = factor(Idents(sce.har),levels = c('NPCa','NPCb','NPCc','NPCd','PTA','RVCSBa','RVCSBb','SSBm/d','SSBpr',                                                    'SSBpod','CnT','DTLH','ErPrT','Pod','UBCD','IPC','ICa','ICb','Mes','End','Leu','Unknown'))sce.har$celltype <- Idents(sce.har)Idents(sce.har) <- factor(Idents(sce.har),levels = rev(levels(Idents(sce.har))))
```

**3\. 看一下注释后的marker**

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
DotPlot(sce.har,features = unique(genes_to_check),cols = c("grey","red")) + theme_bw(base_line_size = 0) +   theme(axis.text.x = element_text(angle = 90,hjust = 1,vjust = 0.5),panel.grid = element_blank()) + labs(x='',y='')ggsave("dotplot_anno.png",width = 19,height = 8,dpi = 500)ggsave("dotplot_anno.pdf",width = 19,height = 8,dpi = 500)

library(RColorBrewer)color_ct=c(brewer.pal(12, "Set3"),"#b3b3b3",           brewer.pal(5, "Set1"),           brewer.pal(3, "Dark2"),           "#fc4e2a","#fb9a99","#f781bf","#e7298a")if(!require(ggunchull))devtools::install_github("sajuukLyu/ggunchull", type = "source")if(!require(scRNAtoolVis))devtools::install_github('junjunlab/scRNAtoolVis')
```

![](../../images/677476cc6bd3275d.webp)

**注释后可视化**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
## umap/tsneclusterCornerAxes(object = sce.har,reduction = 'umap',clusterCol = 'celltype',pSize = 0.1,cellLabel = T,cellLabelSize = 5,                  noSplit = T) +  scale_color_manual(values = alpha(color_ct,0.65)) + NoLegend() +  scale_fill_manual(values = alpha(color_ct,0.65))ggsave("umap.pdf",width = 10,height = 9,dpi = 500)ggsave("umap.png",width = 10,height = 9,dpi = 500)

clusterCornerAxes(object = sce.har,reduction = 'tsne',clusterCol = 'celltype',cellLabel = T,cellLabelSize = 5,                  noSplit = T) +  scale_color_manual(values = alpha(color_ct,0.65)) +  NoLegend() +  scale_fill_manual(values = alpha(color_ct,0.65))ggsave("tsne.pdf",width = 10,height = 9,dpi = 500)ggsave("tsne.png",width = 10,height = 9,dpi = 500)

clusterCornerAxes(object = sce.har,reduction = 'umap',clusterCol = 'orig.ident',pSize = 0.01,                  noSplit = T) ggsave("umap_indi.pdf",width = 5.5,height = 5,dpi = 500)ggsave("umap_indi.png",width = 5.5,height = 5,dpi = 500)

clusterCornerAxes(object = sce.har,reduction = 'tsne',clusterCol = 'orig.ident',pSize = 0.01,                  noSplit = T) ggsave("tsne_indi.pdf",width = 5.5,height = 5,dpi = 500)ggsave("tsne_indi.png",width = 5.5,height = 5,dpi = 500)

clusterCornerAxes(object = sce.har,reduction = 'tsne',clusterCol = 'orig.ident',pSize = 0.01,groupFacet = 'orig.ident',noSplit = F) + NoLegend()ggsave("tsne_indi_s.pdf",width = 15,height = 4,dpi = 500)ggsave("tsne_indi_s.png",width = 15,height = 4,dpi = 500)

clusterCornerAxes(object = sce.har,reduction = 'umap',clusterCol = 'orig.ident',pSize = 0.01,groupFacet = 'orig.ident',noSplit = F) + NoLegend()ggsave("umap_indi_s.pdf",width = 15,height = 4,dpi = 500)ggsave("umap_indi_s.png",width = 15,height = 4,dpi = 500)

save(sce.har,file = 'sce_har_anno.RData')
```

![](../../images/2310795cb694d4a0.webp)

![](../../images/886349f2b949e899.webp)

![](../../images/98b23bf2a8d5e424.webp)

**4\. 注释后查看细胞数**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
table(sce.har$celltype)# NPCa    NPCb    NPCc    NPCd     PTA  RVCSBa  RVCSBb  SSBm/d   SSBpr  SSBpod     CnT    DTLH   ErPrT     Pod    UBCD     IPC     ICa     ICb     Mes # 1645     717     838    1699     564     813     268    1468     647    1697    1131     347    1385    7882      89     542    1143    2361     160 # End     Leu Unknown # 706     288     820 as.data.frame(table(sce.har$orig.ident,sce.har$celltype))#     Var1    Var2 Freq# 1    w16    NPCa  703# 2   wk09    NPCa    9# 3   wk11    NPCa  555# 4   wk13    NPCa  238# 5   wk18    NPCa  140# 6    w16    NPCb  491# 7   wk09    NPCb    3# 8   wk11    NPCb  118# 9   wk13    NPCb   45# 10  wk18    NPCb   60# 11   w16    NPCc  307# 12  wk09    NPCc    8# 13  wk11    NPCc  349# 14  wk13    NPCc   88# 15  wk18    NPCc   86# 16   w16    NPCd  706# 17  wk09    NPCd   13# 18  wk11    NPCd  457# 19  wk13    NPCd  270# 20  wk18    NPCd  253# 21   w16     PTA  244# 22  wk09     PTA    6# 23  wk11     PTA  128# 24  wk13     PTA   76# 25  wk18     PTA  110# 26   w16  RVCSBa  265# 27  wk09  RVCSBa    1# 28  wk11  RVCSBa  147# 29  wk13  RVCSBa  207# 30  wk18  RVCSBa  193# 31   w16  RVCSBb   84# 32  wk09  RVCSBb    1# 33  wk11  RVCSBb   52# 34  wk13  RVCSBb   62# 35  wk18  RVCSBb   69# 36   w16  SSBm/d  270# 37  wk09  SSBm/d   12# 38  wk11  SSBm/d  365# 39  wk13  SSBm/d  659# 40  wk18  SSBm/d  162# 41   w16   SSBpr  146# 42  wk09   SSBpr    3# 43  wk11   SSBpr  180# 44  wk13   SSBpr  201# 45  wk18   SSBpr  117# 46   w16  SSBpod  352# 47  wk09  SSBpod    1# 48  wk11  SSBpod  302# 49  wk13  SSBpod  598# 50  wk18  SSBpod  444# 51   w16     CnT  592# 52  wk09     CnT   12# 53  wk11     CnT  118# 54  wk13     CnT  248# 55  wk18     CnT  161# 56   w16    DTLH   54# 57  wk09    DTLH    3# 58  wk11    DTLH   85# 59  wk13    DTLH  171# 60  wk18    DTLH   34# 61   w16   ErPrT  350# 62  wk09   ErPrT    5# 63  wk11   ErPrT  254# 64  wk13   ErPrT  452# 65  wk18   ErPrT  324# 66   w16     Pod  729# 67  wk09     Pod   21# 68  wk11     Pod 1573# 69  wk13     Pod 3675# 70  wk18     Pod 1884# 71   w16    UBCD   68# 72  wk09    UBCD    0# 73  wk11    UBCD    3# 74  wk13    UBCD   10# 75  wk18    UBCD    8# 76   w16     IPC  280# 77  wk09     IPC    5# 78  wk11     IPC  102# 79  wk13     IPC   61# 80  wk18     IPC   94# 81   w16     ICa  582# 82  wk09     ICa    8# 83  wk11     ICa  207# 84  wk13     ICa   87# 85  wk18     ICa  259# 86   w16     ICb 1190# 87  wk09     ICb   12# 88  wk11     ICb  514# 89  wk13     ICb  216# 90  wk18     ICb  429# 91   w16     Mes   87# 92  wk09     Mes    1# 93  wk11     Mes   14# 94  wk13     Mes   14# 95  wk18     Mes   44# 96   w16     End  315# 97  wk09     End    1# 98  wk11     End   86# 99  wk13     End  170# 100 wk18     End  134# 101  w16     Leu  126# 102 wk09     Leu    0# 103 wk11     Leu   38# 104 wk13     Leu   55# 105 wk18     Leu   69# 106  w16 Unknown  211# 107 wk09 Unknown   16# 108 wk11 Unknown  270# 109 wk13 Unknown  162# 110 wk18 Unknown  161
```

![](../../images/56869e2cc75aa830.png)

如何联系我们

![](../../images/7c0febec2249cfa6.gif)公众号后台中消息更新不及时，超过48h后便不允许回复读者消息，这里给大家留一下领取资料、咨询服务器的**微信号** ，方便大家随时交流、提建议（由助理接待）。此外呼声一直很高的交流群也建好了，欢迎大家入群讨论：[你们要的微信、交流群，来了！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487083&idx=1&sn=312a8435f6b938602624a7e9028ad3c6&chksm=9b3f773bac48fe2d3a2886988b35b006bbd05da11e2d7f735afc78c02ffbd179ebc9722a97cd&scene=21#wechat_redirect>)
大家可以阅读完这几篇之后添加[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](../../images/fdb4c49c78e6216c.webp)
