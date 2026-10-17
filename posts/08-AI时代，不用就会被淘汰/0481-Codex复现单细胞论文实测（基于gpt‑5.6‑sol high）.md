---
title: "Codex复现单细胞论文实测（基于gpt‑5.6‑sol high）"
date: 2026-08-30
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541384&idx=1&sn=483a12dca401717fce52e6c608149851&chksm=9b3c5bd8ac4bd2cefa8fabd7fb5b4e695e6a2edb2f6a04956370f041eb344259f5f71f5fb470#rd
albums: ["AI时代，不用就会被淘汰"]
---

# Codex复现单细胞论文实测（基于gpt‑5.6‑sol high）

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541384&idx=1&sn=483a12dca401717fce52e6c608149851&chksm=9b3c5bd8ac4bd2cefa8fabd7fb5b4e695e6a2edb2f6a04956370f041eb344259f5f71f5fb470#rd
> 合集：AI时代，不用就会被淘汰

**一、Codex vs. Claude Code/DeepSeek**

1、直接上结果比对图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwmIk1aNuHWcLQPeicMu3f6exHrWib9KTbbgjqc9HEiaj9icGKQ0n9aZViaJMEHsRp3vdOZ8O4Z0Cricuo8HK7EoshW4DkegZ43OeK7rQ/640?wx_fmt=jpeg)

vs.

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwk87H743icjHicaficevGRMJkI88gMfUmWPPyng3DJbokekBMfANI92ZkITsyB4FVCEDnHkZ4M9icpVYeTfXLQ9CkciaAkoBfbVZXIA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

vs.

[![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkh9M70O31lFPXIBKTE5vrKFKJZIz5VJfEFfQQRyaqSXy6Uu5ic1HSSF4ibLRHmf7h0545vgKVMX6o8NRkrJzdRPWdKzk0PQjCos/640?wx_fmt=png&from=appmsg)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538520&idx=1&sn=6858ae5260580c74fd46e658dbc4e49b&scene=21#wechat_redirect>)

vs.

我们用作[R语言scRNA-seq文献复现专题教学的人工复现结果：](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535877&idx=7&sn=b716aeb8e86eba4acd50b982beb0c963&scene=21#wechat_redirect>)

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzuG7SAX0RGL3Z5CMBpFl34YO4GJqVC1aO7VFTUH8CjjtlOrydr94KlIpuHMiaGKbhF0RbOj5nRjHg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&scene=21#wechat_redirect>)

之前我们测试过：[试试D老师的单细胞代码分析能力怎么样](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538520&idx=1&sn=6858ae5260580c74fd46e658dbc4e49b&scene=21#wechat_redirect>)和claude code复现单细胞文章，这次我们在codex中输入相同的指令“我希望复现GSE163973数据集对应来源文章的全部单细胞分析相关内容，请在本地运行并给我输出图表和代码”，结果图呈现见上图。

2、聊聊感受

实际使用下来，codex零交互，使用下来很丝滑，比之前的D老师和Claude code的交互明显少了很多很多。codex（gpt‑5.6‑sol high）跑完全相同的GSE163973复现指令，同样做到了全程零交互，丢完一句指令就放手交给终端自主跑任务，不需要人中途介入确认、补提示。整套流程里它会自动下载数据集、搭建目录结构、逐段生成执行脚本，本地运行、调试报错、迭代修正分析代码，最后输出整套工程文件与绘图结果，不需要我做任何手动干预。

但代价就是token账单直接冲到￥40+。虽然不需要我来回对话，可它每完成一个分析节点就会输出大段的进度汇报，“已完成数据下载”“QC 质控完成”“归一化处理结束” 这类流水日志源源不断往外吐；每一轮agent循环都会把全部历史日志、完整代码、程序报错全部塞进输入上下文，又没有缓存折扣，叠加sol 本身输出定价偏高，再加上深度推理模式内部大量思考token默默消耗，即便没有人和它聊天，token也在疯狂燃烧。简直是吞金兽啊！！！大家是不是也遇到这种情况呢？可以分享一下我们探讨探讨~

三个AI工具输出的图片，与原文相比各有差异。画风和配色有些出入，图片展示方式也有区别。相同的指令下，为什么差异这么大呢？这个与使用不同中转API有关，也和各个AI工具运行内核有关，还有可能和运行时间段有关。

时间上，codex输出结果比[claude code](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539308&idx=1&sn=c1b2915aac125f4fa31bd50ffb8b98b9&scene=21#wechat_redirect>)更快更多，评论区有没有同时用过三种AI工具的同学，可以结合自己的使用经历上票了：

如果需要Codex、Claude Code在[服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539913&idx=2&sn=516a4224cdf85a68b119ce4a04f12d40&scene=21#wechat_redirect>)中代为部署，也欢迎联系客服微信[**Biomamba_zhushou**]聊聊

**二、使用过程与结果**

演示一下Codex复现单细胞文章流程，本文的输出代码和工程文件下载链接：

通过网盘分享的文件： https://pan.baidu.com/s/1dhyI-W5-JXkylFnfPMpNJg

提取码，联系客服微信[Biomamba_zhushou]领取

此时输入codex，显示的内核就是，然后在光标处输入你的需求并回车就可以啦。![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmqu0MAW4WOg8amtsYXhm8scg1qFaBFtibqTUSokwRfWn93re2yIdd09R4SgjLsRicL0aoJl9tpuFozWp0uHibKxhM05VHibrWic5CY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkGxOEGyhL3eia2pySBlouXMHcQicbVfOSd5KOtWaVVxvawCKVR3rVxBymumjrj09JDW973WVuwL2G1a1Ka1WFxhxsYUIkRmW0ic8/640?wx_fmt=png&from=appmsg)

我们来看一下codex的输出结果：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
/data3/home/zyy/data_HD/codex-project├── data│   ├── raw│   │   ├── GSE160536_counts_ProcessingData.csv.gz│   │   ├── GSE163973_RAW.tar│   │   ├── GSE163973_RAW.tar.md5│   │   ├── GSM4994379_KL1_matrix│   │   │   └── KF1_matrix│   │   │       ├── barcodes.tsv.gz│   │   │       ├── features.tsv.gz│   │   │       └── matrix.mtx.gz│   │   ├── GSM4994379_KL1_matrix.tar.gz│   │   ├── GSM4994380_KL2_matrix│   │   │   └── KF2_matrix│   │   │       ├── barcodes.tsv.gz│   │   │       ├── features.tsv.gz│   │   │       └── matrix.mtx.gz│   │   ├── GSM4994380_KL2_matrix.tar.gz│   │   ├── GSM4994381_KL3_matrix│   │   │   └── KF3_matrix│   │   │       ├── barcodes.tsv.gz│   │   │       ├── features.tsv.gz│   │   │       └── matrix.mtx.gz│   │   ├── GSM4994381_KL3_matrix.tar.gz│   │   ├── GSM4994382_NS1_matrix│   │   │   └── NF1_matrix│   │   │       ├── barcodes.tsv.gz│   │   │       ├── features.tsv.gz│   │   │       └── matrix.mtx.gz│   │   ├── GSM4994382_NS1_matrix.tar.gz│   │   ├── GSM4994383_NS2_matrix│   │   │   └── NF2_matrix│   │   │       ├── barcodes.tsv.gz│   │   │       ├── features.tsv.gz│   │   │       └── matrix.mtx.gz│   │   ├── GSM4994383_NS2_matrix.tar.gz│   │   ├── GSM4994384_NS3_matrix│   │   │   └── NF3_matrix│   │   │       ├── barcodes.tsv.gz│   │   │       ├── features.tsv.gz│   │   │       └── matrix.mtx.gz│   │   └── GSM4994384_NS3_matrix.tar.gz│   └── reference│       ├── GSE160536_family.xml.tgz│       ├── GSE163973_family.xml│       ├── GSE163973_family.xml.tgz│       ├── GSE163973_integrate.all.NS.all.KL_cell.meta.data.csv.gz│       ├── GSE163973_integrate.all.NS.all.KL.fib_cell.meta.data.csv.gz│       ├── GSE163973_integrate.all.NS.all.KL.fib.main.clusters_cell.meta.data.csv.gz│       ├── GSE163973_integrate.all.NS.all.KL.fib.seurat.object.Rdata│       ├── GSE163973_integrate.all.NS.all.KL.fib.seurat.object.Rdata.gz│       ├── GSE163973_integrate.all.NS.all.KL.seurat.object.Rdata│       ├── GSE163973_integrate.all.NS.all.KL.seurat.object.Rdata.gz│       ├── GSE163973_integrate.all.NS.all.KL.seurat.object.Rdata.gz.md5│       ├── PMC8211847_supplementaryFiles.zip│       ├── PMC8211847.xml│       └── supplement│           ├── 41467_2021_24110_Fig1_HTML.gif│           ├── 41467_2021_24110_Fig1_HTML.jpg│           ├── 41467_2021_24110_Fig2_HTML.gif│           ├── 41467_2021_24110_Fig2_HTML.jpg│           ├── 41467_2021_24110_Fig3_HTML.gif│           ├── 41467_2021_24110_Fig3_HTML.jpg│           ├── 41467_2021_24110_Fig4_HTML.gif│           ├── 41467_2021_24110_Fig4_HTML.jpg│           ├── 41467_2021_24110_Fig5_HTML.gif│           ├── 41467_2021_24110_Fig5_HTML.jpg│           ├── 41467_2021_24110_Fig6_HTML.gif│           ├── 41467_2021_24110_Fig6_HTML.jpg│           ├── 41467_2021_24110_Fig7_HTML.gif│           ├── 41467_2021_24110_Fig7_HTML.jpg│           ├── 41467_2021_24110_MOESM1_ESM.pdf│           ├── 41467_2021_24110_MOESM2_ESM.pdf│           ├── 41467_2021_24110_MOESM3_ESM.pdf│           ├── 41467_2021_24110_MOESM4_ESM.xlsx│           ├── 41467_2021_24110_MOESM5_ESM.xlsx│           ├── 41467_2021_24110_MOESM6_ESM.xlsx│           ├── 41467_2021_24110_MOESM7_ESM.xlsx│           ├── 41467_2021_24110_MOESM8_ESM.pdf│           └── 41467_2021_24110_MOESM9_ESM.xlsx├── logs│   ├── sessionInfo_CellChat.txt│   ├── sessionInfo_DE_DPT.txt│   ├── sessionInfo_main_figures.txt│   └── sessionInfo_reprocess.txt├── objects│   ├── author_all_cells_annotated.rds│   ├── author_all_cells.rds│   ├── author_fibroblasts_annotated.rds│   ├── author_fibroblasts.rds│   ├── cellchat_Keloid.rds│   ├── cellchat_Normal_scar.rds│   ├── keloid_sC1_sC4_DPT.rds│   └── reprocessed_from_counts.rds├── README.md├── results│   ├── figures│   │   ├── Figure1G_DE_gene_counts.pdf│   │   ├── Figure1G_DE_gene_counts.png│   │   ├── Figure1_whole_atlas.pdf│   │   ├── Figure1_whole_atlas.png│   │   ├── Figure2_fibroblast_subclusters.pdf│   │   ├── Figure2_fibroblast_subclusters.png│   │   ├── Figure2H_GO_mesenchymal_Keloid_up.pdf│   │   ├── Figure2H_GO_mesenchymal_Keloid_up.png│   │   ├── Figure3_mesenchymal_markers.pdf│   │   ├── Figure3_mesenchymal_markers.png│   │   ├── Figure4_CellChat_Keloid.png│   │   ├── Figure4_CellChat_Normal_scar.png│   │   ├── Figure4_Keloid_FGF.png│   │   ├── Figure4_Keloid_PDGF.png│   │   ├── Figure4_Keloid_TGFb.png│   │   ├── Figure4_Keloid_VEGF.png│   │   ├── Figure6_DPT.pdf│   │   ├── Figure6_DPT.png│   │   ├── S01_reprocessed_QC.pdf│   │   ├── S01_reprocessed_QC.png│   │   ├── S02_reprocessed_UMAP.pdf│   │   └── S02_reprocessed_UMAP.png│   └── tables│       ├── ACTA2_myofibroblast_summary.csv│       ├── author_all_cells_metadata.csv│       ├── CellChat_Keloid_interactions.csv│       ├── CellChat_Normal_scar_interactions.csv│       ├── cell_type_composition.csv│       ├── DE_Keloid_vs_Normal_by_celltype.csv│       ├── DE_mesenchymal_Keloid_vs_Normal.csv│       ├── DE_sC4_vs_sC1_Keloid.csv│       ├── DPT_sC1_sC4_Keloid.csv│       ├── fibroblast_composition.csv│       ├── fibroblast_type_markers.csv│       ├── GO_mesenchymal_Keloid_up.csv│       └── reprocessed_qc_summary.csv├── run_all.sh└── scripts    ├── 00_download_data.sh    ├── 01_reprocess_from_counts.R    ├── 02_author_objects_and_main_figures.R    ├── 03_differential_enrichment_pseudotime.R    ├── 04_cellchat.R    └── 05_velocity_from_bam.sh22 directories, 118 files
```

大家也可以欣赏一下codex的代码：

**00_download_data.sh**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
#!/usr/bin/env bashset -euo pipefailmkdir -p data/raw data/reference data/reference/supplement objects results/figures results/tables logsgeo_base="https://ftp.ncbi.nlm.nih.gov/geo/series/GSE163nnn/GSE163973"curl -L --fail --retry 5 "${geo_base}/suppl/GSE163973_RAW.tar" -o data/raw/GSE163973_RAW.tarcurl -L --fail --retry 5 "${geo_base}/miniml/GSE163973_family.xml.tgz" -o data/reference/GSE163973_family.xml.tgzcurl -L --fail --retry 5 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8211847/fullTextXML" -o data/reference/PMC8211847.xmlcurl -L --fail --retry 5 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8211847/supplementaryFiles" -o data/reference/PMC8211847_supplementaryFiles.ziptar -xf data/raw/GSE163973_RAW.tar -C data/rawfor archive in data/raw/GSM*_matrix.tar.gz; do  out="${archive%.tar.gz}"  mkdir -p "$out"  tar -xzf "$archive" -C "$out"donetar -xzf data/reference/GSE163973_family.xml.tgz -C data/referenceunzip -o data/reference/PMC8211847_supplementaryFiles.zip -d data/reference/supplementmd5sum data/raw/GSE163973_RAW.tar > data/raw/GSE163973_RAW.tar.md5
```

**向下滑查看更多代码****
**

**01_reprocess_from_counts.R**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
#!/usr/bin/env RscriptsuppressPackageStartupMessages({  library(Seurat)  library(Matrix)  library(ggplot2)  library(patchwork)  library(dplyr)})set.seed(20210617)dir.create("results/figures", recursive = TRUE, showWarnings = FALSE)dir.create("results/tables", recursive = TRUE, showWarnings = FALSE)dir.create("objects", recursive = TRUE, showWarnings = FALSE)
sample_info <- data.frame(  sample = c("KF1", "KF2", "KF3", "NF1", "NF2", "NF3"),  condition = rep(c("Keloid", "Normal scar"), each = 3),  path = c(      "data/raw/GSM4994379_KL1_matrix/KF1_matrix",       "data/raw/GSM4994380_KL2_matrix/KF2_matrix",       "data/raw/GSM4994381_KL3_matrix/KF3_matrix",       "data/raw/GSM4994382_NS1_matrix/NF1_matrix",       "data/raw/GSM4994383_NS2_matrix/NF2_matrix",       "data/raw/GSM4994384_NS3_matrix/NF3_matrix"    ))
objs <- lapply(seq_len(nrow(sample_info)), function(i) {  x <- Read10X(sample_info$path[i], gene.column = 2)  o <- CreateSeuratObject(x, project = sample_info$sample[i], min.cells = 3)  o$sample <- sample_info$sample[i]  o$condition <- sample_info$condition[i]  o[["percent.mt"]] <- PercentageFeatureSet(o, pattern = "^MT-")  o})names(objs) <- sample_info$sample
qc_before <- bind_rows(lapply(objs, function(o) {  data.frame(sample = o$sample[1], stage = "before", cells = ncol(o),               median_nFeature = median(o$nFeature_RNA), median_nCount = median(o$nCount_RNA),               median_percent_mt = median(o$percent.mt))}))
# The paper text calls these “UMI-counts”, but the released author's metadata# demonstrate that the applied 200–6000 bounds are nFeature_RNA bounds.objs <- lapply(objs, subset, subset = nFeature_RNA >= 200 & nFeature_RNA <= 6000)qc_after <- bind_rows(lapply(objs, function(o) {  data.frame(sample = o$sample[1], stage = "after_200_6000_features", cells = ncol(o),             median_nFeature = median(o$nFeature_RNA), median_nCount = median(o$nCount_RNA),             median_percent_mt = median(o$percent.mt))}))
write.csv(bind_rows(qc_before, qc_after), "results/tables/reprocessed_qc_summary.csv", row.names = FALSE)qc_data <- bind_rows(lapply(objs, function(o) cbind(o@meta.data, cell = colnames(o))))p_qc <- ggplot(qc_data, aes(sample, nFeature_RNA, fill = condition)) +  geom_violin(scale = "width", trim = TRUE) + geom_boxplot(width = .12, outlier.shape = NA) +  scale_y_log10() + theme_classic(base_size = 11) + labs(x = NULL, y = "Genes per cell (log10)")ggsave("results/figures/S01_reprocessed_QC.png", p_qc, width = 7, height = 4.5, dpi = 300)ggsave("results/figures/S01_reprocessed_QC.pdf", p_qc, width = 7, height = 4.5)
objs <- lapply(objs, function(o) {  o <- NormalizeData(o, normalization.method = "LogNormalize", scale.factor = 10000, verbose = FALSE)  FindVariableFeatures(o, selection.method = "vst", nfeatures = 2000, verbose = FALSE)})features <- SelectIntegrationFeatures(objs, nfeatures = 2000)anchors <- FindIntegrationAnchors(objs, anchor.features = features, dims = 1:15)combined <- IntegrateData(anchors, dims = 1:15)DefaultAssay(combined) <- "integrated"combined <- ScaleData(combined, verbose = FALSE)combined <- RunPCA(combined, npcs = 30, verbose = FALSE)combined <- RunUMAP(combined, dims = 1:15, seed.use = 20210617, verbose = FALSE)combined <- FindNeighbors(combined, dims = 1:15, verbose = FALSE)combined <- FindClusters(combined, resolution = 0.3, algorithm = 1, random.seed = 20210617, verbose = FALSE)saveRDS(combined, "objects/reprocessed_from_counts.rds", compress = FALSE)
p1 <- DimPlot(combined, group.by = "seurat_clusters", label = TRUE, repel = TRUE) + ggtitle("Reprocessed clusters")p2 <- DimPlot(combined, group.by = "sample") + ggtitle("Samples")p3 <- DimPlot(combined, group.by = "condition") + ggtitle("Conditions")p <- p1 + p2 + p3 + plot_layout(ncol = 3)ggsave("results/figures/S02_reprocessed_UMAP.png", p, width = 15, height = 4.8, dpi = 300)ggsave("results/figures/S02_reprocessed_UMAP.pdf", p, width = 15, height = 4.8)writeLines(capture.output(sessionInfo()), "logs/sessionInfo_reprocess.txt")
```

**向下滑查看更多代码**

**02_author_objects_and_main_figures.R**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
#!/usr/bin/env RscriptsuppressPackageStartupMessages({  library(Seurat)  library(ggplot2)  library(patchwork)  library(dplyr)  library(tidyr)  library(scales)})set.seed(20210617)dir.create("results/figures", recursive = TRUE, showWarnings = FALSE)dir.create("results/tables", recursive = TRUE, showWarnings = FALSE)
all <- readRDS("objects/author_all_cells.rds")fib <- readRDS("objects/author_fibroblasts.rds")all$condition <- ifelse(grepl("^KF", all$orig.ident), "Keloid", "Normal scar")fib$condition <- ifelse(grepl("^KF", fib$orig.ident), "Keloid", "Normal scar")all$cluster <- factor(paste0("C", as.integer(as.character(all$seurat_clusters)) + 1), levels = paste0("C", 1:21))fib$subcluster <- factor(paste0("sC", as.integer(as.character(fib$integrated_snn_res.0.45)) + 1), levels = paste0("sC", 1:13))fib$fibroblast_type <- recode(as.character(fib$subcluster),  sC1 = "Mesenchymal", sC4 = "Mesenchymal",  sC2 = "Pro-inflammatory", sC3 = "Pro-inflammatory", sC9 = "Pro-inflammatory",  sC6 = "Secretory-papillary", sC7 = "Secretory-papillary",  sC5 = "Secretory-reticular", .default = "Minor/excluded")fib$fibroblast_type <- factor(fib$fibroblast_type,  c("Secretory-papillary", "Secretory-reticular", "Mesenchymal", "Pro-inflammatory", "Minor/excluded"))
saveRDS(all, "objects/author_all_cells_annotated.rds", compress = FALSE)saveRDS(fib, "objects/author_fibroblasts_annotated.rds", compress = FALSE)
cell_counts <- as.data.frame(table(sample = all$orig.ident, condition = all$condition, cell_type = all$cellType))cell_counts <- cell_counts %>% group_by(sample) %>% mutate(proportion = Freq / sum(Freq)) %>% ungroup()write.csv(cell_counts, "results/tables/cell_type_composition.csv", row.names = FALSE)fib_counts <- as.data.frame(table(sample = fib$orig.ident, condition = fib$condition,                                  subcluster = fib$subcluster, fibroblast_type = fib$fibroblast_type))write.csv(fib_counts, "results/tables/fibroblast_composition.csv", row.names = FALSE)
cell_cols <- c(Endothelial="#1f78b4", Fibroblast="#e31a1c", muscle_fiber="#ff7f00",  Keratinocyte="#6a3d9a", Immune_cell="#33a02c", Lymphatic_endothelial="#a6cee3",  Glandular="#b15928", Unknown="#999999", Neural_cell="#cab2d6", Melanocytes="#fb9a99")p1b <- DimPlot(all, reduction="umap", group.by="cluster", label=TRUE, repel=TRUE, raster=TRUE) +  ggtitle("A  40,655 cells / 21 clusters") + NoLegend()p1c <- DimPlot(all, reduction="umap", group.by="cellType", cols=cell_cols, raster=TRUE) +  ggtitle("B  Author cell-lineage annotation") + labs(color="Cell lineage")markers <- c("COL1A1","ENG","RGS5","KRT14","PTPRC","LYVE1","DCD","S100B","MLANA")p1e <- FeaturePlot(all, features=markers, reduction="umap", order=TRUE, raster=TRUE,                   ncol=3, cols=c("grey92","#b2182b"), max.cutoff="q95")prop <- cell_counts %>% filter(!cell_type %in% c("Keratinocyte","Melanocytes")) %>%  group_by(condition,cell_type) %>% summarise(n=sum(Freq),.groups="drop") %>%  group_by(condition) %>% mutate(proportion=n/sum(n))p1f <- ggplot(prop,aes(condition,proportion,fill=cell_type)) + geom_col(width=.75) +  scale_y_continuous(labels=percent) + scale_fill_manual(values=cell_cols) + theme_classic() +  labs(x=NULL,y="Dermal-cell proportion",fill="Cell lineage")fig1 <- (p1b | p1c) / (p1e | p1f) + plot_annotation(title="Figure 1 — Whole-dataset atlas")ggsave("results/figures/Figure1_whole_atlas.png",fig1,width=16,height=13,dpi=300)ggsave("results/figures/Figure1_whole_atlas.pdf",fig1,width=16,height=13)
p2a <- DimPlot(fib,reduction="umap",group.by="subcluster",label=TRUE,repel=TRUE,raster=TRUE) + ggtitle("A  13 fibroblast subclusters")p2b <- DimPlot(fib,reduction="umap",group.by="condition",split.by="condition",raster=TRUE) + ggtitle("B  Condition")scprop <- fib@meta.data %>% count(orig.ident,condition,subcluster) %>% group_by(orig.ident) %>% mutate(proportion=n/sum(n))p2c <- ggplot(scprop,aes(subcluster,proportion,fill=condition)) + geom_boxplot(outlier.shape=NA,position=position_dodge(.75)) +  geom_point(aes(group=condition),position=position_jitterdodge(jitter.width=.08,dodge.width=.75),size=1.7) +  scale_y_continuous(labels=percent) + theme_classic() + labs(x=NULL,y="Within-sample proportion")main <- subset(fib, subset=fibroblast_type != "Minor/excluded")p2e <- DimPlot(main,reduction="umap",group.by="fibroblast_type",label=TRUE,repel=TRUE,raster=TRUE) + ggtitle("D  Four main fibroblast populations")typeprop <- main@meta.data %>% count(orig.ident,condition,fibroblast_type) %>% group_by(orig.ident) %>% mutate(proportion=n/sum(n))p2f <- ggplot(typeprop,aes(fibroblast_type,proportion,fill=condition)) + geom_boxplot(outlier.shape=NA,position=position_dodge(.75)) +  geom_point(position=position_jitterdodge(jitter.width=.08,dodge.width=.75),size=1.7) +  scale_y_continuous(labels=percent) + theme_classic() + theme(axis.text.x=element_text(angle=25,hjust=1)) + labs(x=NULL,y="Within-sample proportion")fig2 <- (p2a | p2b) / (p2c | p2e) / p2f + plot_annotation(title="Figure 2 — Fibroblast heterogeneity")ggsave("results/figures/Figure2_fibroblast_subclusters.png",fig2,width=16,height=15,dpi=300)ggsave("results/figures/Figure2_fibroblast_subclusters.pdf",fig2,width=16,height=15)
DefaultAssay(main) <- "RNA"genes <- c("POSTN","COL11A1","COMP","ASPN","COL12A1","COL5A2","NREP","ADAM12","TNFRSF12A","CD9","ACTA2")p3a <- FeaturePlot(main,features=c("POSTN","COL11A1"),split.by="condition",ncol=2,order=TRUE,raster=TRUE,cols=c("grey92","#b2182b"),max.cutoff="q95")p3c <- VlnPlot(main,features=genes,group.by="fibroblast_type",stack=TRUE,flip=TRUE,pt.size=0) + NoLegend()fig3 <- p3a / p3c + plot_annotation(title="Figure 3 — Mesenchymal-fibroblast characteristics")ggsave("results/figures/Figure3_mesenchymal_markers.png",fig3,width=14,height=15,dpi=300)ggsave("results/figures/Figure3_mesenchymal_markers.pdf",fig3,width=14,height=15)
# ACTA2-positive definition follows detectable expression (>0), matching the paper.acta <- FetchData(main,vars=c("ACTA2","fibroblast_type","condition","orig.ident")) %>% mutate(ACTA2_positive=ACTA2>0)acta_summary <- acta %>% group_by(orig.ident,condition,fibroblast_type) %>% summarise(n=n(),ACTA2_pos=sum(ACTA2_positive),pct=mean(ACTA2_positive),.groups="drop")write.csv(acta_summary,"results/tables/ACTA2_myofibroblast_summary.csv",row.names=FALSE)writeLines(capture.output(sessionInfo()), "logs/sessionInfo_main_figures.txt")
```

**向下滑查看更多代码**

**03_differential_enrichment_pseudotime.R**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# ============================================================# GSE163973 Analysis - Final Completion# Fix DE heatmap + Enrichment + TF + Trajectory# ============================================================library(Seurat)library(ggplot2)library(dplyr)library(patchwork)library(RColorBrewer)library(pheatmap)

#!/usr/bin/env RscriptsuppressPackageStartupMessages({  library(Seurat); library(dplyr); library(ggplot2); library(patchwork)  library(clusterProfiler); library(org.Hs.eg.db); library(enrichplot); library(destiny)})set.seed(20210617)all <- readRDS("objects/author_all_cells_annotated.rds")fib <- readRDS("objects/author_fibroblasts_annotated.rds")DefaultAssay(all) <- "RNA"; DefaultAssay(fib) <- "RNA"
# Figure 1g: KL versus NS within each lineage containing >100 cells/group.de_counts <- list(); de_tables <- list()for(ct in unique(all$cellType)) {  x <- subset(all, subset=cellType==ct)  if(min(table(x$condition)) <= 100) next  Idents(x) <- "condition"  de <- FindMarkers(x,ident.1="Keloid",ident.2="Normal scar",test.use="wilcox",logfc.threshold=.5)  de$gene <- rownames(de); de$cell_type <- ct  de_tables[[ct]] <- de  fc <- if("avg_log2FC" %in% names(de)) de$avg_log2FC else de$avg_logFC  de_counts[[ct]] <- data.frame(cell_type=ct,up=sum(de$p_val_adj < .05 & fc > .5),down=sum(de$p_val_adj < .05 & fc < -.5))}de_all <- bind_rows(de_tables); write.csv(de_all,"results/tables/DE_Keloid_vs_Normal_by_celltype.csv",row.names=FALSE)dc <- bind_rows(de_counts) %>% tidyr::pivot_longer(c(up,down),names_to="direction",values_to="genes")pde <- ggplot(dc,aes(reorder(cell_type,genes),genes,fill=direction)) + geom_col(position="dodge") + coord_flip() + theme_classic() + labs(x=NULL,y="DE genes (|log2FC| > 0.5, FDR < 0.05)")ggsave("results/figures/Figure1G_DE_gene_counts.png",pde,width=7,height=5,dpi=300)ggsave("results/figures/Figure1G_DE_gene_counts.pdf",pde,width=7,height=5)
# Main fibroblast types only.main <- subset(fib, subset=fibroblast_type != "Minor/excluded")Idents(main) <- "fibroblast_type"markers <- FindAllMarkers(main,only.pos=TRUE,logfc.threshold=.5,test.use="wilcox")write.csv(markers,"results/tables/fibroblast_type_markers.csv",row.names=FALSE)
# Mesenchymal KL versus NS and GO BP.mes <- subset(main, subset=fibroblast_type=="Mesenchymal")Idents(mes) <- "condition"mes_de <- FindMarkers(mes,ident.1="Keloid",ident.2="Normal scar",logfc.threshold=.5,test.use="wilcox")mes_de$gene <- rownames(mes_de); write.csv(mes_de,"results/tables/DE_mesenchymal_Keloid_vs_Normal.csv",row.names=FALSE)fc_col <- if("avg_log2FC" %in% names(mes_de)) "avg_log2FC" else "avg_logFC"up <- mes_de$gene[mes_de$p_val_adj<.05 & mes_de[[fc_col]]>.5]ent <- bitr(up,fromType="SYMBOL",toType="ENTREZID",OrgDb=org.Hs.eg.db)ego <- enrichGO(unique(ent$ENTREZID),OrgDb=org.Hs.eg.db,ont="BP",pAdjustMethod="BH",readable=TRUE)write.csv(as.data.frame(ego),"results/tables/GO_mesenchymal_Keloid_up.csv",row.names=FALSE)if(nrow(as.data.frame(ego))>0) {  pgo <- dotplot(ego,showCategory=15) + ggtitle("GO BP: keloid mesenchymal fibroblasts")  ggsave("results/figures/Figure2H_GO_mesenchymal_Keloid_up.png",pgo,width=9,height=6,dpi=300)  ggsave("results/figures/Figure2H_GO_mesenchymal_Keloid_up.pdf",pgo,width=9,height=6)}
# Figure 6: DPT of KL sC1/sC4; k=100 as specified in Methods.traj <- subset(fib, subset=condition=="Keloid" & subcluster %in% c("sC1","sC4"))DefaultAssay(traj) <- "RNA"mat <- GetAssayData(traj,layer="data")vars <- head(VariableFeatures(fib),2000)if(length(vars)<100) vars <- rownames(mat)[Matrix::rowMeans(mat>0)>.05]vars <- intersect(vars,rownames(mat)); mat <- mat[vars,]dm <- DiffusionMap(t(as.matrix(mat)),k=100,n_eigs=10)# Orient DPT so the sC4-enriched end is early.candidate <- which(traj$subcluster=="sC4")root <- candidate[which.max(eigenvectors(dm)[candidate,1])]dpt <- DPT(dm,tips=root)pt <- as.numeric(dpt$dpt)traj$DPT <- ptemb <- data.frame(DC1=eigenvectors(dm)[,1],DC2=eigenvectors(dm)[,2],DPT=pt,                  subcluster=traj$subcluster,sample=traj$orig.ident,                  POSTN=FetchData(traj,"POSTN")[,1])write.csv(cbind(cell=rownames(emb),emb),"results/tables/DPT_sC1_sC4_Keloid.csv",row.names=FALSE)p6a <- ggplot(emb,aes(DC1,DC2,color=subcluster))+geom_point(size=.45)+theme_classic()+labs(color=NULL,title="A  Subcluster")p6b <- ggplot(emb,aes(DC1,DC2,color=sample))+geom_point(size=.45)+theme_classic()+labs(color=NULL,title="B  Patient")p6c <- ggplot(emb,aes(DC1,DC2,color=POSTN))+geom_point(size=.45)+scale_color_viridis_c()+theme_classic()+ggtitle("C  POSTN")p6d <- ggplot(emb,aes(DC1,DC2,color=DPT))+geom_point(size=.45)+scale_color_viridis_c(option="magma")+theme_classic()+ggtitle("D  Diffusion pseudotime")fig6 <- (p6a|p6b)/(p6c|p6d)+plot_annotation(title="Figure 6 — sC4 to sC1 diffusion-pseudotime")ggsave("results/figures/Figure6_DPT.png",fig6,width=12,height=10,dpi=300)ggsave("results/figures/Figure6_DPT.pdf",fig6,width=12,height=10)
Idents(traj) <- "subcluster"sc4 <- FindMarkers(traj,ident.1="sC4",ident.2="sC1",logfc.threshold=0,test.use="wilcox")sc4$gene <- rownames(sc4); write.csv(sc4,"results/tables/DE_sC4_vs_sC1_Keloid.csv",row.names=FALSE)saveRDS(traj,"objects/keloid_sC1_sC4_DPT.rds",compress=FALSE)writeLines(capture.output(sessionInfo()),"logs/sessionInfo_DE_DPT.txt")
```

**向下滑查看更多代码**

**
**

04_cellchat.R

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
#!/usr/bin/env RscriptsuppressPackageStartupMessages({library(Seurat);library(CellChat);library(patchwork);library(ggplot2)})set.seed(20210617)all <- readRDS("objects/author_all_cells_annotated.rds")fib <- readRDS("objects/author_fibroblasts_annotated.rds")# Replace whole-atlas fibroblast labels with the four main fibroblast populations.# Seurat integration regenerated numeric barcode suffixes independently; sample +# unsuffixed 10x barcode is the stable cross-object key.cell_key <- function(o) paste(o$orig.ident, sub("_[0-9]+$", "", colnames(o)), sep="|")all_key <- cell_key(all); fib_key <- cell_key(fib)all$communication_group <- as.character(all$cellType)ft <- setNames(as.character(fib$fibroblast_type),fib_key)is_fib <- all$cellType == "Fibroblast"all$communication_group[is_fib] <- unname(ft[all_key[is_fib]])# 21/13,437 author-atlas fibroblasts are absent from the released fibroblast# object; exclude these rather than inventing a subtype.all <- subset(all,cells=colnames(all)[!is.na(all$communication_group) & all$communication_group!="Minor/excluded"])DefaultAssay(all) <- "RNA"db <- subsetDB(CellChatDB.human,search="Secreted Signaling")run_one <- function(cond) {  x <- subset(all,cells=colnames(all)[all$condition == cond])  expr <- GetAssayData(x,assay="RNA",layer="data")  meta <- data.frame(group=x$communication_group,row.names=colnames(x))  cc <- createCellChat(expr,meta=meta,group.by="group")  cc@DB <- db  cc <- subsetData(cc)  cc <- identifyOverExpressedGenes(cc)  cc <- identifyOverExpressedInteractions(cc)  # No PPI-projected matrix is constructed here, so use normalized RNA data.  cc <- computeCommunProb(cc,raw.use=TRUE,population.size=TRUE)  cc <- filterCommunication(cc,min.cells=10)  cc <- computeCommunProbPathway(cc)  aggregateNet(cc)}kl <- run_one("Keloid"); ns <- run_one("Normal scar")saveRDS(kl,"objects/cellchat_Keloid.rds");saveRDS(ns,"objects/cellchat_Normal_scar.rds")write.csv(subsetCommunication(kl),"results/tables/CellChat_Keloid_interactions.csv",row.names=FALSE)write.csv(subsetCommunication(ns),"results/tables/CellChat_Normal_scar_interactions.csv",row.names=FALSE)png("results/figures/Figure4_CellChat_Keloid.png",width=2400,height=2200,res=260)netVisual_circle(kl@net$count,vertex.weight=as.numeric(table(kl@idents)),weight.scale=TRUE,label.edge=FALSE,title.name="Keloid interaction counts")dev.off()png("results/figures/Figure4_CellChat_Normal_scar.png",width=2400,height=2200,res=260)netVisual_circle(ns@net$count,vertex.weight=as.numeric(table(ns@idents)),weight.scale=TRUE,label.edge=FALSE,title.name="Normal-scar interaction counts")dev.off()for(sig in c("TGFb","POSTN","PDGF","VEGF","NOTCH","FGF")) if(sig %in% kl@netP$pathways) {  png(paste0("results/figures/Figure4_Keloid_",sig,".png"),width=2400,height=2200,res=260)  netVisual_aggregate(kl,signaling=sig,layout="circle");dev.off()}writeLines(capture.output(sessionInfo()),"logs/sessionInfo_CellChat.txt")
```

`
`

05_velocity_from_bam.sh

  *   *   *   *   *   *   *   *   *   *

```
#!/usr/bin/env bashset -euo pipefail# RNA velocity cannot be reconstructed from the GEO count matrices: spliced and# unspliced molecules are absent. Run this only after supplying each Cell Ranger# output directory (with possorted_genome_bam.bam) under data/cellranger/<sample>.for sample in KF1 KF2 KF3; do  velocyto run10x "data/cellranger/${sample}" data/reference/refdata-cellranger-GRCh38-2.2.0/genes/genes.gtfdone# Continue in velocyto.R/Pagoda2 with the paper settings: top 20 PCs, Euclidean# distance, gene-relative model, k=100, then project onto Figure 6 DPT space.
```

**
**

三、省Token指南

我们已经基于同一指令，分别在Claude Code、Codex、[DeepSeek](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538520&idx=1&sn=6858ae5260580c74fd46e658dbc4e49b&scene=21#wechat_redirect>)上完成对比测试，对三者的输出效果与Token消耗情况有了直观感受，各工具均有自身的优势与短板。

我们在实际项目中，跟AI工具对话肯定不是一句话就能结束的。而且我们使用AI工具的最想要的是：让AI的输出贴合预期效果，同时尽可能控制使用成本。想要实现这一目标，可以做好下面这几件事，

· 理解Token消耗规则一一输入输出5倍关系、缓存命中打一折、滚雪球效应（之前我们已经分享了：[DeepSeek继峰谷收费模式后，再度涨价！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541071&idx=1&sn=568a89e05cc332b242fbed2b8db928e8&scene=21#wechat_redirect>)）

· 掌握提示词结构一一背景+需求+要求，一轮到位不废话

· 学会文件投喂技巧——Python搬砖不花钱，AI才花钱

· 梳理CLAUDE.md配置文件——写一次规则，以后每次自动执

· 了解.claude文件夹和Skills管理一一哪些能删、哪些不能删

· 掌握临时保存和恢复工作进度一-4种方式（存Memory、存MD文档、Memory+MD、/resume）对比选最优

Token消耗的三条省钱小妙招

规则| 说明| 影响
---|---|---
输入两折，输出全价| 发1个字等于AI回复5个字| 输出比输入贵5倍
缓存命中打一折| AI记住了之前的需求，下次自动调用| 命中缓存能省90%费用
对话轮数滚雪球| 第10轮会重新看前9轮，越聊越贵| 对话轮数越少越好

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**欢迎交流**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家一起讨论。![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24)您点的每个赞和在看，我都认真当成了喜欢
