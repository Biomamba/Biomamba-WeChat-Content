---
title: "代码复写|  人类乳腺癌scRNA-seq数据"
date: 2024-01-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507792&idx=2&sn=52dc1c2e5a23910ca0d8330ea917b60d&chksm=9b3ca600ac4b2f16a04624c74f2bcd3d24d300a835053a6f76ac4e1421b90c34b2ea01f1e7c8#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写|  人类乳腺癌scRNA-seq数据

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507792&idx=2&sn=52dc1c2e5a23910ca0d8330ea917b60d&chksm=9b3ca600ac4b2f16a04624c74f2bcd3d24d300a835053a6f76ac4e1421b90c34b2ea01f1e7c8#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是23号作品，复写了题为"A single-cell and spatially resolved atlas of human breast cancers"的论文。**文章链接** ：https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/34493872/**数据原始链接：** 投稿人未提供，可在文末百度云下载相关文件**文献简介** ：投稿人未提供

一、复写内容

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
---title: "breast"author: "Hao lei"date: "2023-12-16"output:  pdf_document: default  html_document: default---
```
{r setup, include=FALSE}library(Seurat)library(dplyr)library(patchwork)library(Matrix)library(ggplot2)library(tidyverse)```
```
{r}scRNA.data <- Read10X(data.dir = "F:/seqdata/work_data/Breastcancer_singlecell/breastcancer", gene.column = 1)sc2 <- CreateSeuratObject(counts = scRNA.data, min.cells = 3, min.features = 200)sc2 <- NormalizeData(sc2, normalization.method = "LogNormalize", scale.factor = 10000)sc2 <- FindVariableFeatures(sc2, selection.method = "vst", nfeatures = 2000)plot1 <- VariableFeaturePlot(sc2)top10 <- head(VariableFeatures(sc2), 10)plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)plot1 + plot2all.genes <- rownames(sc2)sc2 <- ScaleData(sc2, features = all.genes)sc2 <- RunPCA(sc2, features = VariableFeatures(object = sc2))VizDimLoadings(sc2 , dims = 1:6, reduction = "pca")DimPlot(sc2 , reduction = "pca" )DimHeatmap(sc2 , dims = 1, cells = 500, balanced = TRUE)ab=DimHeatmap(sc2, dims = 1:9, cells = 500, balanced = TRUE)ab=DimHeatmap(sc2, dims = 10:18, cells = 500, balanced = TRUE)DimHeatmap(sc2, dims = 19:27, cells = 500, balanced = TRUE)sc2 <- RunPCA(sc2, features = VariableFeatures(object = sc2))sc2 <- JackStraw(sc2, num.replicate = 100)sc2 <- ScoreJackStraw(sc2, dims = 1:20)#这里dims = 1:20表示看前20个PC的P值，因为第一次算出来的结果真的惊人。而且这个dim最大只能是20.JackStrawPlot(sc2, dims = 1:20)#用JackStrawPlot绘图，绘制前10个PC的P值分布曲线ElbowPlot(sc2)sc2 <- FindNeighbors(sc2, dims = 1:15)sc2 <- FindClusters(sc2, resolution = c(0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1))library(clustree)clustree(sc2@meta.data, prefix = "RNA_snn_res.")sc2 <- FindClusters(sc2, resolution = 0.9,label = T)sc2 <- RunUMAP(sc2, dims = 1:15)
sc2 <- RunTSNE(sc2, dims = 1:15)DimPlot(sc2, reduction = "umap",label = T,label.size = 5)DimPlot(sc2, reduction = "tsne",label = T,pt.size =1)
```
```
{r}sc2marker <- FindAllMarkers(sc2, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)sc3 <- sc2metadata <- metadata[match(colnames(sc3), metadata$barcodes), ]sc3@meta.data$celltype_minor <- metadata$celltype_minorsc3@meta.data$celltype_subset <- metadata$celltype_subsetsc3@meta.data$subtype <- metadata$subtypesc3@meta.data$celltype_major <- metadata$celltype_majorIdents(sc3) <- metadata$celltype_minorDimPlot(sc3, reduction = "umap",label = T,label.size = 5)DimPlot(sc3, reduction = "tsne",label = T,pt.size =1)```

```
{r}
a <- Cellratioa <- as.data.frame(a)
Cellratio <- prop.table(table(sc3$orig.ident, sc3$subtype), 1)#计算各组样本不同细胞群比例
colourCount = length(unique(sc3$subtype))library(ggplot2)ggplot(a) +   geom_bar(aes(x =Var1, y= Freq, fill = Var2),stat = "identity",width = 0.7,size = 0.5,colour = '#222222')+   theme_classic() +  labs(x='Cell type',y = 'Ratio')+  coord_flip()+  theme(panel.border = element_rect(fill=NA,color="black", size=0.5, linetype="solid"))
```
```
{r}DimPlot(sc3, reduction = "umap",label = T,label.size = 5,group.by = "celltype_major")``````{r}FeaturePlot(sc3, features = c("EPCAM","MKI67","CD3D","CD68","MS4A1","JCHAIN","PECAM1","PDGFRB"),raster=FALSE)```

```
{r}DimPlot(sc3, reduction = "umap",label = T,label.size = 1,group.by = "orig.ident")```

```
{r}DimPlot(sc3, reduction = "umap",label = T,label.size = 1,group.by = "subtype")```
```
{r}# 图1 f未画sc4 <- sc3unique(sc3$celltype_minor)cancer <- subset(sc3,idents = c("Cancer Her2 SC","Cancer LumB SC","Cancer Basal SC","Cancer LumA SC"))levels(cancer)cancer[['RNA']]cancermarker <- FindAllMarkers(cancer, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)top5 <- cancermarker %>% group_by(cluster) %>% top_n(n = 5, wt = avg_log2FC)library(ComplexHeatmap)mat <- GetAssayData(cancer, slot = "scale.data")cluster_info <- sort(cancer$celltype_minor)mat <- as.matrix(mat[top5$gene,names(cluster_info)])gene <- rownames(mat)gene_pos <- which(rownames(mat) %in%gene)row_anno <- rowAnnotation(gene=anno_mark(at = gene_pos,labels = gene))Heatmap(mat,        cluster_rows = F,        cluster_columns = F,        show_column_names = F,        show_row_names =F,        column_split = cluster_info,        right_annotation = row_anno)col <- c('plum','coral1','darkslategray1','darkslategray4')names(col) <- levels(cluster_info)top_anno <- HeatmapAnnotation(cluster=anno_block(gp=gpar(fill=col),                                                 labels = levels(cluster_info),                                                 labels_gp = gpar(cex=0.5,col='white')))library(circlize)library(RColorBrewer)col_fun <- colorRamp2(c(-4,0,4),c('#377EB8','white','#E41A1C'))ComplexHeatmap::Heatmap(mat,        cluster_rows = F,        cluster_columns = F,        show_column_names = F,        show_row_names = T,        column_split = cluster_info,        top_annotation = top_anno,        column_title = NULL,        right_annotation = row_anno,        heatmap_legend_param = list(          title = 'Scaled average expression',          title_position = 'leftcenter-rot'),        col = col_fun)

```

```
{r}

Cellratio <- prop.table(table(cancer$orig.ident, cancer$celltype_minor), 1)#计算各组样本不同细胞群比例a <- Cellratioa <- as.data.frame(a)colourCount = length(unique(cancer$celltype_minor))library(ggplot2)ggplot(a) +   geom_bar(aes(x =Var1, y= Freq, fill = Var2),stat = "identity",width = 0.7,size = 0.5,colour = '#222222')+   theme_classic() +  labs(x='Cell type',y = 'Ratio')+  coord_flip()+  theme(panel.border = element_rect(fill=NA,color="black", size=0.5, linetype="solid"))

```
```
{r}collapseIDs<-function(x,allids=row.names(x),method="mean"){    allids<-as.vector(allids)  ids<- levels(as.factor(allids))  x.col<- NULL    if(length(ids)==dim(x)[1]){     dimnames(x)[[1]]<-allids    return(x)   }    for(i in 1:length(ids)){    if(sum(allids==ids[i])>1){      indices <- allids==ids[i]       if(method=="mean"){        vals<-apply(x[indices,],2,mean,na.rm=T)      }      if(method=="median"){        vals<-apply(x[indices,],2,median,na.rm=T)      }      if(method=="stdev"){           temp<- x[indices,]        stdevs<- apply(temp,1,sd,na.rm=T)        vals<- temp[match(max(stdevs),stdevs),]      }      if(method=="iqr"){           temp<- x[indices,]        iqrs<- apply(temp,1,function(x){quantile(x,.75,na.rm=T)-quantile(x,.25,na.rm=T)})        vals<- temp[match(max(iqrs),iqrs),]      }      x.col <- rbind(x.col,vals)    }else{      x.col <- rbind(x.col,x[allids==ids[i],])    }  }    dimnames(x.col)<- list(ids,dimnames(x)[[2]])  return(x.col)  }

readarray<-function(dataFile,designFile=NA,hr=1,impute=T,method="mean"){    headerRows <- hr    x<-read.table(dataFile,sep="\t",header=F,fill=T,stringsAsFactors=FALSE)    if(headerRows==1){    sampleNames<-as.vector(t(x[1,-1]))    x<-x[-1,]    classes<-NULL    ids<-x[,1]    xd<-x[,-1]    xd<-apply(xd,2,as.numeric)    xd<-collapseIDs(xd,ids,method)    }else{    sampleNames<-as.vector(t(x[1,-1]))    x<-x[-1,]        classes<-x[1:(headerRows-1),]    dimnames(classes)[[1]]<-classes[,1]    classes<-classes[,-1]    classes[classes==""]<-NA    classes<-t(classes)    rownames(classes)<-sampleNames    classes<-as.data.frame(classes)        xd<-x[(-1:-(headerRows-1)),]    ids<-as.vector(t(xd[,1]))    xd<-xd[,-1]    xd<-apply(xd,2,as.numeric)    xd<-collapseIDs(xd,ids,method)  }    features<- dim(xd)[1]  samples<- dim(xd)[2]  geneNames<-rownames(xd)  xd<-apply(xd,2,as.numeric)  rownames(xd)<-geneNames  colnames(xd)<-sampleNames    if(!is.na(designFile)){    x<-read.table(designFile,sep="\t",header=T,row.names=1,fill=T,,stringsAsFactors=FALSE)    xd<-xd[,sort.list(colnames(xd))]    xd<-xd[,colnames(xd) %in% rownames(x)]    x<-x[rownames(x) %in% colnames(xd),]    x<-x[sort.list(rownames(x)),]    classes<-as.data.frame(x)  }    if(sum(apply(xd,2,is.na))>0 & impute){    library(impute)    allAnn<-dimnames(xd)    data.imputed<-impute.knn(as.matrix(xd))$data    xd<-data.imputed[1:features,]    dimnames(xd)<-allAnn  }    return(list(xd=xd, classes=classes, nfeatures=features, nsamples=samples, fnames=geneNames, snames=sampleNames))}
standardize<-function(x){  annAll<-dimnames(x)  x<-scale(x)  dimnames(x)<-annAll  return(x)}

dwd<-function(x,y){
    y<-factor(y,levels=c("1","2"))  nas<-sum(is.na(y))  if(nas>0){ print("ERROR: Class labels must be '1' and '2'")    return(NA) }    y<-as.numeric(as.vector(t(y)))    x<-rbind(y,x)    cwd<-getwd()  setwd("C:/DWD/DWDdata")  write.table(x,"DWD_Input.txt",sep="\t",col.names=F,row.names=F)    twd<-getwd()  write(twd,"fileDir.txt")    y<-0  write(y,"DWD_MeanAdjustType.txt")    setwd("C:/DWD/lib")  system("BatchAdjustSM.exe",invisible=T)    setwd("C:/DWD/DWDdata")  unlink("fileDir.txt")  unlink("DWD_MeanAdjustType.txt")  unlink("DWD_Input.txt")    setwd("C:/DWD/DWDdata")  dwdVec<-read.table("DWD_Vec.txt",sep="\t",header=F)    setwd(cwd)    return(t(dwdVec))}
medianCtr<-function(x){  annAll <- dimnames(x)  medians <- apply(x,1,median,na.rm=T)  x <- t(scale(t(x),center=medians,scale=F))  dimnames(x) <- annAll  return(x)}
overlapSets<-function(x,y){    # subset the two lists to have a commonly ordered gene list  x<-x[dimnames(x)[[1]] %in% dimnames(y)[[1]],]  y<-y[dimnames(y)[[1]] %in% dimnames(x)[[1]],]    #and sort such that thing are in the correct order  x<-x[sort.list(row.names(x)),]  y<-y[sort.list(row.names(y)),]    return(list(x=x,y=y))}

assignDiffScore.dwd<-function(x,y){  both<-overlapSets(y$xd,x$xd)   # get the overlap of genes  both$x<- apply(both$x,2,function(x){sign(x)*sqrt(x^2/sum(x^2))})   # set the distance to the origin to 1  both$y<- apply(both$y,2,function(x){sign(x)*sqrt(x^2/sum(x^2))})  # set the distance to the origin to 1  msproj<- apply(both$y,2,function(x,y){x%*%y},both$x[,1])  # project the samples on the MS-pL axis  mlproj<- apply(both$y,2,function(x,y){x%*%y},both$x[,2])  # project the samples on the pL-mL axis  diffScore<- mlproj - msproj   return( diffScore )  # return the point on the differentiation axis}```
```

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/1-3LrPfjewymOoVWddVGmDw?pwd=hq1l

提取码：hq1l

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyZQ2Fy9KbPPgaHzzInDibG1KAsAXozyLnKWKAAE91l5K5MQ5EzAibFicKRmGyRWMhxp5ctOApa8E43A/640?wx_fmt=jpeg&from=appmsg)

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
[非小细胞肺癌免疫治疗后肿瘤微环境重塑scRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507757&idx=1&sn=1045b58a64b4602881e9853d2a908012&chksm=9b3ca67dac4b2f6b4d33f10e71da2a6287968512677e77017b3820bf9aedfcd60301bb14d401&scene=21#wechat_redirect>)[colon, tumor, anti-PD-1, scRNA-seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507757&idx=2&sn=8c9c844b9b209c133e3169b66998f4c4&chksm=9b3ca67dac4b2f6b70ad9df39f55643adbe7be50f9cbb1fcdfb027625ab085104b2b66a29d9a&scene=21#wechat_redirect>)[皮质神经注释复写](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507783&idx=2&sn=d1e28f5f4bddb3a3e4f1a85db1feac7f&chksm=9b3ca617ac4b2f01b40ae6adbe48e9371e50f9df543638e8c3e8e57bf9312b5daf731041ee16&scene=21#wechat_redirect>)
[肢端黑色素瘤细胞scRNA-seq图谱&免疫治疗](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507783&idx=1&sn=6ca5dc13a6aefbe78cce3f938fe04e40&chksm=9b3ca617ac4b2f01fb6e4677668f052f6361282ff394745394d363b54ea4c1eb58d2f30da30a&scene=21#wechat_redirect>)

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
