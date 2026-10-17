---
title: "scRNA拟时序分析三大Python包： palantir、PAGA、RNAvelocity"
date: 2026-08-25
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541302&idx=3&sn=32ea0f4c0202797348286c7595afd43e&chksm=9b3c5b66ac4bd2701e2b07a3ca1cff16bbcea43fa1c654d97b4d3140ee143e97c74b28ffc70b#rd
albums: ["单细胞教程全收录"]
---

# scRNA拟时序分析三大Python包： palantir、PAGA、RNAvelocity

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541302&idx=3&sn=32ea0f4c0202797348286c7595afd43e&chksm=9b3c5b66ac4bd2701e2b07a3ca1cff16bbcea43fa1c654d97b4d3140ee143e97c74b28ffc70b#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

写在前面

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)现在所有订阅都能够从官网获取啦：[承包你未来40年的单细胞学习资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540976&idx=1&sn=178859bc9916bd7ccd9a5303aa10ceda&scene=21#wechat_redirect>)

[拟时序](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527850&idx=1&sn=f4e2ca5e2e5e71eeaf132375bb8270eb&scene=21#wechat_redirect>)（Pseudotime）分析是一种在[单细胞](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)转录组学中常用的方法，它通过对细胞在特定生物过程中的[转录组](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2959853503529910274#wechat_redirect>)数据进行排序，推断其发展或变化的时间顺序。尽管单细胞数据通常是静态的（在一个时间点采集），拟时序分析通过基因表达的变化模式来重建细胞的发育轨迹或动态过程，从而模拟细胞随时间推移的变化，揭示细胞在不同状态下的演变路径和关键转折点。

## 拟时序分析作用

（1）推断细胞的发育阶段：通过分析基因表达变化，将处于不同分化阶段的细胞排序，模拟出一个拟时间轴。

（2）识别关键的基因调控事件：通过比较不同拟时间阶段的细胞，识别在特定转折点上调或下调的基因，找出与细胞分化或功能转换相关的关键分子。

（3）推断细胞状态转换：分析细胞从一种状态向另一种状态过渡的动态变化，尤其在干细胞分化或疾病模型中应用广泛。

## 不同拟时序软件的比较

## 该学习手册参考了一篇发表在《Nature Biotechnology》杂志上面的文献，来详细的了解一下不同拟时序软件的异同点。文献的标题为《A comparison of single-cell trajectory inference methods》（链接https://www.nature.com/articles/s41587-019-0071-9）。文章分别从拓扑结构、分支确定、细胞位置以及对于基因的处理能力四个主要方面，对45种拟时序分析软件进行了系统性的评估。该文章我们在B站也同步有详细的视频讲解，感兴趣的同学也可以直接复制链接在浏览器查看：

https://www.bilibili.com/video/BV1S44y1b76Z

本学习手册将针对 palantir、PAGA、[RNAvelocity](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528458&idx=1&sn=900357283922571c6294435be409a2f3&scene=21#wechat_redirect>)三款工具，分别从文献深度解读与实操流程讲解两方面进行剖析。

学习手册图片集锦：![](../../images/2e8fbf164c2ebd54.webp)

优惠订阅资料或参与课程请联系客服微信[Biomamba_zhushou]**更多生信教程可见：[ 为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)**
**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)
![](../../images/f08cdfe212eb6283.png)

所见即所得

![](../../images/2cc9da4d1e6321da.png)![](../../images/007e970626afa0b7.png)

以html格式提供学习手册，可在浏览器中打开并翻阅学习：‍

![](../../images/52168a3508efb916.gif)

教程目录：零、欢迎关注一、前言1.1 定义1.2 拟时序分析作用1.3 不同拟时序软件的比较1.3.1 总体评价结果1.3.2 准确性1.3.3 可扩展性1.3.4 稳定性1.3.5 软件、文档和手稿方面的可用性二、准备工作2.1 环境准备 2.2 库准备三、palantir3.1 文献解读 3.1.1 摘要 3.1.2 结果 3.1.3 小结3.2 数据读入3.3 预处理3.4 可视化 3.5 运行Palantir 3.5.1 获取细胞坐标 3.5.2 定义分化起点和终点 3.5.3 拟时间推断3.6 下游分析 3.6.1 细胞分化概率统计 3.6.2 展示不同细胞分支 3.6.3 基因随轨迹变化趋势分析 3.6.4 基因表达模式聚类3.7 联合scanpy分析 3.7.1 表达模式聚类结合富集分析 (1) 差异基因鉴定 (2) 表达模式聚类 (3) 富集分析 3.7.2 降维图 3.7.3 小提琴图 3.7.4 细胞比例展示 3.7.5 密度分布图四、PAGA4.1 文献解读 4.1.1 摘要 4.1.2 结果 4.1.3 小结4.2 pbmc3k数据实操 4.2.1 数据读入 4.2.2 数据预处理 4.2.3 运行PAGA 4.2.4 可视化 4.2.5 重新定义发育起点4.3 人骨髓数据实操 4.3.1 数据读入 4.3.2 数据预处理 4.3.3 运行PAGA 4.3.4 可视化 4.3.5 重新定义发育起点4.4 联合scanpy分析 4.4.1 拟时间降维图 4.4.2 小提琴图 4.4.3 细胞比例展示 4.4.4 密度分布图4.5 小鼠髓系数据实操五、RNAvelocity5.1 文献解读 5.1.1 摘要 5.1.2 结果 5.1.3 小结5.2 数据下载 5.2.1 bam文件 5.2.2 repeatmask文件 5.2.3 gtf文件5.3 loom文件准备5.4 RNA速率分析 5.4.1 导入loom文件 5.4.2 导入细胞降维坐标和分群文件 5.4.3 轨迹推断 (1) 数据过滤和归一化 (2) 计算表达均值和方差 (3) 计算RNA速率 (4) 构建RNA速率图 (5) 在UMAP降维空间可视RNA速率方向 (6) 在UMAP降维空间以流场形式展示RNA速率方向5.5 下游数据挖掘 5.5.1 关注基因可视化 5.5.2 鉴定重要基因 5.5.3 细胞周期分析 5.5.4 RNA速率的置信度 5.5.5 潜在时间(latent time)分析 5.5.6 Cluster-specific top-likelihood 基因六、软件版本七、单细胞教程全收录八、欢迎致谢

**
**

文末下载链接中包含以下内容：

![](../../images/2628760b4e349c09.png) 测试文件，总大小18.55GB![](../../images/7d247e6c6ef19f87.png)

![](../../images/399758fa7d6941c2.png)

往期推送

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

Biomamba 生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)

2025年我们零差评完成订阅任务（[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)），2026已更新订阅内容：

[单细胞Figure1的常见图表(Python版)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534718&idx=1&sn=f1492239574ad489be9a1aa0c84af87a&scene=21#wechat_redirect>)

[告别R依赖！一文搞定Python单细胞基础分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534702&idx=1&sn=f1531163f8f620b59cf63dfaa1c03e67&scene=21#wechat_redirect>)

[风靡一时的scTenifoldKnk单细胞虚拟基因敲除,准不准?](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535112&idx=1&sn=95a6b88cd49fb2bbb7aa091a00e09e2c&scene=21#wechat_redirect>)

**![](../../images/bc4a928a4947108c.webp)****
**

![](../../images/7d247e6c6ef19f87.png)

解锁前需阅读：**[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)**![图片](../../images/eab31beb8c0e41d2.png)

订阅链接请添加客服微信领取

![图片](../../images/8b04fd62fd8f3d51.png)![](../../images/007e970626afa0b7.png)

![图片](../../images/e43581b4f5118aad.webp)

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)
