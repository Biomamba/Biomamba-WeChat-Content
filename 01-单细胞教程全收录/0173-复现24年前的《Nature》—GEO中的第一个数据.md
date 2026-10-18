---
title: "复现24年前的《Nature》—GEO中的第一个数据"
date: 2025-01-03
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526262&idx=1&sn=0cf9dc3dfb55a636634612a2aa1d2e23&chksm=9b3c1e26ac4b9730379286158af7e6f2a04a1bd496c8264581e361650b4fdb87d8ddef8939fa#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# 复现24年前的《Nature》—GEO中的第一个数据

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526262&idx=1&sn=0cf9dc3dfb55a636634612a2aa1d2e23&chksm=9b3c1e26ac4b9730379286158af7e6f2a04a1bd496c8264581e361650b4fdb87d8ddef8939fa#rd
> 合集：单细胞教程全收录 / 文献速递

**一、写在前面**

突发奇想，现在生信数据的存储主要阵地——GEO数据库所收录的第一篇SCI论文做了怎样的工作？于是我们在GEO数据库中进行了检索(https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE000001)并找到了这篇文章。这是一篇2000 年 8 月 1 日爱荷华大学N. Hayward**& J. Trent*团队在《Nature》上在线发表了题为“Molecular classifcation of cutaneous malignant melanoma by gene expression profling”的letter，主要包含了**38个样本** 的**探针数据** 并进行了黑色素瘤的分型。站在**上帝视角** 的我们显然觉得探针的数据分析起来非常的简单([相关性分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491702&idx=1&sn=5b786a572142e66fa8b0a1a7f71ff6ee&scene=21#wechat_redirect>)、[层次聚类](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520721&idx=1&sn=5f35f0e23d1fc60c357fb35ae6137881&scene=21#wechat_redirect>)谁不会啊)，这类探针数据在如今单细胞、空转等多组学数据满天飞的现在显得有些小儿科(时代的一粒沙，个人的一座山)。但原本**计划两天** 完成的复现工作，实际分析过程我们来回拉扯了**一个月** 。其中许多工具、可视化方法现如今已经逐渐的退出了历史舞台，但大牛们当年能够迈出GEO数据库的第一步，初步提出了表达矩阵的肿瘤分型思想，不可谓不是**跨时代**(永远可以相信《Nature》的含金量)。

![](../../images/21353e257bf3f6a8.webp)

简介：人类最常见的一种皮肤相关的癌症是皮肤恶性肿瘤。**皮肤黑色素瘤** 的发病率正在急剧上升，但在晚期疾病的非手术治疗方面几乎没有进展。尽管付出了大量努力试图识别黑色素瘤预后的独立预测因子，但目前(当时，**2000年以前**)没有公认的组织病理学、分子或免疫组织化学标志物能够定义这种**肿瘤的亚型** 。因此，文章报告通过对一系列样本的基因表达进行分析发现了一种黑色素瘤的亚型。令人惊讶的是，许多用于定义这一亚型的基因在体外形成**原始管状网络** 的侵袭性黑色素瘤中表现出差异性调控，而这种特征出现在某些高度侵袭性转移性黑色素瘤中。转录组分析可以识别出未被认识的皮肤黑色素瘤亚型，并预测可能对疾病进展重要的、可通过实验验证的表型特征。往期复现工作：[《NC》代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性和间充质成纤维细胞增加](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247525649&idx=1&sn=6145f50422ef8680be2a7ffd6c66f5f3&scene=21#wechat_redirect>)
[单细胞复写|3.急性心肌梗塞(AMI)外周血scRNA-Seq分析实战(链接重置)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501145&idx=2&sn=12c2e8d104ad343fc13acb8cda266e6c&scene=21#wechat_redirect>)

**二、主要内容**

###  （1）皮肤黑色素瘤样本聚类分析

文章收集了38例皮肤样本的转录组数据，包括3**1例黑色素瘤样本** 和**7例对照样本** 。fig1展示了几种分析方法的整合，以可视化皮肤黑色素瘤肿瘤样本之间的整体**表达模式** 关系。通过使用所有肿瘤样本的**皮尔逊相关系数** 矩阵，将31个黑色素瘤样本以**层次聚类树状图** 的形式展示出来（fig1a），同时通过多维尺度分析（MDS）展示31例样本的三维分布（fig1b）。分层树状图表明，19个样本紧密聚类在树状图的底部，处于相似度最高的区域。目前还没有一种既定的方法来评估通过聚类预测技术获得的分群关系的可靠性。因此，文章使用两种独立的方法进一步进行测试。第一种方法通过检查强**分类基因的频率** 与此类基因的**预期频率** （如果表达是随机变化的）以及与将相同样本随机划分为19个和12个新分组时强分类器的频率进行比较，来检查单个基因区分19个主要聚类与其余样本的能力。聚类结果的非随机性是显而易见的。具体而言，许多基因的表达模式在初始样本聚类之间有很大差异，因此可以作为良好的分类器（fig1c，红色三角形）。然而，当样本被分组为相同大小的随机分区时，很难找到对样本进行分类的表达模式（fig1c，蓝线）。因此，在随机形成的簇中，表达行为与基因相对于这些簇的真正随机行为基本上没有区别（fig1c，比较蓝线与空心圆）。第二种方法是基于向数据集引入随机扰动后评估聚类成员资格。对于每个样本，通过引入均值为0、标准偏差为0.15的随机高斯噪声来扰动每个基因的对数比（这是通过计算所有31个样本中单个基因的对数比的中位标准偏差得出的变化估计值）。然后对扰动后的数据集进行层次聚类，并对原始树（fig1a）和扰动树进行比较。比较包括原始树和扰动树分割成k个聚类，然后计算原始树中成对样本聚类在一起但在扰动树中不聚类在一起的配对样本的比例（将此度量称为差异对的比例加权，因为它对较大的聚类给予更大的权重）。对于每个可能的分割，在多个扰动数据集上重复进行比较。给定k（k=2：30），随后对扰动数据集中差异对的有权比例进行平均，从而确定了**加权平均差异对** （WADPk）。将原始树分割成9组或更少组所得到的聚类具有很强的可重复性（fig1d）。值得注意的是，WADPk的增加几乎与主要包含19个元素的聚类分裂成较小的子聚类完全重合。这些结果有力地支持了这样一种观点，即在本研究中识别出的黑色素瘤样本的主要聚类代表了一个真实且高度可重复的分组。

![](../../images/9ae980e4ee4597ec.webp)

### （2）两组患者肿瘤倾袭性比较

文中还纳入了两对来自同一患者的标本。它们是M92-001和M93-007（来自同一患者的两个不同样本，分别在手术切除后一年获得），以及TD-1376-3和TC1376-3（同一肿瘤的活检样本和细胞培养物在体外传代三次）。尽管细胞传代次数与聚类组之间没有显著关联，但纳入了TD-1376-3/TC-1376-3这对样本作为细胞培养效果的另一个对照。基于fig1中全部基因表达的线性相关性，fig2和fig3展示了用于指导“基因簇”解释的经验方法。fig2a描绘了用于提取单个基因“加权列表”的统计方法，这些基因在所有实验中的变化方差正确地定义了给定样本簇的边界。fig2b沿垂直轴按降序排列了在19个样本（fig1a和b）中定义主要黑色素瘤簇最有力的基因列表。样本沿水平轴按簇包含情况排序，**颜色饱和度与测量到的基因表达比率的幅度成正比** 。加权基因列表也可用于指导对**更大规模** 的基因表达数据集的分析。fig3a展示了本研究中皮肤黑色素瘤样本的所有数据，以彩色图像的形式呈现，基因按照表达模式的相似性沿垂直轴排列。fig3b-e展示了使用fig2b中“加权列表”中的四个基因（MART-1、CD63、 tropomyosin和WNT5A）。

![](../../images/4046d4c6241e793d.webp)

最后，在对皮肤黑色素瘤的微阵列分析的同时，研究了一系列具有转移相关特征的葡萄膜黑色素瘤标本，包括侵袭能力和体外血管生成模拟能力。令人惊讶的是，高度侵袭性葡萄膜黑色素瘤细胞与皮肤黑色素瘤样本主要簇列中的相同基因呈强烈负相关（fig2b）。这一观察结果，结合加权列表中基因的已知生物学功能，表明被分配到主要皮肤黑色素瘤簇列中的样本具有较低的**运动性和侵袭能力** ，因为它们下调了与细胞扩散或迁移相关的基因。在主要聚类之外的样本中基因表达趋势则是相反的，这些与其他文献报道一致。进一步使用一系列细胞检测来表征皮肤黑色素瘤迁移性和侵袭性区别。正如对它们基因表达模式的分析所预测的那样，与主要簇组外的黑色素瘤相比，主要簇组内的黑色素瘤的迁移性、侵袭能力和血管生成模拟能力都有所降低。

![](../../images/ef9802ce33066941.webp)

**
**

******三、小**** 结**

本研究中的患者群体**预后普遍较差** ，无论是典型的临床因素（如年龄、性别、活检部位）还是体外特征（如传代次数）都与临床结果没有强相关性。相比之下，基于基因表达对这些肿瘤进行分子分类（fig1）可以识别出一种**此前未被检测** 到的癌症亚型。总共有15名患者的生存信息可用，尽管结果在统计学上不显著，但具有一定意义。在紧密关联的19名患者中，有生存信息的10名患者中有3人死亡，而在其余组中，5名患者中有4人死亡。在目前无法确定谁最有可能出现疾病快速进展和死亡风险的情况下，**基于基因表达模式对黑色素瘤进行分类是有可能的** ，可以进一步用于识别对转移过程的各个方面至关重要的基因。目前黑色素瘤样本在临床上通过表达模式进行细分的能力程度仍有待阐明，但是本文为黑色素瘤的其他临床相关亚群研究提供了坚实的分子基础。

****四、文章复现****

1.复现集锦

![](../../images/48aadba7844d45ac.webp)

2.数据下载和预处理

示例数据集从GEO数据库下载即可。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
set.seed(123)setwd("/home/cwj/project/01_GEO")suppressMessages({  library(GEOquery)  library(scatterplot3d)  library(pheatmap)  library(ggplot2)  # 安装并加载 ClassComparison 包  # install.packages("ClassComparison")  library(ClassComparison)})# 从GEO数据库获取基因表达矩阵data <- getGEO("GSE1", destdir="/home/cwj/project/01_GEO",GSEMatrix =TRUE, getGPL=TRUE, AnnotGPL=TRUE)exp <- exprs(data[[1]]) #表达矩阵信息cli <- pData(data[[1]]) #临床信息GPL <- fData(data[[1]]) #平台信息gpl <- GPL[,c(1,3,11)] #提取需要的ID列和gene symbol列write.csv(exp,"GSE1_expeSet.csv")write.csv(cli,"GSE1_metadata.csv")gpl$'Gene symbol' <- data.frame(sapply(gpl$'Gene symbol',function(x)unlist(strsplit(x,"///"))[1]),stringsAsFactors=F)[,1]exp <- as.data.frame(exp)# 样本名替换成结果图中使用的样本名colnames(exp)<-cli$title #增加新列存储基因ID信息exp$ID <- rownames(exp) #为表达矩阵添加Gene symbol名称exp <-merge(exp,gpl,by="ID") dim(exp)
```
```
## [1] 8192   41
```

  *   *   *   *   *

```r
# 相同基因存在不同转录本，行名重新命名rownames(exp) <- paste0(rownames(exp),"_",exp[,"Gene symbol"])#删除无Gene symbol的行exp <- na.omit(exp) dim(exp)
```
```
## [1] 6275   41
```

  *   *   *   *   *   *   *   *   *   *

```r
sample_all <- cli$title# 筛选出肿瘤样本用于后续分析sample_mali <- c("NHGRI_A-357","NHGRI_HA-A","NHGRI_M91-054","NHGRI_M92-001","NHGRI_M93-007","NHGRI_M93-047","NHGRI_TC-1376","NHGRI_TC-F027","NHGRI_TD-1348","NHGRI_TD-1376","NHGRI_TD-1638","NHGRI_TD-1720","NHGRI_TD-1730","NHGRI_UACC-091","NHGRI_UACC-1012","NHGRI_UACC-1022","NHGRI_UACC-1097","NHGRI_UACC-1256","NHGRI_UACC-1273","NHGRI_UACC-1529","NHGRI_UACC-2534","NHGRI_UACC-2873","NHGRI_UACC-3093","NHGRI_UACC-383","NHGRI_UACC-457","NHGRI_UACC-502","NHGRI_UACC-647","NHGRI_UACC-827","NHGRI_UACC-903","NHGRI_UACC-930","NHGRI_WM1791C")exp_mali <- exp[,sample_mali]
```

3.31例黑色素瘤样本聚类

  *   *   *   *   *

```r
# fig1a# 方法1：基于表达矩阵聚类（与原文一致性最低）dist1 <- dist(t(exp_mali), method="euclidean") clust1 <- hclust(dist1,method="average")plot(clust1)
```

![](../../images/23a499131e5390fe.webp)

  *   *   *   *   *

```r
# 方法2：基于所有基因表达矩阵先计算样本之间的相关性矩阵，基于相关性，进行聚类划分（与原文一致性最高）cor2 <- cor(exp_mali, method = "pearson")dist2 <- dist(cor2, method="euclidean") clust2 <- hclust(dist2,method="average")plot(clust2)
```

![](../../images/54e82b860fcfe02f.webp)

  *   *   *   *   *   *   *   *   *   *

```r
# 方法3：unique使用剩下的4902个基因表达矩阵先计算样本之间的相关性矩阵，基于相关性，进行聚类划分（与原文一致性次之）exp_mali_new <- exp[,c(sample_mali,"Gene symbol")]exp_mali_new <- exp_mali_new[!duplicated(exp_mali_new$'Gene symbol'), ] rownames(exp_mali_new) <- exp_mali_new$'Gene symbol'# 去掉Gene symbol列exp_mali_new <- exp_mali_new[,-32]cor3 <- cor(exp_mali_new, method = "pearson")dist3 <- dist(cor3, method="euclidean") clust3<-hclust(dist3, method="average")plot(clust3)
```

![](../../images/62836f6707217b05.webp)

4.31例黑色素瘤样本三维空间分布

  *   *   *   *   *   *   *   *   *   *   *

```r
# fig1b：# 执行MDS，将距离矩阵转换为三维坐标# k 是目标维度数，这里设为3mds <- cmdscale(dist2, k = 3) mds <- as.data.frame(mds)# 给坐标轴命名colnames(mds) <- c("MDS1", "MDS2", "MDS3") # 定义样本所属的两个簇, Cluster 1 有 19 个样本，Cluster 2 有 12 个样本group <- c("1","2","1","1","1","2","1","2","1","1","1","1","1","1","2","1","2","1","1","2","1","2","1","1","1","1","2","2","2","2","2") names(group) <- sample_maliscatterplot3d(mds, color = as.numeric(group), pch = 19)
```

![](../../images/4788cad04b4bd6e7.webp)

##  5.基因与TNOM评分函数

  *   *   *   *   *

```
# fig1c# ClassComparison包中的 TNoM 函数用于计算 TNoM（Transcriptome-based Network of Modules） 分数，它是用于评估基因模块的稳定性和结构的指标。# TNoM 分数越高：表示模块的稳定性较高，网络结构更可靠。set.seed(123)showClass("TNoM")
```
```
## Class "TNoM" [package "ClassComparison"]
##
## Slots:
##
## Name:        data   tnomData       nCol       nRow classifier       call
## Class:     matrix    numeric    numeric    numeric     factor       call
```

  *

```
showClass("fullTNoM")
```
```
## Class "fullTNoM" [package "ClassComparison"]
##
## Slots:
##
## Name:        dex     fakir       obs       scr      name
## Class:   numeric   numeric   numeric   numeric character
```

  *   *   *   *

```r
bogus <- as.matrix(exp_mali)splitter <- rep(FALSE, 31)splitter[sample(1:31, trunc(12))] <- TRUEtn <- TNoM(bogus, splitter)
```
```
## [1] "ordering..."
## [1] "matrifying..."
## [1] "lapplying..."
## [1] "cumsuming..."
## [1] "more matrifying..."
## [1] "another apply..."
```

  *

```
summary(tn)
```
```
## TNoM object with 6275 rows and 31 columns
## Call: TNoM(data = bogus, classes = splitter)
##
## Number of genes with maximum number of misclassifications:
##    0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
##    0    0    0    1    1    5   47  177  479 1043 1643 1998  881    0    0    0
##   16
##    0
```

  *

```r
tnf <- update(tn)
```
```
## Simulation number: 1 . 2 . 3 . 4 . 5 . 6 . 7 . 8 . 9 . 10 .
```

  *

```
plot(tnf)
```

![](../../images/9a66bd2027faa9fd.webp)

##  6.WADP与K值

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# fig1d# WADP（Weighted Average Discrepant Pairs）是通过扰动数据并计算扰动前后聚类结构的稳定性来度量聚类结果的可靠性。即WADP衡量的是在不同的扰动（噪声）下，原始聚类中元素对在重新聚类时是否仍然被放在同一个组中# K值代表聚类的数量，即你在层次聚类树状图中切割的高度或切割点，决定了聚类的个数。不同的 K 值会导致不同的聚类结果。# 计算噪声标准差σ^2log_ratios_variance <- apply(exp_mali, 1, var)sigma_squared <- median(log_ratios_variance)# 计算每个簇的元素对数compute_M_and_D <- function(dendrogram, k, data, sigma_squared) {  # 1. 切割树状图，得到k个簇  clusters <- cutree(dendrogram, k)    # 2. 计算每个簇内的元素对数 (Mi) 和每个簇内的不同对数 (Di)  Nk <- length(unique(clusters))  # 簇的数量  M <- vector("numeric", Nk)  D <- vector("numeric", Nk)    for (i in 1:Nk) {    cluster_indices <- which(clusters == i)    Mi <- choose(length(cluster_indices), 2)  # 簇内对数 Mi    M[i] <- Mi        # 3. 扰动数据并重新聚类    perturbed_data <- data    perturbation <- matrix(rnorm(length(data), mean = 0, sd = sqrt(sigma_squared)), nrow = nrow(data), ncol = ncol(data))    perturbed_data <- perturbed_data + perturbation        # 4. 对扰动数据进行聚类    perturbed_clusters <- cutree(hclust(dist(t(perturbed_data))), k)        # 5. 计算不一致对数 (Di)    Di <- sum(perturbed_clusters[cluster_indices] != perturbed_clusters[cluster_indices[1]])    D[i] <- Di  }    return(list(M = M, D = D))}
# 计算WADPcompute_WADP <- function(k, data, dendrogram, sigma_squared) {  # 计算 M 和 D  M_and_D <- compute_M_and_D(dendrogram, k, data, sigma_squared)  M <- M_and_D$M  D <- M_and_D$D    # 计算加权平均不一致率 (WADP)  total_M <- sum(M)  total_D <- sum(D)  WADP <- total_D / total_M  return(WADP)}
# 对不同的k值进行计算，并绘制WADP与k的关系calculate_and_plot_WADP <- function(data, max_k) {  dendrogram <- hclust(dist(t(data)))    k_values <- 2:max_k  WADP_values <- numeric(length(k_values))    for (i in seq_along(k_values)) {    k <- k_values[i]    WADP_values[i] <- compute_WADP(k, data, dendrogram, sigma_squared)  }    # 绘制散点图  WADP_df <- data.frame(k = k_values, WADP = WADP_values)  ggplot(WADP_df, aes(x = k, y = WADP)) +    geom_point() +    geom_line() +    labs(title = "WADP vs k", x = "Number of clusters (k)", y = "WADP") +    theme_minimal()}calculate_and_plot_WADP(exp_mali, max_k = 30)
```

![](../../images/f2fd0d0af055f91b.png)

##  7.top22权重基因筛选

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# fig2b# top权重基因计算，根据原文公式w = dB / (k1dw1 + k2dw2 + α)# α 参数参考原文赋值alpha <- 0.1# 定义函数计算权重 wcalculate_gene_weight <- function(gene_expression, cluster_labels, alpha) {  # 1. 计算簇 1 和簇 2 的样本  cluster1 <- gene_expression[cluster_labels == 1]  cluster2 <- gene_expression[cluster_labels == 2]  # 2. 计算簇的质心  center1 <- mean(cluster1)  center2 <- mean(cluster2)  # 3. 计算 d_B：两个簇质心之间的欧几里得距离  d_B <- abs(center1 - center2)  # 4. 计算 d_w1 和 d_w2：每个簇内样本对的平均距离  d_w1 <- mean(dist(cluster1,method = "euclidean"))  # 簇 1 内距离  d_w2 <- mean(dist(cluster2,method = "euclidean"))  # 簇 2 内距离  # 5. 计算 k1 和 k2  # choose 函数用于计算组合数，即从n个不同元素中取出k个元素的组合方式的数量。  t1 <- choose(length(cluster1), 2)  # 簇 1 样本对数  t2 <- choose(length(cluster2), 2)  # 簇 2 样本对数  k1 <- t1 / (t1 + t2)  k2 <- t2 / (t1 + t2)  # 6. 计算 w  w <- d_B / (k1 * d_w1 + k2 * d_w2 + alpha)  return(w)}# 对表达矩阵中的每个基因计算权重gene_weights <- apply(exp_mali, 1, calculate_gene_weight, cluster_labels = group, alpha = alpha)# 将基因按照权重排序gene_weights_sorted <- sort(gene_weights, decreasing = TRUE)# 查看权重最大的前n个基因# 权重top22基因和原文top22重叠数有5个：AXL、CD63、MLANA、SNCA、WNT5Atop22 <- names(head(gene_weights_sorted, 22))order <- c("NHGRI_TC-F027","NHGRI_UACC-2873","NHGRI_UACC-1012","NHGRI_UACC-1529","NHGRI_UACC-647","NHGRI_WM1791C","NHGRI_UACC-827","NHGRI_HA-A","NHGRI_UACC-930","NHGRI_UACC-903","NHGRI_UACC-1097","NHGRI_M93-047","NHGRI_TD-1720","NHGRI_TD-1638","NHGRI_TD-1730","NHGRI_TD-1376","NHGRI_TC-1376","NHGRI_TD-1348","NHGRI_UACC-1022","NHGRI_A-357","NHGRI_UACC-3093","NHGRI_UACC-383","NHGRI_UACC-457","NHGRI_M92-001","NHGRI_UACC-2534","NHGRI_UACC-1273","NHGRI_UACC-1256","NHGRI_UACC-502","NHGRI_UACC-091","NHGRI_M91-054","NHGRI_M93-007")# 注意：这里原文是通过实验的方法参考了“Gene Expression Profiling of Alveolar Rhabdomyosarcoma with cDNA Microarrays”文献得到基因比率后绘制热图，具体是通过扫描微阵列，使用激光激发Cy3和Cy5的荧光，分别测量每个基因位置的荧光强度。Cy3和Cy5的信号强度将与各自的基因表达量成正比。在本流程是利用了基因表达矩阵绘制的热图pheatmap(exp_mali[top22,order], cluster_row = T, cluster_col = F, scale="row", border_color = NA)
```

![](../../images/d176dce47c048c41.webp)

  *

```
pheatmap(exp_mali[top22,order], cluster_row = T, cluster_col = F, scale="row", color = colorRampPalette(c("green", "black", "red"))(100), border_color = NA)
```

![](../../images/393bf1362134ab76.webp)

##  8.其他基因表达模式展示

  *   *

```
#fig3 样本*所有基因矩阵的热图pheatmap(t(exp_mali[,order]), cluster_row = F, cluster_col = T, scale="column", show_colnames=F, show_rownames=F, border_color = NA)
```

![](../../images/aa3dfbf0f859dbde.webp)

  *

```
pheatmap(t(exp_mali[,order]), cluster_row = F, cluster_col = T, scale="column", show_colnames=F, show_rownames=F, color = colorRampPalette(c("green", "red"))(100), border_color = NA)
```

![](../../images/e4717cc048d3e685.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 计算基因和基因之间的相关性，原文是按照每个基因所在簇进行定位,但是尝试将基因分成不同簇后，没有得到关注基因合适的聚类分群，因此调整策略计算关注基因相关性高的基因用于后续展示cor4 <- cor(t(exp_mali), method = "pearson")focus_genes <- c("MLANA","CD63","TPM1","WNT5A")cor_gene <- c()# 筛选出与每个关注基因最相似的 10 个基因for (i in focus_genes){  # 提取与关注基因的相关性  col <- colnames(cor4)[grepl(i, colnames(cor4), ignore.case = TRUE)]  gene_cor <- cor4[, col, drop=F]  # 按相关性从高到低排序，选出最相似的前 top_10 个基因  # 使用 for 循环依次对每列进行排序  for (i in col) {    gene_cor <- gene_cor[order(gene_cor[, i],decreasing = T),,drop=F]  }  gene <- rownames(gene_cor)[1:10]  cor_gene <- c(cor_gene, gene )}#准备热图注释条，对每一个组的基因分别命名name <- rep(c("Group1", "Group2", "Group3", "Group4"),each=10)anno_row <- data.frame(Group=name)rownames(anno_row) <- cor_genepheatmap(exp_mali[cor_gene,order], cluster_row = F, cluster_col = F,scale="row", annotation_row = anno_row, border_color = NA)
```

![](../../images/3bb52804c49e6808.webp)

  *

```
pheatmap(exp_mali[cor_gene,order], cluster_row = F, cluster_col = F,scale="row", annotation_row = anno_row, color = colorRampPalette(c("green", "black", "red"))(100), border_color = NA)
```

![](../../images/ac7b92cedb07d63d.webp)

********五、环境版本信息********

  *

```
sessionInfo()
```

```
## R version 4.2.2 Patched (2022-11-10 r83330)
## Platform: x86_64-pc-linux-gnu (64-bit)
## Running under: Ubuntu 20.04.6 LTS
##
## Matrix products: default
## BLAS:   /usr/lib/x86_64-linux-gnu/blas/libblas.so.3.9.0
## LAPACK: /usr/lib/x86_64-linux-gnu/lapack/liblapack.so.3.9.0
##
## locale:
##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C
##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8
##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8
##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C
##  [9] LC_ADDRESS=C               LC_TELEPHONE=C
## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C
##
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base
##
## other attached packages:
## [1] ClassComparison_3.3.2 oompaBase_3.2.9       ggplot2_3.5.1
## [4] pheatmap_1.0.12       scatterplot3d_0.3-42  GEOquery_2.66.0
## [7] Biobase_2.58.0        BiocGenerics_0.44.0
##
## loaded via a namespace (and not attached):
##  [1] tidyselect_1.2.1    xfun_0.35           bslib_0.4.1
##  [4] purrr_1.0.2         splines_4.2.2       colorspace_2.1-1
##  [7] openintro_2.4.0     vctrs_0.6.5         generics_0.1.3
## [10] htmltools_0.5.3     yaml_2.3.6          utf8_1.2.4
## [13] rlang_1.1.4         R.oo_1.25.0         jquerylib_0.1.4
## [16] pillar_1.9.0        R.utils_2.12.2      glue_1.8.0
## [19] withr_3.0.1         DBI_1.1.3           RColorBrewer_1.1-3
## [22] lifecycle_1.0.4     stringr_1.5.1       airports_0.1.0
## [25] munsell_0.5.1       gtable_0.3.5        R.methodsS3_1.8.2
## [28] cherryblossom_0.1.0 evaluate_0.18       labeling_0.4.3
## [31] knitr_1.41          tzdb_0.4.0          fastmap_1.1.0
## [34] curl_4.3.3          fansi_1.0.6         highr_0.9
## [37] readr_2.1.5         scales_1.3.0        cachem_1.0.6
## [40] limma_3.54.0        jsonlite_1.8.3      farver_2.1.2
## [43] hms_1.1.3           digest_0.6.30       stringi_1.8.4
## [46] dplyr_1.1.4         grid_4.2.2          cli_3.6.3
## [49] tools_4.2.2         magrittr_2.0.3      sass_0.4.3
## [52] tibble_3.2.1        cluster_2.1.4       usdata_0.2.0
## [55] tidyr_1.3.1         pkgconfig_2.0.3     data.table_1.14.6
## [58] xml2_1.3.3          rmarkdown_2.18      rstudioapi_0.14
## [61] R6_2.5.1            compiler_4.2.2
```

**六、参考**

https://www.nature.com/articles/35020115https://cran.r-project.org/web/packages/ClassComparison/ClassComparison.pdf
![](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![](../../images/3b8e21da777157f9.webp)![](../../images/7a5130b05d387a24.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=1&sn=d9517a0803ad75cb7be430806834e7b8&chksm=9b3ca7bdac4b2eaba1ad01ed04ab1fbcbafcf4f6ddfe9e4f76ed9229707f545fe7d9c9ffd6ae&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流(别问在么，添加时直接说来意)。呼声很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/7ef00c45433a7bde.webp)

![](../../images/acba43cb3408c3d0.gif) 您点的每个赞和在看，我都认真当成了喜欢
