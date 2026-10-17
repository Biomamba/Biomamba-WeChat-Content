---
title: "VlnPlot用法及ggplot复现"
date: 2023-11-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504768&idx=1&sn=4fc5eb47037d3a80178e32975488d70b&chksm=9b3caad0ac4b23c61147cfb0f46ecd846568f37ce89c963eb5f069d3e89a8ba285897726bb3d#rd
albums: ["单细胞教程全收录"]
---

# VlnPlot用法及ggplot复现

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504768&idx=1&sn=4fc5eb47037d3a80178e32975488d70b&chksm=9b3caad0ac4b23c61147cfb0f46ecd846568f37ce89c963eb5f069d3e89a8ba285897726bb3d#rd
> 合集：单细胞教程全收录

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqxYF92esgbSzibpibzibzTHwLVVnyELLK10c4Gtwf2KmsmltWyKV9Iiar8A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

写在前面

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)随着我们课程的持续深入，以及各位小伙伴分析技能的日益提升，目前很多同学已经不满足于Seurat的可视化功能并希望能够做出一些**改进的可视化** 。我个人对可视化的方式改进其实并不感冒，画图嘛，跟翻译一样**信达雅** 即可，没必要盲目追求视觉效果。不过这也并不方案我给大家做这类的教程。我们准备出一系列**单细胞测图片改造计划** 的推送，大家如果有任何关于可视化的想法，也可以通过文末客服微信联系我们。
本次推送我们进行VlnPlot的基本用法与其ggplot2的复现，下节课课程我们会和大家一起进行VlnPlot的ggplot2改造。
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqxYF92esgbSzibpibzibzTHwLVVnyELLK10c4Gtwf2KmsmltWyKV9Iiar8A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

视频教程

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)B站同步播出，连播更方便，文末阅读原文可直达：https://www.bilibili.com/video/BV1iM4y127Ez?p=6

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqxYF92esgbSzibpibzibzTHwLVVnyELLK10c4Gtwf2KmsmltWyKV9Iiar8A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图文教程

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

# 一、数据基本情况

本部分测试数据是[多样本整合](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21#wechat_redirect>)的输出文件。

```r
# 加载包并读取数据：
library(Seurat)
```
```
## Loading required package: SeuratObject
```
```
## Loading required package: sp
```
```
## The legacy packages maptools, rgdal, and rgeos, underpinning the sp package,
## which was just loaded, were retired in October 2023.
## Please refer to R-spatial evolution reports for details, especially
## https://r-spatial.org/r/2023/05/15/evolution4.html.
## It may be desirable to make the sf package available;
## package maintainers should consider adding sf to Suggests:.
```
```
##
## Attaching package: 'SeuratObject'
```
```
## The following objects are masked from 'package:base':
##
##     intersect, saveRDS
```
```
## Loading Seurat v5 beta version
## To maintain compatibility with previous workflows, new Seurat objects will use the previous object structure by default
## To use new Seurat v5 assays please run: options(Seurat.object.assay.version = 'v5')
```

```r
scRNA <- readRDS('pbmcrenamed.rds')

# 查看一下数据细胞类型及组别：
DimPlot(scRNA,split.by  = 'group')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzhIEb09iaekFyQvQMuEx3eJMoRdEZxCFMHibch6w3CXEj6kZVd3NYkzyA/640?wx_fmt=png)

```
# 共有三个组：
unique(scRNA$group)
```
```
## [1] "C57" "AS1" "P3"
```

```
# 共包含九种细胞类型：
unique(scRNA$celltype)
```
```
## [1] VSMC          T cell        Fibro         EC            Myeloid cells
## [6] B cell        Mono          Macro         Neut
## Levels: VSMC T cell Macro B cell Fibro Myeloid cells Mono Neut EC
```

```r
#### 查看高表达基因：
library(dplyr)
```
```
##
## Attaching package: 'dplyr'
```
```
## The following objects are masked from 'package:stats':
##
##     filter, lag
```
```
## The following objects are masked from 'package:base':
##
##     intersect, setdiff, setequal, union
```

```r
# 按照表达量给基因排序：
myorder <- apply(as.data.frame(scRNA@assays$RNA@data), 1, function(x){sum(x)}) %>% order(.,decreasing = T)

# 看一下总表达量最高的5个基因：
rownames(scRNA)[myorder][1:5]
```
```
## [1] "Gm42418" "Tmsb4x"  "Malat1"  "Actb"    "mt-Atp6"
```

```
# 浅画一下VlnPlot：
VlnPlot(scRNA,features = 'Gm42418')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzeZd8SLslZaGMe8Pf3vOMwgz9hh0eN0tmt50SqG4Ik0kibdt2rL3RfvA/640?wx_fmt=png)

# 二、`VlnPlot`用法

```r
library(patchwork)

# 调整点的大小:
VlnPlot(scRNA,features = 'Gm42418',pt.size = 0.5)| # 默认为1
VlnPlot(scRNA,features = 'Gm42418',pt.size = 0) # 点的大小为0时即关闭点的展示
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzeR9qIQV3ZhXpzxJOGfaUvpnZLUUaoWpk7BGx1VqvxI45QCs89edr8w/640?wx_fmt=png)

```r
ori_p<-VlnPlot(scRNA,features = 'Gm42418',pt.size = 0)
# 调整颜色：
library(ggsci)
# 离散型：
ori_p|
  VlnPlot(scRNA,features = 'Gm42418',pt.size = 0,cols = ggsci::pal_npg()(10) )
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzPTrKXAiaxDDodPSqJgwGYWcH88RG73r8ST0cXxD1eiaa1YQ86VpstlIg/640?wx_fmt=png)

```
# 渐变色：
ori_p|
  VlnPlot(scRNA,features = 'Gm42418',pt.size = 0,cols = ggsci::pal_gsea()(10) )
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzBibvY5hAl0WQwPPwa08blJq02JYP5hRvEX0lqORB73CDJQIYOsVJP4A/640?wx_fmt=png)

```
# 降序：
ori_p|
  VlnPlot(scRNA,features = 'Gm42418',pt.size = 0,sort = T)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzIfUt4BYpHabQq7GiaKFBb2xuknRaQL5kxysNgp16pW6hPLnnrmVNhlw/640?wx_fmt=png)

Hide
```
# 展示不同分组变量：
ori_p|
  VlnPlot(scRNA,features = 'Gm42418',pt.size = 0,group.by = 'group')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyz0rV8bLdCdDwXSuXVB2J1I51kXoPZzX6MImjHRRjvUpOWK4KSN4e0ibg/640?wx_fmt=png)

```
# 把每个celltype：
ori_p|
  VlnPlot(scRNA,features = 'Gm42418',pt.size = 0,split.by  = 'group')
```
```
## The default behaviour of split.by has changed.
## Separate violin plots are now plotted side-by-side.
## To restore the old behaviour of a single split violin,
## set split.plot = TRUE.
##
## This message will be shown once per session.
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzesAlK9ic5XKkiaAHhHlictOibrQKAxVJeyQqxj2PJQFic246ozKGfNzAZuQ/640?wx_fmt=png)

```r
# 绘制多个基因：
he_gene<- rownames(scRNA)[myorder][1:10]

VlnPlot(scRNA,features = he_gene,pt.size = 0)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzgAyvicgAAwT54lxwMcOm65xsqZmGmSib3BXJx7u1mPwDM8dVeiab5OO1g/640?wx_fmt=png)

```
# 多个基因更适合堆积小提琴图：
VlnPlot(scRNA,features = he_gene,pt.size = 0,stack = T )
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzFic8lqbuiaF7ia40ubj3ThCPY3hEJAxbu3UsmpZ9jaVB50ibdlemNp7oPA/640?wx_fmt=png)

# 三、`ggplot2`复现

## 3.1 `VlnPlot`源码

```
# Vlnplot源码(注意下面的函数名不要加括号)：
VlnPlot
```
```r
## function (object, features, cols = NULL, pt.size = NULL, alpha = 1,
##     idents = NULL, sort = FALSE, assay = NULL, group.by = NULL,
##     split.by = NULL, adjust = 1, y.max = NULL, same.y.lims = FALSE,
##     log = FALSE, ncol = NULL, slot = deprecated(), layer = "data",
##     split.plot = FALSE, stack = FALSE, combine = TRUE, fill.by = "feature",
##     flip = FALSE, add.noise = TRUE, raster = NULL)
## {
##     if (is_present(arg = slot)) {
##         deprecate_soft(when = "5.0.0", what = "VlnPlot(slot = )",
##             with = "VlnPlot(layer = )")
##         layer <- slot %||% layer
##     }
##     if (!is.null(x = split.by) & getOption(x = "Seurat.warn.vlnplot.split",
##         default = TRUE)) {
##         message("The default behaviour of split.by has changed.\n",
##             "Separate violin plots are now plotted side-by-side.\n",
##             "To restore the old behaviour of a single split violin,\n",
##             "set split.plot = TRUE.\n      \nThis message will be shown once per session.")
##         options(Seurat.warn.vlnplot.split = FALSE)
##     }
##     return(ExIPlot(object = object, type = ifelse(test = split.plot,
##         yes = "splitViolin", no = "violin"), features = features,
##         idents = idents, ncol = ncol, sort = sort, assay = assay,
##         y.max = y.max, same.y.lims = same.y.lims, adjust = adjust,
##         pt.size = pt.size, alpha = alpha, cols = cols, group.by = group.by,
##         split.by = split.by, log = log, layer = layer, stack = stack,
##         combine = combine, fill.by = fill.by, flip = flip, add.noise = add.noise,
##         raster = raster))
## }
## <bytecode: 0x5644486d9680>
## <environment: namespace:Seurat>
```

依赖了另一个函数出图：

```r
### 这个代码框不要运行 ！！！###
# 函数源码为：
ExIPlot <-
function (object, features, type = "violin", idents = NULL,
  ncol = NULL, sort = FALSE, assay = NULL, y.max = NULL, same.y.lims = FALSE,
  adjust = 1, cols = NULL, pt.size = 0, alpha = 1, group.by = NULL,
  split.by = NULL, log = FALSE, slot = deprecated(), layer = "data",
  stack = FALSE, combine = TRUE, fill.by = NULL, flip = FALSE,
  add.noise = TRUE, raster = NULL)
{
  if (is_present(arg = slot)) {
    layer <- layer %||% slot
  }
  assay <- assay %||% DefaultAssay(object = object)
  DefaultAssay(object = object) <- assay
  cells <- Cells(x = object, assay = NULL)
  if (isTRUE(x = stack)) {
    if (!is.null(x = ncol)) {
      warning("'ncol' is ignored with 'stack' is TRUE",
        call. = FALSE, immediate. = TRUE)
    }
    if (!is.null(x = y.max)) {
      warning("'y.max' is ignored when 'stack' is TRUE",
        call. = FALSE, immediate. = TRUE)
    }
  }
  else {
    ncol <- ncol %||% ifelse(test = length(x = features) >
      9, yes = 4, no = min(length(x = features), 3))
  }
  if (!is.null(x = idents)) {
    cells <- intersect(x = names(x = Idents(object = object)[Idents(object = object) %in%
      idents]), y = cells)
  }
  data <- FetchData(object = object, vars = features, slot = layer,
    cells = cells)
  pt.size <- pt.size %||% AutoPointSize(data = object)
  features <- colnames(x = data)
  data <- data[cells, , drop = FALSE]
  idents <- if (is.null(x = group.by)) {
    Idents(object = object)[cells]
  }
  else {
    object[[group.by, drop = TRUE]][cells]
  }
  if (!is.factor(x = idents)) {
    idents <- factor(x = idents)
  }
  if (is.null(x = split.by)) {
    split <- NULL
  }
  else {
    split <- FetchData(object, split.by)[cells, split.by]
    if (!is.factor(x = split)) {
      split <- factor(x = split)
    }
    if (is.null(x = cols)) {
      cols <- hue_pal()(length(x = levels(x = idents)))
      cols <- Interleave(cols, InvertHex(hexadecimal = cols))
    }
    else if (length(x = cols) == 1 && cols == "interaction") {
      split <- interaction(idents, split)
      cols <- hue_pal()(length(x = levels(x = idents)))
    }
    else {
      cols <- Col2Hex(cols)
    }
    if (length(x = cols) < length(x = levels(x = split))) {
      cols <- Interleave(cols, InvertHex(hexadecimal = cols))
    }
    cols <- rep_len(x = cols, length.out = length(x = levels(x = split)))
    names(x = cols) <- levels(x = split)
    if ((length(x = cols) > 2) & (type == "splitViolin")) {
      warning("Split violin is only supported for <3 groups, using multi-violin.")
      type <- "violin"
    }
  }
  if (same.y.lims && is.null(x = y.max)) {
    y.max <- max(data)
  }
  if (isTRUE(x = stack)) {
    return(MultiExIPlot(type = type, data = data, idents = idents,
      split = split, sort = sort, same.y.lims = same.y.lims,
      adjust = adjust, cols = cols, pt.size = pt.size,
      log = log, fill.by = fill.by, add.noise = add.noise,
      flip = flip))
  }
  plots <- lapply(X = features, FUN = function(x) {
    return(SingleExIPlot(type = type, data = data[, x, drop = FALSE],
      idents = idents, split = split, sort = sort, y.max = y.max,
      adjust = adjust, cols = cols, pt.size = pt.size,
      alpha = alpha, log = log, add.noise = add.noise,
      raster = raster))
  })
  label.fxn <- switch(EXPR = type, violin = if (stack) {
    xlab
  } else {
    ylab
  }, splitViolin = if (stack) {
    xlab
  } else {
    ylab
  }, ridge = xlab, stop("Unknown ExIPlot type ", type, call. = FALSE))
  for (i in 1:length(x = plots)) {
    key <- paste0(unlist(x = strsplit(x = features[i], split = "_"))[1],
      "_")
    obj <- names(x = which(x = Key(object = object) == key))
    if (length(x = obj) == 1) {
      if (inherits(x = object[[obj]], what = "DimReduc")) {
        plots[[i]] <- plots[[i]] + label.fxn(label = "Embeddings Value")
      }
      else if (inherits(x = object[[obj]], what = "Assay")) {
        next
      }
      else {
        warning("Unknown object type ", class(x = object),
          immediate. = TRUE, call. = FALSE)
        plots[[i]] <- plots[[i]] + label.fxn(label = NULL)
      }
    }
    else if (!features[i] %in% rownames(x = object)) {
      plots[[i]] <- plots[[i]] + label.fxn(label = NULL)
    }
  }
  if (combine) {
    plots <- wrap_plots(plots, ncol = ncol)
    if (length(x = features) > 1) {
      plots <- plots & NoLegend()
    }
  }
  return(plots)
}
```

最终的绘图函数为： ![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzUiaz6ibV8jt1CHhg2TheicxPwAKtGbpUJ5aicGxOX6kePIDCTJKHhQ7qcQ/640?wx_fmt=png)

## 3.2 绘图数据整理

`ggplot2`的图片绘制需要一个长格式的数据，我们以上面的高表达基因为例，整理出一个长格式数据框

```r
# 取出表达矩阵：
data4plot <- scRNA@assays$RNA@data[he_gene[1:5],] %>% as.data.frame() %>% t()

# 添加注释信息：
data4plot <- cbind(data4plot,scRNA@meta.data[,c('group','celltype')])

# 查看一下表头：
head(data4plot)
```
```
##                       Gm42418   Tmsb4x   Malat1     Actb  mt-Atp6 group
## AAAGGGCTCGCAGAGA-1_1 3.125663 5.191950 5.443660 4.880147 4.500693   C57
## AACACACAGCATCCCG-1_1 5.717602 4.747414 4.719490 4.166542 5.093166   C57
## AACAGGGTCAACACCA-1_1 4.716741 4.179333 5.849399 3.356926 3.870171   C57
## AACCCAAAGGCCTTGC-1_1 5.104691 3.290715 6.404316 4.364196 3.569047   C57
## AACCCAAAGTGGACGT-1_1 5.853611 7.403626 3.399781 5.316662 3.897164   C57
## AACCCAAGTCCGAAGA-1_1 4.562551 6.145295 4.913077 5.337041 3.646919   C57
##                           celltype
## AAAGGGCTCGCAGAGA-1_1          VSMC
## AACACACAGCATCCCG-1_1        T cell
## AACAGGGTCAACACCA-1_1         Fibro
## AACCCAAAGGCCTTGC-1_1            EC
## AACCCAAAGTGGACGT-1_1 Myeloid cells
## AACCCAAGTCCGAAGA-1_1        T cell
```

## 3.3 `ggplot2`复刻`VlnPlot`

```r
# 待复刻的图：
plot0 <-  VlnPlot(scRNA,features = 'Gm42418',pt.size = 0)
plot0
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzSwXYMJDuMWcicR1lZnv4ScEsRjDPGvfDarDVr3KCoDqE7Q2LmxFtrsg/640?wx_fmt=png)

```r
library(ggplot2)
library(ggthemes)

# 最简单的复刻：
plot1 <- ggplot(data = data4plot,
                aes(x = celltype, y = Gm42418, fill = celltype))+ # 确定坐标与颜色填充
    geom_violin()# 绘制小提琴图

plot1 # 显然这个还不是很像
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzsAYlOmkia68x7Fr8oUsxDbicIcjPEicia3DTlcJ6eXB03rBAqpzC7HL5qQ/640?wx_fmt=png)

```r
# 稍作修改
plot2 <- plot1 +
  labs(x = 'Identity', y = 'Expression Level',  title = 'Gm42418', fill = NULL) + # 修改标题
  geom_violin()+
  theme_bw()+ # 去灰色背景
     theme_few()+ # 去网格
        theme_classic()+ #去掉右侧与上方的边框
          theme(plot.title = element_text(hjust = 0.5,face = 'bold',size=15) )+ # 加粗标题并调整大小
  theme(axis.text.x.bottom = element_text(angle = 45,hjust = 1,vjust = 1, size = 12), # 调整x轴坐标位置、字体、大小
        axis.text.y.left = element_text(size=10))  # y轴坐标斜体45°

plot2
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzt5icqsia4xpZXfrhOficQY9A8ib2GTZhaPqz8SicQK7qLBC3pXZKxbEvUiaQ/640?wx_fmt=png)

```r
# 最后看一下，第一张图和第三张图基本一致
library(patchwork)
plot0/plot1/plot2 # 需要横向排列则是plot0|plot1|plot2
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyztPesP7p5lNmE8xX7UqiaA8iaAu8ekACEUC6icft6egYMxrFN81g7kac6A/640?wx_fmt=png)

## 3.4 `ggplot2`复刻`stack vlnplot`

原本`VlnPlot`中的`stack=True`选项依赖`MultiExIPlo`进行可视化：

```r
# MultiExIPlot源码：
function (data, idents, split = NULL, type = "violin", sort = FALSE,
  same.y.lims = same.y.lims, adjust = 1, pt.size = 0, cols = NULL,
  seed.use = 42, log = FALSE, fill.by = NULL, add.noise = TRUE,
  flip = NULL)
{
  if (!(fill.by %in% c("feature", "ident"))) {
    stop("`fill.by` must be either `feature` or `ident`")
  }
  if (!is.null(x = seed.use)) {
    set.seed(seed = seed.use)
  }
  if (!is.data.frame(x = data) || ncol(x = data) < 2) {
    stop("MultiExIPlot requires a data frame with >1 column")
  }
  data <- Melt(x = data)
  data <- data.frame(feature = data$cols, expression = data$vals,
    ident = rep_len(x = idents, length.out = nrow(x = data)))
  if ((is.character(x = sort) && nchar(x = sort) > 0) || sort) {
    data$feature <- as.vector(x = data$feature)
    data$ident <- as.vector(x = data$ident)
    avgs.matrix <- sapply(X = split(x = data, f = data$ident),
      FUN = function(df) {
        return(tapply(X = df$expression, INDEX = df$feature,
          FUN = mean))
      })
    idents.order <- hclust(d = dist(x = t(x = L2Norm(mat = avgs.matrix,
      MARGIN = 2))))$order
    avgs.matrix <- avgs.matrix[, idents.order]
    avgs.matrix <- L2Norm(mat = avgs.matrix, MARGIN = 1)
    position <- apply(X = avgs.matrix, MARGIN = 1, FUN = which.max)
    mat <- hclust(d = dist(x = avgs.matrix))$merge
    orderings <- list()
    for (i in 1:nrow(mat)) {
      x <- if (mat[i, 1] < 0)
        -mat[i, 1]
      else orderings[[mat[i, 1]]]
      y <- if (mat[i, 2] < 0)
        -mat[i, 2]
      else orderings[[mat[i, 2]]]
      x.pos <- min(x = position[x])
      y.pos <- min(x = position[y])
      orderings[[i]] <- if (x.pos < y.pos) {
        c(x, y)
      }
      else {
        c(y, x)
      }
    }
    features.order <- orderings[[length(x = orderings)]]
    data$feature <- factor(x = data$feature, levels = unique(x = sort(x = data$feature))[features.order])
    data$ident <- factor(x = data$ident, levels = unique(x = sort(x = data$ident))[rev(x = idents.order)])
  }
  else {
    data$feature <- factor(x = data$feature, levels = unique(x = data$feature))
  }
  if (log) {
    noise <- rnorm(n = nrow(x = data))/200
    data$expression <- data$expression + 1
  }
  else {
    noise <- rnorm(n = nrow(x = data))/1e+05
  }
  if (!add.noise) {
    noise <- noise * 0
  }
  for (f in unique(x = data$feature)) {
    if (all(data$expression[(data$feature == f)] == data$expression[(data$feature ==
      f)][1])) {
      warning("All cells have the same value of ", f,
        call. = FALSE, immediate. = TRUE)
    }
    else {
      data$expression[(data$feature == f)] <- data$expression[(data$feature ==
        f)] + noise[(data$feature == f)]
    }
  }
  if (type == "violin" && !is.null(x = split)) {
    data$split <- rep_len(x = split, length.out = nrow(data))
    vln.geom <- geom_violin
    fill.by <- "split"
  }
  else if (type == "splitViolin" && !is.null(x = split)) {
    data$split <- rep_len(x = split, length.out = nrow(data))
    vln.geom <- geom_split_violin
    fill.by <- "split"
    type <- "violin"
  }
  else {
    vln.geom <- geom_violin
  }
  switch(EXPR = type, violin = {
    geom <- list(vln.geom(scale = "width", adjust = adjust,
      trim = TRUE))
  }, ridge = {
    geom <- list(geom_density_ridges(scale = 4), theme_ridges(),
      scale_y_discrete(expand = c(0.01, 0)))
  }, stop("Unknown plot type: ", type))
  if (flip) {
    x <- "ident"
    x.label <- "Identity"
    y <- "expression"
    y.label <- "Expression Level"
  }
  else {
    y <- "ident"
    y.label <- "Identity"
    x <- "expression"
    x.label <- "Expression Level"
  }
  plot <- ggplot(data = data, mapping = aes_string(x = x,
    y = y, fill = fill.by)[c(2, 3, 1)]) + labs(x = x.label,
    y = y.label, fill = NULL) + theme_cowplot()
  plot <- do.call(what = "+", args = list(plot, geom))
  if (flip) {
    plot <- plot + scale_y_continuous(expand = c(0, 0),
      labels = function(x) c(rep(x = "", times = length(x) -
        2), x[length(x) - 1], "")) + facet_grid(feature ~
      ., scales = (if (same.y.lims)
      "fixed"
    else "free")) + FacetTheme(panel.spacing = unit(0, "lines"),
      panel.background = element_rect(fill = NA, color = "black"),
      axis.text.y = element_text(size = 7), axis.text.x = element_text(angle = 45,
        hjust = 1), strip.text.y.right = element_text(angle = 0))
  }
  else {
    plot <- plot + scale_x_continuous(expand = c(0, 0),
      labels = function(x) c(rep(x = "", times = length(x) -
        2), x[length(x) - 1], "")) + facet_grid(. ~
      feature, scales = (if (same.y.lims)
      "fixed"
    else "free")) + FacetTheme(panel.spacing = unit(0, "lines"),
      panel.background = element_rect(fill = NA, color = "black"),
      axis.text.x = element_text(size = 7), strip.text.x = element_text(angle = -90))
  }
  if (log) {
    plot <- plot + scale_x_log10()
  }
  if (!is.null(x = cols)) {
    if (!is.null(x = split)) {
      idents <- unique(x = as.vector(x = data$ident))
      splits <- unique(x = as.vector(x = data$split))
      labels <- if (length(x = splits) == 2) {
        splits
      }
      else {
        unlist(x = lapply(X = idents, FUN = function(pattern,
          x) {
          x.mod <- gsub(pattern = paste0(pattern, "."),
            replacement = paste0(pattern, ": "), x = x,
            fixed = TRUE)
          x.keep <- grep(pattern = ": ", x = x.mod,
            fixed = TRUE)
          x.return <- x.mod[x.keep]
          names(x = x.return) <- x[x.keep]
          return(x.return)
        }, x = unique(x = as.vector(x = data$split))))
      }
      if (is.null(x = names(x = labels))) {
        names(x = labels) <- labels
      }
    }
    else {
      labels <- levels(x = droplevels(data$ident))
    }
    plot <- plot + scale_fill_manual(values = cols, labels = labels)
  }
  return(plot)
}
```

```r
# 再看一眼原图
ori_plot <- VlnPlot(scRNA,features = he_gene,pt.size = 0,stack = T )
ori_plot
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyzFic8lqbuiaF7ia40ubj3ThCPY3hEJAxbu3UsmpZ9jaVB50ibdlemNp7oPA/640?wx_fmt=png)

```r
# 整理数据
library(reshape2)
data4stack <- as.data.frame(scRNA[["RNA"]]@data[he_gene,])
data4stack$Gene <- factor(he_gene,levels = he_gene)
data4stack[1:4,1:4]
```
```
##         AAAGGGCTCGCAGAGA-1_1 AACACACAGCATCCCG-1_1 AACAGGGTCAACACCA-1_1
## Gm42418             3.125663             5.717602             4.716741
## Tmsb4x              5.191950             4.747414             4.179333
## Malat1              5.443660             4.719490             5.849399
## Actb                4.880147             4.166542             3.356926
##         AACCCAAAGGCCTTGC-1_1
## Gm42418             5.104691
## Tmsb4x              3.290715
## Malat1              6.404316
## Actb                4.364196
```

```r
# 把宽格式的数据转换为长格式数据
data4stack <- melt(data4stack,id="Gene")
head(data4stack)
```
```
##      Gene             variable    value
## 1 Gm42418 AAAGGGCTCGCAGAGA-1_1 3.125663
## 2  Tmsb4x AAAGGGCTCGCAGAGA-1_1 5.191950
## 3  Malat1 AAAGGGCTCGCAGAGA-1_1 5.443660
## 4    Actb AAAGGGCTCGCAGAGA-1_1 4.880147
## 5 mt-Atp6 AAAGGGCTCGCAGAGA-1_1 4.500693
## 6  mt-Co1 AAAGGGCTCGCAGAGA-1_1 4.223976
```

```r
colnames(data4stack)[c(2,3)]=c("Cell","Expression")

my_meta=scRNA@meta.data[,c('group','celltype')]
my_meta$Cell <- rownames(my_meta)
data4stack=inner_join(data4stack,my_meta,by="Cell")

# 瞅一眼数据
head(data4stack)
```
```
##      Gene                 Cell Expression group celltype
## 1 Gm42418 AAAGGGCTCGCAGAGA-1_1   3.125663   C57     VSMC
## 2  Tmsb4x AAAGGGCTCGCAGAGA-1_1   5.191950   C57     VSMC
## 3  Malat1 AAAGGGCTCGCAGAGA-1_1   5.443660   C57     VSMC
## 4    Actb AAAGGGCTCGCAGAGA-1_1   4.880147   C57     VSMC
## 5 mt-Atp6 AAAGGGCTCGCAGAGA-1_1   4.500693   C57     VSMC
## 6  mt-Co1 AAAGGGCTCGCAGAGA-1_1   4.223976   C57     VSMC
```

```r
copy_stack <- ggplot(data4stack, aes(x = Expression, y =  celltype, fill = Gene)) +
  geom_violin() +
  labs(x = "Expression Level", y = "Identity") +
  facet_grid(.~Gene, scales = "free_x",space = 'free_x')+ # 按照基因拆分做stack，并使每个小提琴图的坐标按照真实极值生成，而非全部统一
                theme_bw()+ # 去灰色背景
   theme_few()+ # 去网格
   theme( panel.spacing.x = unit(0, "cm"))+# 去间隙
   theme(strip.background = element_blank(), # 去Gene标题的背景
  strip.text.x = element_text(angle = -90, hjust = 1,size=15,face='bold') # 旋转Gene标题的角度
        )
```

对比一下：
```
ori_plot/copy_stack
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzLbNQ9zdeVyWhqkMaNgvyz1zsbV6U0wAtwktia3kcib7ZQicPpwRQNThHA4fCvXulbAoN4y7X5J5h6w/640?wx_fmt=png)

**单细胞系列教程目录**

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 单细胞数据分析系列教程：B站视频，先看一遍视频再去看推送操作，建议至少看三遍：https://www.bilibili.com/video/BV1S44y1b76Z/本公众号单细胞相关资料都可以在这里订阅：[scRNA-Seq学习手册2023_R语言版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500516&idx=1&sn=3c0b9de505fcd232054e38b451fa1742&chksm=9b3cbbb4ac4b32a26b61f3a1f7941fff5852d3e6e744ec680aafd0b84ec976a33bf982fb5f79&scene=21#wechat_redirect>)

单细胞测序基础数据分析保姆级教程，代码部分整理在往期推送之中：[手把手教你做单细胞测序数据分析|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&chksm=9b3cb950ac4b30467a082527547b91aec15b7d1f40d44e362894aedeb6a99e014518fa5e4743&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|2.各类数据结构与读取方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499795&idx=2&sn=68e6298eb43633c71939c146d90230ff&chksm=9b3cb943ac4b3055e09739d77e037d679f3d9ec68780d1aa8c592f806fcc8d2322eaee78752d&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|3.单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|4.多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|5.细胞类型注释，从入门到入土](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500167&idx=2&sn=8de136b938e8d4753042d23166a24026&chksm=9b3cb8d7ac4b31c19c843810c7fe4341515df8ba6fff86a0ebff9d830edfcd656a29d18011c9&scene=21#wechat_redirect>)[手把手教你做单细胞测序数据分析|6组间差异分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=2&sn=d8c4ebf8f63d12bd2ac8e2607864f322&chksm=9b3cb8beac4b31a824e228b486f0d8dd21a8f4113a0a0bcbaf1b20eaade3a83c9c7c1184010b&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析|7基因集富集分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21#wechat_redirect>)
[Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&scene=21#wechat_redirect>)

单细胞图片改造计划：[改造单细胞降维图| 1.DimPlot的探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496162&idx=1&sn=598c2920f7cc0697ee5a1fa6cadaee04&chksm=9b3c88b2ac4b01a415feeebbbec6c4891319439dc8dcdafd33cca7a1222e5adc723ae9d3a73d&scene=21#wechat_redirect>)
[改造单细胞降维图| 2.ggplot2中的DIY](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496239&idx=1&sn=1fe6fd4a7fb88ecc0456b4f5710cb5d6&chksm=9b3c8b7fac4b0269e0abeab951ad6ae0ddd1464dd9d1867280eeb9755fda5ba8f5237d88a7a6&scene=21#wechat_redirect>)
[改造单细胞降维图| 3.3D降维图与动图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498080&idx=2&sn=a9bcf65e3ae34ba201e8d49ee33c0728&chksm=9b3c8030ac4b0926c3f059a9a5d23f1bcdbcaf8e5a562eba2b7e3bec3396c44573269bd08e7b&scene=21&cur_album_id=2707677276481814529#wechat_redirect>)
[改造单细胞降维图| 4.一些造好的轮子](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498191&idx=1&sn=952312a6b26232d460bf787cc276543f&chksm=9b3c809fac4b098972c8c1dd83b9f954a38fe5b5f6bc7e295f3f3a7ba6c4c3d32951679ac24d&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&chksm=9b3ca933ac4b2025f922a325ec6893e93613f130ff1d4fd609e2d7274f7f1fdb5134092e28ad&scene=21#wechat_redirect>)
[改造单细胞FeaturePlot](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504616&idx=1&sn=f7b4a0e6b25d224380cd803e3463a3e4&chksm=9b3cabb8ac4b22aeb65e0d6ec32a1f8674dcf907da078ccb3b61e06c4aa035864ebec092f571&scene=21#wechat_redirect>)

SCENIC转录因子分析：[SCENIC单细胞转录因子预测|1.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|3.软件安装与数据准备](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|5.step1+step2构建共表达网络与regulon](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501692&idx=1&sn=3f7e263a93942ad03faa1ba5f8694ec4&chksm=9b3cbe2cac4b373af9db74a50ffb08a9b8a3b958fc6385c937385f0f7323bc935cdb0fe5275c&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|6.Step3 利用AUCell对Regulon评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501989&idx=1&sn=2700bf779d7d261a4d751d1635fdce2c&chksm=9b3cb1f5ac4b38e3014476242fe956cf510cc45b9f4cef86070af8094fd5f884f9d5c3a3363f&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|7.Step4 二元矩阵的计算与可视化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503995&idx=1&sn=26c7e9ec56af434e62b02853cfe667d6&chksm=9b3ca92bac4b203d7986645ab5a3fb574f44185c7ced8bd47957fa237d436a95bfa2579d052a&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|8.Step5 regulon聚类、分群、降维](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504024&idx=1&sn=143c0ec4d94b8fca0a4a47d3dc24415b&chksm=9b3ca9c8ac4b20de70a87acb2d3f810b0e1497071b1c6f14f1882a6d844fff016e9ba5581eb3&scene=21#wechat_redirect>)

上游fastq文件处理：
[单细胞分析的最上游——处理Fastq文件：cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501751&idx=2&sn=a79512f54db7456ea577de40f1a2d286&chksm=9b3cbee7ac4b37f1ce313d5eeb9a9ac9940640ab599ac5ab5d438fa86a8007796b768e4e68c2&scene=21#wechat_redirect>)
[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501812&idx=2&sn=7feb4d89ebc45ca7d64ad2dd5cd3c832&chksm=9b3cbea4ac4b37b2d2609172d58251076a6ab6a7043600613f0fb2ae0bea427de542b4dcf91e&scene=21#wechat_redirect>)[Cellranger报错：Unable to distinguish between [SC5P-R2, SC3Pv2] ...](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504739&idx=2&sn=e4e6ad0559b9b6a703d6ab37c2a8fdb0&chksm=9b3caa33ac4b23257424184bda44dd600ad98bc0dfdfa90ab0e3ebaf208e598b0b710fbafa4b&scene=21#wechat_redirect>)

细胞通讯B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1Ab4y1W7qx?p=1**往期推送**[《细胞通讯》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501282&idx=2&sn=cd37ea80e0b92f5bfbc98ea286e363da&chksm=9b3cbcb2ac4b35a4258d21fe003374795619fc2356376ebbe4ff640233f4b4c6e3e3ead41370&scene=21#wechat_redirect>)[《细胞通讯》2.1CellChat基础分析教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=2&sn=fb3e252d95ee8b50cd446e71335b1aa0&chksm=9b3cbca0ac4b35b621b4f51d2c3a130f00461faeeff067396222c2fc2eeb53f3544664d7d9bc&scene=21#wechat_redirect>)
[《细胞通讯》2.2CellChat多组别分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501523&idx=2&sn=6fa803f256c2e0b945f93ae7d8245f50&chksm=9b3cbf83ac4b3695b587e9817840f419104c8680f5ef08ee39aa149b79852f48b179f68e3397&scene=21#wechat_redirect>)
[《细胞通讯》CellChat学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501735&idx=2&sn=35fc792961507f4ae1cbae3a2882fba6&chksm=9b3cbef7ac4b37e1417d4108c8bd378c68c3907431ddfc52ad37c916e85649bb450d761a8e19&scene=21#wechat_redirect>)

拟时序分析B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1br4y1x7Hf?p=1**往期推送**[《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)[《拟时序分析》3.monocle2实操：精简版拟时序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487398&idx=1&sn=6621eed90157d8da06ef778c40bd5554&chksm=9b3f76f6ac48ffe081ddfee3a323e0e31c1fda33731012de73168cf2ab30a226cf70c848f769&scene=21#wechat_redirect>)
[《拟时序分析》4.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》7.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)
[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494479&idx=1&sn=32f39c79c4c9fc07aa829eed49016da3&chksm=9b3c921fac4b1b091efcdd151500b69d19f71d5ca518122af697fc37e87acd915f3be5f63fb8&scene=21#wechat_redirect>)

scFAST系列[scFAST分析| 01.绪论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503875&idx=1&sn=2b5ca0c57e17e51abb52adfe199c5736&chksm=9b3ca953ac4b20450f643b94bcfc95aa2b04ded197ce93e455a281901d7ccba099b48cfd03d9&scene=21#wechat_redirect>)
[scFAST分析| 02.单细胞分析准备工作](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504023&idx=1&sn=4091a22e853242b4aae7a7d3b4008f5c&chksm=9b3ca9c7ac4b20d1bb0389fad5fe85a3c4cf49179747fe97dffaab1087b7d2793668d9f63aa4&scene=21#wechat_redirect>)
[scFAST分析| 03.fast模块](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504044&idx=1&sn=d37991280217dcc29280efa344f856bb&chksm=9b3ca9fcac4b20eab124ccd4ba6ad3f5eee640df314e7d8fec0225035f06178e3a51dbe2033f&scene=21#wechat_redirect>)
[scFAST分析| 04.Seurat分析及可视化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504435&idx=1&sn=c6a6f7ca00684601f3cda49e53be5339&chksm=9b3cab63ac4b2275d993bbaa64c71652685065fa377be57319fc6a5c47eb958b3644c7459cd5&scene=21#wechat_redirect>)

其他单细胞相关技术贴也在这里：[细胞的数量由誰决定？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484056&idx=1&sn=4967a054f5241ff3a1bd4a6fe9a502b1&chksm=9b3f7bc8ac48f2deca3141461be035deb8658be184d78597af28f8ba2092d12f020768275248&scene=21#wechat_redirect>)[单细胞中应该如何做GSVA？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&chksm=9b3f7c4dac48f55bf1d11337406ab0e1295e8e1731dbac0715eedc99d11beff7f380e42dd49b&scene=21#wechat_redirect>)[答读者问（三）：单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)[答读者问（四）：如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)[答读者问（八）：为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)
[答读者问（十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)
[答读者问（十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析：Loupe Browser](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a&scene=21#wechat_redirect>)
[什么？不做单细胞也能分析细胞类群和免疫浸润？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485798&idx=1&sn=c849bc7a0093af92fc99e13b55842bb2&chksm=9b3f7036ac48f92048d726b38f2dd978d0b0cce779c1a4090aa4da5cb2df3ad30a5c5dbed27e&scene=21#wechat_redirect>)
[答读者问 （十三）查看Seurat对象时的ERROR：type='text'](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)
[各类单细胞对象（数据格式）转换大全（一）](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485925&idx=1&sn=14e08440200f0f5cb4dcc2dc615efeb8&chksm=9b3f70b5ac48f9a37a43cc2a8b2a5e485a3f84b4ef87949dfe99056bc6301b110e80800f6bb1&scene=21#wechat_redirect>)[批量整理好GEO中下载的单细胞数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486045&idx=1&sn=0b6874bcffc8abafb505cabce4c4fc0e&chksm=9b3f730dac48fa1b140ef01c07a7749e69df4fa7d2056deeed0673c668b6246724cd85741125&scene=21#wechat_redirect>)[答读者问 （十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)
[答读者问 （十六）做单细胞测序到底需要多少内存](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487923&idx=1&sn=15043c6d729b0d5493ab875b0e54a259&chksm=9b3f68e3ac48e1f5dae514a01c857f9a56a90e2977dd7862db28d06fe55888cd9bb4afbb14e0&scene=21#wechat_redirect>)[答读者问 （十七）调用的线程越多就算的越快嘛?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488995&idx=1&sn=7140e0d037671542fb37dff3a3c94b28&chksm=9b3f6cb3ac48e5a5f54a02be9e6af9f5a4cf8da1de1770f9035130c84dedf059a024964fc15a&scene=21#wechat_redirect>)
[答读者问（十八）、一个我至少被问过30遍的monocle报错](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25&scene=21#wechat_redirect>)[没有barcode文件的单细胞数据要怎么读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490952&idx=1&sn=364a3941e59e45234795c906a42fc9ab&chksm=9b3f64d8ac48edcec70384cf5c6a91224d0f7841ce3a7cfcade6513500c13673a6695d6f0299&scene=21#wechat_redirect>)
[单细胞基因集评分之AUCell](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&chksm=9b3c99e1ac4b10f7ca158561e96fec76a49ff32b8412cb146ed3fb7aa9260c75172b4eb16f9a&scene=21#wechat_redirect>)
[粉丝来稿|1. Seurat4相较于Seurat3的几点改动](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494516&idx=1&sn=cb2d4e6b182428ce7b98e7fff2e8729a&chksm=9b3c9224ac4b1b32c4fe99758960305c4845395cfe03851d70a0407043ee36250e55d20106fc&scene=21#wechat_redirect>)
[如何加快Seurat的计算速度](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494116&idx=1&sn=f3dc577cbb464779062aada313191a05&chksm=9b3c90b4ac4b19a27a17f958e3437337d5b10b6ba7153e4dd43dedcb4df812d8c6b4d86fe970&scene=21#wechat_redirect>)
[一文搞定单细胞基因集评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493493&idx=1&sn=2cd725b2f04377f218955bafbcbb877d&chksm=9b3c9e25ac4b17330a9b9ff77302ab95a9dc5dc7e6fe7298f28d682112ee066c7d4bc1947982&scene=21#wechat_redirect>)[答读者问（二十）四个单细胞样本只给了一套文件怎么读](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494879&idx=1&sn=c2287ab3684792747dfac53d6704462b&chksm=9b3c958fac4b1c994a4b075c4f8475816e121966fa8c52cb0a2ce8c14987988ab9bdb49bdf69&scene=21#wechat_redirect>)
[人类单细胞测序数据中有哪些以"**-"开头的基因](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495019&idx=1&sn=f52ac22ca1ea47ecddaa3503bdc2c0b6&chksm=9b3c943bac4b1d2d521f7155ce8f499389dade23828017572a84cdce71e5d08d37d74e08512b&scene=21#wechat_redirect>)
[为什么总把分辨率调的很高](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495765&idx=1&sn=2ec5e3e26491e28c92e25c40630bffae&chksm=9b3c8905ac4b0013a23f9cda2cccd67cdf3c4a941bac161e3a15a12ab98cd4e5eca8aeedbe96&scene=21#wechat_redirect>)
[Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495938&idx=1&sn=2258390c97ec14f3cd336defede59cdb&chksm=9b3c8852ac4b01448fd3b84463d5ab6b697495db6ad57746e7f60e32f491547a3e35290c66ee&scene=21#wechat_redirect>)
[答读者问| 22.object 'CsparseMatrix_validate' not found](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496273&idx=1&sn=fd5a92dd7fdc349b1624784ca74b1220&chksm=9b3c8b01ac4b0217cf06d89bfea49c3fa0c9b580957338c0cc8f55ede3e8f65d6d7162ae27e3&scene=21#wechat_redirect>)
[单细胞数据在R中的读取及存储速度太慢怎么办？这个神包来帮你！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=1&sn=11bdf3c7f9042fc03f9ed237a9b9677b&chksm=9b3cb8beac4b31a8bf1d9fb862553ed32ac9a56f4a6e0f2d38c9478132f87327d8c6b6940573&scene=21#wechat_redirect>)
[单细胞分群分辨率选择困难症](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501241&idx=1&sn=9e15d23f721ad7f4ae1335ce5362031b&chksm=9b3cbce9ac4b35ff43434c0384afbbf5689f5b62a677e55e8a635d4812da57593d85a73cf48b&scene=21#wechat_redirect>)

单细胞文献阅读：[测序技术的发展与应用](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495792&idx=2&sn=1aecc80b68f65f8a44a899df524038c0&chksm=9b3c8920ac4b0036b23268331b457a335b22b4fa3aed1db287ab79e7a4613df8d195bd11421a&scene=21#wechat_redirect>)[Biomamba助推的第二篇文章!发表了！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489823&idx=1&sn=6a5dddd53870395316d2b2e904c6ce72&chksm=9b3f604fac48e959e97e4b0317643efdcf117da7f8b75f1edbcd64dd8e2f07149e6031a94dd4&scene=21#wechat_redirect>)[又来了！Biomamba生信基地助推的第四篇文章!](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492532&idx=1&sn=cddb4691f23defc80b60da231790c53c&chksm=9b3c9ae4ac4b13f2334cc7f6b16eec1d8223800f6ecef71a93cfba21698ac5f4505dbd64f300&scene=21#wechat_redirect>)
[单细胞测序解析糖尿病肾病中肾小球的动态变化](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497682&idx=2&sn=7ef49191c5e334bb291ccdaa8ea444ae&chksm=9b3c8e82ac4b079425433938c831d528eddb9237efaca49acbc210e9cd715d057541589dc290&scene=21#wechat_redirect>)
[Cell metabolism| 单细胞测序技术解析健康人与T2D患者的胰岛差异](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=1&sn=b7f8df758bc4d95b88969378c6dfbeee&chksm=9b3c8ea1ac4b07b7c6a0b5023ebf6c8ecd7d34741ab076baa0b564535d1d753bbf9dc5be5290&scene=21#wechat_redirect>)
[Science| 小鼠全肾单细胞测序开篇之作](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=2&sn=554d6a4e1b28b2e5303695fae5942a34&chksm=9b3c8ea1ac4b07b72323ce25cd49474a9228ec1aaa56243f57dca3f2f668dc42ab9cd58dca21&scene=21#wechat_redirect>)
[一篇不花钱就能白嫖的文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497840&idx=2&sn=1dacbfb190e11d2ff104e32f238cf8c4&chksm=9b3c8120ac4b08367bfe3a0dd8d55f21f5d13528826de3144a9a85ce9b1c9f4c710de703edae&scene=21#wechat_redirect>)
[不会吧不会吧，Nature都能白嫖？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=2&sn=caeb8ed06ffd5239b58cebcd90843cf8&chksm=9b3c81dbac4b08cd9eec50978951a1b890ca08edec644ff75205a09ad1f067dff25d6ecb938e&scene=21#wechat_redirect>)
[高氧下小鼠肺发育损伤的ScRNA图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498513&idx=2&sn=79845edf56a3023c59c73403d7b6494b&chksm=9b3c8241ac4b0b57793402686edc8c35aaa3b0959d3096b5122207fbb70ab809d1df5faee0d7&scene=21#wechat_redirect>)
[IgAN & STRT-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485376&idx=1&sn=02e228d0993d8a653c8bb1d531021cdb&chksm=9b3f7e90ac48f78686d6d5953aeb192db4f28bf577dbebd76d9fabbe797f135b7fb08fb42867&scene=21#wechat_redirect>)
[老树开新花—EGFR、肿瘤、免疫+scRNA-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498596&idx=2&sn=8f63f5856cdf90e15f1d19b4cfe6a39e&chksm=9b3c8234ac4b0b221a5d2c417558f0e63f742459c0a3f8c1cbb4cdf74ce25ddcaf0e48f4a7ce&scene=21#wechat_redirect>)
[癌前基质细胞驱动BRCA1肿瘤发生](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498597&idx=2&sn=9f5fee38d0821052c9c6b3753c2b3bed&chksm=9b3c8235ac4b0b238c4902ad7b3944b285baaa0a7ec6f5c7d08a596fdf89735dc7a7afab91f0&scene=21#wechat_redirect>)
[紧跟生信"钱"沿,胰腺癌&免疫多模态图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498668&idx=2&sn=50cb239885bed65d3d3702c813d8e354&chksm=9b3c82fcac4b0beabece692f6e2d89c5fe4adf3a268e2944d8f0df4393cc554de5432086d6c1&scene=21#wechat_redirect>)
[原发头颈癌和肿瘤转移微生态](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498644&idx=2&sn=6293493263eeb2b4bf3f82cf526dea36&chksm=9b3c82c4ac4b0bd2a9f48b1326bbfbf2b8270ab79e5877f9bca21aa7883f60fb9cb235df2c36&scene=21#wechat_redirect>)
[《Cell Metabolism》：肾脏疾病&代谢&核受体ESRRA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498860&idx=2&sn=156afeec25201c7baa880af8daac8c60&chksm=9b3c853cac4b0c2a2ca09f44fd487c6d8d9701cb447f318c89f83a53e1a7b712d6f10ff17c43&scene=21#wechat_redirect>)
[《Nature communication》：PD-1&急性髓细胞性白血病&T Cell](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498862&idx=2&sn=1ba36b54428198104c5168d84aba6c51&chksm=9b3c853eac4b0c2874eee3d90b5a989fdc2b366c40805b5041a6f1a588e99b45be14469bdd56&scene=21#wechat_redirect>)
[单细胞测序揭示鼻咽癌微环境的基质动力学和肿瘤特异性特征](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498926&idx=2&sn=3bbd43812d2dfcbbd9230c8cb50df36b&chksm=9b3c85feac4b0ce8225b6f77eec91ac9c8150bff171ac6874363b2617ccfe6042400777415c3&scene=21#wechat_redirect>)
[《Nature》：MYB调控衰竭性T细胞对检查点抑制的响应](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498939&idx=2&sn=b63958fb8f28af052036f4ffc05e2fc2&chksm=9b3c85ebac4b0cfdf3fda8f7236c50db168de20ff4795db7af9d6a0b45304e3f6fb3ba888694&scene=21#wechat_redirect>)[单细胞都能活检测序了？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500846&idx=1&sn=d5e9782c0318e411771e746950f5b5f5&chksm=9b3cbd7eac4b3468ea93a5d6a28cfd05409660a532cc8df72ed9b58f30a76b0a8b6cec79934a&scene=21#wechat_redirect>)
[文献阅读(二十九)、单细胞测序做到什么程度能毕业|硕士篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493808&idx=1&sn=52c7d330ffdda47c3409d36fe9cbbcd8&chksm=9b3c91e0ac4b18f6edf59d171a0d982b1e3f842148046d8eed19343484feaa84dbd5b7682a11&scene=21#wechat_redirect>)
[文献阅读(三十)、单细胞测序做到什么程度能毕业|博士篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494017&idx=1&sn=a2dc4e2eef2bcdb40f5074b665dfa45f&chksm=9b3c90d1ac4b19c79ac5128f96d27789241357c9745bb0389ff5f79f96ab825d3e1c9b29e3af&scene=21#wechat_redirect>)[2022年了，都有哪些器官/组织有scRNA-Seq数据|小鼠篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494796&idx=1&sn=92c91a65719bdf39658814eb691a780f&chksm=9b3c95dcac4b1cca5547440a5881e650da3ea430bad3e6017cbd2891606b2ec40e3ec343bc0e&scene=21#wechat_redirect>)
[2022年了，都有哪些器官/组织有scRNA-Seq数据|人类篇](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494806&idx=1&sn=1d15ad9cb4d350a164d3b941bc715233&chksm=9b3c95c6ac4b1cd054cedbd3e8c8f57ee88cc59a6ebda2fd11ba8fea79f5e9e8c65d21ff338c&scene=21#wechat_redirect>)
[2023年了, 都哪些物种有scRNA-Seq数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496958&idx=1&sn=f34c69e2114d99fa25e2524411c028a2&chksm=9b3c8daeac4b04b80a5629433d5eec4d25b8ba7d2a74fa31cd499b98c36601ddfe436e2196eb&scene=21#wechat_redirect>)[终于读到一篇用monocle3做拟时序的文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496064&idx=1&sn=0be38306f9cd8c6b819d58cc2e779b87&chksm=9b3c88d0ac4b01c6773b6c4f1a063788509baa27c57e2098b16b8ebe38cc625a87b9d89272c7&scene=21#wechat_redirect>)
[单细胞转录组+亚细胞空间代谢组=25分文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496126&idx=1&sn=8cb6040a38eb844bb215c0d395196e3a&chksm=9b3c88eeac4b01f8dcb8f4c7a19c5a58841d5fe1623f0a4c585c6dcc281cbbdd2830a1150f6a&scene=21#wechat_redirect>)
[酸了，六个样本的scRNA-Seq+差异分析=9分文章](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496237&idx=1&sn=646cd85b62d08c1739a532242c8991ba&chksm=9b3c8b7dac4b026be9e65b64df8e830d1c2c882272165e64eec6eb258e4ed5342cf30f42dda5&scene=21#wechat_redirect>)[自测scRNA-Seq+scWGBS=3分三区文章？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498939&idx=1&sn=1b33d219c795f2de8ff66a5c330a3d24&chksm=9b3c85ebac4b0cfd050a7c0abe11dead991a988aa5b790eac6fd57de2f76a85ef2191d8b9ca6&scene=21#wechat_redirect>)
[百万级单细胞多组学数据集成](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499336&idx=1&sn=864c535b38ce630487fccc602d893a80&chksm=9b3c8718ac4b0e0e8a0e2560a83546167a82616d99503606e3ac0ef29e90b01cc762e95d64e6&scene=21#wechat_redirect>)[空间转录组与单细胞转录组整合分析工具大比拼](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500243&idx=1&sn=b0e513e85a202ec7ca4041a700a7ae10&chksm=9b3cb883ac4b3195cffd0398d880468b12dd068f9a9fd96b7d0f8aed8961be34293e6ff4a2bb&scene=21#wechat_redirect>)
[<IF=27.4> IgG4相关性疾病中颌下腺和血液中的细胞和分子改变](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503081&idx=1&sn=29890957ab75f050d466ca659292b529&chksm=9b3cb5b9ac4b3cafe279783c49cf7928819c5caeffbc34e52ae0c79f5e701ce8a25dd6f0c913&scene=21#wechat_redirect>)
[微生物组研究技术——微生物也能做单细胞](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488278&idx=1&sn=3662cde0f439a7e7cad7fb0d50082c05&chksm=9b3f6a46ac48e350318b38f1bfe252dd4c315ad058dc4b9aa02fadf2be2291fd0dac50f24cc6&scene=21#wechat_redirect>)
[scRNA-Seq+WGCNA+铁死亡：IF=9.69](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503498&idx=1&sn=fcf38bd6fd1dbaf80e203926bb63d5c4&chksm=9b3cb7daac4b3ecca9f2dd590fc581f5b1ae67a7f89be6f76eb438a017b5c335d8a01830b6a5&scene=21#wechat_redirect>)
[《Nature》: 单细胞解析大脑感知流感过程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503508&idx=1&sn=72781ff97ecae1c32815fe2c4d71b24e&chksm=9b3cb7c4ac4b3ed2b46c8c22f4ce8f93e3f93004ee76542bdd92039d301cec4a10077bb973db&scene=21#wechat_redirect>)
[两万字长文|当前单细胞 RNA-seq 分析的最佳实践](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503544&idx=1&sn=d563497cc912950d07c2284709f3aede&chksm=9b3cb7e8ac4b3efe66fa4e743f9d6c245a7dd6ea370cd0ee397e92761a2d680cac5c6dd4ea87&scene=21#wechat_redirect>)
[数百万级单细胞数据时代的多组学分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503603&idx=1&sn=c146eec4528f418226f0103030cb803c&chksm=9b3cb7a3ac4b3eb5bd8be7e41c8c440c80e8223fb10634bfc6d523fe389e3aa0bc14e5ea87d5&scene=21#wechat_redirect>)
[《Nature Methods》: NiCheNet, 能够考虑到胞内转录调控的细胞通讯软件](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503617&idx=1&sn=18389ffe1d201b1c0592ebc923aac851&chksm=9b3cb651ac4b3f4777cb0a6282ad99cd2aad711050d1590f20f970d843f05fb42f8cc02833e2&scene=21#wechat_redirect>)
[基于scRNA-Seq&空间转录组的AKI研究](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503664&idx=1&sn=39519d9cfa54e2d5b757f6c249ccbc86&chksm=9b3cb660ac4b3f768c8cfb708d8355c426b2d4ad39538acd5584aa9741ccdf1076b7112492df&scene=21#wechat_redirect>)
[自测蛋白质组+Bulk RNA-Seq & 挖掘scRNA-Seq=13.6分JASN](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504408&idx=1&sn=da427a6687b06a82d9dd58ae9f9aa474&chksm=9b3cab48ac4b225e8272d0475ae9295c1ea96172419aa604526f1b8a898748cb3897508d95a0&scene=21#wechat_redirect>)

单细胞注释复写[单细胞注释复写(一):Human Fetal Kidney](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447&scene=21#wechat_redirect>)[单细胞注释复写(二): human colorectal](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491642&idx=1&sn=2246fb702277ddc690f056fc8854142e&chksm=9b3c996aac4b107c059a403978eca7be1ae7987659626272c58430910ad75892ad470517aefb&scene=21#wechat_redirect>)
[单细胞复写|3.急性心肌梗塞(AMI)外周血scRNA-Seq分析实战(链接重置)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501145&idx=2&sn=12c2e8d104ad343fc13acb8cda266e6c&chksm=9b3cbc09ac4b351f4ed708a0ed577a21f48ccb0d4173aed94a027b4170147ab85931ee51d1e5&scene=21#wechat_redirect>)
[单细胞复写|4. GSE157783数据集复现及差异分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503585&idx=1&sn=0035977a80621f09d0774d3c9b0a86cd&chksm=9b3cb7b1ac4b3ea76685ed44abcfb031c698835d9b9b42b269496f6104cd8c9d45467de7eddd&scene=21#wechat_redirect>)

硬件准备：
[生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503225&idx=1&sn=d07afe8ff1787f6226c2d64cc72508f9&chksm=9b3cb429ac4b3d3f06513c5b7e3a5e03b6dc347c3e4edff0544225b57e7f98e8425dff5242f3&scene=21#wechat_redirect>)
[有root权限的共享服务器,报我名字立减200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502932&idx=1&sn=401d384d47616029375224b2d0a3c933&chksm=9b3cb504ac4b3c1299aac5c9f0747ccc36777390d2a939e1ed4af37c2836c1f7e8b4af612989&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息更新不及时，超过48h便不许回复读者消息，这里给大家留一下领取资料及免费服务器([有root权限的共享服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
