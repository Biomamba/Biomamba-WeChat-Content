---
title: "代码复写| 人类肾脏scRNA-seq图谱"
date: 2024-01-16
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=2&sn=dec30ee34e483c3695613b3e41488a78&chksm=9b3ca77dac4b2e6b1734f1fd3d0134468b2ca8bc9f9118edc6e114a37f7ceea7dc4fa41b4556#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写| 人类肾脏scRNA-seq图谱

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507501&idx=2&sn=dec30ee34e483c3695613b3e41488a78&chksm=9b3ca77dac4b2e6b1734f1fd3d0134468b2ca8bc9f9118edc6e114a37f7ceea7dc4fa41b4556#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是14号作品。本作品复写了题为"Single-cell RNA sequencing of human kidney"的论文.**文章链接** ：https://www.nature.com/articles/s41597-019-0351-8**数据原始链接：** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131685**复现图片集锦** ：

![](../../images/e9f3b649f7472848.webp)

**文献简介** ：作者未提供

一、复写内容

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library(devtools)install_github("immunogenomics/harmony")library(Seurat)library(magrittr)library(harmony)library(dplyr)library(ggplot2)library(monocle)
#Kidney data loading 并构建seurat objectfile.link("kidney1/GSM4145204_kidney1_barcodes.tsv.gz", "kidney1/barcodes.tsv.gz")file.link("kidney1/GSM4145204_kidney1_features.tsv.gz", "kidney1/features.tsv.gz")file.link("kidney1/GSM4145204_kidney1_matrix.mtx.gz", "kidney1/matrix.mtx.gz")K1.data <- Read10X(data.dir = "kidney1/")K1 <- CreateSeuratObject(counts = K1.data, project = "kidney1", min.cells = 8, min.features = 200)
file.link("kidney2/GSM4145205_kidney2_barcodes.tsv.gz", "kidney2/barcodes.tsv.gz")file.link("kidney2/GSM4145205_kidney2_features.tsv.gz", "kidney2/features.tsv.gz")file.link("kidney2/GSM4145205_kidney2_matrix.mtx.gz", "kidney2/matrix.mtx.gz")K2.data <- Read10X(data.dir = "kidney2/")K2 <- CreateSeuratObject(counts = K2.data, project = "kidney2", min.cells = 8, min.features = 200)
file.link("kidney3/GSM4145206_kidney3_barcodes.tsv.gz", "kidney3/barcodes.tsv.gz")file.link("kidney3/GSM4145206_kidney3_features.tsv.gz", "kidney3/features.tsv.gz")file.link("kidney3/GSM4145206_kidney3_matrix.mtx.gz", "kidney3/matrix.mtx.gz")K3.data <- Read10X(data.dir = "kidney3/")K3 <- CreateSeuratObject(counts = K3.data, project = "kidney3", min.cells = 8, min.features = 200)
kid <- merge(x = K1, y = list(K2, K3)) #读取文件并用merge函数进行合并
# quality controlkid[["percent.mt"]] <- PercentageFeatureSet(kid, pattern = "^MT-") #提取有关线粒体的基因VlnPlot(kid, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3) #由图可以看出分布还可以
plot1 <- FeatureScatter(kid, feature1 = "nCount_RNA", feature2 = "percent.mt")plot2 <- FeatureScatter(kid, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")CombinePlots(plots = list(plot1, plot2))
kid <- subset(kid, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 30) #筛选条件kid <- NormalizeData(kid, normalization.method = "LogNormalize", scale.factor = 10000)kid <- NormalizeData(kid) #标准化kid <- FindVariableFeatures(kid, selection.method = "vst", nfeatures = 2000) #查找高变基因top10 <- head(VariableFeatures(kid), 10)plot1 <- VariableFeaturePlot(kid)plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE, xnudge = 0, ynudge = 0)CombinePlots(plots = list(plot1, plot2))ggsave("my_plot.png", plot2, width = 10, height = 6, units = "in")##图片因窗口问题，无法显示，选择直接保存查看

# 计算细胞周期s.genes <-cc.genes$s.genesg2m.genes<-cc.genes$g2m.geneskid <- CellCycleScoring(kid, s.features = s.genes, g2m.features = g2m.genes, set.ident = TRUE)all.genes <- rownames(kid)kid <- ScaleData(kid, vars.to.regress = c("S.Score", "G2M.Score"), features = all.genes)##此步骤相当耗费时间，根据文献所得细胞周期必然对单细胞测序结果的干扰，此处仅呈现代码kid <- ScaleData(kid, features = rownames(kid))kid  <- RunPCA(kid , features = c(s.genes, g2m.genes))DimPlot(kid)
#Eliminate batch effects with harmony and cell classificationkid <- RunPCA(kid, pc.genes = kid@var.genes, npcs = 20, verbose = FALSE)options(repr.plot.height = 2.5, repr.plot.width = 6)kid <- kid %>%  RunHarmony("orig.ident", plot_convergence = TRUE)　#等候时间较长，请溜达溜达吧harmony_embeddings <- Embeddings(kid, 'harmony')harmony_embeddings[1:5, 1:5]kid <- kid %>%  RunUMAP(reduction = "harmony", dims = 1:20) %>%  FindNeighbors(reduction = "harmony", dims = 1:20) %>%  FindClusters(resolution = 0.25) %>%  identity()new.cluster.ids <- c(0,1, 2, 3, 4, 5, 6, 7,8,9,10)names(new.cluster.ids) <- levels(kid)kid <- RenameIdents(kid, new.cluster.ids)
#Calculating differentially expressed genes (DEGs) and Save rds filekid.markers <- FindAllMarkers(kid, only.pos = TRUE, min.pct = 0.25, thresh.use = 0.25)#寻找高变基因write.table(kid.markers,sep="\t",file="/home/yuzhenyuan/Seurat/0.2_20.xls")write.table(kid.markers,sep="\t",file="kid.markers.xls")saveRDS(kid,file="kid.rds")
#Some visual figure generationDimPlot(kid, reduction = "umap", group.by = "orig.ident", pt.size = .1, split.by = 'orig.ident')#按样本进行划分DimPlot(kid, reduction = "umap", group.by = "Phase", pt.size = .1)　#按照细胞周期进行划分        DimPlot(kid, reduction = "umap", label = TRUE, pt.size = .1)#注意作者在用同样参数设置后分为10个clusters，其实无关紧要，都需要通过marker重新贴现。kid <- RenameIdents(object = kid,                    "0" = "Proximal convoluted tubule cells",                   "1" = "Proximal tubule cells",                   "2" = "Proximal straight tubule cells",                   "3" = "NK-T cells",                   "4" = "Monocytes",                   "5" = "Glomerular parietal epithelial cells",                   "6" = "Distal tubule cells",                   "7" = "Collecting duct principal cells",                   "8" = "B cells",                   "9" = "Collecting duct intercalated cells"                   )
cell 3 <- DimPlot(object = kid,         reduction = "umap",         label = TRUE,        label.size = 3,        repel = TRUE)ggsave("cell 3.png", a, width = 10, height = 6, units = "in")#热图DoHeatmap(object = kid, features = c("SLC13A3","SLC34A1","GPX3","DCXR","SLC17A3","SLC22A8","SLC22A7","GNLY","NKG7","CD3D","CD3E","LYZ","CD14","KRT8","KRT18","CD24","VCAM1","UMOD","DEFB1","CLDN8","AQP2","CD79A","CD79B","ATP6V1G3","ATP6V0D2","TMEM213"), size = 3 )#　绘制部分基因热图##小提琴图VlnPlot(kid, pt.size =0,         idents= c("Proximal tubule cells","Proximal straight tubule cells","NK-T cells"),         features = c("GPX3", "DCXR","SLC13A3","SLC34A1","SLC22A8","SLC22A7"))VlnPlot(kid,         idents= c("B cells","Collecting duct intercalated cells"),         features = c("AQP2", "ATP6V1B1","ATP6V0D2","ATP6V1G3"))
##tSNE Plotkid <-RunTSNE(kid, reduction = "harmony", dims = 1:20)TSNEPlot(kid, label = TRUE, pt.size = 1)TSNEPlot(kid, pt.size = 1, group.by = "orig.ident", split.by = 'orig.ident')TSNEPlot(kid, pt.size = 1, group.by = "Phase")

#Select a subset of PT cells PT <- subset(x = kid, idents= c("Proximal convoluted tubule cells","Proximal tubule cells","Proximal straight tubule cells")) saveRDS(PT,file="PT.rds")
#3个特征文件转换成CellDataSet格式#PT <- readRDS(file = "PT.rds")data <- as(as.matrix(PT@assays$RNA@counts), 'sparseMatrix') pd <- new('AnnotatedDataFrame', data = PT@meta.data) fData <- data.frame(gene_short_name = row.names(data), row.names = row.names(data)) fd <- new('AnnotatedDataFrame', data = fData) my_cds <- newCellDataSet(data,                          phenoData = pd,                          featureData = fd,                          lowerDetectionLimit = 0.5,                          expressionFamily = negbinomial.size())#将需要进行monocle的对象进行归一化my_cds <- estimateSizeFactors(my_cds)#计算每个单细胞样本的规范化因子（size factors）my_cds <- estimateDispersions(my_cds)#估计每个基因的离散度（dispersion）my_cds <- detectGenes(my_cds, min_expr = 0.1) ##过滤掉低质量的基因。pData(my_cds)$UMI <- Matrix::colSums(exprs(my_cds))disp_table <- dispersionTable(my_cds)#head(disp_table)
table(disp_table$mean_expression>=0.1)unsup_clustering_genes <- subset(disp_table, mean_expression >= 0.1)#细胞平均表达量大于0.1my_cds <- setOrderingFilter(my_cds, unsup_clustering_genes$gene_id)plot_ordering_genes(my_cds)
expressed_genes <- row.names(subset(fData(my_cds), num_cells_expressed >= 10)) #细胞表达个数大于10my_cds_subset <- my_cds[expressed_genes, ]#my_cds_subset#head(pData(my_cds_subset))my_cds_subset <- detectGenes(my_cds_subset, min_expr = 0.1)fData(my_cds_subset)$use_for_ordering <- fData(my_cds_subset)$num_cells_expressed > 0.05 * ncol(my_cds_subset)table(fData(my_cds_subset)$use_for_ordering)plot_pc_variance_explained(my_cds_subset, return_all = FALSE)
```

图片输出：

![](../../images/d3b00238d85cd398.webp)

![](../../images/d5168c106a291fcd.png)

![](../../images/0c76f57a45e33a6e.png)

![](../../images/02ae06b8b83e1c40.png)

![](../../images/cfc4c5dd4823a7fc.png)

![](../../images/ad858e4f2abdaa54.png)

![](../../images/d5b8e3ccd04737f3.webp)

![](../../images/d69c8de3b49f533b.png)

![](../../images/fb04371c800adcb8.png)

![](../../images/71c3a5083bdbc82f.png)

![](../../images/aa5a2b56e0f661a0.png)

![](../../images/af517632f54b42ef.webp)

![](../../images/b1ab1c29a007ebcd.jpg)

![](../../images/c1f772fc8e84dfb4.png)

![](../../images/bc1309a9467ad67d.png)

![](../../images/03bb72e427748700.png)

![](../../images/3293da726b8389d9.png)

![](../../images/f8c10ae292ed7e6e.png)

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/1eBQcA4OMrJNsouWWhzK-uw?pwd=n6lj

![](../../images/ea742359b922190d.jpg)

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
[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507096&idx=1&sn=98e42a5768074d2766f2ce64214ac391&chksm=9b3ca5c8ac4b2cdebe68a8519a087e41a4c88a7e465c5ddc107f633a5fbf3fcc8bbff6aa8821&scene=21#wechat_redirect>)

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
