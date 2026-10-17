---
title: "CellCall怎么推断细胞通讯?从原理到实战一文讲透"
date: 2026-09-21
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542406&idx=1&sn=bfac7ba8d659b6c148b7659e86bed8e0&chksm=9b3c5fd6ac4bd6c0f2de30c877ee204af9323beaa23fb52f17682398f8b1fcdee90b435af9c6#rd
albums: ["单细胞教程全收录"]
---

# CellCall怎么推断细胞通讯?从原理到实战一文讲透

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542406&idx=1&sn=bfac7ba8d659b6c148b7659e86bed8e0&chksm=9b3c5fd6ac4bd6c0f2de30c877ee204af9323beaa23fb52f17682398f8b1fcdee90b435af9c6#rd
> 合集：单细胞教程全收录

**一、写在前面**

想象一个画面：[肿瘤微环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541389&idx=1&sn=16494f5727dcd7bf5f30038ec976d0f6&scene=21#wechat_redirect>)里，[巨噬细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529353&idx=2&sn=2dc1406e0d153849f4e23c1a80ed5697&scene=21#wechat_redirect>)正贴着T细胞“咬耳朵”。它一遍遍释放TGF-β信号，劝T细胞“放下武器”；而T细胞一旦被说服，杀伤功能就会下线，肿瘤便趁机逃逸。

这样的细胞对话，每天都在组织里上演成千上万次。问题是：当你手握一份单细胞表达矩阵时，要怎样才能发现这段“密谈”？又怎么证明，T细胞听完之后真的照做了？

过去，我们常用的工具只回答前半个问题。比如[CellChat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=2&sn=fb3e252d95ee8b50cd446e71335b1aa0&scene=21#wechat_redirect>)，通过匹配配体（Ligand）与受体（Receptor）的表达，可以告诉你“哪群细胞和哪群细胞在通话”——但它答不上来后半句：这通电话打完，对方家里到底发生了什么？

而今天要讲的CellCall，就是来补上这“后半句”的。它不只验证“电话是否打通”，还要顺着配体 → 受体 → 转录因子（TF）这条链，一路查进接收细胞的内部，确认信号是否真正改变了细胞状态。

一句话记住它的定位：CellChat关心“谁与谁通了电话”，[CellCall](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)还要追问“通话之后，对方家里发生了什么”。

更多单细胞教程：

[![图片](../../images/f4c854d9f5c132bd.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542360&idx=1&sn=75ec383953b51b543bbb02531ed173e7&scene=21#wechat_redirect>)

**二、 CellCall 的核心原理
**

### 1\. 学术解释版

#### 1.1 构建 L-R-TF 轴数据库

CellCall基于[KEGG](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504403&idx=7&sn=99c35dd1d7cf7ad20adf0898fa916c73&scene=21#wechat_redirect>) 通路数据库，将“细胞A分泌配体 → 细胞B受体结合 → 细胞内转录因子激活”这一完整信号传导过程作为一个整体（L-R-TF轴）来建模，构建L-R-TF轴数据库。

#### 1.2 综合评分模型

基于L-R-TF轴数据集，CellCall通过计算配体/受体的表达量与下游TF的活性，来推断[细胞间通讯](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535877&idx=4&sn=847ec896b51c5c1571e31a54f198ebc2&scene=21#wechat_redirect>)。

### 2\. 通俗解释版

#### 2.1 构建“L-R-TF”关系词典

我们以打电话做比喻。如果你只想查两个人的“通讯录”，你只需要知道谁有电话（受体），谁有手机（配体）。但CellCall觉得这不够，它要建一个“完整的通话记录档案”。

它去KEGG数据库里，把 “谁打电话（配体） ➔ 接电话的人（受体） ➔ 接完电话后，这个人去做了什么决定（[转录因子](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537055&idx=1&sn=170371b86b42d47373bf7f0500031f19&scene=21#wechat_redirect>)TF） ➔ 最终导致哪些基因表达（靶基因）” 这整条链条，作为预先构建好的一本“词典”存起来。

举个栗子：肿瘤微环境中，[巨噬细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528289&idx=1&sn=b56f00f3d8a4b152e54f3acd40aef21d&scene=21#wechat_redirect>)（Macrophage，细胞A） 和T细胞（T cell，细胞B） 在“聊天”。你想知道巨噬细胞是不是在通过某种信号抑制T细胞的杀伤功能。这些知识我们是提前知道的：巨噬细胞A高表达TGF-β（配体）；T细胞B表面高表达TGFBR2（受体）；配体-受体结合后，T细胞内部会激活SMAD3这个转录因子；如果T细胞里SMAD3下游的靶基因（比如FOXP3 ）也显著高表达，就说明这条信号轴是“真实打通”的。

所以，数据库里有一条记录是“TGF-β（配体） → TGFBR2（受体） → SMAD3（TF） → 激活 FOXP3（靶基因）”。CellCall建这个数据库的目的，就是让你在分析时，不需要自己去手动搜这些生物学知识，系统直接按图索骥。

#### 2.2 对照“L-R-TF”关系词典，给真实细胞“L-R-TF”打个综合分

有了上面的“词典”，CellCall现在要对你手里的数据（比如巨噬细胞和T细胞的表达矩阵）进行“打分”了。它的打分层级比别的工具要“苛刻”得多。

我们分三步来看打分是怎么算的：

**第一关（表面关：配体和受体是否配对）** ：巨噬细胞里TGF-β表达高不高？T细胞里的TGFBR2表达高不高？如果两者都很高，说明表面结合的可能性很大，先给一个基础分。

**第二关（内部关：TF是否真的激活）** ：接完信号后，T细胞内部的SMAD3（转录因子）真的被激活了吗？CellCall会去检查 T细胞里所有受SMAD3调控的靶基因（比如FOXP3）是否真的高表达。如果靶基因没动，说明信号被“拦截”了，内部没响，分数会被大幅扣减。

**最终得分** ：把配体表达量 × 受体表达量 × 转录因子的活性评分结合起来，算出一个最终的通讯分数。

**关键点** ：如果一个配体-受体对（L-R）表面表达很高，但下游的TF活性极低，CellCall就会认为这条信号通路“没有真正发挥作用”，最终得分会很低。反之，只有表面和内部都“真实打通”了，得分才会很高。

> 一句话理解原理：CellCall通过构建完整的 “配体-受体-转录因子”因果链条，并通过综合评分模型评估这条链条在实际数据中是否真的被激活。

**三、 CellCall 的分析步骤**

标准的 CellCall 分析流程通常包含以下几个关键步骤：

  1. 准备环境与加载数据：安装并加载cellcall,[ Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&scene=21#wechat_redirect>)等包，并准备表达矩阵（行=基因，列=细胞）。

  2. 创建 CellCall 对象：使用CreateNichConObject()函数创建S4对象，并在此设定[细胞类型注释](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&scene=21#wechat_redirect>)（names.field）、物种（Org）、数据来源（source）等参数。

  3. 计算通讯分数：核心步骤。使用TransCommuProfile()函数，通过整合配体-受体表达和TF活性，计算细胞间的通讯得分矩阵。

  4. 通路[富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541688&idx=1&sn=6f79a9bf31753a3da40279a5df3b45e4&scene=21#wechat_redirect>)：使用getHyperPathway()函数，对通讯活跃的细胞对进行超几何检验，识别在其中显著富集的KEGG通路。

  5. 结果可视化：利用丰富的图形功能展示结果，如[桑基图](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530369&idx=2&sn=2215cdfa7e0400bf487d60bca29ef377&scene=21#wechat_redirect>)（展示L-R-TF流）、气泡图（展示通路富集）、Circos圈图、山脊图等。

**四、 CellCall 的代码实战**

### 1\. 准备环境与加载数据

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
## 清空环境并加载包rm(list = ls())library(cellcall)library(stringr)library(ggalluvial)library(ggplot2)## 加载软件自带测试数据f.tmp <- system.file("extdata", "example_Data.Rdata", package="cellcall")load(f.tmp)# 检查数据格式（行=基因，列=细胞类型）dim(in.content)             # 查看维度in.content[1:4, 1:4]        # 查看前几行table(str_split(colnames(in.content), "_", simplify = T)[,2]) # 查看细胞类型
```

**目的** ：加载CellCall软件自带的示例数据，熟悉软件要求的输入格式。通常用于测试代码是否能跑通。

**输入** ：system.file("extdata", "example_Data.Rdata",) 获取的内置数据文件，其中包含变量 in.content。

**输出** ：一个名为 in.content 的数据框。注意格式：行名是基因，列名是“Barcode_细胞类型”。

我们来看看，输出数据长啥样~

![](../../images/fe32ff15f6351119.webp)

▲ 加载示例数据后，in.content 的维度与前几行视图

### 2\. 创建 CellCall 对象

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
## 创建 CellCall 对象（这里以人类 TPM 数据为例，使用默认参数）# 使用 CellCall 包的 CreateNichConObject 函数，创建 CellCall 分析专用的 S4 对象mt <- CreateNichConObject(  # 【输入数据】：行名为基因，列名为细胞的表达矩阵（通常是从单细胞对象提取的）  data = in.content,  # 【基因过滤】：一个基因至少要在 3 个细胞中表达（低表达基因会被过滤掉，减少计算量）  min.feature = 3,  # 【列名解析】：告诉软件，列名由两部分组成，第 2 部分是细胞类型。  # 例如列名 "1_ST"，用 "_" 拆分后，第一部分是 "1"（样本索引），第二部分是 "ST"（细胞类型）  names.field = 2,  names.delim = "_",   # 指定拆分列名的分隔符为下划线 "_"  # 【数据类型】：指定输入数据的标准化格式为 TPM（Transcripts Per Million，每百万转录本）  source = "TPM",  # 【缩放因子】：将原始读数标准化到每百万单位的系数（TPM 通常使用 10^6 作为分母基准）  scale.factor = 10^6,  # 【物种设置】：指定分析物种为人类（Homo sapiens），这决定了软件调用哪种 KEGG 通路数据库  Org = "Homo sapiens",  # 【项目名称】：给当前分析起个名字（会保存在对象中，方便溯源）  project = "Microenvironment")
```

向下滑动查看全部~

**目的** ：将整理好的表达矩阵打包成CellCall官方认可的S4数据结构（NichConObject），并写入样本来源、物种等分析元数据。

**输入** ：上述生成的表达矩阵 in.content。

**输出** ：一个命名为mt的CellCall专用对象。现在的mt数据是一个打包好的S4对象（包含[表达矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&scene=21#wechat_redirect>)、注释信息等）。

### 3\. 计算通讯分数

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 使用 CellCall 包的 TransCommuProfile 函数，进行核心的细胞通讯推断计算（约需 35 分钟至1小时）mt <- TransCommuProfile(  # 【输入对象】：上一步 CreateNichConObject 生成的 CellCall 专用对象  object = mt,  # 【TF靶基因筛选】：使用 Spearman 相关分析筛选 TF 与其靶基因的相关性显著性阈值。  # 调大（如0.1）：保留更多候选靶基因，TF活性计算更“宽容”，通讯信号更丰富（但可能有假阳性）。  pValueCor = 0.1,  # 【相关性强度阈值】：设定相关性的绝对值下限。  # 调低（如0.05）：允许更多弱相关的基因对进入计算，信号更丰富。  CorValue = 0.05,  # 【保留靶基因数量】：每个配体-受体对保留多少条相关性最强的靶基因。  # 调大（如2）：给每条信号轴留更多“证人”，下游激活评分更稳健。  topTargetCor = 2,  # 【多重检验校正阈值】：经过多重检验校正后的显著性 p 值阈值。  # 调大（如0.1）：允许更多结果通过显著性检验，找回被抑制的信号（适用于信号弱的数据）。  p.adjust = 0.1,  # 【统计量类型】：指定在计算过程中使用的统计量，这里表示使用中位数（更稳健）。  use.type = "median",  # 【细胞类型代表表达量】：一种细胞类型中代表该细胞类型的基因表达百分比。  # 调低（如0.8）：对基因表达的要求更宽松，更能捕捉稀有细胞群中的微弱信号。  probs = 0.8,  # 【下游激活方法】：评估给定配体-受体关系的所有规则的下游配体-受体激活。  # "weighted" 是默认值，表示加权计算；也可以选择 "max" 或 "mean"。  method = "weighted",  # 【核心参考数据】：布尔型参数，TRUE 表示将高置信度的核心参考 LR 数据纳入分析。  IS_core = TRUE,  # 【物种设置】：指定分析物种为人类（Homo sapiens），确保数据库匹配。  Org = 'Homo sapiens')
```

向下滑动查看全部~

计算完成后，可以查看对象里的多份关键结果：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 1. 查看原始表达矩阵（大表格，只取前5行和前5列）head(mt@data$count, n = 5)[, 1:5]# 2. 查看未取log的原始表达矩阵head(mt@data$withoutlog, n = 5)[, 1:5]# 3. 查看细胞类型的平均表达量（基因 × 细胞类型）head(mt@data$expr_mean, n = 5)# 4. 查看转录因子活性评分矩阵（TF × 细胞类型）head(mt@data$regulons_matrix, n = 5)# 5. 查看GSEA结果列表（只查看第一个细胞群的GSEA结果前5行）head(mt@data$gsea.list$ST@result, n = 5)# 6. 查看差异倍数列表（FC list，看前5行）head(mt@data$fc.list$ST, n = 5)# 7. 查看配体-受体通讯评分（最终核心成绩单，前5行）head(mt@data$expr_l_r_log2_scale, n = 5)# 8. 查看配体-受体到转录因子的KEGG通路距离（前5行，前8列）head(mt@data$DistanceKEGG, n = 5)[, 1:8]# 保存结果，防止下次重新计算（强烈建议执行）saveRDS(mt, "cellcall_test.rds")
```

向下滑动查看全部~

**目的** ：核心计算步骤。通过整合配体-受体（L-R）的表达和下游转录因子（TF）的活性，为每一对“发送细胞-接收细胞”计算通讯得分。

**输入** ：第二步创建的CellCall对象（mt 或 mt.new）。

**输出** ：计算好通讯分数的对象，并且会在对象内部新增一个expr_l_r_log2_scale数据框（包含所有配体-受体对在不同细胞对之间的评分）。

这一步，包含了 6 个计算步骤：

  * step1：compute means of gene
  * step2：filter tf-gene with correlation, then score regulons
  * step3：get distance between receptor and tf in pathway
  * step4：score downstream activation of ligand-receptor all regulons of given ligand-receptor relation (weighted, max, or mean)
  * step5：softmax for ligand
  * step6：score ligand-receptor relation (weighted, max, or mean)

这是这一步计算产生的最核心的数据结果，是CellCall经过前 6 步计算后，交出的“最终通讯得分成绩单”。

![](../../images/54097441fcf3dad9.webp)

▲ 成绩单局部：expr_l_r_log2_scale数据框（每行一条 L-R 信号轴，每列一个细胞对）

这张表格非常清晰，直接告诉你：“在哪些细胞对之间，通过哪些配体-受体对，通讯信号有多强。”

![](../../images/50abfe2f044622b2.webp)

#### 6 个计算步骤通俗解释（以下是假设，以统计结果为准）

CellCall 自带数据的 example_Data.Rdata 是一组睾丸组织的单细胞数据，包含的细胞类型是：ST（支持细胞）、SSC（精原干细胞）、SPGing（精原细胞增殖期）、SPGed（精原细胞减数分裂期）。

现在以 ST（支持细胞） ➔ SSC（精原干细胞）的通讯关系为例。我们将计算通讯分数的 6 个步骤，完整复盘一遍它们之间的通讯。

**第 1 步：算嗓门大小（compute means of gene）**

  * 在干什么：把支持细胞（ST）群里所有基因的表达量求个平均，把精原干细胞（SSC）群里所有基因的表达量也求个平均。
  * 具体例子：算出支持细胞里 TGFA（EGFR配体）平均表达量是10，精原干细胞里 EGFR（受体）平均表达量是8。
  * 通俗理解：先确认支持细胞“喊得够不够大声”（配体表达高不高），精原干细胞“耳朵灵不灵”（受体表达高不高）。

**第 2 步：看领导有没有干活（filter tf-gene with correlation, then score regulons）**

  * 在干什么：不看转录因子TF（比如 JUN 或 FOS）本身的表达量，而是用[GSEA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484175&idx=1&sn=3e45ad62b045a541874e5ae7ca03f849&scene=21#wechat_redirect>)算法看它下游的“靶基因”有没有被激活。
  * 具体例子：精原干细胞里有JUN这个转录因子。如果它的靶基因在精原干细胞里集体上调，说明JUN在“拼命干活”，活性很高，打90分。如果靶基因没动静，说明JUN在睡觉，活性只有10分。
  * 通俗理解：支持细胞打完电话后，精原干细胞内部的“领导”（TF）有没有真的去发号施令。

**第 3 步：查通话线路的跳数（get distance between receptor and tf in pathway）**

  * 在干什么：利用KEGG通路图，查一下从受体（EGFR）到转录因子（JUN），中间隔了几步。
  * 具体例子：查表发现：EGFR通过激活下游的ERK激酶，再直接激活JUN，中间隔了1级信号传递，距离是1（很近）。如果另一个通路中，受体要先激活A，A激活B，B才能激活TF（比如 MYC），那距离就是3（很远）。
  * 通俗理解：打电话时，是“直拨专线”快，还是“总机转分机再转分机”快？距离越近，信号越准、越强。

**第 4 步：算内部接听效率（score downstream activation of ligand-receptor）**

  * 在干什么：把第2步的“TF活性评分”和第3步的“通路距离”结合起来，算一下配体-受体信号在对方内部到底激活了多少。
  * 具体例子：因为EGFR和JUN距离很近（第3步得1分），同时JUN活性很高（第2步得90分），所以这条信号内部激活程度很高，综合得分95分。
  * 通俗理解：电话不仅接通了，而且接电话的人立刻就叫全公司的人行动起来了。

**第 5 步：调整嗓门大小（softmax for ligand）**

  * 在干什么：对配体表达量做数学归一化（softmax），防止某个高表达配体“喧宾夺主”。
  * 具体例子：支持细胞表达了几百种配体。如果TGFA表达量是10，而它旁边有另一个配体表达量是100，直接算的话，TGFA会被淹没。Softmax就是让支持细胞所有的配体站在一起，按比例重新排个“标准分贝”，大家都站在同一条起跑线上比。
  * 通俗理解：这叫“雨露均沾”，不能因为某个配体嗓门大，就只听到它的声音。

**第 6 步：算最终通话账单（score ligand-receptor relation）**

  * 在干什么：把前面5步攒下的所有分数综合起来，乘一乘、加一加（用 weighted、max 或 mean 方法），算出这条通路最终的通讯得分。
  * 具体例子：支持细胞表达了 TGFA（第1步高），精原干细胞有受体 EGFR（第1步高），内部 JUN 激活了（第2步高），距离近（第3步高），内部激活效率高（第4步高），配体归化后不被淹没（第5步）。全部加在一起，最终的通讯得分是 98分！
  * 通俗理解：这是一笔完美的“通话账单”，证明支持细胞通过 TGFA-EGFR 这条信号轴，确实打通了精原干细胞内部 JUN 介导的增殖与耐药相关信号通路。

### 4\. 通路富集分析

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
## 通路富集分析# ==========================================# 提取通讯评分矩阵n <- mt@data$expr_l_r_log2_scale# 对每一对细胞（colnames(n)）进行通路富集pathway.hyper.list <- lapply(colnames(n), function(i){  print(i)  tmp <- tryCatch({    getHyperPathway(      data = n,      object = mt,      cella_cellb = i,      Org = "Homo sapiens"    )  }, error = function(e) {    message(sprintf("skip"))    return(NULL)  })  return(tmp)})# 整理成数据框，用于气泡图myPub.df <- getForBubble(pathway.hyper.list, cella_cellb = colnames(n))head(myPub.df) # 查看结果
```

向下滑动查看全部~

**目的** ：找出“这对细胞在对话时，具体是通过哪条生物学信号通路（如 TGF-β、Wnt 等）”产生的影响。

**输入** ：第三步生成的对象 mt，及其内部的通讯评分数据框 n。

**输出** ：

  * pathway.hyper.list：一个包含不同细胞对（如巨噬细胞-T细胞）显著富集通路（超几何检验结果）的列表。
  * myPub.df：整理后的绘图数据框。

![](../../images/1c6ed74e13101a97.webp)

▲ head(myPub.df) 的局部视图

这份 head(myPub.df) 是 getHyperPathway() 的最终输出。它把上一张“通讯得分成绩单”翻译成了有生物学意义的“结案报告”。

具体来说，它告诉您：在特定的细胞对之间（比如 ST-ST），那些高分信号轴，到底集中在哪些生物学通路上，显著性如何。

列名| 含义| 通俗理解
---|---|---
pathway| KEGG 富集到的生物学通路名称| 细胞间通讯的“主话题”
cc| 细胞对（发送方-接收方）| 谁在和谁打电话
pvalue| 超几何检验算出的 p 值| 这个“主话题”是不是碰巧聊到的？p 越小越真实
NES| 标准化富集分数（Normalized Enrichment Score）| 聊这个话题的“热度”。>0 代表正向富集，越高越热

通路富集分析这一步，可以说是核心计算的第 7 步。

**第 7 步：查通话记录，写结案报告（getHyperPathway）**

  * 在干什么：拿到前6步算出的“通讯得分表”（也就是 expr_l_r_log2_scale），针对每一个“细胞对”（比如 ST→SSC，即 cc 列），把里面得分最高的那些“配体-受体对”全部拎出来。然后，利用KEGG数据库，用超几何检验算一下：这些高分信号，到底集中指向了哪些生物学通路？这些通路是不是纯属巧合？
  * 具体例子：假设在“ST→SSC”这对里，得分最高的是TGFA-EGFR（得分98），紧接着是NRG4-ERBB4（得分95）、CSF1-CSF1R（得分90）。getHyperPathway() 在后台一查：这三个高分对，全部属于KEGG里的EGFR tyrosine kinase inhibitor resistance（EGFR酪氨酸激酶抑制剂耐药） 信号通路！经过超几何检验，算出这种“扎堆”纯属巧合的概率只有0.000000001（p 值极小），于是它得出结论：“这对细胞之间的通讯，不仅真实有效，而且主要‘话题’就是 EGFR酪氨酸激酶抑制剂耐药！”
  * 通俗理解：前6步完成了“谁在打电话、电话打得通不通、里面的人有没有动起来”，第7步就是把过去一个月的通话记录全部调出来，做一份“大数据分析报告”。报告上写着：“支持细胞和精原干细胞这个月聊得最多的主题是‘EGFR酪氨酸激酶抑制剂耐药’，其次还有‘干细胞分化’等话题。”这份报告，也就是之前看到的 myPub.df 表格（包含 pathway, cc, pvalue, NES）。

### 5\. 结果可视化

  *   *   *   *   *   *   *   *

```r
## 绘制通路富集气泡图 (Bubble Plot)# 使用 plotBubble 绘制气泡图p2 <- plotBubble(myPub.df) +  theme(axis.text.y = element_text(color = "black")) + # y轴字体设置为黑色（原图为灰色，这里优化）  coord_flip() # 横纵坐标反转（让通路名横着排，看得更清楚）print(p2)ggsave(filename = "CellCall_BubblePlot.pdf", plot = p2, width = 8, height = 6)ggsave(filename = "CellCall_BubblePlot.png", plot = p2, width = 8, height = 6, dpi = 300)
```

![](../../images/6511d2caf49dde8f.webp)

▲ 通路富集气泡图（plotBubble 输出）：横轴为细胞对，纵轴为显著富集的 KEGG 通路

阿Yan

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

[IF=15，生信基地作为作者单位的第一篇SCI：计算机设计CLDN4导向肽载纳米气泡](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541821&idx=1&sn=27235b32dda0a46efa1df58ca6a0cdbd&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)
![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家一起讨论。![](../../images/fe8ecb8594a1f419.webp)![图片](../../images/acba43cb3408c3d0.gif)您点的每个赞和在看，我都认真当成了喜欢
