---
title: "10X Visium上游定量过程"
date: 2024-11-02
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522444&idx=1&sn=91ddf9e2ca3fb75db3ad524fe0042fab&chksm=9b3ce1dcac4b68cae69b4da8444dbccbf8c5cddd04697797420d1cc43a2048575a5f23d9d395#rd
albums: ["空间转录组"]
---

# 10X Visium上游定量过程

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522444&idx=1&sn=91ddf9e2ca3fb75db3ad524fe0042fab&chksm=9b3ce1dcac4b68cae69b4da8444dbccbf8c5cddd04697797420d1cc43a2048575a5f23d9d395#rd
> 合集：空间转录组

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

# 1 软件简介

Space Ranger是10x 公司为空间转录分析量身打造的一款数据分析软件，一般会用它来完成上游的分析步骤，主要用来处理Visium空间基因表达数据与明场和荧光显微镜图像，将测序数据和图片作为输入的数据，输出表达定量矩阵，为下游的seurat包提供整合之后的数据。也结合配套的loupe软件，做一些降维，聚类结果的可视化。

官网：https://www.10xgenomics.com/support/software/space-ranger/latest

如果你对下面的教程比较迷茫，那么你可以先行学习Linux教程：[十小时学会Linux](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&chksm=9b3cae21ac4b2737f5923b246470d699474c041bb78de50d2b71b99d537f9f44ca2938002cda&scene=21#wechat_redirect>)
[生信Linux及服务器使用技巧](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2980604042328702978#wechat_redirect>)
如果你的计算机不足以支持下面流程的学习，可按需选用适合自己的计算资源：共享(经济实惠)：[有root权限的共享服务器,报我名字立减200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)独享(省电省心)：[生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508226&idx=1&sn=69e0eea720ac6aecc0362bcb9ac339ba&chksm=9b3cd852ac4b51445651a091be0fb6f638bd8cf5eb399af1c54804631fe3047706cf1d4044de&scene=21#wechat_redirect>)

[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508226&idx=1&sn=69e0eea720ac6aecc0362bcb9ac339ba&chksm=9b3cd852ac4b51445651a091be0fb6f638bd8cf5eb399af1c54804631fe3047706cf1d4044de&scene=21#wechat_redirect>)实体(稳定高效)：[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506028&idx=2&sn=3b479a92f0c6119c4584efbc23b8c32a&chksm=9b3ca13cac4b282a9ffe1fc4f4ab1a50b14688c6490f859ef714b84a755c286cb8a585054486&scene=21#wechat_redirect>)

访问链接(复制到浏览器打开)：

https://biomamba.xiyoucloud.net/

更多内容可咨询客服微信[**Biomamba_yunying**]

# 2 在linux系统中下载和安装Space Ranger

下载网址https://www.10xgenomics.com/support/software/space-ranger/downloads

## 2.1 软件下载

选择wegt方法下载：

```bash
#新建一个属于它的文件夹
mkdir spaceranger
wget -O spaceranger-3.0.0.tar.gz "https://cf.10xgenomics.com/releases/spatial-exp/spaceranger-3.0.0.tar.gz?Expires=1713228032&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA&Signature=CdQ1bLjxIGu4jJbCJDzLpHozbM486wFSwzzl5TM3-sNR2AkssP~WqHmzBV7xwZmw93HqOg95QoT8p-xwXczVBEeEiMZ~nsPJRj7Gd9SVGlbj9DUi3EA7AFcgqgj-5vn0LpnvV1JXAJhpXF8AD-oEsvnWRkc0~rYVqmL2LIeoqa2mNiUkr9-G2Wkjkzwj46Ee1Y~rWb1-nYM3Jr9LtsmDs79SPLed3UOoXUeZJwsoTppdBplbGRiH~OzpiKTjIsl51lI-FS1xB0qoAo40XOGtCXxKVLMdL8Kv7QyKQZRj5bC5LpDjVnRyO7Da-5hEFKShC4vXTgdQ2I3MAjLNC68lAA__"
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzrus7AutPWammN15CmudppwhSeHibFvsy04D3VSiaWk1ibsON09q0Iia6Pw/640?wx_fmt=png&from=appmsg)

需要几分钟进行下载

## 2.2 安装

### 解压

```bash
cd spaceranger
tar -xzvf spaceranger-3.0.0.tar.gz
```

### 添加环境量

将 Space Ranger 目录添加到您的$PATH。这允许您调用 spaceranger 命令。这里我的路径为/home/wangyan/spaceranger

```
export PATH=/home/wangyan/spaceranger/spaceranger-3.0.0:$PATH
```

### 检查系统是否满足运行该软件的最小配置，结果保存在sitecheck.txt中

```
spaceranger sitecheck > sitecheck.txt
```

### 检查是否安装成功

```
export PATH=/opt/spaceranger-3.0.0:$PATH
spaceranger testrun --id=tiny
-----------------------------------------------------------------------------
Running preflight checks (please wait)...
Checking sample info...
Checking FASTQ folder...
Checking reference...

...

Pipestance completed successfully!
```

如果运行成功则会出现虚线下面的内容。尤其是这句：Pipestance completed successfully!

## 2.3 参考基因下载解压

### 下载

分别下载人的（11G需要1多小时）参考基因组：

```bash
#这里以GRCh38基因组为例
wget "https://cf.10xgenomics.com/supp/spatial-exp/refdata-gex-GRCh38-2020-A.tar.gz"
```

和鼠参考基因（9.7G）：

```bash
#这里以mm10基因组为例，下载了38分钟
wget "https://cf.10xgenomics.com/supp/spatial-exp/refdata-gex-mm10-2020-A.tar.gz"
```

### 解压

```
#这里以GRCh38基因组为例
tar -xzvf refdata-gex-GRCh38-2020-A.tar.gz
```

# 3 使用space ranger分析数据

## 3.1 prepare input(准备输入数据)

在开始运行Space Ranger之前，您需要准备输入文件。这些文件将根据您的实验参数、选择的检测方法以及您使用的 Space Ranger 管道而有所不同。

### 3.1.1 总览

#### input for spaceranger count

1.需要参考基因：

需要提前下载解压准备好，如果是人和小鼠以外的物种则需要自行制作，可参考下面网址进行：

https://www.10xgenomics.com/support/software/space-ranger/latest/advanced/custom-references

2.准备Fastq文件(测序数据)：可以用**spaceranger mkfast** 将BCL文件转化为fastq文件，再进行下一步的space count。

3.需要显微镜图像（明场或荧光或CytAssist 图像）用作表达数据的解剖图。

4.需要slide ID和capture area，如果提供的是 CytAssist 图像，则可以从图像元数据中自动检索此信息，并且不需要进一步的输入。

5.手动对齐：对于荧光图像（Visium v1，直接放置）、基准标记物受阻或组织边界不清晰或自动比对失败的情况，手动对齐是必要的。使用 –loupe-alignment 选项将生成的 JSON 文件指定为 spaceranger count。

6.要分析蛋白质表达数据（Visium HD 不支持），必须设置功能参考Feature Reference CSV。

#### input for spaceranger aggr

spaceranger aggr pipeline 需要一个 CSV 文件，该文件指定 molecule_info.h5 文件（从 spaceranger count输出）的路径，该文件表示要聚合的库。spaceranger aggr 不支持 Visium HD。

其中的spaceranger mkfastq用的比较少，spaceranger count用的最多。

## 3.2 spaceranger mkfastq

有时拿到的数据是BCL(binary base call)文件，需要转换为fastq格式文件。

SpaceRanger MKFastq可识别两种用于描述样本的文件格式:1.简单的三列CSV格式;2.bcl2fastq使用的Illumina Experiment Manager（IEM）样品表格式。下面的示例展示了使用每种格式运行 mkfastq。

### 示例展示(用tiny-bcl例子进行举例)

#### (1)下载举例数据

```bash
#下载tiny-bcl tar文件并解压
wget "https://cf.10xgenomics.com/supp/spatial-exp/spaceranger-tiny-bcl-1.0.0.tar.gz"
tar -xzvf spaceranger-tiny-bcl-1.0.0.tar gz

#下载简单的csv布局文件
wget "https://cdn.10xgenomics.com/raw/upload/v1682709348/software-support/Spatial-GEX/SR-v2.1/SR-mkfastq/spaceranger-tiny-bcl-simple-1.0.0.csv"

#下载IEM样品表格式
wget "https://cdn.10xgenomics.com/raw/upload/v1682709348/software-support/Spatial-GEX/SR-v2.1/SR-mkfastq/spaceranger-tiny-bcl-samplesheet-1.0.0.csv"
```

#### (2)Running mkfastq with a simple CSV sample sheet

大部分时候比较推荐使用simple csv，内容只包含3列 (泳道Lane, 样品名称Sample, Index)：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzpnIBHxswCVzedzzIrjGjNzHia3cVQs8VayOsJ2T0iaqIQAk0uJkqHicSQ/640?wx_fmt=png&from=appmsg)

run:

Hide
```
spaceranger mkfastq --id=tiny-bcl #设置output文件名
                    --run=/PATH/TO/tiny-bcl #
                    --csv=spaceranger-tiny-bcl-simple-1.0.0.csv
```

#### (3)Running mkfastq with an IEM sample sheet

IEM样品表有几个特定于在Illumina平台上运行的字段，包括指定样品和索引信息的[数据]部分。spaceranger mkfastq 支持列出索引集名称或寡核苷酸序列。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzu96lGAwgFE3cUh2EXYTtqTIzqeUwj4YZpoPZZWq1txnPfMLzqQypLQ/640?wx_fmt=png&from=appmsg)

run:

```
spaceranger mkfastq --id=tiny-bcl \
                    --run=/PATH/TO/tiny-bcl \
                    --samplesheet==spaceranger-tiny-bcl-samplesheet-1.0.0.csv
```

#### (4)检查fastq ouput

只有成功完成 spaceranger mkfastq 后才会输出为一个新文件夹，该文件夹的名字就是前面设置的 –id 选项中提供的命名：

```bash
ls -l

# expected output
drwxr-xr-x 4 jdoe  jdoe     4096 Nov 14 12:05 tiny-bcl
```

关键输出文件可以在 outs/fastq_path 中找到：

```bash
ls -l tiny-bcl/outs/fastq_path/ tiny-bcl/outs/fastq_path/

# expected output
drwxr-xr-x 3 jdoe jdoe         3 Nov  14 12:26 Reports
drwxr-xr-x 2 jdoe jdoe         8 Nov  14 12:26 Stats
drwxr-xr-x 3 jdoe jdoe         3 Nov  14 12:26 tiny-bcl
-rw-r--r-- 1 jdoe jdoe  20615106 Nov  14 12:26  Undetermined_S0_L001_I1_001.fastq.gz
-rw-r--r-- 1 jdoe jdoe  51499694 Nov  14 12:26 Undetermined_S0_L001_R1_001.fastq.gz
-rw-r--r-- 1 jdoe jdoe 152692701 Nov  14 12:26 Undetermined_S0_L001_R2_001.fastq.gz

tree tiny-bcl/outs/fastq_path/tiny_bcl/

# expected output
tiny-bcl/outs/fastq_path/tiny_bcl/
└── Sample1
    ├── Sample1_S1_L001_I1_001.fastq.gz
    ├── Sample1_S1_L001_R1_001.fastq.gz
    └── Sample1_S1_L001_R2_001.fastq.gz
```

# 4 Run pipelin (运行spaceranger)

## 4.1 spaceranger count

### 4.1.1 Visium V2 –count for Visium CytAssist, Spatial Gene and Protein Expression

Space Ranger v2.1 及更高版本可以分析使用福尔马林固定石蜡包埋 （FFPE） 样品生成的 Visium 空间基因和蛋白质表达数据集。在这个支持 CytAssist 的工作流程中，从 Visium 载玻片上的同一捕获区域生成单独的基因表达(GEX)和蛋白质表达 (PEX)测序文库。

常规的空间转录组的分析流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzVGC97XLFyEvVq4hDjBgJhJ8x2tInLibk57UjYLPq0OwWuibiaWN25ZHOw/640?wx_fmt=png&from=appmsg)

#### (1)input file输入文件准备

需要的文件包括：

1.libraries CSV(文库csv)，即GEX或PEX的fastq文件(**可选** ，如果结果基于RNAseq得到则需要的，可以用spaceranger mkfastq将BCL文件转化为fastq格式的文件，见3.2；如果是基于探针得到则不需要):

```
spaceranger --libraries
```

2.CytAssist图像(tiff，**可选** ，CytAssist捕获的图像时才用到):

```
spaceranger --cytaimage
```

3.Microscope image 组织的照片(明场或荧光照片，tiff、QPTIFF or JPEG，和CytAssist图像只选其一，取决于组织图像是那种类型，具体可以参考**5 Space Ranger的分析流程中的3种图像的参数**):

```
spaceranger --image #for 明场图像
            --darkimage #for 暗色背景荧光显微镜图像
            --colorizedimage #for 彩色荧光显微图像
```

4.slide 参数，包括ID和area：

```
spaceranger --slide,--area #联网的情况下
            --slidefile,--slide,--area #没联网时
```

其中slidefile必须直接下载，网址；https://www.10xgenomics.com/support/software/space-ranger/downloads#reference-downloads中的**Slide File Download**

5.参考基因组：人和鼠的可以从网上下载，其他的则需要自己构建

6.probe set CSV(**可选** ，结果是基于探针得到的则需要，否则不需要)

基于Visium探针的检测靶向人或小鼠转录组中的基因。对于这些检测，需要指定设置为 spaceranger 计数管道的相关探针。探针套装与Space Ranger套件捆绑在一起，下载网址：；https://www.10xgenomics.com/support/software/space-ranger/downloads#reference-downloads的**Probe Sets**

7.Feature Reference CSV(**可选** ,处理 Visium CytAssist **蛋白** 表达数据时，需要功能Feature Reference CSV 文件)：

Space Ranger v2.1 及更高版本与 Visium_Human_Immune_Cell_Profiling_Panel_v1.0.csv 捆绑在一起，其中包含 panel 中存在的每种抗体的蛋白质靶标信息和独特的寡核苷酸序列。CSV 的每一行都声明一种独特的抗体。特征参考 CSV 文件将使用 –feature-ref 标志传递给 spaceranger 计数。请注意，CSV 不得包含 ASCII 范围之外的字符。

#### (2)代码

```
spaceranger count --id=Visium_GEX_PEX #结果文件夹名
--fastqs=/.../.../fastq_path  #存放fastq文件的路径
--probe-set=Visium_Human_Transcriptome_Probe_Set_v2.0_GRCh38-2020-A.csv #存放探针文件的路径(可选项非必须,可从官网下载)
--image=/.../.../CytAssist_FFPE_tissue_image.tif #组织图像文件路径
--cytaimage=/.../.../CytAssist_FFPE_Protein_Expression_Human_Tonsil_image.tif  #CytAssist图像位置(可选：取决于样本测序时用的技术)
--transcriptome=/.../.../refdata-gex-GRCh38-2020-A
--slide=V43J30-093 CytAssist #slide ID
--slidefile=V19L01-041.gpr #如果未联网，slide布局文件(可选)
--area=D1 # slide area
--feature-ref=/.../.../CytAssist_FFPE_Protein_Expression_Human_Tonsil_feature_reference.csv #feature_reference.csv的存放位置(可选：计算蛋白表达量才需要)
--loupe-alignment=/…/…/sample.json  #如果手动对齐，json文件路径(可选)
--create-bam true #必填，选择true还是false，一般选择true
```

注意：

1.除了最后一行外，其他行代码结尾必须加****，这个符号表示这串代码是整体运行，不加的话切换到下一行就是新的一串代码了。

2.运行的路径中必须是在spaceranger软件所在路径，并且已经添加了环境量，否则会提示spaceranger cannot find the command.

#### (3)示例展示

这里用一个25岁男性扁桃体样本进行举例，具体样本信息见https://www.10xgenomics.com/datasets/visium-cytassist-gene-and-protein-expression-library-of-human-tonsil-with-add-on-antibodies-h-e-6-5-mm-ffpe-2-standard 利用空间转录分析其蛋白表达情况。

##### (3.1)下载需要的输入数据

```bash
wget https://s3-us-west-2.amazonaws.com/10x.files/samples/spatial-exp/2.1.0/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_fastqs.tar
wget https://cf.10xgenomics.com/samples/spatial-exp/2.1.0/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_image.tif
wget https://cf.10xgenomics.com/samples/spatial-exp/2.1.0/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_alignment_file.json
wget https://cf.10xgenomics.com/samples/spatial-exp/2.1.0/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_probe_set.csv
wget https://cf.10xgenomics.com/samples/spatial-exp/2.1.0/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_feature_reference.csv
wget https://cf.10xgenomics.com/samples/spatial-exp/2.1.0/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_tissue_image.btf
```

解压其中的fastq.tar文件：

```
tar -xvf CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_fastqs.tar
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzCZDngWO4QAlP4kXhgQXbzV2Tsb1Mozbb3OjtsPUIPUA4B6tPVxHOibg/640?wx_fmt=png&from=appmsg)

##### (3.2)run(这里进行图像的自动对齐)

```
spaceranger count --id=sample_count_test \
--fastqs=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_GEX_fastqs \
--probe-set=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_probe_set.csv \
--image=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_image.tif \
--cytaimage=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_image.tif \
--transcriptome=/home/wangyan/spaceranger/refdata-gex-GRCh38-2020-A \
--feature-ref=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_feature_reference.csv \
--slide=V43M23-019 \
--area=D1 \
--create-bam true \
--no-libraries
```

也可以写成一个shell(.sh文件)，把上面代码写进去，方法如下：

```
touch count_test.sh #新建一个shell文件

#用vim编辑，按i进入编辑界面
vim count_test.sh
#写入以下内容到该shell脚本
#!./bin/bash
spaceranger count --id=sample_count_test \
--fastqs=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_GEX_fastqs \
--probe-set=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_probe_set.csv \
--image=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_image.tif \
--cytaimage=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_image.tif \
--transcriptome=/home/wangyan/spaceranger/refdata-gex-GRCh38-2020-A \
--feature-ref=/home/wangyan/spaceranger/count_test/CytAssist_FFPE_Protein_Expression_Human_Tonsil_AddOns_feature_reference.csv \
--slide=V43M23-019 \
--area=D1 \
--create-bam true \
--no-libraries
#按esc后输入:wq保存退出

#在 Linux 中，要执行一个文件，必须具有执行权限：
chmod +x count_test.sh

#运行该shell脚本
./count_test.sh
```

##### (3.3)result

运行成功后会得到以下内容：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzMsmUIY76YfCKZjrfEiceqH8Xn524yZnNicSdMgKtVMtsficuSnOCfxKyA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmz6tBNuG9ibAnxQvHxTxYYDbOZPbwkAJGGoduLvwN2uaYmX6KYVVNic0cw/640?wx_fmt=png&from=appmsg)

得到的结果文件内主要包含以下内容：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzYpFMF5EbXNvCicC3LeydrCoibVkgbtOlh1xasc2XEPy4gOxmmeVicVrkw/640?wx_fmt=png&from=appmsg)

其中后续分析需要用到的数据在outs中，主要是filtered_feature_bc_matrix ，spatial (用于后续的seurat分析)；spaceranger本身也会进行下游分析 ，分析的结果保存在.cloupe，可以配合Loupe Browser进行使用；这次分析结果也会生成一个网页报告(web_summary.html)，里面包含本次分析信息例如分析数据信息(Summary)，质控信息(在网页报告中的Sequencing)以及下游分析信息(Gene Expression)。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzYbb7vzILyL9JEHuvJdWgVbcmklwr3o8bogLrSQxjPlBZwLz4gCUEZQ/640?wx_fmt=png&from=appmsg)

# 5 下游分析

## 5.1 Loupe Browser

spaceranger运行完成后的outs文件中的.cloupe文件就用于在Loupe Browser上进行下游分析。下面用上面得到的cloupe文件基于Loupe Browser7.0.1进行演示：

基本操作可以参考Loupe Browser的用法介绍那篇文章，之前的数据不是空间转录测序，这与前面不同的是，在菜单栏中有一项spot deconvolution，点击后生成的视图类似于 K 均值聚类的视图，但现在 K 表示不同的主题;deconvolution结果按 K 分层聚类，以反映细胞类型的不同粒度。具体的用法可以参考以下网址：https://www.10xgenomics.com/support/software/loupe-browser/latest/tutorials/space-ranger-spot-deconvolution

## 5.2 Seurat

这部分内容见Seurat文章。

```r
Library(Seurat)
Sample <- Read10X(data.dir = ‘/…/…/outs/filtered_feature_bc_matrix/’) #加载表达矩阵
Sample <- CreateSeuratObject(Sample, project = ‘brain’, assay = ‘Spatial’, min.cells = 3) #创建Seurat对象
Image <- Read10X_Image(‘/…/…/outs/spatial’) #加载图像
DefaultAssay(Image) <- 'Spatial'
Sample[[‘image’]] <- Image #整合表达矩阵与图像
```

# 6 空间区域的挑选

## (1)先在Loupe软件处理

Loupe中选择需要研究了cluster，并下载对应的Graph Based.csv文件：

a.方式一直接选择cluster，并下载该文件内容共2列，分别是barcode ID和cluster编号；

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzcHgUK9udaTuEkicpxibwqv5xZaQrBR9AOQYvcSMPhVTDaFFUricygtxxw/640?wx_fmt=png&from=appmsg)

b.方式二先选中目标cluster，再用右上方的套索和画笔工具，选好后生成新的分析，点击export–projection to csv，得到csv文件共3列，分别是barcode ID和X、Y坐标点。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzMbFQ1Q7Mmo7h2cBQPrfzzMWwmSzqtlU1SIF5CtTc5glqqYyAJdafSA/640?wx_fmt=png&from=appmsg)

## (2)Seurat处理

利用细胞ID(barcode ID)进行筛选子集,如果上一步得到的目标cluster细胞barcode ID保存在sub.csv文件中：

```r
cell_ID <- read.csv("sub.csv",header = TRUE)#从CSV文件中读取细胞ID
cell_ID <- as.character(cell_ID$Barcode)
sub_data <- Seurat::subset(object = seurat_object, cells = cell_ID)
```

object指原始数据，就是过滤后的表达矩阵。

**其他步骤与单细胞测序相同？？**

#  7 手动对齐

工具：Loupe，按图片操作：

a.红框选中的地方

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmz1W9ke0zibJhKS0PY8NPUq9O4AbJbS1iaoyoZoG8ftAI93cTgOhqG8b3A/640?wx_fmt=png&from=appmsg)

b.选择哪个取决于空间转录组是用什么技术做的，左边是普通，右边是用cytassist：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzW2IMEeIqib544YZpYUfXlKAu8UqXAHhR8hgtictbsaCsVRYTogia1KfmA/640?wx_fmt=png&from=appmsg)

c.这里选则右边，共4步骤，第一步上传图像，左边上传cyassist图像，右边上传组织图像，并在下方选择图像格式为明场还是荧光：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzUbYVVzZM6icjibcr809hUbv848gA666q9s9jibHfvEhibianwI1J6INPSYA/640?wx_fmt=png&from=appmsg)

d.上传成功后进行Next，Pin landmarks，进行左右定位，选择两张图中组织相同的位置，尽量选择5-8个点：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzrnaprej2TsNmtabjNkibcHhK1ck9qCwm0xwft7MlVAGkI3iamcevAerQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmz44gjY3lJXJbTcD2T1osEib9dZxVumn3Nk8wiccic3VNBu5pC45k922slw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzYdeqzLiaxkp8ODiahHcxqDHnyZvsVTqHs84Vfib6Ybm3XqTmG9atvuH6g/640?wx_fmt=png&from=appmsg)

e.完成后进行下一步

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzG6OvjiaLZ0he1ia4YfuFt8z5b5O0CM1tTkuAUkhHeInhwNI64BibehvPA/640?wx_fmt=png&from=appmsg)

f.选择生成JSON文件或者继续手动对齐：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxC2bk057etEhV9DiazfoMmzziaI8mq3nEecL0xsbInVTicHia95ufQSYq9u6DWBgrWXrzJO570k8IUZA/640?wx_fmt=png&from=appmsg)

# 补充1. Space Ranger的分析流程中的三种图像的参数

| 图像格式| **Space Ranger语法**|  是否自动基准对齐
---|---|---|---
**明场(eg:HE)**|  24位彩色TIFF/BigTIFF或JPEG| \--image| 是
**明场(eg:HE)**|  16位灰度TIFF/BigTIFF或JPEG| \--image| 是
**荧光**|  8 位或 16 位灰度单幅，8 位或 16 位灰度单幅；16位灰度TIFF/BigTIFF或JPEG| \--darkimage\--dapi-index| 否，必须在loupe中手动对齐
**荧光**|  24 位单色图像 TIFF/BigTIFF 或 JPEG| \--colorizedImage\--dapi-index| 否，必须在loupe中手动对齐
**CytAssist图像**|  24位彩色图像| \--cytaimage| 是

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**空间转录组内容合集**

**代码教程** ：

[空间转录组学习手册合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508744&idx=2&sn=8b13dec563b3dde70d6a1438300a4a3a&chksm=9b3cda58ac4b534ee4028b11d74f635dfdd1b1f17b3ca7d29135e4990229349e7ddc4ca0d9be&scene=21#wechat_redirect>)(包含[Seurat](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505213&idx=2&sn=6b9aad43c273009c3d7f80c63bb9f619&chksm=9b3cac6dac4b257b8fca1980fd5437ce131dd26377eeef8614d09c11a7ee22ed771cbf323a60&scene=21#wechat_redirect>)、[Scanpy](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505248&idx=2&sn=18995c7248ca6f13b61edfef24208ae1&chksm=9b3cac30ac4b2526050f91dd431bef96ab3dfbdc1a20b3dac32daa5138c11ceb8781b14a2bcd&scene=21#wechat_redirect>)、[Squidpy](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505844&idx=2&sn=5756c0702d080d6e602c504e7d461013&chksm=9b3caee4ac4b27f268c5f7cd39b6a1cbc138e465a6375c26c9a49b31697b63a4af2f702ec6b2&scene=21#wechat_redirect>)、[Stereopy](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505686&idx=2&sn=925ce770136ec3e964b954c639eed29e&chksm=9b3cae46ac4b2750f4c9f6d249d82257047334d7a7d5642288f5c2f909c51c934d692032eaa0&scene=21#wechat_redirect>))

[一文搞定空间转录组与单细胞测序的整合分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507210&idx=1&sn=f32037ffefd60b0d1bcca7bf9c3e0823&chksm=9b3ca45aac4b2d4cf0c68299db3a2891130d89d9e0fe2a9ecb34b394736550bcf7d7c51090cc&scene=21#wechat_redirect>)

[如何将已经构建好的Seurat空转对象转存为原始文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508133&idx=1&sn=297b8fb9cc8f33a1d19167dba1104e97&chksm=9b3cd9f5ac4b50e36df53e3e18bb2990d9635d88a725f1e54fc5eb5967ac9f0934b79cbb8b34&scene=21#wechat_redirect>)

**文献阅读** ：

[长脑子了!时空转录组揭示大脑再生机制](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498650&idx=1&sn=6321c00467e4c339c48080ef2c816178&chksm=9b3c82caac4b0bdc1bebbc8a77d40073d6d82792c02272bc639391483e3d7dfd671237028555&scene=21#wechat_redirect>)

[《Cell》| Stere-Seq力作](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499922&idx=1&sn=0795ec70b57723a46ccd5d643b3af11c&chksm=9b3cb9c2ac4b30d44e4218ecbdc50d210aa9c349400382f81ddb9f4f8e734fdef45453155d7b&scene=21#wechat_redirect>)

[空间转录组与单细胞转录组整合分析工具大比拼](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500243&idx=1&sn=b0e513e85a202ec7ca4041a700a7ae10&chksm=9b3cb883ac4b3195cffd0398d880468b12dd068f9a9fd96b7d0f8aed8961be34293e6ff4a2bb&scene=21#wechat_redirect>)

[《Nature》空间转录组综述](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=1&sn=cf4762197652fb023618bea6234f6343&chksm=9b3cbca0ac4b35b659392c508634c0efeb2ba5e203116de4854ece9bb32b648cc2648b2466cc&scene=21#wechat_redirect>)

[基于scRNA-Seq&空间转录组的AKI研究](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503664&idx=1&sn=39519d9cfa54e2d5b757f6c249ccbc86&chksm=9b3cb660ac4b3f768c8cfb708d8355c426b2d4ad39538acd5584aa9741ccdf1076b7112492df&scene=21#wechat_redirect>)

[真·单个细胞级别的空间转录组](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505451&idx=1&sn=c6f0694507ef839b123416c5160c01f6&chksm=9b3caf7bac4b266d853ad4e1f2aa2bb69922447e0cc7d83cd41b3a4bc697a6f5cf92ca5adca1&scene=21#wechat_redirect>)

[有免疫特征的基质细胞，有没有可能是双细胞？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506493&idx=1&sn=ed65c6b0738a1fb8492da0b4ecdc9c63&chksm=9b3ca36dac4b2a7b4ca45f169526c6ed51777e20811d50c2892e683eee405c25607a42cc7a66&scene=21#wechat_redirect>)

[Squidpy: 一站式完成空间多组学数据分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509220&idx=2&sn=19aaf18f6cc5f5fe16d3ce4bd35aed0a&chksm=9b3cddb4ac4b54a2d73892e093e560ab7d7ba913f480ccf11cd95b68bcd466a8758670d9de39&scene=21#wechat_redirect>)

[临床样本+单细胞+空转=IF4.8？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508744&idx=1&sn=1bc02443acab6d1720fe64e0334ce57a&chksm=9b3cda58ac4b534e3bf7ed2ab225d104d9976c5dc21b8443f88d3a555c5db67449b622ac91b4&scene=21#wechat_redirect>)

[单细胞空间转录组在脑科学领域的应用](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520599&idx=1&sn=f5de77dfcb186b29ff0f0657ea680baf&chksm=9b3ce807ac4b61119cff06d6dc1517e05e6296b2039d8a150121964eb134d30259e5f9e965ff&scene=21#wechat_redirect>)

[《Nature Methods》教你如何挑选空转平台](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520891&idx=1&sn=147d185643bd5dbba4e58b20b2eed872&chksm=9b3ceb2bac4b623d0273eb53b44709e951a493d79338d622b07e256cb4bf385c7d77983e7f48&scene=21#wechat_redirect>)

[Tangram利用深度学习完成空间与单细胞数据的整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521196&idx=1&sn=f77395164cd2e2568daa2aae811b8861&chksm=9b3ceafcac4b63ea5349ea37e1376ca3e0de875466bfc296721bd9e65568de342ddc406293df&scene=21#wechat_redirect>)

[空间转录组做到啥程度能博士毕业？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521581&idx=1&sn=0d7e4373a7bd011161e0e2b256c6461e&chksm=9b3cec7dac4b656bd062ec6b779916220b85903d1a4c955717c34b04867b92551e391772d8a6&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**欢迎致谢**

如果以上内容对你有帮助，欢迎在文章的Acknowledgement中加上这一段，联系客服微信可以发放奖励：
```
Since Biomamba and his wechat public account team produce bioinformatics tutorials and share code with annotation, we thank Biomamba for their guidance in bioinformatics and data analysis for the current study.
```

**欢迎在发文/毕业时向我们分享你的喜悦~**

**已致谢文章：**

**[《Advanced Science》新型Arf1抑制剂促进癌症干细胞衰老并增强抗肿瘤免疫](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522233&idx=1&sn=287a380de741ff55f0ce78dc9c727985&chksm=9b3ceee9ac4b67ffd925abafeba2cb215a5984e6dc85f0d8607340a07ec9208f1d19eae0e04b&scene=21#wechat_redirect>)
**

**[13分+文章利用scRNA-Seq揭示地铁细颗粒物引起肺部炎症的分子机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511886&idx=1&sn=31c712d00377b0f0ed33703b5b4fbfd8&chksm=9b3cd61eac4b5f084fde14a2eb50356f2f40a66c608d38909f12a3d81f48cff029a09ce2ee8c&token=1453608870&lang=zh_CN&scene=21#wechat_redirect>)
[IF14.3| scRNA-seq+脂质组多组学分析揭示宫内生长受限导致肝损伤的性别差异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520900&idx=1&sn=157134292ffc2e5df730c5ba8a357b61&chksm=9b3cebd4ac4b62c286543c30381e9b4fdb8b44b28d4fa902fb963bbd45b28e1d3f1bc98eb148&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)
[鼻咽癌的Bulk RNA-Seq与scRNA-Seq联合分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510548&idx=1&sn=58048c46e837b1d56dffa282272c6d96&chksm=9b3cd344ac4b5a52369e91b4e61fa0a2c951b82cc21165b99f42ba2c2191d4add803bd73c928&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)
[除了铁死亡，还有铜死亡？！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247518144&idx=1&sn=d036f1bb04b09eb73f53e2104d69404c&chksm=9b3cfe90ac4b77862f2f463b42132c7bfdb687a1b61d350dcf656117b1331271e179710fd4fa&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)
[银屑病和脂肪肝病中共同病理和免疫特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521069&idx=1&sn=4ef441a885cb2525ee3b5c81001feddf&chksm=9b3cea7dac4b636be9f10ffdf75e13531fccae62129944b21a457db2e08c3f2db1e1b553ac34&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)**

[**scRNA-seq揭示脓毒症预后水平预测的关键靶点！**](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522281&idx=1&sn=f95eb12fdc340b8da1123ec6253e6fac&chksm=9b3ceeb9ac4b67afa587e5fa3a2a8960e9bb28a1ad6dc48e49120a76154417a4c8be95af90b0&scene=21#wechat_redirect>)

**
**

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 公众号后台消息更新不及时，超过48h便不许回复读者消息，这里给大家留一下领取资料及免费服务器([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=2&sn=c2ba75edc0382855cfc914c3bb713e7e&chksm=9b3caa9bac4b238d0690d2aa5a236c18c8ad8f0d7a23421eb63b5236ff1201c9ec99e12efc8f&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)您点的每个赞和在看，我都认真当成了喜欢
