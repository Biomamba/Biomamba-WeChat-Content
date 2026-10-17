---
title: "学员代码复现|scRNA-seq解析非酒精性脂肪性肝发生机制"
date: 2026-01-09
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534107&idx=1&sn=24c3f2f1a2ba2a3db6d49acc1ba1220a&chksm=9b3c3f4bac4bb65da77d919d3b0b5dcf3987e444260f910055ebf7848c41b78370d33ed244c7#rd
albums: ["全文复现"]
---

# 学员代码复现|scRNA-seq解析非酒精性脂肪性肝发生机制

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534107&idx=1&sn=24c3f2f1a2ba2a3db6d49acc1ba1220a&chksm=9b3c3f4bac4bb65da77d919d3b0b5dcf3987e444260f910055ebf7848c41b78370d33ed244c7#rd
> 合集：全文复现

**一、写在前面**

非酒精性脂肪性肝病（NAFLD）是目前全球最常见的慢性肝病之一，可进一步进展为NASH（非酒精性脂肪性肝炎）、 肝纤维化、肝硬化甚至肝癌。然而，NAFLD的发生发展并不是单一肝细胞异常，而是一个多细胞类型参与、免疫—代谢—炎症高度交织的复杂过程。传统[bulk RNA-seq](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2959853503529910274&token=1721358726&lang=zh_CN#wechat_redirect>)只能得到“平均表达”，难以解析不同细胞亚群在NAFLD中的特异性变化。因此,[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865&token=1721358726&lang=zh_CN#wechat_redirect>)RNA 测序（scRNA-seq）成为解析NAFLD肝脏微环境的关键技术。GSE270583 正是一个基于小鼠模型的NAFLD肝脏单细胞转录组数据集，为研究 NAFLD的[细胞异质性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&payreadticket=HD-76LXEnfWXkPet86Gy-qrQn76Pbx30kmwfg5-oYXJ-pjA-Q3n6dTvTsy8gFiIpSygl5TY&scene=21#wechat_redirect>)和分子机制提供了重要资源。

本推送是我们[82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)的学员作业，单细胞分析并不难学！欢迎联系我们参加课程。

如果需要[Python版单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)/[R语言单细胞小白全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531092&idx=1&sn=9968319b84186bb9b717b7b409132d8b&scene=21#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469&token=827157490&lang=zh_CN#wechat_redirect>)、自测数据个性化分析辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532039&idx=2&sn=1e7a1ae6097fe217182f1ff305325512&scene=21&token=827157490&lang=zh_CN&poc_token=HAu7Q2mj4g12fl0KnW3ea82YSsZC41y8EAkeGbBI#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、样本信息**

该数据集共包含 4 个 scRNA-seq 样本（GSM）：

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibt7lR70tLMwZMpLRGHa3yR77D0nDQqxdeaUBwDEpW4ic5zLAyaQZrgf9g/640?wx_fmt=png&from=appmsg)

**数据集基本信息一览：**

**![image.png](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtZCDU7u4B8JTsicQJPsxJPLmMCIZC22YPfEuK6dyKSkVMVTpgDCJSIxg/640?wx_fmt=png&from=appmsg)**

**三、实操**

#  1、数据读入和对象创建
```
# 加载包import scanpy as scimport anndata as adimport os# 检查版本print(sc.__version__)
```
```
1.11.5
```

**数据下载链接** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE270583

![image.png](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtlO99lZVoyvOqnZksad5EbSfqGzibBLOV7zRN9dj6khwMjOhDpTahQjg/640?wx_fmt=png&from=appmsg)
```
‍
```

# Targeting` ``immune cellular populations and transcription factors: unraveling the therapeutic potential of JQF for NAFLD # 本次分析只涉及 ND 和 HFD 组，不涉及药物干预组`
data_root = "/data1/home/zouhuren/data/scanpy"

# 只获取非隐藏文件夹
samples= [d for d in os.listdir(data_root)
if os.path.isdir(os.path.join(data_root, d)) and not d.startswith(".")]

adatas= {}
for sample_id in samples:
folder = os.path.join(data_root, sample_id)
adata = sc.read_10x_mtx(
folder,
var_names="gene_symbols",
cache=True
)
adata.var_names_make_unique()
adata.obs["sample"] = sample_id
adatas[sample_id] = adata

# 查看读取结果（GSE270583）
for sid, adata in adatas.items():
print(f"\n样本 {sid}: 细胞数 {adata.n_obs}, 基因数 {adata.n_vars}")
```
样本 GSM8347729: 细胞数 10943, 基因数 32285

样本 GSM8347727: 细胞数 7254, 基因数 32285
```

```
样本 GSM8347728: 细胞数 7554, 基因数 32285
```

```
# 将多个样本的 AnnData 对象合并为一个整体 AnnData
# label="sample" 会在合并后的 obs 中添加一列 'sample'，表示每个细胞的来源
adata_all=sc.concat(
    adatas,# 你的字典 adatas
    label="sample",# 生成 obs 中的 'sample' 列
    join="outer",# 合并基因时取并集（有的样本可能有不同基因）
    fill_value=0# 缺失值填 0
)# 确保细胞名字唯一，避免合并后重复
adata_all.obs_names_make_unique()

# 查看每个样本的细胞数量
print(adata_all.obs["sample"].value_counts())

# 查看合并后 AnnData 的基本信息
print(adata_all)
```
```
sample
GSM8347729    10943
GSM8347728     7554
GSM8347727     7254
Name: count, dtype: int64
AnnData object with n_obs × n_vars = 25751 × 32285
         obs: 'sample'
```
```
adata_all.obs
```

| sample
---|---
AAACCCAAGGACGCAT-1| GSM8347729
AAACCCAAGGCTAAAT-1| GSM8347729
AAACCCAAGTTCCAGT-1| GSM8347729
AAACCCACAGCACGAA-1| GSM8347729
AAACCCACATGTAACC-1| GSM8347729
...| ...
TTTGTTGCAAAGCACG-1| GSM8347728
TTTGTTGCAACCGACC-1| GSM8347728
TTTGTTGCATATCTCT-1| GSM8347728
TTTGTTGGTTGCCAAT-1| GSM8347728
TTTGTTGTCACAAGGG-1| GSM8347728

25751 rows × 1 columns

# 2、数据质控及可视化
```
# 1. 标记线粒体基因（小鼠）
# -------------------------
adata_all.var["mt"]=adata_all.var_names.str.startswith("mt-")

# -------------------------
# 2. 标记核糖体基因
# -------------------------
adata_all.var["ribo"]=adata_all.var_names.str.startswith(("Rps","Rpl"))

# -------------------------
# 3. 标记血红蛋白基因
# -------------------------
# 血红蛋白基因一般以 Hb 开头（小鼠基因名首字母大写）
adata_all.var["hb"]=adata_all.var_names.str.match("^Hb(?!p)")

# -------------------------
# 4. 计算 QC 指标
# -------------------------
sc.pp.calculate_qc_metrics(
adata_all,
qc_vars=["mt","ribo","hb"],
inplace=True,
log1p=True
)

# -------------------------
# 5. 绘制 QC 小提琴图
# -------------------------
sc.pl.violin(
adata_all,
["n_genes_by_counts","total_counts","pct_counts_mt"],
jitter=0.4,
multi_panel=True,
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtFqODzbiaG4HlOaziabrK8Biaz0bnbAn5icQvswH4ngzK9BRGmy5oh95x0w/640?wx_fmt=png&from=appmsg)
```
# 绘制散点图，查看每个细胞的总 counts vs 检测到的基因数，颜色表示线粒体基因占比
sc.pl.scatter(
adata_all,# 使用合并后的 AnnData 对象
x="total_counts",# X 轴：每个细胞的总 counts
y="n_genes_by_counts",# Y 轴：每个细胞检测到的基因数
color="pct_counts_mt",# 颜色：线粒体基因占比
size=20,# 点大小，可根据需要调整
alpha=0.6# 点透明度，方便观察密集区域
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtEDibJjtMqqQcTibsdxNGXYO1icD6Yib95AiaU57Q7NXWRltdpYQWQTXnlCg/640?wx_fmt=png&from=appmsg)
```
# 按阈值过滤细胞
adata_all=adata_all[
(adata_all.obs["n_genes_by_counts"]>500)&
(adata_all.obs["n_genes_by_counts"]<5000)&
(adata_all.obs["pct_counts_mt"]<10)&
(adata_all.obs["pct_counts_hb"]<1),
:
].copy()

# 过滤低表达基因
sc.pp.filter_genes(adata_all,min_cells=3)

# 查看过滤后的数据
print(adata_all)

# 或者快速看 QC 指标分布
adata_all.obs[[
"n_genes_by_counts",
"total_counts",
"pct_counts_mt",
"pct_counts_hb"
]].describe()
```
```
AnnData object with n_obs × n_vars = 19528 × 23055
    obs: 'sample', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb'
    var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'n_cells'
```
[/code]
```

| n_genes_by_counts| total_counts| pct_counts_mt| pct_counts_hb
---|---|---|---|---
count| 19528.000000| 19528.000000| 19528.000000| 19528.000000
mean| 2770.776782| 9566.176758| 3.016162| 0.011421
std| 1122.763284| 6204.673828| 1.889050| 0.025680
min| 501.000000| 629.000000| 0.000000| 0.000000
25%| 1947.000000| 4803.500000| 1.801323| 0.000000
50%| 2732.000000| 8161.500000| 2.606931| 0.000000
75%| 3645.000000| 13318.250000| 3.803340| 0.014522
max| 4999.000000| 50992.000000| 9.996863| 0.899888
[code]
# 保存原始 count
# 将原始表达矩阵复制到 layers["counts"]，以便后续保留原始数据
adata_all.layers["counts"]=adata_all.X.copy()
```

# 3、细胞分群
```
# -------------------------
# 1. 数据标准化
# 将每个细胞的总 counts 归一化到 1e4
sc.pp.normalize_total(adata_all,target_sum=1e4)

# -------------------------
# 2. 对数化
# 对归一化后的数据做 log1p 转换（log(1 + x)），减小表达量差异
sc.pp.log1p(adata_all)

# -------------------------
# 3. 计算高变基因（Highly Variable Genes, HVGs）
# 选出对下游分析最有信息量的基因
# batch_key="sample" 表示在每个样本内计算高变基因，再整合
sc.pp.highly_variable_genes(adata_all,n_top_genes=1500,batch_key="sample")

# 可视化高变基因
sc.pl.highly_variable_genes(adata_all)

# -------------------------
# 4. PCA 降维
# 用高变基因进行主成分分析（Principal Component Analysis）
sc.tl.pca(adata_all)

# 可视化 PCA 的方差贡献率
sc.pl.pca_variance_ratio(adata_all,n_pcs=50,log=True)

# -------------------------
# 5. 绘制 PCA 散点图
# 可视化前四个主成分，并用样本和线粒体占比染色
sc.pl.pca(
adata_all,
color=["sample","sample","pct_counts_mt","pct_counts_mt"],
dimensions=[(0,1),(2,3),(0,1),(2,3)],
ncols=2,
size=2,
)
```

WARNING: adata.X seems to be already log-transformed.

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtyicNSx089SNWOiaWJKunNg9IibaxBhbhUqcSEPoyaa8OX4fSgrY6g7icWQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtWFesNRapHZ3RqSETKo8QpPXwtTDVz7hY7CZrhJCyAkdgEVtmxFk6Pw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtMeOS9A2NCiaWVUVtqcU7GAbpDRib2p92sHibXz9thQMGlrxfzgaRibGMzA/640?wx_fmt=png&from=appmsg)
```
# 1. 构建最近邻图（基于 PCA 空间）
sc.pp.neighbors(
adata_all,
n_neighbors=15,# 常用默认值
n_pcs=30# 使用前 30 个 PCA
)

# -------------------------
# 2. 计算 UMAP 嵌入
sc.tl.umap(adata_all)

# -------------------------
# 3. 可视化：按 sample 展示细胞来源
sc.pl.umap(
adata_all,
color="sample",
size=2
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibttQd8HV0ZX5GXI3TEj22u3jDqOnSIQb3DOvhHnmkWc0SwzHvn9tVfbg/640?wx_fmt=png&from=appmsg)
```
# 仅指定使用 PCA 多少个主成分
sc.tl.tsne(
adata_all,
n_pcs=30,# 使用前 30 个 PCA
use_rep='X_pca'# 明确告诉 Scanpy 使用 PCA 结果
)

# 可视化 t-SNE
sc.pl.tsne(
adata_all,
color=['sample'],
size=2
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtHQFMJlM8kK2LnesPN1gL0w7xn1pYB7rfmEFiaE1qlrZDT2YyohemGxw/640?wx_fmt=png&from=appmsg)
```
# -------------------------
# 1. Leiden 聚类
sc.tl.leiden(
adata_all,
resolution=0.2,# 常用起始分辨率
flavor="igraph",
n_iterations=2
)

# -------------------------
# 2. 在 UMAP 上可视化聚类结果
sc.pl.umap(
adata_all,
color="leiden",
size=2
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibto8X04YYp6hiaa0QXxAz5TCSCkdBV5cr6hAZibiaLeCtdMCGHBaEezeInQ/640?wx_fmt=png&from=appmsg)
```
# -------------------------
# 1. Leiden 聚类（保持不变）
sc.tl.leiden(
adata_all,
resolution=0.2,# 可调整分辨率
flavor="igraph",
n_iterations=2
)

# -------------------------
# 2. 计算 t-SNE
sc.tl.tsne(
adata_all,
n_pcs=30,# 使用前30个主成分，可根据数据调整
random_state=42
)

# -------------------------
# 3. 在 t-SNE 上可视化聚类结果
sc.pl.tsne(
adata_all,
color="leiden",
size=20# 点的大小，可根据需要调整
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibt6mKt9xicKl3att9CeWE9sgic2HZMbqZm4CO3bLiaxJSdFMQRPOfV4bMgA/640?wx_fmt=png&from=appmsg)

# 4、批次效应
```
import harmonypy as hm
import scanpy as sc

# -------------------------
# 1. 使用 PCA 作为输入
# 可以直接使用 adata_all.obsm['X_pca']，但保证只用高变基因
pca_data=adata_all.obsm['X_pca']

# -------------------------
# 2. 运行 Harmony 校正
# batch_key='sample' 表示按照样本批次进行校正
ho=hm.run_harmony(
pca_data,# PCA 数据
adata_all.obs,# 细胞元数据
'sample'# 批次列
)

# -------------------------
# 3. 将校正后的 PCA 结果放回 AnnData
adata_all.obsm['X_pca_harmony']=ho.Z_corr.T

# -------------------------
# 4. 用校正后的 PCA 进行邻接图计算和 UMAP
sc.pp.neighbors(adata_all,use_rep='X_pca_harmony')
sc.tl.umap(adata_all)

# -------------------------
# 5. 可视化校正后的 UMAP
sc.pl.umap(adata_all,color=["sample","leiden"],size=2)
```
```
2025-12-23 22:13:41,970 - harmonypy - INFO - Computing initial centroids with sklearn.KMeans...
2025-12-23 22:13:52,347 - harmonypy - INFO - sklearn.KMeans initialization complete.
2025-12-23 22:13:52,454 - harmonypy - INFO - Iteration 1 of 10
2025-12-23 22:13:56,043 - harmonypy - INFO - Iteration 2 of 10
2025-12-23 22:13:59,340 - harmonypy - INFO - Iteration 3 of 10
2025-12-23 22:14:02,581 - harmonypy - INFO - Iteration 4 of 10
2025-12-23 22:14:05,801 - harmonypy - INFO - Iteration 5 of 10
2025-12-23 22:14:09,044 - harmonypy - INFO - Converged after 5 iterations
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtFcBWDJzrMUOaHP6mptaMpGkqg7cRV2BibMEzR66BAQ3ia8Yic2fqtEw3A/640?wx_fmt=png&from=appmsg)
```
# -------------------------
#  计算 t-SNE（基于校正后的 PCA）
# 注意：新版本 Scanpy t-SNE 只接受 n_pcs, use_rep
sc.tl.tsne(
adata_all,
use_rep='X_pca_harmony',# 使用 Harmony 校正后的 PCA
n_pcs=30# 使用前 30 个主成分
)

# -------------------------
# 6. 可视化 t-SNE
# 按样本染色
sc.pl.tsne(adata_all,color=['sample','leiden'],size=2)

# -------------------------
# 可选：保存 t-SNE 结果
# adata_all.obsm['X_tsne'] 已经包含 t-SNE 坐标
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtoG4Sict8xdYlSicCIY3ATfQ0vIqGMlfge1Pa04ic1D7Hp552FTjzrqOmg/640?wx_fmt=png&from=appmsg)
```
adata_all
```
```
AnnData object with n_obs × n_vars = 19528 × 23055
    obs: 'sample', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb', 'leiden'
    var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'n_cells', 'highly_variable', 'means', 'dispersions', 'dispersions_norm', 'highly_variable_nbatches', 'highly_variable_intersection'
    uns: 'log1p', 'hvg', 'pca', 'sample_colors', 'neighbors', 'umap', 'tsne', 'leiden', 'leiden_colors'
    obsm: 'X_pca', 'X_umap', 'X_tsne', 'X_pca_harmony'
    varm: 'PCs'
    layers: 'counts'
    obsp: 'distances', 'connectivities'
```
```
# 保存整个 AnnData 对象
adata_all.write("adata_all_harmony.h5ad")
```

# 5、细胞注释
```
adata_all = sc.read_h5ad("adata_all_harmony.h5ad")
```
```python
import scanpy as sc
import matplotlib.pyplot as plt

# -------------------------
# 1. 使用你自己的 AnnData
adata = adata_all
print(adata)

# -------------------------
# 2. 计算每个 Leiden 聚类的差异基因
sc.tl.rank_genes_groups(adata, groupby="leiden", method="wilcoxon")
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)
```
```
AnnData object with n_obs × n_vars = 19528 × 23055
    obs: 'sample', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb', 'leiden'
    var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'n_cells', 'highly_variable', 'means', 'dispersions', 'dispersions_norm', 'highly_variable_nbatches', 'highly_variable_intersection'
    uns: 'hvg', 'leiden', 'leiden_colors', 'log1p', 'neighbors', 'pca', 'rank_genes_groups', 'sample_colors', 'tsne', 'umap'
    obsm: 'X_pca', 'X_pca_harmony', 'X_tsne', 'X_umap'
    varm: 'PCs'
    layers: 'counts'
    obsp: 'connectivities', 'distances'
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtOCWS3N8GMian5u7ywHvkMBUWnibPkcjAnutvA39sX8PTvRWicP18XlOFw/640?wx_fmt=png&from=appmsg)
```
# 3. 提取每个 cluster 的 top5 基因
all_markers = sc.get.rank_genes_groups_df(adata, group=None)
top5_per_group = all_markers.groupby("group").head(5)["names"].unique()
print("Top 5 marker genes per cluster:", top5_per_group)

# Dotplot 展示 top5 基因
sc.pl.dotplot(
    adata,
    var_names=top5_per_group,
    groupby="leiden",
    title="Top 5 marker genes per cluster",
    standard_scale="var",
    show=False
)
plt.tight_layout()
plt.show()
```
```
/tmp/ipykernel_1261103/323136341.py:3: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
  top5_per_group = all_markers.groupby("group").head(5)["names"].unique()
```
```
Top 5 marker genes per cluster: ['Scp2' 'Alb' 'Fabp1' 'Hmgcs2' 'Mat1a' 'Tox' 'Nkg7' 'Ccl5' 'Cd8a' 'Cd3g'
 'Skap1' 'Itk' 'Gm2682' 'Bcl11b' 'Trbc2' 'Tcf4' 'Bst2' 'Irf8' 'Lair1'
 'Siglech' 'Ifi30' 'H2-Ab1' 'H2-Eb1' 'Ccdc88a' 'Grk3' 'Lyz2' 'Pid1' 'Cybb'
 'Apobec1' 'Zeb2' 'C1qa' 'C1qc' 'C1qb' 'Lgmn' 'Apoe' 'Srgn' 'S100a8'
 'Clec4d' 'S100a9' 'Tyrobp' 'Ptprb' 'Selenop' 'Adgrf5' 'Igfbp7' 'F8'
 'Ebf1' 'Cd79a' 'Igkc' 'Bank1' 'Ighm' 'Gsn' 'Gstm1' 'Egfr' 'Efna5'
 'Sema3c' 'Magi1' 'Ptprk' 'Sorbs2' 'Pkhd1' 'Bicc1' 'Cst3' 'Flt3' 'Tbc1d8'
 'Batf3' 'Klrk1' 'Klrb1c' 'Klre1' 'Il2rb' 'Clnk']
```
```
/tmp/ipykernel_1261103/323136341.py:15: UserWarning: This figure includes Axes that are not compatible with tight_layout, so results might be incorrect.
  plt.tight_layout()
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibt8jzKrIibObcF5KfAicwiblbcibzuG4YK8PqGNctha4XqLHbbk3ypRR0waw/640?wx_fmt=png&from=appmsg)

```
markers_df = sc.get.rank_genes_groups_df(
    adata_all,
    group=None
)

# 查看每个 cluster 的前10个 marker
cluster_top_markers = (
    markers_df
    .groupby("group")
    .head(10)
)

cluster_top_markers

cluster_top_markers.to_csv(
    "Leiden_cluster_top10_markers.csv",
    index=False
)
```
```
/tmp/ipykernel_1261103/4242299856.py:9: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
  .groupby("group")
```
```
# 假设原 cluster 存在 adata_all.obs['leiden']
new_cluster_names = [
    "Hepatocytes",              # 0
    "CD8 T cells",              # 1
    "CD4 T cells",              # 2
    "pDC",                      # 3
    "cDC2",                     # 4
    "Monocytes",                # 5
    "Kupffer cells",            # 6
    "Neutrophils",              # 7
    "LSECs",                    # 8
    "B cells",                  # 9
    "Hepatic stellate cells",   # 10
    "Cholangiocytes",           # 11
    "cDC1",                     # 12
    "NK cells"                  # 13
]

# 将原始 cluster 转为整数类型
adata_all.obs['leiden'] = adata_all.obs['leiden'].astype(int)

# 创建新列
adata_all.obs['cell_type'] = adata_all.obs['leiden'].map(lambda x: new_cluster_names[x])

# 查看标注结果
adata_all.obs[['leiden','cell_type']].head(10)
```

| leiden| cell_type
---|---|---
AAACCCAAGGACGCAT-1| 0| Hepatocytes
AAACCCAAGGCTAAAT-1| 1| CD8 T cells
AAACCCAAGTTCCAGT-1| 3| pDC
AAACCCACAGCACGAA-1| 4| cDC2
AAACCCACATGTAACC-1| 7| Neutrophils
AAACCCAGTCGTCATA-1| 2| CD4 T cells
AAACCCAGTGCTTATG-1| 2| CD4 T cells
AAACGAAAGAACCGCA-1| 8| LSECs
AAACGAACACACCAGC-1| 8| LSECs
AAACGAACACGTCATA-1| 6| Kupffer cells

```
# 肝脏主要细胞类型经典 marker
marker_dict = {
    "Hepatocytes": ["Alb", "Fabp1", "Aldob"],
    "CD8 T cells": ["Cd3d", "Cd8a", "Ccl5"],
    "CD4 T cells": ["Cd3d", "Cd4", "Lck"],
    "pDC": ["Siglech", "Tcf4", "Irf8"],
    "cDC2": ["H2-Aa", "H2-Ab1", "Cd74"],
    "Monocytes": ["Lyz2", "Csf1r", "Ctss"],
    "Kupffer cells": ["C1qa", "C1qb", "C1qc"],
    "Neutrophils": ["S100a8", "S100a9", "Ly6g"],
    "LSECs": ["Kdr", "Ptprb", "Aqp1"],
    "B cells": ["Cd79a", "Ms4a1", "Igkc"],
    "Hepatic stellate cells": ["Col1a1", "Col3a1", "Des"],
    "Cholangiocytes": ["Krt19", "Pkhd1", "Onecut2"],
    "cDC1": ["Flt3", "Batf3", "Irf8"],
    "NK cells": ["Nkg7", "Klrk1", "Ncr1"]
}
```
```
import scanpy assc
import matplotlib.py plotasplt
# 展平成一个 marker 列表
marker_genes = sum(marker_dict.values(), [])
sc.pl.dotplot(
    adata_all,
    var_names=marker_dict,
    groupby="cell_type",
    standard_scale="var",
    dot_max=0.7,
    title="Marker gene expression across annotated cell types",
    show=False
)
plt.tight_layout()
plt.savefig("Dotplot_marker_celltype.png", dpi=300)
plt.show()
```
```
/tmp/ipykernel_1261103/2425698508.py:17: UserWarning: This figure includes Axes that are not compatible with tight_layout, so results might be incorrect.
  plt.tight_layout()
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtGN3icjXQhsKSlVvSI65hLsPDLoEUCRYLJIfrCyYCvbhX7qSqmeIGoaA/640?wx_fmt=png&from=appmsg)
```python
import scanpy as sc
import matplotlib.pyplot as plt

# -------------------------
# 1. 确认 cell_type 已经标注
print(adata_all.obs[['leiden', 'cell_type']].head())

# -------------------------
# 2. UMAP 可视化
sc.pl.umap(
    adata_all,
    color='cell_type',
    size=30,             # 点大小，可根据细胞数量调整
    palette='tab20',     # 使用分类调色板
    legend_loc='on data' # 将图例直接显示在图上
)

# -------------------------
# 3. t-SNE 可视化
# 注意：确保已经计算过 t-SNE 并保存在 adata_all.obsm['X_tsne']
sc.pl.tsne(
    adata_all,
    color='cell_type',
    size=30,
    palette='tab20',
    legend_loc='on data'
)

# -------------------------
# 4. 可选：保存图片
plt.savefig('./UMAP_cell_type.png', dpi=300)
plt.savefig('./tSNE_cell_type.png', dpi=300)
```
```
                    leiden    cell_type
```
```
AAACCCAAGGACGCAT-1       0  Hepatocytes
AAACCCAAGGCTAAAT-1       1  CD8 T cells
AAACCCAAGTTCCAGT-1       3          pDC
AAACCCACAGCACGAA-1       4         cDC2
AAACCCACATGTAACC-1       7  Neutrophils
```

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtemFVcasDQtEtDt3UZkWCNrarwIK7ofib19ibO40ggFMSic5hs3EiaLwy7Q/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtvxsRVxr95m2gpy7qK8WeNtiaMiaMmnkHA2M1Cibic7sWDNxEhChjvwhiadQ/640?wx_fmt=png&from=appmsg)
```
<Figure size 640x480 with 0 Axes>
```
```
# 保存最终整合和注释后的 AnnData 对象
adata.write("GSE270583_adata_annotated_v2.h5ad")
```

**四、演示环境**

一切不给测试文件和分析环境版本的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibtu1C6bia3oGlXnEWITWpsxLTSHtm440N0ibrAqqtFCgFiap8G5bIS9yw1w/640?wx_fmt=png&from=appmsg)

通过网盘分享的文件: https://pan.baidu.com/s/1n9sVVVc7EYW-Yq-h8ad1AQ

提取码: 48vp

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzicGthkGORDBlBDdwW1x3ibt7iavtcGhTqD12bucQnw5Er0ibxV0yQrLEUiaHuQdWARI1kQE2XGnM7y6Q/640?wx_fmt=jpeg)

R语言演示环境([开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>))：
```
sessionInfo()
```
```
## R version 4.4.2 (2024-10-31)
## Platform: x86_64-pc-linux-gnu
## Running under: Ubuntu 20.04.4 LTS
##
## Matrix products: default
## BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3
## LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/liblapack.so.3;  LAPACK version 3.9.0
##
## locale:
##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C
##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8
##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8
##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C
##  [9] LC_ADDRESS=C               LC_TELEPHONE=C
## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C
##
## time zone: Etc/UTC
## tzcode source: system (glibc)
##
## attached base packages:
## [1] stats  graphics   grDevices  utils  datasets    methods   base
##
## other attached packages:
## [1] Seurat_5.2.1       SeuratObject_5.0.2 sp_2.2-0
##
## loaded via a namespace (and not attached):
##   [1] deldir_2.0-4          pbapply_1.7-2     gridExtra_2.3
##   [4] airports_0.1.0         rlang_1.1.5       magrittr_2.0.3
##   [7] RcppAnnoy_0.0.22      spatstat.geom_3.4-1  matrixStats_1.5.0
##  [10] ggridges_0.5.6         compiler_4.4.2      png_0.1-8      ##  [13] vctrs_0.6.5          reshape2_1.4.4    stringr_1.5.1
##  [16] pkgconfig_2.0.3        fastmap_1.2.0      labeling_0.4.3
##  [19] promises_1.3.2         rmarkdown_2.29     tzdb_0.4.0
##  [22] openintro_2.5.0        purrr_1.0.2        xfun_0.50
##  [25] cachem_1.1.0           jsonlite_1.8.9      goftest_1.2-3
##  [28] later_1.4.1          spatstat.utils_3.1-4   irlba_2.3.5.1
##  [31] parallel_4.4.2         cluster_2.1.8      R6_2.5.1       ##  [34] ica_1.0-3        spatstat.data_3.1-6    stringi_1.8.4       ##  [37] bslib_0.9.0     RColorBrewer_1.1-3     reticulate_1.43.0.9001
##  [40] spatstat.univar_3.1-3  parallelly_1.42.0      lmtest_0.9-40
##  [43] jquerylib_0.1.4      scattermore_1.2        Rcpp_1.0.14    ##  [46] knitr_1.49        tensor_1.5       future.apply_1.11.3
##  [49] zoo_1.8-12         cherryblossom_0.1.0    readr_2.1.5
##  [52] sctransform_0.4.1    httpuv_1.6.15        Matrix_1.7-2
##  [55] splines_4.4.2      igraph_2.1.4        tidyselect_1.2.1
##  [58] abind_1.4-8       rstudioapi_0.17.1    yaml_2.3.10
##  [61] spatstat.random_3.4-1 spatstat.explore_3.4-3 codetools_0.2-20
##  [64] miniUI_0.1.1.1       listenv_0.9.1      lattice_0.22-6
##  [67] tibble_3.2.1        plyr_1.8.9         withr_3.0.2
##  [70] shiny_1.10.0        ROCR_1.0-11        evaluate_1.0.3
##  [73] Rtsne_0.17         future_1.34.0       fastDummies_1.7.5
##  [76] survival_3.8-3    polyclip_1.10-7      fitdistrplus_1.2-2
##  [79] pillar_1.10.1     KernSmooth_2.23-26    plotly_4.10.4
##  [82] generics_0.1.3     RcppHNSW_0.6.0       hms_1.1.3
##  [85] ggplot2_3.5.1     munsell_0.5.1      scales_1.3.0
##  [88] globals_0.16.3     xtable_1.8-4      glue_1.8.0
##  [91] lazyeval_0.2.2     tools_4.4.2       data.table_1.16.4
##  [94] RSpectra_0.16-2     RANN_2.6.2      dotCall64_1.2
##  [97] cowplot_1.1.3     grid_4.4.2        tidyr_1.3.1
## [100] colorspace_2.1-1     nlme_3.1-168     patchwork_1.3.0
## [103] usdata_0.3.1       cli_3.6.3     spatstat.sparse_3.1-0
## [106] spam_2.11-1     viridisLite_0.4.2  dplyr_1.1.4
## [109] uwot_0.2.2     gtable_0.3.6      sass_0.4.9
## [112] digest_0.6.37       progressr_0.15.1   ggrepel_0.9.6
## [115] htmlwidgets_1.6.4  farver_2.1.2       htmltools_0.5.8.1
## [118] lifecycle_1.0.4      httr_1.4.7         mime_0.12
## [121] MASS_7.3-64sessionInfo()
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
