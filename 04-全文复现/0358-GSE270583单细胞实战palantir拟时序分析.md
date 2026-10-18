---
title: "GSE270583单细胞实战palantir拟时序分析"
date: 2026-07-30
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539638&idx=1&sn=e6b10f24ec98c8e15046430307399db8&chksm=9b3c22e6ac4babf0cd7fd192be85e514fdf78e9d415fdc6c1af0b28623888bb41324e923dee9#rd
albums: ["全文复现"]
---

# GSE270583单细胞实战palantir拟时序分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539638&idx=1&sn=e6b10f24ec98c8e15046430307399db8&chksm=9b3c22e6ac4babf0cd7fd192be85e514fdf78e9d415fdc6c1af0b28623888bb41324e923dee9#rd
> 合集：全文复现

![](../../images/9734e48a74d488fe.png)

**写在前面**

本教程可视化集锦：

![](../../images/fdb44039fd3a404d.webp)

单细胞发育轨迹分析（Pseudotime Analysis）是揭开细胞分化、状态转换及发育命运谜团的核心技术。传统的分析往往通过聚类识别离散的细胞群，但难以捕捉从祖细胞到成熟谱系之间连续的转录组流形演变。

**Palantir** 算法的出现，为解析这种复杂的发育动态提供了系统性的视角——它不再局限于线性的轨迹推导，而是通过构建扩散映射（Diffusion Maps）和多尺度空间，模拟细胞在分化潜能（Entropy）驱动下的随机游走。Palantir 能够精准计算细胞在发育轴上的拟时间（Pseudotime）位置，并量化其向不同终端谱系分化的概率，从而将零散的单细胞快照串联成一部完整的“发育电影”，识别驱动谱系特异性分化的核心枢纽基因。

**本文主要涵盖以下十大核心实操模块：**

**① 数据读入与初始化：** 演示已注释 AnnData 对象的标准化加载，并完成 Counts 层备份以保障原始表达数据在后续插补中的溯源；

**② 高变基因筛选与降维：** 通过高度变异基因（HVGs）的精准筛选与 PCA 降维，剔除背景噪声，聚焦核心生物学差异信号；

**③ 扩散映射（Diffusion Map）构建：** 深度解析 Palantir 算法基石，构建扩散映射空间以捕捉单细胞数据中复杂的非线性发育流形；

**④ 多尺度空间（Multiscale Space）确定：** 基于扩散组件进一步精炼特征空间，增强流形结构的鲁棒性，为拟时间计算奠定数学基础；

**⑤ 聚类与 UMAP 可视化：** 结合邻近图构建与 Leiden 聚类，在二维 UMAP 空间中直观勾勒前体细胞与各分化分支的分布轮廓；

**⑥ MAGIC 算法表达量插补：** 利用马尔可夫亲和矩阵修复单细胞测序中的数据缺失（Dropout），实现基因表达水平的流形平滑处理；

**⑦ 拟时间核心推断：** 指定分化起点（Root Cell）与多个谱系终点，运行 Palantir 计算拟时间进度、分化熵及命运决策概率；

**⑧ 分支细胞提取与谱系分析：** 根据分化概率矩阵精准识别属于特定分支的细胞子集，并可视化各路径内部的发育流向；

**⑨ 基因动态表达趋势拟合：** 拟合关键 Marker 基因随拟时间轴演变的表达曲线及趋势热图，识别驱动各谱系分化的特征基因；

**⑩ 功能富集与多维统计展示：** 联合 GSEA/GO 分析揭示分支背后的生物学功能转变，并通过拟时间四分位占比统计实现对发育全景的深度解析。

更多教程可见：

****

[![图片](../../images/35e4c65d09fabc5d.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538934&idx=2&sn=9ae059e29a064302bcb737d23a58d87f&scene=21#wechat_redirect>)

学前tips: 本教程基于[Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)环境的[jupyter](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531443&idx=3&sn=0930f54959a9bd13b99780d8f26a1155&scene=21#wechat_redirect>)演示，计算资源不足的同学可参考：[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=2&sn=4708fac31ac8f4e347847e4b7f2a4fed&scene=21#wechat_redirect>)[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21#wechat_redirect>)[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)访问链接：https://biomamba.xiyoucloud.net/欢迎滴滴[Biomamba_zhushou]获取帮助

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)、[生信个性化分](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539480&idx=1&sn=9f1d8a76c0a5ddad4983c3fcf7620622&scene=21#wechat_redirect>)析、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎滴滴[Biomamba_zhushou]获取帮助。

![](../../images/9734e48a74d488fe.png)

**实操流程**

资料下载见文末：
如果你对下面的教程比较迷茫，那么你可以先行学习编程教程：[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)[生信Linux及服务器使用技巧](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2980604042328702978#wechat_redirect>)

**[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520999&idx=2&sn=7f6aa90c2ffa786bd660aa40b109de49&scene=21#wechat_redirect>)**

1.环境导入与依赖准备

  *   *   *   *   *   *   *

```
import osimport scanpy as scimport palantirimport pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as sns
```

2.数据预处理

  *   *   *

```
# 载入已注释的单细胞数据adata = sc.read('/data1/home/zouhuren/data/GSE270583_adata_annotated_v2.h5ad')adata
```

AnnData object with n_obs × n_vars = 19528 × 23055

obs: 'sample', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb', 'leiden', 'cell_type'

var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'n_cells', 'highly_variable', 'means', 'dispersions', 'dispersions_norm', 'highly_variable_nbatches', 'highly_variable_intersection'

uns: 'cell_type_colors', 'hvg', 'leiden', 'leiden_colors', 'log1p', 'neighbors', 'pca', 'rank_genes_groups', 'sample_colors', 'tsne', 'umap'

obsm: 'X_pca', 'X_pca_harmony', 'X_tsne', 'X_umap'

varm: 'PCs'

layers: 'counts'

obsp: 'connectivities', 'distances'

  *   *   *   *   *   *

```
# 备份原始 counts：后续 MAGIC 插补和趋势分析需调用原始计数信息adata.layers["counts"] = adata.X.copy()# 筛选 1500 个高变基因，捕捉细胞间的主要差异信号sc.pp.highly_variable_genes(adata, n_top_genes=1500)# 执行 PCA 降维，为构建发育流形提供基础特征空间sc.pp.pca(adata)
```

#### **3\. 构建扩散映射与多尺度空间**

  *   *   *   *

```
# 计算扩散映射 (Diffusion Map)：Palantir 捕捉非线性发育流形的核心步骤dm_res = palantir.utils.run_diffusion_maps(adata, n_components=5)# 确定多尺度空间：基于扩散组件消除噪声，增强流形结构的稳定性ms_data = palantir.utils.determine_multiscale_space(adata)
```

4\. 聚类与 UMAP 可视化

  *   *   *   *   *   *

```
sc.pp.neighbors(adata)# Leiden 聚类：初步划分细胞群体，设置分辨率为 0.2sc.tl.leiden(adata, resolution=0.2)sc.tl.umap(adata)# UMAP 展示：检查细胞类型在降维空间中的分布情况sc.pl.umap(adata, color='cell_type', frameon=False)
```

![No description has been provided for this image](../../images/4fde68099ad3f206.webp)

#### **5\. MAGIC 插补（填补数据缺失）**

  *   *   *   *   *   *   *   *   *   *   *

```
# MAGIC 插补：填补 Dropout 数据缺失，使基因表达在流形上更加连续、平滑imputed_X = palantir.utils.run_magic_imputation(adata)# 基因表达可视化：展示插补后关键 Marker 基因的表达丰度genes_to_plot = ["Alb", "Lyz2", "S100a8", "Col1a1"]sc.pl.embedding(    adata,    basis="umap",    layer="MAGIC_imputed_data",    color=genes_to_plot,    frameon=False)plt.show()
```

![No description has been provided for this image](../../images/6562fcb81e4d3cc3.webp)

#### **6\. Palantir 核心轨迹推断**

**6.1 起始与终点细胞选择**

  *   *   *   *   *   *   *   *   *

```
# 查看 Monocytes 的细胞数量adata.obs['cell_type'].value_counts()['Monocytes']# 查看 Monocytes 的前几个细胞 barcodemonocytes_barcodes = adata.obs_names[adata.obs['cell_type'] == 'Monocytes']print(monocytes_barcodes[:10])  # 打印前10个# 随机选择一个作为 Palantir 起点import randomstart_cell = random.choice(monocytes_barcodes)print("Monocytes 起点细胞 barcode:", start_cell)
```

Index(['AAACGAACATAAGATG-1', 'AAACGAAGTGAGCGAT-1', 'AAACGAATCAACACCA-1',

'AAAGAACGTTGCCGCA-1', 'AAAGAACTCGCAATGT-1', 'AAAGGATTCGAAGCCC-1',

'AAAGGATTCGACGCGT-1', 'AAAGGGCCATGACAGG-1', 'AAAGGTATCCATCGTC-1',

'AAAGTGATCCCGTAAA-1'],

dtype='object')

Monocytes 起点细胞 barcode: CTGCAGGGTTCCGCTT-1

  *   *   *   *   *   *   *   *   *   *   *   *

```
# Kupffer cells 终点kupffer_cells = adata.obs_names[adata.obs['cell_type'] == 'Kupffer cells']print(kupffer_cells[:10])  # 打印前10个# cDC 终点cdc_cells = adata.obs_names[adata.obs['cell_type'].str.contains('cDC')]print(cdc_cells[:10])# LSECs 终点lsecs_cells = adata.obs_names[adata.obs['cell_type'] == 'LSECs']print(lsecs_cells[:10])# Hepatocytes 终点hepatocytes_cells = adata.obs_names[adata.obs['cell_type'] == 'Hepatocytes']print(hepatocytes_cells[:10])
```

Index(['AAACGAACACGTCATA-1', 'AAACGCTGTTAAGGAT-1', 'AAACGCTTCCTGGGAC-1',

'AAAGAACCATTGAAAG-1', 'AAAGAACTCGCCTCTA-1', 'AAAGGATAGGTGGCTA-1',

'AAAGGATCATGCGGTC-1', 'AAAGGATTCATCGACA-1', 'AAAGGGCAGTCACACT-1',

'AAAGGGCGTAATTAGG-1'],

dtype='object')

Index(['AAACCCACAGCACGAA-1', 'AAACGAACAGCTGAAG-1', 'AAACGCTGTTCAACGT-1',

'AAAGAACAGAGCCGAT-1', 'AAAGAACCAGAAGCTG-1', 'AAAGGATGTTTAAGGA-1',

'AAAGGTAAGGATGCGT-1', 'AAAGTCCCACTTACAG-1', 'AAATGGACAATCGCAT-1',

'AAATGGACAATCTCTT-1'],

dtype='object')

Index(['AAACGAAAGAACCGCA-1', 'AAACGAACACACCAGC-1', 'AAACGAATCGTAACCA-1',

'AAACGCTAGTTAACGA-1', 'AAAGAACCAACGATTC-1', 'AAAGAACTCTCGGTAA-1',

'AAAGGTAGTAGTGTGG-1', 'AAAGTGAGTTGTGGAG-1', 'AACAAAGAGTGCACTT-1',

'AACAACCAGTGTCATC-1'],

dtype='object')

Index(['AAACCCAAGGACGCAT-1', 'AAAGGATTCTGGCCTT-1', 'AAAGTCCCAGACCGCT-1',

'AAAGTGATCGCTTGCT-1', 'AACGTCACAACTCCCT-1', 'AAGACAAAGTTGTCGT-1',

'AAGCGAGAGCGATGCA-1', 'AAGTCGTAGACTTCGT-1', 'AATGACCTCTCTGCTG-1',

'AATGGAACATAATGAG-1'],

dtype='object')

  *   *   *   *   *   *   *   *   *   *   *   *

```
# 起点细胞：Monocytes，被认为是 Kupffer cells 和树突状细胞的前体start_cell = "GTCCTCACAGCACAGA-1"  # 替换成你数据里 Monocytes 中任意代表性细胞的 barcode# 终点细胞：成熟细胞类型的代表性 barcodeterminal_states = pd.Series(    ["Kupffer cells", "cDC", "LSECs", "Hepatocytes"],    index=[        "AAACGAACACGTCATA-1",   # 替换为实际 barcode        "AAACCCACAGCACGAA-1",       # 替换为实际 barcode        "AAACGAAAGAACCGCA-1",     # 替换为实际 barcode        "AAACCCAAGGACGCAT-1" # 替换为实际 barcode    ])
```

  *   *   *   *   *   *

```
# 检查起点start_cell = "GTCCTCACAGCACAGA-1"print(start_cell in adata.obs_names)  # True 才行# 检查终点for cell in terminal_states.index:    print(cell, cell in adata.obs_names)  # 都应该是 True
```

True

AAACGAACACGTCATA-1 True

AAACCCACAGCACGAA-1 True

AAACGAAAGAACCGCA-1 True

AAACCCAAGGACGCAT-1 True

6.2 运行palantir核心函数

  *   *   *   *   *

```
# 运行 Palantir：计算拟时间 (Pseudotime)、分化熵 (Entropy) 及分化概率pr_res = palantir.core.run_palantir(    adata, start_cell, num_waypoints=500,    terminal_states=terminal_states,    eigvec_key='DM_EigenVectors_multiscaled')
```

Sampling and flocking waypoints...

Time for determining waypoints: 0.016318086783091226 minutes

Determining pseudotime...

Shortest path distances using 30-nearest neighbor graph...

Time for shortest paths: 0.23866192897160848 minutes

Iteratively refining the pseudotime...

Correlation at iteration 1: 1.0000

Entropy and branch probabilities...

Markov chain construction...

Computing fundamental matrix and absorption probabilities...

Project results to all cells...

6.3 可视化拟时间和分化概率

  *   *   *   *   *   *   *   *   *   *

```
# 展示拟时间进度图、命运不确定性(熵)图以及各谱系分化概率图palantir.plot.plot_palantir_results(    adata,    s=1,    embedding_basis='X_umap',               # UMAP 展示    pseudo_time_key='palantir_pseudotime',  # 拟时间：颜色渐变 → 细胞从干细胞到成熟细胞的轨迹    entropy_key='palantir_entropy',         # 分化熵；Entropy（命运不确定性）；高熵细胞通常在干细胞或早期祖细胞区域，低熵细胞通常在成熟分支末端    fate_prob_key='palantir_fate_probabilities'  # 分化概率矩阵，颜色表示该细胞向该终点分化的概率)plt.show()
```

![No description has been provided for this image](../../images/1f9f634039d26d9c.webp)

7\. 分支提取与动态演变

  *   *

```
# 选择分支细胞masks = palantir.presults.select_branch_cells(adata, q=.01, eps=.01)
```

  *   *   *   *   *

```
# 假设 masks 的列顺序与 terminal_states 中终点顺序一致branch_Kupffer_cells = adata.obs_names[masks[:, 0]]branch_cDC_cells      = adata.obs_names[masks[:, 1]]  # cDC1 + cDC2branch_LSECs_cells    = adata.obs_names[masks[:, 2]]branch_Hepatocytes_cells = adata.obs_names[masks[:, 3]]
```

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 可视化单分支示例for branch_name, cells in zip(        ['Kupffer cells', 'cDC', 'LSECs', 'Hepatocytes'],        [branch_Kupffer_cells, branch_cDC_cells, branch_LSECs_cells, branch_Hepatocytes_cells]    ):    ad_branch = adata[cells, :].copy()    sc.pl.umap(        ad_branch,        color=["total_counts", "palantir_pseudotime"],  # 用 total_counts 替代 n_counts        frameon=False,        cmap="viridis",        title=branch_name    )
```

![No description has been provided for this image](../../images/da8b93455ac61c13.webp)

![No description has been provided for this image](../../images/777d48667ce83dd1.webp)

![No description has been provided for this image](../../images/58e624abecc40d02.webp)

![No description has been provided for this image](../../images/85b6fc38cc2e82e6.webp)

#### **8\. 基因表达趋势拟合**

  *   *   *   *   *

```
# 计算基因随拟时间变化gene_trends = palantir.presults.compute_gene_trends(    adata,    expression_key="MAGIC_imputed_data")
```

Hepatocytes

[2026-01-08 19:14:50,006] [INFO ] Using sparse Gaussian Process since n_landmarks (500) < n_samples (8,666) and rank = 1.0.

[2026-01-08 19:14:50,008] [INFO ] Using covariance function Matern52(ls=1.0).

[2026-01-08 19:14:52,690] [INFO ] Sigma interpreted as element-wise standard deviation.

cDC

[2026-01-08 19:14:55,105] [INFO ] Using sparse Gaussian Process since n_landmarks (500) < n_samples (4,440) and rank = 1.0.

[2026-01-08 19:14:55,106] [INFO ] Using covariance function Matern52(ls=1.0).

[2026-01-08 19:14:56,225] [INFO ] Sigma interpreted as element-wise standard deviation.

LSECs

[2026-01-08 19:14:59,494] [INFO ] Using sparse Gaussian Process since n_landmarks (500) < n_samples (10,790) and rank = 1.0.

[2026-01-08 19:14:59,495] [INFO ] Using covariance function Matern52(ls=1.0).

[2026-01-08 19:15:00,696] [INFO ] Sigma interpreted as element-wise standard deviation.

Kupffer cells

[2026-01-08 19:15:02,903] [INFO ] Using sparse Gaussian Process since n_landmarks (500) < n_samples (2,557) and rank = 1.0.

[2026-01-08 19:15:02,904] [INFO ] Using covariance function Matern52(ls=1.0).

[2026-01-08 19:15:03,973] [INFO ] Sigma interpreted as element-wise standard deviation.

  *   *   *   *   *   *   *   *   *

```
# 绘制趋势# Alb → 肝细胞特异性标记# Lyz2 → 单核/巨噬细胞标记# S100a8 → 中性粒细胞标记# Col1a1 → 纤维细胞/星状细胞标记genes_of_interest = ["Alb", "Lyz2", "S100a8", "Col1a1"]palantir.plot.plot_gene_trends(adata, genes_of_interest)palantir.plot.plot_gene_trend_heatmaps(adata, genes_of_interest)plt.show()
```

![No description has been provided for this image](../../images/d6403e7bdec3c18f.webp)

![No description has been provided for this image](../../images/e264ca54a5c26376.webp)

  *   *   *   *   *   *   *   *   *

```
# 单分支基因趋势聚类top_genes = adata.var_names[:200]branch_list = ['Hepatocytes', 'Kupffer cells', 'cDC', 'LSECs']branch_communities = {}for branch in branch_list:    communities = palantir.presults.cluster_gene_trends(adata, branch, top_genes)    branch_communities[branch] = communities    palantir.plot.plot_gene_trend_clusters(adata, branch)    plt.show()
```

![No description has been provided for this image](../../images/7d07d234b4f6a60c.webp)

![No description has been provided for this image](../../images/6f13eacde19efe57.webp)

![No description has been provided for this image](../../images/54b274364cde47ed.webp)

![No description has been provided for this image](../../images/745cae30bb0575c2.webp)

#### **9.富集分析（GSEA/GO/KEGG）**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
import gseapy as gpfrom gseapy.plot import dotplot# 针对每个分支 cluster '1' 基因做富集分析go_bp = gp.get_library(name='GO_Biological_Process_2025', organism='Mouse')for branch in branch_list:    communities = branch_communities[branch]    cluster_genes = communities[communities == '1'].index.tolist()    if len(cluster_genes) == 0:        print(f"{branch} 分支 cluster 1 没有基因，跳过富集分析")        continue    enr = gp.enrichr(        gene_list=cluster_genes,        gene_sets=go_bp,        organism='Human'    )    print(f"{branch} 分支 cluster 1 富集 top5:")    display(enr.results.head(5))
```

| Gene_set| Term| Overlap| P-value| Adjusted P-value| Odds Ratio| Combined Score| Genes
---|---|---|---|---|---|---|---|---
0| gs_ind_0| Apoptotic Process (GO:0006915)| 1/232| 0.151753| 0.183559| 9.532682| 17.973872| IL17F
1| gs_ind_0| Cartilage Development (GO:0051216)| 1/57| 0.039389| 0.087071| 39.547741| 127.907594| IL17F
2| gs_ind_0| Cell Surface Toll-Like Receptor Signaling Path...| 1/30| 0.020909| 0.087071| 75.888492| 293.505189| LY96
3| gs_ind_0| Cellular Defense Response (GO:0006968)| 1/47| 0.032582| 0.087071| 48.086587| 164.648719| LY96
4| gs_ind_0| Cellular Response to Interleukin-18 (GO:0071351)| 1/5| 0.003512| 0.051601| 498.368421| 2816.497721| IL18RAP
```
Kupffer cells 分支 cluster 1 富集 top5:
```

| Gene_set| Term| Overlap| P-value| Adjusted P-value| Odds Ratio| Combined Score| Genes
---|---|---|---|---|---|---|---|---
0| gs_ind_0| Blood Vessel Morphogenesis (GO:0048514)| 1/51| 0.003587| 0.007707| 841.574257| 4738.372834| SOX17
1| gs_ind_0| Cardiac Cell Fate Commitment (GO:0060911)| 1/6| 0.000422| 0.006270| 7751.727273| 60234.287030| SOX17
2| gs_ind_0| Circulatory System Development (GO:0072359)| 1/132| 0.009285| 0.013411| 321.342205| 1503.686077| SOX17
3| gs_ind_0| Determination of Heart Left/Right Asymmetry (G...| 1/42| 0.002954| 0.007544| 1024.734940| 5968.593345| SOX17
4| gs_ind_0| Digestive Tract Morphogenesis (GO:0048546)| 1/16| 0.001125| 0.006270| 2748.677419| 18662.433918| SOX17
```
cDC 分支 cluster 1 富集 top5:
```

| Gene_set| Term| Overlap| P-value| Adjusted P-value| Odds Ratio| Combined Score| Genes
---|---|---|---|---|---|---|---|---
0| gs_ind_0| 'De Novo' Post-Translational Protein Folding (...| 1/36| 0.051886| 0.129913| 29.188939| 86.361379| UGGT1
1| gs_ind_0| \+ Reg of Transmembrane Receptor Prot Serine/Th...| 1/84| 0.117091| 0.183547| 12.367606| 26.526132| SULF1
2| gs_ind_0| Adenylate Cyclase-Activating G Protein-Coupled...| 1/153| 0.203384| 0.264096| 6.738665| 10.732392| ADGRB3
3| gs_ind_0| Adenylate Cyclase-Modulating G Protein-Coupled...| 1/202| 0.259721| 0.312996| 5.082188| 6.851536| ADGRB3
4| gs_ind_0| Aerobic Respiration (GO:0009060)| 1/81| 0.113144| 0.182287| 12.831238| 27.960503| SDHAF4
```
LSECs 分支 cluster 1 富集 top5:
```

| Gene_set| Term| Overlap| P-value| Adjusted P-value| Odds Ratio| Combined Score| Genes
---|---|---|---|---|---|---|---|---
0| gs_ind_0| \+ Reg of Transmembrane Receptor Prot Serine/Th...| 1/84| 0.046313| 0.076158| 33.835928| 103.955571| SULF1
1| gs_ind_0| 2-Oxoglutarate Metabolic Process (GO:0006103)| 1/15| 0.008412| 0.049613| 195.800000| 935.561461| ADHFE1
2| gs_ind_0| Action Potential (GO:0001508)| 1/68| 0.037639| 0.072061| 41.903704| 137.432527| KCNB2
3| gs_ind_0| Adenylate Cyclase-Activating G Protein-Coupled...| 1/153| 0.082940| 0.107676| 18.436066| 45.899171| ADGRB3
4| gs_ind_0| Adenylate Cyclase-Modulating G Protein-Coupled...| 1/202| 0.108197| 0.129139| 13.904218| 30.920183| ADGRB3

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 分支列表branch_list = ['Hepatocytes', 'Kupffer cells', 'cDC', 'LSECs']# GO librarygo_bp = gp.get_library(name='GO_Biological_Process_2025', organism='Mouse')for branch in branch_list:    # cluster 1 的基因    communities = branch_communities[branch]    cluster_genes = communities[communities == '1'].index.tolist()    if len(cluster_genes) == 0:        print(f"{branch} 分支 cluster 1 没有基因，跳过富集分析")        continue    # 富集分析    enr = gp.enrichr(        gene_list=cluster_genes,        gene_sets=go_bp,        organism='Human'    )    if enr.res2d.empty:        print(f"{branch} 分支 cluster 1 富集无结果，跳过")        continue    # 新增 -log10(FDR) 列（可以作为颜色参考）    enr.res2d['log10_FDR'] = -np.log10(enr.res2d['Adjusted P-value'] + 1e-300)    # -------------------- 绘图 --------------------    # dotplot 返回 matplotlib Axes    ax = dotplot(        enr.res2d,        title=f'{branch} GO Biological Process',        cmap='viridis_r',        size=12,                     # 放大圆圈        figsize=(6, 8),              # 图大小        cutoff=0.25,                  # 富集比例阈值        fontsize=9,                   # 坐标轴字体        show=False,        legend_title='Significance (-log10 FDR)'  # 图例标题    )    # 调整坐标轴字体大小    ax.tick_params(axis='y', labelsize=9)    ax.tick_params(axis='x', labelsize=9)    # 调整图例标题（部分 gseapy 版本需要这样设置）    if ax.get_legend() is not None:        ax.get_legend().set_title("Significance (-log10 FDR)")    # 自动调整布局    plt.tight_layout()    plt.show()
```

![No description has been provided for this image](../../images/dbf7e41c5fe48f36.webp)

![No description has been provided for this image](../../images/cca6afd343da13a1.webp)

![No description has been provided for this image](../../images/f34b6c97f7e51941.webp)

![No description has been provided for this image](../../images/6c34c0ce8ecaee4a.webp)

10\. Scanpy联合分析10.1 UMAP 可视化 pseudotime 和熵

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
fig, axes = plt.subplots(1, 3, figsize=(18,5))# 1️⃣ cell_type（有 legend）sc.pl.umap(    adata,    color='cell_type',    ax=axes[0],    legend_loc='right margin',  # 关键    show=False)axes[0].set_title("Cell type")# 2️⃣ pseudotime（无 legend）sc.pl.umap(    adata,    color='palantir_pseudotime',    ax=axes[1],    show=False)axes[1].set_title("Palantir pseudotime")# 3️⃣ entropy（无 legend）sc.pl.umap(    adata,    color='palantir_entropy',    ax=axes[2],    show=False)axes[2].set_title("Palantir entropy")plt.tight_layout()plt.show()
```

![No description has been provided for this image](../../images/f695178a873ed78c.webp)

10.2 小提琴图

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
fig, axes = plt.subplots(1, 2, figsize=(14,4))# 左：pseudotimesc.pl.violin(    adata,    keys='palantir_pseudotime',    groupby='cell_type',    rotation=90,    ax=axes[0],    show=False)axes[0].set_title("Palantir pseudotime")# 右：entropysc.pl.violin(    adata,    keys='palantir_entropy',    groupby='cell_type',    rotation=90,    ax=axes[1],    show=False)axes[1].set_title("Palantir entropy")plt.tight_layout()plt.show()
```

![No description has been provided for this image](../../images/1b0bc459922dd5f5.webp)

10.3 pseudotime 四等分与堆积图

  *   *   *   *   *   *   *

```
adata.obs['pseudotime_quartile'] = pd.qcut(adata.obs['palantir_pseudotime'], 4, labels=['Q1','Q2','Q3','Q4'])# 饼图quartile_counts = adata.obs['pseudotime_quartile'].value_counts().sort_index()plt.figure(figsize=(6,6))plt.pie(quartile_counts, labels=quartile_counts.index, autopct='%.1f%%', startangle=90)plt.title('Pseudotime Quartiles')plt.show()
```

![No description has been provided for this image](../../images/13754f24db0524cd.png)

  *   *   *   *   *   *   *   *   *   *

```
# 堆积柱形图：按 cell_type 显示 pseudotime 四分位占比cellnum = pd.crosstab(adata.obs['cell_type'], adata.obs['pseudotime_quartile'])cellprop = cellnum.div(cellnum.sum(axis=0), axis=1).T.reset_index()cellprop.plot(kind='bar', stacked=True, figsize=(8,5))plt.title("Celltype Proportion per Pseudotime Quartile")plt.ylabel("Proportion")plt.xticks(rotation=45)plt.legend(bbox_to_anchor=(1,1))plt.tight_layout()plt.show()
```

![No description has been provided for this image](../../images/f853276bc478ac77.webp)

10.4 密度分布

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
plt.figure(figsize=(8,5))ax = sns.kdeplot(    data=adata.obs,    x='palantir_pseudotime',    hue='cell_type',    fill=True,    alpha=0.3)# 把 legend 移到图外右侧sns.move_legend(    ax,    "center left",    bbox_to_anchor=(1.02, 0.5),    frameon=False)plt.tight_layout()plt.show()
```

![No description has been provided for this image](../../images/f666ed277161ba38.webp)

  *   *   *

```
# 保存到当前目录，文件名自定义adata.write("adata_palantir_full_analysis.h5ad")print("已保存为 adata_pseudotime.h5ad")
```
```
已保存为 adata_pseudotime.h5ad
```

![](../../images/9734e48a74d488fe.png)

**资料领取**

一切不给测试文件和分析环境版本的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：![](../../images/dbfa514d8a686fa2.webp)

通过网盘文件分享的文件：

https://pan.baidu.com/s/1X9xklW5hNCBT0m2EKouzwA

提取码请滴滴我们领取

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

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)

**欢迎交流**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)[‍](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)[料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**助手[Biomamba_zhushou]** ，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif)您点的每个赞和在看，我都认真当成了喜欢
