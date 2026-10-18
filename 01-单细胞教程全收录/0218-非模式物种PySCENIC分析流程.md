---
title: "非模式物种PySCENIC分析流程"
date: 2025-04-11
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528411&idx=1&sn=efa4ace804c343379073dea63de64b4e&chksm=9b3c168bac4b9f9d6809de7c7aea255d92db3f9f9d333532cc09817f2604974ee5a1478ee40f#rd
albums: ["单细胞教程全收录"]
---

# 非模式物种PySCENIC分析流程

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528411&idx=1&sn=efa4ace804c343379073dea63de64b4e&chksm=9b3c168bac4b9f9d6809de7c7aea255d92db3f9f9d333532cc09817f2604974ee5a1478ee40f#rd
> 合集：单细胞教程全收录

**一、写在前面**

目前pyscenic分析支持的物种仅为人、小鼠和果蝇，其他物种暂时还没有相应的数据库，因此无法直接分析。如果是这三个物种之外的物种想要做scenic分析的话, 可以使用同源基因转换后再进行分析, 将要分析的物种的gene Symbol转换为人、小鼠或者是果蝇的gene Symbol后进行分析。

例如我们有一个Pelodiscus sinensis（中华鳖）的基因-细胞的矩阵，进行pyscenic分析的话，可参考以下示例。

本文分析集锦：

![](../../images/3f4f02bded857a70.webp)

关于SCENIC我们做过一系列图文及视频教程：

**SCENIC转录因子分析 ：****[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|3.软件安装与数据准备](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|5.step1+step2构建共表达网络与regulon](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501692&idx=1&sn=3f7e263a93942ad03faa1ba5f8694ec4&chksm=9b3cbe2cac4b373af9db74a50ffb08a9b8a3b958fc6385c937385f0f7323bc935cdb0fe5275c&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|6.Step3 利用AUCell对Regulon评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501989&idx=1&sn=2700bf779d7d261a4d751d1635fdce2c&chksm=9b3cb1f5ac4b38e3014476242fe956cf510cc45b9f4cef86070af8094fd5f884f9d5c3a3363f&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|7.Step4 二元矩阵的计算与可视化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503995&idx=1&sn=26c7e9ec56af434e62b02853cfe667d6&chksm=9b3ca92bac4b203d7986645ab5a3fb574f44185c7ced8bd47957fa237d436a95bfa2579d052a&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|8.Step5 regulon聚类、分群、降维](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504024&idx=1&sn=143c0ec4d94b8fca0a4a47d3dc24415b&chksm=9b3ca9c8ac4b20de70a87acb2d3f810b0e1497071b1c6f14f1882a6d844fff016e9ba5581eb3&scene=21#wechat_redirect>)****[SCENIC单细胞转录因子预测|9.下游探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505276&idx=1&sn=949c753feb85d5877121433caaa33013&chksm=9b3cac2cac4b253affb587a937d3f5e0576851a4f4e1570cb7510a594d155873961bbd91758d&scene=21#wechat_redirect>)****[SCENIC转录因子调控网络图](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520750&idx=1&sn=496bead1531a7eddd5c286030d350745&chksm=9b3ce8beac4b61a8589a1f8a66bd0571e09c0646655b6d805348bf6f4a0c7b52851615c22868&scene=21#wechat_redirect>)****[比R版本快几十倍| Pyscenic单细胞转录因子预测](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528198&idx=1&sn=2bdac420c143423d8a7012d028473573&scene=21#wechat_redirect>)**

**二、软件安装**

本教程基于Linux及服务器中的Rstudio环境（[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526504&idx=2&sn=417d07347cebe0a1bd403f6c3e7d9b29&scene=21#wechat_redirect>)）演示，计算资源不足的同学可参考：
[生信分析为什么要使用服务器？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491007&idx=1&sn=8619c2bad23791b3252a1c4cb1831931&chksm=9b3f64efac48edf9c02f84959aeee9b12480736fce70c5ddb8b41d79cfc22ce590ea2cb60fba&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[配置一个心仪的工作站(硬件+环境配置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519707&idx=1&sn=73dcab26f9b2ed75a954327317d07112&chksm=9b3cf48bac4b7d9df5b5a432fbe70d4f9c13bc8d739aa401732614f022223d1912642a7e4bea&scene=21#wechat_redirect>)
[
](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)[独享服务器半价活动~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528318&idx=1&sn=a58d8147203f10750d3723a3120ea305&scene=21#wechat_redirect>)
[
](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

更多内容可咨询客服微信[**Biomamba_yunying**]

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# pyscenic环境创建流程conda env remove --name pyscenicconda create -n pyscenic python=3.8.1conda activate pyscenic# !!!!!按照下面的顺序安装，不然可能出现彼此不兼容的报错# 参考：https://www.jianshu.com/p/dc7397fda327pip install numpy==1.19.5pip install pandas==1.3.5pip install numba==0.56.4pip install pyscenic==0.12.1# 检查安装软件版本python -c "import numpy; print(numpy.__version__)"python -c "import pandas; print(pandas.__version__)"python -c "import pyscenic; print(pyscenic.__version__)"pyscenic -hcd /home/biomamba/project/09_pyscenic/data# 下载motif排序文件，motif 注释文件和转录因子文件# 以人类基因组hg19版本为参考，转录起始位点（TSS）上下游5kb区域的基因与基序（motifs）的排名数据，数据整合7个物种信息用于评估基因与基序结合可能性，确定转录因子和靶基因间调控关系wget https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg19/refseq_r45/mc9nr/gene_based/hg19-tss-centered-5kb-7species.mc9nr.genes_vs_motifs.rankings.feather# 基序到转录因子的映射关系，通过分析转录因子结合位点基序，识别可能结合特定基序的转录因子。wget https://resources.aertslab.org/cistarget/motif2tf/motifs-v10nr_clust-nr.hgnc-m0.001-o0.0.tbl# 人类基因组中所有转录因子列表wget  https://resources.aertslab.org/cistarget/tf_lists/allTFs_hg38.txt
```

**三、中华鳖PySCENIC分析流程**

##  1、表达矩阵准备

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# Pelodiscus sinensis（中华鳖）的表达矩阵创建seurat对象dir <- list.files("/home/biomamba/project/08_depth_compar/data/BMK/")[7:8]names(dir) <- c("CgS1","CgS2","GgS1","GgS2","HsS1","HsS2","PsS1","PsS2","PfS1","PfS2","RnS1","RnS2","SsS1","SsS2")[7:8]dirobj_list <- list()for(i in 1:length(dir)){  counts <- Read10X(paste0("/home/biomamba/project/08_depth_compar/data/BMK/",dir[i],"/filtered_feature_bc_matrix"))  obj_list[[i]] <- CreateSeuratObject(counts,project = names(dir)[i],min.cells=0,min.features=0)}obj_listobj_Ps <- merge(x=obj_list[[1]],y=obj_list[-1])obj_Ps <- JoinLayers(obj_Ps)obj_Ps obj_Ps [["percent.mt"]] <-PercentageFeatureSet(obj_Ps , pattern = "^mt[-\\.]")obj_Ps <- subset(obj_Ps, subset = nFeature_RNA > 200 & nFeature_RNA < 5000 & percent.mt < 30)obj_Ps<- obj_Ps %>%  NormalizeData() %>%  FindVariableFeatures() %>%  ScaleData() %>% RunPCA() %>%  FindNeighbors() %>%  FindClusters(resolution = 1.0) %>%  RunTSNE(dims = 1:10) %>%  RunUMAP(dims = 1:10)#saveRDS(obj_Ps,"/home/biomamba/project/09_pyscenic/result/obj_Ps.rds")#obj_Ps_sub <- subset(obj_Ps,downsample=30)#saveRDS(obj_Ps_sub,"/home/biomamba/project/09_pyscenic/result/obj_Ps_sub.rds")
```

## 2、同源基因转换

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# Pelodiscus sinensis（中华鳖）和人的基因ID同源转换# 查看可以用的数据库（这一步可能受到网络影响而提示"timed out"，如果失败了可以多尝试几次）all_mart <- useMart("ensembl")head(listDatasets(all_mart))# 连接人类基因数据库（这一步可能受到网络影响而提示"timed out"，如果失败了可以多尝试几次）human_mart <- useMart("ensembl", dataset = "hsapiens_gene_ensembl")# 提取中华鳖基因IDpsinensis_gene_symbols <- rownames(obj_Ps_sub)# 保存基因表达矩阵的其他列名（除基因符号列）#other_column_names <- setdiff(colnames(gene_expression_matrix), "Symbol_Gene")# 查询中华鳖基因符号对应的人类基因符号head(listAttributes(human_mart))homo_gene <- getBM(attributes = c("hgnc_symbol","ensembl_gene_id","external_gene_name"),                      filters = "external_gene_name",                       values = psinensis_gene_symbols,                      mart = human_mart)obj_Ps_sub <-subset(obj_Ps_sub, features = homo_gene$hgnc_symbol)obj_Ps_subcounts_Ps <- as.matrix(obj_Ps_sub@assays$RNA@layers$counts)colnames(counts_Ps) <- colnames(obj_Ps_sub)rownames(counts_Ps) <- rownames(obj_Ps_sub)#write.csv(counts_Ps,file = "/home/biomamba/project/09_pyscenic/result/counts_Ps.csv")
```

## 3、loom文件准备

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# loom文件准备import os,sysimport loompy as lpimport numpy as npimport pandas as pdos.getcwd()os.listdir(os.getcwd())counts=pd.read_csv("/home/biomamba/project/09_pyscenic/result/counts_Ps.csv",index_col = 0, header = 0)features = counts.index.tolist()barcodes = counts.columns.tolist()#loom行属性：用于存储与基因相关的元数据。这些属性可以包括基因名称、基因长度、基因所属的染色体等信息。#loom列属性：存储与细胞相关的元数据。例如细胞类型、细胞来源、细胞所处的发育阶段等信息。row_attrs = {'Gene':np.array(features)}col_attrs = {'CellID':np.array(barcodes)}lp.create("/home/biomamba/project/09_pyscenic/result/counts_Ps.loom", counts.values,row_attrs,col_attrs)
```

## 4、pyscenic分析

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 第一步 grn (耗时：2.5h)pyscenic grn \  --num_workers 15 \  --output /home/biomamba/project/09_pyscenic/result/grn_Ps_output.tsv \  --method grnboost2 \  /home/biomamba/project/09_pyscenic/result/counts_Ps.loom \  /home/biomamba/project/09_pyscenic/data/allTFs_hg38.txt# 如果出现Could not find data: {'ndarray-922cb62afe37c1431b930b4a03c73f34': ['tcp://127.0.0.1:38175']} on workers"类似这样的提示，可能是服务器端口被占用，可以用以下命令替换，参考https://pyscenic.readthedocs.io/en/latest/faq.htmlpython /home/biomamba/miniconda3/envs/pyscenic/bin/arboreto_with_multiprocessing.py \  --num_workers 15 \  --output /home/biomamba/project/09_pyscenic/result/grn_Ps_output.tsv \  --method grnboost2 \  /home/biomamba/project/09_pyscenic/result/counts_Ps.loom \  /home/biomamba/project/09_pyscenic/data/allTFs_hg38.txt#  第二步 ctx (耗时：40min)pyscenic ctx \  /home/biomamba/project/09_pyscenic/result/grn_Ps_output.tsv \  /home/biomamba/project/09_pyscenic/data/hg19-tss-centered-5kb-7species.mc9nr.genes_vs_motifs.rankings.feather \  --annotations_fname /home/biomamba/project/09_pyscenic/data/motifs-v10nr_clust-nr.hgnc-m0.001-o0.0.tbl \  --expression_mtx_fname /home/biomamba/project/09_pyscenic/result/counts_Ps.loom \  --mode "dask_multiprocessing" \  --output /home/biomamba/project/09_pyscenic/result/ctx_Ps.csv \  --num_workers 20 \  --mask_dropouts#  第三步 AUCellpyscenic aucell \  /home/biomamba/project/09_pyscenic/result/counts_Ps.loom \  /home/biomamba/project/09_pyscenic/result/ctx_Ps.csv \  --output /home/biomamba/project/09_pyscenic/result/aucell_Ps.loom \  --num_workers 20
```

## 5、结果可视化

  *   *   *

```r
obj_Ps <- readRDS("/home/biomamba/project/09_pyscenic/result/obj_Ps.rds")obj_Ps_sub <- readRDS("/home/biomamba/project/09_pyscenic/result/obj_Ps_sub.rds")obj_Ps_sub
```
```
## An object of class Seurat
## 12467 features across 450 samples within 1 assay
## Active assay: RNA (12467 features, 1018 variable features)
##  3 layers present: counts, data, scale.data
##  3 dimensional reductions calculated: pca, tsne, umap
```

  *

```
DimPlot(obj_Ps_sub)
```

## ![](../../images/1a56fdb45d238708.webp)

  *   *   *   *   *   *   *   *   *   *   *

```r
loom <- open_loom("./result/aucell_Ps.loom")#获取调节因子矩阵：regulons_incidMat <- get_regulons(loom, column.attr.name="Regulons")#将调节因子矩阵转换为基因列表regulons <- regulonsToGeneLists(regulons_incidMat)#获取调节因子的AUC值regulonAUC <- get_regulons_AUC(loom,column.attr.name='RegulonsAUC')#获取调节因子的阈值regulonAucThresholds <- get_regulon_thresholds(loom)sub_regulonAUC <- regulonAUC[,match(colnames(obj_Ps_sub),colnames(regulonAUC))]identical(colnames(sub_regulonAUC), colnames(obj_Ps_sub))
```
```
## [1] TRUE
```

  *   *   *   *

```
#每个细胞的aucell值添加到seurat对象的meta.data中obj_Ps_sub@meta.data = cbind(obj_Ps_sub@meta.data ,t(sub_regulonAUC@assays@data$AUC))#指定关注的转录因子绘图VlnPlot(obj_Ps_sub, features = c("ARNT(+)"),pt.size = 0)
```

## ![](../../images/42d5bc0b7a5295ac.webp)

  *

```
FeaturePlot(object = obj_Ps_sub,features = c("ARNT(+)"))
```

## ![](../../images/907356e67a5eaf8b.webp)

  *   *   *   *

```r
# regulon特异性分数(Regulon Specificity Score, RSS)rss<-calcRSS(AUC=getAUC(sub_regulonAUC),cellAnnotation=obj_Ps_sub@meta.data$RNA_snn_res.1)rssPlot <- plotRSS(rss)rssPlot$plot
```

## ![](../../images/ad2db98446fc5270.webp)

  *   *   *   *   *   *

```r
#分细胞类型展示regulon特异性分数p1 <- plotRSS_oneSet(rss,'1')p2 <- plotRSS_oneSet(rss,'2')p3 <- plotRSS_oneSet(rss,'3')p4 <- plotRSS_oneSet(rss,'4')grid.arrange(p1, p2, p3, p4, ncol = 2, nrow = 2)
```

## ![](../../images/bec7111e773839ea.webp)

  *   *   *

```r
# 热图展示每个细胞中每个转录因子的aucll分值auc <- getAUC(sub_regulonAUC)pheatmap::pheatmap(auc, show_colnames = F)
```

## ![](../../images/ddf4d3b757fcd5a5.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 热图展示每个细胞类型中部分转录因子的aucll均值auc_avg <- data.frame(t(auc))auc_avg[,"group"] <- obj_Ps_sub@meta.data$RNA_snn_res.1auc_avg <- auc_avg %>%  group_by(group) %>%  summarise_all(mean)auc_avg <- as.data.frame(auc_avg )rownames(auc_avg ) <- auc_avg$groupcolnames(auc_avg) <- c("group",rownames(auc)) #计算后+号会因为R要求变成点，重新赋予原来的名称reg <- c("ARID5A(+)","ARNT(+)","ATF1(+)","ATF2(+)","ATF3(+)","BCL6(+)","BCLAF1(+)","BHLHE40(+)","BHLHE41(+)","BPTF(+)","CEBPA(+)","CEBPB(+)","CEBPG(+)","CREB1(+)","CREB3L2(+)")auc_avg_sub <- auc_avg[,reg]rownames(auc_avg) <- factor(rownames(auc_avg) , levels = )pheatmap::pheatmap(t(auc_avg_sub), show_colnames = T, cluster_rows = F, cluster_cols = F,scale = "row")
```

## ![](../../images/0f92f071f3432c3b.webp)

**测试文件下载**

不要再说我的链接失效啦，文字识别链接容易出错，推荐微信扫码领取资料(无提取码)，真的失效了再提醒客服更换链接哦~本推送教程二维码:

通过网盘分享的文件：Py_SCENIC教程

链接:

https://pan.baidu.com/s/1S-e6-PEWV-e-a15m2661OQ?pwd=6kdf

提取码: 6kdf

![](../../images/ce9094a99d5dc72e.webp)

![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.gif) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_yunying]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/7ef00c45433a7bde.webp)![图片](../../images/acba43cb3408c3d0.gif) 您点的每个赞和在看，我都认真当成了喜欢
