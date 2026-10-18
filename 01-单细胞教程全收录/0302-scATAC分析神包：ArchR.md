---
title: "scATAC分析神包：ArchR"
date: 2026-09-15
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541958&idx=1&sn=221dbcea3fed4f7dfcf5b619ac67e2a1&chksm=9b3c5d96ac4bd4805c2eb90c0e461d46d1907126996c0e6a874c46bdb429fa85382ce588525f#rd
albums: ["单细胞教程全收录"]
---

# scATAC分析神包：ArchR

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541958&idx=1&sn=221dbcea3fed4f7dfcf5b619ac67e2a1&chksm=9b3c5d96ac4bd4805c2eb90c0e461d46d1907126996c0e6a874c46bdb429fa85382ce588525f#rd
> 合集：单细胞教程全收录

**一、写在前面**

在制作每个教程时，我们都建议大家了解分析背后的背景知识，学习这部分数据分析之前，我们先和大家一起看一篇综述： Sinha S, Satpathy AT, Zhou W, Ji H, Stratton JA, Jaffer A, Bahlis N, Morrissy S, Biernaskie JA. Profiling Chromatin Accessibility at Single-cell Resolution. Genomics Proteomics Bioinformatics. 2021 Apr;19(2):172-190.

1、[染色质可及性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540922&idx=2&sn=6e5463fcea9b18bf51b01d31d8ba3efe&scene=21#wechat_redirect>)

[scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541830&idx=2&sn=c4b21887049290ba96d38b1763e94ed3&scene=21#wechat_redirect>)能够帮助我们解析细胞特异性表达模型，但基因调控的过程与染色质活动情况则是这项技术的盲区。在基因的表达过程中，染色质可及性会发生一系列的改变，通过暴露不同的启动子、增强子和其它顺式调控元件(这个过程中就涉及染色质可及性的改变)，可以使[转录因子](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528198&idx=2&sn=86d1324d8f65c91f1221acfb1f984520&scene=21#wechat_redirect>)能够结合在染色质上调节相应基因的表达。染色质可及性（chromatin accessibility）是指染色质中DNA序列的可接触性和可转录性的程度。染色质可及性越高，DNA区域越容易被转录因子和其他调控因子访问，从而更容易进行转录和表达。常用的染色质可及性测定技术包括染色质免疫沉淀测序（ChIP-seq）、ATAC-seq（Assay for Transposase-Accessible Chromatin with high-throughput sequencing）等。

2、scATAC-seq文库构建

细胞内的Tn5转座酶能够通过“剪切和粘贴”机制催化转座子向基因组不同部分的运动。改造后的高活性版Tn5转座酶可用于ATAC-seq中用于检测基因组中无核小体区域。改造后的Tn5转座酶包含连接序列(测序的接头、样本标识符)，实验中导入细胞核后便能切割暴露的DNA并连接上Tn5转座酶所带上的标记序列。经过NGS测序后，我们通过对reads向基因组的比对，理论上来说获得reads数越多的区域，染色质可及性就越高。把ATAC-Seq改造成[scATAC-Seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&scene=21#wechat_redirect>)，那在Tn5连接的核酸序列上加上细胞条形码(cell barcode)即可。早期Shendure课题组使用组合的细胞标签在96孔板中标记Tn5转座酶，通过“组合条形码”来区分reads的细胞来源。Chang/Greenleaf实验室则是用微流体芯片完成了类似的建库。目前应用最广泛的还是10X Genomics提供的方案，其利用微流控技术，可以将10000个细胞核分割在纳米级液滴中，最多可以对6000个细胞进行标记。更多变种不再介绍，感兴趣的同学可以看一下原文（https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8602754/）。

3、scATAC-seq分析

scATAC-seq面临着与scRNA-seq一样的难点——[稀疏性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529675&idx=1&sn=4d16321d68430f9a1c2d20fb77234d24&scene=21#wechat_redirect>)。相对于[Bulk](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539518&idx=2&sn=c5ae4de79cf56486445597c13fe31db0&scene=21#wechat_redirect>)级别的技术而言，scATAC中每个细胞能够获得的reads数大大减少。scATAC的基础分析通常包括：

(1)原始数据→矩阵(测序接头去除、低质量序列过滤、双端reads匹配、基因组定量)

(2)Feature定义(将信号划分为预定义的TF基序/基因注释列表，可以降低数据集的方差)

(3)[异质性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&scene=21#wechat_redirect>)计算(类比scRNA-seq中的[高变基因选择](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537219&idx=1&sn=043692316d09cbfa24ececb3eb7166bf&scene=21#wechat_redirect>))

(4)降维、聚类分群(scATAC通常是一个很大的矩阵，约几千细胞X几万~几十万位点，单细胞常用的tSNE、UMAP在这里也同样可以使用)

学习手册可视化集锦（文末可获得代码和测试文件）：

![](../../images/e44ca2ce7abbcce6.webp)
更多scATAC教程可见：![](../../images/5d1de29dd4020889.webp)

**二、 ArchR绪论
**

1、ArchR论文解读

ArchR(Analyzing single-cell regulatory Chromatin in R)由斯坦福大学Greenleaf实验室的Granja等人开发，文章于2021年发表在《Nature Genetics》上，我们同样先来阅读一下原文： Granja JM, Corces MR, Pierce SE, Bagdatli ST, Choudhry H, Chang HY, Greenleaf WJ. ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis. Nat Genet. 2021 Mar;53(3):403-411.

scATAC-seq技术在测序层面的发展速度快于下游分析软件的发展速度，作者开发的ArchR正是为此而生。作者宣称ArchR能够在8小时内完成超过120万个单细胞的完整分析(在标准Unix笔记本上)，是端到端的scATAC分析套件，其功能覆盖了[双细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&scene=21#wechat_redirect>)鉴定(doublet removal)、聚类与细胞类型识别(single-cell clustering and cell type identification)、统一峰值集生成(unified peak set generation)、轨迹推断(cellular trajectory identification)、DNA元件与基因的连接(DNA element-to-gene linkage)、转录因子足迹(transcription factor footprinting)、由染色质可及性预测mRNA表达(mRNA expression level prediction from chromatin accessibility)以及[多组学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541095&idx=2&sn=1c354a87ce9ecbacf2406a30d759c077&scene=21#wechat_redirect>)整合(multi-omic integration with scRNA-seq)等。

为了实现大规模数据的分析，ArchR的核心创新在于其数据存储格式。ArchR不把整个计数矩阵读入内存，而是利用Apache Arrow格式将[稀疏矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&scene=21#wechat_redirect>)以列式存储的方式保存在磁盘上(Arrow文件)，并支持按需的随机访问。这使得ArchR能够在内存占用远低于传统方案(如把矩阵整体读入R的Seurat/Signac工作流)的情况下完成[百万级细胞的分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=1&sn=ecf56af3b929ec2b241854c89d25c671&scene=21#wechat_redirect>)：

  * 原始数据(fragments文件)被整理为TileMatrix(500bp窗口矩阵)、GeneScoreMatrix(基因评分矩阵)等多个投影(projection)矩阵，随用随取

  * 所有分析步骤围绕Arrow文件进行，内存中仅保留必要的中间结果

  * ArchRProject整合一个项目中的所有Arrow文件、细胞元数据与embedding(降维)结果，并通过saveArchRProject()保存/恢复完整分析状态

  * ArchR官方手册见：https://www.archrproject.com/bookdown/index.html ，源码见：https://github.com/GreenleafLab/ArchR

2、ArchR与Signac的对比

在[姊妹篇教程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527911&idx=1&sn=9407093c64e0b725bea160014fa6fb64&scene=21#wechat_redirect>)中我们使用了Satija lab的Signac(Stuart T, et al. Single-cell chromatin state analysis with Signac. Nat Methods. 2021 Nov;18(11):1333-1341.)。二者同为R语言中主流的scATAC分析工具，Signac构建在[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&scene=21#wechat_redirect>)框架之上(与Seurat对象无缝衔接)，而ArchR则使用独立的Arrow文件系统。值得一提的是，两篇文章各自在基准测试中都声称自己比对方更快——Signac论文中比较了PBMC与小鼠脑数据集中各分析步骤的运行时间，认为Signac端到端分析略快于ArchR；而ArchR论文则强调其Arrow格式带来的内存优势与百万级细胞的可扩展性。抛开“赛马”的成分，从实际使用体验来说：

  * [内存](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534017&idx=1&sn=725042656580b41c79ef4e3bb68063eb&scene=21#wechat_redirect>)友好：ArchR的磁盘存储方案内存占用更低，更适合大样本量数据

  * 功能全面：ArchR原生集成了peak calling(MACS2)、双细胞鉴定、motif富集、chromVAR偏差、TF足迹、[拟时序](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535114&idx=1&sn=95b6364b67d7ae9f03ba8455863ddabe&scene=21#wechat_redirect>)([monocle3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&scene=21#wechat_redirect>)/[slingshot](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527850&idx=1&sn=f4e2ca5e2e5e71eeaf132375bb8270eb&scene=21#wechat_redirect>))、scRNA整合等完整流程，几乎不需要额外“拼装”第三方工具

  * 面向文件系统：ArchR的项目围绕Arrow文件组织，项目目录结构清晰、便于复现

如果你的数据规模较大(几十万以上细胞)或者希望在一个框架内跑完全部分析，ArchR是非常好的选择；如果你已经深度使用Seurat生态、需要与scRNA对象频繁交互，那么Signac可能更顺手。本教程将带你完整走一遍ArchR的标准流程。

3、官方demo

ArchR官方手册的Getting Started with ArchR（https://www.archrproject.com/bookdown/getting-started-with-archr.html）章节使用人类骨髓造血干细胞分化(human hematopoiesis)的scATAC-seq数据进行演示，该数据来源于Granja et al. 2021(即ArchR原论文)，包含scATAC-Hematopoiesis-All-MPBC(全髓系/淋巴系祖细胞)与scATAC-CD34-BMMC-R1(CD34+骨髓单个核细胞)两个样本。官方demo覆盖了Arrow文件创建、质控、双细胞过滤、LSI降维、聚类、UMAP、基因评分、marker基因、peak calling、motif富集与足迹等核心章节。此外官方手册还提供了scRNA整合、多组学(multiome)、拟时序、共可及性等专题章节，大家可以根据课题需要按图索骥。

考虑到与姊妹篇(Signac)教程的数据衔接，本教程的实战部分选用10x Genomics官方发布的10k人PBMC scATAC-seq公开数据集(atac_pbmc_10k_nextgem, Chromium X平台v1.2化学)进行演示，该数据集的姊妹样本(atac_pbmc_500/1k/5k/10k_nextgem)同样用于姊妹篇教程的多样本章节，大家可以对比两个工具的分析结果。所有的官方教程链接、数据链接均经过笔者核验，测试数据已替大家下载在./data目录中。

**三、环境搭建
**

1、创建conda环境

按照惯例，我们通过[conda](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530994&idx=2&sn=3f3bdf2d06532c0b0ab8c9a477b8332c&scene=21#wechat_redirect>)创建一个独立的分析环境，并命名为archr_env。这里选择R 4.4+Bioconductor 3.20+Seurat V5的组合(与最新版ArchR 1.0.3兼容，该组合实测通过)。注意两点：新版bioconda中Bioconductor包已从r-前缀更名为bioconductor-前缀；如果本地~/.condarc配置了失效的[镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533721&idx=2&sn=ff2f23c988bb2e96038671f713f62807&scene=21#wechat_redirect>)通道，需要加上--override-channels参数：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
mamba create -y -n archr_env --override-channels \  -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge \  -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda \  r-base=4.4 r-devtools r-biocmanager r-remotes r-data.table r-matrix r-nabor \  bioconductor-rhdf5 bioconductor-rsamtools bioconductor-biostrings \  bioconductor-bsgenome bioconductor-genomicranges bioconductor-iranges \  bioconductor-s4vectors bioconductor-summarizedexperiment \  bioconductor-biocgenerics bioconductor-genomeinfodb \  bioconductor-genomicalignments bioconductor-rtracklayer \  bioconductor-chromvar bioconductor-motifmatchr bioconductor-tfbstools \  bioconductor-complexheatmap bioconductor-sparsematrixstats \  bioconductor-org.hs.eg.db bioconductor-bsgenome.hsapiens.ucsc.hg19 \  bioconductor-txdb.hsapiens.ucsc.hg38.knowngene \  bioconductor-deseq2 bioconductor-edger bioconductor-limma \  bioconductor-hdf5array bioconductor-singlecellexperiment \  r-ggplot2 r-gridextra r-gtools r-plyr r-stringr r-magrittr r-dplyr r-rcurl r-readr r-tidyr \  r-rmarkdown r-knitr r-patchwork r-future r-future.apply r-cowplot r-hdf5r r-seurat=5.3 \  r-xml r-rsqlite r-dbplyr r-sf r-spdep r-cairo \  macs2 samtools hdf5 openssl udunits2 gsl \  gcc_linux-64 gxx_linux-64 gfortran_linux-64 make pkg-config# 激活环境conda activate archr_env
```

向下滑动查看全部~

2、安装R包

ArchR本体及其部分依赖未收录在conda中，需要从CRAN与GitHub安装：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 设置镜像源: CRAN可用清华镜像加速;# 注意: Bioconductor不要设置国内镜像(清华/USTC镜像只保留最新版本),# 使用官方源即可自动重定向到官方归档镜像:options(repos = c(CRAN = "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))# BiocManager(R 4.4对应Bioconductor 3.20, conda已装好大部分Bioc包, 这里补齐遗漏项):if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager")BiocManager::install(version = "3.20", ask = FALSE, update = FALSE)# CRAN包:install.packages(c("ggrepel","gtable","harmony","matrixStats","uwot","RcppArmadillo",                   "ggseqlogo","hexbin","openintro","future","cowplot"))# GitHub包(ArchR的依赖):devtools::install_github("immunogenomics/presto")devtools::install_github("GreenleafLab/chromVARmotifs") # CIS-BP等motif数据库devtools::install_github("cole-trapnell-lab/monocle3")  # 拟时序分析# ArchR本体(重要: 官方1.0.3存在GeneScoreMatrix计算的索引bug, 见下文Bug 12,# 请安装笔者修复后的补丁版, 补丁包已放在data/software/目录):install.packages("data/software/ArchR_1.0.3_patched.tar.gz", repos = NULL, type = "source")
```

向下滑动查看全部~

Bug 12提醒: 官方ArchR 1.0.3的.addGeneScoreMat函数中，负链基因的方向判断使用了基因索引去索引overlap级别的向量(signDist[isMinus] <\- ...)，当染色体上存在没有任何tile重叠的负链基因时，会触发向量自动扩展，导致创建Arrow文件时报错length(x) must not exceed length(i)(官方issue #2158，作者已宣布维护停滞，未修复)。笔者已在补丁版中将负链判断修正为overlap级别：isMinus <\- which(as.character(strand(geneRegionz)[queryHits(tmp)]) == "-")。所有bug的排查记录见配套的ArchR_debug手册.md。

3、测试安装

  *   *   *   *

```
# 加载ArchR并测试安装(能正常加载并完成基因组注释即说明安装成功):library(ArchR)# 包版本信息:packageVersion("ArchR")
```
```
## [1] '1.0.3'
```

  *   *   *   *

```
# 设置参与并行计算的线程数:addArchRThreads(threads = 16)# 加载hg38基因组注释(ArchR会自动从TxDb与BSgenome构建基因注释与基因组注释):addArchRGenome("hg38")
```

**四、 ArchR实战：10k人PBMC scATAC数据分析
**

1\. 数据准备

本教程使用10x Genomics官方发布的10k人PBMC scATAC-seq数据(atac_pbmc_10k_nextgem, Chromium X平台)，共3个文件，其中fragments.tsv.gz是ArchR构建Arrow文件所必需的输入(记录了每个细胞barcode的所有Tn5插入片段)，filtered_peak_bc_matrix.h5是10x的peak矩阵(在ArchR流程中不必须，ArchR会自己call peak)：

  *   *   *   *   *

```
# 下载数据(约2GB):mkdir -p data/PBMC && cd data/PBMCwget https://cf.10xgenomics.com/samples/cell-atac/1.2.0/atac_pbmc_10k_nextgem/atac_pbmc_10k_nextgem_fragments.tsv.gzwget https://cf.10xgenomics.com/samples/cell-atac/1.2.0/atac_pbmc_10k_nextgem/atac_pbmc_10k_nextgem_fragments.tsv.gz.tbiwget https://cf.10xgenomics.com/samples/cell-atac/1.2.0/atac_pbmc_10k_nextgem/atac_pbmc_10k_nextgem_filtered_peak_bc_matrix.h5
```

10x的fragments.tsv.gz由cellranger-atac生成，已经是按染色体排序并bgzip压缩的tabix索引文件，可以直接作为ArchR的输入。fragments文件为5列的bed类格式(染色体、起始、终止、细胞barcode、片段数)：

  *   *

```
# 查看fragments文件前几行(不显示#注释行):zcat data/PBMC/atac_pbmc_10k_nextgem_fragments.tsv.gz | sed -n '10,13p'
```
```
## chr1 10097   10530   GTCTACCCATAAAGTG-1  1
## chr1 10108   10215   CAACGGCTCAAAGTAG-1  1
## chr1 10131   10321   GAACGTTAGCCTATAC-1  1
## chr1 10132   10261   GAACTTGGTATACGCT-1  1
```

2\. 创建Arrow文件与ArchRProject

Arrow文件是ArchR的核心数据格式。createArrowFiles()在创建过程中会完成三项工作：生成TileMatrix(500bp窗口)与GeneScoreMatrix(基因评分)投影矩阵、计算每个细胞的TSS富集分数(转录起始位点富集，scATAC重要的质控指标)与片段大小分布信息。这一步较为耗时(我们的测试数据约21.5分钟)，跑一次即可：

  *   *   *   *   *   *   *   *   *   *   *

```r
# 创建Arrow文件:# 约21.5mininputFiles <- "data/PBMC/atac_pbmc_10k_nextgem_fragments.tsv.gz"ArrowFiles <- createArrowFiles(  inputFiles = inputFiles,  sampleNames = "PBMC10k", # 样本名  minTSS = 2,              # TSS富集分数下限(该数据集的插入位点型TSS分数整体偏低, 说明见3.1节)  minFrags = 1000,         # 每个细胞最少fragments数  addTileMat = TRUE,       # 是否生成500bp tile矩阵(LSI降维需要)  addGeneScoreMat = TRUE   # 是否生成基因评分矩阵(marker基因分析需要))
```

  *   *   *   *   *   *   *

```r
# 创建ArchRProject(整合项目中所有Arrow文件):proj <- ArchRProject(  ArrowFiles = "PBMC10k.arrow",  outputDirectory = "result/PBMC10k", # 项目输出目录  copyArrows = TRUE                   # 将Arrow文件复制到项目目录中, 便于整体保存/迁移)proj
```

3\. 质量控制与[双细胞过滤](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&scene=21#wechat_redirect>)

3.1 质控指标可视化

  *   *

```r
# 加载已保存的项目(创建Arrow与QC指标已在上一步完成并保存):proj <- loadArchRProject("result/PBMC10k")
```

关于本教程minTSS = 2的说明：ArchR的TSS富集分数基于插入位点(cut site)在TSS±50bp窗口的富集程度计算，而10x Genomics官方web summary中的TSS富集指标基于片段重叠计算，两种指标不可直接比较。笔者对该数据集(atac_pbmc_10k_nextgem)的实测发现：其插入位点在TSS±50bp的富集倍数整体偏低(全基因组窗口/侧翼密度比约1.1)，但片段重叠型TSS信号正常(10x官方web summary的TSS富集分数中位数约8.2×10^3，promoter类型peak达11,703个)。因此ArchR默认的minTSS = 4对该数据集过于严苛(仅5个细胞通过)，笔者将其放宽至minTSS = 2，并主要依靠片段数(minFrags)、双细胞评分与下游聚类完成质控。如果你的数据插入位点型TSS分数正常(大部分数据如此)，仍推荐使用默认的minTSS = 4。相关排查过程详见配套的ArchR_debug手册.md(Bug 14)。

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# TSS富集分数分布(山脊图):p1 <- plotGroups(  ArchRProj = proj,  groupBy = "Sample",            # 按样本分组  colorBy = "cellColData",  name = "TSSEnrichment",        # TSS富集分数  plotAs = "ridges"              # 山脊图展示分布)# 片段大小分布(判断核小体条带模式, 正常应在147bp整数倍处出现周期峰):p2 <- plotFragmentSizes(ArchRProj = proj)# TSS富集分数 vs fragments数量散点图:p3 <- plotTSSEnrichment(ArchRProj = proj)patchwork::wrap_plots(p1, p2, p3, ncol = 3)
```

![](../../images/7144499f13264f48.webp)

3.2 双细胞鉴定与过滤

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 计算双细胞评分(内部会先做一次LSI+UMAP):# 约1.6minproj <- addDoubletScores(  input = proj,  k = 10,              # kNN邻居数  knnMethod = "UMAP",  # 使用UMAP空间中的邻居  LSIMethod = 1        # LSI实现方式, 1=TF-IDF+SVD)saveArchRProject(proj, load = FALSE) # 保存项目# 过滤双细胞:proj <- filterDoublets(proj, filterRatio = 1.5) # 双细胞富集分数超过阈值1.5的细胞被去除saveArchRProject(proj, load = FALSE)# 过滤后剩余2790个细胞(2917个通过QC的细胞中127个被判定为双细胞)
```

双细胞评分在UMAP上的分布将在第4节完成降维后与聚类结果一并展示。

4\. 降维聚类

ArchR使用迭代LSI(iterative LSI)对tile矩阵进行线性降维——第一轮LSI识别出的cluster用于排除与批次/测序深度相关的维度后，再进行第二轮LSI，使低维空间更聚焦于生物学变异：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 迭代LSI降维:# 约2.3minproj <- addIterativeLSI(  ArchRProj = proj,  useMatrix = "TileMatrix",       # 使用500bp tile矩阵  name = "IterativeLSI",  iterations = 2,                 # 迭代轮数  clusterParams = list(           # 每轮迭代中的聚类参数    resolution = c(0.2),    sampleCells = 10000,          # 每轮聚类最多抽样的细胞数    n.start = 10  ),  varFeatures = 25000,            # 参与计算的高变tile数量  dimsToUse = 1:30,               # 使用的LSI维度  force = TRUE)# 聚类(Seurat的图聚类实现):proj <- addClusters(  input = proj,  reducedDims = "IterativeLSI",  name = "Clusters",  resolution = 0.8,               # 聚类分辨率  force = TRUE)# UMAP非线性降维:proj <- addUMAP(  ArchRProj = proj,  reducedDims = "IterativeLSI",  name = "UMAP",  nNeighbors = 30,                # 邻居数量  minDist = 0.5,                  # 控制聚散程度  metric = "cosine",              # LSI结果常用cosine距离  force = TRUE)saveArchRProject(proj, load = FALSE)
```

向下滑动查看全部~

  *   *

```r
# 重新加载已保存的项目(包含降维/聚类结果; 后续展示均基于该项目):proj <- loadArchRProject("result/PBMC10k")
```

  *   *   *   *   *   *   *   *   *

```r
# 可视化聚类结果:p1 <- plotEmbedding(ArchRProj = proj, colorBy = "cellColData",                    name = "Clusters", embedding = "UMAP")# 双细胞评分在UMAP上的分布(鉴定潜在双细胞区域):p2 <- plotEmbedding(ArchRProj = proj, colorBy = "cellColData",                    name = "DoubletScore", embedding = "UMAP")p3 <- plotEmbedding(ArchRProj = proj, colorBy = "cellColData",                    name = "DoubletEnrichment", embedding = "UMAP")patchwork::wrap_plots(p1, p2, p3, ncol = 3)
```

![](../../images/d64931bffd6eab00.webp)

5\. 基因评分矩阵与marker基因

scATAC没有表达矩阵，ArchR通过统计基因体及其上游区域的Tn5插入信号生成基因评分矩阵(GeneScoreMatrix)，并可以用MAGIC算法插补(impute)来缓解稀疏性，用于marker基因的可视化与细胞注释：

  *   *   *

```r
# 计算impute权重(MAGIC):proj <- addImputeWeights(proj)saveArchRProject(proj, load = FALSE)
```

  *   *   *   *   *   *   *   *   *   *   *   *

```r
# PBMC经典marker基因的基因评分可视化(经过插补), 以4x4拼图展示:markerGenes <- c("CD14","CD3D","CD8A","CD4","MS4A1","NKG7","FCGR3A",                 "PPBP","GZMB","LYZ","IL7R","GNLY","CST7","XCR1","TREM1")p <- plotEmbedding(  ArchRProj = proj,  colorBy = "GeneScoreMatrix",  name = markerGenes,  embedding = "UMAP",  imputeWeights = getImputeWeights(proj) # 使用插补后的基因评分)# patchwork拼图(p为ggplot列表):patchwork::wrap_plots(p, ncol = 4)
```

![](../../images/cc1f42acb7331958.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 先按marker基因注释细胞类型(依据下表与热图):proj$CellType <- plyr::mapvalues(  proj$Clusters,  from = c("C1","C3","C6","C7","C8"),  to = c("CD14 Mono","B","CD4 T","CD4 T","NK"))saveArchRProject(proj, load = FALSE)# 注释完成后按CellType计算各细胞类型的marker基因:markersGS <- getMarkerFeatures(  ArchRProj = proj,  useMatrix = "GeneScoreMatrix",  groupBy = "CellType",                        # 以注释后的细胞类型分组  bias = c("TSSEnrichment", "log10(nFrags)"), # 矫正TSS富集分数与测序深度带来的偏差  testMethod = "wilcoxon"                      # Wilcoxon秩和检验)saveRDS(markersGS, "result/markerFeatures_GS_ct.rds")# 提取marker基因列表(FDR<=0.01且Log2FC>=1.25):markerList <- getMarkers(markersGS, cutOff = "FDR <= 0.01 & Log2FC >= 1.25")# 查看前几个细胞类型的top marker:sapply(names(markerList), function(x) head(markerList[[x]]$name, 6))
```

向下滑动查看全部~

  *   *   *   *   *   *   *

```r
# marker基因热图(以注释后的细胞类型展示):heatmapGS <- markerHeatmap(  seMarker = readRDS("result/markerFeatures_GS_ct.rds"),  cutOff = "FDR <= 0.01 & Log2FC >= 1.25",  labelMarkers = markerGenes, # 高亮标注经典marker  transpose = TRUE            # 转置(细胞类型为行))
```

![](../../images/a8cbf27db266a688.webp)

根据marker基因热图及经典marker的显著性(下表)，我们对cluster进行注释。值得注意的是，scATAC的基因评分信号弱于转录组，部分cluster的marker并不典型(C2、C4、C5)，对这些cluster我们保持cluster编号不做强行注释，后续第10节的scRNA整合注释会给出这些cluster的细胞类型预测：

![](../../images/3a9ed9171354ee69.png)

可以看到，scATAC基因评分注释存在不确定性(C7、C9、C10与整合预测不完全一致)，这正是scATAC单独注释的典型困难，第10节中我们将以scRNA整合结果为准完成注释。

6\. peak calling与差异peak

ArchR内置了基于MACS2的peak calling流程——每个cluster分别构建伪bulk replicates并call peak，取并集作为统一的peak集：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 先计算各细胞类型的伪bulk覆盖度(peak calling需要):# 约7minproj <- addGroupCoverages(ArchRProj = proj, groupBy = "CellType")# 基于MACS2的peak calling:# 约1.2minpathToMacs2 <- findMacs2() # 自动寻找macs2路径(conda环境需先conda activate archr_env)proj <- addReproduciblePeakSet(  ArchRProj = proj,  groupBy = "CellType",         # 按细胞类型分别call peak  pathToMacs2 = pathToMacs2,  genomeSize = 2.7e9,           # hg38的有效基因组大小  peakMethod = "Macs2",  method = "q",                 # 使用q值过滤  cutOff = 0.05,  force = TRUE)getPeakSet(proj) # 查看获得的peak集# 生成peak矩阵:proj <- addPeakMatrix(proj, force = TRUE)# 各细胞类型差异peak:markersPeaks <- getMarkerFeatures(  ArchRProj = proj,  useMatrix = "PeakMatrix",  groupBy = "CellType",  bias = c("TSSEnrichment", "log10(nFrags)"),  testMethod = "wilcoxon")saveRDS(markersPeaks, "result/markerFeatures_peaks_ct.rds")saveArchRProject(proj, load = FALSE)
```

向下滑动查看全部~

  *   *   *   *   *   *

```r
# 差异peak热图(以细胞类型展示):heatmapPeaks <- markerHeatmap(  seMarker = readRDS("result/markerFeatures_peaks_ct.rds"),  cutOff = "FDR <= 0.01 & Log2FC >= 1",  transpose = TRUE)
```
```
##   [1] "chr1:800921-801421"       "chr1:1071792-1072292"
##   [3] "chr1:1079341-1079841"     "chr1:1107055-1107555"    ##   [5] "chr1:1710250-1710750"     "chr1:1765384-1765884"    ##   [7] "chr1:3582751-3583251"     "chr1:4066906-4067406"    ##   [9] "chr1:4067477-4067977"     "chr1:4087489-4087989"    ##  [11] "chr1:8487532-8488032"     "chr1:8724064-8724564"    ##  [13] "chr1:9096667-9097167"     "chr1:9129538-9130038"    ##  [15] "chr1:9135013-9135513"     "chr1:1034101-1034601"    ##  [17] "chr1:1034607-1035107"     "chr1:1143316-1143816"    ##  [19] "chr1:1152346-1152846"     "chr1:1154694-1155194"    ##  [21] "chr1:1565085-1565585"     "chr1:1617644-1618144"    ##  [23] "chr1:1695623-1696123"     "chr1:1711705-1712205"    ##  [25] "chr1:1714072-1714572"     "chr1:9860410-9860910"    ##  [27] "chr1:203651706-203652206" "chr1:235460776-235461276"##  [29] "chr10:16829384-16829884"  "chr10:43827513-43828013" ##  [31] "chr10:69372683-69373183"  "chr10:71267493-71267993" ##  [33] "chr11:35257433-35257933"  "chr11:75219143-75219643" ##  [35] "chr12:12635138-12635638"  "chr12:46613500-46614000" ##  [37] "chr12:52545795-52546295"  "chr12:58148454-58148954" ##  [39] "chr1:6520341-6520841"     "chr1:11800782-11801282"  ##  [41] "chr1:15743369-15743869"   "chr1:15743922-15744422"  ##  [43] "chr1:17223147-17223647"   "chr1:19274813-19275313"  ##  [45] "chr1:20014528-20015028"   "chr1:23429796-23430296"  ##  [47] "chr1:23437128-23437628"   "chr1:23445587-23446087"  ##  [49] "chr1:25248703-25249203"   "chr1:27113841-27114341"  ##  [51] "chr1:28655282-28655782"   "chr1:33284456-33284956"  ##  [53] "chr1:35923148-35923648"   "chr1:2236484-2236984"    ##  [55] "chr1:3806464-3806964"     "chr1:3807510-3808010"    ##  [57] "chr1:7990862-7991362"     "chr1:8242436-8242936"    ##  [59] "chr1:8555982-8556482"     "chr1:8556492-8556992"    ##  [61] "chr1:8580444-8580944"     "chr1:8936541-8937041"    ##  [63] "chr1:10570865-10571365"   "chr1:11120858-11121358"  ##  [65] "chr1:11710354-11710854"   "chr1:12233731-12234231"  ##  [67] "chr1:12261583-12262083"   "chr1:1891392-1891892"    ##  [69] "chr1:2163244-2163744"     "chr1:2168539-2169039"    ##  [71] "chr1:2454767-2455267"     "chr1:2486240-2486740"    ##  [73] "chr1:2756880-2757380"     "chr1:2811163-2811663"    ##  [75] "chr1:2949575-2950075"     "chr1:3528067-3528567"    ##  [77] "chr1:3688460-3688960"     "chr1:3818663-3819163"    ##  [79] "chr1:8212607-8213107"     "chr1:8570134-8570634"    ##  [81] "chr1:1788481-1788981"     "chr1:1821486-1821986"    ##  [83] "chr1:1927539-1928039"     "chr1:2043788-2044288"    ##  [85] "chr1:2074226-2074726"     "chr1:2082134-2082634"    ##  [87] "chr1:2082692-2083192"     "chr1:2165757-2166257"    ##  [89] "chr1:2177477-2177977"     "chr1:3585355-3585855"    ##  [91] "chr1:3710146-3710646"     "chr1:25183545-25184045"  ##  [93] "chr1:25362616-25363116"   "chr1:36866436-36866936"  ##  [95] "chr1:38474975-38475475"   "chr1:67692249-67692749"  ##  [97] "chr1:94224410-94224910"   "chr1:104599810-104600310"##  [99] "chr1:116185166-116185666" "chr1:157369754-157370254"## [101] "chr1:162381810-162382310" "chr1:162383564-162384064"## [103] "chr1:164629581-164630081" "chr1:167455580-167456080"
## [105] "chr1:198489605-198490105" "chr1:200098570-200099070"
```

向下滑动查看全部~

  *

```
ComplexHeatmap::draw(heatmapPeaks, heatmap_legend_side = "bot", annotation_legend_side = "bot")
```

![](../../images/cdf3ecd55a2fd8d0.webp)

7\. motif富集与chromVAR偏差

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 添加CIS-BP人类motif注释(使用chromVARmotifs包内置数据, 无需联网下载):# 约2.5minproj <- addMotifAnnotations(  ArchRProj = proj,  motifSet = "cisbp", # CIS-BP数据库  name = "Motif",  force = TRUE)# 生成用于富集检验的背景peak:proj <- addBgdPeaks(proj, force = TRUE)# motif过表达富集(基于上一步按CellType计算的差异peak):enrichMotifs <- peakAnnoEnrichment(  seMarker = markersPeaks,  ArchRProj = proj,  peakAnnotation = "Motif",  cutOff = "FDR <= 0.1 & Log2FC >= 0.5")saveRDS(enrichMotifs, "result/enrichMotifs_ct.rds")# 计算chromVAR motif活性偏差矩阵:# 约4.7minproj <- addDeviationsMatrix(  ArchRProj = proj,  peakAnnotation = "Motif",  force = TRUE)saveArchRProject(proj, load = FALSE)
```

向下滑动查看全部~

  *   *   *   *   *   *   *   *   *   *

```r
# motif富集热图(每个细胞类型取top10富集motif):m <- readRDS("result/enrichMotifs_mlog10p_top_ct.rds")ht <- ComplexHeatmap::Heatmap(  m, name = "-log10(FDR)",  cluster_rows = TRUE, cluster_columns = TRUE,  col = colorRampPalette(c("white", "#FFF3B0", "#E09F3E", "#9E2A2B"))(100),  row_names_gp = grid::gpar(fontsize = 8),  column_title = "Motif Enrichment (-log10 FDR)")ComplexHeatmap::draw(ht, heatmap_legend_side = "bot")
```

![](../../images/ae5d64f221a107b4.webp)

富集结果中可以看到一些与细胞类型吻合的调控因子：CD14 Mono富集了髓系关键TFCEBPB(p=4.2)，B细胞富集了B细胞谱系决定因子BCL11A(p=3.6)，CD4 T富集了EGR1(p=4.5)、SMAD5，C10富集了EOMES(p=2.9, 与NK细胞标志一致)，C9富集了ETS家族成员ERG、ELK3等，这与marker基因注释的细胞类型相互印证。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# chromVAR偏差在UMAP上的可视化(新版plotEmbedding不支持MotifMatrix, 手动提取矩阵绘图):dev <- getMatrixFromProject(proj, useMatrix = "MotifMatrix")z <- as.matrix(SummarizedExperiment::assay(dev))umap <- getEmbedding(proj, embedding = "UMAP")df <- data.frame(  UMAP1 = umap[, 1], UMAP2 = umap[, 2],  SPIB = z["SPIB_336", ], BCL11A = z["BCL11A_194", ],  EOMES = z["EOMES_788", ], RUNX1 = z["RUNX1_733", ])plots <- lapply(c("SPIB","BCL11A","EOMES","RUNX1"), function(tf) {  ggplot(df, aes(UMAP1, UMAP2, color = .data[[tf]])) +    geom_point(size = 0.4) +    scale_color_gradientn(colors = ArchR::paletteContinuous(set = "horizonExtra")) +    ggtitle(paste0(tf, " chromVAR z-score")) +    theme_ArchR(baseSize = 8) +    theme(axis.text = element_blank(), axis.ticks = element_blank())})patchwork::wrap_plots(plots, ncol = 4)
```

向下滑动查看全部~

![](../../images/5a1ce31b3b88c325.webp)

8\. TF足迹分析

转录因子结合在DNA上时会保护其结合位点不被Tn5转座酶切割，ArchR通过比较各cluster中motif位点附近的Tn5插入模式来完成TF足迹分析：

  *   *   *   *   *   *   *   *   *   *

```r
# 获取motif位置:motifPositions <- getPositions(proj)# 计算足迹(以细胞类型分组):# 约23minseFoot <- getFootprints(  ArchRProj = proj,  positions = motifPositions,  groupBy = "CellType")saveRDS(seFoot, "result/seFoot_ct.rds")
```

  *   *   *   *   *   *   *   *   *   *   *

```r
# 足迹可视化(选取10个与PBMC谱系相关的TF):seFoot <- readRDS("result/seFoot_ct.rds")sel <- c("CEBPB_140","SPI1_322","PAX5_709","EBF1_67","TBX21_780",         "EOMES_788","RUNX1_733","BCL11A_194","IRF4_632","GATA3_384")plotFootprints(  seFoot = seFoot,  names = sel,  normMethod = "Subtract", # 双侧标准化, 足迹越明显motif中心信号越凹  plot = TRUE,  smoothWindow = 5)
```

9\. [拟时序分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539638&idx=2&sn=1baa7842af4a6d63bb3e8ed2b6e67b93&scene=21#wechat_redirect>)

新版ArchR(1.0.3)的addMonocleTrajectory()不再自动构建轨迹，而是接受外部构建好的monocle3对象(CDS)，我们先用插补后的基因评分矩阵构建CDS，再将其导入：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library(monocle3)# 从ArchR项目构建monocle3 CDS(使用插补后的基因评分矩阵):gsm <- getMatrixFromProject(proj, useMatrix = "GeneScoreMatrix")imp <- imputeMatrix(mat = assay(gsm), imputeWeights = getImputeWeights(proj))imp <- as(imp, "dgCMatrix")        # imputeMatrix返回dgeMatrix(稠密), 转换为monocle3可接受的稀疏格式rownames(imp) <- rowData(gsm)$name # 基因名存储在rowData$name中cds <- monocle3::new_cell_data_set(  expression_data = imp,  cell_metadata = as.data.frame(getCellColData(proj)),  gene_metadata = data.frame(gene_short_name = rownames(imp), row.names = rownames(imp)))# 使用ArchR的UMAP坐标作为monocle3的降维:reducedDims(cds)[["UMAP"]] <- getEmbedding(proj, embedding = "UMAP")# 聚类与轨迹学习:cds <- cluster_cells(cds, reduction_method = "UMAP")cds <- learn_graph(cds, use_partition = TRUE)# 以CD14单核细胞作为拟时序起点:root_cells <- rownames(getCellColData(proj))[proj$CellType == "CD14 Mono"]closest_vertex <- as.matrix(cds@principal_graph_aux[["UMAP"]]$pr_graph_cell_proj_closest_vertex[colnames(cds), ])root_pr_nodes <- igraph::V(principal_graph(cds)[["UMAP"]])$name[as.numeric(names(which.max(table(closest_vertex[root_cells, ]))))]cds <- order_cells(cds, root_pr_nodes = root_pr_nodes)# 将拟时序导入ArchR项目(以细胞类型分组):proj <- addMonocleTrajectory(  ArchRProj = proj,  name = "Monocle3",  groupBy = "CellType",  useGroups = unique(proj$CellType), # 参与轨迹的细胞类型(useGroups必须是groupBy取值的子集)  monocleCDS = cds,  force = TRUE)saveArchRProject(proj, load = FALSE)
```

向下滑动查看全部~

  *   *   *   *

```r
# 拟时序可视化(仅展示UMAP轨迹面板, plotTrajectory返回列表的第1个元素):p1 <- plotTrajectory(proj, trajectory = "Monocle3", colorBy = "cellColData",                     name = "Monocle3", continuousSet = "horizonExtra")p1[[1]]
```

![](../../images/748106906ff0ff8f.webp)

  *   *   *   *   *   *

```r
# 轨迹基因评分热图:trajMM <- getTrajectory(ArchRProj = proj, name = "Monocle3",                        useMatrix = "GeneScoreMatrix", log2Norm = TRUE)pTrajG <- plotTrajectoryHeatmap(trajMM, pal = paletteContinuous(set = "horizonExtra"),                                varCutOff = 0.9, maxFeatures = 100,                                labelTop = 30, returnMatrix = FALSE)
```

10\. 与scRNA整合

scATAC单独注释存在困难时，可以借助配对组织/样本的scRNA-seq参考数据进行整合注释，ArchR的addGeneIntegrationMatrix()基于Seurat的整合框架完成这一任务。

10.1 用Seurat处理scRNA参考数据

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library(Seurat)# 读取10x pbmc_10k_v3 scRNA数据:counts <- Read10X_h5("data/scRNA/pbmc_10k_v3_filtered_feature_bc_matrix.h5")seRNA <- CreateSeuratObject(counts = counts, project = "pbmc10k_v3",                            min.cells = 3, min.features = 200)# 标准预处理:seRNA[["percent.mt"]] <- PercentageFeatureSet(seRNA, pattern = "^MT-")seRNA <- subset(seRNA, subset = nFeature_RNA > 200 & nFeature_RNA < 5000 & percent.mt < 15)seRNA <- NormalizeData(seRNA)seRNA <- FindVariableFeatures(seRNA, nfeatures = 2000)seRNA <- ScaleData(seRNA)seRNA <- RunPCA(seRNA, npcs = 50)seRNA <- FindNeighbors(seRNA, dims = 1:30)seRNA <- FindClusters(seRNA, resolution = 0.5)seRNA <- RunUMAP(seRNA, dims = 1:30)# 依据经典marker基因注释细胞类型(DotPlot核对后手动注释):new.ident <- c(  "0"="CD14 Mono", "1"="CD4 T", "2"="CD14 Mono", "3"="CD4 T",  "4"="B", "5"="NK", "6"="CD8 T", "7"="NK", "8"="B",  "9"="CD16 Mono", "10"="CD8 T", "11"="CD14 Mono", "12"="Platelet",  "13"="CD14 Mono", "14"="CD4 T", "15"="NK", "16"="pDC",  "17"="CD14 Mono", "18"="CD4 T", "19"="DC")seRNA <- RenameIdents(seRNA, new.ident)seRNA$celltype <- Idents(seRNA)table(seRNA$celltype)saveRDS(seRNA, "result/seRNA_pbmc10k_annotated.rds")
```

向下滑动查看全部~

10.2 ArchR基因整合矩阵

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
seRNA <- readRDS("result/seRNA_pbmc10k_annotated.rds")proj <- addGeneIntegrationMatrix(  ArchRProj = proj,  useMatrix = "GeneScoreMatrix",  matrixName = "GeneIntegrationMatrix",  reducedDims = "IterativeLSI",  seRNA = seRNA,           # 带注释的scRNA参考  addToArrow = FALSE,      # 不写入Arrow文件(节省空间)  force = TRUE,  groupRNA = "celltype",   # 参考数据中的细胞类型注释列  nameCell = "predictedCell",  nameGroup = "predictedGroup",  nameScore = "predictedScore")saveArchRProject(proj, load = FALSE)
```

  *   *   *   *   *   *

```r
# 预测的细胞类型在UMAP上的分布:p1 <- plotEmbedding(proj, colorBy = "cellColData", name = "predictedGroup",                    embedding = "UMAP")p2 <- plotEmbedding(proj, colorBy = "cellColData", name = "predictedScore",                    embedding = "UMAP")p1 + p2
```

![](../../images/5efb99ddaccad197.webp)

11\. 最终效果展示

  *   *   *   *   *   *   *

```r
# 综合展示: 细胞类型注释、marker基因、motif偏差与拟时序p_final <- patchwork::wrap_plots(  plotEmbedding(proj, colorBy = "cellColData", name = "CellType", embedding = "UMAP"),  p2,  ncol = 2)p_final
```

![](../../images/e35d1f43841f1cc3.webp)

**五、资料领取**

本推送的代码和测试文件可以在以下链接中下载：

![](../../images/6112b49343fc9265.webp)![](../../images/ff40d14bc8f4d4be.png)

百度网盘链接: https://pan.baidu.com/s/1cXBiDtqXTC6Tv1RINkY0lQ

滴滴助手[Biomamba_zhushou]获取提取码

**六、 环境版本信息**

  *

```
sessionInfo()
```
```
## R version 4.4.3 (2025-02-28)
## Platform: x86_64-conda-linux-gnu## Running under: Ubuntu 20.04.4 LTS## ## Matrix products: default## BLAS/LAPACK: /home/biomamba/miniforge3/envs/archr_env/lib/libopenblasp-r0.3.34.so;  LAPACK version 3.12.0## ## Random number generation:##  RNG:     L'Ecuyer-CMRG ##  Normal:  Inversion ##  Sample:  Rejection ##  ## locale:##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              ##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    ##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   ##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 ##  [9] LC_ADDRESS=C               LC_TELEPHONE=C            ## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       ## ## time zone: Asia/Shanghai## tzcode source: system (glibc)## ## attached base packages:##  [1] parallel  stats4    grid      stats     graphics  grDevices utils    ##  [8] datasets  methods   base     ## ## other attached packages:##  [1] circlize_0.4.18             ComplexHeatmap_2.22.0      ##  [3] hexbin_1.28.6               ggridges_0.5.7             ##  [5] rhdf5_2.50.0                SummarizedExperiment_1.36.0##  [7] Biobase_2.66.0              RcppArmadillo_15.4.2-1     ##  [9] Rcpp_1.1.2                  Matrix_1.6-5               ## [11] GenomicRanges_1.58.0        GenomeInfoDb_1.42.0        ## [13] IRanges_2.40.0              S4Vectors_0.44.0           ## [15] BiocGenerics_0.52.0         sparseMatrixStats_1.18.0   ## [17] MatrixGenerics_1.18.0       matrixStats_1.5.0          ## [19] data.table_1.18.4           stringr_1.6.0              ## [21] plyr_1.8.9                  magrittr_2.0.5             ## [23] ggplot2_4.0.3               gtable_0.3.6               ## [25] gtools_3.9.5                gridExtra_2.3.1            ## [27] devtools_2.5.2              usethis_3.2.1              ## [29] ArchR_1.0.3                ## ## loaded via a namespace (and not attached):##  [1] bitops_1.0-9                      airports_0.1.0                   ##  [3] rlang_1.3.0                       clue_0.3-68                      ##  [5] GetoptLong_1.1.1                  otel_0.2.0                       ##  [7] compiler_4.4.3                    png_0.1-9                        ##  [9] vctrs_0.7.3                       shape_1.4.6.1                    ## [11] pkgconfig_2.0.3                   crayon_1.5.3                     ## [13] fastmap_1.2.0                     XVector_0.46.0                   ## [15] ellipsis_0.3.3                    labeling_0.4.3                   ## [17] Rsamtools_2.22.0                  rmarkdown_2.31                   ## [19] sessioninfo_1.2.4                 tzdb_0.5.0                       ## [21] openintro_2.5.1                   UCSC.utils_1.2.0                 ## [23] purrr_1.2.2                       xfun_0.60                        ## [25] BSgenome.Hsapiens.UCSC.hg38_1.4.5 zlibbioc_1.52.0                  ## [27] cachem_1.1.0                      jsonlite_2.0.0                   ## [29] rhdf5filters_1.18.0               DelayedArray_0.32.0              ## [31] Rhdf5lib_1.28.0                   BiocParallel_1.40.0              ## [33] cluster_2.1.8.3                   R6_2.6.1                         ## [35] bslib_0.12.0                      stringi_1.8.7                    ## [37] RColorBrewer_1.1-3                rtracklayer_1.66.0               ## [39] pkgload_1.5.3                     jquerylib_0.1.4                  ## [41] iterators_1.0.14                  knitr_1.51                       ## [43] cherryblossom_0.1.0               readr_2.2.0                      ## [45] tidyselect_1.2.1                  abind_1.4-8                      ## [47] yaml_2.3.12                       doParallel_1.0.17                ## [49] codetools_0.2-20                  curl_8.0.0                       ## [51] pkgbuild_1.4.8                    lattice_0.23-1                   ## [53] tibble_3.3.1                      withr_3.0.3                      ## [55] S7_0.2.2                          evaluate_1.0.5                   ## [57] Biostrings_2.74.0                 pillar_1.11.1                    ## [59] foreach_1.5.2                     generics_0.1.4                   ## [61] RCurl_1.98-1.17                   hms_1.1.4                        ## [63] scales_1.4.0                      glue_1.8.1                       ## [65] tools_4.4.3                       BiocIO_1.16.0                    ## [67] BSgenome_1.74.0                   GenomicAlignments_1.42.0         ## [69] fs_2.1.0                          XML_3.99-0.17                    ## [71] Cairo_1.6-2                       colorspace_2.1-3                 ## [73] GenomeInfoDbData_1.2.13           patchwork_1.3.2                  ## [75] restfulr_0.0.16                   usdata_0.3.1                     ## [77] cli_3.6.6                         S4Arrays_1.6.0                   ## [79] dplyr_1.2.1                       sass_0.4.10                      ## [81] digest_0.6.39                     SparseArray_1.6.0                ## [83] rjson_0.2.23                      farver_2.1.2                     ## [85] memoise_2.0.1                     htmltools_0.5.9                  ## [87] lifecycle_1.0.5                   httr_1.4.9
## [89] GlobalOptions_0.1.4
```

向下滑动查看全部~

![图片](../../images/cb4255ab8010219d.gif)

**欢迎致谢**

如果以上内容对你有帮助，欢迎在文章的Acknowledgement中加上这一段，联系客服微信可以发放奖励：
```
Since Biomamba and his wechat public account team produce bioinformatics tutorials and share code with annotation, we thank Biomamba for their guidance in bioinformatics and data analysis for the current study.
```

**欢迎在发文/毕业时向我们分享你的喜悦~**

**已致谢文章**

[ 鼻咽癌的Bulk RNA-Seq与scRNA-Seq联合分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510548&idx=1&sn=58048c46e837b1d56dffa282272c6d96&chksm=9b3cd344ac4b5a52369e91b4e61fa0a2c951b82cc21165b99f42ba2c2191d4add803bd73c928&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)

[13分+文章利用scRNA-Seq揭示地铁细颗粒物引起肺部炎症的分子机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511886&idx=1&sn=31c712d00377b0f0ed33703b5b4fbfd8&chksm=9b3cd61eac4b5f084fde14a2eb50356f2f40a66c608d38909f12a3d81f48cff029a09ce2ee8c&token=1453608870&lang=zh_CN&scene=21#wechat_redirect>)

[除了铁死亡，还有铜死亡？！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247518144&idx=1&sn=d036f1bb04b09eb73f53e2104d69404c&chksm=9b3cfe90ac4b77862f2f463b42132c7bfdb687a1b61d350dcf656117b1331271e179710fd4fa&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)

[IF14.3| scRNA-seq+脂质组多组学分析揭示宫内生长受限导致肝损伤的性别差异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520900&idx=1&sn=157134292ffc2e5df730c5ba8a357b61&chksm=9b3cebd4ac4b62c286543c30381e9b4fdb8b44b28d4fa902fb963bbd45b28e1d3f1bc98eb148&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)[银屑病和脂肪肝病中共同病理和免疫特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521069&idx=1&sn=4ef441a885cb2525ee3b5c81001feddf&chksm=9b3cea7dac4b636be9f10ffdf75e13531fccae62129944b21a457db2e08c3f2db1e1b553ac34&scene=21&cur_album_id=3425248581018714114#wechat_redirect>) [《Advanced Science》新型Arf1抑制剂促进癌症干细胞衰老并增强抗肿瘤免疫](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522233&idx=1&sn=287a380de741ff55f0ce78dc9c727985&chksm=9b3ceee9ac4b67ffd925abafeba2cb215a5984e6dc85f0d8607340a07ec9208f1d19eae0e04b&scene=21#wechat_redirect>)

[scRNA-seq揭示脓毒症预后水平预测的关键靶点！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522281&idx=1&sn=f95eb12fdc340b8da1123ec6253e6fac&chksm=9b3ceeb9ac4b67afa587e5fa3a2a8960e9bb28a1ad6dc48e49120a76154417a4c8be95af90b0&scene=21#wechat_redirect>)

[机器学习+生信多组学联合构建牙周炎"线粒体功能障碍与免疫微环境"关联网络](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527168&idx=1&sn=0791d2bf53a9a60015577f892b10d370&scene=21#wechat_redirect>)

[KIF18A在肝细胞癌转移中的双重角色](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528014&idx=1&sn=d285c9ebd415be328fc682d00e6182c0&scene=21#wechat_redirect>)

[bulk+scRNA-seq挖掘BCL2-MAPK14-TXN氧化应激诊断模型，鉴定脓毒症中氧化应激关键基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530000&idx=1&sn=e8ddca4e1b2e60839cdf2a7fe87b3dfe&chksm=9b3c0f40ac4b86562e0e307b9dbb8688159e72b3c19d9ceebf8a4bb2e21638896f005b497b11&scene=21&cur_album_id=3425248581018714114&search_click_id=#wechat_redirect>)

[致谢文章+1，中科院1区，scRNA-seq揭示麻黄-甘草配对治疗呼吸系统症状和多(I:C)诱发肺炎模型机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536407&idx=1&sn=4da88e13f112662a02fea89d1b7798e9&scene=21#wechat_redirect>)

[致谢文章又+1，生物信息学+机器学习鉴定驱动糖尿病肾病免疫激活和小管间隙损伤的PANoptosis枢纽基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537544&idx=1&sn=6e5bb738eb11af53173f9fef67b977df&scene=21#wechat_redirect>)

[致谢论文+1，MXRA7在骨髓衰老中调控巨噬细胞极化与微环境重塑](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541265&idx=1&sn=1f6d654ad1c0e774756a982a455a9144&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)
![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家一起讨论。![](../../images/fe8ecb8594a1f419.webp)![图片](../../images/acba43cb3408c3d0.gif)您点的每个赞和在看，我都认真当成了喜欢
