---
title: "勘误| infercnv亚群注释"
date: 2025-05-18
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528855&idx=1&sn=a300e28967e868d16babad700e35883a&chksm=9b3c08c7ac4b81d1f6dbfed2f997ef3a87e7c90cc9a77771e66434c46362065d60459683b744#rd
albums: ["单细胞教程全收录"]
---

# 勘误| infercnv亚群注释

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528855&idx=1&sn=a300e28967e868d16babad700e35883a&chksm=9b3c08c7ac4b81d1f6dbfed2f997ef3a87e7c90cc9a77771e66434c46362065d60459683b744#rd
> 合集：单细胞教程全收录

**一、发现问题**

有同学提问我们的[单细胞拷贝数变异学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522733&idx=1&sn=4e3a0707fd8f83b5ad9377bc91ee8e53&scene=21#wechat_redirect>)中根据infercnv score的聚类分群部分描述有问题，这是由于给大家编译教程的环境和我们之前测试环境不一致造成的。图片显示cluster1、3、5、6亚群的c明显高于2、4两个亚群，cluster7的界限就比较模糊了。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwUHtyDG8kmTBjgA0aubSiaQ1krScvYpZEDchDr5nnKKWtQb32vlpeWAg/640?wx_fmt=png&from=appmsg)
不过在先前注释的细胞比例中，cluster7与Malignant cells的交叉比例还是非常高的，考虑到infercnv score，那我们就姑且叫它"Malignant-transition cells"。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwhEKABCEfzIptMq6u58JopL6yo0iaJR9fAggaTib5zxBHDiaDV5RsLgwuQ/640?wx_fmt=png&from=appmsg)

**二、解决问题**

这部分修正后的流程如下，完整拷贝数变异分析教程与测试文件可见：[单细胞拷贝数变异学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522733&idx=1&sn=4e3a0707fd8f83b5ad9377bc91ee8e53&scene=21#wechat_redirect>)

### 5.2 infercnv流程

这里我们再走一遍infercnv的基础流程

  *   *   *

```
# 加载包：library(infercnv)library(tidyverse)
```
```
## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
## ✔ dplyr     1.1.4     ✔ readr     2.1.5
## ✔ forcats   1.0.0     ✔ stringr   1.5.1
## ✔ ggplot2   3.5.1     ✔ tibble    3.2.1
## ✔ lubridate 1.9.4     ✔ tidyr     1.3.1
## ✔ purrr     1.0.2
## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors
```

  *   *

```r
library(ComplexHeatmap)library(circlize)
```

  *   *   *   *

```r
library(RColorBrewer)library(infercnv)### 整理数据 ###exprMatrix <- as.matrix(GetAssayData(Epi, slot='counts'))# 获取count矩阵
```
```
## Warning: The `slot` argument of `GetAssayData()` is deprecated as of SeuratObject 5.0.0.
## ℹ Please use the `layer` argument instead.
## This warning is displayed once every 8 hours.
## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
## generated.
```

  *   *

```r
cellAnnota <- subset(Epi@meta.data,select='Cell_subtype')# 取出分组注释信息dir.create('Epi_infercnv/')# 创建文件夹
```
```
## Warning in dir.create("Epi_infercnv/"): 'Epi_infercnv' already exists
```

  *   *   *

```
write.table(cellAnnota,file ="Epi_infercnv/groupFiles.txt",sep = '\t',col.names = F)# 把分组注释信息写到本地### 制作基因与染色体位置的文件 ###if(!require(AnnoProbe))install.packages('AnnoProbe')# 加载注释基因信息的包
```
```
## Loading required package: AnnoProbe
## AnnoProbe v 0.1.7  welcome to use AnnoProbe!
## If you use AnnoProbe in published research, please acknowledgements:
## We thank Dr.Jianming Zeng(University of Macau), and all the members of his bioinformatics team, biotrainee, for generously sharing their experience and codes.
```

  *

```
geneInfor=annoGene(rownames(Epi),"SYMBOL",'human')#  获取基因注释信息，这里物种是人，如果是小鼠，把human换成mouse
```
```
## Warning in annoGene(rownames(Epi), "SYMBOL", "human"): 31.29% of input IDs are
## fail to annotate...
```

  *

```
colnames(geneInfor)# 包含以下信息
```
```
## [1] "SYMBOL"   "biotypes" "ENSEMBL"  "chr"      "start"    "end"
```

  *   *   *

```
geneInfor=geneInfor[with(geneInfor, order(chr, start)),c(1,4:6)]# 选取基因的geneInfor=geneInfor[!duplicated(geneInfor[,1]),]# 去重length(unique(geneInfor[,1]))# 查看一共有多少基因
```
```
## [1] 20363
```

  *

```
head(geneInfor)# 查看最终的注释信息
```
```
##        SYMBOL  chr  start    end
## 23 AP006222.2 chr1 266855 268655
## 51     FAM87B chr1 817371 819837
## 53  LINC00115 chr1 826206 827522
## 55     FAM41C chr1 868071 876903
## 62     SAMD11 chr1 923928 944581
## 63      NOC2L chr1 944203 959309
```

  *   *   *   *   *   *   *

```
write.table(geneInfor, 'Epi_infercnv/geneLocate.txt', row.names=F, col.names=F, sep='\t')# 注释信息需要写到本地供infercnv读取# 创建infercnv对象：infercnv_obj = CreateInfercnvObject(raw_counts_matrix=exprMatrix,                                    annotations_file="Epi_infercnv/groupFiles.txt",                                    delim="\t",                                    gene_order_file= "Epi_infercnv/geneLocate.txt",                                    ref_group_names="AT1")
```
```
## INFO [2025-05-16 04:45:04] Parsing gene order file: Epi_infercnv/geneLocate.txt
## INFO [2025-05-16 04:45:04] Parsing cell annotations file: Epi_infercnv/groupFiles.txt
## INFO [2025-05-16 04:45:04] ::order_reduce:Start.
## INFO [2025-05-16 04:45:04] .order_reduce(): expr and order match.
## INFO [2025-05-16 04:45:04] ::process_data:order_reduce:Reduction from positional data, new dimensions (r,c) = 29634,1500 Total=13628902 Min=0 Max=5783.
## INFO [2025-05-16 04:45:05] num genes removed taking into account provided gene ordering list: 10109 = 34.1128433556051% removed.
## INFO [2025-05-16 04:45:05] -filtering out cells < 100 or > Inf, removing 0 % of cells
## WARN [2025-05-16 04:45:05] Please use "options(scipen = 100)" before running infercnv if you are using the analysis_mode="subclusters" option or you may encounter an error while the hclust is being generated.
## INFO [2025-05-16 04:45:06] validating infercnv_obj
```

  *   *   *   *   *   *   *   *

```
# 运行infercnv：infercnv_obj = infercnv::run(infercnv_obj,                              cutoff=0.1, # use 1 for smart-seq, 0.1 for 10x-genomics                               out_dir=  'Epi_infercnv/output' ,  # dir is auto-created for storing outputs                              hclust_method="ward.D2", plot_steps=F,denoise=TRUE,                              HMM=F,  ##特别耗时间                              num_threads=10)
```
```
## INFO [2025-05-16 04:45:06] ::process_data:Start
## INFO [2025-05-16 04:45:06] Checking for saved results.
## INFO [2025-05-16 04:45:06] Trying to reload from step 22
## INFO [2025-05-16 04:45:07] Using backup from step 22
## INFO [2025-05-16 04:45:07] Trying to reload from step 15
## INFO [2025-05-16 04:45:07]
##
##  STEP 1: incoming data
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 02: Removing lowly expressed genes
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 03: normalization by sequencing depth
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 04: log transformation of data
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 08: removing average of reference data (before smoothing)
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 09: apply max centered expression threshold: 3
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 10: Smoothing data per cell by chromosome
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 11: re-centering data across chromosome after smoothing
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 12: removing average of reference data (after smoothing)
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 14: invert log2(FC) to FC
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 15: computing tumor subclusters via leiden
##
## INFO [2025-05-16 04:45:07]
##
##  STEP 22: Denoising
##
## INFO [2025-05-16 04:45:10]
##
## ## Making the final infercnv heatmap ##
## INFO [2025-05-16 04:45:11] ::plot_cnv:Start
## INFO [2025-05-16 04:45:11] ::plot_cnv:Current data dimensions (r,c)=7292,1500 Total=10988883.0171584 Min=0.762388537428658 Max=1.57869976486215.
## INFO [2025-05-16 04:45:11] ::plot_cnv:Depending on the size of the matrix this may take a moment.
## INFO [2025-05-16 04:45:12] plot_cnv(): auto thresholding at: (0.829906 , 1.170094)
## INFO [2025-05-16 04:45:12] plot_cnv_observation:Start
## INFO [2025-05-16 04:45:12] Observation data size: Cells= 1000 Genes= 7292
## INFO [2025-05-16 04:45:12] plot_cnv_observation:Writing observation groupings/color.
## INFO [2025-05-16 04:45:12] plot_cnv_observation:Done writing observation groupings/color.
## INFO [2025-05-16 04:45:12] plot_cnv_observation:Writing observation heatmap thresholds.
## INFO [2025-05-16 04:45:12] plot_cnv_observation:Done writing observation heatmap thresholds.
```
```
## INFO [2025-05-16 04:45:13] Colors for breaks:  #00008B,#24249B,#4848AB,#6D6DBC,#9191CC,#B6B6DD,#DADAEE,#FFFFFF,#EEDADA,#DDB6B6,#CC9191,#BC6D6D,#AB4848,#9B2424,#8B0000
## INFO [2025-05-16 04:45:13] Quantiles of plotted data range: 0.829906399244205,1.00117985183862,1.00117985183862,1.00117985183862,1.1700936007558
```
```
## INFO [2025-05-16 04:45:14] plot_cnv_references:Start
## INFO [2025-05-16 04:45:14] Reference data size: Cells= 500 Genes= 7292
## INFO [2025-05-16 04:45:16] plot_cnv_references:Number reference groups= 1
## INFO [2025-05-16 04:45:16] plot_cnv_references:Plotting heatmap.
```
```
## INFO [2025-05-16 04:45:16] Colors for breaks:  #00008B,#24249B,#4848AB,#6D6DBC,#9191CC,#B6B6DD,#DADAEE,#FFFFFF,#EEDADA,#DDB6B6,#CC9191,#BC6D6D,#AB4848,#9B2424,#8B0000
## INFO [2025-05-16 04:45:16] Quantiles of plotted data range: 0.829906399244205,1.00117985183862,1.00117985183862,1.00117985183862,1.1700936007558
```

看一下”那一张热图“：
![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwvOoZEP7rWZl9ZoxbmUuic6Qto1Y4WrFmelib5dglMibnSgY81AfbAhFiaQ/640?wx_fmt=png&from=appmsg)
可以看到作为参考的`AT1`(上方热图)发生的拷贝数变异事件比较少。而`Malignant cells`出现了大量且密集的拷贝数变异。`tS1`似乎也存在着少量的拷贝数变异，所以单凭热图还不行，还得继续分析。

### 5.4 小提琴图

#### (1)从细胞类群的角度看

  *   *

```
### 转化cnvscore数据 ###fivenum(expr)# 原始的cov_score是以1为中心分布的数据
```
```
## [1] 0.7623885 1.0011799 1.0011799 1.0011799 1.5786998
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
CNV_score=expr-1# 转换为以0为中心分布的数据CNV_score=CNV_score ^ 2# 平方，防止累加的过程中cnv lose和cnv gain相互抵消，造成没有cnv事件发生的假象CNV_score=as.data.frame(colMeans(CNV_score))# 以细胞为单位，获得cnv scorecolnames(CNV_score)="CNV_score"# 更改列名CNV_score$CB=rownames(CNV_score)# 加入cell barcode列kmeans_df_s$CB=rownames(kmeans_df_s)# 把kmeans_df_s中的cell barcode也加上CNV_score=CNV_score%>%inner_join(kmeans_df_s,by="CB")# 合并cnvscore和聚类结果library(ggplot2)library(ggsignif) ggplot(CNV_score,aes(Sub_type,CNV_score,fill=Sub_type))+      geom_violin(alpha=0.4)+ #小提琴图需要一定的透明度      stat_boxplot(geom="errorbar",position = position_dodge(width = 0.1),width=0.1)+ # 加上误差棒      geom_boxplot(alpha=0.5,outlier.size=0, size=0.3, width=0.3)+ # 加上箱线图      scale_fill_manual(values = ggsci::pal_aaas()(3))+ # 填充颜色      theme_bw()+# 主题为空白      geom_signif(comparisons = list(c("AT1","tS1"),                                     c("tS1", "Malignant cells"),                                     c("AT1" ,"Malignant cells")),                  step_increase = 0.1,map_signif_level = F)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwLSEXciahub2cmjRxtltPqDH1YtAZXIFiarkgV82bI4iaDA3pBBrEmkiapA/640?wx_fmt=png&from=appmsg)

作为正常细胞的`AT1`与`tS1`与`Malignant` cells之间的统计结果呈现出极显著的关系，而AT1与tS1之间则没有显著性差异(0.086)

#### (2) 从聚类的角度来看

  *   *   *   *   *   *

```
ggplot(CNV_score,aes(kmeans_class,CNV_score,fill=kmeans_class))+    geom_violin(alpha=0.4)+ #小提琴图需要一定的透明度    stat_boxplot(geom="errorbar",position = position_dodge(width = 0.1),width=0.1)+ # 加上误差棒    geom_boxplot(alpha=0.5,outlier.size=0, size=0.3, width=0.3)+ # 加上箱线图    scale_fill_manual(values = ggsci::pal_nejm()(8))+ # 填充颜色    theme_bw()# 主题为空白
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwOJH4VtycyibQWC3MBBAjK90ibQiaMPQqM8wjPI3WRkYY0UMRJTXXQggyQ/640?wx_fmt=png&from=appmsg)实际上cluster1、3、5、6亚群的c明显高于2、4两个亚群，cluster7的界限就比较模糊了。我们可以通过cluster在Sub_type中的亚群来辅助判断它们的身份：

  *   *   *   *   *   *   *   *   *   *

```r
cell.prop<-as.data.frame(prop.table(table(CNV_score$kmeans_class, CNV_score$Sub_type)))colnames(cell.prop)<-c("kmeans_class","Sub_type","proportion")ggplot(cell.prop,aes(kmeans_class,proportion,fill=Sub_type))+geom_bar(stat="identity",position="fill")+ggtitle("")+theme_bw()+theme(axis.ticks.length=unit(0.5,'cm'))+guides(fill=guide_legend(title=NULL))+  theme( axis.text.x.bottom = element_text(angle = 45,hjust = 1,vjust = 1))+  scale_fill_manual(values = ggsci::pal_nejm()(8)) # 填充颜色
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwxOTuKA7pTtHdMg4ktI7p07q3IkaA5usC8hMx0DmYAJJ20ovTnBnHbA/640?wx_fmt=png&from=appmsg)果然不出所料，1、3、5、6中均存在很高比例的Malignant cells，而cluster7与Malignant cell的交叉比例较高，假设这是一个未经注释的数据集，我一定会这么命名：

  *   *   *   *   *   *   *   *   *

```r
CNV_score$Type <- recode(CNV_score$kmeans_class,                                  '1'='Malignant cells',                                  '2'='Normal Epi',                                  '3'='Malignant cells',                                  '4'='Normal Epi',                                  '5'='Malignant cells',                                  '6'='Malignant cells',                                  '7'='Malignant-transition cells')unique(CNV_score$Type)
```
```
## [1] Normal Epi                 Malignant cells
## [3] Malignant-transition cells
## Levels: Malignant cells Normal Epi Malignant-transition cells
```

  *   *   *   *   *   *   *   *   *   *   *

```
# 看一下重命名过的cnv score怎么分布：ggplot(CNV_score,aes(Type,CNV_score,fill=Type))+    geom_violin(alpha=0.4)+ #小提琴图需要一定的透明度    stat_boxplot(geom="errorbar",position = position_dodge(width = 0.1),width=0.1)+ # 加上误差棒    geom_boxplot(alpha=0.5,outlier.size=0, size=0.3, width=0.3)+ # 加上箱线图    scale_fill_manual(values = ggsci::pal_nejm()(8))+ # 填充颜色    theme_bw()+# 主题为空白    geom_signif(comparisons = list(c( 'Malignant cells', 'Normal Epi'),                                   c('Normal Epi', 'Malignant-transition cells'),                                   c('Malignant cells', 'Malignant-transition cells')),                step_increase = 0.1,map_signif_level = F)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwZQBncrCr2eyotJajOShhHNFeqh2kiaGP5YY1PibuunQAZNic7IjHyAVCA/640?wx_fmt=png&from=appmsg)猜的没错，三个类型的cnv score两两间均有显著性差异，我们可以将这个注释导回原来的上皮细胞Seurat对象中：
```r
rownames(CNV_score) <- CNV_score$CB# 设置Cell barcode行名，AddMeta会按照行名匹配

Epi <-AddMetaData(Epi,metadata = CNV_score)# 添加CNV score注释信息

Idents(Epi) <-'Type'# 改变Seurat对象默认标签

DimPlot(Epi,cols = ggsci::pal_nejm()(8))# 查看不同type的降维情况
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3Twgq9qmTtnkSN2UyNaQuTaLNr0NXrBJEt6Pn8k4NNSUvhyMtqEmaMs9A/640?wx_fmt=png&from=appmsg)

  *   *   *

```r
# 下面的工作就是生物学方面的意义啦，比如做个差异分析：  DEG <- FindMarkers(Epi, ident.1 = 'Malignant cells',ident.2 = 'Normal Epi')head(DEG)
```
```
##                  p_val avg_log2FC pct.1 pct.2     p_val_adj
## IGFBP3   2.298313e-120   6.362855 0.526 0.021 6.810821e-116
## TMEM176B  5.718259e-98   4.859484 0.558 0.060  1.694549e-93
## HMGB3     2.088671e-95   4.098322 0.761 0.183  6.189567e-91
## VSTM2L    1.889219e-94   4.029765 0.544 0.053  5.598510e-90
## TMEM176A  1.495375e-91   4.775832 0.516 0.051  4.431395e-87
## GAPDH     1.454763e-88   1.793153 0.986 0.830  4.311043e-84
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
DEG$Gene <- row.names(DEG)# 画个火山图看一下：   ggplot(DEG,aes(avg_log2FC , -log10(p_val)))+  # 横向水平参考线：  geom_hline(yintercept = -log10(0.05), linetype = "dashed", color = "#999999")+  # 纵向垂直参考线：  geom_vline(xintercept = c(-1.2,1.2), linetype = "dashed", color = "#999999")+  # 散点图:  geom_point(aes(size=-log10(p_val), color= -log10(p_val)))+  # 指定颜色渐变模式：  scale_color_gradientn(values = seq(0,1,0.2),                        colors = c("#39489f","#39bbec",'#FFA500',"#f38466","#b81f25"))+  # 指定散点大小渐变模式：  scale_size_continuous(range = c(0.5,4))+  # 主题调整：  theme_bw()+  # 调整主题和图例位置：  # theme(panel.grid = element_blank(),  #       legend.position = c(0.01,0.7),  #       legend.justification = c(0,1)  # )+  # 设置部分图例不显示：  guides(col = guide_colourbar(title = "-Log10_q-value"),         size = "none")+  # 添加标签：  geom_text(aes(label=Gene, color = -log10(p_val)), size = 3, vjust = 1.5, hjust=1)+  # 修改坐标轴：  xlab("Log2FC")+  ylab("-Log10(FDR q-value)")
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw0NDcqDcKsnLh9uoDUT3TwJN3Cu7ibibAznhticqWktbo61CL9GeUCGKzQSibNkjcXKm26EnHVTVyNwg/640?wx_fmt=png&from=appmsg)

**三、欢迎勘误**

人要勇于承认自己的错误并改正![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_14@2x.png)。这里也允许我找个小借口，我们的很多教程都是数万字代码+注释+数十GB的文件，很难保证一桩桩一件件都没有错误。欢迎大家为我们勘误，不仅能够帮助我们做的更好，更能帮助其它粉丝朋友们少走弯路~
Biomamba生信基地还给大家准备了大量的周边，可以作为大家为我们勘误的小礼品任选一件~
Linux速查超大鼠标垫：![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwxvBkwhVBCGFWFIYwS7u9RO1DA22lRWyU5ONLdgL6VoUBXNTtpDib1VSS9eUOufbhH7LOr3gKtgyg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)
Biomamba同款背包与词云展示：![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzLmznOnvnQ1c5NalBlCLKxRK7BBFFVY92BicN8MMDdadYIxtuA17IJN8jvTtyJxoGoxxHoKEFicbKA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw1iaU2Vvcj9zsGVYWvqIdzpvm0VWOKYTsNLpfwY2Ea0ic3YL4RxhibMgkAYrZLpOnBZCk7Xe9SiawaSw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

金士顿64GB、3.0存储高速U盘：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyWaOKGagbYpZrLeBC5pxjbV6G3Ksz4WGkql0hGTxtZZTX8j9q5ZIkaR8w9hic1QrAwkjKVF7oBAHw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**Biomamba生信基地定制咖啡杯吧！Biomamba亲测好用，质感高级![图片](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png?tp=webp&wxfrom=5&wx_lazy=1)**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwDwviaZibEEU8S7ffoRDPY7GPxT1AhGe3OMIbO3BqlVVlaw0AZkXfOAs5U4IMmeCTJiaUgsK4NZjgIA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
