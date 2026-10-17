---
title: "详解anndata对象的.obs与.var"
date: 2026-02-09
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534988&idx=1&sn=1e673ac2838aae9c14c9b79024fbfc57&chksm=9b3c30dcac4bb9ca7cd3397a3ddfdb35c3d01fff8bd2440745b61c126bdb51c6b78cf87ba9e8#rd
albums: ["单细胞教程全收录"]
---

# 详解anndata对象的.obs与.var

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534988&idx=1&sn=1e673ac2838aae9c14c9b79024fbfc57&chksm=9b3c30dcac4bb9ca7cd3397a3ddfdb35c3d01fff8bd2440745b61c126bdb51c6b78cf87ba9e8#rd
> 合集：单细胞教程全收录

**一、写在前面**

随着[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)技术的不断发展，单个样本能够测得的细胞数目相较于单细胞技术出现的初始阶段已经有了明显的提升。R语言由于其本身的环境越来越难以满足大数量级别的单细胞数据分析了。[Python](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2914943677591224321#wechat_redirect>)依托其核心优势：其强大的生态体系，不仅能灵活扩展工具包，还能无缝衔接机器学习与可视化环节，让单细胞分析更高效、更贴合科研实际需求！因此，顺应时代的洪流，我们也为大家准备了[82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)和[一次搞定Python空间转录组分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531918&idx=2&sn=315a5d550c6c3bac578c8a188eef76a2&scene=21#wechat_redirect>)。

python进行单细胞数据分析的过程中，相信有一个工具大家一定不陌生--**[Scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505248&idx=2&sn=18995c7248ca6f13b61edfef24208ae1&scene=21#wechat_redirect>)** 。Scanpy作为基于python语言开发的单细胞分析工具，可以帮助我们实现但不仅限于如下功能：

**（1）[ 单样本分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&scene=21#wechat_redirect>)**
**（2）[ 多样本整合](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&scene=21#wechat_redirect>)**
**（3）[ 差异分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500270&idx=2&sn=d8c4ebf8f63d12bd2ac8e2607864f322&scene=21#wechat_redirect>)**
**（4）adata对象处理**
**（5）单细胞图形可视化**
**（6）单细胞图形优化**

基本可以帮助我们完成单细胞基础分析全流程内容。在文献中我们常见的Fig1图片组图基本上都是靠Scanpy完成的。

在Scanpy分析全流程制作过程中，我们发现了一些意外的分析细节。如果大家有自己的**分析经验** 或者**曾经踩过的坑** ，也非常欢迎大家和我们一起交流分享。

本教程基于Linux环境的jupyter演示，计算资源不足的同学可参考：

[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21&token=1904068475&lang=zh_CN#wechat_redirect>)[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21&token=1904068475&lang=zh_CN&poc_token=HF-eN2mj01zsfxe_I4r8D5pfZx80xO2AVYSB6qtT#wechat_redirect>)[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21&token=1904068475&lang=zh_CN&poc_token=HHWeN2mjUe1w7qMDvfaBNJZRTCq3qpve8MrnSv_z#wechat_redirect>)访问链接：https://biomamba.xiyoucloud.net/欢迎联系客服微信[Biomamba_zhushou]获取帮助

**二、准备工作**

如果你对下面的教程比较迷茫，那么你可以先行学习编程教程：

[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)

[生信Linux及服务器使用技巧](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2980604042328702978#wechat_redirect>)

[生信Python速通](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2914943677591224321#wechat_redirect>)

那么话不多说，今天在这里以Scanpy官网提供的经典PBMC3k数据作为测试数据。在数据演示之前，大家要完成如下的准备工作：

## 2.1 jupyter安装

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 这里基于Python3.11创建jupyter环境# conda create -n scRNA-seq_python python=3.11 -vv -y# -vv：启用详细输出模式（-v 是 --verbose 的缩写，-vv 表示更详细的日志，会显示更多安装过程中的细节，如依赖检查、下载进度等）。# -y：自动确认所有提示（-y 是 --yes 的缩写），执行命令时不会弹出确认对话框，直接按默认设置完成创建# conda activate scRNA-seq_python# conda  install jupyter -y -vv# conda install -c conda-forge jupyterlab jupyter_server -y#cd ~# 生成配置文件# jupyter notebook --generate-config
# 输入登录密码# jupyter notebook password
# 允许远程登录 使用默认端口8888（jupyter notebook 运行端口，根据实际情况设置，3.0系统就使用8888即可）# cat >> ~/.jupyter/jupyter_notebook_config.py << EOF# c.NotebookApp.ip='*'# c.NotebookApp.open_browser = False# c.NotebookApp.port = 8888# EOF
# 激活环境# conda activate scRNA-seq_python# 前台运行，关闭SSH终端后会终止服务# jupyter lab
# 安装拓展包# conda install jupyter_contrib_nbextensions# jupyter contrib nbextension install --user
```

##

## **2.2 python库安装**

  *   *   *   *   *   *   *   *   *

```
# conda install -c conda-forge scanpy python-igraph leidenalg# conda install -c conda-forge pooch# conda install -c conda-forge scikit-misc# pip install bbknn# pip install harmonypy# pip install statannotations# conda install -c bioconda gseapy# pip install celldex# pip install singler
```

##

## **2.3 库加载**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 导入 pandas，用于数据表格处理（如 DataFrame）import pandas as pd
# 导入 scanpy，用于单细胞转录组数据分析（核心库）import scanpy as sc
# 导入 matplotlib.pyplot，用于绘图与可视化import matplotlib.pyplot as plt
# 导入 numpy，用于矩阵计算与数值分析import numpy as np
# 导入 anndata，用于存储单细胞数据结构（AnnData对象）import anndata as ad
# 导入 os，用于文件路径和系统操作（如创建目录）import os
# 导入 seaborn，用于统计可视化，支持更美观的绘图风格import seaborn as sns
sc.settings.verbosity = 3# verbosity: errors (0), warnings (1), info (2), hints (3)# 同时设置 dpi 和 figsize（根据需要调整宽和高）sc.set_figure_params(dpi=300, facecolor="white", figsize=(8, 6))  # 宽8英寸，高6英寸
```

**三、实操流程**

##  实操环节正式开始，接下来将从单样本分析得到adata.obs和adata.var的信息，以及回答了adata.obs中的n_genes和n_genes_by_counts区别，且解析了adata.var中的mean_counts、means和mean区别。

## **3\. 单样本分析**

## **3.1 数据下载**

  *   *   *   *

```
## 数据下载，在终端运行下面命令# cd data# test -f pbmc3k_filtered_gene_bc_matrices.tar.gz || curl https://cf.10xgenomics.com/samples/cell/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz -o pbmc3k_filtered_gene_bc_matrices.tar.gz# tar -xzf pbmc3k_filtered_gene_bc_matrices.tar.gz
```

**
**

**3.2 数据读入和对象创建**

  *   *   *   *   *   *   *   *

```
# 数据读入adata = sc.read_10x_mtx(    "/data/scanpy/data/filtered_gene_bc_matrices/hg19",  # 表达矩阵存储位置    var_names="gene_symbols",  # 使用基因符号作为变量名    cache=True,   #写入缓存文件以便后续读取更快)
adata
```
```
... reading from cache file cache/data-scanpy-data-filtered_gene_bc_matrices-hg19-matrix.h5ad
```
```
AnnData object with n_obs × n_vars = 2700 × 32738
    var: 'gene_ids'
```

## **3.3 数据质控及可视化**

  *   *   *   *

```
# 确保基因id唯一adata.var_names_make_unique()
adata
```
```
AnnData object with n_obs × n_vars = 2700 × 32738
    var: 'gene_ids'
```

  *   *   *

```
# 预处理# sc.pl.highest_expr_genes 是 Scanpy 中用于可视化高表达基因的函数，它会生成一个条形图，展示数据集中表达量最高的前 N 个基因，并显示这些基因在所有细胞中的平均表达比例sc.pl.highest_expr_genes(adata, n_top=20)
```
```
normalizing counts per cell
    finished (0:00:00)
```

**![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMKepWacG4vN95ILnM2WOia0tzBDOWHlZJRL5wDBjicqHzMhqFoT2NFwaA/640?wx_fmt=png&from=appmsg)**

**
**

  *   *   *   *

```
# 基本过滤sc.pp.filter_cells(adata, min_genes=200)  sc.pp.filter_genes(adata, min_cells=3)adata
```
```
filtered out 19024 genes that are detected in less than 3 cells
```
```
AnnData object with n_obs × n_vars = 2700 × 13714
    obs: 'n_genes'
    var: 'gene_ids', 'n_cells'
```

  *   *   *   *   *   *   *   *   *   *   *

```
# 线粒体基因表达比例# 为 adata.var 数据框添加一个布尔类型的 "mt" 列，True 表示对应基因是线粒体基因，False 表示不是# 注意: 人为 MT 开头 ,小鼠为 mt 开头adata.var["mt"] = adata.var_names.str.startswith("MT-")sc.pp.calculate_qc_metrics(    adata,     qc_vars=["mt"], # 指定要单独计算质控指标的变量集合，这里是之前标记的线粒体基因（"mt" 列）    percent_top=None, # 不计算 top N 基因的占比统计    log1p=True, # 对数据进行 log (1+x) 转换    inplace=True # 直接在原 AnnData 对象中添加计算结果，不返回新对象)
```

  *   *   *   *   *   *

```
sc.pl.violin(    adata,    ["n_genes_by_counts", "total_counts", "pct_counts_mt"],    jitter=0.4,    multi_panel=True,)
```

**![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMJ30Nj9T5yzvhjfnyJtZLQIehWGzM1HJKV1WRloYnA9eeyNhVwr4SuA/640?wx_fmt=png&from=appmsg)**

  *   *   *   *   *   *   *   *   *   *

```
# 细胞过滤,去除表达过多线粒体基因或表达基因总数过多或过低的细胞：adata = adata[    (adata.obs.n_genes_by_counts< 2500)    & (adata.obs.n_genes_by_counts > 200)    & (adata.obs.pct_counts_mt < 5),    :,].copy()adata.layers["counts"] = adata.X.copy()
adata
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
    layers: 'counts'
```

  *   *   *   *   *   *   *

```
# 查看过滤后的质量sc.pl.violin(    adata,    ["n_genes_by_counts", "total_counts", "pct_counts_mt"],    jitter=0.4,    multi_panel=True,)
```

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMzFupur3wMZVvBO4qzObIgMqKEbgqzvlUmxfqiaaIJLWdEoUdF1RjdUg/640?wx_fmt=png&from=appmsg)

## **
**

## **3.4 细胞分群**

  *   *   *   *   *   *

```
# 矩阵标准化sc.pp.normalize_total(adata, target_sum=1e4)# 数据进行对数处理sc.pp.log1p(adata)adata# 执行标准化和对数转换（会修改adata.X），此时adata.X是标准化并对数转换后的数据，原始数据仍保存在adata.layers['counts']中
```
```
normalizing counts per cell
    finished (0:00:00)
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
    uns: 'log1p'
    layers: 'counts'
```

  *   *   *   *   *   *   *   *   *   *

```
# 识别高变基因sc.pp.highly_variable_genes(    adata,    layer="counts",    n_top_genes=2000,    min_mean=0.0125,    max_mean=3,    min_disp=0.5,    flavor="seurat_v3",)
```
```
extracting highly variable genes
--> added
    'highly_variable', boolean vector (adata.var)
    'highly_variable_rank', float vector (adata.var)
    'means', float vector (adata.var)
    'variances', float vector (adata.var)
    'variances_norm', float vector (adata.var)
```

  *   *   *

```
# 绘制高变基因plt.rcParams['figure.figsize'] = (6, 5)  sc.pl.highly_variable_genes(adata)
```

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMRHdRdthnGjWMIL9vwXRXfqX5Tvzj7D7KmvwZj5zcfQuJgqeYen7uIA/640?wx_fmt=png&from=appmsg)

  *   *   *   *   *   *

```
# 创建缩放层并存储原始表达数据adata.layers["scaled"] = adata.X.toarray()# 同样在"scaled"图层上操作# 这一步是降维、聚类等分析的重要预处理步骤sc.pp.scale(adata, max_value=10, layer="scaled")adata
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'highly_variable', 'highly_variable_rank', 'means', 'variances', 'variances_norm', 'mean', 'std'
    uns: 'log1p', 'hvg'
    layers: 'counts', 'scaled'
```

  *   *

```
# 主成分分析sc.pp.pca(adata, layer="scaled", svd_solver="arpack")
```
```
computing PCA
    with n_comps=50
    finished (0:00:14)
```

  *   *

```
# 让我们检查单个 PC 对数据总方差的贡献。这为我们提供了有关我们应该考虑多少 PC 以计算单元格的邻域关系的信息，例如用于聚类函数或 tSNE 。sc.pl.pca_variance_ratio(adata, n_pcs=20)
```

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMKsKouDkb1d7icticSfzH61iaqjmYE7DBSoibM16GMeC22ia6qReiaLlpkbsA/640?wx_fmt=png&from=appmsg)

  *   *   *   *   *

```
# 计算算邻域图# 使用数据矩阵的 PCA 表示来计算单元格的邻域图。您可以在这里简单地使用默认值。为了和Scanpy官网保持一致，我们取以下值。sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)sc.tl.leiden(adata, resolution=1.0) sc.tl.umap(adata)
```
```
computing neighbors
    using 'X_pca' with n_pcs = 40
    finished: added to `.uns['neighbors']`
    `.obsp['distances']`, distances for each pair of neighbors
    `.obsp['connectivities']`, weighted adjacency matrix (0:00:07)
running Leiden clustering
    finished: found 9 clusters and added
    'leiden', the cluster labels (adata.obs, categorical) (0:00:00)
computing UMAP
```
```
  finished: added
```
```
    'X_umap', UMAP coordinates (adata.obsm)
```
```
    'umap', UMAP parameters (adata.uns) (0:00:04)
```

  *

```
sc.pl.umap(adata, color="leiden")
```

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMEEInicmic5JjIlKHMWWbxiavDUmHCl0oJhic2PPwxK4KOSXzZibiaiajotjPg/640?wx_fmt=png&from=appmsg)

**4\. adata.obs的变化**

进行到这里其实我们已经完成scanpy基础分析中的关键的数据质控和细胞分群的工作了，后续的我们就根据自己的样本针对性的进行细胞类型注释和下游分析就可以了。因此，分析到这里我准备暂停一下，看一下我的adata对象的变化和详细的细胞数字分群信息。没想到就这一看，就有两个问题让我迷惑了一段时间。我们首先看一下adata对象现在的内容包含有哪些：

  *

```
adata
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'leiden'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'highly_variable', 'highly_variable_rank', 'means', 'variances', 'variances_norm', 'mean', 'std'
    uns: 'log1p', 'hvg', 'pca', 'neighbors', 'leiden', 'umap', 'leiden_colors'
    obsm: 'X_pca', 'X_umap'
    varm: 'PCs'
    layers: 'counts', 'scaled'
    obsp: 'distances', 'connectivities'
```

scanpy生成的adata对象不仅可以保存表达矩阵，每个细胞（如样本来源、细胞类型等）及每个基因（如别名、基因ID等）还会有自己的注释信息。而最为重要的和我们后续分析息息相关的细胞注释相关的基因信息就存储在**adata.var** 中。细胞数字分群信息则包含在了**adata.obs** 中。如果没有接触过adata对象的同学可以先看下我们[一文了解Python中的单细胞通货：AnnData](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528513&idx=1&sn=1ff1b8bee321f8f5bcac425ce96dc6ff&scene=21#wechat_redirect>)帖子。除此之外adata对象还可以和Seurat对象实现无缝转换，详细的转换过程可以参考[Seurat与Scanpy的数据转换](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533070&idx=1&sn=eb762b5b475695f418438d6628d8012f&scene=21#wechat_redirect>)。

  *   *

```
# 细胞注释信息adata.obs
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMtCOmQDgRIofuEvTmztJbgImZVgfxfuR9FvfWvE7LIGAw5KUorAtCYA/640?wx_fmt=png&from=appmsg)

  *   *

```
# 基因注释信息adata.var
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMfI5G2M5HM0icicmiaI29I0tPEib7C3kKtGey7wlxibqGEZRVNwGhz4kIhkw/640?wx_fmt=png&from=appmsg)

## **
**

## **4.1 问题1：n_genes和n_genes_by_counts区别是什么？**

  *   *

```
# 如果仅想查看adata.obs列名称的话可以运行下方代码adata.obs.columns
```
```
Index(['n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts',
       'total_counts', 'log1p_total_counts', 'total_counts_mt',
       'log1p_total_counts_mt', 'pct_counts_mt', 'leiden'],
      dtype='object')
```

可以看到，和细胞相关的信息很多哈，比如'pct_counts_mt'表示当前细胞线粒体基因的表达比例，'leiden'则为每个细胞的数字分群。但是'n_genes'和 'n_genes_by_counts'这两列仅通过列名分辨的话，让人一下子难以分辨清楚。而且如果你仔细对比两列数值的话，你也会发现对于同一个细胞内部，他们数值上也会有细微的差异。如下图的第一个细胞的'n_genes'是781，而'n_genes_by_counts'是779。那么这两列区别是什么呢？稍后我们来一起探讨一下。

## **4.2 问题2：mean_counts、means和mean区别是什么？**

  *

```
adata.var.columns
```
```
Index(['gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts',
       'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts',
       'log1p_total_counts', 'highly_variable', 'highly_variable_rank',
       'means', 'variances', 'variances_norm', 'mean', 'std'],
      dtype='object')
```

和基因相关的注释信息也是有很多列哈。有一些是比较好理解的，比如gene_ids'代表的是基因ENS编码。'mt'代表的是该基因是否是线粒体相关的基因。但是后面开始有一些列就让人摸不着头脑来了。比如：mean_counts、means和mean列他们就像是三胞胎一样，也是一下子很难从肉眼判断出他们的区别是什么。

那么，为了解决以上两个问题，接下来我们就抽丝剥茧，看看他们究竟是在哪一个分析步骤生成的，以及他们具体的含义有什么不同！

# **5\. n_genes和n_genes_by_counts区别**

## **5.1 初始对象**

  *   *   *   *   *   *

```
# 数据读入adata = sc.read_10x_mtx(    "/data/scanpy/data/filtered_gene_bc_matrices/hg19",  # 表达矩阵存储位置    var_names="gene_symbols",  # 使用基因符号作为变量名    cache=True,   #写入缓存文件以便后续读取更快)
```
```
... reading from cache file cache/data-scanpy-data-filtered_gene_bc_matrices-hg19-matrix.h5ad
```

  *   *   *   *

```
# 确保基因id唯一adata.var_names_make_unique()
adata
```
```
AnnData object with n_obs × n_vars = 2700 × 32738
    var: 'gene_ids'
```

## **5.2 n_genes**

  *   *   *   *   *   *   *   *

```
cell_id = "AAACATACAACCAC-1"
# 获取该细胞的表达向量（可能是稀疏矩阵）cell_expr = adata[cell_id, :].X
# 计算非 0 基因的数量nonzero_genes = (cell_expr > 0).sum()print(f"当前基因总数为{adata.n_vars} , 细胞 {cell_id} 表达非 0 的基因数量为: {nonzero_genes}")
```
```
当前基因总数为32738 , 细胞 AAACATACAACCAC-1 表达非 0 的基因数量为: 781
```

  *   *   *   *

```
# 基本过滤sc.pp.filter_cells(adata, min_genes=200)  sc.pp.filter_genes(adata, min_cells=3)adata
```
```
filtered out 19024 genes that are detected in less than 3 cells
AnnData object with n_obs × n_vars = 2700 × 13714
obs: 'n_genes'
var: 'gene_ids', 'n_cells'
```

  *

```
adata.obs
```

---

| n_genes
---|---
AAACATACAACCAC-1| 781
AAACATTGAGCTAC-1| 1352
AAACATTGATCAGC-1| 1131
AAACCGTGCTTCCG-1| 960
AAACCGTGTATGCG-1| 522
...| ...
TTTCGAACTCTCAT-1| 1155
TTTCTACTGAGGCA-1| 1227
TTTCTACTTCCTCG-1| 622
TTTGCATGAGAGGC-1| 454
TTTGCATGCCTCAC-1| 724

2700 rows × 1 columns

## **5.3 n_genes_by_counts**

  *   *   *   *   *   *   *   *   *   *   *

```
# 线粒体基因表达比例# 为 adata.var 数据框添加一个布尔类型的 "mt" 列，True 表示对应基因是线粒体基因，False 表示不是# 注意: 人为 MT 开头 ,小鼠为 mt 开头adata.var["mt"] = adata.var_names.str.startswith("MT-")sc.pp.calculate_qc_metrics(    adata,     qc_vars=["mt"], # 指定要单独计算质控指标的变量集合，这里是之前标记的线粒体基因（"mt" 列）    percent_top=None, # 不计算 top N 基因的占比统计    log1p=True, # 对数据进行 log (1+x) 转换    inplace=True # 直接在原 AnnData 对象中添加计算结果，不返回新对象)
```

  *

```
adata
```
```
AnnData object with n_obs × n_vars = 2700 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
```

关键：这一步运行完成后，在adata.obs中会得到新的一列就是n_genes_by_counts。

  *

```
adata.obs[['n_genes', 'n_genes_by_counts']]
```

---

| n_genes| n_genes_by_counts
---|---|---
AAACATACAACCAC-1| 781| 779
AAACATTGAGCTAC-1| 1352| 1352
AAACATTGATCAGC-1| 1131| 1129
AAACCGTGCTTCCG-1| 960| 960
AAACCGTGTATGCG-1| 522| 521
...| ...| ...
TTTCGAACTCTCAT-1| 1155| 1153
TTTCTACTGAGGCA-1| 1227| 1224
TTTCTACTTCCTCG-1| 622| 622
TTTGCATGAGAGGC-1| 454| 452
TTTGCATGCCTCAC-1| 724| 723

2700 rows × 2 columns

  *   *   *   *   *   *   *   *

```
cell_id = "AAACATACAACCAC-1"
# 获取该细胞的表达向量（可能是稀疏矩阵）cell_expr = adata[cell_id, :].X
# 计算非 0 基因的数量nonzero_genes = (cell_expr > 0).sum()print(f"当前基因总数为{adata.n_vars} , 细胞 {cell_id} 表达非 0 的基因数量为: {nonzero_genes}")
```
```
当前基因总数为13714 , 细胞 AAACATACAACCAC-1 表达非 0 的基因数量为: 779
```

## **
**

## **5.4 小结**

n_genes和n_genes_by_counts区别在于这两列中间我们执行了下方步骤：sc.pp.filter_genes(adata, min_cells=3)，过滤了表达少于三个细胞的基因，导致基因总数发生了变化。n_genes统计的是过滤之前完整矩阵每个细胞表达的基因数目，n_genes_by_counts统计的是过滤了基因之后每个细胞表达的基因数目。n_genes_by_counts会小于等于n_genes的数值。

# **6\. mean_counts、means和mean区别**

## **6.1 初始对象**

  *   *   *   *   *   *

```
# 数据读入adata = sc.read_10x_mtx(    "/data/scanpy/data/filtered_gene_bc_matrices/hg19",  # 表达矩阵存储位置    var_names="gene_symbols",  # 使用基因符号作为变量名    cache=True,   #写入缓存文件以便后续读取更快)
```
```
... reading from cache file cache/data-scanpy-data-filtered_gene_bc_matrices-hg19-matrix.h5ad
```

  *   *   *   *

```
# 确保基因id唯一adata.var_names_make_unique()
adata
```
```
AnnData object with n_obs × n_vars = 2700 × 32738
    var: 'gene_ids'
```

**6.2 mean_counts**

  *   *   *   *

```
# 基本过滤sc.pp.filter_cells(adata, min_genes=200)  sc.pp.filter_genes(adata, min_cells=3)adata
```
```
filtered out 19024 genes that are detected in less than 3 cells
```
```
AnnData object with n_obs × n_vars = 2700 × 13714
    obs: 'n_genes'
    var: 'gene_ids', 'n_cells'
```

  *

```
adata.var
```
[/code]
```

---

| gene_ids| n_cells
---|---|---
AL627309.1| ENSG00000237683| 9
AP006222.2| ENSG00000228463| 3
RP11-206L10.2| ENSG00000228327| 5
RP11-206L10.9| ENSG00000237491| 3
LINC00115| ENSG00000225880| 18
...| ...| ...
AC145212.1| ENSG00000215750| 16
AL592183.1| ENSG00000220023| 323
AL354822.1| ENSG00000215615| 8
PNRC2-1| ENSG00000215700| 110
SRSF10-1| ENSG00000215699| 69

13714 rows × 2 columns

  *   *   *   *   *   *   *   *   *   *   *   *

[code]
# 线粒体基因表达比例# 为 adata.var 数据框添加一个布尔类型的 "mt" 列，True 表示对应基因是线粒体基因，False 表示不是# 注意: 人为 MT 开头 ,小鼠为 mt 开头adata.var["mt"] = adata.var_names.str.startswith("MT-")sc.pp.calculate_qc_metrics(    adata,     qc_vars=["mt"], # 指定要单独计算质控指标的变量集合，这里是之前标记的线粒体基因（"mt" 列）    percent_top=None, # 不计算 top N 基因的占比统计    log1p=True, # 对数据进行 log (1+x) 转换    inplace=True # 直接在原 AnnData 对象中添加计算结果，不返回新对象)adata
```
```
AnnData object with n_obs × n_vars = 2700 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
```

  *

```
adata.var
```

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnxKiaziaQLpTHVibBzTNBmicpnvDtsGG7ae6h7ribUwibTlD3wgnHFBU5O0P2eHEO0kl8oHLbiaXCZvJaDWch8dHbI7Z43icncQsHPIe8/640?wx_fmt=png&from=appmsg)

分析到这里，我们的第一个主角终于出现了，我们以第一个基因AL627309.1为例，他的mean_counts数值为0.003333。这个其实是比较简单的，我们可以从一个简单的数学上的除法运算计算得到。通过这个列名我们可以推测下mean_counts列应该是计算了当前的基因AL627309.1在所有细胞中的平均counts数目。

  *   *   *

```
# 目前剩余所有细胞数目cell_num = adata.n_obsprint(cell_num)
```
```
2700
```

  *   *   *

```
# AL627309.1基因检测到的总counts数目counts = adata.var.loc['AL627309.1','n_cells_by_counts']print(counts)
```

9

  *   *   *

```
# AL627309.1基因在所有细胞的mean_countsmean_counts = counts / cell_numprint(mean_counts)
```

0.0033333333333333335

和adata.var中该基因的mean_counts数值一模一样，所以mean_counts代表的就是某基因在所有细胞中的平均counts数目。

## **6.3 means**

  *   *   *   *   *   *   *   *   *   *

```
# 细胞过滤,去除表达过多线粒体基因或表达基因总数过多或过低的细胞：adata = adata[    (adata.obs.n_genes_by_counts < 2500)    & (adata.obs.n_genes_by_counts > 200)    & (adata.obs.pct_counts_mt < 5),    :,].copy()adata.layers["counts"] = adata.X.copy()
adata
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
    layers: 'counts'
```

  *   *   *   *   *   *

```
# 矩阵标准化sc.pp.normalize_total(adata, target_sum=1e4)# 数据进行对数处理sc.pp.log1p(adata)adata# 执行标准化和对数转换（会修改adata.X），此时adata.X是标准化并对数转换后的数据，原始数据仍保存在adata.layers['counts']中
```
```
normalizing counts per cell
    finished (0:00:00)
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
    uns: 'log1p'
    layers: 'counts'
```

  *   *   *   *   *   *   *   *   *   *

```
# 识别高变基因sc.pp.highly_variable_genes(    adata,    layer="counts",    n_top_genes=2000,    min_mean=0.0125,    max_mean=3,    min_disp=0.5,    flavor="seurat_v3",)
```
```
extracting highly variable genes
--> added
    'highly_variable', boolean vector (adata.var)
    'highly_variable_rank', float vector (adata.var)
    'means', float vector (adata.var)
    'variances', float vector (adata.var)
    'variances_norm', float vector (adata.var)
```

  *

```
adata
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'highly_variable', 'highly_variable_rank', 'means', 'variances', 'variances_norm'
    uns: 'log1p', 'hvg'
    layers: 'counts'
```

  *

```
adata.var
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwEoDVhM9sSUm17UJ7bSibSMTUDspGXkARNAdicg4ecnqg903DS96fpoLcaiatjmt2KW0oLvGnIjxIqw/640?wx_fmt=png&from=appmsg)第二位主角means则出现在sc.pp.highly_variable_genes高变基因计算完成后。means其实也是表示基因在所有细胞的平均counts数目。但是由于这里我们再次基于线粒体基因表达比例对于对于adata对象进行了过滤，所以我们的细胞数目有了新的变化。我们还是以AL627309.1为例，它的means数值为0.003412。

  *   *   *

```
# 目前剩余所有细胞数目cell_num = adata.n_obsprint(cell_num)
```
```
2638
```

  *   *   *

```
# AL627309.1基因检测到的总counts数目counts = adata.var.loc['AL627309.1','n_cells_by_counts']print(counts)
```
```
9
```

  *   *   *

```
# AL627309.1基因在所有细胞的mean_countsmean_counts = counts / cell_numprint(mean_counts)
```
```
0.003411675511751327
```

## **6.4 mean**

  *   *   *   *   *   *

```
# 创建缩放层并存储原始表达数据adata.layers["scaled"] = adata.X.toarray()# 同样在"scaled"图层上操作# 这一步是降维、聚类等分析的重要预处理步骤sc.pp.scale(adata, max_value=10, layer="scaled")adata
```
```
AnnData object with n_obs × n_vars = 2638 × 13714
    obs: 'n_genes', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt'
    var: 'gene_ids', 'n_cells', 'mt', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'highly_variable', 'highly_variable_rank', 'means', 'variances', 'variances_norm', 'mean', 'std'
    uns: 'log1p', 'hvg'
    layers: 'counts', 'scaled'
```

  *

```
adata.var
```

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmiaopkToW1FnJqbg7pK1oVa8ibMricKyJgtNp6GRB8FOweGtSOgriapIwy9oMibqRIEr8Ewe7hbREgCWuebgGia3hEkic3nINujoAywU/640?wx_fmt=png&from=appmsg)

最后一个mean出现在sc.pp.scale计算完成后，那么mean数值应该至少是和sc.pp.scale计算步骤有关。官方解释为Means per gene before scaling。也就是mean为scaled层计算这个基因在所有细胞的表达量的均值，尤其要注意这里的scale由来，我们这里来源于adata.layers["scaled"] = adata.X.toarray()这一步骤的赋值过程。

我们还是以AL627309.1基因为例，他的mean数值是0.005436。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
gene = "AL627309.1"idx = adata.var_names.get_loc(gene)
# 1. 准备 layeradata.layers["scaled"] = adata.X.toarray()
# 2. 在 scale 之前计算该基因的 meanX_gene = adata.layers["scaled"][:, idx]manual_mean = np.mean(X_gene)
# 3. scale（会把 mean 写入 adata.var['mean']）sc.pp.scale(adata, layer="scaled")
# 5. 对比print("manual_mean:", manual_mean)print("adata.var mean:", adata.var.loc[gene, "mean"])
```
```
manual_mean: 0.0054355143
adata.var mean: 0.005435514305467584
```

结果一致

## **6.5 小结**

mean_counts、means和mean分别来源于sc.pp.calculate_qc_metrics、sc.pp.highly_variable_genes和sc.pp.scale步骤结果。计算过程中随时要注意矩阵的维度变化。但是他们也有一定相似，其实都是表征了对应基因在不同细胞间的表达均值结果。

**四、资料领取**

一切不给测试文件和分析环境版本的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmhkj45qgWOm55Ls72ZCZf3QPtofxoKMicRbfQbeC83qthvnYHTbfktFwHO2ltlzS4DQiaq20bWGfIbE19hHM1Qa27k8QicPZobib8/640?wx_fmt=png&from=appmsg)

通过网盘分享的文件: https://pan.baidu.com/s/1ou3GyYT44BHWyYHYm0Hpvw

提取码: 1e2d

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/buxFNhaTGwmWquhHgdGWKLZvp5qASTJvmC930n0OfFudicn6Xrr6BfnIwmSTPyjCDn8o0KRyhaaX2GHJmxftOSV8V82Aa4Byia5gjib67QraW8/640?wx_fmt=jpeg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=qywuinol&tp=webp#imgIndex=77)

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

向下滑动查看更多

欢迎大家致谢~

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=7lj2ti0t&tp=webp#imgIndex=78)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=8)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=9)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=10) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
