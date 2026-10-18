---
title: "fastXXX、rapidXXX系列加速你的单细胞数据分析"
date: 2026-05-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538079&idx=2&sn=9ecd53f31d266d0d3db9db396f8275e2&chksm=9b3c2ccfac4ba5d9fbb82a568a35b2728da5d4cde10ddaa6570f54574c29078421aeb5fb630b#rd
albums: ["单细胞教程全收录"]
---

# fastXXX、rapidXXX系列加速你的单细胞数据分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538079&idx=2&sn=9ecd53f31d266d0d3db9db396f8275e2&chksm=9b3c2ccfac4ba5d9fbb82a568a35b2728da5d4cde10ddaa6570f54574c29078421aeb5fb630b#rd
> 合集：单细胞教程全收录

![](../../images/f08cdfe212eb6283.png)

写在前面

![](../../images/2cc9da4d1e6321da.png)![](../../images/007e970626afa0b7.png)

最近发现很多带有FastXXX、RapidXXX字符的单细胞分析工具上架，顾名思义，这类工具能够以不同数量级的速度完成原有的单细胞分析。例如FastCCC，利用包含1600万个细胞、450种细胞类型的数据作为参考模板快速获取[细胞通讯](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=1&sn=c3eb2d3abad1952b3b7fa88099c607b7&scene=21#wechat_redirect>)的计算结果。

在本次学习手册，我们也整理了多款可显著提升分析效率的工具，包括：fastCCC（[细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)加速）、fastCNV（[拷贝数变异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535878&idx=2&sn=6d3315ba0d9d3f3246665f11f30adfb9&scene=21#wechat_redirect>)推断加速）、rapid single-cell（[GPU加速](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)单细胞流程计算）

欢迎大家在评论区留言补充更多高效工具。

学习手册部分图片集锦：![](../../images/28f8b862eb822da8.webp)优惠订阅资料或参与课程请联系客服微信[Biomamba_zhushou]![](../../images/fe8ecb8594a1f419.webp)**更多生信教程可见：[为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)****-Biomamba**![](../../images/7d247e6c6ef19f87.png)![](../../images/f08cdfe212eb6283.png)

三款高效加速工具介绍

![](../../images/2cc9da4d1e6321da.png)![](../../images/007e970626afa0b7.png)

1\. fastCCC

用途：[细胞通讯](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)加速

文章链接： https://www.nature.com/articles/s41467-025-66272-z

代码仓库：https://github.com/Svvord/FastCCC

特点介绍：FastCCC的速度至少是CPDB V5和V4、[CellChat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)、SingleCellSignalR、[ICELLNET](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)、[NicheNet](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)、[CellCall](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=3&sn=e44b787fa7a653fb8d98588d88cf26e0&scene=21#wechat_redirect>)这些工具中任意一种的十倍。计算时调用的内存也是所有算法中最小的，并能够支持100万个细胞的数据分析(文中作者最多测试到200w细胞)。除了召回率和FPR外，FastCCC在精度、准确性、特异性、平衡准确率和Jaccard指数、F1分数、马修相关系数均优于其它方法。通过快速傅里叶变换（FFT）利用卷积技术，FastCCC推导出C-S零分布的解析解，实现了p值的可扩展解析计算，而无需计算密集的置换。FastCCC引入了模块化的C-S计算框架，通过配体与受体表达水平之间的代数运算捕捉相互作用强度。它还容纳配体和受体的多亚基蛋白复合物，解释了不同亚基的独特相互作用强度。

![](../../images/c6ca81fe0ba0a3b4.webp)

2\. fastCNV

用途：[拷贝数变异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536094&idx=2&sn=a00c0ccd8868781ddbc8ba0eaf874ac8&scene=21#wechat_redirect>)推断加速

文章链接：https://www.biorxiv.org/content/10.1101/2025.10.22.683855v1.full.pdf

代码仓库：https://github.com/must-bioinfo/fastCNV/

特点介绍：基于R语言的fastCNV能够加速空间转录组学、scRNA-seq数据预测拷贝数变异（CNVs），有助于区分恶性细胞与非恶性细胞，并对肿瘤细胞的克隆结构进行表征。fastCNV在样本之间汇集二倍体参考序列，并在每个样本内将读数较少的相似斑点或细胞合并为元斑点或细胞。它会自动构建克隆性树，并且比其他方法运行速度快数倍，同时占用内存更少。通过[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&scene=21#wechat_redirect>)数据的输入，fastCNV能够直接返回每个细胞是上皮、肿瘤、还是其它细胞的注释。为了评估fastCNV的准确性，作者使用了117 个同时拥有scRNA-seq和WES数据的癌症细胞系进行测试。fastCNV所识别的CNV与从WES数据计算出的CNV高度相关（中位相关性超过 0.75）。fastCNV首次实现了对Visium HD空间转录组学技术所得CNV的分析。FastCNV相较于现有的R方法在速度、内存使用、灵敏度和准确性等方面具有显著优势。

3\. rapid single-cell

用途：[GPU加速](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)单细胞流程计算

文章链接：https://arxiv.org/pdf/2603.02402

代码仓库：https://rapids-singlecell.readthedocs.io/en/latest/tutorials.html

特点介绍：这是由scverse(就是那个开发了[scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533070&idx=1&sn=eb762b5b475695f418438d6628d8012f&scene=21#wechat_redirect>)、[anndata](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528513&idx=1&sn=1ff1b8bee321f8f5bcac425ce96dc6ff&scene=21#wechat_redirect>)、[squidpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532641&idx=1&sn=c8422ab7c1cd70751fb3109a84cb64ea&scene=21#wechat_redirect>)这些神包组织)开发的工具，通过CuPy内核处理SciPy数据，可以借助NVIDIA-GPU(NVIDIA的官网也可以看到这个项目:https://github.com/NVIDIA-AI-Blueprints/single-cell-analysis-blueprint)加速数百倍的提升单细胞数据计算过程，可以无缝接入scanpy分析anndata数据。值得一提的是，通过RAPIDS内存管理系统，可以在GPU显存不足时把数据暂存到内存当中，并且在GPU充足时支持跨GPU的分布式计算，这意味着rapid single-cell支持数[百万单细胞数据](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534670&idx=1&sn=7178b77f1efe4ca253f90b9121231204&scene=21#wechat_redirect>)的计算(试试上作者测试了100million的数据分析，也只需200min)。在预处理、标准化、高变基因计算、降维(PCA、UMAP、t-SNE)、临近图谱构建、leiden分群等操作时可以提升约120倍计算速度。rapid single-cell准还能支持空间自相关指标、通路及转录因子活性推断、批次矫正、干扰距离计算等操作。只要细胞数超过5w，rapid single-cell准能大大的提升你的计算效率。

![](../../images/faed385df26c56bc.webp)

以上是三款工具的基本信息，具体实操见我们手册~，领取资料联系客服[Biomamba_zhushou]:![](../../images/fe8ecb8594a1f419.webp)
![](../../images/7d247e6c6ef19f87.png)![](../../images/f08cdfe212eb6283.png)

所见即所得

![](../../images/2cc9da4d1e6321da.png)![](../../images/007e970626afa0b7.png)

以html格式提供学习手册，可在浏览器中打开并翻阅学习：‍

![](../../images/2e6398108a8fd465.webp)

学习手册目录：

零、欢迎关注

一、写在前面

二、fastCCC

2.1 安装

2.2 测试数据

2.3 主函数演示

2.4 输出文件

2.5 结果可视化

三、fastCNV

3.1 安装

3.2 测试数据

3.3 运行主函数

3.3.1 [单个样本](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&scene=21#wechat_redirect>)

3.3.2 [多个样本](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&scene=21#wechat_redirect>)运行

3.4 CNV频率

3.5 CNV分群

3.6 进化树

四、rapid single-cell

4.1 安装

4.2 rapid single-cell流程

准备工作

文末下载链接中包含以下内容：

![](../../images/23458d27b7f9b032.webp)测试文件，总大小9.30GB![](../../images/7d247e6c6ef19f87.png)

![](../../images/399758fa7d6941c2.png)

往期推送

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

Biomamba 生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)

2025年我们零差评完成订阅任务（[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)），2026已更新订阅内容：

[单细胞Figure1的常见图表(Python版)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534718&idx=1&sn=f1492239574ad489be9a1aa0c84af87a&scene=21#wechat_redirect>)

[告别R依赖！一文搞定Python单细胞基础分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534702&idx=1&sn=f1531163f8f620b59cf63dfaa1c03e67&scene=21#wechat_redirect>)

[风靡一时的scTenifoldKnk单细胞虚拟基因敲除,准不准?](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535112&idx=1&sn=95a6b88cd49fb2bbb7aa091a00e09e2c&scene=21#wechat_redirect>)

[scRNA拟时序分析三大Python包： palantir、PAGA、RNAvelocity](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535114&idx=1&sn=95b6364b67d7ae9f03ba8455863ddabe&scene=21#wechat_redirect>)

[正刊都在用的AI驱动蛋白质从头设计流程：RFdiffusion+ProteinMPNN+AlphaFold3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)

[CellphoneDB搞定细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536366&idx=1&sn=c3eb2d3abad1952b3b7fa88099c607b7&scene=21#wechat_redirect>)

[scRNA-seq肿瘤细胞药物敏感性预测分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536705&idx=1&sn=7fbfeba5dee45f6c3311bd31082a428c&scene=21#wechat_redirect>)

[fastXXX、rapidXXX系列加速你的单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536940&idx=1&sn=57eea9f64dfeff9231977ab5028c3dcd&scene=21#wechat_redirect>)

[转录因子、基因共表达网络分析手册：pySCENIC在脑、黑色素瘤中的应用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537055&idx=1&sn=170371b86b42d47373bf7f0500031f19&scene=21#wechat_redirect>)

[让你的scRNA数据变得更干净~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537531&idx=1&sn=e5f08c08b352287ddfda069a20019afb&scene=21#wechat_redirect>)

[保姆级视频教程| 空间转录组分析手册(基于Seurat)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537631&idx=1&sn=b702b29384fd4f4878cc0b4d0fcf51e7&scene=21#wechat_redirect>)

[拷贝数变异分析的python实现及R语言对比](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537733&idx=1&sn=b938e687d0acf2d906139314e137b903&scene=21#wechat_redirect>)

[Ai驱动结合蛋白设计：Bindcraft全流程教学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537769&idx=1&sn=5dbfe76b35fd2f7593e55bff48c6fa73&scene=21#wechat_redirect>)

[千万级细胞预训练，如何用AI搞定单细胞注释与质控](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537859&idx=1&sn=cd3f1fff64f2147afb6222d65db4917f&scene=21#wechat_redirect>)

文件夹中已经更新的教程有：

**![](../../images/bc4a928a4947108c.webp)**

持续更新中~

![](../../images/7d247e6c6ef19f87.png)

解锁前需阅读：**[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)**![图片](../../images/eab31beb8c0e41d2.png)

学习手册领取：

![图片](../../images/8b04fd62fd8f3d51.png)![](../../images/007e970626afa0b7.png)

本推送教程、测试文件下载链接：

https://pan.baidu.com/s/100GgFRIP51MPo7bakcYPuA

提取码请联系客服微信获取：

![](../../images/fe8ecb8594a1f419.webp)![](../../images/7d247e6c6ef19f87.png)
