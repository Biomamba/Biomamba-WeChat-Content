---
title: "scRNA-Seq学习手册Python版"
date: 2023-11-08
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&chksm=9b3caabdac4b23ab6e28425a4a5eb4d40ee3612e51f84f5d1e53ac91bef93f717e9e754398e3#rd
albums: ["单细胞教程全收录"]
---

# scRNA-Seq学习手册Python版

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&chksm=9b3caabdac4b23ab6e28425a4a5eb4d40ee3612e51f84f5d1e53ac91bef93f717e9e754398e3#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)我们B站的[十八万播放量的单细胞教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503465&idx=1&sn=e62ea7c78885c6959a535c2f1a10cd6d&chksm=9b3cb739ac4b3e2ffb60d625dc83b0b914d2956a64a6e8400712920dd2ac4c9f11e4e7752d74&scene=21#wechat_redirect>)是基于**R语言** 实现的。因此这里我们再整理一个scRNA-Seq学习手册的**Python版**(基于scanpy)，包含"准备工作"、"Anndata数据结构理解"、"单样本分析"、"scanpy可视化"、"多样本整合"、"PAGA轨迹推断"共六个章节。文末下载链接包含代码、学习手册、测试文件和输出结果。希望该手册可以帮助大家完成Python环境中单细胞基础分析的一站式学习，学习手册的演示可以看如下动图，翻阅起来比较方便：

![](../../images/abc9781887b03d2a.gif)

文末下载资料包含测试数据、**单细胞** 学习手册、输出文件、输出图片、标记语言文件(jupyter notebook和Rmarkdown，感兴趣的同学也可以点开学一学咱们的手册是怎么制作出来的)以及scanpy的**空间转录组学习** 手册：

![](../../images/6bfcb97d12ae393a.webp)

学习手册中的主要输出图片可参考：

![](../../images/52a73f790141eedc.webp)

当然，也更推荐大家直接在scanpy的官网学习：
https://scanpy.readthedocs.io/en/latest/_tutorials.html

**-Biomamba**

![](../../images/7d247e6c6ef19f87.png)

![](../../images/f08cdfe212eb6283.png)

文末还可解锁以下内容

![](../../images/2cc9da4d1e6321da.png)![](../../images/556752da2b520ff6.png)

公众号至今的573篇推送中，刚好有20篇付费内容，联系文末微信可以以119￥获取全部资料(包括今年后面更新的内容)。当然，付费不是目的，以下资料都可以通过**转发领取**(更推荐这种方式)。

[2022资料合辑(重置链接)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497402&idx=2&sn=4873b9088938bb39caab6f95ba4c085a&chksm=9b3c8feaac4b06fc88dc2bf696bb728c3d4bd3a4fb5c028ce4d3c9bbadd3aa6dc560510762b9&scene=21#wechat_redirect>)
[scRNA-Seq学习手册2023_R语言版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500516&idx=1&sn=3c0b9de505fcd232054e38b451fa1742&chksm=9b3cbbb4ac4b32a26b61f3a1f7941fff5852d3e6e744ec680aafd0b84ec976a33bf982fb5f79&scene=21#wechat_redirect>)[一文搞定拟时序分析的下游可视化探索](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497634&idx=1&sn=64872660e8ce80ff08c6c0745c2b241b&chksm=9b3c8ef2ac4b07e4a2ef03870c91fdc1c3ded245dcecd5a2049841cb7e9749bd1cd0852133f1&scene=21#wechat_redirect>)
[Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497669&idx=3&sn=ac3408c7dd28425426d954f81d283252&chksm=9b3c8e95ac4b0783c12182a960e8158c8a0992a20335f8c70f1dc63855c5984dd22e4dee706d&scene=21#wechat_redirect>)
[《拟时序分析》3.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)
[一文搞定单细胞基因集评分](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497831&idx=2&sn=82fa51c76a381fba0b444e9b6b23eb5f&chksm=9b3c8137ac4b0821dfb62e9b365ea3c32abbbd80df42df63181c37ad9ed991c0183c2c7981d8&scene=21#wechat_redirect>)
[改造单细胞降维图| 2.ggplot2中的DIY](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=1&sn=37a539bbd37dafb6cce5cd52dec84f52&chksm=9b3c81dbac4b08cd34b5edab4da14df5d0964a5c6fbe4dbab6f9879bbac9bc3f9e08abe8dd1c&scene=21#wechat_redirect>)
[改造单细胞降维图| 3.3D降维图与动图绘制](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498080&idx=2&sn=a9bcf65e3ae34ba201e8d49ee33c0728&chksm=9b3c8030ac4b0926c3f059a9a5d23f1bcdbcaf8e5a562eba2b7e3bec3396c44573269bd08e7b&scene=21#wechat_redirect>)
[一文搞定单细胞/空间转录组的WGCNA分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499737&idx=1&sn=b3f6174e1908494692d82ac154ce3218&chksm=9b3c8689ac4b0f9fbb0c8ba42172c702ca978683c4de28f9f56bd8e7764fe114ba9a1b9c7dac&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|2.学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21#wechat_redirect>)[生信Python速查手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&chksm=9b3cb9c1ac4b30d7bbd44057b181f87541f5904d24f903494ae557e768ae00c208c1b68b45c7&scene=21#wechat_redirect>)
[单细胞复写|3.急性心肌梗塞(AMI)外周血scRNA-Seq分析实战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501145&idx=2&sn=12c2e8d104ad343fc13acb8cda266e6c&chksm=9b3cbc09ac4b351f4ed708a0ed577a21f48ccb0d4173aed94a027b4170147ab85931ee51d1e5&scene=21#wechat_redirect>)
[SCENIC单细胞转录因子预测|4.精简版流程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21#wechat_redirect>)
[《细胞通讯》2.CellChat基础分析教程](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=2&sn=fb3e252d95ee8b50cd446e71335b1aa0&chksm=9b3cbca0ac4b35b621b4f51d2c3a130f00461faeeff067396222c2fc2eeb53f3544664d7d9bc&scene=21#wechat_redirect>)
[《细胞通讯》2.2CellChat多组别分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501523&idx=2&sn=6fa803f256c2e0b945f93ae7d8245f50&chksm=9b3cbf83ac4b3695b587e9817840f419104c8680f5ef08ee39aa149b79852f48b179f68e3397&scene=21#wechat_redirect>)
[《细胞通讯》CellChat学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501735&idx=2&sn=35fc792961507f4ae1cbae3a2882fba6&chksm=9b3cbef7ac4b37e1417d4108c8bd378c68c3907431ddfc52ad37c916e85649bb450d761a8e19&scene=21#wechat_redirect>)
[《拟时序分析》3.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&scene=21#wechat_redirect>)
[ComplexHeatmap学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503470&idx=1&sn=81b5142c5c4f1af9ae87bdc480d5469b&chksm=9b3cb73eac4b3e285467305c2a8d08b07d8b56d85bce96bd978c422d1f22b2c0dad0ed1dc752&scene=21#wechat_redirect>)[沉浸式统计细胞比例](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&chksm=9b3ca933ac4b2025f922a325ec6893e93613f130ff1d4fd609e2d7274f7f1fdb5134092e28ad&scene=21#wechat_redirect>)[VlnPlot的ggplot改造](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=1&sn=b795a3e36ae092d8f87abb5a87187828&chksm=9b3caa9bac4b238dd33e905c33924b58aa4ff14e83abbf08046fba7fe765ecb0204163cb6acf&scene=21#wechat_redirect>)

![](../../images/3536da08710707f3.png)
![](../../images/399758fa7d6941c2.png)

订阅后获取学习手册下载链接：

![](../../images/fbfc4b8be383f432.png)
