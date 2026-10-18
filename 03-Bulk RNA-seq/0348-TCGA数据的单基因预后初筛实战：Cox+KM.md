---
title: "TCGA数据的单基因预后初筛实战：Cox+KM"
date: 2026-09-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542426&idx=1&sn=428c83b091c13a4b1cc3fc6493a8d828&chksm=9b3c5fcaac4bd6dc4a7acec5331efa551c39b1a5a80727f899cee985448e262975fcd676cc8f#rd
albums: ["Bulk RNA-seq"]
---

# TCGA数据的单基因预后初筛实战：Cox+KM

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542426&idx=1&sn=428c83b091c13a4b1cc3fc6493a8d828&chksm=9b3c5fcaac4bd6dc4a7acec5331efa551c39b1a5a80727f899cee985448e262975fcd676cc8f#rd
> 合集：Bulk RNA-seq

**一、写在前面**

面向生信初学者的一篇实操合集，分成两个独立部分：第一部分教你用 `TCGAbiolinks` 从GDC下载TCGA表达数据；第二部分教你拿到数据后，对你自己选定的基因做单因素Cox回归 + 中位数截断KM[生存分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539068&idx=1&sn=2acad38f76a1e54c9d9d4318d2d08a7e&scene=21#wechat_redirect>)（以FSTL3为例，把GENE <\- "FSTL3"换成自己的基因名即可）。

需要说明的是，第二部分完成的实际上是在 [TCGA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539068&idx=1&sn=2acad38f76a1e54c9d9d4318d2d08a7e&scene=21#wechat_redirect>) 队列中的单基因预后关联分析（初筛），而不是严格意义上的”独立外部验证”。

**二、 TCGA 数据下载
**

TCGA数据获取最常用的方案是TCGAbiolinks，核心四个函数：查询 → 下载 → 整理 → 保存。

步骤| 函数| 作用
---|---|---
1\. 查询| `GDCquery()`| 按项目/数据类型/样本类型等条件，生成文件清单
2\. 下载| `GDCdownload()`| 按清单把文件下载到本地
3\. 整理| `GDCprepare()`| 把分散文件合并成一个 `SummarizedExperiment`（SE）对象
4\. 保存| `saveRDS()`| 保存为 R 原生对象，供后续分析

2.1 查询：GDCquery

  *   *   *   *   *   *   *   *   *

```r
library(TCGAbiolinks)library(SummarizedExperiment)query <- GDCquery(  project       = "TCGA-LUAD",                     # 项目 ID  data.category = "Transcriptome Profiling",       # 转录组  data.type     = "Gene Expression Quantification",# 基因表达定量  workflow.type = "STAR - Counts",                 # STAR 流程（TCGA 官方推荐）  sample.type   = "Primary Tumor"                  # 只要原发肿瘤)
```

运行输出如下（能打印出 `o Preparing output`即表示查询成功）：
```
--------------------------------------
o GDCquery: Searching in GDC database
--------------------------------------
Genome of reference: hg38
--------------------------------------------
oo Accessing GDC. This might take a while...
--------------------------------------------
ooo Project: TCGA-LUAD
--------------------
oo Filtering results
--------------------
ooo By data.type
ooo By workflow.type
ooo By sample.type
----------------
oo Checking data
----------------
ooo Checking if there are duplicated cases
ooo Checking if there are results for the query
-------------------
o Preparing output
-------------------
```

📌 通俗理解：GDCquery 就像在淘宝里按条件搜索商品——“我要 LUAD 的转录组定量、STAR 流程、原发肿瘤样本”，它返回一张”购物清单”，而不是数据本身。

🚫 务必避坑：**`sample.type` ** 别漏了。如果省略 sample.type，会同时下载 Solid Tissue Normal（癌旁正常组织）和 Primary Tumor 等所有类型。如果研究目标是肿瘤患者预后分析，建议在查询阶段明确限定 Primary Tumor，避免把不同样本类型混入预后队列。

2.2 下载：GDCdownload

  *   *

```
# 下载（api 方式，每次 20 个文件，断点续传更稳）GDCdownload(query, method = "api", files.per.chunk = 20)
```

运行输出如下（会显示总文件数、总大小，并按 chunk 分批下载）：
```
Downloading data for project TCGA-LUAD
GDCdownload will download 540 files. A total of 2.288476735 GB
Downloading chunk 1 of 27 (20 files, size = 84.718875 MB) as Sun_Sep__6_14_18_37_2026_0.tar.gz
```

2.3 查看下载的文件结构：list.files

下载完成后，可以用 list.files() 查看文件结构：

  *   *

```
list.files("GDCdata", recursive = TRUE)           # 递归列出所有文件length(list.files("GDCdata", recursive = TRUE))   # 文件总数
```

list.files的结果如下（实际会列出全部 540 个文件，此处为目录结构示意）：
```
GDCdata/
└── TCGA-LUAD/
    └── harmonized/
        └── Transcriptome_Profiling/
            └── Gene_Expression_Quantification/
                ├── Sun_Sep__6_14_18_37_2026_0.tar.gz   # 分块包
                ├── Sun_Sep__6_14_18_37_2026_1.tar.gz
                └── ...                                  # 共 27 个 chunk
```

📌 提示：这些.tar.gz 是分块打包的原始文件。通常不需要手动逐个处理，后续可通过GDCprepare()对已下载数据进行整理、合并成 SummarizedExperiment对象。

2.4 整理与保存：GDCprepare + saveRDS

  *   *   *   *

```r
# 整理成 SummarizedExperimentse <- GDCprepare(query, summarizedExperiment = TRUE)# 保存为 R 原生对象（后续分析直接 readRDS）saveRDS(se, "TCGA-LUAD_se.rds")
```

GDCprepare得到的se是标准的SummarizedExperiment对象：assay() 存表达矩阵，colData() 存临床信息，rowData() 存基因注释。

💡 关键知识点：STAR - Counts 流程会给出三种定量方式，都在 assayNames(se)里：

  *   *   *   *

```
assayNames(se)# [1] "unstranded"         # 原始 counts# [2] "tpm_unstrand"       # TPM# [3] "fpkm_uq_unstrand"   # FPKM-UQ
```

⚠️ 定量方式怎么选：本教程的生存/预后分析统一使用 TPM；但如果要做 RNA-seq 差异表达分析（如 DESeq2），应基于原始整数 counts，不能简单把 TPM 当作 DESeq2 的输入。FPKM-UQ 是 GDC 数据体系中提供的一种标准化表达量，不同下游分析对尺度的要求不同，这里选 TPM 是本教程的分析方案，不代表所有 TCGA 预后分析都必须用 TPM。

  *

```r
tpm <- assay(se, "tpm_unstrand")   # 行 = 基因，列 = 样本
```

**三、 单基因预后初筛：Cox + KM
**

3.1 开始前的分析设计

动手写代码前，先明确下面几点，能少走很多弯路：

① 分析对象：是 LUAD 还是 LUSC，还是合并的 NSCLC？

② 样本范围：是否只纳入 Primary Tumor？

③ 去重策略：如何保证”一个患者只保留一个独立样本”？

④ 生存定义：OS 的”时间”和”事件”分别怎么算？

⑤ Cox 形式：用连续表达量，还是分组变量？

⑥ KM 截断：cut-off 是否预先指定（如中位数）？

⑦ 结果定位：当前结果是”初筛/关联分析”，还是”独立外部验证”？

3.2 开始前，你需要准备什么

你只需要两样东西：

① 表达矩阵：TCGA的 SummarizedExperiment（SE）对象（含tpm_unstrand assay），或等价的”基因 × 样本” TPM 矩阵；

② 生存数据：每个样本的vital_status（Dead/Alive）、days_to_death、days_to_last_follow_up，以及样本barcode、patient。

💡 如果还没下载数据，请先按第一部分拿到SE对象。本文假设你已经有了 TCGA-LUAD_se.rds这样的文件。

📌 关键字段说明：vital_status == "Dead" 用 days_to_death 作为生存时间，否则用 ddays_to_last_follow_up（删失）。OS_event 中 1 表示死亡、0 表示删失。

3.3 核心：一个可复用脚本

下面是一个可直接套用的完整脚本。你只需要改最上面 3 行：基因名、SE 文件路径、输出目录。脚本会同时输出Cox结果、log-rank P、High vs Low 分组 Cox HR、KM 图，并保存结果表CSV。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# ================ 只需改这里 ================GENE    <- "FSTL3"                 # ← 换成你自己的基因名SE_FILE <- "TCGA-LUAD_se.rds"      # ← 换成你的 SE 文件路径OUT_DIR <- "FSTL3_validation"      # ← 换成你的输出目录# =============================================library(SummarizedExperiment)library(survival)library(survminer)se <- readRDS(SE_FILE)cd <- as.data.frame(colData(se))tpm_all <- assay(se, "tpm_unstrand")# 1) 基因名 -> ENSG ID（若 SE 行名已是基因符号，可跳过）gn <- rowData(se)$gene_namenames(gn) <- rownames(se)gid <- names(gn)[gn == GENE]if (length(gid) == 0) stop("未找到目标基因: ", GENE)if (length(gid) > 1)  warning("基因 symbol 匹配到多个 ENSG ID，取第一个: ", GENE)gid <- gid[1]# 2) 去重：1 patient = 1 sample（本数据集处理规则）#    (a) 同患者、同 sample+vial+portion -> TPM 取均值（技术重复合并）#    (b) 同患者多个 vial -> 保留 vial 最小 (A < B < C)，规则需在研究设计里预先声明vp <- paste(cd$patient, sapply(cd$barcode, function(bc) {  p <- strsplit(bc, "-")[[1]]; if (length(p) >= 5) paste(p[4], p[5], sep = "-") else bc}), sep = "::")grp <- split(seq_len(ncol(se)), vp)tpm <- do.call(cbind, lapply(grp, function(i) {  if (length(i) == 1) tpm_all[, i] else rowMeans(tpm_all[, i, drop = FALSE])}))clin <- do.call(rbind, lapply(grp, function(i) cd[i[1], , drop = FALSE]))#    (b) 同患者多 vial -> 保留 vial 最小 (A < B < C)vl <- sapply(clin$barcode, function(bc) {  p <- strsplit(bc, "-")[[1]]; if (length(p) >= 4) substr(p[4], 3, 3) else "Z"})pt <- split(seq_len(nrow(clin)), clin$patient)keep <- sapply(pt, function(i) if (length(i) == 1) i else i[order(vl[i])[1]])tpm <- tpm[, keep, drop = FALSE]clin <- clin[keep, , drop = FALSE]# 3) 构建 OS 生存数据clin$OS_time  <- ifelse(clin$vital_status == "Dead",                        as.numeric(clin$days_to_death),                        as.numeric(clin$days_to_last_follow_up))clin$OS_event <- ifelse(clin$vital_status == "Dead", 1, 0)valid <- !is.na(clin$OS_time) & clin$OS_time > 0expr <- as.numeric(tpm[gid, ])[valid]clin <- clin[valid, , drop = FALSE]# 4) 单因素 Cox（连续变量 log2(TPM+1)）fit_cox <- coxph(Surv(clin$OS_time, clin$OS_event) ~ log2(expr + 1))s <- summary(fit_cox)cox_hr <- s$conf.int[1, "exp(coef)"]cox_lo <- s$conf.int[1, "lower .95"]cox_up <- s$conf.int[1, "upper .95"]cox_p  <- s$coefficients[1, "Pr(>|z|)"]cat(sprintf("Cox: HR = %.3f (%.3f-%.3f), p = %.3e\n", cox_hr, cox_lo, cox_up, cox_p))# 5) KM（中位数截断 + log-rank + High vs Low 分组 Cox HR）surv <- data.frame(time = clin$OS_time, event = clin$OS_event, expr = expr)cutoff <- median(surv$expr)surv$group <- factor(ifelse(surv$expr > cutoff, "High", "Low"),                     levels = c("Low", "High"))fit <- survfit(Surv(time, event) ~ group, data = surv)lr_p <- 1 - pchisq(survdiff(Surv(time, event) ~ group, data = surv)$chisq, df = 1)grp_cox <- summary(coxph(Surv(time, event) ~ group, data = surv))km_hr <- grp_cox$conf.int[1, "exp(coef)"]km_lo <- grp_cox$conf.int[1, "lower .95"]km_up <- grp_cox$conf.int[1, "upper .95"]cat(sprintf("KM: log-rank p = %.4f; High vs Low Cox HR = %.3f (%.3f-%.3f)\n",            lr_p, km_hr, km_lo, km_up))# 6) 保存结果表dir.create(OUT_DIR, recursive = TRUE, showWarnings = FALSE)res <- data.frame(gene = GENE, n = nrow(clin), nevent = sum(clin$OS_event),                  cutoff = cutoff,                  cox_HR = cox_hr, cox_lower95 = cox_lo, cox_upper95 = cox_up, cox_p = cox_p,                  group_HR = km_hr, group_lower95 = km_lo, group_upper95 = km_up,                  logrank_p = lr_p)write.csv(res, file.path(OUT_DIR, paste0(GENE, "_survival_result.csv")), row.names = FALSE)# 7) 绘图p <- ggsurvplot(fit, data = surv,                pval = TRUE, risk.table = TRUE, conf.int = TRUE,                palette = c("#4DBBD5", "#E64B35"),                legend.labs = c("Low", "High"), legend.title = GENE,                xlab = "Time (days)", ylab = "Overall Survival")pdf(file.path(OUT_DIR, paste0(GENE, "_KM.pdf")), width = 7, height = 7)print(p)dev.off()
```

向下滑动查看全部~

分步要点：

① 去重：区分”技术重复”和”独立样本”（最容易被忽略的一步）

TCGA barcode 是分层级的，例如：
```
TCGA-XX-XXXX-01A-01R-XXXX-XX
               ↑ sample+vial（p[4]=01A）
                    ↑ portion+analyte（p[5]=01R）
                            ↑ plate（p[6]）
```

生存分析通常要求一个患者只贡献一个独立样本。但”去重”不能一刀切：

  * 技术重复 / 同一生物样本的重复测序：可以合并（如取均值）；

  * 同一患者存在多个独立生物学样本：需要预先定义选择规则——例如优先指定样本类型、选择临床信息完整的样本，或根据研究设计决定。

🚫 避坑：本文脚本里的”同 vial 多 plate 取均值、多 vial 保留 A”是本数据集的约定处理规则，不是 TCGA 通用铁律。照搬前请确认你的数据里 A/B/C vial 确实是同一生物样本的技术分装；否则应换成你自己的选择规则，并在方法里写清楚。

② 本教程的Cox使用连续表达变量

  *

```
coxph(Surv(OS_time, OS_event) ~ log2(expr + 1))
```

将表达量直接作为连续变量，可以减少人为 High/Low 二分造成的信息损失。但 Cox 本身并不是”只能”用连续变量——连续、二分类、多分类都可以。

⚠️ HR的单位：这里的HR对应 **`log2(TPM+1)`** 每增加 1 个单位时的相对风险变化，而不是”原始TPM每增加 1”或严格意义的”表达翻倍”。HR > 1 表示较高表达与较高死亡风险相关，HR < 1 表示较高表达与较低死亡风险相关——这是统计学关联，不代表基因已被证明具有直接致病或保护作用。

③ KM用中位数截断，但要知道它的边界

  *   *

```r
cutoff <- median(expr)group  <- ifelse(expr > cutoff, "High", "Low")
```

中位数截断简单、透明，能避免”遍历所有截断点、选log-rank p最小的那个”这种明显过拟合。但它仍然会把连续变量硬切成两组、丢失信息；正式研究中还应结合预先定义的cut-off、连续变量模型或独立验证队列综合判断。

3.4 实战结果：以FSTL3为例

把脚本里的GENE <\- "FSTL3" 跑一遍（以本次运行结果为例，经过当前样本筛选、去重和生存信息过滤后，共纳入504例患者，其中182例发生死亡事件）：

指标| 结果
---|---
单因素 Cox HR (95% CI)| **1.29 (1.13–1.46)**
Cox p 值| 8.2 × 10⁻⁵
High vs Low 分组 Cox HR (95% CI)| 1.54 (1.15–2.07)
log-rank p| 0.0036
中位数截断值 (TPM)| 34.3

![FSTL3 在 TCGA-LUAD 的 KM 曲线](../../images/8593c11f60739eb1.webp)

FSTL3 在 TCGA-LUAD的KM曲线

📌 结果解读：FSTL3高表达组（High，红色）的总生存低于低表达组（Low，蓝色），log-rank p = 0.0036；连续变量Cox HR = 1.29 > 1，同样指向”较高表达与较高死亡风险相关”。两者方向一致、互相印证。

⚠️ 注意：这是单因素关联分析，不能单独证明 FSTL3 是独立预后因子；正式研究还需结合临床变量做多因素Cox、检查比例风险假设，并尽可能在独立队列中验证。

📚 文献对照：本教程得到的High vs Low分组Cox HR与Meng et al. 报道的结果方向和数量级接近（文献HR = 1.55，95% CI 1.16–2.07，p = 0.003），但由于数据筛选与分析流程可能存在差异，这应理解为结果对照，而非严格意义上的完全复现。

3.5 避坑清单（汇总）

  * ✅ 样本类型：GDCquery 记得 sample.type = "Primary Tumor"，避免混入其他样本类型；

  * ✅ 去重：区分”技术重复”与”独立样本”，并预先声明选择规则，保证 1 患者 = 1 独立样本；

  * ✅ Cox形式：本教程用连续变量 log2(TPM+1)，HR单位是”log2(TPM+1) 每增加 1”；

  * ✅ KM截断：中位数截断可减少过拟合，但仍会损失连续信息；

  * ✅ 比例风险假设：正式研究建议用 survival::cox.zph()检查Cox的PH假设；

  * ✅ 结果定位：单因素Cox/KM是”关联/初筛”，不是”独立预后因子已被证明”；

  * ✅ 换基因：仅当基因能正确匹配、且有足够表达与生存信息时，改GENE即可；否则要检查样本数、事件数与模型结果。

3.6 总结

环节| 关键函数| 一句话要点
---|---|---
数据下载| `GDCquery → GDCdownload → GDCprepare`| 查、下、并，拿到 SE
读数据| `readRDS` \+ `assay(se, "tpm_unstrand")`| 取 SE 的 TPM 矩阵
去重| 两步行索引| 1 患者 = 1 独立样本
生存数据| `vital_status + days_to_*`| Dead 用死亡时间，Alive 用随访时间
单因素 Cox| `coxph(Surv ~ log2(TPM+1))`| 连续变量，HR 与 p
KM 分析| `survfit + survdiff + ggsurvplot`| 中位数截断 + log-rank + 分组 HR

📌 最务实的心法：第一部分拿数据，第二部分做初筛。单基因预后初筛就是”三步——把基因名一换、跑脚本、看HR和log-rank p”。同时记住：单因素 Cox/KM给出的是统计学关联，不是因果结论；连续变量Cox+合理的KM分组 + 患者级样本去重+PH假设检查，是开展单基因预后分析时值得注意的基础规范。

**四、参考文献
**

[1]Meng X, Zhao X, Zhou B, Song W, Liang Y, Liang M, Du M, Shi J, Gao Y. FSTL3 is associated with prognosis and immune cell infiltration in lung adenocarcinoma. Journal of Cancer Research and Clinical Oncology, 2024, 150:17. DOI: 10.1007/s00432-023-05553-w

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

![图片](../../images/4ec66ccdb832fd05.gif)Coco![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家一起讨论。![](../../images/fe8ecb8594a1f419.webp)![图片](../../images/acba43cb3408c3d0.gif)您点的每个赞和在看，我都认真当成了喜欢
