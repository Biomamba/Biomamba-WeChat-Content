---
title: "代码复写| CellRank的教程重现"
date: 2024-01-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507012&idx=1&sn=fb01cca63326fd6e8c682434a53fc2ea&chksm=9b3ca514ac4b2c02115ae5dea368190ce74997ac16a07fdc29f76cef815600b1e5b813c71163#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写| CellRank的教程重现

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507012&idx=1&sn=fb01cca63326fd6e8c682434a53fc2ea&chksm=9b3ca514ac4b2c02115ae5dea368190ce74997ac16a07fdc29f76cef815600b1e5b813c71163#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是07号作品。本作品复写了题为"CellRank for directed single-cell fate mapping"的论文，**文章链接** ：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8828480/
**复现图片集锦** ：

![](../../images/81665b76f2df518e.webp)

一、复写内容

## Fig. 1: Combining RNA velocity with cell-cell similarity to determine initial and terminal states and compute a global map of cellular fate potential.

使用dygen的模拟数据描述CellRank特性

# 准备

## 导入相关包

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
# 数据分析基础包import numpy as npimport pandas as pd
import matplotlib.pyplot as pltfrom mpl_toolkits.mplot3d import Axes3D import seaborn as sns
import osimport sys
# 单细胞相关包import scanpy as scimport scanpy.external as sceimport scvelo as scvimport cellrank as cr
# 相关工具日志输出等级sc.settings.verbosity = 2cr.settings.verbosity = 2scv.settings.verbosity = 3
```

## 设置路径

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 添加工作路径，项目主目录sys.path.insert(0, "..")
# 使用py文件统一管理路径from paths import DATA_DIR, FIG_DIR
# 当前notebook输出图片的路径FIG_DIR = FIG_DIR / "fig_1_concept"
# 相关工具输出图片的位置设置scv.settings.figdir = str(FIG_DIR)sc.settings.figdir = str(FIG_DIR)cr.settings.figdir = str(FIG_DIR)
```

## 全局绘图设置

  *   *   *   *

```
# scvelo的绘图参数dpi = 120scv.settings.set_figure_params("scvelo", dpi_save=dpi, dpi=dpi, transparent=True, fontsize=20, color_map="viridis")scv.settings.plot_prefix = ""
```

## 导入dygen模拟数据

  *   *   *

```
adata = scv.read(DATA_DIR / "dyngen_simulated_data" / "bifurcating.h5ad")scv.pl.scatter(adata, color=["lineage","global_time"]) # 模拟数据已知细胞类型和伪时间金标准adata
```

# 运行基础分析

## 数据预处理，构建KNN图

### 原始数据保存（使用scanpy的预处理）

  *   *   *   *   *   *   *

```
# 创建新adata，用作scanpy数据变换， 后续查看基因表达都要用这个adataadata_raw = adata.copy()sc.pp.filter_genes(adata_raw, min_cells=3)scv.pp.normalize_per_cell(adata_raw)sc.pp.log1p(adata_raw)sc.pp.highly_variable_genes(adata_raw)adata.raw = adata_raw # 保存为raw
```

### 用作速率图计算的数据（使用scvelo的预处理）

  *   *   *   *   *   *   *   *   *   *

```
# 数据变换scv.pp.filter_genes(adata, min_shared_counts=20)scv.pp.normalize_per_cell(adata)scv.pp.filter_genes_dispersion(adata, n_top_genes=34)scv.pp.log1p(adata)
# pca与邻居构建sc.tl.pca(adata, random_state=0)# sc.pl.pca_variance_ratio(adata) # 查看pca重要性，提取关键维度sc.pp.neighbors(adata, n_pcs=7, n_neighbors=15, random_state=0)
```

## 使用scVelo计算速率图（Fig1 a）

二维速率图展示

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
scv.pp.moments(adata, n_pcs=7)
# 保存邻居结构到adata_raw上adata_raw.obsp["connectivities"] = adata.obsp["connectivities"].copy()adata_raw.obsp["distances"] = adata.obsp["distances"].copy()adata_raw.uns["neighbors"] = adata.uns["neighbors"].copy()
scv.pp.moments(adata_raw, n_neighbors=None)
scv.tl.recover_dynamics(adata, n_jobs=8)scv.tl.velocity(adata, mode="dynamical", n_jobs=8)scv.tl.velocity_graph(adata)scv.pl.velocity_embedding_stream(adata, legend_fontsize=12, title="", smooth=0.8, min_mass=2.5,                                 color="lineage")
```

![](../../images/a0d75c92e8c14bc3.webp)

三维速率图展示

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
umap = adata.obsm["X_umap"] # 提取3D降维图velocity = adata.obsm["velocity_umap"]color = scv.utils.interpret_colorkey(adata, c="lineage")
fig = plt.figure(dpi=dpi)ax = fig.add_subplot(111, projection="3d")ax.scatter(umap[:, 0], umap[:, 1], umap[:, 2], c=color, cmap="viridis")
# 绘制箭头ax.quiver(umap[:, 0], umap[:, 1], umap[:, 2], velocity[:, 0], velocity[:, 1], velocity[:, 2],          color="k", normalize=True, length=0.5, arrow_length_ratio=0.5, linewidth = 0.5)
ax.view_init(20, 100)
# 关闭坐标轴ax.set_xticklabels([])ax.set_yticklabels([])ax.set_zticklabels([])
plt.savefig(FIG_DIR / "fig_1_a_high_dim_projection.pdf")plt.show()
```

![](../../images/0fe23e98bda3587e.webp)

  *   *

```
adata.obsm["X_umap"][:, :2] = -adata.obsm["X_umap"][:, :2] # 微调二维UMAP降维图微调成与论文中一致，后续图片与论文中一致adata_raw.obsm["X_umap"][:, :2] = -adata_raw.obsm["X_umap"][:, :2]
```

# 运行CellRank

## 初始化kernel和estimator

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
from cellrank.tl.estimators import GPCCA
# 转移矩阵计算中的参数配置weight_connectivities=0.2mode="stochastic" n_jobs=8softmax_scale=None
# 计算转移矩阵kernel = cr.tl.transition_matrix(adata,                                      weight_connectivities=weight_connectivities,                                      mode=mode,                                      n_jobs=n_jobs,                                      softmax_scale=softmax_scale)
# GPCCA进行矩阵分解g_fwd = GPCCA(kernel)
# 鉴定宏状态g_fwd.compute_macrostates(n_states=4, cluster_key="lineage")
g_fwd
```

## 绘制细胞级别和宏状态级别的转移矩阵（Fig1 c）

### 细胞级别的转移矩阵（Fig1 c左上角）

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 提取转移矩阵T = adata.obsp["T_fwd"].A
# 排序meta_states_probs = g_fwd.macrostates_membershipscell_assignment = meta_states_probs.argmax(1).X.flatten() p = np.argsort(cell_assignment) # 根据到终止状态宏状态的最大概率进行排序print(meta_states_probs.names)
vmax = np.quantile(T[T>0], 0.90)
fig = plt.figure(None, dpi=dpi)ax = fig.add_subplot(111)
cax = ax.imshow(T[p ,:][:, p], vmin=0, vmax=vmax, cmap="Reds", interpolation="sinc", filterrad=4.0)
ax.set_xticks([])ax.set_yticks([])ax.set_title("transition matrix")
plt.colorbar(mappable=cax)plt.savefig(FIG_DIR / "fig_1_c_1_transition_matrix.pdf", bbox_inches="tight")plt.show()
```
```
['sA -> sB_1' 'sA -> sB_2' 'sD -> sEndD' 'sC -> sEndC']
```

![](../../images/faabeac03aae397d.webp)

### 宏状态级别的转移矩阵（Fig1 c右上角）

  *   *   *   *   *   *

```
fig_kwargs = {"text_kwargs": {"fontsize": 40},              "show_stationary_dist": False,              "annotate": False,              "cmap": "viridis",              "save":"fig_1_c_2_transition_matrix_coarse.pdf"}g_fwd.plot_coarse_T(**fig_kwargs)
```

![](../../images/fc440347b7609727.webp)

### 宏状态在UMAP中的显示（Fig 1c下部）

  *   *   *   *   *   *

```
g_fwd.compute_macrostates(n_states=4, cluster_key="lineage")
fig_kwargs = {"discrete": True,              "legend_loc": "right",              "save": "fig_1_c_3_macrostates.pdf"}g_fwd.plot_macrostates(**fig_kwargs)
```

![](../../images/5dcdb020c3c57d58.webp)

鉴定，区分宏状态中的初始和终止状态，区分Fig1 c下部的初始、终止状态

  *   *   *   *   *

```
g_fwd.compute_terminal_states()g_fwd._compute_initial_states()
# 使用scvelo绘制scv.pl.scatter(adata, c=["initial_states", "terminal_states"], legend_loc="right")
```

![](../../images/cc479868f5bdc69a.webp)

## UMAP图上计算吸收概率（Fig1 d）

  *   *   *   *   *   *   *   *

```
# 计算吸收概率g_fwd.compute_absorption_probabilities(keys=["sD -> sEndD", "sC -> sEndC"])
fig_kwargs = {"dpi": dpi,              "add_outline": True,              "legend_loc": "right",              "save":"fig_1_d_fate_map.pdf"}g_fwd.plot_absorption_probabilities(**fig_kwargs)
```

![](../../images/e182d2f798e6b946.webp)

## 可视化基因表达趋势（Fig1 e）

### UMAP降维图上的marker基因表达（Fig1 e左部）

  *   *   *   *   *   *   *   *   *   *   *

```
# 绘制谱系相关的基因fig_kwargs = {"color": ["114","72"],  # 背景知识已知114，72基因分别对应着终止状态sC-sEndC, sB->sEndD的marker基因              "ncols": 1,              "perc": [0, 98],               "dpi": dpi,               "title": ["gene 1", "gene 2"],               "colorbar": False,               "color_map": "viridis",               "size": 100,              "save": "fig_1_e_1_gene_expression_embedding.pdf"}scv.pl.scatter(adata, **fig_kwargs)
```

![](../../images/f58457945fbd0ac6.webp)

### Marker基因着伪时间变化的曲线（Fig1 e右部）

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 这里用scanpy处理的基因表达值来绘制曲线adata_raw.obsm["to_terminal_states"] = adata.obsm["to_terminal_states"].copy()adata_raw.uns["terminal_states_colors"] = adata.uns["terminal_states_colors"].copy()
fig_kwargs = {"data_key": "Ms",               "genes": ["114", "72"],               "ncols": 1,               "legend_loc": None,               "time_key": "global_time", # 这里的伪时间是已知的金标准              "same_plot": True,               "hide_cells": True,              "save":"fig_1_e_2_gene_expression_time.pdf"}
model = cr.ul.models.GAM(adata_raw, n_knots=6, spline_kwargs={"lam": 5})cr.pl.gene_trends(adata_raw, model=model, **fig_kwargs)
```

## 展示潜在的驱动基因热图（Fig1 f）

### 早、中、晚期Marker基因在UMAP降维图上的表达值（Fig1 f左部）

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
fig_kwargs = {"color": ["11", "54",  "43"],              "ncols":1,http://localhost:12345/notebooks/%E5%85%AC%E4%BC%97%E5%8F%B7/%E5%AF%BB%E5%9B%A0/%E5%AF%BB%E5%9B%A0%E6%9D%AF/%E5%AF%BB%E5%9B%A0%E6%9D%AF%E7%A8%BF%E4%BB%B6/07_HuangJoya/paper_reproducibility_xunyin/notebook/fig1_concept.ipynb#%E6%97%A9%E3%80%81%E4%B8%AD%E3%80%81%E6%99%9A%E6%9C%9FMarker%E5%9F%BA%E5%9B%A0%E5%9C%A8UMAP%E9%99%8D%E7%BB%B4%E5%9B%BE%E4%B8%8A%E7%9A%84%E8%A1%A8%E8%BE%BE%E5%80%BC%EF%BC%88Fig1-f%E5%B7%A6%E9%83%A8%EF%BC%89              "legend_loc": "on data",               "layer": "Ms",               "perc": [0, 99],               "colorbar": False,              "color_map": "viridis",               "title": ["GeneX", "GeneY", "GeneZ"],               "dpi": dpi,               "size": 100,              "save": "fig_1_f_1_early_late_genes.pdf"}
scv.pl.scatter(adata_raw, **fig_kwargs)
```

![](../../images/88b4b33670d8cdc1.webp)

###

### 随伪时间的表达热图（Fig1 f右部）¶

计算所有基因与终止状态吸收概率的相关性corr与显著性pval等统计值。

  *   *

```
g_fwd.compute_lineage_drivers(use_raw=True)# adata.raw.varm["terminal_lineage_drivers"] # 排序后展示
```

![](../../images/d45e9ccb06beb3f1.png)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 选择其中与“sD -> sEndD”终止状态相关的基因lin = "sD -> sEndD"corr = adata.raw.varm["terminal_lineage_drivers"].sort_values(by=f"{lin}_corr", ascending=False) # 按照与吸收概率的相关性从小到达排序，越靠前表示越早期的Marker基因corr = corr.head(50)
# 绘制参数fig_kwargs = {"genes": corr.index,              "lineages": [lin],              "cluster_key": "lineage",              "time_key": "global_time",              "data_key": "Ms",              "show_absorption_probabilities": False,              "figsize": (10, 15),              "show_all_genes": False,              "weight_threshold": (0.05, 0.05),              "xlabel": "Pseudotime",              "save": "fig_1_f_2_heatmap.pdf",              "dpi":dpi,              }
model = cr.ul.models.GAM(adata_raw, n_knots=10)cr.pl.heatmap(adata_raw, model, **fig_kwargs)
```

## Fig. 2: Delineating fate choice in pancreatic development & Fig. 3 :Zooming into the delta state to explain differentiation paths¶

Fig 2: 在胰腺Pancreas数据集上运行，鉴定初始状态和终止状态，展示Ngn3 high EP细胞到各个终止状态的命运概率 Fig 3: Fev+细胞亚群细分，并解释到Delta细胞的关键基因

# 准备

## 导入相关包

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
# 数据分析基础包import numpy as npimport pandas as pd
import matplotlib.pyplot as pltimport seaborn as sns
import osimport sysfrom typing import Optional
# 单细胞相关包import scanpy as scimport scanpy.external as sceimport scvelo as scvimport cellrank as crfrom anndata import AnnData
# 工具from cellrank.tl._utils import _merge_categorical_series
# 相关工具日志输出等级sc.settings.verbosity = 2cr.settings.verbosity = 2scv.settings.verbosity = 3
```

## 设置路径

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 添加工作路径，项目主目录sys.path.insert(0, "..")
# 使用py文件统一管理路径from paths import DATA_DIR, FIG_DIR
# 当前notebook输出图片的路径FIG_DIR = FIG_DIR / "fig_2_pancreas_main"
# 相关工具输出图片的位置设置scv.settings.figdir = str(FIG_DIR)sc.settings.figdir = str(FIG_DIR)cr.settings.figdir = str(FIG_DIR)
```

## 全局绘图设置

  *   *   *   *   *   *   *

```
# scvelo的绘图参数dpi = 120scv.settings.set_figure_params("scvelo", dpi_save=dpi, dpi=dpi, transparent=True, fontsize=20, color_map="viridis")scv.settings.plot_prefix = ""
# 是否保存图片save_figure = True
```

## 导入Pancreas胰腺数据

  *   *   *   *

```
DATA_DIR / "pancreas" / "pancreas.h5ad"adata = cr.datasets.pancreas(DATA_DIR / "pancreas" / "pancreas.h5ad")magic_imputed_data = pd.read_csv(DATA_DIR / "pancreas" / "pancreas_magic_imputed_data.csv", index_col=0) # 使用magic插补后的数据adata
```

#

# 使用scVelo计算和分析速率（Fig 2）¶

## 数据预处理

### 原始数据保存（使用scanpy的预处理）

  *   *   *   *   *   *   *   *

```
# 创建新adata，用作scanpy数据变换adata_raw = adata.copy()sc.pp.filter_genes(adata_raw, min_cells=10)scv.pp.normalize_per_cell(adata_raw)sc.pp.log1p(adata_raw)
sc.pp.highly_variable_genes(adata_raw)adata.raw = adata_raw # 保存为raw
```

添加MAGIC插补后的数据

  *   *

```
assert(adata_raw.shape == magic_imputed_data.shape), "Shape mismatch between AnnData and MAGIC imputed data"adata_raw.layers["magic_imputed_data"] = magic_imputed_data[adata_raw.var_names].loc[adata_raw.obs_names]
```

### 用作速率图计算的数据

  *   *   *   *   *   *   *

```
# 数据变换scv.pp.filter_and_normalize(adata, min_shared_counts=20, log=True, n_top_genes=2000)
# pca与邻居构建sc.tl.pca(adata)sc.pp.neighbors(adata, n_pcs=30, n_neighbors=30)scv.pp.moments(adata, n_pcs=30, n_neighbors=30)
```

## 使用scVelo计算速率图（Fig2 a）

  *   *   *   *   *   *   *   *   *   *

```
scv.tl.recover_dynamics(adata, n_jobs=8)scv.tl.velocity(adata, mode="dynamical")
scv.tl.velocity_graph(adata)
fig_kwargs = {"color": ["clusters"],                 "legend_loc": "right",                 "dpi": dpi,                 "save": "fig_2_a_velocities_umap.pdf"}scv.pl.velocity_embedding_stream(adata, **fig_kwargs)
```

![](../../images/e933c4f9626dd239.webp)

# 运行CellRank（Fig2）

## 初始化kernel和estimator

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
from cellrank.tl.estimators import GPCCA
# 转移矩阵计算中的参数配置weight_connectivities=0.2mode="stochastic" n_jobs=8softmax_scale=None
# 计算转移矩阵kernel = cr.tl.transition_matrix(adata,                                     weight_connectivities=weight_connectivities,                                     mode=mode,                                     n_jobs=n_jobs,                                     softmax_scale=softmax_scale)
# GPCCA进行矩阵分解g_fwd = GPCCA(kernel)
# 鉴定宏状态n_states = 12 # 论文中对应着12个宏状态g_fwd.compute_macrostates(cluster_key="clusters", n_states=n_states)
g_fwd
```

## 宏状态在UMAP中的显示（Fig 2b）

原文略有差异，文章没有提供Cache文件，无法完全复现宏状态，但大致类似。细胞类型的文字需要手动移动到指定位置上

  *   *

```
fig_kwargs = {"legend_loc": "right", "discrete": False, "dpi":dpi, "size": 100, "save":"fig_2_b_macrostates_umap.pdf"}g_fwd.plot_macrostates(**fig_kwargs)
```

![](../../images/46e2a97578e7049f.webp)

## 宏状态级别的转移矩阵（Fig2 c）¶

需要Adobe Illustrator/Adobe Acraft手动把坐标轴中相同细胞类型的宏状态进行合并。

  *   *   *   *   *   *   *   *   *

```
T_coarse = g_fwd.coarse_T# NOTE: 根据具体的宏状态按照顺序指定macro_names = ["Ngn3 low EP_1", "Ngn3 low EP_2", "Ngn3 high EP_1", "Ngn3 high EP_2", "Ngn3 high EP_3", "Ngn3 high EP_4", "Ngn3 high EP_3", "Fev+", "Epsilon", "Alpha", "Delta", "Beta"]
fig = plt.figure(None, (6, 5), dpi=dpi)ax = fig.add_subplot(111)sns.heatmap(T_coarse[macro_names].loc[macro_names], cmap="viridis", ax=ax)plt.savefig(FIG_DIR / "fig_2_c_t_coarse.pdf", bbox_inches="tight")plt.show()
```

![](../../images/37cddee402a9dfab.webp)

## 初始和终止状态在UMAP中的显示（Fig 2d）

计算初始和终止状态

  *   *   *   *

```
g_fwd.compute_terminal_states() # 鉴定终止状态print("===> 自动计算的终止状态：", list(adata.obs["terminal_states"].cat.categories)) # 自动计算的终止状态有偏差g_fwd.set_terminal_states_from_macrostates(names=["Alpha", "Beta", "Epsilon", "Delta"]) # 新机器上跑出来Epilon又是单独的一群了g_fwd._compute_initial_states() # 鉴定初始状态
```

UMAP绘制初始和终止状态

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 对于手动添加的初始、终止状态，添加注释def _create_initial_terminal_annotations(    adata: AnnData,    terminal_key: str = "terminal_states",    initial_key: str = "initial_states",    terminal_prefix: Optional[str] = "terminal",    initial_prefix: Optional[str] = "initial",    key_added: Optional[str] = "initial_terminal",) -> None:    """    Create categorical annotations of both initial and terminal states.        This is a utility function for creating a categorical :class:`pandas.Series` object which combines    the information about initial and terminal states. The :class:`pandas.Series` is written directly    to the :class:`anndata.AnnData`object. This can for example be used to create a scatter plot in :mod:`scvelo`.    Parameters    ----------    adata        AnnData object to write to ``.obs[key_added]``.    terminal_key        Key from ``adata.obs`` where terminal states have been saved.    initial_key        Key from ``adata.obs`` where initial states have been saved.    terminal_prefix        Forward direction prefix used in the annotations.    initial_prefix        Backward direction prefix used in the annotations.    key_added        Key added to ``adata.obs``.    Returns    -------    None        Nothing, just writes to ``adata``.    """
    # get both Series objects    cats_final, colors_final = (        adata.obs[terminal_key],        adata.uns[f"{terminal_key}_colors"],    )    cats_root, colors_root = adata.obs[initial_key], adata.uns[f"{initial_key}_colors"]
    # merge    cats_merged, colors_merged = _merge_categorical_series(        cats_final,        cats_root,        colors_old=list(colors_final),        colors_new=list(colors_root),    )
    # adjust the names    final_names = cats_final.cat.categories    final_labels = [        f"{terminal_prefix if key in final_names else initial_prefix}: {key}"        for key in cats_merged.cat.categories    ]    cats_merged = cats_merged.cat.rename_categories(final_labels)
    # write to AnnData    adata.obs[key_added] = cats_merged    adata.uns[f"{key_added}_colors"] = colors_merged
```

  *   *   *   *   *

```
_create_initial_terminal_annotations(adata)
figure_params = {"title": f"initial and terminal states", "legend_loc": "right", "dpi": dpi,                  "color": "initial_terminal", "s": 150, "save": "fig_2_d_initial_terminal.pdf"}scv.pl.scatter(adata, **figure_params)
```

![](../../images/d8d79b48e69e40f1.webp)

##

## 计算吸收概率（Fig2e）

### 绘制所有细胞的到达终止状态的命运概率（吸收概率）（Fig 2e上部）

  *   *   *   *

```
g_fwd.compute_absorption_probabilities()
figure_kwargs = {"title": f"cell fate map", "dpi": dpi, "same_plot": True, "size": 100, "legend_loc": "right", "save":"fig_2_e_1_fate_probabilities.pdf"}g_fwd.plot_absorption_probabilities(**figure_kwargs)
```

![](../../images/ed1a2dfd1f824b4d.webp)

###

### 合并Ngn3 high EP到终止状态的命运概率（Fig2 e下部）

  *   *   *   *   *   *

```
figure_kwargs = {"cluster_key": "clusters",                  "mode": "heatmap",                 "lineages": ["Alpha", "Beta", "Epsilon", "Delta"],  # 不同机器跑出的结果不一样                 "clusters": ["Ngn3 high EP"], "figsize": (1, 3),                 "save": "fig_2_e_2_ngn3_high_fate_probs.pdf"}cr.pl.cluster_fates(adata, **figure_kwargs)
```

![](../../images/e784d7a11006f021.webp)

## 可视化基因趋势（Fig 2f）

基因趋势的拟合参数

  *   *   *   *   *   *   *   *   *   *   *

```
pseudotime = "palantir_pseudotime" # 使用palantir计算出的伪时间data_key = "magic_imputed_data" # 使用MAGIC插补的数据，更加平滑
# pyGAM设置n_knots = 10weight_threshold = (0.05, 0.05)
# mgcv设置n_knots_mgcv = 6weight_threshold_mgcv = (1e-3, 1e-3)smoothing_penalty_mgcv = 10.0
```

把终止状态移动到adata_raw上

  *   *

```
adata_raw.obsm["to_terminal_states"] = adata.obsm["to_terminal_states"].copy()adata_raw.uns["terminal_states_colors"] = adata.uns["terminal_states_colors"].copy()
```

绘制Marker基因在UMAP上的表达值

  *   *   *   *   *

```
# 用于绘制的基因，这里表示四种终止状态的Marker基因fig_2_genes = ["Arx", "Pdx1", "Irs4", "Hhex"]
fig_kwargs = {"color": fig_2_genes, "perc": [0, 99], "ncols": 1, "title": fig_2_genes, "size": 100, "colorbar": False, "save":"fig_2_f_1_gene_expression_umap.pdf", }scv.pl.scatter(adata_raw, **fig_kwargs)
```

![](../../images/30eed4624b7c16aa.webp)

绘制Marker基因随着伪时间变化的趋势曲线

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 使用mgcvmodel = cr.ul.models.GAMR(adata_raw, n_knots=n_knots_mgcv, smoothing_penalty=smoothing_penalty_mgcv)
fig_kwargs = {"model": model,              "data_key": data_key,               "gene_as_title": False,               "legend_loc": None,              "genes": fig_2_genes,               "ncols": 1,              "time_key": pseudotime,               "same_plot": True,               "hide_cells": True,              "weight_threshold": weight_threshold_mgcv,               "figsize": (6, 9),               "suptitle": "",              "save": "fig_2_f_2_gene_trends_mgcv.pdf"}
cr.pl.gene_trends(adata_raw, **fig_kwargs)
```

# Delta亚群细分（Fig 3）

重新调整图片文件保存路径

  *   *   *   *   *   *   *   *   *   *

```
# 使用py文件统一管理路径from paths import DATA_DIR, FIG_DIR
# 当前notebook输出图片的路径FIG_DIR = FIG_DIR / "fig_3_pancreas_delta"
# 相关工具输出图片的位置设置scv.settings.figdir = str(FIG_DIR)sc.settings.figdir = str(FIG_DIR)cr.settings.figdir = str(FIG_DIR)
```

##

## Fev+细胞亚群细分的UMAP降维图（Fig 3a）

  *   *   *   *   *   *   *   *

```
fig_kwargs = {"color": "clusters_fine",                 "legend_loc": "right",                 "groups": ["Fev+ Beta", "Fev+ Alpha", "Fev+ Delta","Fev+ Epsilon", "Fev+ Pyy"],                "title": "subclustering of Fev+ cells",                  "dpi": 150,                 "save": "fig_3_a_fev+.pdf"                }scv.pl.scatter(adata, **fig_kwargs)
```

![](../../images/4925d2c9758e344d.webp)

##

## 到达Delta细胞的命运概率的UMAP降维图（Fig 3b）

  *   *   *   *   *   *

```
fig_kwargs = {"same_plot": False,              "perc": [0, 96],              "dpi": dpi,              "states": ["Delta"],              "save":"fig_3_b_fate_probabilities_umap.pdf"}g_fwd.plot_absorption_probabilities(**fig_kwargs)
```

![](../../images/5611ffbd2eeda90d.webp)

## Fev+到达Delta细胞的命运概率的小提琴分布图（Fig 3c）

  *   *   *   *   *   *   *

```
fev_clusters = ["Fev+ Beta", "Fev+ Alpha", "Fev+ Delta", "Fev+ Epsilon", "Fev+ Pyy"]fig_kwargs = {"mode": "violin",              "lineages": ["Delta"],              "cluster_key": "clusters_fine",              "clusters": fev_clusters,              "save":"fig_3_c_fate_probabilities_fev+_violin.pdf"}cr.pl.cluster_fates(adata, **fig_kwargs)
```

![](../../images/6b6ea57600526005.webp)

## 展示潜在驱动向delta分化的基因热图（Fig 3d）

### 随伪时间的表达热图（Fig3 d左部）

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
g_fwd.compute_lineage_drivers(lineages=["Delta"], cluster_key="clusters", clusters=["Fev+"],                               use_raw=True)delta_corr = adata.raw.varm["terminal_lineage_drivers"].sort_values(by="Delta_corr", ascending=False)delta_corr = delta_corr.head(50)print(f"Selected {len(delta_corr)} genes")
# using mgcvmodel = cr.ul.models.GAMR(adata_raw, n_knots=n_knots_mgcv, smoothing_penalty=smoothing_penalty_mgcv)fig_kwargs = {"model": model,               "genes": delta_corr.index,               "lineages": ["Delta"],               "cluster_key": "clusters",               "data_key": data_key,               "time_key": pseudotime,               "show_absorption_probabilities": False,               "figsize": (10, 8),               "show_all_genes": False,               "weight_threshold": weight_threshold_mgcv,              "save": "fig_3_d_1_heatmap_small_mgcv.pdf"}
cr.pl.heatmap(adata_raw, **fig_kwargs)
```

### 早、中、晚期Marker基因在UMAP降维图上的表达值（Fig3 d右部）

  *   *   *   *

```
delta_genes = ["Hhex", "Cd24a", "Hadh"]fig_kwargs = {"color": delta_genes, "size": 100, "layer": "magic_imputed_data", "title": delta_genes, "ncols":1,             "dpi": dpi, "colorbar": False, "save":"fig_3_d_2_known_genes.pdf"}scv.pl.scatter(adata_raw, **fig_kwargs)
```

![](../../images/43c95a08fca58aee.webp)

## 基因聚类（Fig 3e）TODO: 这里聚类结果时好时坏，选择的基因也时有时无

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 执行基因聚类model = cr.ul.models.GAM(adata_raw, n_knots=n_knots)gene_cluster_kwargs = {"model": model,                        "genes": adata_raw.var_names,                        "lineage": "Delta",                        "time_key": pseudotime,                        "n_jobs": n_jobs,                        "data_key": data_key,                        "recompute": True,                        "random_state": 0,                        "weight_threshold": weight_threshold,                        "clustering_kwargs": {"resolution": 0.2, "random_state": 0},                       "neighbors_kwargs": {"random_state": 0}}
cr.pl.cluster_lineage(adata_raw, **gene_cluster_kwargs) # 展示所有基因群gdata = adata_raw.uns["lineage_Delta_trend"].copy()
```

![](../../images/2ead46a329f09917.webp)

选择其中的第0群查看

  *   *   *   *   *   *   *   *   *   *   *   *

```
gene_clusters = ["2"] # NOTE: 这里群选择要按照基因聚类的结果选择
mask = np.in1d(gdata.obs["clusters"], gene_clusters)gene_df = gdata[mask].obs
# 重新计算该群的驱动基因g_fwd.compute_lineage_drivers(lineages=["Delta"], cluster_key="clusters",                               clusters=["Fev+"], use_raw=True)
gene_df = gene_df.join(adata.raw.varm["terminal_lineage_drivers"])gene_df = gene_df.sort_values(by="Delta_corr", ascending=False) # 按照相关性排序gene_df.head(10) # 看看前几个最高的
```

![](../../images/eaedd814025787aa.png)

  *   *   *   *   *   *   *   *

```
# candidates = ["Map2k4", "Msi1", "Nefl"] # NOTE: 选择基因聚类也不能完全聚出文中的效果，但还后续还能看# {gene: np.where(np.in1d(gene_df.index, gene))[0][0] for gene in candidates}
candidates = ["Map2k4", "Msi1", "Nefl"]
fig_kwargs = {"color": candidates, "layer": data_key, "title": candidates, "colorbar": False, "size": 100,              "perc": [0, 99], "save": "fig_3_e_candidate_drivers.pdf"}scv.pl.scatter(adata_raw, **fig_kwargs)
```

![](../../images/4694adbcf74fe5a9.webp)

## Extended Data Fig. 2: GPCCA and fate probabilities extract the essence of cellular state transitions. ¶

使用简单示例解释GPCCA

# 准备

## 导入相关包

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
# import standard packagesimport numpy as npimport pandas as pd
import matplotlib.pyplot as pltimport seaborn as sns
import osimport sys
# 马尔可夫链与网络绘图包import pydtmcimport networkx as nx
import cellrank as cr
cr.settings.verbosity = 2
```

## 设置路径

  *   *   *   *   *   *   *   *   *   *   *

```
# 添加工作路径，项目主目录sys.path.insert(0, "..")
# 使用py文件统一管理路径from paths import DATA_DIR, FIG_DIR
# 当前notebook输出图片的路径FIG_DIR = FIG_DIR / "extended_fig2"
# 相关工具输出图片的位置设置cr.settings.figdir = str(FIG_DIR)
```

##

## Set global parameters

## 全局绘图设置

  *

```
dpi = 120
```

# 把GPCCA应用到示例数据集上

## 构造示例数据，创建Markov链

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
p = np.array([    # 0.   1.   2.   3.   4.   5.   6.   7.   8.   9.   10.  11.       [0.0, 0.8, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], #0    [0.2, 0.0, 0.6, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], #1    [0.6, 0.2, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], #2        [0.0, 0.05, 0.05, 0.0, 0.6, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], #3    [0.0, 0.0, 0.0, 0.25, 0.0, 0.25, 0.4, 0.0, 0.0, 0.1, 0.0, 0.0], #4    [0.0, 0.0, 0.0, 0.25, 0.25, 0.0, 0.1, 0.0, 0.0, 0.4, 0.0, 0.0], #5        [0.0, 0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.7, 0.2, 0.0, 0.0, 0.0], #6    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.8, 0.0, 0.0, 0.0], #7    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.2, 0.0, 0.0, 0.0, 0.0], #8        [0.0, 0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0, 0.7, 0.2], #9    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.8], #10    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.2, 0.0], #11            ])
```

  *   *   *

```
states = np.arange(p.shape[1]).astype("str")mc = pydtmc.MarkovChain(p, list(states))print(mc)
```

## 可视化状态空间，细胞间的转移矩阵（Extend Fig 2a）

  *   *   *   *   *   *   *   *   *   *   *   *

```
fig_kwargs = {"self_loops": False,               "self_loop_radius_frac": 0.05,               "labels": states,               "layout": nx.layout.spring_layout,               "color_nodes": False,               "node_size": 3000,               "edge_weight_scale": 10,               "font_size": 22,               "edge_width_limit": 10,              "save": "extended_fig_2_a_graph.pdf",              "dpi": dpi}cr.pl.graph(p, **fig_kwargs)
```

![](../../images/c3c1cde08866aea8.webp)

## 计算Shur分解，展示特征值（Fig 2b）

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 设置核from cellrank.tl.kernels import PrecomputedKernelpk = PrecomputedKernel(p)
# 修改内部AnnData对象pk._adata.obs_names = statesannot = ["initial", "initial", "initial", "interm", "interm", "interm", "terminal_1", "terminal_1", "terminal_1",          "terminal_2", "terminal_2", "terminal_2"]pk._adata.obs["clusters"] = pd.Series(index=pk._adata.obs_names, data=annot, dtype="category")
# GPCCA进行矩阵分解g_cr = cr.tl.estimators.GPCCA(pk)
# 计算分解的特征值g_cr.compute_schur(method="krylov", n_components=12, which="LR")
fig_kwargs = {"real_only": True,              "marker": "o",              "s": 100,              "figsize": (6, 6),              "save":"extended_fig_2_b_spectrum.pdf",              "dpi": dpi}g_cr.plot_spectrum(**fig_kwargs)
```

![](../../images/b5b435af4c07d106.png)

## 可视化转移矩阵（Extend Fig 2c）

  *   *   *   *   *

```
fig =  plt.figure(None, (9, 7), dpi=dpi)ax = fig.add_subplot(111)sns.heatmap(p, cmap="viridis")plt.savefig(FIG_DIR / "extended_fig_2_c_transition_matrix.pdf")plt.show()
```

![](../../images/047f546a16949e3a.png)

## 可视化宏状态矩阵（Extended Fig2d）

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
n_states = 4n_cells = 3
g_cr.compute_macrostates(n_states=n_states, n_cells=n_cells, cluster_key="clusters")g_cr.compute_terminal_states(n_cells=n_cells, method="stability")macro_names = ["initial", "interm", "terminal_1", "terminal_2"]T_coarse = g_cr.coarse_T
fig = plt.figure(None, (6, 5), dpi=dpi)ax = fig.add_subplot(111)sns.heatmap(T_coarse[macro_names].loc[macro_names], cmap="viridis")plt.savefig(FIG_DIR / "extended_fig_2_d_t_coarse.pdf")plt.show()
```

![](../../images/eab40d5eab483b49.png)

## 可视化所有细胞到宏状态的概率（Extended Fig2e）

  *   *   *   *   *

```
m_g = g_cr._macrostates_memberships[macro_names]sns.heatmap(m_g, robust=True, annot=False, ax=plt.figure(None, (5, 10)).gca(), fmt=".2f",           cmap="viridis", xticklabels=m_g.names)plt.savefig(FIG_DIR / "extended_fig_2_e_membership_matrix.pdf")plt.show()
```

![](../../images/4df46634e7c2c94f.png)

## 可视化到终止状态的命运概率（Extended Fig2f）

  *   *   *   *   *   *

```
g_cr.compute_absorption_probabilities()m_c = g_cr.absorption_probabilities[["terminal_1", "terminal_2"]]sns.heatmap(m_c, robust=True, annot=False, ax=plt.figure(None, (5, 10)).gca(), fmt=".2f",           cmap="viridis", xticklabels=m_c.names)plt.savefig(FIG_DIR / "extended_fig_2_f_fate_probs.pdf")plt.show()
```

![](../../images/6925cd8b8d90b110.png)

## Fig. 4: CellRank predicts reprogramming outcome

CellRank应用到小鼠体外重编程数据，并与CellTagging获得真实的轨迹标签比较

# 准备

## 导入相关包

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
# 数据分析基础包import numpy as npimport pandas as pd
import matplotlib.pyplot as pltimport seaborn as sns
import osimport sys
# 单细胞相关包import scanpy as scimport scanpy.external as sceimport scvelo as scvimport cellrank as cr
# 相关工具日志输出等级sc.settings.verbosity = 2cr.settings.verbosity = 2scv.settings.verbosity = 3
```

## 设置路径

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 添加工作路径，项目主目录sys.path.insert(0, "..")
# 使用py文件统一管理路径from paths import DATA_DIR, FIG_DIR
# 当前notebook输出图片的路径FIG_DIR = FIG_DIR / "fig_4_reprogramming"
# 相关工具输出图片的位置设置scv.settings.figdir = str(FIG_DIR)sc.settings.figdir = str(FIG_DIR)cr.settings.figdir = str(FIG_DIR)
```

##

## 全局绘图设置

  *   *   *   *

```
# scvelo的绘图参数dpi = 120scv.settings.set_figure_params("scvelo", dpi_save=dpi, dpi=dpi, transparent=True, fontsize=20, color_map="viridis")scv.settings.plot_prefix = ""
```

## 导入重编程数据

  *   *   *   *

```
adata = cr.datasets.reprogramming_morris(path=DATA_DIR / "mef_reprogramming" / "mef_reprogramming.h5ad", subset="48k")# 细胞数太多，这里进行采样sc.pp.subsample(adata, fraction=0.1)adata
```

  *   *

```
scv.pl.scatter(adata, basis="tsne", color=["reprogramming_day", "Apoa1", "Col1a2",  "cluster"],              legend_loc="right",perc=[0, 99], size=30, dpi=dpi, save="fig_4_a_umaps_with_annotations.pdf")
```

![](../../images/3ea9c84e3bfa4345.webp)

# 运行基础分析

## 数据预处理，构建KNN图

### 原始数据保存（使用scanpy的预处理）

  *   *   *   *   *   *   *   *

```
# 创建新adata，用作scanpy数据变换adata_raw = adata.copy()sc.pp.filter_genes(adata_raw, min_cells=10)scv.pp.normalize_per_cell(adata_raw)sc.pp.log1p(adata_raw)
sc.pp.highly_variable_genes(adata_raw)adata.raw = adata_raw # 保存为raw
```

### 用作速率图计算的数据（使用scvelo的预处理）

  *   *   *   *   *   *   *

```
# 数据变换scv.pp.filter_and_normalize(adata, min_shared_counts=20, log=True, n_top_genes=2000)
# pca与邻居构建sc.tl.pca(adata)sc.pp.neighbors(adata, n_pcs=30, n_neighbors=30)scv.pp.moments(adata, n_pcs=None, n_neighbors=None)
```

## 使用scVelo计算速率图（Fig4 b）

  *   *   *   *   *   *   *   *   *   *   *   *

```
n_jobs = 12
scv.tl.recover_dynamics(adata, n_jobs=n_jobs)scv.tl.velocity(adata, mode="dynamical", n_jobs=n_jobs)
scv.tl.velocity_graph(adata, n_jobs=n_jobs)scv.pl.velocity_embedding_stream(adata,                                 basis="tsne",                                 color=["cluster"],                                 legend_loc="right",                                 dpi=dpi,                                 save="fig_4_b_umap_velocity.pdf" )
```

![](../../images/7eea35f179f6ca63.webp)

# 运行CellRank

## 初始化kernel和estimator¶

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
from cellrank.tl.estimators import GPCCA
# 转移矩阵计算中的参数配置weight_connectivities=0.2mode="stochastic" n_jobs=8softmax_scale=None
# 计算转移矩阵kernel = cr.tl.transition_matrix(adata,                                     weight_connectivities=weight_connectivities,                                     mode=mode,                                     n_jobs=n_jobs,                                     softmax_scale=softmax_scale)
# GPCCA进行矩阵分解g_fwd = GPCCA(kernel)
# 鉴定宏状态g_fwd.compute_macrostates(n_states=5, cluster_key="cluster")
g_fwd
```

### 宏状态在UMAP中的显示（Fig 4c）

  *   *   *   *   *   *   *

```
g_fwd.compute_macrostates(n_states=5, cluster_key="cluster")g_fwd.plot_macrostates(discrete=True,                       basis="tsne",                       size=100,                       legend_loc="right",                       dpi=dpi,                        save="fig_4_c_umap_macrostates.pdf")
```

![](../../images/3c598b297a94befd.webp)

## 查看宏状态中"day", "cluster"比例（fig4 d）

  *   *   *

```
g_fwd.plot_macrostate_composition(key="reprogramming_day",                                  dpi=dpi,                                  save="fig_4_d_1_histogram_day.pdf")
```

![](../../images/baf30efde7d439d9.webp)

  *   *   *

```
g_fwd.plot_macrostate_composition(key="cluster",                                  dpi=dpi,                                  save="fig_4_d_2_histogram_cluster.pdf")
```

![](../../images/e14337740bbc0127.webp)

## UMAP图上计算吸收概率（Fig4 e）¶

预测标签

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 手动设置终止状态successful_state = "1"dead_end_state = "3"
g_fwd.set_terminal_states_from_macrostates(names=[successful_state, dead_end_state])g_fwd.compute_absorption_probabilities(use_petsc=True, solver="gmres")
g_fwd.plot_absorption_probabilities(same_plot=False,                                    basis="tsne",                                    size=30,                                    perc=[0, 94],                                     states=successful_state,                                     dpi=dpi,                                    save="fig_4_e_1_umap_fate_probs.pdf")
```

![](../../images/1099b3ab1f946d97.webp)

  *   *

```
adata.obs["reprogramming_probability"] = adata.obsm["to_terminal_states"][successful_state].X.flatten()adata.obs["non_reprogramming_probability"] = adata.obsm["to_terminal_states"][dead_end_state].X.flatten()
```

真实标签

  *   *   *   *   *   *

```
scv.pl.scatter(adata, basis="tsne",               color=["reprogramming"],                legend_loc="right",               size=100,                dpi=dpi,               save="fig_4_e_2_umap_celltag_labels.pdf")
```

![](../../images/0ac38fa6910da7c7.webp)

## 命运概率与真实标签的ROC曲线（fig4 f）

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 与真实标签相比，预测重编程的输出，使用ROC曲线定量描述from typing import Optional, Sequence, Iterablefrom sklearn.linear_model import LogisticRegressionfrom sklearn.model_selection import train_test_splitfrom sklearn import metricsfrom anndata import AnnData
# 定义工具函数def predict_reprogramming_outcome(adata: AnnData,                                   day_key: str = "reprogramming_day",                                  day_selection: Optional[Sequence] = None,                                  binary_label_key: str = "reprogramming",                                  predictor_key: str = "reprogramming_probability",                                   random_state: int = 0,                                   figsize: Optional[Iterable[float]] = None,                                   lw: float = 2,                                   save: Optional[str] = None):    """    Predict reprogramming outcome for a subset of labelled cells given fate probabilities.         Given a subset of days from the reprogramming timecourse, treat the clonal information as ground-truth    binary labels in a classification task in which we predict reprogramming outcome based on fate probabilities     using logistic regression. Data is subsampled so that sucessful/dead-end classes are balanced and split    into train/test sets. Classification is evaluated using ROC curves. Note that cells used to define the terminal    states are always removed from training/test sets.         Parameters    ----    adata        Annotated data matrix.    day_key        Key from `.obs` where time-point information can be found.    day_selection        Lists of strings representing days that the data should be restricted to.     binary_label_key        Key from `.obs` where the ground truth labels from CellTagging can be found.     predictor_key        Key from `.obs` where the fate probability of sucessful reprogramming can be found.    random_state        Random seed used to subsample data.    figzise        Size of the overall figure    save        Path where figure is to be saved            Returns    ---    Noting, just plots the ROC curve.     """        # Restrict to cells from selected days that we have labels for    # Exclude the cells that were used to define the terminal states    if "terminal_states" not in adata.obs.keys():        raise ValueError("Compute terminal states first. ")    terminal_mask = np.sum(adata.obs["terminal_states"].isna())    label_mask = ~adata.obs[binary_label_key].isna()    _mask = np.logical_and(terminal_mask, label_mask)            if day_selection is None:        day_selection = adata.obs[day_key].cat.categories            # get the corresponding colors    _colors = adata.uns[f"{day_key}_colors"]    colors = [_colors[np.where(np.in1d(adata.obs[day_key].cat.categories, day))[0][0]]                       for day in day_selection]            # initialise figure and axis object    fig = plt.figure(None, figsize)    ax = fig.add_subplot(111)            # loop over days    for day, color in zip(day_selection, colors):                # restrict to current day        day_mask = np.in1d(adata.obs[day_key], day)        mask = np.logical_and(_mask, day_mask)        print(f"\nThis selects {np.sum(mask)} cells from day {day}." )
        # For these cells, get data matrices        data = sc.get.obs_df(adata[mask], keys=[binary_label_key, predictor_key])        X = data[predictor_key].values[:, None]        y = np.array(data[binary_label_key].values) == "True"        assert(X.shape[0] == np.sum(mask)), "Shape mismatch between X and number of cells. "
        # Check for inbalanced classes        print(f"There are {100* np.sum(y == True) / len(y):.2f}% positive examples. Correcting for class inbalance. ")
        # Correct for class inbalance        np.random.seed(random_state)
        # split the data into positive and negative examples        positive_mask = y        X_positive, y_positive = X[positive_mask], y[positive_mask]        X_negative, y_negative = X[~positive_mask], y[~positive_mask]
        # subsample the negative examples        neg_ixs = np.random.choice(range(len(y_negative)), size=len(y_positive), replace=False)        X_negative_sub, y_negative_sub = X_negative[neg_ixs], y_negative[neg_ixs]
        # concatenate positive and subsampled negative examples        X_balanced = np.concatenate((X_positive, X_negative_sub))        y_balanced = np.concatenate((y_positive, y_negative_sub))
        # assert that classes are balanced now        assert(np.sum(y_balanced == True) / len(y_balanced) == 0.5), "Class inbalance could not be fixed. "
        # Split into training/test sets        X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, random_state=0, test_size=0.4)        n_data = X_train.shape[0] + X_test.shape[0]        print(f"There are {X_train.shape[0]}/{n_data} training examples and {X_test.shape[0]}/{n_data} testing examples. ")
        # fit logistic regression classifier and show ROC on test set        clf = LogisticRegression(random_state=random_state).fit(X_train, y_train)        metrics.plot_roc_curve(clf, X_test, y_test, ax=ax, name=f"day {day}", lw=lw, color=color)        plt.legend(bbox_to_anchor=(1.05, 1.))         if save is not None:         plt.savefig(save)    plt.show()
```

  *   *

```
predict_reprogramming_outcome(adata, day_selection=["12", "15", "21"], lw=3,                              save=FIG_DIR / "roc_curves.pdf")
```

![](../../images/914114e2944657ce.webp)

##

## Fig. 6: CellRank predicts a novel de-differentiation trajectory in murine lung regeneration ¶

把CellRank应用于小鼠肺部上皮组织时间序列数据集

# 准备

## 导入相关包

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
# 数据分析基础包import numpy as npimport pandas as pd
import matplotlib.pyplot as pltimport seaborn as sns
import osimport sys
# 单细胞相关包import scanpy as scimport scanpy.external as sceimport scvelo as scvimport cellrank as cr
# 相关工具日志输出等级sc.settings.verbosity = 2cr.settings.verbosity = 2scv.settings.verbosity = 3
```

## 设置路径

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 添加工作路径，项目主目录sys.path.insert(0, "..")
# 使用py文件统一管理路径from paths import DATA_DIR, FIG_DIR
# 当前notebook输出图片的路径FIG_DIR = FIG_DIR / "fig_6_lung"
# 相关工具输出图片的位置设置scv.settings.figdir = str(FIG_DIR)sc.settings.figdir = str(FIG_DIR)cr.settings.figdir = str(FIG_DIR)
```

## 全局绘图设置

  *   *   *   *

```
# scvelo的绘图参数dpi = 120scv.settings.set_figure_params("scvelo", dpi_save=dpi, dpi=dpi, transparent=True, fontsize=20, color_map="viridis")scv.settings.plot_prefix = ""
```

  *   *   *   *   *

```
# 计算转移矩阵的参数weight_connectivities=0.2mode="stochastic" n_jobs=8softmax_scale=None
```

## 导入肺部数据

  *   *   *   *

```
adata = cr.datasets.lung(DATA_DIR / "lung" / "lung.h5ad")# 细胞数太多，这里进行采样sc.pp.subsample(adata, fraction=0.1)adata
```

颜色设置

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
from typing import Optional, Iterable, TypeVar, Tuplefrom matplotlib import cm as cmfrom cellrank.tl._colors import _convert_to_hex_colors
def _create_categorical_colors(n_categories: Optional[int] = None):    cmaps = [cm.tab10, cm.Pastel1]    max_cats = sum(c.N for c in cmaps)
    if n_categories is None:        n_categories = max_cats    if n_categories > max_cats:        raise ValueError(            f"Maximum number of colors ({max_cats}) exceeded: `{n_categories}`."        )
    colors = []    for cmap in cmaps:        colors += [cmap(i) for i in range(cmap.N)][: n_categories - len(colors)]        if len(colors) == n_categories:            return _convert_to_hex_colors(colors)
    raise RuntimeError(f"Unable to create `{n_categories}` colors.")
```

  *   *   *   *   *   *   *   *   *

```
adata.obs["clusters"].cat.reorder_categories(["Basal","Goblet","Club activated", "MHC-II+ Club","Club","AT1", "AT2",                                              "Krt8+ ADI", "AT2 activated", "Ciliated activated", "Ciliated",                                                "Neuroendocrine", "Club to ciliated", "Mki67+ proliferation"], inplace=True)n_clusters = len(adata.obs["clusters"].cat.categories)print(f"There are {n_clusters} clusters here. ")
# assign colorsclusters_colors = _create_categorical_colors(n_clusters)adata.uns["clusters_colors"] = clusters_colors
```

#

# 运行基础分析

## 数据预处理，构建KNN图

### 原始数据保存（使用scanpy的预处理）

  *   *   *   *   *   *   *   *

```
# 创建新adata，用作scanpy数据变换adata_raw = adata.copy()sc.pp.filter_genes(adata_raw, min_cells=10)scv.pp.normalize_per_cell(adata_raw)sc.pp.log1p(adata_raw)
sc.pp.highly_variable_genes(adata_raw)adata.raw = adata_raw # 保存为raw
```

### 用作速率图计算的数据（使用scvelo的预处理）

  *   *   *

```
scv.pp.filter_and_normalize(adata, min_shared_counts=20, log=True, n_top_genes=2000)sc.pp.neighbors(adata, n_neighbors=30) # 使用scanpy构建邻居scv.pp.moments(adata, n_neighbors=None)
```

## 使用scVelo计算速率图（Fig 6a）

  *   *   *   *   *   *   *   *   *   *

```
scv.tl.recover_dynamics(adata, n_jobs=n_jobs)scv.tl.velocity(adata, mode="dynamical", n_jobs=n_jobs)scv.tl.velocity_graph(adata, n_jobs=n_jobs)
airway_subset = ["Basal", "Goblet", "Club activated", "MHC-II+ Club", "Club"]fig_kwargs = {"color": ["clusters"],               "legend_loc": "right",               "dpi": 200,              "save": "fig_6_a_umap_velocities.pdf"}scv.pl.velocity_embedding_stream(adata, **fig_kwargs)
```

![](../../images/356156c4d18b95a8.webp)

# 运行CellRank

## 初始化kernel和estimator

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```python
from cellrank.tl.estimators import GPCCA
# 计算转移矩阵kernel = cr.tl.transition_matrix(adata,                                     weight_connectivities=weight_connectivities,                                     mode=mode,                                     n_jobs=n_jobs,                                     softmax_scale=softmax_scale)
# GPCCA进行矩阵分解g_fwd = GPCCA(kernel)
# 鉴定宏状态n_states = 9g_fwd.compute_macrostates(cluster_key="clusters", n_states=n_states, n_cells=30)
g_fwd
```

## 宏状态在UMAP中的显示（Fig 6b）

  *   *

```
g_fwd.plot_macrostates(legend_loc="right", dpi=150, discrete=True, size=100,                       save=scv.settings.figdir + "fig_6_c_umap_macrostates.pdf")
```

![](../../images/98baf40bf69a6368.webp)

  *   *

```
g_fwd.set_terminal_states_from_macrostates()g_fwd.compute_absorption_probabilities(solver="gmres", n_jobs=n_jobs)
```

## 所有细胞的环图（Fig 6c）

  *   *   *   *   *   *   *   *   *

```
cr.pl.circular_projection(adata,                          keys=["clusters"],                           legend_loc="right",                          figsize=(40, 40),                          title="",                          normalize_by_mean=True,                          s=70,                           dpi=dpi,                          save="fig_6_c_circ_clusters.pdf" )
```

![](../../images/a8c0238e7c9a3800.webp)

## 到终止状态basal的吸收概率（Fig 6d）

  *   *   *   *   *   *

```
fig_kwargs = {"same_plot": False,              "dpi": dpi,              # "states": ["Basal"], # 这里由于抽样了，没有检测到该状态              "states": ["Club"],              "save": "fig_6_d_umap_fate_probs.pdf"}g_fwd.plot_absorption_probabilities(**fig_kwargs)
```

![](../../images/57ec260478aef80a.webp)

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/19PJI-UqPxKUG3XeQH0V0_Q?pwd=sxia

提取码：sxia

![](../../images/aa4b0e49bcc66553.jpg)

02

三、合作方介绍

****本次活动由**Biomamba生信基地** 组织主办、**北京寻因生物科技** 有限公司独家冠名、科研者之家、西柚云超算联合赞助，设立总价值约**50W** 的科研助力基金。
北京寻因生物科技有限公司：

北京寻因生物科技有限公司（简称寻因生物）成立于2018年，秉承“用技术温暖生命，预见未来”的企业愿景，致力于全球单细胞市场标准普世化发展，推动单细胞技术在早筛、临床、药研等应用方向的深耕落地，为全球科学家、技术公司及药企工业等客户提供可信赖的高品质单细胞技术服务及实验室建设解决方案。

科研者之家：

科研者之家（www.home-for-researchers）是目前国内最知名的科研工具箱平台，以“科研不停，神器不止”为理念，自2019年上线以来，多款工具火爆科研界，如AI写作助手、Figdraw在线绘图平台、生信零代码平台、AI润色、DLP一键改写降重、中文版Pubmed、课题思路助手等。截止目前，包括Nature，Advanced Materials等顶级期刊在内，科研者之家相关科研工具被论文引用已超2300次之多。

西柚云超算：

西柚云是一家专注于科研共享计算的云服务基建型公司。于2022年推出独立研发的大禹共享型计算系统，具有实例动态迁移（拒绝传统型共享服务器单节点卡顿）、开箱即用的生信环境、每个用户拥有[独立的实例和root权限](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)等特性。

03

四、往期作品回顾

[干细胞样CD4+ T细胞与自身免疫性血管炎](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506684&idx=1&sn=c27703a05d4fffae6a5e9e54b4fa7dfe&chksm=9b3ca3acac4b2abaa1e5d4f4a7e4d0730f2e5c4d72c7b3d3d29a653c3bae6590d90e31908dde&scene=21#wechat_redirect>)
[结直肠癌免疫图谱中的基因表达程序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506720&idx=2&sn=4760277df5a7b6f0d6d1698ac734aa3b&chksm=9b3ca270ac4b2b66b0330e822893fa233ba3bdfd45d857097fba6e86561196c1497c20db25b8&scene=21#wechat_redirect>)
[MLP模型鉴定免疫细胞发育和瘤内T细胞耗竭的单细胞染色质图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506754&idx=1&sn=3e3e9b4857bb0371b7c1113df792df2e&chksm=9b3ca212ac4b2b043baf0c72684d186a1c065ff7b3d865c308aff4f3483ab5923638fda8d1ff&scene=21#wechat_redirect>)
[T Cell单细胞参考图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506779&idx=1&sn=dc97a74cfac6caeabaa838160385c3b2&chksm=9b3ca20bac4b2b1da51998764b22ac3c08415298a47ded14283337386f18f9548749de70725e&scene=21#wechat_redirect>)
[小鼠纹状体单细胞基因变化图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506900&idx=1&sn=83774f3062e42ca0eee1df2cf19144f0&chksm=9b3ca284ac4b2b9221736162ac44280d6184c9f8b0cc13bbcc4c914c14b707fe13a850c6418e&scene=21#wechat_redirect>)
[人类肾脏snRNA-seq图谱拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506960&idx=1&sn=9f5913231f9583411e47ccf0dcadedf6&chksm=9b3ca540ac4b2c56a60b5f71ab32e1eacd3194af4bfef819b2de60fc50781360876b45837bf7&scene=21#wechat_redirect>)

04

**本次活动最终解释权归主办方所有!********主办方拥有对作品的编辑、宣发权利!**

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
