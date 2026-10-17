---
title: "六千字深度解析| 可变剪切分析神器rmats环境配置与使用教程"
date: 2025-07-25
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529986&idx=1&sn=4aa7f4e1721d707703fb83b1e0ad8574&chksm=9b3c0f52ac4b8644808307ffdef60cfd2f09602229997cd8e74969ce08143357fb263c97e069#rd
albums: ["Bulk RNA-seq"]
---

# 六千字深度解析| 可变剪切分析神器rmats环境配置与使用教程

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529986&idx=1&sn=4aa7f4e1721d707703fb83b1e0ad8574&chksm=9b3c0f52ac4b8644808307ffdef60cfd2f09602229997cd8e74969ce08143357fb263c97e069#rd
> 合集：Bulk RNA-seq

一、写在前面

选择性剪接（Alternative splicing，AS）是剪除未成熟mRNA中的内含子、保留外显子后生成成熟mRNA的过程。在各类疾病发生和发展过程中，异常的选择性剪接起着重要作用。目前RNA-seq已经成为定量分析选择性剪切的有力工具。在[可变剪切分析神器——rMATs](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520911&idx=1&sn=1662a0b8ba6daa27cac8de6e581f3bfd&scene=21#wechat_redirect>)中我们分享过：作者在先前研究两个样本RNA-seq数据之间的**MATS(multivariate analysis of transcript splicing)的基础上，针对重复（replicate）的样本进行分析，开发了一种新的方法称为 rMATS。**我们在此前的课程转录组教程中已经包含了rMATS的实战([Bulk RNASeq| 转录组实战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510793&idx=1&sn=bfa69e8f261932d9bea74443fab732f0&chksm=9b3cd259ac4b5b4fd4b3bb80d0210a3396cda777b32ab49be1a45339453db314bb2a17fc438d&scene=21#wechat_redirect>))。rmats安装与环境配置较为复杂，Biomamba也踩过很多坑，这里让我们一起来看看这个工具的环境配置与具体语法教程。

二、安装

本教程基于[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528429&idx=2&sn=26c1d429b2458ea066582e0cb823d935&scene=21#wechat_redirect>)测试(Ubuntu 20.04 LTS)，对Linux还不熟悉的小伙伴可以先行学习：[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)。rMATS还依赖于以下环境：

  * Python (3.6.12 or 2.7.15)
  * Cython (0.29.21 or 0.29.15 for Python 2)

  * BLAS, LAPACK
  * GNU Scientific Library (GSL 2.5)
  * GCC (>=5.4.0)
  * gfortran (Fortran 77)
  * CMake (3.15.4)
  * PAIRADISE (optional)
  * Samtools (optional)
  * STAR (optional)

此外有r-base==3.6.3和Cython==0.29.21、python==3.6.12等要求，conda可以自行解决依赖(conda安装使用可见教程：[生信软件管家——conda的安装、使用、卸载](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506208&idx=1&sn=24d27bc2ff8de340b1f542610b4dc09e&scene=21#wechat_redirect>))

以下R包需要安装：

  *   *   *   *   *   *   *   *   *   *

```
conda create -n rmats python==3.6.12conda install mambamamba install r-nloptrmamba install r-foreachmamba install r-doParallel#以上三个一般R环境中都已存在mamba install bioconductor-pairadise #二进制的编译可以参考这里：https://github.com/Xinglab/PAIRADISEmamba install rmats==4.1.2mamba install gsl#否则可能会因找不到libgsl.so.25而报错
```

  *

```
pip install Cython
```

  *   *   *   *   *   *   *   *   *   *   *   *

```bash
wget https://codeload.github.com/Xinglab/rmats-turbo/zip/refs/heads/master -O rmats-turbo-master.ziptar -xvf rmats-turbo-master.ziprm rmats-turbo-master.zipcd rmats-turbo-master.sudo apt-get install cmake # 确保cmake已安装，才能完成以下的编译与安装./build_rmats#使用：python rmats.py {arguments}python rmats.py --help # 能正常返回帮助信息则说明安装成功./build_rmats [--conda] [--no-paired-model]--conda: 创建R与python的依赖环境--no-paired-model: 不创建依赖环境
```

需要依赖gsl运行，否则rmats后续输出txt列表均为空：

  *   *   *   *   *   *   *   *

```bash
wget http://ftp.club.cc.cmu.edu/pub/gnu/gsl/gsl-2.5.tar.gztar xzf gsl-2.5.tar.gzcd gsl-2.5/./configuremakesudo make installexport PATH="/home/biomamba/miniconda3/lib/:$PATH"export LD_LIBRARY_PATH="/home/biomamba/miniconda3/lib/"
```

三、快速上手

rmat支持fatsq、fastg.gz、sam等格式的文件输入

1、fastq文件输入

准备两个txt文件，用:分割配对reads，用,分割重复(样本)

  * /path/to/s1.txt

  *

```
/path/to/1_1.R1.fastq:/path/to/1_1.R2.fastq,/path/to/1_2.R1.fastq:/path/to/1_2.R2.fastq
```

  * /path/to/s2.txt

  *

```
/path/to/2_1.R1.fastq:/path/to/2_1.R2.fastq,/path/to/2_2.R1.fastq:/path/to/2_2.R2.fastq
```

那么运行过程就是：

  *   *   *   *

```
python rmats.py --s1 /path/to/s1.txt \--s2 /path/to/s2.txt --gtf /path/to/the.gtf \--bi /path/to/STAR_binary_index -t paired --readLength 50 \--nthread 4 --od /path/to/output --tmp /path/to/tmp_output
```

显然，这个过程是需要依赖STAR索引做比对的，也就是说，fastq实则无法直接参与ramts的pipeline，而是暂时将FASTQ文件转为BAM文件并存于--tmp中

2、bam文件输入

任何比对工具生成的BAM文件也可以用作rMATS的输入文件，rMATS会虎烈alignments的soft活hard clip，除非设定--alow-clipping参数

同样需要准备两个分组文件：

  * /path/to/b1.txt

  *

```
/path/to/1_1.bam,/path/to/1_2.bam
```

  * /path/to/b2.txt

  *

```
/path/to/2_1.bam,/path/to/2_2.bam
```

那么这么运行即可：

  *   *   *   *   *

```
python rmats.py --b1 /path/to/b1.txt --b2 /path/to/b2.txt \--gtf /path/to/the.gtf -t paired \--readLength 50 --nthread 4 --od /path/to/output \--tmp /path/to/tmp_output
```

3、分解prep与post步骤

prep步骤中输入的数据被处理为.rmats文件并存于--tmp目录中，post步骤则将.rmat文件处理为最终输出的文件。\--task可以将两个步骤拆开，这样可以使两步在不同的时间甚至不同的机器中运行，例如你有两台各4线程的机器与8个BAM文件，那么你可以一台运行prep、一台运行post。

machine1：

  *   *   *   *   *

```
python rmats.py --b1 /path/to/prep1.txt \--gtf /path/to/the.gtf -t paired --readLength 50 \--nthread 4 --od /path/to/output --tmp /path/to/tmp_output_prep_1 \--task prep
```

machine2:

  *   *   *   *

```
python rmats.py --b1 /path/to/prep2.txt \--gtf /path/to/the.gtf -t paired --readLength 50 \--nthread 4 --od /path/to/output --tmp /path/to/tmp_output_prep_2 \--task prep
```

需要将中间文件整理至post步骤运行的位置，过于鸡肋，不做记录。。。。

统计检验的步骤也可以分开运行，这里我们计算资源充分，不做记录。

Tips:

1、统计检验可以通过\--statoff跳过，并且单个分组、单个样本也可以进行剪切分析，在设定\--statoff的同时只设定\--b1 or \--s1选项即可

2、两组的样本重复可以不同，例如--b1包含3个样本，--b2近包含一个样本也被允许

3、fastq的gz压缩可以被自动识别(依赖于扩展名)

4、prep step可以同时允许，全部prep步骤结束后post step才可以开始

5、拆分步骤时注意中间文件.rmats的移动

6、prep步骤产生的.rmats文件按可以能会冲突，个人不建议拆分运行，除非算力不足或有特殊需求

7、拆分时两步的bam路径需要给定相同样本的完整路径

8、若数据集较小，则可以通过\--task both同时运行两步

9、\--novelSS可以允许为被注释位点的剪接位点被检测

10、\--fixed-event-set可以指定一个文件fromGTF.[AS].txt，这样允许此前允许的.rmats文件被载入而无需从头运行

四、帮助文档

如果你希望查看所有选项参数的介绍，可以看看主脚本的帮助文档：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
python rmats.py -husage: rmats.py [options]optional arguments:  -h, --help            show this help message and exit  --version             show program's version number and exit  --gtf GTF             An annotation of genes and transcripts in GTF format  --b1 B1               A text file containing a comma separated list of the                        BAM files for sample_1. (Only if using BAM)  --b2 B2               A text file containing a comma separated list of the                        BAM files for sample_2. (Only if using BAM)  --s1 S1               A text file containing a comma separated list of the                        FASTQ files for sample_1. If using paired reads the                        format is ":" to separate pairs and "," to separate                        replicates. (Only if using fastq)  --s2 S2               A text file containing a comma separated list of the                        FASTQ files for sample_2. If using paired reads the                        format is ":" to separate pairs and "," to separate                        replicates. (Only if using fastq)  --od OD               The directory for final output from the post step  --tmp TMP             The directory for intermediate output such as ".rmats"                        files from the prep step  -t {paired,single}    Type of read used in the analysis: either "paired" for                        paired-end data or "single" for single-end data.                        Default: paired  --libType {fr-unstranded,fr-firststrand,fr-secondstrand}                        Library type. Use fr-firststrand or fr-secondstrand                        for strand-specific data. Default: fr-unstranded  --readLength READLENGTH                        The length of each read  --variable-read-length                        Allow reads with lengths that differ from --readLength                        to be processed. --readLength will still be used to                        determine IncFormLen and SkipFormLen  --anchorLength ANCHORLENGTH                        The anchor length. Default is 1  --tophatAnchor TOPHATANCHOR                        The "anchor length" or "overhang length" used in the                        aligner. At least "anchor length" NT must be mapped to                        each end of a given junction. The default is 6. (Only                        if using fastq)  --bi BINDEX           The directory name of the STAR binary indices (name of                        the directory that contains the SA file). (Only if                        using fastq)  --nthread NTHREAD     The number of threads. The optimal number of threads                        should be equal to the number of CPU cores. Default: 1  --tstat TSTAT         The number of threads for the statistical model. If                        not set then the value of --nthread is used  --cstat CSTAT         The cutoff splicing difference. The cutoff used in the                        null hypothesis test for differential splicing. The                        default is 0.0001 for 0.01% difference. Valid: 0 <=                        cutoff < 1. Does not apply to the paired stats model  --task {prep,post,both,inte,stat}                        Specify which step(s) of rMATS to run. Default: both.                        prep: preprocess BAMs and generate a .rmats file.                        post: load .rmats file(s) into memory, detect and                        count alternative splicing events, and calculate P                        value (if not --statoff). both: prep + post. inte                        (integrity): check that the BAM filenames recorded by                        the prep task(s) match the BAM filenames for the                        current command line. stat: run statistical test on                        existing output files  --statoff             Skip the statistical analysis  --paired-stats        Use the paired stats model  --novelSS             Enable detection of novel splice sites (unannotated                        splice sites). Default is no detection of novel splice                        sites  --mil MIL             Minimum Intron Length. Only impacts --novelSS                        behavior. Default: 50  --mel MEL             Maximum Exon Length. Only impacts --novelSS behavior.                        Default: 500  --allow-clipping      Allow alignments with soft or hard clipping to be used  --fixed-event-set FIXED_EVENT_SET                        A directory containing fromGTF.[AS].txt files to be                        used instead of detecting a new set of events
```

五、输出文件

每一种可变剪切事件(alternative splicing event, AS_Event)会存放在一定的输出文件中，例如skipped exon(SE), mutually exclusive exons(MXE)，alternative 3' splice site (A3SS), alternative 5' splice site (A5SS), retained intron (RI)等均会有自己的命名，但似乎没有提到可变启动子与可变终止子。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwHYwad8w124lUZprOKNfnM1XVtLbTrFRq9uYxK55coQuibqlpOxd7WUEY6nvFSZkFgkjJYDflaIQw/640?wx_fmt=png&from=appmsg)

示意图为：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwHYwad8w124lUZprOKNfnMfCL0aAmVc0hozpcAsSxo4UtvQgLwcEXReFLspXubNdWFzCEq1T7w0A/640?wx_fmt=png&from=appmsg)

每个文件对应关系为：

\--od contains the final output files from the post step:

  * [AS_Event].MATS.JC.txt: Final output including only reads that span junctions defined by rmats (Junction Counts)
  * [AS_Event].MATS.JCEC.txt: Final output including both reads that span junctions defined by rmats (Junction Counts) and reads that do not cross an exon boundary (Exon Counts)
  * fromGTF.[AS_Event].txt: All identified alternative splicing (AS) events derived from GTF and RNA
  * fromGTF.novelJunction.[AS_Event].txt: Alternative splicing (AS) events which were identified only after considering the RNA (as opposed to analyzing the GTF in isolation). This does not include events with an unannotated splice site.
  * fromGTF.novelSpliceSite.[AS_Event].txt: This file contains only those events which include an unannotated splice site. Only relevant if \--novelSS is enabled.
  * JC.raw.input.[AS_Event].txt: Event counts including only reads that span junctions defined by rmats (Junction Counts)
  * JCEC.raw.input.[AS_Event].txt: Event counts including both reads that span junctions defined by rmats (Junction Counts) and reads that do not cross an exon boundary (Exon Counts)

输出文件一般包含以下几列：

  * ID: rMATS event id
  * GeneID: Gene id
  * geneSymbol: Gene name
  * chr: Chromosome
  * strand: Strand of the gene
  * IJC_SAMPLE_1: Inclusion counts for sample 1. Replicates are comma separated
  * SJC_SAMPLE_1: Skipping counts for sample 1. Replicates are comma separated
  * IJC_SAMPLE_2: Inclusion counts for sample 2. Replicates are comma separated
  * SJC_SAMPLE_2: Skipping counts for sample 2. Replicates are comma separated
  * IncFormLen: Length of inclusion form, used for normalization（比如用于TPM与FPKM的计算）
  * SkipFormLen: Length of skipping form, used for normalization
  * PValue: Significance of splicing difference between the two sample groups. (Only available if the statistical model is on)
  * FDR: False Discovery Rate calculated from p-value. (Only available if statistical model is on)
  * IncLevel1: Inclusion level for sample 1. Replicates are comma separated. Calculated from normalized counts
  * IncLevel2: Inclusion level for sample 2. Replicates are comma separated. Calculated from normalized counts
  * IncLevelDifference: average(IncLevel1) - average(IncLevel2)

不同的剪切形式也会包含一些特殊的“列”：

  * SE: exonStart_0baseexonEndupstreamESupstreamEEdownstreamESdownstreamEE

      * The inclusion form includes the target exon (exonStart_0base, exonEnd)

    * MXE: 1stExonStart_0base1stExonEnd2ndExonStart_0base2ndExonEndupstreamESupstreamEEdownstreamESdownstreamEE

      * If the strand is + then the inclusion form includes the 1st exon (1stExonStart_0base, 1stExonEnd) and skips the 2nd exon
      * If the strand is - then the inclusion form includes the 2nd exon (2ndExonStart_0base, 2ndExonEnd) and skips the 1st exon

    * A3SS,A5SS: longExonStart_0baselongExonEndshortESshortEEflankingESflankingEE

      * The inclusion form includes the long exon (longExonStart_0base, longExonEnd) instead of the short exon (shortESshortEE)

    * RI: riExonStart_0baseriExonEndupstreamESupstreamEEdownstreamESdownstreamEE

      * The inclusion form includes (retains) the intron (upstreamEE, downstreamES)

  * summary.txt: Brief summary of all AS event types. Includes the total event counts and significant event counts. By default, events are counted as significant if FDR <= 0.05. The summary can be regenerated with different criteria by running rMATS_P/summary.py

\--tmp产生的中间文件一般分以下三类：

  *   *   *   *

```
--tmp contains the intermediate files generated by the prep step:{datetime}_{id}.rmats: Summary generated from processing a BAM{datetime}_bam{sample_num}_{replicate_num}/Aligned.sortedByCoord.out.bam: result of mapping input FASTQ files{datetime}_read_outcomes_by_bam.txt: Counts of the reads used from each BAM along with counts of the reasons that reads were not able to be used
```

运行结果提示：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
gtf: 12.340827226638794There are 42081 distinct gene ID in the gtf fileThere are 133556 distinct transcript ID in the gtf fileThere are 22653 one-transcript genes in the gtf fileThere are 1520735 exons in the gtf fileThere are 9656 one-exon transcripts in the gtf fileThere are 7737 one-transcript genes with only one exon in the transcriptAverage number of transcripts per gene is 3.173784Average number of exons per transcript is 11.386497Average number of exons per transcript excluding one-exon tx is 12.195956Average number of gene per geneGroup is 7.400260statistic: 0.03252887725830078read outcome totals across all BAMsUSED: 0NOT_PAIRED: 100541924NOT_NH_1: 106297216NOT_EXPECTED_CIGAR: 3511602NOT_EXPECTED_READ_LENGTH: 211435449NOT_EXPECTED_STRAND: 0EXON_NOT_MATCHED_TO_ANNOTATION: 0JUNCTION_NOT_MATCHED_TO_ANNOTATION: 0CLIPPED: 78046087total: 499832278outcomes by BAM written to: /RNA-Seq/06.alter.splice/tmp/2023-01-01-18_54_52_749622_read_outcomes_by_bam.txtnovel: 699.3913233280182The splicing graph and candidate read have been saved into /home/biomamba/analysis/WGBS.RNA-Seq/RNA-Seq/06.alter.splice/tmp/2023-01-01-18_54_52_749622_*.rmatssave: 0.0010285377502441406/RNA-Seq/03.sam.bam/sample2-3.sorted.bam found 2 times in .rmats files/RNA-Seq/03.sam.bam/sample4-3.sorted.bam found 2 times in .rmats files/RNA-Seq/03.sam.bam/sample2-2.sorted.bam found 2 times in .rmats files/RNA-Seq/03.sam.bam/sample-1.sorted.bam found 2 times in .rmats files/RNA-Seq/03.sam.bam/sample-3.sorted.bam found 2 times in .rmats files/RNA-Seq/03.sam.bam/sample45-1.sorted.bam found 2 times in .rmats files/RNA-Seq/03.sam.bam/sample8-3.sorted.bam found 2 times in .rmats files
```

六、可视化(rmats2sashimiplot)

显然我们通过上面的流程拿到.rmat的文件是并不能达到我们的目的，rmats2sashimiplot可以利用rMATS的输出结果依赖于MISO进行可视化。

5.1 依赖环境：

  * Python 2.7 (Python 3 can be used after running 2to3.sh)

  *

```
2to3 -w -n src
```

    * numpy
    * scipy
    * matplotlib
    * pysam

  * Samtools
  * bedtools

5.2 安装：

  *   *   *   *

```
cd /home/biomamba/biosoftwget https://github.com/Xinglab/rmats2sashimiplot/archive/refs/heads/master.zipunzip master.zipcd rmats2sashimiplot-master/
```

rmats2sasmimiplot不安装也可以运行：

  *

```
python ./src/rmats2sashimiplot/rmats2sashimiplot.py
```

可以如此安装：

  *

```
python ./setup.py install
```

更新：

  *   *

```bash
pip uninstall rmats2sashimiplotpython ./setup.py install
```

安装以后则可直接调用：

  *

```
安装以后则可直接调用：
```

所以还是推荐用conda安装一下：

  *   *   *

```
mamba install python==2.7mamba install rmats2sashimiplotconda install -c conda-forge ncurses
```

需要有gff3文件：

  *   *

```
gffread --keep-genes GCF_000001635.27_GRCm39_genomic.gff  \-o ./GCF_000001635.27_GRCm39_genomic.gff3
```

依赖包：

  *   *   *   *

```bash
pip install pysampip install matplotlibpip install matplotlib --upgrade --ignore-installed sixpip install scipy
```

5.3 使用：

sam文件：

  *   *   *   *   *

```
rmats2sashimiplot --s1 ./rmats2sashimiplot_test_data/sample_1_replicate_1.sam,./rmats2sashimiplot_test_data/sample_1_replicate_2.sam,./rmats2sashimiplot_test_data/sample_1_replicate_3.sam \--s2 ./rmats2sashimiplot_test_data/sample_2_replicate_1.sam,./rmats2sashimiplot_test_data/sample_2_replicate_2.sam,./rmats2sashimiplot_test_data/sample_2_replicate_3.sam \-t SE -e ./rmats2sashimiplot_test_data/SE.MATS.JC.txt \--l1 SampleOne --l2 SampleTwo \--exon_s 1 --intron_s 5 -o test_events_output
```

bam文件：

  *   *   *   *   *   *

```
rmats2sashimiplot --b1 ./rmats2sashimiplot_test_data/sample_1_replicate_1.bam,./rmats2sashimiplot_test_data/sample_1_replicate_2.bam,./rmats2sashimiplot_test_data/sample_1_replicate_3.bam \--b2 ./rmats2sashimiplot_test_data/sample_2_replicate_1.bam,./rmats2sashimiplot_test_data/sample_2_replicate_2.bam,./rmats2sashimiplot_test_data/sample_2_replicate_3.bam \-c chr16:+:9000:25000:./rmats2sashimiplot_test_data/annotation.gff3 \--l1 SampleOne --l2 SampleTwo --exon_s 1 --intron_s 5 \-o test_coordinate_output#b1和b2需要直接给路径，不可给txt文件
```

5.4 组间差异：

  *   *   *   *   *

```
rmats2sashimiplot --b1 ./rmats2sashimiplot_test_data/sample_1_replicate_1.bam,./rmats2sashimiplot_test_data/sample_1_replicate_2.bam,./rmats2sashimiplot_test_data/sample_1_replicate_3.bam \--b2 ./rmats2sashimiplot_test_data/sample_2_replicate_1.bam,./rmats2sashimiplot_test_data/sample_2_replicate_2.bam,./rmats2sashimiplot_test_data/sample_2_replicate_3.bam \-t SE -e ./rmats2sashimiplot_test_data/SE.MATS.JC.txt \--l1 SampleOne --l2 SampleTwo --exon_s 1 --intron_s 5 \-o test_grouped_output --group-info grouping.gf
```

分组文件每行的格式为：

  *

```
groupname: indices of mapping files
```

indices可以用,分割，并且可以是固定的单个数字或者是一个范围，比如：1-3，数字按b1至b2的顺序排开

比如\--b1 a.bam,b.bam,c.bam --b2 d.bam,e.bam,f.bam 的groupfile可以是：

  *   *

```
firstGroup: 1-3 #对应 a.bam,b.bam,c.bam secondGroup: 4-6 #对应 d.bam,e.bam,f.bam
```

绘制出的图纵坐标是RPKM，这是一种用于单端测序的值，不是很推荐，后面想办法转化一下。

gff3文件可以如是获得：

  *

```
gffread --keep-genes ./some_file.gtf -o ./some_file.gff3
```

rmats2sashimiplot只可以单线程运行，但是可以自行拆分命令达到多线程运行的效果。-e可以绘制指定文件(例如SE.MATS.JC.txt)包含的所有alternative splicing event，你也可以过滤这一文件绘制部分event。

获取帮助文档：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
                python src/rmats2sashimiplot/rmats2sashimiplot.py -husage: rmats2sashimiplot [-h] -o OUT_DIR [--l1 L1] [--l2 L2]                         [-t {SE,A5SS,A3SS,MXE,RI}] [-e EVENTS_FILE]                         [-c COORDINATE] [--s1 S1] [--s2 S2] [--b1 B1]                         [--b2 B2] [--exon_s EXON_S] [--intron_s INTRON_S]                         [--group-info GROUP_INFO] [--min-counts MIN_COUNTS]                         [--color COLOR] [--font-size FONT_SIZE]                         [--hide-number] [--no-text-background]                         [--keep-event-chr-prefix] [--remove-event-chr-prefix]optional arguments:  -h, --help            show this help message and exitRequired:  -o OUT_DIR            The output directory.Labels:  --l1 L1               The label for the first sample.  --l2 L2               The label for the second sample.rMATS event input:  Use either (rMATS event input) or (Coordinate and annotation input)  -t {SE,A5SS,A3SS,MXE,RI}                        Type of event from rMATS result used in the analysis.                        'SE': skipped exon, 'A5SS': alternative 5' splice                        site, 'A3SS' alternative 3' splice site, 'MXE':                        mutually exclusive exons, 'RI': retained intron. (Only                        if using rMATS event input)  -e EVENTS_FILE        The rMATS output event file (Only if using rMATS event                        input)Coordinate and annotation input:  Use either (Coordinate and annotation input) or (rMATS event input)  -c COORDINATE         The genome region coordinates and a GFF3 (not GTF)                        annotation file of genes and transcripts. The format                        is -c                        {chromosome}:{strand}:{start}:{end}:{/path/to/gff3}                        (Only if using Coordinate and annotation input)SAM Files:  Mapping results for sample_1 & sample_2 in SAM format. Replicates must be  in a comma separated list. (Only if using SAM)  --s1 S1               sample_1 sam files: s1_rep1.sam[,s1_rep2.sam]  --s2 S2               sample_2 sam files: s2_rep1.sam[,s2_rep2.sam]BAM Files:  Mapping results for sample_1 & sample_2 in BAM format. Replicates must be  in a comma separated list. (Only if using BAM)  --b1 B1               sample_1 bam files: s1_rep1.bam[,s1_rep2.bam]  --b2 B2               sample_2 bam files: s2_rep1.bam[,s2_rep2.bam]Optional:  --exon_s EXON_S       How much to scale down exons. Default: 1  --intron_s INTRON_S   How much to scale down introns. For example,                        --intron_s 5 results in an intron with real length of                        100 being plotted as 100/5 = 20. Default: 1  --group-info GROUP_INFO                        The path to a *.gf file which groups the replicates.                        One sashimi plot will be generated for each group                        instead of the default behavior of one plot per                        replicate  --min-counts MIN_COUNTS                        Individual junctions with read count below --min-                        counts will be omitted from the plot. Default: 0  --color COLOR         Specify a list of colors with one color per plot.                        Without grouping there is one plot per replicate. With                        grouping there is one plot per group: --color                        '#CC0011[,#FF8800]'  --font-size FONT_SIZE                        Set the font size. Default: 8  --hide-number         Do not display the read count on the junctions  --no-text-background  Do not put a white box behind the junction read count  --keep-event-chr-prefix                        force the contig name in the provided events file to                        be used  --remove-event-chr-prefix                        remove any leading "chr" from contig names in the                        provided events file
```

输出：

通过-o指定一个文件夹进行文件输出

  * Sashimi_index/: contains intermediate files used to create the plot
  * Sashimi_index_{Gene}_{event_id}/: like Sashimi_index/ but one directory for each rMATS event plotted
  * Sashimi_plot/: contains the generated sashimi plots in .pdf format

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528482&idx=1&sn=7cc0715eace4f592a62bdaf157b25c01&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
