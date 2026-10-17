---
title: "基于SpliceAI的TCGA-LIHC体细胞突变剪接效应预测"
date: 2026-10-13
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247543076&idx=1&sn=f4154bf4816cf4c05d17764c03ad1ac4&chksm=9b3c5074ac4bd9623d43ec9a45711602efa4a15054b497212d6241082913f44c15d0c18f85db#rd
albums: ["Bulk RNA-seq"]
---

# 基于SpliceAI的TCGA-LIHC体细胞突变剪接效应预测

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247543076&idx=1&sn=f4154bf4816cf4c05d17764c03ad1ac4&chksm=9b3c5074ac4bd9623d43ec9a45711602efa4a15054b497212d6241082913f44c15d0c18f85db#rd
> 合集：Bulk RNA-seq

**一、写在前面**

> 运行说明：本文档为教学型实操流程文档。第 3–5 节的代码需在具备数据与运行环境的服务器终端或 RStudio 中按序执行，大家可参考给出代码，将数据路径修改为自己的实际路径， 其中标注“(终端执行)”的命令不参与 Knit；其余 R 代码块在数据就绪后可执行复现。第 6 节结果表为既往一次运行的真实输出，可作为复现结果的对照。

1 分析概述

1.1 研究背景

肝细胞[肝癌](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529253&idx=1&sn=136209939b24c9b3508da46dd364c15a&scene=21#wechat_redirect>)（LIHC）的发生发展与体细胞基因突变密切相关。现有肿瘤基因组分析多聚焦于突变对蛋白编码序列的改变（错义、无义突变等）；然而，大量位于编码区及邻近区域的单碱基突变可通过破坏或新增mRNA剪接位点，造成外显子跳跃、内含子滞留及异常剪接转录本的产生，最终导致基因功能紊乱。此类剪接层面的变异效应在常规突变注释中易被忽略。因此，系统性预测肝癌体细胞突变的剪接扰动效应，对补充肿瘤突变致病机制、挖掘潜在功能性突变具有重要意义。

1.2 工具介绍

SpliceAI是一款基于深度神经网络的剪接变异预测工具，用于评估单碱基突变对人类mRNA剪接模式的影响。该工具依托大规模基因组与转录组数据训练，可基于局部DNA序列特征，定量预测突变对剪接供体、剪接受体位点的扰动强度，已广泛应用于肿瘤及遗传病的功能性突变注释。本研究采用 [GPU 加速](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529437&idx=1&sn=1f8f39ba2ae063e1e0ec6646cebf2d2d&scene=21#wechat_redirect>)模式完成大批量突变位点的预测。

设备受限的同学可参考：[AI时代人人都在写代码，但是你有设备去运行代码吗？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542152&idx=2&sn=7e7748b4a35a1c3cab4c2e9df21d3da9&scene=21#wechat_redirect>)

1.3 基本原理

SpliceAI 采用基于序列对比的[深度学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507794&idx=1&sn=c70dd03a962adb3f3b92ffed47e978bb&scene=21#wechat_redirect>)预测方法：输入突变位点上下游参考基因组序列与突变后序列，经神经网络模型评估突变是否改变原有剪接位点，或产生新的剪接位点，最终输出4项取值区间为0–1的剪接损伤分值（DS 值）：

  * DS_AG：突变产生新的剪接受体位点；

  * DS_AL：突变破坏原有剪接受体位点；

  * DS_DG：突变产生新的剪接供体位点；

  * DS_DL：突变破坏原有剪接供体位点。

本研究取四项分值的最大值DS_max作为综合剪接损伤指标，以领域通用阈值DS_max ≥ 0.5判定该突变具有潜在高剪接破坏效应，可能引起异常mRNA剪接。需说明的是，上述结果均为算法预测，须经[转录组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541362&idx=1&sn=aa987d7569fa3892a65adb616fe9a73e&scene=21#wechat_redirect>)数据或实验验证后方可确认。

1.4 整体分析流程

本研究基于TCGA-LIHC体细胞突变数据，完成从数据预处理、剪接预测、结果解析到队列统计的全部分析，具体步骤如下：

① 数据获取：从UCSC Xena数据库下载TCGA-LIHC体细胞突变TSV表格，数据包含肿瘤样本突变位点、基因注释、样本条形码等信息，同时包含SNP与INDEL变异。

② 数据预处理与VCF构建：在R中对原始突变数据清洗，过滤全部INDEL变异，仅保留单碱基SNP；去除染色体 “chr” 前缀，使其与GRCh38参考基因组命名规范一致；构建满足SpliceAI运行要求的简易VCF文件作为预测输入。

③环境搭建与GPU加速配置：构建Python 3.8专属[conda](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530994&idx=2&sn=3f3bdf2d06532c0b0ab8c9a477b8332c&scene=21#wechat_redirect>)环境，安装SpliceAI及适配版本的TensorFlow；解决服务器高版本驱动与旧版本TensorFlow的兼容问题，通过配置动态库搜索路径（LD_LIBRARY_PATH）启用GPU加速，并依托[tmux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528249&idx=2&sn=a3603d5ef77ae9aceb181e59d8b067ff&scene=21#wechat_redirect>)实现后台稳定运行。

④ SpliceAI批量[剪接预测](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539292&idx=1&sn=b8f548af5e7b50fb73fea214e236736e&scene=21#wechat_redirect>)：基于GRCh38参考基因组完成全部SNP位点的剪接效应预测，输出携带剪接分值信息的结果VCF；运行过程中自动过滤格式异常的残留INDEL位点，属预期现象。

⑤ 结果解析与样本关联：在R中读取输出VCF，提取四项剪接分值并计算 DS_max；通过“染色体–位置–参考碱基–突变碱基”唯一键值与原始样本信息匹配，完成突变位点与肿瘤样本、对应基因的关联注释。

⑥ 统计分析与结果汇总：区分“突变–样本事件”与“独立突变位点”双统计口径，筛选高剪接破坏性变异，统计携带高风险突变的肿瘤样本数量，汇总高频受扰动基因，完成TCGA-LIHC队列剪接突变特征的初步分析。

2 运行环境配置

2.1 硬件环境

本分析的全部剪接预测运算部署于Linux远程服务器。服务器搭载NVIDIA RTX 3080 GPU，支持CUDA并行加速，可满足大批量突变位点的预测需求；配备大容量内存与多核CPU，保障基因组数据读写与批量运算稳定执行。任务全程通过SS 远程操作，并采用tmux虚拟终端会话维持后台进程，避免SSH断开导致运算中断。

[不推荐用自己的电脑做生信](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533659&idx=2&sn=8e7b9243228fa6531fb7549399f21d95&scene=21#wechat_redirect>)，不想让自己电脑负重前行的同学，也可以看看服务器处理数据的优势，按需选用适合自己的计算资源：

共享(经济实惠)：[有root权限的共享服务器,报我名字立减200￥](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532797&idx=2&sn=1ee326256c4a818e2d9c563e6d3ea28d&scene=21#wechat_redirect>)

独享(省电省心)：[生信分析不求人](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

更多内容可咨询客服微信[**Biomamba_zhushou**]

2.2 系统与环境管理

采用Miniconda3实现项目环境隔离，独立构建专属运行环境，以避免系统软件与多项目依赖间的版本冲突。依据SpliceAI及配套深度学习框架的兼容要求，选用[Python](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537399&idx=1&sn=d14c7987d1384fe133094748844b8d59&scene=21#wechat_redirect>)3.8构建运算环境，单独创建并激活spliceai_env专用分析环境，所有预测相关依赖均在此独立环境中安装与运行。

2.3 核心软件与依赖配置

本分析核心依赖剪接预测工具与深度学习框架，需严格匹配兼容版本：安装 SpliceAI 主程序用于突变剪接效应预测，配套安装TensorFlow 2.10与Keras 2.4.3稳定版本。

服务器存在高版本NVIDIA驱动与低版本TensorFlow、CUDA库不兼容的问题，默认状态下无法识别GPU，仅能低速运行于CPU。通过手动配置动态链接库环境变量LD_LIBRARY_PATH，将conda内置CUDA库纳入系统搜索路径，可激活GPU加速。该环境变量为会话级配置，每次新建终端或tmux会话后均需重新设置。

2.4 参考基因组

采用Samtools对GRCh38 primary_assembly参考基因组构建索引文件（.fa.fai），供SpliceAI快速读取局部基因组序列。构建索引过程中出现的ncurses库版本兼容性警告由系统库与conda库版本差异所致，不影响索引生成。

参考基因组采用GRCh38 primary_assembly标准版本，可保证突变位点坐标匹配、序列读取准确，符合[TCGA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539068&idx=1&sn=2acad38f76a1e54c9d9d4318d2d08a7e&scene=21#wechat_redirect>)数据集基因组注释标准。

2.5 数据分析环境

数据预处理、VCF文件构建、预测结果解析、样本注释关联与统计分析均在[RStudio Server](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247524106&idx=1&sn=f23405302a3705007d33b688870196e0&scene=21#wechat_redirect>)中完成，基于[tidyverse](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531327&idx=1&sn=f798dffbab0f5ba51fae3433dbcf1b31&scene=21#wechat_redirect>)工具包实现数据清洗、字段拆分、表格匹配与批量统计。

**二、实战内容
**

1 数据获取

1.1 数据来源

本研究的LIHC体细胞突变数据取自UCSC Xena数据库的公开TCGA数据集，采用经过统一质控与去冗余的体细胞突变数据集TCGA-LIHC.somaticmutation_wxs.tsv。该数据集包含全外显子测序得到的全部体细胞SNP与小片段INDEL变异，并记录突变位点坐标、参考碱基、突变碱基、对应基因及肿瘤样本条形码（Tumor_Sample_Barcode），为本次剪接效应分析的原始数据源。

1.2 数据下载与解压

数据下载与存储均在[Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)服务器终端完成，统一存放于项目数据目录，以保证路径规范、结果可复现。

  *   *   *   *   *   *   *   *

```
# 切换至项目数据目录cd ~/LIHC_data/ESV_data# 下载 TCGA-LIHC 体细胞突变数据集wget https://gdc-hub.s3.us-east-1.amazonaws.com/download/TCGA-LIHC.somaticmutation_wxs.tsv.gz# 解压原始 TSV 文件gunzip TCGA-LIHC.somaticmutation_wxs.tsv.gz# 校验文件完整性head -5 TCGA-LIHC.somaticmutation_wxs.tsv
```

2 数据处理

2.1 处理目的

原始TCGA-LIHC体细胞突变数据为TSV表格格式，包含大量INDEL变异与格式不规范位点，无法直接用于SpliceAI剪接预测。SpliceAI仅支持标准VCF格式输入，无法直接读取TSV表格，且其对INDEL变异兼容性较差，运行时会自动跳过绝大多数插入缺失位点。因此需统一数据格式、过滤无效变异、校正基因组坐标，最终生成合规的VCF文件。

2.2 处理内容

本阶段处理主要包括三步：变异筛选、坐标格式校正、TSV转VCF结构化重建。

① 变异筛选（仅保留单碱基SNP）：SpliceAI无法识别不规范的插入缺失位点，运行时会自动跳过并提示。本研究统一剔除全部INDEL，仅保留ref与alt均为单碱基的SNP变异。

② 基因组命名统一：Xena原始数据染色体名称带有chr前缀，而所采用的GRCh38参考基因组无该前缀。为保证位点序列匹配成功，统一去除前缀，使突变坐标与参考基因组完全对齐。

③ 简易VCF重建：基于原始突变坐标手动重构标准VCF四元组（CHROM、POS、REF、ALT），其余非必要字段填充缺失值，生成满足预测最低标准的简易VCF文件。

2.3 处理代码

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library(tidyverse)# 设置工作目录setwd("/home/cheemsyu/LIHC_data/ESV_data")# 读取原始突变数据mut_df <- read_tsv("TCGA-LIHC.somaticmutation_wxs.tsv")# 1. 筛选有效 SNP，剔除全部 INDELsnp_only <- mut_df %>%filter(str_length(ref) == 1,str_length(alt) == 1)# 2. 统一染色体命名（去除 chr 前缀）snp_only <- snp_only %>%mutate(chrom = str_remove(chrom, "^chr"))# 3. 构建简易 VCF 输入文件vcf_input <- snp_only %>%select(chrom, start, ref, alt) %>%mutate(ID = ".",QUAL = ".",FILTER = ".",INFO = ".",FORMAT = ".",SAMPLE = ".") %>%rename(`#CHROM` = chrom,POS = start,REF = ref,ALT = alt)# 输出 SpliceAI 预测输入文件write_tsv(vcf_input, "lihc_snp_only.vcf", na = ".")
```

向下滑动查看全部~

2.4 处理后数据特征

处理完成后得到lihc_snp_only.vcf，作为SpliceAI的唯一输入文件，具有以下特征：

  * 仅包含单碱基体细胞SNP，无INDEL干扰；

  * 染色体坐标与GRCh38参考基因组一致；

  * 结构简洁，满足SpliceAI批量预测的输入要求。

需说明的是，该文件为人工构建的简易VCF，未包含完整VCF元注释头部；对SpliceAI预测运行无影响，但结果解析阶段需手动定义列名。

3 工具调用与分析过程

3.1 分析目的

在完成SNP简易VCF输入文件准备后，调用SpliceAI深度学习模型，依托GRCh38参考基因组提取突变上下游DNA序列，批量预测体细胞单碱基突变对mRNA剪接位点的扰动程度，得到每个变异的剪接损伤分值，为筛选肝癌潜在功能性突变提供定量预测结果。

3.2 运行前置条件

① 已进入tmux后台会话，防止SSH断开造成进程中断；

② spliceai_env conda环境已激活；

③ 参考基因组Homo_sapiens.GRCh38.dna.primary_assembly.fa 及对应的 .fa.fai 索引文件完整；

④ 输入文件lihc_snp_only.vcf预处理完成。

> 关键兼容说明：旧版本 TensorFlow 与服务器高版本 NVIDIA 驱动存在动态库不匹配，每次新建会话均需设置 LD_LIBRARY_PATH 环境变量以启用 GPU 加速，否则仅以 CPU 低速运行。

3.3 程序调用命令

  *   *   *   *   *   *   *   *   *   *

```
# 激活专用 conda 环境conda activate spliceai_env# 设置 conda 内部 CUDA 动态库搜索路径，启用 GPUexport LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH# SpliceAI 批量剪接预测主命令spliceai \-I /home/cheemsyu/LIHC_data/ESV_data/lihc_snp_only.vcf \-O /home/cheemsyu/SpliceAI/SpliceAI_out/lihc_spliceai_result.vcf \-R /home/cheemsyu/ref/GRCh38_ensembl/Homo_sapiens.GRCh38.dna.primary_assembly.fa \-A grch38
```

3.3.1 参数说明

参数| 说明
---|---
`-I`| 输入文件，预处理得到的简易 VCF，仅包含 SNP 变异
`-O`| 输出文件，存储携带 SpliceAI 打分的结果 VCF
`-R`| GRCh38 primary_assembly 参考基因组序列文件
`-A grch38`| 指定基因组注释版本，与参考基因组坐标体系一致

3.4 运行监控

监控命令可在新开终端执行，无需激活conda：

  *   *   *   *   *   *

```
# 查看 GPU 利用率，确认 GPU 正常工作nvidia-smi# 观察输出文件大小动态变化，判断任务是否仍在执行ls -lh /home/cheemsyu/SpliceAI/SpliceAI_out/lihc_spliceai_result.vcf# 统计已处理完成的变异记录行数grep -v "^##" /home/cheemsyu/SpliceAI/SpliceAI_out/lihc_spliceai_result.vcf | wc -l
```

3.5 运行过程中的正常提示

① WARNING:root:Skipping record (ref issue)：少数残留格式异常、非单碱基变异被程序自动跳过。本研究已提前过滤INDEL，该类记录占比很低，不影响SNP预测结果。

② WARNING:tensorflow:No training configuration found in save file：预训练模型仅保存权重、未保存训练配置。该警告仅与模型训练相关，推理预测不受影响，无需处理。

3.6 输出文件结构

输出VCF的INFO字段存储全部预测结果，包含4项剪接损伤分值DS_AG、DS_AL、DS_DG、DS_DL及对应的位置信息DP。后续取四项DS的最大值 DS_max作为综合剪接损伤指标，并以DS_max ≥ 0.5作为潜在高剪接破坏性变异的筛选阈值。

3.7 任务完成判断

① 终端返回命令提示符，不再持续打印日志；

② 通过nvidia-smi观察该任务GPU占用降为0；

③ 输出VCF文件大小不再增长。

4 结果展示与解读

4.1 分析目的

SpliceAI输出为VCF格式文件，仅存储每个变异位点的剪接预测分值，不携带样本与基因注释信息。本阶段在[R](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535038&idx=2&sn=717a8673a8bf82d5ac40af4441a07f65&scene=21#wechat_redirect>)中解析输出VCF，提取剪接打分，并与原始Xena突变表关联，将样本条形码、基因名称等注释挂接至每条预测结果；基于DS_max ≥ 0.5筛选潜在高剪接破坏性突变，完成队列层面的统计描述。

4.2 输入文件

文件| 说明
---|---
`lihc_spliceai_result.vcf`| SpliceAI 预测输出结果，INFO 字段携带 4 项 DS 剪接分值
`TCGA-LIHC.somaticmutation_wxs.tsv`| 原始 Xena 突变表，包含样本条形码、基因名、变异坐标等注释

由于输出VCF缺少完整头部元信息，R读取时不可使用自动表头识别，需手动指定全部列名。

4.3 结果解析与关联代码

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library(tidyverse)# 设置工作目录setwd("/home/cheemsyu/SpliceAI/SpliceAI_out")# 1. 读取 SpliceAI 输出 VCF，手动指定标准 VCF 列名vcf_res <- read_tsv("lihc_spliceai_result.vcf",comment = "##",header = FALSE,col_names = c("#CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO","FORMAT","SAMPLE"))# 2. 从 INFO 字段提取 SpliceAI 打分字符串# INFO 格式示例：SpliceAI=DS_AG|DS_AL|DS_DG|DS_DL|DP_AG|DP_AL|DP_DG|DP_DLspliceai_raw <- vcf_res$INFO %>%str_extract("SpliceAI=[0-9|.]+") %>%str_remove("SpliceAI=")# 拆分 8 个数值字段score_df <- str_split_fixed(spliceai_raw, "\\|", n = 8) %>% as.data.frame()colnames(score_df) <- c("DS_AG","DS_AL","DS_DG","DS_DL","DP_AG","DP_AL","DP_DG","DP_DL")# 转换为数值型，计算综合得分 DS_maxscore_df <- score_df %>%mutate(across(everything(), as.numeric)) %>%mutate(DS_max = pmax(DS_AG, DS_AL, DS_DG, DS_DL))# 合并坐标与打分res_coordinate <- vcf_res %>%select(`#CHROM`, POS, REF, ALT) %>%bind_cols(score_df) %>%rename(chrom = `#CHROM`)# 3. 读取原始突变表，用于关联样本与基因信息setwd("/home/cheemsyu/LIHC_data/ESV_data")original_mut <- read_tsv("TCGA-LIHC.somaticmutation_wxs.tsv") %>%filter(str_length(ref)==1, str_length(alt)==1) %>%mutate(chrom = str_remove(chrom,"^chr"))# 构建匹配键：chrom:start:ref:altres_coordinate <- res_coordinate %>%mutate(key = str_c(chrom,":",POS,":",REF,":",ALT))original_mut <- original_mut %>%mutate(key = str_c(chrom,":",start,":",ref,":",alt))# 表连接：同一突变可出现在多个肿瘤样本（many-to-many）final_result <- inner_join(res_coordinate,original_mut,by = "key",relationship = "many-to-many")# 4. 筛选潜在高剪接破坏性变异 DS_max >= 0.5high_risk_splice <- final_result %>%filter(DS_max >= 0.5)# 输出结果表格write_tsv(final_result, "spliceai_all_result.tsv")write_tsv(high_risk_splice, "spliceai_highrisk.tsv")
```

向下滑动查看全部~

4.4 统计口径说明

两个统计口径需严格区分，以避免结果误读：

统计口径| 定义
---|---
突变–样本事件| 不去重，同一突变发生于多名患者时多次计数，反映事件在队列中的发生频次
独立突变位点| 按 chrom:POS:REF:ALT 去重，代表基因组上不同的变异位置

4.5 队列统计结果

统计指标| 数值| 含义
---|---|---
全部有效突变–样本事件| 40,247| SNP 预测结果与样本信息成功匹配的总记录数
高剪接破坏性事件（DS_max ≥ 0.5）| 701| 样本–突变层面，预测会显著破坏剪接的事件数
去重独立高风险 SNP 位点| 654| 互不重复的高风险突变位点总数
携带高风险突变的肿瘤样本| 260| 至少携带 1 处高剪接破坏性 SNP 的肿瘤样本数

TCGA-LIHC队列纳入统计的肿瘤样本约374例，携带高风险突变的样本占比为260/374 ≈ 69.5%。该比例以纳入队列统计的肿瘤样本总数为分母，报告时应注明分母定义。

4.6 高频受影响基因

排名| 基因| 高剪接突变事件数| 生物学意义
---|---|---|---
1| TP53| 18| 肝癌核心抑癌基因，高频突变同时伴随剪接破坏效应
2| ADAM28| 9| 金属蛋白酶，参与细胞黏附与肿瘤微环境
3| NUP133| 9| 核孔复合体组分，核转运异常与肿瘤相关
4| PSD3| 9| 磷脂信号通路相关
5| CREB3L3| 6| 转录因子，肝脏代谢调控
6| AXIN1| 5| Wnt 通路关键抑癌基因，肝癌驱动基因
7| EPG5| 4| 自噬相关基因
8| RORA| 4| 核受体转录因子
9| RB1| 3| 经典抑癌基因
10| AKAP9| 2| A 激酶锚定蛋白

4.7 结果解读

① DS_max取值区间为0–1，数值越接近1，代表该变异对剪接位点扰动的模型预测置信度越高。

② DS_max ≥ 0.5为工具经验阈值，属计算预测结果，不等同于体内真实发生剪接异常。

③ TP53 居首（18 次事件）：TP53是肝细胞癌突变频率最高的抑癌基因。其大量体细胞SNP除改变蛋白氨基酸序列外，部分位点可能同时伴随剪接改变（如外显子跳跃、内含子滞留），此为常规突变注释（MAF）易忽略的层面；是否真实发生异常剪接仍需转录组验证。

④ AXIN1（5 次）：AXIN1为Wnt/β-catenin通路关键抑癌基因及肝癌驱动基因，其预测剪接破坏可能进一步加剧通路异常。

⑤ 高风险位点仅提示该突变有较高概率干扰mRNA剪接，后续需以[Bulk RNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529986&idx=2&sn=301d44caa8d63cba8243d13579775cf5&scene=21#wechat_redirect>)可变剪接数据或体外实验进一步验证。

5 局限性与后续分析

5.1 数据层面

① 原始数据来源于UCSC Xena处理后的TCGA-LIHC体细胞突变数据，并非GDC官方标准VCF；分析过程直接舍弃全部INDEL变异，仅对单碱基SNP开展剪接效应预测，插入缺失变异的剪接扰动未作评估。

② 输入为自制简易VCF，缺少完整VCF元注释，依赖坐标与碱基字符串进行表连接匹配，存在极低概率的匹配错误。

5.2 工具预测层面的局限

① SpliceAI属深度学习计算预测工具，DS_max ≥ 0.5为文献通用经验阈值，仅代表序列层面的潜在剪接扰动，不等于肿瘤细胞内真实发生可变剪接异常，存在假阳性，不能直接等同于功能性突变。

② 模型仅依赖突变位点上下游DNA序列进行预测，不考虑基因表达量、染色质状态、RNA结合蛋白及其他顺式、反式调控因子等体内真实生物学环境。

③ 模型无法区分突变带来的具体剪接表型（外显子跳跃、内含子滞留、隐蔽剪接位点激活等），仅给出综合损伤分值。

5.3 队列与注释层面的局限

① 本研究仅有突变基因组数据，无配套的同一批样本转录组测序结果，无法直接验证预测所得的剪接异常是否真实存在。

② 仅分析肿瘤体细胞突变，未纳入胚系变异；未区分突变为驱动突变或乘客突变。

③ 统计仅描述突变–样本事件分布，未结合mRNA表达、蛋白表达及临床预后开展定量关联。

5.4 后续可进行的分析

5.4.1 [多组学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542028&idx=1&sn=3be4b95376e4468cfdda566e44f5f7d0&scene=21#wechat_redirect>)联合分析

① 转录组关联：利用TCGA-LIHC Bulk RNA-seq数据，比较携带高风险剪接突变的样本与其余样本的对应基因表达水平差异；进一步检测可变剪接事件，验证SpliceAI预测位点是否真实发生剪接异常。

② 蛋白表达：结合TCGA[蛋白组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541307&idx=1&sn=93379316e05539b26b3b29fcececbda9&scene=21#wechat_redirect>)数据，观察高剪接突变样本对应蛋白丰度是否改变。

③ 临床特征关联：将样本分为“携带高风险剪接SNP”与“无高风险剪接SNP”两组，比较两组的年龄、性别、肿瘤分级与分期等临床指标差异；绘制Kaplan–Meier生存曲线，探究潜在剪接破坏性突变与患者总生存期、无病生存期的关系。

5.4.2 基因与位点深度挖掘

① 聚焦高频基因（如TP53、AXIN1），统计同一基因内高风险剪接突变的位置分布，区分错义、同义突变中哪些同时附带剪接损伤效应，补充传统突变注释遗漏的功能信息。

② 筛选关键候选位点：挑选分值极高（DS_max接近1）且在多个样本中重复出现的突变，作为后续体外功能验证的候选位点。

6 附录

6.1 文件路径汇总

文件| 路径
---|---
原始突变数据| `~/LIHC_data/ESV_data/TCGA-LIHC.somaticmutation_wxs.tsv`
预处理后 SNP VCF| `~/LIHC_data/ESV_data/lihc_snp_only.vcf`
参考基因组| `~/ref/GRCh38_ensembl/Homo_sapiens.GRCh38.dna.primary_assembly.fa`
SpliceAI 输出| `~/SpliceAI/SpliceAI_out/lihc_spliceai_result.vcf`
全部结果表| `spliceai_all_result.tsv`
高风险结果表| `spliceai_highrisk.tsv`

6.2 软件与依赖包版本信息

6.2.1 服务器系统

  * 操作系统：Ubuntu 20.04

  * GPU：NVIDIA RTX 3080

6.2.2 Conda 环境 spliceai_env

软件 / 包| 版本| 用途
---|---|---
python| 3.8| 基础运行环境
spliceai| 1.3| 剪接效应预测主程序
tensorflow| 2.10| 深度学习推理框架
keras| 2.4.3| 深度学习依赖库
samtools| 1.15-1| 参考基因组索引构建

6.2.3 R 及 R 包（RStudio Server）

R 包| 版本| 用途
---|---|---
R| 4.x| 统计分析环境
tidyverse| 2.0.0| 数据清洗、表格处理、字符串拆分
readr| 2.x| TSV/VCF 文件读写
dplyr| 1.1.x| 数据筛选、表连接
tidyr| 1.3.x| 字段拆分处理

参考基因组版本：GRCh38 primary_assembly（Ensembl release-110）。

6.3 常见报错、警告与排查

6.3.1 SpliceAI 运行–GPU 相关

现象：GPU不工作，仅以CPU运行，速度较慢。

  * 原因：conda内部CUDA动态库未被系统识别，会话环境变量丢失。

  * 排查：每次新建 tmux 或终端会话后执行

  *

```
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH
```

  * 验证：通过nvidia-smi观察GPU利用率是否上升。

现象：WARNING:tensorflow:No training configuration found in save file。

  * 说明：预训练模型仅保存权重，该警告不影响推理预测，无需处理。

6.3.2 SpliceAI 运行–变异位点警告

现象：WARNING:root:Skipping record (ref issue)。

  * 原因：VCF中残留INDEL、碱基不匹配或染色体名称不一致的位点被程序跳过。

  * 排查：确认输入VCF染色体不带chr前缀，与参考基因组一致；预处理阶段已过滤INDEL，少量该警告属正常现象，不影响SNP结果。

6.3.3 服务器会话断开导致程序终止

现象：关闭SSH后SpliceAI进程直接退出。

  * 原因：前台进程依附于SSH会话，会话断开信号终止进程。

  * 处理：长时运算须在tmux会话内部运行。

  *   *   *

```
tmux new -s splice_run# 在 tmux 内部执行 spliceai 命令# 快捷键 Ctrl+b 后按 d 脱离会话；重新接入 tmux attach -t splice_run
```

6.3.4 samtools faidx 索引警告

现象：samtools运行输出libncursesw.so版本无版本信息警告。

  * 原因：conda库与系统库版本冲突，属动态库告警。

  * 排查：检查目录下是否生成 .fa.fai索引文件，生成成功即可忽略。

6.3.5 R 读取 VCF 文件出错

现象：读入VCF后列错乱、字段错位，打分提取失败。

  * 原因：自制简易 VCF 缺少完整元注释头部，自动识别表头失败。

  * 处理：设置comment = "##" 与header = FALSE，手动指定全部VCF列名，不可直接使用默认方式读取。

6.3.6 R 表连接匹配失败，大量 NA

现象：inner_join后结果行数很少，大量打分字段为NA。

  * 排查要点：染色体是否统一去除chr前缀；key拼接格式是否严格统一为 chrom:POS:REF:ALT；ref、alt碱基大小写是否一致；原始数据是否已提前过滤INDEL并仅保留SNP记录。

6.3.7 conda 安装软件包失败

现象：conda install samtools 提示包不存在。

  * 原因：默认defaults通道不包含部分生物信息学工具。

  * 处理：使用bioconda通道安装，或直接使用服务器预装的[samtools](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521633&idx=1&sn=c9560d3300419d2e339019ef47f7ef5c&scene=21#wechat_redirect>)。

6.3.8 wget下载 URL 解析失败

现象：wget报域名解析失败或链接乱码。

  * 原因：复制链接时带入全角破折号等非半角字符。

  * 排查：检查粘贴命令中的符号，统一使用英文半角符号。

Cheems Yu

![图片](../../images/cb4255ab8010219d.webp)

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

[IF=15，生信基地作为作者单位的第一篇SCI：计算机设计CLDN4导向肽载纳米气泡](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541821&idx=1&sn=27235b32dda0a46efa1df58ca6a0cdbd&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)
![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家一起讨论。![](../../images/fe8ecb8594a1f419.webp)![图片](../../images/acba43cb3408c3d0.webp)您点的每个赞和在看，我都认真当成了喜欢
