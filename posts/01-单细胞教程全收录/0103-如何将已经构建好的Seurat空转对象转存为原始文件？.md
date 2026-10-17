---
title: "如何将已经构建好的Seurat空转对象转存为原始文件？"
date: 2024-02-21
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508133&idx=1&sn=297b8fb9cc8f33a1d19167dba1104e97&chksm=9b3cd9f5ac4b50e36df53e3e18bb2990d9635d88a725f1e54fc5eb5967ac9f0934b79cbb8b34#rd
albums: ["单细胞教程全收录", "空间转录组", "粉丝来稿"]
---

# 如何将已经构建好的Seurat空转对象转存为原始文件？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508133&idx=1&sn=297b8fb9cc8f33a1d19167dba1104e97&chksm=9b3cd9f5ac4b50e36df53e3e18bb2990d9635d88a725f1e54fc5eb5967ac9f0934b79cbb8b34#rd
> 合集：单细胞教程全收录 / 空间转录组 / 粉丝来稿

空转的分析生态还没有单细胞那么成熟，经常需要跨软件、跨平台完成数据分析，这里我们以10X Visium为例演示演示如何将R语言中的Seurat空转对象转变为本地输出，并用Python中Scanpy进行读取检查。当然，Scanpy可以直接以sc.read_visium的形式读入数据，这里我们假设了一种只能拿到rds文件的情况。

本教程测试文件：https://pan.baidu.com/s/1uFSVCH86JZ8RAHR7kb30ig?pwd=j9nv

提取码：j9nv

更多空转教程可见：[空间转录组学习手册合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505088&idx=1&sn=9f60dca1b21f5ba8c32d09595a512134&chksm=9b3cad90ac4b2486820dd335d997d2a96b77beb6ad463b1df6a2f307e47ebe8d7de3304ebf7c&scene=21#wechat_redirect>)一、Seurat中读取并转存10X Visium数据(在R中完成)

  *   *   *   *   *   *   *   *   *   *   *   *   *

```r
### 读取数据 #### 加载R包library(DropletUtils)library(tibble)library(Seurat)library(jsonlite)library(stringr)
# 读入10X Visium数据data <- Load10X_Spatial('~/data/test/10X_data')
# 保存为RDSsaveRDS(data,file = '~/data/test/RDS/data.rds')
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
### 保存为scanpy可以读取的格式 ###
# 从 data 对象中提取空间图像的缩放因子。Visium 数据通常包括高分辨率（hires）和低分辨率（lowres）的图像数据。这里，low_factor 和 hi_factor 分别存储了低分辨率和高分辨率图像的缩放因子。这些因子在分析空间转录组数据时非常重要，因为它们帮助调整图像大小以匹配转录组数据。low_factor <- data@images$slice1@scale.factors$lowreshi_factor <- data@images$slice1@scale.factors$hires
dir.create('~/data/test/Export_data/spatial')
# 获取并保存图像images <- GetImage(data, mode = "raw")images <- magick::image_read(images) image_height <- magick::image_info(images)$heightEBImage::writeImage(magick::as_EBImage(images), file = '~/data/test/Export_data/spatial/tissue_lowres_image.png')images <- images %>% magick::image_resize(paste0('x',round(image_height/low_factor*hi_factor)))EBImage::writeImage(magick::as_EBImage(images), file = '~/data/test/Export_data/spatial/tissue_hires_image.png')
# 获取并保存坐标信息coordinates <- data@images$slice1@coordinatescoordinates <- rownames_to_column(coordinates)# coordinates[,1] <- str_split(coordinates[,1],'_',simplify = TRUE)[,2] #可以用这行修改barcodes前缀write.table(coordinates,file = '~/data/test/Export_data/spatial/tissue_positions_list.csv',quote = F,row.names = F,col.names = F,sep=',')
# 整理并保存缩放因子scale_factors <- data.frame(spot_diameter_fullres=data@images$slice1@scale.factors$spot,                            tissue_hires_scalef=data@images$slice1@scale.factors$hires,                            fiducial_diameter_fullres=data@images$slice1@scale.factors$fiducial,                            tissue_lowres_scalef=data@images$slice1@scale.factors$lowres)
jsondata <- toJSON(scale_factors)cat(str_remove_all(jsondata, '[\\[\\]]'), file = '~/data/test/Export_data/spatial/scalefactors_json.json', fill = FALSE, labels = NULL, append = FALSE)
# 保存矩阵write10xCounts(x = data@assays$Spatial$counts,               #barcodes = str_split(colnames(P2_noninf@assays$Spatial$counts),'_',simplify = TRUE)[,2] ,                # 如果barcodes已经被修改过带有前缀了，如果不想要前缀可以用上一行去掉，不过记得改coordinates里面的barcodes               gene.id = rownames(data@assays$Spatial$counts),               gene.symbol = rownames(data@assays$Spatial$counts),               gene.type = "Gene Expression",               overwrite = FALSE,               type = 'HDF5',               genome = "CRCh38",               version = "3",               chemistry = "Single Cell 3' v1",               library.ids = "slice1",               path = '~/data/test/Export_data/filtered_feature_bc_matrix.h5')
```

二、在Scanpy中查看是否能够读入(在[Python](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&chksm=9b3cb9c1ac4b30d7bbd44057b181f87541f5904d24f903494ae557e768ae00c208c1b68b45c7&scene=21#wechat_redirect>)中完成)

  *   *   *   *   *   *   *

```
### 导入数据 ###import scanpy as scimport pandas as pdimport matplotlib.pyplot as pltimport seaborn as snsdata_export = sc.read_visium('/home/zbt/data/test/Export_data',library_id='slice1')data_10x = sc.read_visium('/home/zbt/data/test/10X_data')
```

两个数据均可正常导入:

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxwtL210ID1Q7S1RsnC1B9djzOJvYIs4zh1IGogGyfSuqpbbiaglliayGWS6fG5ud63SNgFBqjUBmSg/640?wx_fmt=png&from=appmsg)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
### 做点预处理看看是否能够正常分析 ###data_export.var_names_make_unique()data_export.var["mt"] = data_export.var_names.str.startswith("MT-")sc.pp.calculate_qc_metrics(data_export, qc_vars=["mt"], inplace=True)
data_10x.var_names_make_unique()data_10x.var["mt"] = data_10x.var_names.str.startswith("MT-")sc.pp.calculate_qc_metrics(data_10x, qc_vars=["mt"], inplace=True)
plt.rcParams["figure.figsize"] = (8, 8)sc.pl.spatial(data_export, img_key="hires", color=["total_counts", "n_genes_by_counts"])
plt.rcParams["figure.figsize"] = (8, 8)sc.pl.spatial(data_10x, img_key="hires", color=["total_counts", "n_genes_by_counts"])
```

可以看出与原始数据相比几乎无差异：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxwtL210ID1Q7S1RsnC1B9daIdH1TiaPG1xenh4v2neib9yB8mW2d7pf53fshibjQzMB57ibjhZbNxmXg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxwtL210ID1Q7S1RsnC1B9dfqmusD0NB434AzictticzjOLxUlEYtibTSP401l6wwavTJK8zhsRpT96g/640?wx_fmt=png&from=appmsg)

此方法唯一的缺陷是是Seurat对象中仅存储lowres图像，所以只能利用rds文件图像强制拉伸到hires分辨率。hires图像会略微模糊。如果原文提供了hires图像则可以直接替换进spatial文件夹。

更多空转教程可参考：[空间转录组学习手册合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505088&idx=1&sn=9f60dca1b21f5ba8c32d09595a512134&chksm=9b3cad90ac4b2486820dd335d997d2a96b77beb6ad463b1df6a2f307e47ebe8d7de3304ebf7c&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=1&sn=d9517a0803ad75cb7be430806834e7b8&chksm=9b3ca7bdac4b2eaba1ad01ed04ab1fbcbafcf4f6ddfe9e4f76ed9229707f545fe7d9c9ffd6ae&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
