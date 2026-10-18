---
title: "Seurat单细胞亚群分析"
date: 2026-01-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534661&idx=1&sn=16872e942170ace88f26deb0ea6c4b34&chksm=9b3c3115ac4bb803117843eac175a7f37f0934d4b84ac7f88461eb1e23e2b754d380093d22d2#rd
albums: ["单细胞教程全收录"]
---

# Seurat单细胞亚群分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534661&idx=1&sn=16872e942170ace88f26deb0ea6c4b34&chksm=9b3c3115ac4bb803117843eac175a7f37f0934d4b84ac7f88461eb1e23e2b754d380093d22d2#rd
> 合集：单细胞教程全收录

![](../../images/f225780b0e012caf.gif)

**一、写在前面**

## **[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>) RNA 测序（scRNA-seq）技术的飞速发展，彻底打破了传统 [bulk RNA-seq](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2959853503529910274#wechat_redirect>) 对细胞群体 “平均化” 解读的局限，使我们能够以单细胞分辨率解析细胞异质性、挖掘稀有细胞亚群、揭示细胞命运转变轨迹，为发育生物学、肿瘤学、免疫学等领域的研究带来了革命性突破。在复杂的单细胞数据分析流程中，细胞亚群划分与注释是核心环节 —— 它不仅是识别细胞类型、解析群体结构的基础，更是后续差异基因分析、细胞互作网络构建、疾病机制探索的前提。简单来说，亚群分析是单细胞当中的常见“套路”。Seura中单细胞亚群分析视频教程可见：**

更多单细胞教程可见：[100个小时沉浸式学会scRNA-seq数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531092&idx=1&sn=9968319b84186bb9b717b7b409132d8b&scene=21#wechat_redirect>)和[82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)

学前tips:

本教程基于Linux环境的[Rstudio](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247524106&idx=1&sn=f23405302a3705007d33b688870196e0&scene=21#wechat_redirect>)演示，计算资源不足的同学可参考：

[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21&token=1904068475&lang=zh_CN#wechat_redirect>)

[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21&token=1904068475&lang=zh_CN&poc_token=HF-eN2mj01zsfxe_I4r8D5pfZx80xO2AVYSB6qtT#wechat_redirect>)

[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21&token=1904068475&lang=zh_CN&poc_token=HHWeN2mjUe1w7qMDvfaBNJZRTCq3qpve8MrnSv_z#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

欢迎联系客服微信[Biomamba_zhushou]获取帮助

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)、自测数据个性化分析辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、测试数据**

这是我们此前演示scDEAL时用到的小鼠胚胎数据，我们将选取数量最多的Epiblast进行亚群分析。
```r
library(Seurat)
```
```
## Loading required package: SeuratObject
```
```
## Loading required package: sp
```
```
## 'SeuratObject' was built with package 'Matrix' 1.7.1 but the current
## version is 1.7.2; it is recomended that you reinstall 'SeuratObject' as
## the ABI for 'Matrix' may have changed
```
```
##
## Attaching package: 'SeuratObject'
```
```
## The following objects are masked from 'package:base':
##
##     intersect, t
```

###
```r
# 数据读取：
scRNA <-readRDS('mice_embryo.rds')
# 查看降维情况
p1 <-DimPlot(scRNA,group.by ='celltype',label =T)
p1
```

### **![](../../images/8d3906010de85ea3.webp)**

###
```
# 该数据共包含16152个细胞：scRNA
```
```
## An object of class Seurat
## 5000 features across 16152 samples within 1 assay
## Active assay: RNA (5000 features, 2000 variable features)
##  3 layers present: counts, data, scale.data
##  2 dimensional reductions calculated: pca, tsne
```
```
# 各细胞类型数量：
table(scRNA$celltype)
```
```
##
## Anterior Primitive Streak           Caudal epiblast           Caudal Mesoderm
##                       437                         9                         1
##                  Epiblast              ExE ectoderm              ExE endoderm
##                      5625                      2441                      1668
##              ExE mesoderm     Intermediate mesoderm                Mesenchyme
##                        73                         3                       138
##            Mixed mesoderm          Nascent mesoderm         Parietal endoderm
##                       505                      2033                       105
##          Primitive Streak         Visceral endoderm
##                      2755                       359
```

### **✌**** Seurat::FindSubCluster()**

### **1.亚群分析**

` FindSubCluster`算是最简单直接的方法，能够直接在原有的Seurat对象中指定选定的细胞类型名称、`graph.name`、`resolution`等选项参数，直接生成一列包含亚群信息的注释。使用起来很简单：
```r
library(ggplot2)
# 提前设定分辨率：
my_resolution <-0.3
scRNA <-FindSubCluster(scRNA,# 原来的Seurat对象
resolution = my_resolution , # 指定分亚群的分辨率
graph.name ='RNA_snn',# 聚类算法中的graph名称，可以在scRNA@graphs找，一般为"RNA_nn"与"RNA_snn"，nn = Nearest Neighbors（最近邻，无权重），snn = Shared Nearest Neighbors（共享最近邻，有权重，更适合亚群精细拆分）
cluster ='Epiblast',# 想要分压群的细胞类型
subcluster.name =paste0('Epiblast_res_',my_resolution)# 存储亚群信息的slot
                        )
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 211402
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.8398
## Number of communities: 4
## Elapsed time: 0 seconds
```
```
# 降维展示包含大群细胞的亚群，可以看到Epiblast被分为了0-3这4个亚群：
DimPlot(scRNA,group.by =paste0('Epiblast_res_',my_resolution))
```

### **![](../../images/1430dbe0bdf96901.webp)**
```r
# 单独展示这部分亚群：
sub_cell<- scRNA[,grep('^Epiblast_',scRNA$Epiblast_res_0.3)]
DimPlot(sub_cell,group.by =paste0('Epiblast_res_',my_resolution))
```

![](../../images/6dd77e870220b8ab.webp)

### **2 可视化**
```r
# 计算这些marker的差异基因，注意此处不能用所有大群的细胞类型参与差异计算，否则亚群间的特征marker可能无法观察到。
all_mk <-FindAllMarkers(sub_cell,
group.by =paste0('Epiblast_res_',my_resolution))
```
```
## Calculating cluster Epiblast_0
```
```
## Calculating cluster Epiblast_2
```
```
## Calculating cluster Epiblast_1
```
```
## Calculating cluster Epiblast_3
```
```r
library(dplyr)
```
```
##
## Attaching package: 'dplyr'
```
```
## The following objects are masked from 'package:stats':
##
##     filter, lag
```
```
## The following objects are masked from 'package:base':
##
##     intersect, setdiff, setequal, union
```
```r
# 筛选每个亚群的top5 marker
top_mk <- all_mk %>%group_by(cluster) %>%top_n(wt = avg_log2FC, n =5) %>%pull(gene)

# 气泡图展示marker Gene
DotPlot(sub_cell,
        top_mk,group.by =paste0('Epiblast_res_',my_resolution),
scale.by ='size')+
theme( axis.text.x.bottom =element_text(angle =45,hjust =1,vjust =1))
```
```
## Warning: Scaling data with a low number of groups may produce misleading
## results
```

`![](../../images/70aa5b99f2dec03b.webp)`

**
**
```r
# 经过marker查阅后，大家可以重命名亚群：
sub_cell$Epi_sub<-recode(sub_cell$Epiblast_res_0.3,
"Epiblast_0"='Sub_1',
"Epiblast_2"='Sub_2',
"Epiblast_1"='Sub_3',
"Epiblast_3"='Sub_4'
                           )

p2 <-DimPlot(sub_cell,group.by ='Epi_sub')
p2
```

###

![](../../images/c504e76a128434fb.webp)

### 利用此前学过的[pathwork](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532754&idx=1&sn=7b9e196e20de37fd08bf24ca46cd9a82&scene=21#wechat_redirect>)，我们还可以把这个亚群分析内容贴回主图：
```r
library(patchwork)
p1 +inset_element(p2, left =0, bottom =0.7, right =0.3, top =1)
```

![](../../images/3b67c107f6228a56.webp)

## **3 循环探索亚群**

当然，大多数真实情况下，大家不一定选择一次分辨率就可以获得理想的、marker gene表达清晰的亚群。相信大家从上面的代码也可以看出，我写了一些中间变量，就是为了循环做准备。
```r
dim_list <-list()
dot_list <-list()

for (my_resolution inseq(0.1,0.9,0.2)) { # 以0.1至0.9分辨率，0.2为步长，利用这些分辨率进行亚群分析
scRNA <-FindSubCluster(scRNA,# 原来的Seurat对象
resolution = my_resolution , # 指定分亚群的分辨率
graph.name ='RNA_snn',# 聚类算法中的graph名称，可以在scRNA@graphs找，一般为"RNA_nn"与"RNA_snn"，nn = Nearest Neighbors（最近邻，无权重），snn = Shared Nearest Neighbors（共享最近邻，有权重，更适合亚群精细拆分）
cluster ='Epiblast',# 想要分压群的细胞类型
subcluster.name =paste0('Epiblast_res_',my_resolution)# 存储亚群信息的slot
                        )

# 降维展示包含大群细胞的亚群，可以看到Epiblast被分为了0-3这4个亚群：
DimPlot(scRNA,group.by =paste0('Epiblast_res_',my_resolution))
# 单独展示这部分亚群：
sub_cell <- scRNA[,grep('^Epiblast_',scRNA$Epiblast_res_0.3)]
temp_dim <-DimPlot(sub_cell,group.by =paste0('Epiblast_res_',my_resolution))
dim_list[[paste0('res_',my_resolution)]] <- temp_dim

# 计算这些marker的差异基因，注意此处不能用所有大群的细胞类型参与差异计算，否则亚群间的特征marker可能无法观察到。
all_mk <-FindAllMarkers(sub_cell,
group.by =paste0('Epiblast_res_',my_resolution))
library(dplyr)
# 筛选每个亚群的top5 marker
top_mk <- all_mk %>%group_by(cluster) %>%top_n(wt = avg_log2FC, n =5) %>%pull(gene)

# 气泡图展示marker Gene
temp_dot <-DotPlot(sub_cell,
        top_mk,group.by =paste0('Epiblast_res_',my_resolution),
scale.by ='size')+
theme( axis.text.x.bottom =element_text(angle =45,hjust =1,vjust =1))
dot_list[[paste0('res_',my_resolution)]] <- temp_dot
}
```

###

```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 211402
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.9271
## Number of communities: 2
## Elapsed time: 0 seconds
```
```
## Calculating cluster Epiblast_1
```
```
## Calculating cluster Epiblast_0
```
```
## Warning: Scaling data with a low number of groups may produce misleading
## results
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 211402
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.8398
## Number of communities: 4
## Elapsed time: 0 seconds
```
```
## Calculating cluster Epiblast_0
```
```
## Calculating cluster Epiblast_2
```
```
## Calculating cluster Epiblast_1
```
```
## Calculating cluster Epiblast_3
```
```
## Warning: Scaling data with a low number of groups may produce misleading
## results
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 211402
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.7999
## Number of communities: 7
## Elapsed time: 0 seconds
```
```
## Calculating cluster Epiblast_4
```
```
## Calculating cluster Epiblast_2
```
```
## Calculating cluster Epiblast_1
```
```
## Calculating cluster Epiblast_0
```
```
## Calculating cluster Epiblast_3
```
```
## Calculating cluster Epiblast_5
```
```
## Calculating cluster Epiblast_6
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 211402
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.7669
## Number of communities: 8
## Elapsed time: 0 seconds
```
```
## Calculating cluster Epiblast_3
```
```
## Calculating cluster Epiblast_2
```
```
## Calculating cluster Epiblast_0
```
```
## Calculating cluster Epiblast_1
```
```
## Calculating cluster Epiblast_5
```
```
## Calculating cluster Epiblast_6
```
```
## Calculating cluster Epiblast_4
```
```
## Calculating cluster Epiblast_7
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 211402
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.7381
## Number of communities: 10
## Elapsed time: 0 seconds
```
```
## Calculating cluster Epiblast_2
```
```
## Calculating cluster Epiblast_0
```
```
## Calculating cluster Epiblast_5
```
```
## Calculating cluster Epiblast_1
```
```
## Calculating cluster Epiblast_3
```
```
## Calculating cluster Epiblast_9
```
```
## Calculating cluster Epiblast_6
```
```
## Calculating cluster Epiblast_7
```
```
## Calculating cluster Epiblast_4
```
```
## Calculating cluster Epiblast_8
```
```
CombinePlots(dim_list)
```
```
## Warning in CombinePlots(dim_list): CombinePlots is being deprecated. Plots
## should now be combined using the patchwork system.
```

![](../../images/8e0cecedcf1140f2.webp)
```
CombinePlots(dot_list)
```
```
## Warning in CombinePlots(dot_list): CombinePlots is being deprecated. Plots## should now be combined using the patchwork system.
```

![](../../images/86bdfd0377aafd5e.webp)

**三、取子集重新聚类分群**

相比`FindSubCluster()`，我们可以将对应细胞类型通过`subset`等方式取子集，重新run一遍[基础流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&payreadticket=HO1-0kRJymfAw-HyM-Ee4mrDLTZWEacMUg1o_tPw9EtOS1gxw_gxyHeq2PYobNjDEoBbhhg&scene=21#wechat_redirect>)。
```r
sub_cell <- scRNA[,scRNA$celltype =='Epiblast']
DimPlot(sub_cell)
```

![](../../images/f3246069c56b96e0.webp)
```r
# normalization是每个细胞单独执行的，不需要做了
# FindVariableFeatures需要重新做一下，子集的高变基因与大群的高变基因会存在一定差别.由于细胞数量的减少，高变基因数量也应该随之降低，变异系数较低的基因保留反而会给下游分析引入“噪声”。
sub_cell <-FindVariableFeatures(sub_cell, selection.method ="vst", nfeatures =2000)
sub_cell <-ScaleData(sub_cell, features =VariableFeatures(sub_cell))
```
```
## Centering and scaling data matrix
```
```r
sub_cell <-RunPCA(sub_cell, features =VariableFeatures(object = scRNA))
```
```
## Warning in PrepDR(object = object, features = features, verbose = verbose): The
## following 1063 features requested have not been scaled (running reduction
## without them): Srgn, Cck, Gsto1, Serpinh1, Anxa1, Fth1, Cdh5, Lgals3, Lama1,
## Afp, Lgmn, Elf5, Igfbp1, Cyba, Lgals1, Arpc1b, Gjb3, Spin2c, Ctsb, Pmp22, Cd63,
## Sfn, Krt19, Ddah1, Ctsc, Foxq1, Kdelr3, Fgfbp1, Esam, Apoa2, Nup62cl, S100a6,
## Spp2, Cubn, Cotl1, P4ha2, Apob, Bmp4, S100a1, F3, Anxa5, Aqp3, Ctsz, Cd9, Gjb5,
## 2610528J11Rik, Lamc1, Zfp42, Rtp4, Rnf128, Wnt6, Bex3, Htra1, Serpinb6b, Procr,
## Tmem150a, Fgb, Adora2b, Cdx4, Nppb, Wfdc1, Pcbd1, Vamp8, Lamb1, Duoxa2, Rhox9,
## Slc2a2, Sct, Selenop, Car4, Ptger3, Scin, Grem2, Cd8a, S100a11, Pilra, Hes7,
## Trf, Lrpap1, Amot, Hoxb2, Prss50, Plaur, Slc16a1, Fthl17a, Gm9, Nid1, Gipc2,
## Ripply2, Lect2, Gpc4, Fgg, Clic6, Emb, Xlr3c, Tmem114, Prss12, Creb3l3, Wnt2,
## Pyy, Bcr, 3830417A13Rik, Pla2g5, Rhox6, Slc13a4, Sprr2a3, Reep6, Apoc3, Nrk,
## Bex1, Serping1, Apoc1, Hoxb6, Fosl1, Plat, Klhl6, Epas1, Igfbp3, Copz2, Slc7a8,
## Cpne3, Tacstd2, Slc39a5, Gng12, Gria1, Rbm38, Asb4, Pim2, C2cd4a, Tnnc1, Rab4a,
## Ang, Dnmt3b, Foxc2, Tagln2, Nat8l, Slc7a9, Pdzk1ip1, Pecam1, Ak8, Pitx1, Mmp9,
## Dpp4, Fn1, Cystm1, S100a16, Bambi, Shisa2, Adgrf5, Aqp11, Inpp1, Phlda1, Peg10,
## Csrp3, Agmo, Fzd5, 4732419C18Rik, Batf3, Susd3, Klhl13, Stx7, Klf5, Spn,
## Cdkn2a, Mybph, Bmp2, Oxct1, AU018091, Bmp8b, Rhox2a, Isl1, Sfmbt2, Tph1, Kdr,
## Atp6v0b, Hkdc1, F10, Hebp1, Hsd17b2, Ubash3b, Cpn1, Crh, Dnmt3l, Olfr1459,
## Hnf4a, Litaf, Ppic, Zfp600, Ptk6, Hoxd9, Ecm1, Vstm2b, Gfi1b, Gjb2, Gm29480,
## Pon1, Mageb16, Podxl, Cpa1, Rbms1, Cd24a, Gm26739, Irs3, Pglyrp1, Hoxb3os,
## Cracr2b, Serpinb6c, Arid3c, Ihh, Dnajc22, Plut, Tsga8, Hoxd1, Akr1c12, Plod2,
## St8sia1, Mbl2, Gata1, Dll1, Ccnd3, Psph, Dnajb13, Mpc2, Cd55, Apoc2, Snrpn,
## Wfdc2, Sec14l2, Slc22a2, Ly6a, 1700018B24Rik, Cideb, Cldn2, Serpinb9, Tbx6,
## Snx29, Slc40a1, Lncenc1, Bex4, Vil1, Tmprss2, Trim10, Sigirr, 1700011H14Rik,
## Fcgrt, Rgs8, Ifi27l2b, Hnf1b, Syngr1, Rhox2g, Gprc5a, Mpzl2, Mgst3, Tmem252,
## Nkx2-5, Cfi, Chst7, Hoxb5, Akr1c19, Timd2, Chst15, Dkkl1, Slc41a2, Aldh1a1,
## Gm11789, Anxa3, Chrna9, Tceal8, Blvra, F2, Serpinb9b, Gfra3, Esrrb, Pqlc2,
## Akr1c21, Ermn, Sgce, Fasl, Tex101, Leap2, Gsn, Dok4, Tceal9, Gata3, F11r,
## Serpinf2, Ezr, Calb2, Socs3, Igsf23, Krt23, Lmo4, Lrp2, Tubb6, Pcdh19,
## 9530034E10Rik, Halr1, Aspdh, Fabp2, Frk, Fgfr2, Nlrx1, Rhbg, Rpp21, Gramd1b,
## Stard8, Ftl1, Prap1, Efnb1, Syt8, Casz1, Lfng, Rab17, Prss22, Dusp14, Cmklr1,
## Zar1, Noct, Cemip, Tmem181a, Mgarp, Dpf3, Cmtm5, Nrp1, Rgs5, Cib2, Ninj1,
## Barhl2, F5, Gm15848, Cited4, Rasgrp2, Igfbp5, Prkcq, Gjb1, Ier3, Zcchc12,
## Klrg1, Samsn1, Stmn1, Prdm6, Rhoj, Jaml, Tnfsf12, Lsp1, Col1a1, Aass,
## 2200002D01Rik, Enkur, Vax1, Myl1, Smarcd3, Eif4ebp1, Prss35, Arl14epl, Cfap52,
## Cpm, Vkorc1, Cpne2, Tgfb1, Optc, Spon2, Pdzd3, Hmces, Saa3, Lgals9, Npy,
## Tex13b, Fstl3, Clta, Gal, Lgals3bp, Abcc2, Ly6k, Gata4, Lrrc19, Ly6g6e,
## 2900052N01Rik, Bhmt2, Runx1, Ins2, Trpc5os, Vnn1, Mlph, B3gnt3, Apobec2,
## Cfap126, Ankrd33b, Epcam, Ube2l6, Parm1, Vtn, Hapln4, Stra6, Ppp1r18, Slc39a4,
## Susd1, Atp8a1, Mybl2, Tead4, Exoc3l4, Pcsk6, Gm5868, Cd82, Fam124a, Nupr1,
## Stx11, Fbxo2, Tbx18, Slc34a3, Higd1a, Tmem119, Nptxr, 4833427G06Rik, Inpp5j,
## Adh7, Cd200, Fgf10, AC131677.1, Sord, Gm1070, Als2cr12, Sox21, Ifitm2, Fzd8,
## Ptma, Adrb3, Hoxa1, Erich4, Kcne1, Matn4, Apoa5, Tekt2, Tfeb, Stard10, Ccdc141,
## Gm5771, Zfp977, Scmh1, Slc9a3r1, Nod2, Col23a1, Ifi27, Lcp1, Isg15, Fcer1g,
## Eps8l2, Igfbp4, Tmed6, Wnt3a, Hoxa10, Fcgr3, Gm13203, Dcaf12l1, Rdh10, Bace2,
## Erich2, Mkrn1, Col9a1, Bmper, Npm1, Ptprtos, Pax2, Sowahb, Gas6, Spats1,
## Cfap45, Liph, BC025446, Gm14168, Dnah9, Gp1bb, Cd300a, Rab3il1, Pkm, Bves,
## Mtus2, Satb2, Pdx1, Tmem27, Phactr1, Foxa3, Mras, Lipg, Prss44, BC048679,
## Mlana, Mkrn2os, Slc25a45, Fbxo15, Ppfibp2, Proc, Zfpm1, Sod3, Cltb, Dgat2,
## Dram1, Pqlc1, Gabarapl1, Il15, Tulp2, Mpped2, Eml1, Abca3, Six2, Foxa1, Prodh2,
## Maf, Gm11992, A530084C06Rik, Tap1, Pdgfra, Tmem88, Galk1, AI464131, Gng3,
## Ptgfr, St6galnac5, Rflna, Iffo2, Gm36028, Fam189a2, Vgll1, Tha1, Thnsl2, Aim1,
## Tmem81, 1700029I15Rik, Olig2, Sdc4, Pramef12, Fbln2, Wsb2, Smim14, S100z, Ddt,
## Mcub, Gm5622, Cdo1, Rinl, Clps, Gh, Kctd12, Gpat3, Mbnl2, Tfcp2l1, Glb1l,
## 3830403N18Rik, Pfkp, Itgb4, Bhlhe40, Ninj2, Gpr4, Tm4sf5, Zfp382, Adh6b,
## 2610206C17Rik, Serpina10, Mum1l1, Bst1, Pcgf5, Car8, Agrp, Spns2, Cmbl, Duox2,
## Cib1, Ltb4r2, F2rl1, 9230105E05Rik, Upk3a, Hs3st3b1, Abcc12, Atp9a, Mfsd1,
## Unc5c, Paqr5, Was, Il17re, Ripk3, Oxct2b, Nat8f5, Slc43a2, Itpr3, Slc35g2,
## Gatsl3, Pabpn1l, S100a13, Art5, Mbnl3, Ranbp17, Rnd1, Rftn1, Ccdc3, Tax1bp3,
## Itga7, Stat1, Fam114a1, Anxa7, Hoxb4, Lipc, Ppp1r9b, Col13a1, Twist1, Rbm24,
## Cbfa2t3, 2410141K09Rik, Fosl2, Slc5a2, Panct2, Pde6c, Igf2os, Prkch, Npffr1,
## Ccdc153, Laptm5, Eps8l3, Vsir, Fam19a4, Capn1, Rnf125, Aknaos, AC157019.2,
## Tspan13, Pnma5, Sox9, Cbln1, Foxc1, Slitrk4, Mmp12, Serpinb1a, Ifi35, Gm42835,
## Rasgrf1, Irx4, Bmp1, Notum, Il15ra, Alx1, Tex19.2, Gad1, Dusp2, Lhb, Myo5b,
## Slc29a1, Large2, Gimap1, Pnp2, Errfi1, Nfkbiz, Kcns3, Eif2s2, Cd160, Tnfrsf9,
## Gchfr, Bmp8a, Proz, Tshz2, Plcl1, Inpp5d, Acmsd, Fmod, Ddr2, Barhl1, Hoxd3,
## Angpt4, Gm14226, Gata5os, Sox18, Smpx, Zbbx, Cym, Vcam1, Palmd, Emcn, Tlr4,
## Hspb7, Lhfpl3, Pf4, Gm43050, Urad, Stra8, 5730596B20Rik, Smco3, Klk1, Gm44670,
## Il16, Slco2b1, AC153369.1, Gypa, Hp, Slc38a8, Slc22a14, Pik3r6, Slfn14, Abca9,
## Gm29590, Lrrn3, AC154863.1, Abra, Tg, Gml2, Csf2rb2, Hoxc11, Hcls1, Chodl, Erg,
## Cyp1b1, Sh3rf2, Gm20467, Socs2, Tpcn1, Tmem140, Klhl3, Fbxo6, Crip2, Creb3l1,
## Nccrp1, Gm14419, Fbxo21, Gm13056, Lgi4, Serpina1b, Lef1, Sox4, Islr2, Elf1,
## Hk1, Irf2, Metrnl, 4833407H14Rik, Scn1b, Plagl1, Anxa4, Aprt, Gramd2, Daam2,
## Tfap2b, Gm28723, Klhl30, 9430024E24Rik, 5031425F14Rik, Naaladl2, Mpl, Cav1,
## Hoxa9, 4930429H19Rik, Fsd2, Sox6os, Myct1, Gm15221, Dgkh, Nme9, Osbp2, Gm11985,
## Unc45b, Prr29, Gng4, 1700018A04Rik, Krt5, Cfap44, Gm29418, Scgb3a2, Ppp1r32,
## AW112010, Arhgap31, Mettl25, Nrg2, Cygb, Gm45802, Ptpre, Rnf224, Kctd14, Ppm1j,
## G430049J08Rik, Gamt, Ceacam10, Gng11, Myzap, Htr5b, Hnf1aos1, Pparg, Slc25a43,
## 0610040J01Rik, Tmem125, Tnni1, Slc44a4, Cd47, Triml2, AC147634.1, Slc24a3,
## Glt28d2, Gm16230, Gm28727, Prss8, Bglap3, Ltc4s, Pcdh18, Gjd2, Fam43b, Bend7,
## Epha4, Plk3, Slc22a18, Sdk1, Tuba3b, 6030419C18Rik, Dynlrb2, 2700046A07Rik,
## Anks1b, Atrx, Bok, Cnbd2, Susd5, Them7, Tmem25, Cyp2d26, Nfam1, As3mt, Pdzd2,
## Gpc5, Flt1, Hsf4, Tbr1, Susd2, Ackr3, Tceal3, Rbpms2, Gm16136, Cmtm7, Gm14295,
## Mobp, Slc30a2, Icam1, Col27a1, Tac1, Cd46, Tll1, Gpr20, Zmynd10, Plec, Adam8,
## Atp8b2, Gm10332, Eps8, Pllp, Gnb4, Tgm2, Arhgap18, Habp2, Ttc9, Tenm4, Ly96,
## Scx, 4930444M15Rik, Gbx2, Mfsd4b3, Cdc42ep3, Marc1, Mustn1, Spef2, Cpa6, Lmx1a,
## Dlx1, Hoxd8, Gm826, Prdm13, Palm2, Dmbx1, Pla2g2d, Crybb1, Grifin, Cpa5, Hoxa4,
## Dnah6, Clec4f, Arhgap25, Gm44210, Lmod3, Olfr539, Kcnq1, AC155709.2, Stab2,
## Ascl1, Lyz2, Fezf2, Mbl1, Gm26563, Gpr179, Slc6a18, Gzmk, Msgn1, Lst1, Fhl2,
## Prrx2, Vegfc, Tnfsf9, Muc1, Nkx2-9, Gltpd2, Gucy1b3, Phf19, Sccpdh, Slc23a1,
## Prdm1, Synpo2l, Tlx2, AC122326.1, Ccdc152, Emp2, AC132085.1, Opcml, Cdh17,
## 9130204K15Rik, AC241534.3, Fancd2os, Slco4c1, Zdhhc9, Pdzrn4, Spats2l, Stat3,
## Pdcd6, Nr4a1, 8030474K03Rik, Acad10, Stk32a, Rbm20, Ppp1r16b, Bhlhe22, Smim6,
## Sec16b, Lacc1, P3h2, Tnfaip8l1, Nr4a2, Adam19, Nrp2, Haao, Fam69a, Sqrdl,
## Tmem86b, Gm16702, Efna4, Slc16a9, Fank1, Rarb, AU022754, Pou4f3, Nxph4, Rin3,
## Hmcn2, Epha10, Sox6, Nfix, Fbln5, Tead3, Nat8, Mylip, Arl14, Gm6569, Dpyd,
## Mef2c, Chst2, Pon2, Man2c1os, Irak2, Pklr, Esrp2, Igfbp7, Cd37, Hsd11b2, S1pr5,
## Itpr2, Igsf5, Snai3, Eng, Plxnd1, Myo7a, Spag6, Gm14426, Gm595, Fgf16, Glra2,
## Hsd3b1, 1700013F07Rik, Hemgn, Slc5a9, Shh, Kel, 5430402O13Rik, Hoxa13, Gm44029,
## C3ar1, Pde6h, Gm10603, Lama2, 1700040L02Rik, AC160146.1, Rbp2, Il9r, Hba-x,
## Krt36, Fam20a, Slc17a4, A830082K12Rik, Tmem171, Hoxc5, BC048502, Vit, Lox,
## Redrum, Ms4a10, Pclaf, Pwwp2b, Adra2b, Rnf157, Galnt6, Sema3b, Elf3, Slc32a1,
## Chl1, Ccnd1, B4galt5, Acot4, Hoxd13, Gm8113, Tuba8, Ntn1, Cryl1, Myoz1,
## Ppp2r2b, Acp5, Gfpt2, Ddc, Rassf10, Gm8773, Adap1, Tmem40, Gng2, Naa11,
## Gm45036, Gm5784, Gm12408, Htr1d, Nol3, Prss16, AC124772.5, Efcab1, Amer3,
## CK137956, Dnali1, Fam19a1, Sv2b, Gm26884, Necab2, Krt222, Cxcr4, Ddx4, Pla1a,
## Fgf18, BC049762, Phf11d, Apoc4
```
```
## PC_ 1
## Positive:  Tuba1b, Gapdh, Hspa8, Atp5b, Tubb5, Eef1a1, Eif4a1, Slc25a5, Hsp90aa1, Actg1
##     Eno1, Tubb4b, Hsp90ab1, Pgk1, Slc7a3, Tuba1a, Actb, Ldha, Ubc, Utf1
##     Pou5f1, Tuba1c, Ctsl, Slc2a1, Fdps, Cldn6, Gsta4, Uchl1, Hist1h2ap, Igfbp2
## Negative:  mt-Nd1, Fgf8, Fst, Eomes, Tdgf1, mt-Co2, Ccnd2, Sp5, Npm3, Rpl22l1
##     Pdgfa, Xist, Evx1, Uqcrb, Grrp1, Nkd1, Wnt3, Evx1os, Id1, Cxx1b
##     T, Nefl, Id2, Prdx1, Cxcl12, Gpx4, Frzb, Msx1, Cfc1, Rpl39
## PC_ 2
## Positive:  mt-Nd1, mt-Cytb, Utf1, Pou3f1, Mt1, Dppa5a, Prdx1, Mt2, Rpl39, Xist
##     mt-Co2, Dppa4, Pmaip1, Otx2, Dppa2, Pla2g1b, Erdr1, Cebpb, Cthrc1, Cdk2ap1
##     Smagp, Plac8, Fgf4, Rpl22l1, Gm13075, Zfp987, Cyct, Slc35d3, Loxl2, Fkbp6
## Negative:  Ldha, Fst, Eomes, Nefl, Fgf8, Ccnd2, Npm3, Gapdh, Sp5, Cxx1b
##     Actb, Fabp5, Wnt3, Hsp90ab1, Trh, Nkd1, Grrp1, Tuba1a, Ldhb, Tdh
##     Atp5b, Pdgfa, Tdgf1, Eno1, Id1, Msx1, Evx1, T, Msx2, Actg1
## PC_ 3
## Positive:  Dppa5a, Pgk1, Tdgf1, mt-Cytb, Fgf8, Mt1, Mt2, Dppa4, Id2, Id1
##     Eif4a1, Eef1a1, Pla2g1b, Pitx2, Basp1, Nefl, Smad7, Pim1, Hes1, Cyr61
##     Cxcl12, Sgk1, Dppa2, Hist1h2ap, Gdf3, Olig1, Wnt3, Nodal, Slc25a5, Eomes
## Negative:  Tuba1a, Fabp5, Utf1, Stmn2, Trh, Ldhb, H1f0, Ldha, Chst1, Fdps
##     Ebf1, Tubb3, Slc7a3, Penk, Grp, Trap1a, Smagp, Stmn4, Gpx3, Asns
##     Uqcrb, Malat1, Lypd6b, Krt7, Msmo1, Lhfp, Slc35d3, Atp5b, Chac1, Rpl22l1
## PC_ 4
## Positive:  Id1, Id2, Id3, Msx1, Msx2, Ckb, Cxcl12, Ccnd2, Irx3, Dlx5
##     Id4, Hand1, Cdx2, Cdkn1a, Evx1, Phlda2, Vsx1, Prdx1, Lor, Phlda3
##     Efna1, Krt18, Evx1os, Fabp5, Cebpb, Crabp2, Cox4i2, Irx5, Nkd1, Pdgfa
## Negative:  Fgf8, Fgf5, Tdgf1, Npm3, Trh, Ube2c, Car2, Sgk1, Ccnb1, Psors1c2
##     Meg3, Foxa2, Upp1, Nefl, Eomes, Aurka, Xist, Ldhb, Igfbp2, Malat1
##     Kpna2, Gsc, Pou3f1, Apela, Lefty1, H1f0, Hes1, Ndrg1, Fst, Slc7a7
## PC_ 5
## Positive:  Ube2c, Aurka, Ccnb1, Meg3, Pou3f1, Kpna2, Malat1, Xist, Id3, Id1
##     Ubc, Sparc, Sox2, Id2, Smad7, Msx2, H1f0, Cdk2ap1, Basp1, Utf1
##     Cfc1, Chst1, Tuba1c, Erdr1, Crabp2, Id4, Fermt1, Ccnd2, Dusp9, Dlx5
## Negative:  Prdx1, Uqcrb, Rpl22l1, Rpl39, mt-Co2, mt-Nd1, Pmaip1, Hspa8, Trh, Cebpb
##     Actg1, Eif4a1, Fst, Ldhb, Oat, Tdh, Eif2s3y, Eomes, Ctsl, Atp5b
##     Car2, Tubb3, Nefl, Eno1, mt-Cytb, Phlda3, Hist4h4, Baz1a, Tubb5, Msmo1
```
```
ElbowPlot(sub_cell)
```

![](../../images/296fb0a9e284b90e.png)
```r
sub_cell <-FindNeighbors(sub_cell, dims =1:20)
```
```
## Computing nearest neighbor graph
```
```
## Computing SNN
```
```r
# 可以看到，同样是0.3的分辨率，此时我们直接获得了5个cluster
sub_cell <-FindClusters(sub_cell, resolution =0.3)
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 5625
## Number of edges: 202858
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.8342
## Number of communities: 6
## Elapsed time: 0 seconds
```
```r
# 看一下与大群形状一致的降维：
ori_dim <-DimPlot(sub_cell)
ori_dim
```

![](../../images/dc3da6ace829af51.webp)

```r
# 觉得降维分的不够开，可以重新Run一下，但是形状会与大群中的不同哦：
sub_cell <-RunTSNE(sub_cell, dims =1:20)
re_dim <-DimPlot(sub_cell, reduction ="tsne")
re_dim
```

![](../../images/0a73b708be38dfb0.webp)
```r
# 计算marker gene
sub_cell.markers <-FindAllMarkers(sub_cell, only.pos =TRUE, min.pct =0.25, logfc.threshold =0.25)
```
```
## Calculating cluster 0
```
```
## Calculating cluster 1
```
```
## Calculating cluster 2
```
```
## Calculating cluster 3
```
```
## Calculating cluster 4
```
```
## Calculating cluster 5
```
```r
if(!require(dplyr))install.packages("dplyr")
# 筛选每个cluster中marker的Top5
top_mk <- sub_cell.markers %>%group_by(cluster) %>%top_n(n =5, wt = avg_log2FC)

# 展示marker Gene：
DotPlot(sub_cell,
        top_mk$gene,
scale.by ='size')+
theme( axis.text.x.bottom =element_text(angle =45,hjust =1,vjust =1))
```

![](../../images/bc4458f52b033a87.webp)可以明显发现，两种亚群分析方式获得的效果是不同的，至于如何选择，就要看大家手里的数据特征啦~

**四、资料领取**

一切不给测试文件和分析环境版本的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：![](../../images/2bad3ed0864fc986.jpg)

链接: https://pan.baidu.com/s/1xv2SC7Sa6S2fv7r2YFXvLw

提取码：fyxv

![](../../images/2080bcc495becfbe.webp)
![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
