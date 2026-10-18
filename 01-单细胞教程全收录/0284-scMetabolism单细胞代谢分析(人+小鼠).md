---
title: "scMetabolism单细胞代谢分析(人+小鼠)"
date: 2026-07-02
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539046&idx=1&sn=509645075f925860d621b8e5b5a9a196&chksm=9b3c2036ac4ba9207f05bea7f5051680a7bd31f895cf05b4cbfc328525d1d9fc15d73b6eb601#rd
albums: ["单细胞教程全收录"]
---

# scMetabolism单细胞代谢分析(人+小鼠)

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539046&idx=1&sn=509645075f925860d621b8e5b5a9a196&chksm=9b3c2036ac4ba9207f05bea7f5051680a7bd31f895cf05b4cbfc328525d1d9fc15d73b6eb601#rd
> 合集：单细胞教程全收录

**一、写在前面**

scMetabolism 是发表在 Cancer Discovery 一个用于[单细胞转录组数据](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)代谢活性评估的 R 包，主要目标是在单细胞分辨率下推断不同细胞、细胞群或实验条件中的代谢通路活性。与传统[差异基因分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=2&sn=d8c4ebf8f63d12bd2ac8e2607864f322&scene=21#wechat_redirect>)不同，scMetabolism 关注的是“通路层面”的代谢状态：它根据代谢相关基因集，对每个细胞的糖酵解、氧化磷酸化、TCA 循环、脂肪酸代谢、氨基酸代谢等通路进行打分，从而帮助研究者理解细胞功能状态、免疫微环境变化、肿瘤代谢重编程以及不同细胞类型之间的代谢异质性。

更多单细胞教程可见：[趁着暑假拿捏单细胞，带着分析技能入组](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538847&idx=1&sn=2ad605c6d70d4e6ee921fda1798bfd8b&scene=21#wechat_redirect>)

![截屏2026-05-25 15.37.34](../../images/a0ec8d4f7f69f2c0.webp)

该工具支持基于 Seurat 对象或普通表达矩阵进行分析，内置[ KEGG](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490795&idx=1&sn=65dbe1a8e026466d0c5ce391c823c215&scene=21#wechat_redirect>) 和 Reactome 代谢通路基因集，其中 KEGG 包含 85 条代谢通路，Reactome 包含 82 条代谢通路。[评分算法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497831&idx=2&sn=82fa51c76a381fba0b444e9b6b23eb5f&scene=21#wechat_redirect>)方面，scMetabolism 支持 VISION、[AUCell](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&scene=21#wechat_redirect>)、ssGSEA 和 [GSVA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&scene=21#wechat_redirect>) 等方法，并提供可选的数据插补功能。计算完成后，代谢评分会以矩阵形式保存，可以进一步结合细胞注释、分组信息或降维结果进行可视化和统计比较。

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469&token=827157490&lang=zh_CN#wechat_redirect>)、自测数据个性化分析辅导、[实验科研服务](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=1&sn=578993fdfa060d38c80e2df6fc200c39&scene=21&token=2103718893&lang=zh_CN&poc_token=HJGfHmqjXvxSF975KYZOUi-ADSn9_E6PyDzhb2zM#wechat_redirect>)和[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537678&idx=2&sn=1d329f22e35586dc794ce30aa6bd0ce4&scene=21&token=2103718893&lang=zh_CN&poc_token=HMSfHmqjNvuep9CuChyf19pUrcVxme3JNuT0h6zV#wechat_redirect>)，欢迎后台交流。

**二、实操流程**
```
1. 下载安装包
```

  *   *   *   *   *   *   *   *   *   *   *

```
# 可选：如果没有安装devtools与remotes需要安装这两个包install.packages("devtools")install.packages("remotes")# 进行安装library(devtools)library(remotes)remotes::install_github("cran/loe")install_local("./pkg/VISION-2.1.0.tar.gz")install_local("./pkg/scMetabolism-main.zip")# 小鼠基因同源转化需要devtools::install_github("saeyslab/nichenetr")
```

如果是macOS在安装loe包时会遇到如下报错

![截屏2026-05-26 14.08.58](../../images/e8cc16143f6d98d5.webp)

需要在官方页面（https://mac.r-project.org/tools/）下载gfortran-14.2-universal.pkg进行安装，下载完成后直接双击打开进行安装即可。安装完成后重启R再此安装即可成功

2\. 人类样本代谢分析流程

首先加载数据并进行简单的浏览

  *   *   *   *   *

```r
# 加载函数sce.all.int <- readRDS('./data/Human_sce_epi.rds')FeaturePlot(sce.all.int,features = "EPCAM")table(sce.all.int$RNA_snn_res.0.01)DimPlot(sce.all.int,group.by = "RNA_snn_res.0.01",label = T)
```

![截屏2026-05-26 15.11.44](../../images/4953f2126b0c9007.webp)

如果你使用的[seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537631&idx=1&sn=b702b29384fd4f4878cc0b4d0fcf51e7&scene=21#wechat_redirect>)版本是v5版本，在使用此包前需要先要修改一下函数

  *   *   *   *

```r
# 执行后会打开如下弹窗，进行修改fix(sc.metabolism.Seurat)#把countexp读取counts代码修改为countexp <- LayerData(obj, assay = "RNA", layer = "counts")
```

![scmet_1](../../images/3af7efd4f0f35b4f.webp)

接着载入功能函数，使用source函数加载

  *   *

```
# 加载函数source('./functions/Human_sc_metabolism.R')
```

此函数可以按照下述方法使用，会自动进行代谢分析流程，并保存点图

  *   *   *   *   *   *   *   *   *   *   *

```r
# 设置基本seurat_obj <- sce.all.int # 上述单细胞数据group_col <- "RNA_snn_res.0.01" # 你所关注的注释（为后续点图的横坐标）out_dir <- file.path(getwd(), "scMetabolism", "epi-human") # 输出文件保存位置method <- "AUCell" # 富集通路时选择的方法（VISION, AUCell, ssgsea and gsva）imputation <- FALSE # 是否对单细胞表达矩阵做表达值补全 / 平滑。ncores_by_type <- c(KEGG = 10, REACTOME = 10) # 使用的运算核心数chunk_size <- 20 # 绘制点图时多少个通路绘制在一张图中plot_width <- 8 # 点图宽度plot_height <- 7 # 点图高度metabolism_types <- c("KEGG", "REACTOME") # 进行分析基因集
```

设置好参数后就可以运行下述代码进行代谢分析

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 代谢分析seurat_obj <- prepare_seurat_v5_counts(seurat_obj, assay = "RNA")base_obj <- seurat_objfor (metabolism_type in metabolism_types) {  result_obj <- run_scmetabolism_one_type(    obj = base_obj,    metabolism_type = metabolism_type,    group_col = group_col,    output_root = out_dir,    method = method,    imputation = imputation,    ncores = unname(ncores_by_type[[metabolism_type]]),    chunk_size = chunk_size,    plot_width = plot_width,    plot_height = plot_height  )}
```

上述函数会自动进行矩阵的预处理，执行scMetabolism的代谢分析，并挑选出在所选分组中有变化的通路，接着绘制点图保存在指定文件夹内，执行结束后文件夹结构如下：

![截屏2026-05-26 15.38.21](../../images/1a6288d21838e3c3.webp)

valid_pathways.csv文件中是所选出在各组中有变化的通路名，matrix.rds文件则是代谢分析的结果文件，点图内容则如下所示

![截屏2026-05-26 15.41.00](../../images/b8af77f54c779372.webp)

接着可以利用matrix.rds此进一步绘图。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 载入matrix.rds数据pathways_matrix <- readRDS("~/work/scMetabolism_test/scMetabolism/epi-human/kegg/kegg_epi_core_matrix.rds")pathways_matrix[1:5,1:5]# 挑选通路进一步可视化#pathways_to_add <- rownames(pathways_matrix)pathways_to_add <- c(  "Glycolysis / Gluconeogenesis",  "Pentose phosphate pathway")common_cells <- intersect(colnames(pathways_matrix), rownames(sce.all.int@meta.data))for (pw in pathways_to_add) {  meta_col <- pw  sce.all.int@meta.data[common_cells, meta_col] <- as.numeric(pathways_matrix[pw, common_cells])}head(sce.all.int$"Glycolysis / Gluconeogenesis")FeaturePlot(sce.all.int,             features = pathways_to_add,            cols = c("gray90","#C1362B") ,order = T)
```

![截屏2026-05-26 15.45.02](../../images/31b8fa9f934bb766.webp)

```
3. 小鼠样本代谢分析流程
```

首先加载数据并进行简单的浏览

  *   *   *   *   *   *

```r
# 载入并浏览数据sce.all.int <- readRDS('./data/Mouse_sce_endo.rds')DimPlot(sce.all.int, group.by = "celltype", label = T)FeaturePlot(sce.all.int,features = "Pecam1")table(sce.all.int$RNA_snn_res.0.3)DimPlot(sce.all.int,group.by = "RNA_snn_res.0.3",label = T)
```

![截屏2026-05-26 15.49.55](../../images/1cf6f594a462fe9b.webp)

与人类样本流程相同，如果你使用的seurat版本是v5版本，在使用此包前也需要先要修改一下函数

  *   *   *   *

```r
# 执行后会打开如下弹窗，进行修改fix(sc.metabolism.Seurat)#把countexp读取counts代码修改为countexp <- LayerData(obj, assay = "RNA", layer = "counts")
```

接着载入功能函数，使用source函数加载

  *   *

```
# 加载函数source('./functions/Mouse_sc_metabolism.R')
```

此函数可以按照下述方法使用，会自动进行代谢分析流程，并保存点图

  *   *   *   *   *   *   *   *   *   *   *

```r
# 设置基本seurat_obj <- sce.all.int # 上述单细胞数据group_col <- "RNA_snn_res.0.3" # 你所关注的注释（为后续点图的横坐标）out_dir <- file.path(getwd(), "scMetabolism", "endo-mouse") # 输出文件保存位置method <- "AUCell" # 富集通路时选择的方法（VISION, AUCell, ssgsea and gsva）imputation <- FALSE # 是否对单细胞表达矩阵做表达值补全 / 平滑。ncores_by_type <- c(KEGG = 10, REACTOME = 10) # 使用的运算核心数chunk_size <- 20 # 绘制点图时多少个通路绘制在一张图中plot_width <- 8 # 点图宽度plot_height <- 7 # 点图高度metabolism_types <- c("KEGG", "REACTOME") # 进行分析基因集
```

设置好参数后就可以运行下述代码进行代谢分析

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)prepared_input <- prepare_mouse_scmetabolism_input(  obj = seurat_obj,  assay = "RNA",  layer = "counts")base_obj <- prepared_input$objcounts_human <- prepared_input$counts_humangene_map <- prepared_input$gene_mapmetabolism_results <- list()for (metabolism_type in metabolism_types) {  metabolism_results[[metabolism_type]] <- run_mouse_scmetabolism_one_type(    obj = base_obj,    counts_human = counts_human,    gene_map = gene_map,    metabolism_type = metabolism_type,    group_col = group_col,    output_root = out_dir,    method = method,    imputation = imputation,    ncores = get_ncores(metabolism_type, ncores_by_type),    chunk_size = chunk_size,    plot_width = plot_width,    plot_height = plot_height  )}
```

与人类样本流程不同，小鼠样本的处理流程是提取出表达矩阵后，进行了同源转换为了人类基因名，再进行计算代谢通路，接着挑选出在所选分组中有变化的通路，接着绘制点图保存在指定文件夹内，执行结束后文件夹结构如下：

![截屏2026-05-26 16.03.17](../../images/4cef3a7c4a348660.webp)

valid_pathways.csv文件中是所选出在各组中有变化的通路名，matrix.rds文件则是代谢分析的结果文件，会比人类样本流程中多一个基因转化的对应文件mouse_to_human_gene_map.csv，点图内容则如下所示

![截屏2026-05-26 16.04.09](../../images/acd630f738c523cd.webp)

接着可以利用matrix.rds此进一步绘图。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# 挑选通路进一步可视化pathways_matrix <- readRDS("~/work/scMetabolism_test/scMetabolism/endo-mouse/kegg/kegg_mouse_metabolism_score_matrix.rds")pathways_matrix[1:5,1:5]#pathways_to_add <- rownames(pathways_matrix)pathways_to_add <- c(  "Glycolysis / Gluconeogenesis",  "Pentose phosphate pathway")common_cells <- intersect(colnames(pathways_matrix), rownames(sce.all.int@meta.data))for (pw in pathways_to_add) {  meta_col <- pw  sce.all.int@meta.data[common_cells, meta_col] <- as.numeric(pathways_matrix[pw, common_cells])}head(sce.all.int$"Glycolysis / Gluconeogenesis")FeaturePlot(sce.all.int,             features = pathways_to_add,            cols = c("gray90","#C1362B") ,order = T)
```

4.功能函数

Human_sc_metabolism.R内容如下

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
## Standard scMetabolism workflow for Seurat object## Prerequisite: sce.all.int already exists in the current R session.library(Seurat)library(scMetabolism)library(ggplot2)library(rsvd)prepare_seurat_v5_counts <- function(obj, assay = "RNA") {  ## scMetabolism may expect a counts slot. In Seurat v5, counts can be stored  ## as a layer, so JoinLayers helps expose a conventional layer structure.  if ("JoinLayers" %in% getNamespaceExports("Seurat")) {    obj <- JoinLayers(obj)  }  counts_ok <- tryCatch({    counts_mat <- LayerData(obj, assay = assay, layer = "counts")    !is.null(counts_mat) && nrow(counts_mat) > 0 && ncol(counts_mat) > 0  }, error = function(e) {    FALSE  })  if (!counts_ok) {    stop(      "Cannot find RNA counts layer. Please check: ",      "LayerData(obj, assay = 'RNA', layer = 'counts')"    )  }  obj}get_metabolism_score_matrix <- function(obj) {  score_matrix <- tryCatch({    as.matrix(obj@assays$METABOLISM$score)  }, error = function(e) {    NULL  })  if (is.null(score_matrix)) {    score_matrix <- tryCatch({      as.matrix(LayerData(obj, assay = "METABOLISM", layer = "score"))    }, error = function(e) {      NULL    })  }  if (is.null(score_matrix)) {    stop("Cannot extract METABOLISM score matrix from the Seurat object.")  }  score_matrix}get_variable_pathways_by_group_median <- function(score_matrix, group_labels) {  keep <- vapply(    rownames(score_matrix),    FUN.VALUE = logical(1),    FUN = function(pathway) {      medians <- tapply(score_matrix[pathway, ], group_labels, median, na.rm = TRUE)      medians <- medians[is.finite(medians)]      length(medians) >= 2 && max(medians) > min(medians)    }  )  rownames(score_matrix)[keep]}save_dotplots_by_chunks <- function(    obj,    pathways,    phenotype,    output_dir,    chunk_size = 20,    width = 8,    height = 7) {  if (length(pathways) == 0) {    warning("No valid pathways found. DotPlot files will not be generated.")    return(invisible(NULL))  }  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)  pathway_groups <- split(pathways, ceiling(seq_along(pathways) / chunk_size))  for (i in seq_along(pathway_groups)) {    current_pathways <- pathway_groups[[i]]    start_idx <- (i - 1) * chunk_size + 1    end_idx <- start_idx + length(current_pathways) - 1    p <- DotPlot.metabolism(      obj = obj,      pathway = current_pathways,      phenotype = phenotype,      norm = "y"    )    file_name <- sprintf("Metabolism_Dotplot_Group_%02d.pdf", i)    file_path <- file.path(output_dir, file_name)    message(sprintf(      "Saving %s: valid pathways %d-%d",      file_name, start_idx, end_idx    ))    ggsave(      filename = file_path,      plot = p,      width = width,      height = height,      device = cairo_pdf    )  }  invisible(NULL)}run_scmetabolism_one_type <- function(    obj,    metabolism_type,    group_col,    output_root,    method = "AUCell",    imputation = FALSE,    ncores = 5,    chunk_size = 20,    plot_width = 8,    plot_height = 7) {  if (!group_col %in% colnames(obj@meta.data)) {    stop(sprintf("Column '%s' is not found in obj@meta.data.", group_col))  }  output_dir <- file.path(output_root, tolower(metabolism_type))  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)  message(sprintf("\n===== Running scMetabolism: %s =====", metabolism_type))  obj <- sc.metabolism.Seurat(    obj = obj,    method = method,    imputation = imputation,    ncores = ncores,    metabolism.type = metabolism_type  )  score_matrix <- get_metabolism_score_matrix(obj)  group_labels <- obj@meta.data[[group_col]]  valid_pathways <- get_variable_pathways_by_group_median(    score_matrix = score_matrix,    group_labels = group_labels  )  message(sprintf("Original pathways: %d", nrow(score_matrix)))  message(sprintf("Valid pathways: %d", length(valid_pathways)))  saveRDS(    score_matrix,    file = file.path(output_dir, sprintf("%s_epi_core_matrix.rds", tolower(metabolism_type)))  )  write.csv(    data.frame(pathway = valid_pathways),    file = file.path(output_dir, sprintf("%s_valid_pathways.csv", tolower(metabolism_type))),    row.names = FALSE  )  save_dotplots_by_chunks(    obj = obj,    pathways = valid_pathways,    phenotype = group_col,    output_dir = output_dir,    chunk_size = chunk_size,    width = plot_width,    height = plot_height  )  obj}
```

Mouse_sc_metabolism.R内容如下

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
## Standard mouse scMetabolism workflow for Seurat object## Prerequisite: sce.all.int already exists in the current R session.#### Mouse genes are converted to human symbols before running scMetabolism,## because scMetabolism pathway gene sets are human-centered.library(Seurat)library(Matrix)library(ggplot2)library(nichenetr)library(scMetabolism)range01_safe <- function(x) {  r <- range(x, na.rm = TRUE)  if (!all(is.finite(r)) || r[1] == r[2]) {    return(rep(0, length(x)))  }  (x - r[1]) / (r[2] - r[1])}get_ncores <- function(metabolism_type, ncores_by_type, default = 5) {  if (metabolism_type %in% names(ncores_by_type)) {    return(unname(ncores_by_type[[metabolism_type]]))  }  default}get_group_order <- function(group_labels) {  if (is.factor(group_labels)) {    return(levels(droplevels(group_labels)))  }  group_labels <- group_labels[!is.na(group_labels)]  if (is.numeric(group_labels) || is.integer(group_labels)) {    return(as.character(sort(unique(group_labels))))  }  group_labels <- as.character(group_labels)  group_values <- unique(group_labels)  numeric_values <- suppressWarnings(as.numeric(group_values))  if (all(!is.na(numeric_values))) {    return(group_values[order(numeric_values)])  }  sort(group_values)}prepare_seurat_v5_counts <- function(obj, assay = "RNA", layer = "counts") {  if (!assay %in% Assays(obj)) {    stop("Cannot find assay: ", assay)  }  if (inherits(obj[[assay]], "Assay5")) {    if (!layer %in% Layers(obj[[assay]])) {      layer_matches <- Layers(obj[[assay]], search = paste0("^", layer))      if (length(layer_matches) > 1) {        message("Detected multiple ", layer, " layers. Running JoinLayers() ...")        obj <- tryCatch({          JoinLayers(obj, assay = assay)        }, error = function(e) {          obj[[assay]] <- JoinLayers(obj[[assay]])          obj        })      } else if (length(layer_matches) == 1) {        message("Using matched layer: ", layer_matches)        layer <- layer_matches      }    }    if (!layer %in% Layers(obj[[assay]])) {      stop(        "Cannot find layer = ", layer, " in assay = ", assay,        ". Available layers: ", paste(Layers(obj[[assay]]), collapse = ", ")      )    }    counts <- LayerData(obj, assay = assay, layer = layer)  } else {    counts <- tryCatch({      GetAssayData(obj, assay = assay, layer = layer)    }, error = function(e) {      GetAssayData(obj, assay = assay, slot = layer)    })  }  if (is.null(rownames(counts))) {    stop("The expression matrix has no rownames.")  }  list(obj = obj, counts = counts)}convert_mouse_counts_to_human <- function(counts) {  gene_map <- data.frame(    mouse = rownames(counts),    human = nichenetr::convert_mouse_to_human_symbols(rownames(counts)),    stringsAsFactors = FALSE  )  gene_map <- gene_map[!is.na(gene_map$human) & gene_map$human != "", ]  if (nrow(gene_map) == 0) {    stop("No mouse genes were converted to human symbols.")  }  counts <- counts[gene_map$mouse, , drop = FALSE]  human_factor <- factor(gene_map$human, levels = unique(gene_map$human))  mapper <- Matrix::sparseMatrix(    i = seq_along(human_factor),    j = as.integer(human_factor),    x = 1,    dims = c(length(human_factor), nlevels(human_factor)),    dimnames = list(NULL, levels(human_factor))  )  counts_human <- Matrix::t(mapper) %*% counts  rownames(counts_human) <- levels(human_factor)  colnames(counts_human) <- colnames(counts)  message("Converted and collapsed genes: ", nrow(counts_human))  list(    counts_human = counts_human,    gene_map = gene_map  )}prepare_mouse_scmetabolism_input <- function(obj, assay = "RNA", layer = "counts") {  counts_res <- prepare_seurat_v5_counts(    obj = obj,    assay = assay,    layer = layer  )  convert_res <- convert_mouse_counts_to_human(counts_res$counts)  list(    obj = counts_res$obj,    counts_human = convert_res$counts_human,    gene_map = convert_res$gene_map  )}align_metabolism_score_cells <- function(metabolism_score, input_cells) {  score_cells <- colnames(metabolism_score)  if (identical(score_cells, input_cells)) {    return(metabolism_score[, input_cells, drop = FALSE])  }  if (setequal(score_cells, input_cells)) {    return(metabolism_score[, input_cells, drop = FALSE])  }  idx <- match(score_cells, make.names(input_cells, unique = TRUE))  if (all(!is.na(idx))) {    colnames(metabolism_score) <- input_cells[idx]    return(metabolism_score[, input_cells, drop = FALSE])  }  stop(    "Metabolism score cell names cannot be matched to input cells.\n",    "score: ", paste(head(score_cells), collapse = ", "), "\n",    "input: ", paste(head(input_cells), collapse = ", ")  )}calculate_mouse_metabolism_score <- function(    counts_human,    metabolism_type,    method = "AUCell",    imputation = FALSE,    ncores = 5) {  metabolism_type <- match.arg(metabolism_type, c("KEGG", "REACTOME"))  method <- match.arg(method, c("VISION", "AUCell", "ssGSEA", "GSVA"))  metabolism_score <- scMetabolism::sc.metabolism(    countexp = counts_human,    method = method,    imputation = imputation,    ncores = ncores,    metabolism.type = metabolism_type  )  metabolism_score <- as.matrix(metabolism_score)  storage.mode(metabolism_score) <- "numeric"  align_metabolism_score_cells(    metabolism_score = metabolism_score,    input_cells = colnames(counts_human)  )}get_variable_pathways_by_group_median <- function(score_matrix, group_labels) {  keep <- vapply(    rownames(score_matrix),    FUN.VALUE = logical(1),    FUN = function(pathway) {      medians <- tapply(score_matrix[pathway, ], group_labels, median, na.rm = TRUE)      medians <- medians[is.finite(medians)]      length(medians) >= 2 && max(medians) > min(medians)    }  )  rownames(score_matrix)[keep]}DotPlot.metabolism.safe <- function(    score_matrix,    meta,    pathway,    phenotype,    norm = "y") {  if (!phenotype %in% colnames(meta)) {    stop("Cannot find phenotype column: ", phenotype)  }  meta <- meta[colnames(score_matrix), , drop = FALSE]  group_labels <- as.character(meta[[phenotype]])  group_order <- get_group_order(meta[[phenotype]])  score_sub <- score_matrix[pathway, rownames(meta), drop = FALSE]  plot_df <- data.frame(    group = rep(group_labels, times = length(pathway)),    pathway = rep(pathway, each = nrow(meta)),    score = as.numeric(as.vector(t(score_sub))),    stringsAsFactors = FALSE  )  plot_df <- plot_df[!is.na(plot_df$group), , drop = FALSE]  med_df <- aggregate(    plot_df$score,    by = list(group = plot_df$group, pathway = plot_df$pathway),    FUN = median,    na.rm = TRUE  )  colnames(med_df)[3] <- "median_score"  med_df$value <- med_df$median_score  if (norm == "y") {    med_df$value <- ave(med_df$median_score, med_df$pathway, FUN = range01_safe)  } else if (norm == "x") {    med_df$value <- ave(med_df$median_score, med_df$group, FUN = range01_safe)  } else if (!norm %in% c("na", "none", "raw")) {    stop("norm must be one of: y, x, na, none, raw")  }  med_df$group <- factor(med_df$group, levels = group_order)  med_df$pathway <- factor(med_df$pathway, levels = rev(pathway))  ggplot(med_df, aes(x = group, y = pathway, color = value, size = value)) +    geom_point() +    scale_color_gradientn(colors = c("#2166AC", "#F7F7F7", "#B2182B")) +    scale_size_continuous(range = c(1.5, 6)) +    labs(x = phenotype, y = "Metabolic Pathway", color = "Value", size = "Value") +    theme_bw() +    theme(      axis.text.x = element_text(angle = 45, hjust = 1),      panel.grid.minor = element_blank(),      panel.grid.major = element_blank()    )}save_dotplots_by_chunks <- function(    score_matrix,    meta,    pathways,    phenotype,    output_dir,    chunk_size = 20,    width = 8,    height = 7,    norm = "y") {  if (length(pathways) == 0) {    warning("No valid pathways found. DotPlot files will not be generated.")    return(invisible(NULL))  }  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)  pathway_groups <- split(pathways, ceiling(seq_along(pathways) / chunk_size))  for (i in seq_along(pathway_groups)) {    current_pathways <- pathway_groups[[i]]    start_idx <- (i - 1) * chunk_size + 1    end_idx <- start_idx + length(current_pathways) - 1    p <- DotPlot.metabolism.safe(      score_matrix = score_matrix,      meta = meta,      pathway = current_pathways,      phenotype = phenotype,      norm = norm    )    file_name <- sprintf("Metabolism_Dotplot_Group_%02d.pdf", i)    file_path <- file.path(output_dir, file_name)    message(sprintf(      "Saving %s: valid pathways %d-%d",      file_name, start_idx, end_idx    ))    ggsave(      filename = file_path,      plot = p,      width = width,      height = height,      device = cairo_pdf,      limitsize = FALSE    )  }  invisible(NULL)}run_mouse_scmetabolism_one_type <- function(    obj,    counts_human,    gene_map,    metabolism_type,    group_col,    output_root,    method = "AUCell",    imputation = FALSE,    ncores = 5,    chunk_size = 20,    plot_width = 8,    plot_height = 7,    norm = "y") {  if (!group_col %in% colnames(obj@meta.data)) {    stop(sprintf("Column '%s' is not found in obj@meta.data.", group_col))  }  output_dir <- file.path(output_root, tolower(metabolism_type))  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)  message(sprintf("\n===== Running mouse scMetabolism: %s =====", metabolism_type))  metabolism_score <- calculate_mouse_metabolism_score(    counts_human = counts_human,    metabolism_type = metabolism_type,    method = method,    imputation = imputation,    ncores = ncores  )  obj@assays$METABOLISM <- list(score = metabolism_score)  meta <- obj@meta.data[colnames(metabolism_score), , drop = FALSE]  group_labels <- meta[[group_col]]  valid_pathways <- get_variable_pathways_by_group_median(    score_matrix = metabolism_score,    group_labels = group_labels  )  message(sprintf("Original pathways: %d", nrow(metabolism_score)))  message(sprintf("Valid pathways: %d", length(valid_pathways)))  saveRDS(    metabolism_score,    file = file.path(output_dir, sprintf("%s_mouse_metabolism_score_matrix.rds", tolower(metabolism_type)))  )  write.csv(    gene_map,    file = file.path(output_dir, "mouse_to_human_gene_map.csv"),    row.names = FALSE  )  write.csv(    data.frame(pathway = valid_pathways),    file = file.path(output_dir, sprintf("%s_valid_pathways.csv", tolower(metabolism_type))),    row.names = FALSE  )  save_dotplots_by_chunks(    score_matrix = metabolism_score,    meta = meta,    pathways = valid_pathways,    phenotype = group_col,    output_dir = output_dir,    chunk_size = chunk_size,    width = plot_width,    height = plot_height,    norm = norm  )  list(    obj = obj,    metabolism_score = metabolism_score,    gene_map = gene_map,    valid_pathways = valid_pathways  )}
```

**三、资料领取**

更多编程教程可见：

[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)

[5.5小时掌握R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535038&idx=2&sn=717a8673a8bf82d5ac40af4441a07f65&scene=21#wechat_redirect>)

[8小时掌握生信Python](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537399&idx=1&sn=d14c7987d1384fe133094748844b8d59&scene=21#wechat_redirect>)

本推送的相关源代码和文件可通过下方链接下载：

![](../../images/3b41aa17d16f03d9.webp)

链接：https://pan.baidu.com/s/19_X16CbTPGPGDkqVr_9KbA

提取码获取请联系客服：

![](../../images/fe8ecb8594a1f419.webp)![图片](../../images/cb4255ab8010219d.gif)

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

# [致谢文章又+1，生物信息学+机器学习鉴定驱动糖尿病肾病免疫激活和小管间隙损伤的PANoptosis枢纽基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537544&idx=1&sn=6e5bb738eb11af53173f9fef67b977df&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)
