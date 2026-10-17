---
title: "Seurat单细胞标准化：LogNormalize vs SCTransform，到底该怎么选？"
date: 2026-08-17
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541025&idx=1&sn=2d5089001cb486b102cb2dea2de71626&chksm=9b3c5871ac4bd167ed7480e9c8d0452ff8596f71bcd67676119b792692c0ef4199ed7e862cb4#rd
albums: ["单细胞教程全收录"]
---

# Seurat单细胞标准化：LogNormalize vs SCTransform，到底该怎么选？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541025&idx=1&sn=2d5089001cb486b102cb2dea2de71626&chksm=9b3c5871ac4bd167ed7480e9c8d0452ff8596f71bcd67676119b792692c0ef4199ed7e862cb4#rd
> 合集：单细胞教程全收录

**一、写在前面**

[ 单细胞RNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538847&idx=1&sn=2ad605c6d70d4e6ee921fda1798bfd8b&scene=21#wechat_redirect>)数据分析的核心前置步骤就是标准化（Normalization）。先搞懂一个根本问题：我们为什么一定要做标准化？

在单细胞实验中，细胞之间的测序深度（即每个细胞捕获到的 UMI 总数）是最主要的技术干扰因素。即便是完全相同的细胞类型，由于仪器捕获效率波动、细胞裂解效率差异等原因，每个细胞最终检测到的转录本数量也可能相差数倍甚至一个数量级。这种单纯由测序深度带来的数值差异属于技术噪音，会严重掩盖细胞之间真实的生物学差异。即便采用了 UMI 技术去除了 PCR 扩增的重复偏差，细胞间测序深度不均一的问题依然无法避免。

标准化的核心目标：剔除测序深度带来的技术偏差，使得后续分析中基因表达的波动尽可能来源于细胞本身的生物学特征，而非实验技术的干扰。

一套理想的标准化结果应当满足两点：

· 基因表达的方差不受测序深度高低的影响；

· 基因的变异程度与其自身的平均表达丰度脱钩。

这样才能保证后续识别出的[高变基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537219&idx=1&sn=043692316d09cbfa24ececb3eb7166bf&scene=21#wechat_redirect>)（Highly Variable Genes, HVG），是真正能够区分细胞类型的生物学标志物，而非技术波动造成的假阳性。

通俗理解：有的细胞抓到的转录本多、有的抓得少，并不代表细胞本身的基因表达真的差那么多——可能只是实验过程中的随机波动。如果不做标准化就直接分析，算法很容易把”测序深浅不同”误判为”细胞类型不同”。标准化，就是尽量抹平这种”实验运气带来的读数差距”。

目前 [Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&scene=21#wechat_redirect>) 主要提供两套标准化方案：经典的 LogNormalize 流程，以及后来推出的 SCTransform。二者底层原理和适用场景差异巨大，很多研究者在分析时不知如何取舍。本文系统梳理两者的区别，讲清选择逻辑。

建议先学习 [scRNA-Seq学习手册(基于Seurat V5) ](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&scene=21#wechat_redirect>)，快速搞懂Seurat 对象结构，

想知道 ScaleData 与 SCTransform 的详细对比？请阅读[SCTransform与ScaleData](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489675&idx=1&sn=be27cd0a25fe4f2924582bd87a3d86d4&scene=21#wechat_redirect>)。

更多单细胞分析技巧可见：

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwniaDJ0aKcPIOIUheqrSYttfdUwa1Cg3KhD9v1gh34lHFJ2lwM7iab8a6Ijnp2lcDKZDexiaicb7fPdRiau7WXAuO1XTPSxIWllOpKE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540932&idx=2&sn=713686d522279f84f3c2cc2aad7cb1bc&scene=21#wechat_redirect>)

**二、 LogNormalize vs SCTransform**

1、LogNormalize：经典三步走

LogNormalize 是 Seurat 最早提供、也是目前使用最广泛的[标准化流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492295&idx=1&sn=d4e81588c0ac2906849c8bc44d079209&scene=21#wechat_redirect>)，由三个连续步骤组成：

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnicNJUPd9g3hAUUWvAmhZFNZIZg5xKibUIWeapyqDjicUJQlFZxqG5hibSPsGTEDAzaw7URWDiau3YPkDjMlUkfBxLiaJuGZD7a6k9k/640?wx_fmt=png&from=appmsg)

这套流程存在一个核心局限：对数变换 log(y/s × 10000 + 1) 将技术噪声和生物学变异混在一起处理，缺乏对测序深度效应的精细建模——LogNormalize 是全局线性缩放，每个基因共享同一个 scale factor，无基因特异性的离散度参数建模。

🚫 务必避坑：log(CPM + 1)

Seurat 默认 scale.factor = 10000，伪计数 1 是合理量级。但若误用 log(CPM + 1)（scale factor = 1,000,000），在常规 10x 数据（~5000 UMI/细胞）下，等效伪计数仅 0.005，对应过度离散参数 α ≈ 50，远超真实单细胞数据的 α ≈ 0.05，人为放大低表达基因噪音，性能断崖式下降（Ahlmann-Eltze & Huber, 2023）。

2、SCTransform：一步到位的负二项回归

SCTransform 用一个函数替代了传统三步。其本质是一个正则化负二项回归模型（Regularized Negative Binomial GLM）：对每个基因拟合一个负二项广义线性模型（GLM），以 UMI 深度作为自变量，同时回归线粒体比例等协变量。模型的条件皮尔逊残差（Conditional Pearson Residuals）——即”该基因在这个细胞中超出测序深度 + 协变量预期的表达部分”——即为真正的生物学变异。

区别于 LogNormalize 的全局线性缩放，SCT会对每个基因的离散度做正则化平滑估计，而非完全独立拟合，避免低计数基因出现极端离散度估值。

💡 注意负值的不同含义：LogNormalize 的 z-score 和 SCTransform 的皮尔逊残差都会产生负值，但生物学含义完全不同——z-score 负值仅表示”低于该基因平均表达”，皮尔逊残差负值表示”低于模型预期”。二者不可直接对比表达量。

两种方法的核心差异对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkBicw58kuWkEyCibqqhyh11oxQaDDVRcPm8VjiaUbKveaT7r4JoHOXzGlKfC6iaI42MW9icQI6UY3w4CNiafZS0fzSC6jg3OtMxsxrg/640?wx_fmt=png&from=appmsg)

3、代码对比

  *   *   *

```r
merged_obj <- NormalizeData(merged_obj)# 标准化merged_obj <- FindVariableFeatures(merged_obj)# 计算高变基因merged_obj <- ScaleData(merged_obj)# 缩放高变基因
```

  *

```r
merged_obj <- SCTransform(merged_obj)
```

两种方法的代码实现差异直观明了：

从代码可以看出，SCTransform 单个函数一站式完成了传统流程中 NormalizeData、FindVariableFeatures、ScaleData 三步的全部工作。从校正技术噪音的理论表现来看，多项可视化指标（均值-方差曲线、PCA 混杂相关性等）均证实，SCTransform 对细胞测序深度和细胞总 RNA 量差异的校正效果显著优于 LogNormalize：它能均衡高低表达基因的方差，更重视低丰度基因的信号。

4、Nature Methods 2023 基准测试：理论优势 ≠ 实际胜出

以上所有指标——同质 RNA PCA、均值-方差曲线、双峰标记基因可视化——SCTransform 在理论上全面占优。但关键问题是：这些理论指标的提升，能否转化为下游细胞分群、轨迹推断等实际任务的性能提升？

2023 年发表于 Nature Methods 的 “Comparison of transformations for single-cell RNA-seq data”（Ahlmann-Eltze & Huber, 2023）给出了出人意料的答案。论文系统对比了 22 种单细胞标准化方案（除 Log/SCT 外，还包括 Sanity、GLM PCA 等复杂模型——但这些模型计算极慢且性能无优势，不推荐常规使用），从以下三大维度进行了大规模基准测试：

  * 细胞分群一致性（10 套真实 10x 数据集）

  * 仿真数据集金标准还原

  * 高深度数据下采样模拟（模拟常规 10x 低深度场景）

4.1 测序深度（Size Factor）混杂效应

![Extended Data Fig 1（Ahlmann-Eltze & Huber, 2023）。核心结论：SCTransform 几乎消除了测序深度带来的 PCA 分层。同质 RNA 混合液 PCA，颜色深浅 = 测序深度。左：对数变换组，深浅细胞明显分离（ρ = 0.7~0.95）；右：GLM 残差组，深浅细胞充分混合（ρ = 0.15~0.49）。](https://mmbiz.qpic.cn/sz_mmbiz_jpg/buxFNhaTGwnzujRwnIgS3QYtLiafibqVibh5qU7DngI1cEMAVyVBW47H8G35FYE8nzyJwNPPMMysxwzrMgIkdz5rhibUzmqIu48zQUUnfN4kJrQ/640?wx_fmt=other&from=appmsg)

Extended Data Fig 1（Ahlmann-Eltze & Huber, 2023）。核心结论：SCTransform 几乎消除了测序深度带来的 PCA 分层。同质 RNA 混合液 PCA，颜色深浅 = 测序深度。左：对数变换组，深浅细胞明显分离（ρ = 0.7~0.95）；右：GLM 残差组，深浅细胞充分混合（ρ = 0.15~0.49）。

  * LogNormalize（Delta 对数变换）：典型相关系数 ρ 普遍较高（0.57~0.95），PCA 散点图明显按测序深度分层（不同深浅测序的细胞在图上分离），存在严重缺陷——仅简单除以 size factor 后取对数，无法消除测序深度带来的全局技术变异。在同质 RNA 混合液的 PCA 中，size factor 与前 10 个主成分的典型相关系数 ρ 高达 0.7~0.95，技术噪音掩盖了真实细胞分群。

  * SCTransform（GLM 皮尔逊残差类）：同质数据下 ρ 显著更低（0.15~0.49），PCA 图中不同测序深度的细胞充分混合，几乎看不到按测序深度的分层现象，技术混杂被大幅削弱。

4.2 均值-方差稳定效果（Mean-Variance 关系）

![Extended Data Fig 2（Ahlmann-Eltze & Huber, 2023）。核心结论：SCTransform 实现全表达区间方差均衡，低表达基因不再被压制。左：对数变换组，方差随均值攀升，低表达基因方差 → 0；右：GLM 残差组，曲线大幅扁平化。](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwn62jIPf3bMatQUt4l4eHLn0kRY537yg4t4SRZhrAGYuhiaBaT6eo0Cu1ibKsJJysHMO1ehEJNa9JU0oWpPX1F43S2SibPse53SmU/640?wx_fmt=other&from=appmsg)

Extended Data Fig 2（Ahlmann-Eltze & Huber, 2023）。核心结论：SCTransform 实现全表达区间方差均衡，低表达基因不再被压制。左：对数变换组，方差随均值攀升，低表达基因方差 → 0；右：GLM 残差组，曲线大幅扁平化。

  * LogNormalize：极低表达基因（均值 < 0.1）变换后方差几乎归零，丢失了低丰度基因的生物学信号；高表达基因方差被过度压缩，均值-方差趋势未能完全抹平。

  * SCTransform：全表达区间方差趋近均匀，对低表达基因赋予更高权重，理论上更适合保留稀有细胞亚群和低丰度标记基因的信号。无截断 Pearson 残差会引入大量极端离群值——这解释了 SCTransform 引入截断（clip）操作的必要性。

4.3 双峰标记基因的表达分布（以 Sftpc 为例）

![Extended Data Fig 3（Ahlmann-Eltze & Huber, 2023）。核心结论：LogNormalize 对双峰标记基因的区分可视化更出色。Sftpc 表达直方图，紫红 = II 型肺泡细胞，灰 = 其余。左：对数变换，两峰界限清晰；右：GLM 残差，阳性细胞弥散、峰重叠。](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwk3KePGeRyib1wEwGNicfFIF5OfZrThapg4WicRSc9eqxf0XEEibeLichu0tIlia7Nb1fa7CMd93tsQtxosstJ0h0Gx3t37GdThjjjx8/640?wx_fmt=other&from=appmsg)

Extended Data Fig 3（Ahlmann-Eltze & Huber, 2023）。核心结论：LogNormalize 对双峰标记基因的区分可视化更出色。Sftpc 表达直方图，紫红 = II 型肺泡细胞，灰 = 其余。左：对数变换，两峰界限清晰；右：GLM 残差，阳性细胞弥散、峰重叠。

Sftpc 是肺泡 II 型上皮细胞的经典标记基因，呈现典型的双峰分布——一类细胞几乎不表达，另一类细胞高表达。它是检验不同变换方法能否清晰区分高/低表达亚群的理想案例。

  * LogNormalize（对数变换组）：✅ 双峰分离效果最优。对数变换是非线性压缩，压低高表达区域的方差，拉开阴性细胞与阳性 II 型肺泡细胞的分布间距，两个峰界限清晰，能直观区分表达/不表达细胞。

  * SCTransform（GLM 残差组）：❌ 双峰区分度弱于对数变换。皮尔逊残差属于近似线性变换，无法压缩高表达亚群的波动，阳性细胞分布更加弥散，高低峰重叠程度上升，标记基因可视化的对比度下降。

小结：理论优势 ≠ 标记基因可视化优势。SCTransform 理论性能更强（更好地稳定方差、消除测序深度混杂），但面对双峰标记基因时，其表达分布对比度更低。根本原因：对数变换具备非线性压缩特性，适合展示双峰标记基因；皮尔逊残差近似线性，无法压缩高表达群体的离散度。

5、三大定量基准测试：核心结论

论文选用 k-NN 近邻重叠度作为核心评价指标——它衡量变换前后细胞的近邻关系保持一致的比例，特别适合评估连续细胞轨迹和过渡态的还原质量。对于离散分群任务，论文同时参考了 ARI / AMI 等指标，结论一致。以下为三大基准测试结果：

整体综合表现：LogNormalize ≈ SCTransform，对数法略占优势。

  * 一致性基准（10 套真实 10x 数据集）：移位对数（shifted logarithm）的 k-NN 重叠均值高于所有残差类方法（含 SCTransform），稳定性最优；

  * 仿真数据集：两者性能差距极小，不同仿真框架下互有胜负，无一方显著碾压；

  * 下采样基准（模拟常规 10x 低深度测序）：将高深度数据随机降采样后，以原始高深度数据的细胞近邻作为”金标准”，评估低深度下的还原效果。趋势与前两套完全一致——log(y/s+1)+PCA 整体不弱于 SCTransform。测序深度越高，所有方法的 k-NN 性能均同步提升。

⚠️ 避坑清单（汇总）

  * 不要指望 HVG 筛选或 Z-score 带来增益——论文三种基准一致证明：对 LogNormalize 增加 HVG 筛选、Z-score，或对 SCTransform 叠加 z 标准化，均无法稳定提升 k-NN 重叠。这些只是表面优化。

  * 不要用 log(CPM+1)——等效伪计数过小，人为制造过度离散。

  * SCTransform 不必逐基因精确估算离散度——使用固定过度离散参数即可达到同等效果，大幅降低计算量。

  * 无截断 Pearson 残差会产生极端离群值——这解释了 SCTransform 必须引入截断（clip）操作。

计算资源开销（速度梯队）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmecNkN3fUt0Js58jOK5nGvMpYnOb1ERDdXR4m4Iw5rS9mk0AkcWVVdb0VkFicWpHtcrhGJAHVtC31NicpyqaQc7gIQgxn2V56RA/640?wx_fmt=png&from=appmsg)

注意：LogNormalize 和 SCTransform 的复杂度均接近线性，可扩展至百万级细胞。

在处理百万级或数十万大样本数据时，算法的内存与耗时至关重要，[你的电脑算单细胞有多快?](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534021&idx=2&sn=16ac13e108e5c6fdbaf0f6efddce7034&scene=21#wechat_redirect>)如果你的计算机不足以支持大规模的计算，可按需选用适合自己的计算资源：

共享(经济实惠)：[云服务器已进入黑暗森林时代，教你一招安全连接](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540790&idx=1&sn=d7c13305d73c88ae94a17c35e6924b31&scene=21#wechat_redirect>)

独享(省电省心)：[如何拥有一台服务器，且不用自己搭建维护](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534670&idx=2&sn=b4296f98e4f8e171a8833a202bd9f926&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

更多内容可滴滴[**Biomamba_zhushou**]

文献的核心颠覆性结论：

尽管 SCTransform 拥有更严谨的 Gamma-Poisson 理论基础、能更好地校正 size factor、均衡全基因组方差，但在还原细胞真实亚群结构（k-NN、聚类）这个单细胞分析的核心任务上，最简单的 LogNormalize + PCA 综合表现不弱于甚至优于 SCTransform。

这证明了一个重要观点：理论优势 ≠ 下游实际分析性能。PCA 降维的平滑降噪作用，会在一定程度上抵消 SCTransform 在方差稳定方面的理论增益。

6、实操建议：到底该怎么选？

✅ 优先选用 LogNormalize 的场景

  * 常规 10x droplet 单细胞实验，追求快速分析、处理批量大数据集；

  * 核心目标是细胞分群、轨迹推断、常规降维聚类与可视化；

  * 关注双峰标记基因的可视化效果，无需专门挖掘低表达稀有细胞；

  * 数据量大，算力有限。

优势：速度快、内存占用低、k-NN 细胞拓扑还原综合最优。

✅ 优先选用 SCTransform 的场景

  * 研究稀有细胞亚群，依赖低表达基因来区分细胞亚型；

  * 下游分析重点是差异基因筛选、重视低丰度基因的生物学信号。

优势：理论方差稳定更完善，弱化测序深度技术干扰。

短板：计算速度较慢，双峰标记基因的可视化效果不如 LogNormalize，大规模数据集耗时明显增加。

**三、总结**

选择对比：场景| 推荐方法| 说明
---|---|---
常规分群/可视化/快速分析| LogNormalize| k-NN细胞拓扑还原最优，完成速度快
稀有细胞/低表达基因挖掘| SCTransform| 低丰度信号保留更好，需要接受较慢速度

陈聪

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=qywuinol&tp=wxpic#imgIndex=77)

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

[致谢文章又+1，生物信息学+机器学习鉴定驱动糖尿病肾病免疫激活和小管间隙损伤的PANoptosis枢纽基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537544&idx=1&sn=6e5bb738eb11af53173f9fef67b977df&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=7lj2ti0t&tp=wxpic#imgIndex=78)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家一起讨论。![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)您点的每个赞和在看，我都认真当成了喜欢

CoCo
