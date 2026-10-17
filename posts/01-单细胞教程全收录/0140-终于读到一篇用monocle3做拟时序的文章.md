---
title: "终于读到一篇用monocle3做拟时序的文章"
date: 2022-12-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496064&idx=1&sn=0be38306f9cd8c6b819d58cc2e779b87&chksm=9b3c88d0ac4b01c6773b6c4f1a063788509baa27c57e2098b16b8ebe38cc625a87b9d89272c7#rd
albums: ["单细胞教程全收录"]
---

# 终于读到一篇用monocle3做拟时序的文章

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496064&idx=1&sn=0be38306f9cd8c6b819d58cc2e779b87&chksm=9b3c88d0ac4b01c6773b6c4f1a063788509baa27c57e2098b16b8ebe38cc625a87b9d89272c7#rd
> 合集：单细胞教程全收录

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

在今年7月的时候我们拟时序的教程就把monocle2、3部分都介绍完了，当时Biomamba就表示发表的文献还都是以monocle2为主流，没想到目前我读过的文章依旧是以monocle2为主，去除那些我刻意检索monocle3的文章，我至今方才读到一篇通过monocle3完成拟时序分析的单细胞论文，题为**Single-Nucleus RNA Sequencing Identifies New Classes of Proximal Tubular Epithelial Cells in Kidney Fibrosis** ，投稿日期为**2020年的八月**[1]。

monocle3发布了已经有相当一段时间了，至于为什么现在文章中的拟时序分析以monocle2为主，我想最重要的原因可能还是用monocle3完成分析的文章大部分都还在**稿件准备** 和**审稿阶段** ，我依然相信明年和后年会成为monocle3的主战场。当然，这可能也不是主要原因，我们更应该关注monocle2与3的异同，我在做教程时就我就枚举过monocle2与3的优缺点：

### **monocle3的缺点**

目前monocle3已经更新到 _β_ 版本了，作者在官网也承认了缺点[2]，`monocle3`  _α_ 已经是不推荐使用的，可能会存在bug，但是`monocle3`  _β_ 仍然处于搭建中的状态，也就是说monocle3仍然是可能存在bug的，并且我们之前讲绪论的时候说到monocle1、2都发表在了Nature系列之上，但是`monocle3`迟迟没有发表，并且目前发表的文章还是使用`monocle2`的比较多，`monocle3`的不稳定性可能是重要原因。
官方表述如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpy5HLPX8ZLalmTNe48YRmicRkUzHmwGVQA8eZyGaqfYr9geJ0294gaibibVBNThpqlljo7twk987iaqtw/640?wx_fmt=jpeg)

### **monocle3的优点**

咱们抛开可能存在的**bug** 不谈，`monocle3`相较于`monocle2`具有以下几点优势：
(1)最大的优点就是**计算量** 变大了，可以处理**百万** 级别的单细胞数据集，也就是说整个器官、甚至整个胚胎的矩阵交给`monocle3`处理完全没压力。
(2)代码结构性优化：这点我要**吐槽** 一下，monocle系列的语法我一直觉得很奇怪，默认参数也很不人性化
(3)支持`UMAP`算法的降维，这个也非常Nice，速度比`tSNE`快的不是一星半点。
(4)支持多谱系的拓扑结构：换句话说拟时序的轨迹可以做的很复杂
(5)相较于原来的RGE算法，新的**approximate graph abstraction** 能够计算不连续的、平行的拓扑结构
(6)新的基因表达量计算及差异分析方法被引入，也就是说原来的`differentialGeneTest()`和`BEAM()`可以被替代。
(7)可以像`Seurat`的多样本整合一样对拟时序对象进行整合：这个功能可以说是刚需了，换句话说，如果你有合适的、已构建好拟时序的参考数据集，可以直接把自己的数据跟参考数据集进行投影、比对。
(8)数据整合时也可同时加上注释：这有点类似于`Seurat`中的`TransferData`，可以利用已经注释好的参考数据给现行数据添加注释。
(9)对`monocle`对象的读取、加载、转换做了一定的优化，我们后面可以看看效果如何
(10)优化了负二项分布模型：也就是说对处理count的优化
(11)可视化提供了**3D** 展示功能

总体来说monocle3给我的感觉主要是：
1、语法复杂、函数奇怪，似乎与monocle2完全不是一个团队开发出的产物。
2、算法与功能强大，但也意味着学习成本的提升3、最值得一提的功能是monocle3可以**选取** 细胞作为拟时序的**起点/终点** ，这对半监督式的分析来说是个利好，比如今天读到的这篇文章就是指定了正常的肾小管细胞为起点，指定纤维化的肾小管细胞为终点，从而满足作者的分析需求。4、从个人感官上来说，这个轨迹图真的让我犯密恐。。。。。。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpy5HLPX8ZLalmTNe48YRmicR1dTfictbBzztuBLicCbKEP1hVBjRZGsAItYOe2YHd9ibEH9mFUKubsGGQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpy5HLPX8ZLalmTNe48YRmicRysxAx3xu14SAumXfoyiaV0Ogdc10jghLX9oRnqumIQ3wM2Krckm2OuA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqxYF92esgbSzibpibzibzTHwLVVnyELLK10c4Gtwf2KmsmltWyKV9Iiar8A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

拟时序分析教程

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgEPt6jo0gEwibQzFX4zmOqqiaM9bZyTy3bIjLJcicVlkUFwFvyicJx8wR2ZslWiaBicM4nw9AtyQ7k7ugA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)B站连续播放起来比较方便：
https://www.bilibili.com/video/BV1br4y1x7Hf?p=1**往期推送**[单细胞测序数据进阶分析—《拟时序分析》1.概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》3.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487400&idx=1&sn=223a96a245c408c31e2c3c16afac88fc&chksm=9b3f76f8ac48ffee769dc76870e15bbd0275647dcfb9bf21bf499b7eaee86121b254e4b2da54&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》4.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
[解决monocle2的orderCells报错的两种方法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&scene=21#wechat_redirect>)
[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494479&idx=1&sn=32f39c79c4c9fc07aa829eed49016da3&chksm=9b3c921fac4b1b091efcdd151500b69d19f71d5ca518122af697fc37e87acd915f3be5f63fb8&scene=21#wechat_redirect>)

参考：

[1]Lu YA, Liao CT, Raybould R, Talabani B, Grigorieva I, Szomolay B, Bowen T, Andrews R, Taylor PR, Fraser D. Single-Nucleus RNA Sequencing Identifies New Classes of Proximal Tubular Epithelial Cells in Kidney Fibrosis. J Am Soc Nephrol. 2021 Oct;32(10):2501-2516.[2]http://cole-trapnell-lab.github.io/monocle3/
