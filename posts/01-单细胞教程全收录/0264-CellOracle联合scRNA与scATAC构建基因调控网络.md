---
title: "CellOracle联合scRNA与scATAC构建基因调控网络"
date: 2026-02-28
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535250&idx=1&sn=a2839b6cb9d3618dff3f20570c48cf0f&chksm=9b3c33c2ac4bbad4df20b6cb9e2f966ec71d320fe6358fdb104d465ce1de30bcf469e5d47105#rd
albums: ["单细胞教程全收录"]
---

# CellOracle联合scRNA与scATAC构建基因调控网络

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535250&idx=1&sn=a2839b6cb9d3618dff3f20570c48cf0f&chksm=9b3c33c2ac4bbad4df20b6cb9e2f966ec71d320fe6358fdb104d465ce1de30bcf469e5d47105#rd
> 合集：单细胞教程全收录

**一、写在前面**

细胞身份由复杂的基因表达调控决定，其核心调控形式表现为基因调控网络。研究人员基于[单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534762&idx=2&sn=60d56d856036cf523f1dfcf7ea284d18&scene=21#wechat_redirect>)多组学数据推断的基因调控网络，在计算机模拟转录因子扰动分析，仅用未受干扰的野生型数据模拟细胞身份的相关变化。作者将基于机器学习的CellOracle方法应用于小鼠和人类造血细胞、斑马鱼胚胎发生等体系，正确建模了因转录因子扰动引起的表型变化。简单来说，CellOracle可用于分析转录因子对细胞身份的调控，且能提供发育和分化的机制性见解。此前我们介绍过多种[一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&payreadticket=HMQmfIA8dLyMln3Qn22G6WUefAwTYEdiHwqwAfFmmN0n4Yv5kKZlwYlDcI61cKp4eU2Eusg&scene=21#wechat_redirect>)，此次介绍的`CellOracle`的主要功能为利用[scATAC](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&scene=21#wechat_redirect>)构建调控网络、进行[基因调控网络](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)（Gene Regulatory Network，GRN）构建与分析。
目前oracle支持的物种与基因组版本有：
Human: ['hg38', 'hg19']，Mouse: ['mm39', 'mm10', 'mm9']，S.cerevisiae: ["sacCer2", "sacCer3"]，Zebrafish: ["danRer7", "danRer10", "danRer11"]，Xenopus tropicalis: ["xenTro2", "xenTro3"]，Xenopus laevis: ["Xenopus_laevis_v10.1"]，Rat: ["rn4", "rn5", "rn6"]，Drosophila: ["dm3", "dm6"]，C.elegans: ["ce6", "ce10"]，Arabidopsis: ["TAIR10"]，Chicken: ["galGal4", "galGal5", "galGal6"]，Guinea Pig: ["Cavpor3.0"]，Pig: ["Sscrofa11.1"]
本教程基于Linux环境的jupyter演示，计算资源不足的同学可参考：

[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21&token=1904068475&lang=zh_CN#wechat_redirect>)

[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21&token=1904068475&lang=zh_CN&poc_token=HF-eN2mj01zsfxe_I4r8D5pfZx80xO2AVYSB6qtT#wechat_redirect>)

[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)访问链接：https://biomamba.xiyoucloud.net/欢迎联系客服微信[Biomamba_zhushou]获取帮助
如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21#wechat_redirect>)教学、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)、自测数据个性化分析辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、实操流程**

如果你对下面的教程比较迷茫，那么你可以先行学习编程教程：

#

[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)

[生信Linux及服务器使用技巧](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2980604042328702978#wechat_redirect>)

[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&scene=21#wechat_redirect>)

1\. 安装

参考CellOracle的推荐方式，考虑到大家未必都有[有root权限的共享服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532785&idx=2&sn=c364ab8365a845cd709251c026075e0a&scene=21#wechat_redirect>)，推荐通过[conda](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530994&idx=2&sn=3f3bdf2d06532c0b0ab8c9a477b8332c&scene=21#wechat_redirect>)和pip来安装。

  *   *   *   *   *   *   *   *

```
# 这个代码框在终端运行conda install python=3.10mamba install -c conda-forge numpy=1.26.4 cython scipy h5py pandas=1.5.3pip install setuptools wheelpip install velocyto>=0.17--no-cache-dirpip install celloracle --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/pip install matplotlib-inline==0.1.7--no-cache-dirpip install fa2-modified -i https://mirrors.aliyun.com/pypi/simple/
```

# **2. 单细胞数据处理流程**

这里其实就是单细胞数据的基础分析流程，演示数据来源于一篇《Cell》(http://doi.org/10.1016/j.cell.2015.11.013)，不理解的同学可以看一下我们此前的基础教程：[scRNA-Seq学习手册Python版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&scene=21#wechat_redirect>)[82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)

  *   *   *   *   *   *   *

```
# 导包：import celloracleimport osimport matplotlib.pyplot as pltimport numpy as npimport pandas as pdimport scanpy as sc
```
```
2.1 预处理、分群
```

  *   *

```
# 加载scanpy的内置数据集：adata = sc.datasets.paul15()
```
```
... storing 'paul15_clusters' as categorical
```

  *   *   *   *

```
# 如果你加载失败，我们也给你下载好了adata.write_h5ad('data/paul15/paul15.h5ad')adata = sc.read_h5ad('data/paul15/paul15.h5ad')adata
```
```
AnnData object with n_obs × n_vars = 2730 × 3451
    obs: 'paul15_clusters'
```
```
    uns: 'iroot'
```

标准的单细胞过滤、标准化、对数化、降维过程，不理解的同学可以参考我们此前的教程[82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)。原始矩阵和对数化后的矩阵在后续celloracle的运用中都用得到。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
### 处理过程 ###sc.pp.filter_genes(adata, min_counts=1)# 过滤count数不超过1的基因sc.pp.normalize_per_cell(adata, key_n_counts='n_counts_all')# 对UMI counts进行标准化filter_result = sc.pp.filter_genes_dispersion(adata.X,                                              flavor='cell_ranger',                                              n_top_genes=2000,                                              log=False)# 计算top2000的高变基因adata = adata[:, filter_result.gene_subset]# 只保留高变基因用于后续分析sc.pp.normalize_per_cell(adata)# 对过滤后的数据重新标准化 adata.raw = adata# 做备份切片adata.layers["raw_count"] = adata.raw.X.copy()# 做矩阵备份切片，后续celloracle的输入用得到
sc.pp.log1p(adata)# 对标准化后的矩阵取对数sc.pp.scale(adata)# 缩放，用于PCA分析sc.tl.pca(adata, svd_solver='arpack')# PCA分析sc.pp.neighbors(adata, n_neighbors=4, n_pcs=20)# 计算临近矩阵sc.tl.diffmap(adata)# 计算扩散映射sc.pp.neighbors(adata, n_neighbors=10, use_rep='X_diffmap')# 利用扩散映射计算临近图sc.tl.louvain(adata, resolution=0.8)# 进行louvain聚类分群
```

**2.2 注释**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
### marker 可视化 ### # 先导入必要包import scanpy as scimport matplotlib.pyplot as plt
# 启用matplotlib inline后端（核心：让图在Jupyter中显示）%matplotlib inline# 可选：提高图的分辨率，显示更清晰%config InlineBackend.figure_format = 'retina'# 可选：设置全局绘图参数plt.rcParams["savefig.dpi"] = 300markers = {"Erythroids":["Gata1", "Klf1", "Gypa", "Hba-a2"],           "Megakaryocytes":["Itga2b", "Pbx1", "Sdpr", "Vwf"],            "Granulocytes":["Elane", "Cebpe", "Ctsg", "Mpo", "Gfi1"],            "Monocytes":["Irf8", "Csf1r", "Ctsg", "Mpo"],            "Mast_cells":["Cma1", "Gzmb", "Kit"],            "Basophils":["Mcpt8", "Prss34"]            }
sc.pl.dotplot(adata,markers,groupby='louvain')
```

![No description has been provided for this image](../../images/71ca340d25898201.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
### 细胞注释重命名 #### louvain数字编号：cluster_list = adata.obs.louvain.unique()cluster_list
# 细胞名称与cluster数字对应的字典：annotation = {"MEP":[5],              "Erythroids": [15, 10, 16, 9, 8, 14, 19, 3, 12, 18],              "Megakaryocytes":[17, 22],                "GMP":[11, 1],              "late_GMP" :[0],                 "Granulocytes":[7, 13, 4],              "Monocytes":[6, 2],              "DC":[21],              "Lymphoid":[20]}
# 改变字典格式：annotation_rev = {}for i in cluster_list:    for k in annotation:        if int(i) in annotation[k]:            annotation_rev[i] = k
# 最终的字典annotation_rev
# 重命名：adata.obs["cell_type"] = [annotation_rev[i] for i in adata.obs.louvain]sc.tl.umap(adata)sc.pl.umap(adata,legend_loc = 'on data',color = 'cell_type')
```
```
... storing 'cell_type' as categorical
```

![No description has been provided for this image](../../images/3f58f5e3437e20f2.webp)

## **2.3 PAGA拟时序**

PAGA拟时序分析，不理解这一块内容的同学可参考：[轨迹分析专题](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)

  *   *   *

```
sc.tl.paga(adata, groups='louvain')# 进行PAGA计算plt.rcParams["figure.figsize"] = [6, 4.5]# 设置绘图参数sc.pl.paga(adata)# PAGA结果可视化
```

![No description has been provided for this image](../../images/ccece55b6dcc6af6.webp)

  *   *

```
# 力导向图计算：sc.tl.draw_graph(adata, init_pos='paga', random_state=123)# 确保你拥有fa2-modified，否则这一行无法运行
```

  *   *

```
# 力导向图可视化：sc.pl.draw_graph(adata, color='louvain', legend_loc='on data')# 跟大家熟悉的monocle轨迹图类似，把有时序关系的细胞在降维中进行排序
```

![No description has been provided for this image](../../images/c13ac867da179813.webp)

  *

```
adata.write_h5ad('./data/adata_for_GRN.h5ad')
```

# **3\. 利用scATAC数据获取TF与motif调控关系**

#  依赖scATAC数据，celloracle能够做到扫描peaks构建TF与其结合motif，预测其调控关系分值，对scATAC分析不了解的同学可以参考： [scATAC分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&payreadticket=HD_abkHKUCDLeu-EOu5eLnzDcF7NruyJQbGRgSA4J-MVNy69fcNU3BFW8-OLHEzWSBX0tCE&scene=21#wechat_redirect>)

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
### 导包 ###import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as snsquitimport os, sys, shutil, importlib, globfrom tqdm.notebook import tqdm
import celloracle as cofrom celloracle import motif_analysis as mafrom celloracle.utility import save_as_pickled_objectco.__version__
```
```
'0.20.0'
```

  *   *   *   *   *   *

```
### 绘图参数设置 ###%config InlineBackend.figure_format = 'retina'%matplotlib inline
plt.rcParams['figure.figsize'] = (15,7)plt.rcParams["savefig.dpi"] = 600
```

cellorlce的运行需要依赖genomepy提供的参考基因组，这里的演示数据是小鼠，我们检查一下mm10是否能够正常调用：

  *   *   *   *

```
# 获取mm10的安装状态genome_installation = ma.is_genome_installed(ref_genome="mm10",                                             genomes_dir=None)print(ref_genome, "installation: ", genome_installation)
```
```
mm10 installation:  True
```

  *   *

```
# celloracle支持的其它参考基因组可在这个列表中查看ma.SUPPORTED_REF_GENOME
```

![](../../images/00b4bb12f41c3bce.png)

如果在上面的判断中你发现自己没有安装对应基因组，也可以通过这种方式安装：

  *   *   *   *   *   *   *

```
if not genome_installation:    import genomepy    genomepy.install_genome(name='mm10', # 物种名称，对应上面ref_genome一列                            provider="UCSC", # 数据提供机构，对应上面provider一列                            genomes_dir=None)else:    print(ref_genome, "is installed.")
```
```
mm10 is installed.
```

  *   *

```
# 下载测试scATAC数据的peaks文件!wget https://raw.githubusercontent.com/morris-lab/CellOracle/master/docs/demo_data/processed_peak_file.csv -O data/processed_peak_file.csv
```

![](../../images/eee77d0b2233954c.png)

  *   *   *   *   *

```
# 读取peaks信息peaks = pd.read_csv("data/processed_peak_file.csv", index_col=0)peaks.head()# 除了行名，这个文件一共两列，第一列是peak的名称，格式为染色体编号_起始位点_终止位点# 第二列是这个peaks对应的基因名
```

![](../../images/516fa19c643892ac.png)

  *   *

```
# 检查peaks信息与基因组是否一一对应peaks = ma.check_peak_format(peaks, ref_genome, genomes_dir=None)
```
```
Peaks before filtering:  15779
Peaks with invalid chr_name:  0
Peaks with invalid length:  2
Peaks after filtering:  15777
```

  *   *   *   *

```
# 实例化TFinfo对象，将peaks按照基因组信息转换为DNA序列tfi = ma.TFinfo(peak_data_frame=peaks[1:1000].copy(), # 我们取前1000个peaks做测试，完整的数据可能要运行数个小时，速度取决于你的计算设备                ref_genome=ref_genome,                genomes_dir=None)
```

  *   *   *   *   *   *   *

```
%%time# 扫描DNA序列，寻找TF结合motifs并构建GRNtfi.scan(fpr=0.02,          motifs=None,  # 选择none时会默认读取数据库motif信息         verbose=True,# 是否展示进度条         batch_size=500# 批次大小)
```
```
No motif data entered. Loading default motifs for your species ...
 Default motif for vertebrate: gimme.vertebrate.v5.0.
 For more information, please see https://gimmemotifs.readthedocs.io/en/master/overview.html
Initiating scanner...
2026-01-19 15:45:06,540 - DEBUG - using background: genome mm10 with size 200
Calculating FPR-based threshold. This step may take substantial time when you load a new ref-genome. It will be done quicker on the second time.
Motif scan started .. It may take long time.
Scanning:   0%|          | 0/905 [00:00<?, ? sequences/s]
CPU times: user 1min 33s, sys: 936 ms, total: 1min 34s
Wall time: 1min 34s
```

  *   *   *   *

```
# 把TFI实例保存为hdf5文件tfi.to_hdf5(file_path="data/test1.celloracle.tfinfo")# 查看GRNA包含的信息tfi.scanned_df.head(
```

![](../../images/d2e60c11f730f2cd.png)

  *   *   *   *   *   *   *   *

```
# 重置过滤参数tfi.reset_filtering()
# 过滤掉score低于10的序列和motif对tfi.filter_motifs_by_score(threshold=10)
# 格式化过滤后的结果tfi.make_TFinfo_dataframe_and_dictionary(verbose=True)
```
```
Filtering finished: 892798 -> 169196
1. Converting scanned results into one-hot encoded dataframe.
0%|          | 0/904 [00:00<?, ?it/s]
2. Converting results into dictionaries.
0%|          | 0/963 [00:00<?, ?it/s]
0%|          | 0/1092 [00:00<?, ?it/s]
```

  *   *   *   *   *

```
# 将GRN数据转换为数据框df = tfi.to_dataframe()df.head()# 将这个数据框保存到本地：df.to_parquet("base_GRN_dataframe.parquet")# 这就是下文调控网络里分析中用到的GRN_base
```

![](../../images/f51d5bbbb5e6fa74.webp)
```
5 rows × 1094 columns
```

# **4\. 基因调控网络模型构建**

CellOracle的最主要功能就是构建基因调控网络(Gene Regulatory Network，GRN)，为完成GRN构建，这一章中需要用到上面刚生成的两个数据：1、adata注释数据 2、输出的TFI。CellOracle 可构建基于簇的基因调控网络模型，即可供大家研究细胞类型特异性的GRN。

## **4.1 数据准备**

  *   *   *   *   *   *   *   *   *   *   *

```
### 导包 ###import osimport sys
import matplotlib.pyplot as pltimport numpy as npimport pandas as pdimport scanpy as scimport seaborn as snsimport celloracle as coco.__version__
```
```
'0.20.0'
```

  *   *   *   *   *   *

```
### 设置绘图参数 ###%config InlineBackend.figure_format = 'retina'# 提升图表分辨率%matplotlib inline
plt.rcParams['figure.figsize'] = [6, 4.5]plt.rcParams["savefig.dpi"] = 300# 保存图片的DPI
```

  *   *

```
save_folder = "figures"# 保存图片的文件夹os.makedirs(save_folder, exist_ok=True)
```

  *   *   *

```
# 读取此前注释好的adata文件：adata = sc.read_h5ad('./data/adata_for_GRN.h5ad')adata
```
```
AnnData object with n_obs × n_vars = 2730 × 1999
    obs: 'paul15_clusters', 'n_counts_all', 'n_counts', 'louvain', 'cell_type'
    var: 'n_counts', 'mean', 'std'
    uns: 'cell_type_colors', 'diffmap_evals', 'draw_graph', 'iroot', 'log1p', 'louvain', 'louvain_colors', 'louvain_sizes', 'neighbors', 'paga', 'pca', 'umap'
    obsm: 'X_diffmap', 'X_draw_graph_fa', 'X_draw_graph_fr', 'X_pca', 'X_umap'
    varm: 'PCs'
    layers: 'raw_count'
    obsp: 'connectivities', 'distances'
```

  *   *   *

```
# 查看基因与细胞数print(f"Cell number is :{adata.shape[0]}")print(f"Gene number is :{adata.shape[1]}")
```
```
Cell number is :2730
Gene number is :1999
```

  *   *   *   *   *   *   *

```
# 如果你的细胞数量很多，可以如此downsamplen_cells_downsample = 2500 # 例如这里我们downsample到2500个细胞if adata.shape[0] > n_cells_downsample:    sc.pp.subsample(adata, n_obs=n_cells_downsample,                     random_state=123)# 设置随机数# 检查downsample结果：print(f"Cell number is :{adata.shape[0]}")
```
```
Cell number is :2500
```

  *   *   *   *   *

```
# 读取小鼠数据集的TFI信息base_GRN = co.data.load_mouse_scATAC_atlas_base_GRN()
# 检查数据：base_GRN.head()# 其实就是我们上文保存的df.to_parquet("base_GRN_dataframe.parquet")
```

![](../../images/b101444e3e344773.webp)

5 rows × 1095 columns

## **4.2 构建Oracle对象**

  *   *   *   *   *   *   *   *   *   *   *

```
# 实例化Oracle对象oracle = co.Oracle()# 检查anndataprint("Metadata columns :", list(adata.obs.columns))print("Dimensional reduction: ", list(adata.obsm.keys()))# 这里输入数据为原始count，我们在上面做过"raw_count"切片：adata.X = adata.layers["raw_count"].copy()# 利用anndata构建oracle对象：oracle.import_anndata_as_raw_count(adata=adata,                                   cluster_column_name="cell_type",                                   embedding_name="X_diffmap")
```
```
Metadata columns : ['paul15_clusters', 'n_counts_all', 'n_counts', 'louvain', 'cell_type']
Dimensional reduction:  ['X_diffmap', 'X_draw_graph_fa', 'X_draw_graph_fr', 'X_pca', 'X_umap']
WARNING: adata.X seems to be already log-transformed.
```

  *   *   *   *   *

```
# 向oracle对象中导入TFIoracle.import_TF_data(TF_info_matrix=base_GRN)
# 如果你的信息是一个字典，可以如是导入：# oracle.import_TF_data(TFdict=TFinfo_dictionary)
```

  *   *

```
# 下载TF与靶基因的对应关系!wget https://raw.githubusercontent.com/morris-lab/CellOracle/master/docs/demo_data/TF_data_in_Paul15.csv -O ./data/paul15/TF_data_in_Paul15.csv
```
```
--2026-01-19 14:19:48--  https://raw.githubusercontent.com/morris-lab/CellOracle/master/docs/demo_data/TF_data_in_Paul15.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1771 (1.7K) [text/plain]
Saving to: ‘./data/paul15/TF_data_in_Paul15.csv’

./data/paul15/TF_da 100%[===================>]   1.73K  3.39KB/s    in 0.5s

2026-01-19 14:19:49 (3.39 KB/s) - ‘./data/paul15/TF_data_in_Paul15.csv’ saved [1771/1771]
```

  *   *   *

```
# 读取TF与靶基因的对应关系：Paul_15_data = pd.read_csv("./data/paul15/TF_data_in_Paul15.csv")Paul_15_data
```

![](../../images/b59dec6399a1f0e5.png)

  *   *   *   *   *   *   *   *

```
### 制作一个key为TF，填充值为TG名的字典 ###TF_to_TG_dictionary = {}# 定义空字典
for TF, TGs in zip(Paul_15_data.TF, Paul_15_data.Target_genes):    # 将TG以逗号为分隔符变为列表    TG_list = TGs.replace(" ", "").split(",")    # 把TG列表存储到对应TF的key中    TF_to_TG_dictionary[TF] = TG_list
```

  *   *   *   *   *   *   *   *   *   *   *

```
### 制作一个key为TF，填充值为TG名的字典 ###TF_to_TG_dictionary = {}# 定义空字典
for TF, TGs in zip(Paul_15_data.TF, Paul_15_data.Target_genes):    # 将TG以逗号为分隔符变为列表    TG_list = TGs.replace(" ", "").split(",")    # 把TG列表存储到对应TF的key中    TF_to_TG_dictionary[TF] = TG_list
# 将这个字典转换为一一对应的形式TG_to_TF_dictionary = co.utility.inverse_dictionary(TF_to_TG_dictionary)
```
```
  0%|          | 0/178 [00:00<?, ?it/s]
```

  *   *

```
# 将字典信息添加到oracle对象中oracle.addTFinfo_dictionary(TG_to_TF_dictionary)
```

## 4.3 PCA分析与插补

  *   *   *   *   *   *   *   *   *   *   *

```
### PCA分析 ###oracle.perform_PCA()# 执行PCA
# 可视化，选择PCA的最佳维度plt.plot(np.cumsum(oracle.pca.explained_variance_ratio_)[:100])# 通过累计方差解释率的二阶差分 + 阈值筛选找到 “变异贡献的拐点”n_comps = np.where(np.diff(np.diff(np.cumsum(oracle.pca.explained_variance_ratio_))>0.002))[0][0]plt.axvline(n_comps, c="k")plt.show()print(n_comps)n_comps = min(n_comps, 50)
```
[/code]
```
  *   *

[code]
n_cell = oracle.adata.shape[0]print(f"cell number is :{n_cell}")
```
```
cell number is :2730
```

  *   *

```
k = int(0.025*n_cell)print(f"Auto-selected k is :{k}")
```
```
Auto-selected k is :68
```

  *   *   *   *   *   *   *

```
# 利用KNN插补方法对缺失值进行填充：oracle.knn_imputation(n_pca_dims=n_comps, # PCA主成分                      k=k, # 插补的核心近邻数量                      balanced=True, # 开启平衡采样                      b_sight=k*8,# 临近搜索的候选范围                      b_maxl=k*4, # 临近搜索的最大迭代                      n_jobs=4)# 并行计算数量
```

  *   *   *   *

```
# 保存oracle对象：oracle.to_hdf5("./data/paul15/Paul_15_data.celloracle.oracle")# 后续可以如此加载回来：# oracle = co.load_hdf5("Paul_15_data.celloracle.oracle")
```

## 4.4 GRN计算

`get_links`函数能够获取推断的GRN信息与对应的metadata。后续的网络分析会以links对象为基础。

  *   *   *   *   *   *

```
%%time# 按照细胞类型进行links计算：links = oracle.get_links(cluster_name_for_GRN_unit="cell_type",                          alpha=10,                         verbose_level=10)# 这个步骤不能支持GPU加速，运行的时间非常长，做好心理准备。
```
```
 0%|          | 0/9 [00:00<?, ?it/s]
```
```
Inferring GRN for DC...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for Erythroids...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for GMP...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for Granulocytes...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for Lymphoid...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for MEP...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for Megakaryocytes...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for Monocytes...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
Inferring GRN for late_GMP...
```
```
  0%|          | 0/1849 [00:00<?, ?it/s]
```
```
CPU times: user 23min 16s, sys: 37.9 s, total: 23min 54s
Wall time: 29min 8s
```

  *   *

```
#links对象包含以下信息：links.links_dict.keys()
```
```
dict_keys(['DC', 'Erythroids', 'GMP', 'Granulocytes', 'Lymphoid', 'MEP', 'Megakaryocytes', 'Monocytes', 'late_GMP'])
```

  *   *

```
# 例如获取DC细胞的GRN列表：links.links_dict["DC"]
```

![](../../images/0628d17af1b770a9.webp)

74429 rows × 6 columns

  *   *

```
# links中具有调色板属性，可以分配各细胞类型的颜色：links.palette
```

  *   *   *   *   *

```
# 设定细胞类型颜色顺序：order = ['DC', 'Erythroids', 'GMP', 'Granulocytes', 'Lymphoid',          'MEP', 'Megakaryocytes', 'Monocytes', 'late_GMP']links.palette = links.palette.loc[order]links.palette
```

![](../../images/61fd38c1efb75448.png)

  *   *

```
# 将links对象保存到本地：links.to_hdf5(file_path="data/links.celloracle.links")
```

  *   *

```
# 按照P值和权重过滤links对象：links.filter_links(p=0.001, weight="coef_abs", threshold_number=2000)
```

  *   *   *   *   *   *   *   *   *   *   *

```
# Network degree收录了每个node的edges数，可以反馈网络的性能plt.rcParams["figure.figsize"] = [9, 4.5]links.plot_degree_distributions(plot_model=True, # 是否输出图片到画布                #save=f"{save_folder}/degree_distribution/",# 保存图片                                               )
# 绘制的图片：#横轴：网络节点的度（Degree）（即每个节点的连接数，对应细胞 / 点位的相互作用数量）；#纵轴：对应度值的频次 / 概率密度（通常会做对数转换，方便观察规律，即每行的右图）；# 双对数坐标（log-log） 下呈现近似线性下降的趋势# 若出现泊松分布（单峰、快速衰减），则模型存在问题，需要调整上面分析流程的参数
```
```
DC
```

![No description has been provided for this image](../../images/f8996e3b3a20038e.webp)

```
Erythroids
```
[/code]
```

[code]
GMP
```

![No description has been provided for this image](../../images/de695857c9094ed4.webp)

```
Granulocytes
```

![No description has been provided for this image](../../images/d038c922de550dee.webp)

```
Lymphoid
```

![No description has been provided for this image](../../images/cb88231531358c3c.webp)

```
MEP
```

![No description has been provided for this image](../../images/bd6e06f449ad3098.webp)

```
Megakaryocytes
```

![No description has been provided for this image](../../images/c23cc1aada43f74c.webp)

```
Monocytes
```

![No description has been provided for this image](../../images/222721c4fe6ed401.webp)

```
late_GMP
```

![No description has been provided for this image](../../images/00edfe727c69b97b.webp)

  *   *   *   *

```
# links.get_score()会有一些R依赖，但是get_network_score()则无需，这一功能在celloracle >= 0.10.0时可以使用links.get_network_score()#links.to_hdf5(file_path="./data/links.celloracle.links")# 将links保存至本地#links = co.load_hdf5(file_path="./data/links.celloracle.links")# 重新读取
```

  *   *

```
# 检查分群情况：links.cluster
```
```
['DC',
 'Erythroids',
 'GMP',
 'Granulocytes',
 'Lymphoid',
 'MEP',
 'Megakaryocytes',
 'Monocytes',
 'late_GMP']
```

  *   *   *   *

```
# 每个指标排名前30的基因links.plot_scores_as_rank(cluster="DC", n_gene=30                         # save=f"{save_folder}/ranked_score",                         )
```

![No description has been provided for this image](../../images/bce4850a8be175a7.png)

![No description has been provided for this image](../../images/a3a25939484b09b0.webp)

![No description has been provided for this image](../../images/593c444799eedf47.png)

![No description has been provided for this image](../../images/0dc98eedfc5cc655.webp)

![No description has been provided for this image](../../images/939a9defc798c3f0.png)

  *   *   *   *   *   *   *

```
# 两种细胞类型之间的基因比较links.plot_score_comparison_2D(value="betweenness_centrality",                               cluster1="DC",                                cluster2="Monocytes",                                percentile=98                               #,save=f"{save_folder}/score_comparison"                              )
```

![No description has been provided for this image](../../images/6b3e39e1652a730a.png)

  *   *   *   *   *   *

```
# 两种细胞类型间的GRN eigenvector_centrality分值比较：links.plot_score_comparison_2D(value="eigenvector_centrality",                               cluster1="DC", cluster2="Monocytes",                                percentile=98                               #,save=f"{save_folder}/score_comparison"                              )
```

![No description has been provided for this image](../../images/1b35f85901f5aa5c.webp)

  *   *   *   *   *   *   *

```
# 两种细胞类型间的GRN degree_centrality_all分值比较：links.plot_score_comparison_2D(value="degree_centrality_all",                               cluster1="DC",                                cluster2="Monocytes",                                percentile=98                               #,save=f"{save_folder}/score_comparison"                              )
```

![No description has been provided for this image](../../images/4773bdd1b0909c0f.webp)

  *   *   *   *

```
# 指定基因的调控网络评分links.plot_score_per_cluster(goi="Gata2"                             #, save=f"{save_folder}/network_score_per_gene/"                            )
```

![No description has been provided for this image](../../images/99a2217e4392f790.webp)

  *

```
links.plot_score_per_cluster(goi="Cebpa")
```

![No description has been provided for this image](../../images/86483b418c71a0e0.webp)

  *   *   *   *

```
# 过滤特定细胞的linkcluster_name = "DC"filtered_links_df = links.filtered_links[cluster_name]filtered_links_df.head()
```

![](../../images/48a6b8b66397d891.png)

  *   *

```
# 按照特定sourece过滤linksfiltered_links_df[filtered_links_df.source == "Cebpa"]
```

![](../../images/da250d05e210b312.png)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 可视化对应细胞类型的性能plt.rcParams["figure.figsize"] = [6, 4.5]plt.subplots_adjust(left=0.15, bottom=0.3)plt.ylim([0,0.040])links.plot_score_discributions(values=["degree_centrality_all"],                                method="boxplot",                                save=f"{save_folder}",                              )

plt.subplots_adjust(left=0.15, bottom=0.3)plt.ylim([0, 0.28])links.plot_score_discributions(values=["eigenvector_centrality"],                               method="boxplot",                               save=f"{save_folder}")

plt.subplots_adjust(left=0.15, bottom=0.3)links.plot_network_entropy_distributions(save=f"{save_folder}")
```
```
degree_centrality_all
```

![No description has been provided for this image](../../images/15d02be6bcc33467.png)

```
eigenvector_centrality
```

![No description has been provided for this image](../../images/517cdffbbfd52c3d.png)![No description has been provided for this image](../../images/e59f361a78b1ef66.webp)

**三、参考**
```
[1]https://morris-lab.github.io/CellOracle.documentation/installation/index.html
```
```
[2]Paul,F.,Arkin,Y.,Giladi,A.,etal.(2015).Transcriptionalheterogeneityandlineagecommitmentinmyeloidprogenitors.Cell,163(7),1663-1677.
```

**四、资料领取**

一切不给测试文件和分析环境版本的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：

![](../../images/65ce9a0aaeece57c.webp)

通过网盘分享的文件: https://pan.baidu.com/s/1lApJi1fRGmwMGrlvZAJGmg

提取码: ij5g

![](../../images/34cbf89a4d2ca903.webp)
![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
