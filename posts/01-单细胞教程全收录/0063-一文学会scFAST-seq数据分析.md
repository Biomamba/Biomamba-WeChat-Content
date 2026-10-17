---
title: "一文学会scFAST-seq数据分析"
date: 2023-11-17
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505213&idx=1&sn=5f4ed0587dd96149d127a98d36f721f0&chksm=9b3cac6dac4b257bbc00c4647382d27883139bf06ab3071947bf1cccde8d1d501006dabab5f1#rd
albums: ["单细胞教程全收录"]
---

# 一文学会scFAST-seq数据分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505213&idx=1&sn=5f4ed0587dd96149d127a98d36f721f0&chksm=9b3cac6dac4b257bbc00c4647382d27883139bf06ab3071947bf1cccde8d1d501006dabab5f1#rd
> 合集：单细胞教程全收录

**学习手册**

![](../../images/07e88994d32c0968.png)

## ![](../../images/086c3b2d9d29435d.gif)

与以往的教程一样，我们给大家准备了数据分析的学习手册，目前分为scFAST绪论、准备工作、fast模块、Seurat分析与可视化、mut模块等五节内容及对应测试文件(更多章节持续创作中)，大家可以添加企业微信回复关键字"**scFAST学习手册即领** ":
![](../../images/a1dbb3a25a832fe1.webp)

**一、scFAST绪论**

![](../../images/07e88994d32c0968.png)

## 1.1 写在前面

单细胞的论文我们介绍过很多，大家可以前往合集查看更多内容：[文献速递](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2802463431357661184&scene=173&from_msgid=2247498597&from_itemidx=1&count=3&nolastread=1&uin=&key=&devicetype=Windows+11+x64&version=63090621&lang=zh_CN&ascene=1>)。此处我们需要向大家介绍一个单细胞组学新技术，该文于3月23号发布在预印本，题为”High throughput detection of variation in single-cell whole transcriptome through streamlined scFAST-seq”的文章。这项技术(single cell Full-length RNA Sequence, **scFAST-seq**)。该单细胞平台由**寻因生物** 历时三年开发完成，可以在`8h`内建库构建约`12,000`个细胞的全长RNA文库。这是一种依托于随机引物建库策略的单细胞全新技术。传统的`3'`端建库策略由于其通过`oligo-dT`去捕获转录本的`polyA`尾，因此对非polyA尾的`lncRNA`、`rRNA`、`circRNA`、`eRNA`等RNA分子敏感性不足。因此，相较于3‘端策略来说，`scFAST-seq`利用随机引物进行随机捕获，避免poly A尾的介入，使得其在检测`非polyA`的转录本、覆盖 _更长的转录本_ 长度和鉴定更多的 _剪接位点_ 方面具有明显的优势（这意味着能够更深入的挖掘转录本层面的信息）。对于细胞分化、拟时序分析、RNA动力学分析等进阶分析内容来说，scFAST-seq也较3’端策略而言具有更好的效果。在cDNA终文库的基础上也可以灵活选择 _cDNA巢式扩增_ 或测序文库的探针捕获，从而针对不同的研究目的富集对应的序列。

视频教程可见(文末阅读原文可跳转)：https://www.bilibili.com/video/BV1F94y1879j/

## 1.2 主要结果

### 1.2.1 建库流程与特征

具体建库的实验流程的受众比较少，感兴趣的同学可以阅读一下原文的methods(https://www.biorxiv.org/content/10.1101/2023.03.19.533382v1.full)。大致来说，与大家熟悉的`10X Genomics`一样，单细胞悬液会被制备成一个**油包水** 的体系，但`scFAST-seq`使用随机引物而非3’端的oligo-dT去捕获RNA分子参与逆转录，优化后的随机引物`12N7F`能够捕获到更多的转录本与RNA分子：
![](../../images/9c89850943524424.webp)

以往的`5'`策略在`Bulk RNA-Seq`中被频繁使用，因为Bulk RNA-Seq可以很方便的使用`RNase H`降解`rRNA`，但在单细胞建库中，这就是个难题。因此`scFAST-seq`使用在使用随机引物的同时加入了一种”阻断”探针，能够特异性的 _阻断_`rRNA`与`mtRNA`的逆转录从而大大降低文库中`rRNA(30%→10%)`与`mtRNA(6%→1%)`的占比：
![](../../images/9b3b0b55fd6b58ca.png)

`scFAST-seq`的流程示意图如下所示：
![](../../images/698fda5787b6dbbe.webp)

### 1.2.2 `scFAST-seq`与`3'`策略的`scRNA-seq`一致性评价

作者对`K562`、`A549`、`HCC827`混合细胞系、乳腺癌、胶质母细胞瘤、小鼠胰腺癌、外周血等样本分别进行了`scFAST-seq`与`3'`策略的`scRNA-seq`的测序，与上文表述的一样，`scFAST-seq`获得的`mtRNA`与`rRNA`数量都更少(图A)。与此同时，`scFAST-seq`的`reads`分布在基因中的位置更加的均匀，而不是像`3'`测序那般主要集中在`RNA`分子的`3'`端(图B)；这显然更有利于 _转录本结构_ 的研究。在基因定量方面，相关性分析(图D)、降维分析(图E)与细胞比例分析(图F)均显示`scFAST-seq`与`3' scRNA-seq`具有极为相似的表达矩阵；`infercnv`分析方面两种技术的一致性极高(图G)。但在转录本的捕获数量上而言，在对应样本中`scFAST-seq`依旧是更胜一筹(图C)。 ![](../../images/5c00f8f5ac337397.webp)

### 1.2.3 `scFAST-seq`与目的区域富集技术的结合

期望简单的通过增大测序量来增大目的区域的`reads`数是不切实际的，因此通过生物素探针或`巢式PCR`可以提升目的区域的捕获效率，例如`EGFR 19del`可通过生物素探针 _提升近一倍_(图A)、巢式PCR也可以在少量的细胞中捕获到更多对应的转录本(图B)。`scFAST-seq`与目的区域富集策略的结合可以用最低的测序成本获取更多的目的信息。

![](../../images/a3ec521598401010.webp)

## 1.3 小结

作为全序列的产品，相较于3’单细胞测序而言，其有以下优势：

![](../../images/cb85758a68ebbe1b.webp)

作为一款对标SMART-Seq2的国产测序技术，scFAST-seq的表现十分优秀。scFAST-seq与SMART-Seq2对比可见：

![](../../images/af59d4d08f9f1208.webp)

当然，scFAST-seq也并不是没有缺点，其对于低丰度的转录本捕获效率稳定性不足。为寻因生物点赞的同时也期待单细胞领域出现越来越多有竞争力的国产平台！

**二、准备工作**

![](../../images/1189c1178040d051.png)

##  scFAST学习资料可添加**文末企业微信** 领取，本节的视频教程可见(点击文末阅读原文可跳转)：

## https://www.bilibili.com/video/BV1F94y1879j?p=2

## 2.1 `SeekSoul®Tools`简介

``

#### 2.1.1 简介

`SeekSoul® Tools`是寻因自主研发的单细胞数据自动化质控分析软件，包括细胞标签提取、测序数据质控、参考基因组比对、基因定量以及表达矩阵构建等流程。兼容寻因生物`SeekOne® MM`、`SeekOne® DD`不同单细胞技术平台数据，实现高水平质控分析。

### 2.1.2 模块组成

目前该软件包含三个模块:
-（1）rna模块
用于识别细胞标签`barcode`，比对定量，得到可用于下游分析的细胞表达矩阵，之后进行细胞聚类和差异分析，该模块不仅支持`SeekOne`系列试剂盒产出数据，还可通过对`barcode`的描述，支持多种自定义设计结构。
-（2）fast模块
该模块专门针对`SeekOne`全序列试剂盒产出的数据，用于对数据进行`barcode`提取，**双端**`reads`比对，定量，以及全序列数据特有的指标统计
-（3）mut模块
该模块针对 _SeekOne全序列_(`scFASTA-seq`)数据及`panel`捕获后数据变异检测及可视化分析。

### 2.1.3 软件优势

1、灵敏检测低UMI细胞：采用高UMI阈值+EmptyDrops的方法判定细胞；
2、支持多平台数据分析：适配寻因自主平台及10x 等其他平台数据；
3、分析结果格式支持下游多种开源软件。

## 2.2 预备知识

为了无障碍的学习本教程，建议先行学习以下教程：

### 2.2.1 单细胞教程全收录

B站视频:先看一遍视频再去看推送操作，建议至少**看三遍**
以下的资料都可以在这里订阅： [单细胞数据基础分析学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492295&idx=1&sn=d4e81588c0ac2906849c8bc44d079209&chksm=9b3c9b97ac4b1281ab462f866538f096ba2473a3d1426a27d8d97ccc636bfd081e1ba8934dfd&scene=21#wechat_redirect>)

#### 1\. 单细胞测序基础数据分析**保姆级教程** ，代码部分整理在往期推送之中：

[手把手教你做单细胞测序数据分析（一）——绪论](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&chksm=9b3cb950ac4b30467a082527547b91aec15b7d1f40d44e362894aedeb6a99e014518fa5e4743&token=767842863&lang=zh_CN&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析（二）——各类数据结构与读取方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499795&idx=2&sn=68e6298eb43633c71939c146d90230ff&chksm=9b3cb943ac4b3055e09739d77e037d679f3d9ec68780d1aa8c592f806fcc8d2322eaee78752d&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（三）——单样本分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（四）——多样本整合](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（五）——细胞类型注释](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（六）——组间差异分析及可视化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（七）——基因集富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)

#### 2\. 上游**fastq** 文件处理：

[单细胞分析的最上游——处理Fastq文件：cellranger](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484923&idx=1&sn=b5876af14fbee68d1e9db4b0f70cd1c8&chksm=9b3f7cabac48f5bdb3aac7d20201d89121a83720b41a10017564fedbb8c4a13df0da92daffd7&scene=21#wechat_redirect>)
[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484937&idx=1&sn=4fe1fa518202bdaf462bb93a2614ed32&chksm=9b3f7f59ac48f64fafaf34bac2c80f06d3a86b6a84ccf12566c7eac25bb71c7edd3d74004cf7&scene=21#wechat_redirect>)
[有奖提问,这个smart-Seq2数据实战的比对率为何如此低？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488441&idx=1&sn=dac4efc4a8901a4abb133f9e5c80831e&chksm=9b3f6ae9ac48e3fff5a7112a0127726441ccb9dc2c3369d4a0fe98a2120df991954ff0567732&scene=21#wechat_redirect>)

#### 3\. **细胞通讯**

B站连续播放起来比较方便
**往期推送**
[单细胞测序数据进阶分析—《细胞通讯》1.概论](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485403&idx=1&sn=e148e2d09556a85333cd9c212a880aaa&chksm=9b3f7e8bac48f79d6288977f3a67ebed5813dfe92e4a227a2e304eb68321771b3511fdaf5ba5&scene=21#wechat_redirect>)
[](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485680&idx=1&sn=8168685ab9bbf772dce24e8673994033&chksm=9b3f71a0ac48f8b6554aa6f30a81f7e622fd8bf2f6a83701839290b7dd8f1c90343592603413&scene=21#wechat_redirect>)[单细胞测序数据进阶分析—《细胞通讯》2.1CellChat基础分析教程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485680&idx=1&sn=8168685ab9bbf772dce24e8673994033&chksm=9b3f71a0ac48f8b6554aa6f30a81f7e622fd8bf2f6a83701839290b7dd8f1c90343592603413&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《细胞通讯》2.2CellChat多组别分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485706&idx=1&sn=2d39360b41733b0be6f88d2922388507&chksm=9b3f705aac48f94cc478210f7f11d37294156517c489dedb333d8647ca287134a29944f39a3d&scene=21#wechat_redirect>)
[给你们申请到了免费的128GB云服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485734&idx=1&sn=32c75f6d07b49084e518af6d18099e8b&chksm=9b3f7076ac48f9600593b319d2e0b36bf5a62399a9835caa5783ad36fbdec6004e04cb656db9&scene=21#wechat_redirect>)

#### 4\. **拟时序分析**

B站连续播放起来比较方便
**往期推送**
[单细胞测序数据进阶分析—《拟时序分析》1.概论](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486553&idx=1&sn=b689ec962a17ca1a1ada29ae8ff8c019&chksm=9b3f7509ac48fc1f0f81e288de8f15c86548215a1cd9d5c740dc63f2421371d13890398ab1df&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》2.monocle概论](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487001&idx=1&sn=329129e75f703e3f332e76af9c66871e&chksm=9b3f7749ac48fe5f081248c2a48c56685e3915015036c73f8f67ec3e6acc246ddf815daedb22&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》3.monocle2实操：完整版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497730&idx=2&sn=930dc0e276219d70c937e943119388ff&chksm=9b3c8152ac4b08446d457cef3ede4a4a17c0ebacaec0c36efe7d7c8706fb4a3d62222d702ee5&scene=21&cur_album_id=2820794880947159043#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》4.初识monocle3](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489044&idx=1&sn=061dbfc34d200b73a8227d0bb28a1d27&chksm=9b3f6f44ac48e65251f7e5ecce84637c05d50ecb92769e8386f221f8e7b9bfeb719232def863&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》5.monocle3的降维、分群、聚类](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489494&idx=1&sn=44f0a44857c12fcf9a1ab84e4f2cbebf&chksm=9b3f6e86ac48e79026321de2fdca81a139d104d655884ffe87a68e0a1551ddffa5af7919d19e&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》6.monocle3的拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490418&idx=1&sn=18ae0b6139fe1a2436dcf6cc47850297&chksm=9b3f6222ac48eb3450de0b02a34eb5fff2db89ab8f155460d554cbb23be0cd27fd349079e7b2&scene=21#wechat_redirect>)
[单细胞测序数据进阶分析—《拟时序分析》7.解决monocle2的orderCells报错的两种方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491083&idx=1&sn=c5697ab024193cb6595d27e4f4d3bfaf&chksm=9b3f675bac48ee4d7244d9819e14fe210f7e42e40fc7a6a8df7b95bfd92f06334d60d226cb93&token=333450324&lang=zh_CN&scene=21#wechat_redirect>)
[一文搞定拟时序分析的下游可视化探索](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497634&idx=1&sn=64872660e8ce80ff08c6c0745c2b241b&chksm=9b3c8ef2ac4b07e4a2ef03870c91fdc1c3ded245dcecd5a2049841cb7e9749bd1cd0852133f1&scene=21&cur_album_id=2820794880947159043#wechat_redirect>)

#### 5\. 其他单细胞相关**技术贴** :

[细胞的数量由誰决定？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484056&idx=1&sn=4967a054f5241ff3a1bd4a6fe9a502b1&chksm=9b3f7bc8ac48f2deca3141461be035deb8658be184d78597af28f8ba2092d12f020768275248&scene=21#wechat_redirect>)
[单细胞中应该如何做GSVA？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484701&idx=1&sn=ad90680f252d092a2e21f349c8f32cab&chksm=9b3f7c4dac48f55bf1d11337406ab0e1295e8e1731dbac0715eedc99d11beff7f380e42dd49b&scene=21#wechat_redirect>)
[答读者问（三）：单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)
[答读者问（四）：如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)
[答读者问（八）：为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)
[答读者问（十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)
[答读者问（十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析：Loupe Browser](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a&scene=21#wechat_redirect>)
[什么？不做单细胞也能分析细胞类群和免疫浸润？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485798&idx=1&sn=c849bc7a0093af92fc99e13b55842bb2&chksm=9b3f7036ac48f92048d726b38f2dd978d0b0cce779c1a4090aa4da5cb2df3ad30a5c5dbed27e&scene=21#wechat_redirect>)
[答读者问 （十三）查看Seurat对象时的ERROR：type=‘text’](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)
[各类单细胞对象（数据格式）转换大全（一）](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485925&idx=1&sn=14e08440200f0f5cb4dcc2dc615efeb8&chksm=9b3f70b5ac48f9a37a43cc2a8b2a5e485a3f84b4ef87949dfe99056bc6301b110e80800f6bb1&scene=21#wechat_redirect>)
[批量整理好GEO中下载的单细胞数据](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486045&idx=1&sn=0b6874bcffc8abafb505cabce4c4fc0e&chksm=9b3f730dac48fa1b140ef01c07a7749e69df4fa7d2056deeed0673c668b6246724cd85741125&scene=21#wechat_redirect>)
[答读者问 （十四）Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)
[答读者问 （十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)
[答读者问 （十六）做单细胞测序到底需要多少内存](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487923&idx=1&sn=15043c6d729b0d5493ab875b0e54a259&chksm=9b3f68e3ac48e1f5dae514a01c857f9a56a90e2977dd7862db28d06fe55888cd9bb4afbb14e0&scene=21#wechat_redirect>)
[答读者问 （十七）调用的线程越多就算的越快嘛?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488995&idx=1&sn=7140e0d037671542fb37dff3a3c94b28&chksm=9b3f6cb3ac48e5a5f54a02be9e6af9f5a4cf8da1de1770f9035130c84dedf059a024964fc15a&scene=21#wechat_redirect>)
[答读者问（十八）、一个我至少被问过30遍的monocle报错](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25&scene=21#wechat_redirect>)
[一文搞定单细胞基因集评分](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497831&idx=2&sn=82fa51c76a381fba0b444e9b6b23eb5f&chksm=9b3c8137ac4b0821dfb62e9b365ea3c32abbbd80df42df63181c37ad9ed991c0183c2c7981d8&payreadticket=HCkRKr7R3-O3p5-0VkAwOOfgIXR8STjX9HoZYYWKS3jgJtptsG2Mu4KWI6Pz6cAuCOxiFPM&scene=21#wechat_redirect>)
[沉浸式统计细胞比例](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490949&idx=1&sn=b8dbe07d901f7c24f82d078be7a2fc77&chksm=9b3f64d5ac48edc33980363c7bc862a9f6283b78dac407e9c082d80bd7d9669215eecac62347&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[没有barcode文件的单细胞数据要怎么读取](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490952&idx=1&sn=364a3941e59e45234795c906a42fc9ab&chksm=9b3f64d8ac48edcec70384cf5c6a91224d0f7841ce3a7cfcade6513500c13673a6695d6f0299&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[单细胞基因集评分之AUCell](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491761&idx=1&sn=41f5c1ceaacf6a1c4840567f8a349e06&chksm=9b3c99e1ac4b10f7ca158561e96fec76a49ff32b8412cb146ed3fb7aa9260c75172b4eb16f9a&scene=21&token=7173752&lang=zh_CN#wechat_redirect>)
[如何加快Seurat的计算速度](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494116&idx=1&sn=f3dc577cbb464779062aada313191a05&chksm=9b3c90b4ac4b19a27a17f958e3437337d5b10b6ba7153e4dd43dedcb4df812d8c6b4d86fe970&token=416896563&lang=zh_CN&scene=21#wechat_redirect>)
[粉丝来稿|1. Seurat4相较于Seurat3的几点改动](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494516&idx=1&sn=cb2d4e6b182428ce7b98e7fff2e8729a&chksm=9b3c9224ac4b1b32c4fe99758960305c4845395cfe03851d70a0407043ee36250e55d20106fc&scene=21&token=1634975705&lang=zh_CN#wechat_redirect>)
[如何加快Seurat的计算速度](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494116&idx=1&sn=f3dc577cbb464779062aada313191a05&chksm=9b3c90b4ac4b19a27a17f958e3437337d5b10b6ba7153e4dd43dedcb4df812d8c6b4d86fe970&token=468535359&lang=zh_CN&scene=21#wechat_redirect>)
[答读者问（二十）四个单细胞样本只给了一套文件怎么读](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494879&idx=1&sn=c2287ab3684792747dfac53d6704462b&chksm=9b3c958fac4b1c994a4b075c4f8475816e121966fa8c52cb0a2ce8c14987988ab9bdb49bdf69&token=468535359&lang=zh_CN&scene=21#wechat_redirect>) [人类单细胞测序数据中有哪些以”**-“开头的基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495019&idx=1&sn=f52ac22ca1ea47ecddaa3503bdc2c0b6&chksm=9b3c943bac4b1d2d521f7155ce8f499389dade23828017572a84cdce71e5d08d37d74e08512b&scene=21&token=1624480671&lang=zh_CN#wechat_redirect>)
[为什么总把分辨率调的很高](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495765&idx=1&sn=2ec5e3e26491e28c92e25c40630bffae&chksm=9b3c8905ac4b0013a23f9cda2cccd67cdf3c4a941bac161e3a15a12ab98cd4e5eca8aeedbe96&token=133749967&lang=zh_CN&scene=21#wechat_redirect>)
[答读者问（六）：Seurat中如何让细胞听你指挥](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497669&idx=3&sn=ac3408c7dd28425426d954f81d283252&chksm=9b3c8e95ac4b0783c12182a960e8158c8a0992a20335f8c70f1dc63855c5984dd22e4dee706d&scene=21&cur_album_id=2820794880947159043#wechat_redirect>)

#### 6\. 单细胞文献阅读

[Biomamba助推的第二篇文章!发表了！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489823&idx=1&sn=6a5dddd53870395316d2b2e904c6ce72&chksm=9b3f604fac48e959e97e4b0317643efdcf117da7f8b75f1edbcd64dd8e2f07149e6031a94dd4&scene=21#wechat_redirect>)
[又来了！Biomamba生信基地助推的第四篇文章!](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492532&idx=1&sn=cddb4691f23defc80b60da231790c53c&chksm=9b3c9ae4ac4b13f2334cc7f6b16eec1d8223800f6ecef71a93cfba21698ac5f4505dbd64f300&scene=21#wechat_redirect>)
[单细胞测序解析糖尿病肾病中肾小球的动态变化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497682&idx=2&sn=7ef49191c5e334bb291ccdaa8ea444ae&chksm=9b3c8e82ac4b079425433938c831d528eddb9237efaca49acbc210e9cd715d057541589dc290&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[单细胞测序技术解析健康人与T2D患者的胰岛差异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=1&sn=b7f8df758bc4d95b88969378c6dfbeee&chksm=9b3c8ea1ac4b07b7c6a0b5023ebf6c8ecd7d34741ab076baa0b564535d1d753bbf9dc5be5290&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[小鼠全肾单细胞测序开篇之作](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497713&idx=2&sn=554d6a4e1b28b2e5303695fae5942a34&chksm=9b3c8ea1ac4b07b72323ce25cd49474a9228ec1aaa56243f57dca3f2f668dc42ab9cd58dca21&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[Nature也能白嫖？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=2&sn=caeb8ed06ffd5239b58cebcd90843cf8&chksm=9b3c81dbac4b08cd9eec50978951a1b890ca08edec644ff75205a09ad1f067dff25d6ecb938e&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[一篇不花钱就能白嫖的文章](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497840&idx=2&sn=1dacbfb190e11d2ff104e32f238cf8c4&chksm=9b3c8120ac4b08367bfe3a0dd8d55f21f5d13528826de3144a9a85ce9b1c9f4c710de703edae&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[高氧下小鼠肺发育损伤的ScRNA图谱](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498513&idx=2&sn=79845edf56a3023c59c73403d7b6494b&chksm=9b3c8241ac4b0b57793402686edc8c35aaa3b0959d3096b5122207fbb70ab809d1df5faee0d7&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[文献阅读（十二）、IgAN & STRT-Seq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485376&idx=1&sn=02e228d0993d8a653c8bb1d531021cdb&chksm=9b3f7e90ac48f78686d6d5953aeb192db4f28bf577dbebd76d9fabbe797f135b7fb08fb42867&scene=21#wechat_redirect>)
[老树开新花——EGFR、肿瘤、免疫+scRNA-Seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498596&idx=2&sn=8f63f5856cdf90e15f1d19b4cfe6a39e&chksm=9b3c8234ac4b0b221a5d2c417558f0e63f742459c0a3f8c1cbb4cdf74ce25ddcaf0e48f4a7ce&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[癌前基质细胞驱动BRCA1肿瘤发生](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498597&idx=2&sn=9f5fee38d0821052c9c6b3753c2b3bed&chksm=9b3c8235ac4b0b238c4902ad7b3944b285baaa0a7ec6f5c7d08a596fdf89735dc7a7afab91f0&scene=21&cur_album_id=2802463431357661184#wechat_redirect>)
[文献阅读（十八）、紧跟生信”钱”沿,胰腺癌&免疫多模态图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489045&idx=1&sn=29feb00f094a9a7e20418b22aa54dd8c&chksm=9b3f6f45ac48e653d4223838eb1d96e65e5ee51ac3f7782841d9b33013bdb67b5e22e9599fac&scene=21#wechat_redirect>)
[文献阅读（十九）、原发头颈癌和肿瘤转移微生态](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489511&idx=1&sn=76ec706ebd97e3edd08687f5cf3b6816&chksm=9b3f6eb7ac48e7a10bb81aec5332ecc0544a683f576ea680c8baa621e504816bf65c7d331bdf&scene=21#wechat_redirect>)
[文献阅读（二十一）、肾脏疾病&代谢&核受体ESRRA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490575&idx=1&sn=b931a1d50ddcfc4e34999763139695a0&chksm=9b3f655fac48ec49eb2fb01ce8acb15e230091ab3c29ce1471747850be5dae54dbe97fd103b0&scene=21#wechat_redirect>) [文献阅读（二十二）、PD-1&急性髓细胞性白血病&T Cell](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490929&idx=1&sn=82bf93ccbd9dd906caad8ec709c86153&chksm=9b3f6421ac48ed37117794e7c5b878fa78760627e8bced9c37a2c7c67fd8afd58d0cf0add17e&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[文献阅读（二十二）、PD-1&急性髓细胞性白血病&T Cell](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490929&idx=1&sn=82bf93ccbd9dd906caad8ec709c86153&chksm=9b3f6421ac48ed37117794e7c5b878fa78760627e8bced9c37a2c7c67fd8afd58d0cf0add17e&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[文献阅读（二十三）鼻咽癌微环境&scRNA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491084&idx=1&sn=e450844d4f102caa88cab6deb630a3f4&chksm=9b3f675cac48ee4a6883559859a21d77256479bb8d030c54a91240827d85b925066bc4f8ebb6&token=333450324&lang=zh_CN&scene=21#wechat_redirect>)
[文献阅读(二十四)、《Nature》：MYB调控衰竭性T细胞对检查点抑制的响应](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491909&idx=1&sn=5d47d2917397248dd6a3a9e85f2acd6d&chksm=9b3c9815ac4b11037e52ba00215a0b6cd23b554139955123ef21ac2cd07a646e97309e7def78&scene=21&token=7173752&lang=zh_CN#wechat_redirect>)
[文献阅读(二十八)、单细胞都能活检测序了？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493604&idx=1&sn=d0f8738e26a4b1c870d329b6a4a7b689&chksm=9b3c9eb4ac4b17a2d0b04d72c350c20f575701de7179f77fcd3567f4b1533cf35df4157f67e1&token=416896563&lang=zh_CN&scene=21#wechat_redirect>)
[文献阅读(二十九)、单细胞测序做到什么程度能毕业|硕士篇](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493808&idx=1&sn=52c7d330ffdda47c3409d36fe9cbbcd8&chksm=9b3c91e0ac4b18f6edf59d171a0d982b1e3f842148046d8eed19343484feaa84dbd5b7682a11&token=416896563&lang=zh_CN&scene=21#wechat_redirect>)
[文献阅读(三十)、单细胞测序做到什么程度能毕业|博士篇](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494017&idx=1&sn=a2dc4e2eef2bcdb40f5074b665dfa45f&chksm=9b3c90d1ac4b19c79ac5128f96d27789241357c9745bb0389ff5f79f96ab825d3e1c9b29e3af&token=416896563&lang=zh_CN&scene=21#wechat_redirect>)
[2022年了，都有哪些器官/组织有scRNA-Seq数据|小鼠篇](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494796&idx=1&sn=92c91a65719bdf39658814eb691a780f&chksm=9b3c95dcac4b1cca5547440a5881e650da3ea430bad3e6017cbd2891606b2ec40e3ec343bc0e&scene=21&token=468535359&lang=zh_CN#wechat_redirect>)
[2022年了，都有哪些器官/组织有scRNA-Seq数据|人类篇](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494806&idx=1&sn=1d15ad9cb4d350a164d3b941bc715233&chksm=9b3c95c6ac4b1cd054cedbd3e8c8f57ee88cc59a6ebda2fd11ba8fea79f5e9e8c65d21ff338c&scene=21&token=468535359&lang=zh_CN#wechat_redirect>) [终于读到一篇用monocle3做拟时序的文章](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496064&idx=1&sn=0be38306f9cd8c6b819d58cc2e779b87&chksm=9b3c88d0ac4b01c6773b6c4f1a063788509baa27c57e2098b16b8ebe38cc625a87b9d89272c7&scene=21&token=445940587&lang=zh_CN#wechat_redirect>)
[单细胞转录组+亚细胞空间代谢组=25分文章](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496126&idx=1&sn=8cb6040a38eb844bb215c0d395196e3a&chksm=9b3c88eeac4b01f8dcb8f4c7a19c5a58841d5fe1623f0a4c585c6dcc281cbbdd2830a1150f6a&scene=21&token=445940587&lang=zh_CN#wechat_redirect>)

#### 7\. 单细胞注释复写

[单细胞注释复写(一):Human Fetal Kidney](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490504&idx=1&sn=0066b2b33067cedb9d1c28689a53faab&chksm=9b3f6298ac48eb8e12cdc7bdd6263e5feb9039f549f7b9dbf4e258854ee61476d09f702f1447&scene=21#wechat_redirect>)
[单细胞注释复写(二):Human colorectal](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491642&idx=1&sn=2246fb702277ddc690f056fc8854142e&chksm=9b3c996aac4b107c059a403978eca7be1ae7987659626272c58430910ad75892ad470517aefb&scene=21#wechat_redirect>)

#### 8\. 非技术帖

[生信分析为什么要使用服务器？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491007&idx=1&sn=8619c2bad23791b3252a1c4cb1831931&chksm=9b3f64efac48edf9c02f84959aeee9b12480736fce70c5ddb8b41d79cfc22ce590ea2cb60fba&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[有root权限的共享服务器,报我名字立减200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492383&idx=1&sn=b8d912877cb38e8d8c9084d1d9370ded&chksm=9b3c9a4fac4b135926091a8af972c45a17a2fa1f94c704779c60df5f733847036c3797894c1c&scene=21#wechat_redirect>)

### 2.2.2 `Linux`基础教程

B站爆款视频同步播出
[Linux| 一.计算机硬件组成](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491413&idx=1&sn=1252abc3bd5584bdf5d59487c8dd61e3&chksm=9b3f6605ac48ef13bf0bc605a9f3bba4b804f56b824a0b2a550f7c831516441e829f35ed9f69&scene=21#wechat_redirect>)
[Linux| 二.计算机软件组成与Linux](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492243&idx=1&sn=bbb06cfd7a0836943262bf4897a390d1&chksm=9b3c9bc3ac4b12d529d9e5173c1ef22f43db3dbffac9143384fb463f30da1ca6afeea8d987bb&scene=21#wechat_redirect>)
[Linux| 三.免费获得Linux系统-WSL](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493279&idx=1&sn=ab7f430ea98de7f29d8f4bfb238eb0d6&chksm=9b3c9fcfac4b16d916ba186e658ffb8973043e85f2fd0cf524a1f27715056555ba0130b0c2d5&scene=21#wechat_redirect>)
[Linux| 四.免费获得Linux系统-虚拟机](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493649&idx=1&sn=0b3070157cc16bb54424bec5b8641d32&chksm=9b3c9141ac4b18574a6a09a78749e40df7bbbb320fad2a593d7a61586526085ebbdabd148384&scene=21#wechat_redirect>)
[Linux| 五.免费获得Linux系统-服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494994&idx=2&sn=0cecd945228792a6be108cca83e85779&chksm=9b3c9402ac4b1d14893b28d8618d437c0aec1ac6117154bd8ffeaac8f8f129ddefb0d4377cfb&scene=21#wechat_redirect>)
[Linux| 五.免费获得Linux系统-服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495054&idx=2&sn=13d1f8d0c6b8c974e31a355ed7b997eb&chksm=9b3c94deac4b1dc81477c239380aea22aeac952fa0495f61cd769393d165d8122c42bab830af&scene=21#wechat_redirect>)
[Linux| 六.命令行与与基本命令](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495054&idx=2&sn=13d1f8d0c6b8c974e31a355ed7b997eb&chksm=9b3c94deac4b1dc81477c239380aea22aeac952fa0495f61cd769393d165d8122c42bab830af&scene=21#wechat_redirect>)
[Linux| 七.获取Linux命令帮助的几种方式](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495054&idx=1&sn=1a418b6877f7d8905902abe7f73ebf7a&chksm=9b3c94deac4b1dc8e1da4756108994ba6f4e0e385385df21d8fbc5a0947edef369592b9b1d3a&scene=21#wechat_redirect>)
[Linux| 八.Linux的文件目录系统](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496291&idx=2&sn=1813f6615aa2f5a8598851f43bfdafbf&chksm=9b3c8b33ac4b0225b397b56465d559ae80c1d6cc1ab6135bb12153b9beaa04ff1e0ca1ec4402&scene=21#wechat_redirect>)
[Linux| 九.路径查看与切换: pwd,cd,ls命令](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496291&idx=1&sn=e4afc3656c82173ff5ec8fa6b39c9d9f&chksm=9b3c8b33ac4b0225a50550199bb85c025667b2c104af270812e2baa81577789308572ac4da23&scene=21#wechat_redirect>)
[Linux| 十.通配符](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496442&idx=1&sn=3a60951daf331f134f2959b3e654d085&chksm=9b3c8baaac4b02bc952d526e498861efa4fabf0eb8fbdf6b7f291c7e80d0105aaff454323ccb&scene=21#wechat_redirect>)
[Linux| 11.文件删除: rm命令](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496527&idx=1&sn=fe8eec0be5994a08496bf41d803abeb9&chksm=9b3c8a1fac4b030974c5c1bdc8ccd18cb96ba6e23c5aea29fe30353db0b433294d9952d765c1&scene=21#wechat_redirect>)
[Linux| 12.文件的复制(cp)与移动(mv)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496599&idx=1&sn=648b97b3ffc0e7d37faf8b71f7ba2a8e&chksm=9b3c8ac7ac4b03d11c0bc81aa4c411d6bdad34e4c07cad476c792938844ae2d4e76e1c979c54&scene=21#wechat_redirect>)
[Linux| 13.用户与组群概念](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496613&idx=1&sn=463621761f8ebb28ae229c7a4eff809a&chksm=9b3c8af5ac4b03e37a3e959617a49fb0e7304b042dbd7a548cda620c682013632214e41ae911&scene=21#wechat_redirect>)
[Linux| 14.用户管理命令(useradd, passwd, userdel, su)](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496892&idx=1&sn=960dbca843a51a73c1b331abee5c127d&chksm=9b3c8decac4b04fa3fb1fec375e6c6950f277f6c128c9decf5c38a689086ef798f519cd10acd&scene=21#wechat_redirect>)
[Linux| 15.文件权限管理: chown, chmod](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496931&idx=1&sn=392e2b97f850374c96de50194b95bfbf&chksm=9b3c8db3ac4b04a5ddc57970bcb36f64587725d1ddcd9bec12e0902953483eeec314a5f4a3aa&scene=21#wechat_redirect>)
[Linux| 16.快捷键](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497180&idx=1&sn=e4d998d9c9d5a7672cba67654f7e8c1c&chksm=9b3c8c8cac4b059abd73e1e026f5d705d1bd2f25883b462cb09bdc72f140fe2727f93abb0c1f&scene=21#wechat_redirect>)
[Linux| 17.输出重定向](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497255&idx=1&sn=304d5492738068f33d377317c31bf75b&chksm=9b3c8f77ac4b0661a7e4306071f129f06a2ca680caeecaa9d6af1f24720170d9e1fa3a371de1&scene=21#wechat_redirect>)
[Linux| 18.管道符](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497261&idx=1&sn=8d4177937f7ff4ee7db2eb9a59878af9&chksm=9b3c8f7dac4b066b7ce3dd9f815d631bc43c8d7115c508c88c1b8038b2a5af5b6cfde6734148&scene=21#wechat_redirect>)
[Linux| 19.文件查找 find, locate, which](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497743&idx=1&sn=f8e9fda7d325262f129a80faf77217dd&chksm=9b3c815fac4b0849c12cfb926cef2eaed8e0c779cb50c92647c48230b99492dc12aed135e03f&scene=21#wechat_redirect>)
[Linux| 20.别名 alias](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498050&idx=1&sn=9f29a0c594743a6cd0ce2b2beaaef037&chksm=9b3c8012ac4b0904666979588c25b2025eded47d5f05885f9101d7d0e81a96d8feeff837859c&scene=21#wechat_redirect>)
[Linux| 21.软链接与硬链接ln](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498073&idx=1&sn=658f9059b05cc2859deb3cd4f2b5df4b&chksm=9b3c8009ac4b091f9baea3f3ca640b138358edd768d906703004323622516c7af7fedb72c446&scene=21#wechat_redirect>)
[Linux| 22. (解)压缩与md5值校验](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499664&idx=1&sn=4864161942d45fedee2fa28e6d85460e&chksm=9b3c86c0ac4b0fd67ff1798290f95695b8284943d468aaa9ae2db38fe79927ef47dd7d73f7f6&scene=21#wechat_redirect>)
[Linux| 23. 文件查看 wc, cat, head, tail](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500401&idx=1&sn=e4270e426c7e1dcbc55ce9320955c21a&chksm=9b3cbb21ac4b3237b1be87b1ea466584fd996c18564b50b65a6ff7e66d0732530b0bf5e006eb&scene=21#wechat_redirect>)
[Linux| 24. 文件浏览器 more,less](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500554&idx=2&sn=3d20b135ac7f78500d439beac16f2067&chksm=9b3cba5aac4b334c89ad2b040b90f291118072bf3a6ee566591b42920163a965f3095e41a4e4&scene=21#wechat_redirect>)
[Linux| 25. 文件编辑器 vim](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500900&idx=1&sn=f8e41737d22588beaeb6cfeea8865a7d&chksm=9b3cbd34ac4b3422ded73466e862117a5b4989eb0ca2125f2c1f45b67f9ca3772d40a1bb6835&scene=21#wechat_redirect>)
[Linux| 26. 文件处理 cut, paste](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501934&idx=1&sn=2f942aef95ba543a5bf0226b0c7301bf&chksm=9b3cb13eac4b382838329a8519730347602e993374b063e7abafcecb7b2f476eedae6c9dd9bb&scene=21#wechat_redirect>)
[Linux| 27. 文件处理 sort, uniq](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502039&idx=1&sn=8e92a5f845315b6fd2c0d229aa606d17&chksm=9b3cb187ac4b3891b9e94b1e4cd3849975db7461291a1d905f28b1751619803fc89e335d9a83&scene=21#wechat_redirect>)
[Linux| 28. 正则表达式](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502156&idx=1&sn=b006d7cb09cd38eb754ad3f8d111fa1b&chksm=9b3cb01cac4b390a5f05a3f51d0c932f35c9d5d7b23e6aa8939f60a558bf2396fb3cbffa0191&scene=21#wechat_redirect>)
[Linux| 29. 文本处理 grep](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502360&idx=1&sn=e143be1043640ce47528d17eed784984&chksm=9b3cb348ac4b3a5e69b14b072b8ba828f0cabddf42aa3a7140198c631df19d99c4eef39e6be6&scene=21#wechat_redirect>)
[Linux| 30. 文本处理 sed命令](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502411&idx=1&sn=f4c9ecd855a6c75f620630f710f5a120&chksm=9b3cb31bac4b3a0d89fccf39154c74f548f3b1b3144f58c808b5c400aec645bff64eea8ae16c&scene=21#wechat_redirect>)
[Linux| 31. 文本处理 awk命令](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502424&idx=1&sn=6ff93ae4974eec7547e2e4f0f0b139fc&chksm=9b3cb308ac4b3a1e4a06a3216ea1c351e96705136241a0e6a496d472ce29ffe0a633353d9e0b&scene=21#wechat_redirect>)
[Linux| 32. shell脚本](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503080&idx=1&sn=88ed8835cf877156f9089fc37795b62d&chksm=9b3cb5b8ac4b3caee6ee8b28c08a748eb4eac1ac2e63b13343053efe039363589c2483b219cd&scene=21#wechat_redirect>)
[Linux| 33. shell变量](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503099&idx=1&sn=27c083d71a28820be6ffb1333a97898c&chksm=9b3cb5abac4b3cbdb73077aa1976e2afbae8656ea642942f1e0f60d11032f68d8b1e0cc7b8d4&scene=21#wechat_redirect>)
[Linux| 34. if条件语句](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503140&idx=1&sn=60c5f1b1315245d9a9a2d3f30c16c8d5&chksm=9b3cb474ac4b3d62c05300945e1a1fdc0af0c0c5af72fce7eee752fb20d2e99c6e0ca3033d6b&scene=21#wechat_redirect>)
[Linux| 35. 循环](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503144&idx=1&sn=9dce6d9c0f8ae56c0ceee545b480e76e&chksm=9b3cb478ac4b3d6e497f480a15545e09b0dbabfdccd2a8ed82741dd3a984994512287177ef4d&token=478412110&lang=zh_CN&scene=21#wechat_redirect>)

### 2.2.3 R语言教程

持续更新中，敬请期待：[生信R语言保姆级教程](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3083225482621648898#wechat_redirect>)

### 2.2.4 服务器准备

下列教程实测至少需要`4核`以及`60GB`的内存，如果自己电脑不满足计算要求的同学可以参考以下内容：
[生信分析为什么要使用服务器？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501099&idx=1&sn=78446147184292fad3417495926b3096&chksm=9b3cbc7bac4b356dcf0460781f9bf16df4ede481f8cc57282c7384b9d2baccaa820d64c89bab&scene=21&cur_album_id=2725521219349151745#wechat_redirect>)
[独享服务器，满足你对生信分析的所有幻想](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500111&idx=1&sn=1dfc668263614efb82e0659af5fcd438&chksm=9b3cb81fac4b3109a8e19a09cc68122b1943dcd45c653627e77dfa47d476280079ea6a8dd63d&scene=21&cur_album_id=2725521219349151745&poc_token=HFu97mSj9hyBWmQKH3wMhmeWBGYtExlTp_Trdwn6#wechat_redirect>)
[为实验室准备一份生物信息学不动产](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247502932&idx=1&sn=401d384d47616029375224b2d0a3c933&chksm=9b3cb504ac4b3c1299aac5c9f0747ccc36777390d2a939e1ed4af37c2836c1f7e8b4af612989&scene=21&cur_album_id=2725521219349151745#wechat_redirect>)

## 2.3 依赖工具下载

### 2.3.1 `conda`与`mamba`

```bash
# 下载Anaconda：
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh
# 安装：
bash Anaconda3-5.3.1-Linux-x86_64.sh
# 疯狂按回车，遇到询问输出yes，注意vs code安装询问选择no

# 利用conda安装mamba，后者与前者功能相同，但运行速度更快：
conda install mamba
```

### 2.3.2 `gffread`

用于后面的`gff`文件转`gtf`文件，用`mamba`装起来很方便

```bash
# 一行搞定:
mamba install gffread

# 当然你也可以自行从github抓取并安装：
# 安装gffread
# 下载文件：
git clone https://github.com/gpertea/gffread
# 切换工作路径：
cd gffread
# 编译安装：
make release
# 切换工作路径：
cd ../
```

### 2.3.3 `annovar`安装及库文件下载

```bash
# annovar下载配置：
wget http://www.openbioinformatics.org/annovar/download/0wgxR2rIVP/annovar.latest.tar.gz
# 以上链接可能会失效，如失效可在百度云盘中下载：https://pan.baidu.com/s/1bWbNbOrXHUpeu0qSJv49ig?pwd=ptey

# 解压：
tar -xvf annovar.latest.tar.gz

# 切换工作路径：
cd annovar

# 大约花费一个小时，具体取决于机器硬件配置与网速：
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar refGene humandb/
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar gnomad312_genome humandb/
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar exac03 humandb/
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar avsnp150 humandb/
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar 1000g2015aug humandb/
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar clinvar_20220320 humandb/
perl annotate_variation.pl -buildver hg38 --downdb --webfrom annovar cosmic70 humandb/

# 更改文件名，方便后续mut模块调用：
mv hg38_gnomad312_genome.txt hg38_gnomad.txt
mv hg38_clinvar_20220320.txt hg38_clinvar.txt
mv hg38_cosmic70.txt hg38_cosmic.txt
mv hg38_avsnp150.txt hg38_avsnp.txt
mv hg38_exac03.txt  hg38_exac.txt

# 将annovar路径添加致配置文件中：
echo "export PATH=/home/biomamba/analysis/xunyin/annovar:$PATH" >> ~/.bashrc
source ~/.bashrc
```

### 2.3.4 `fastp`下载安装

`fastp`用于原始`fastq`文件过滤生成`clean fastq`

```bash
# 下载：
wget http://opengene.org/fastp/fastp
# 无需安装，赋予运行权限即可
chmod a+x ./fastp
```

## 2.4 `SeekSoul®Tools`下载与安装

本手册用到的所有资料均可在文末领取

当前教程演示的是seeksoultools 1.0 版本制作

seeksoul tools 软件由**寻因生物公司** 负责开发和维护，更新版本的seeksoul tools 软件见http://seeksoul.seekgene.com/

```bash
# 下载上述软件后，在Linux终端中进行安装

# 创建文件夹：
mkdir -p seeksoultools
# 切换工作目录
cd seeksoultools

# 解压
tar zxf seeksoultools_fast_mut_dev.tar.gz

# 激活seeksoultools环境
source seeksoultools/bin/activate

# 利用conda配置软件
seeksoultools/bin/conda-unpack

# 将文件安装地址配置到环境变量PATH中：
export PATH=`pwd`/seeksoultools/bin:$PATH

# 将配置写入~/.bashrc，这样每次登入服务器时均会生效
echo "export PATH=$(pwd)/seeksoultools/bin:\$PATH" >> ~/.bashrc

# 安装起来总体比较智能，上述步骤没报错即为成功

# 所以，我的工作路径在：
cd /home/biomamba/analysis/xunyin/
```

## 2.5 参考基因组下载及索引构建

```bash
# 创建文件夹：
mkdir my_refference

# 切换工作目录：
cd my_refference
```

下文教程为人类来源细胞系数据，因此我们以人类参考基因组的两个版本`GRCh38`与`hg38`为例。

### 2.5.1 `GRCh38`

这一步，你可以选择直接下载构建好的参考基因组，或者自行构建

#### (1) 直接下载

```bash
# wget下载：
wget -c -O GRCh38.tar.gz "https://seekgene-public.oss-cn-beijing.aliyuncs.com/software/data/reference/GRCh38.tar.gz"
# 解压：
tar -zxvf GRCh38.tar.gz

# 或者通过curl下载：
curl -C - -o GRCh38.tar.gz "https://seekgene-public.oss-cn-beijing.aliyuncs.com/software/data/reference/GRCh38.tar.gz"
# 解压
tar -zxvf GRCh38.tar.gz
```

#### (2) 自行构建

```bash
# 下载GRCh38基因组fatsq文件：
wget https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz
# 下载GRCh38基因组gff注释文件：
wget https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.gff.gz

gunzip ./*gz

# 将gff文件转换为gtf文件：
gffread  GRCh38_latest_genomic.gff -T -o GRCh38_latest_genomic.gtf

# 运行STAR构建基因组索引，我的机器上大约花费1.5h，具体时长需要取决于你的硬件条件：
nohup STAR \
--runMode genomeGenerate \
--genomeDir /home/biomamba/analysis/xunyin/seeksoultools/my_refference/GRCh38_index \ # 基因组索引输出路径
--genomeFastaFiles /home/biomamba/analysis/xunyin/seeksoultools/my_refference/GRCh38_latest_genomic.fna \ # 基因组fastq文件
--sjdbGTFfile /home/biomamba/analysis/xunyin/seeksoultools/my_refference/GRCh38_latest_genomic.gtf \ # 基因组注释gtf文件地址
--sjdbOverhang 149 \  # 读段长度，PE150则填149
--runThreadN 8 & # 并行计算调用的线程数

# 构建好后待后续调用
```

### 2.5.2 `hg38`

```bash
### hg38 ####
# 创建目录：
mkdir /home/biomamba/analysis/xunyin/seeksoultools/my_refference/hg38/
# 更改工作路径：
cd hg38
# 我的机器花费五分钟，主要取决于网速：
wget --timestamping  'ftp://hgdownload.cse.ucsc.edu/goldenPath/hg38/chromosomes/*'

# 解压
gunzip ./*gz

# 合并fastq文件：
cat ./*fa > hg38.fa

# 下载基因组注释gtf文件：
wget https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/genes/hg38.refGene.gtf.gz
# 解压：
gunzip hg38.refGene.gtf.gz

# 运行STAR构建索引：
nohup STAR \
--runMode genomeGenerate \
--genomeDir /home/biomamba/analysis/xunyin/seeksoultools/my_refference/hg38/hg38_index \
--genomeFastaFiles /home/biomamba/analysis/xunyin/seeksoultools/my_refference/hg38/hg38.fa \
--sjdbGTFfile /home/biomamba/analysis/xunyin/seeksoultools/my_refference/hg38/hg38.refGene.gtf \
--sjdbOverhang 149 \
--runThreadN 8 &
```

### 2.5.3 `rRNA`基因组索引

```bash
# rRNA基因组
wget -c -O hg38_rRNA.tar "https://seekgene-public.oss-cn-beijing.aliyuncs.com/software/data/reference/hg38_rRNA.tar.gz"
# 解压
tar -zxvf hg38_rRNA.tar
```

**三、fast模块**

![](../../images/1189c1178040d051.png)

##  本节视频教程可见B站(文末阅读原文可直接跳转)：

https://www.bilibili.com/video/BV1F94y1879j?p=3

## 3.1 `rna`模块说明

### 3.1.1 算法及流程说明

当前教程基于seeksoultools 1.0 版本制作

**seeksoul tools** 软件由**寻因生物公司** 负责开发和维护，更新版本的**seeksoul tools** 软件见http://seeksoul.seekgene.com/

`rna`模块：用于识别细胞标签`barcode`，比对定量，得到可用于下游分析的细胞表达矩阵，之后进行细胞聚类和差异分析，该模块不仅支持`SeekOne`系列试剂盒产出数据，还可通过对`barcode`的描述，支持多种自定义设计结构。

  * Step1: barcode/umi提取
seeksoultools可以根据不同的R1结构设计和每种结构的不同的参数对barcode/umi提取和处理，对R1以及对应的R2进行过滤，生成新的R2文件。

 _结构描述，以下的两种R1结构为例：_ `MM: B8L8B8L10B8U8`（错位设计)
`DDV2: B17U12`

```
B表示barcode部分碱基；
L表示linker部分碱基；
U表示umi部分碱基；
X表示任意碱基，用于占位；
字母后数字表示碱基长度。
```

 _错位设计的Anchor定位_
有些设计下，为了使测序`reads`碱基多样性，加入了`1-4bp`的移码碱基，即`anchor`；`anchor`决定了`barcode`的起始位置。`seeksoultools`尝试在`R1`序列前7个碱基中寻找`Anchor`序列，若没找`到anchor`序列，此条`read`以及对应的R2被认为是无效`read`。

 _Barcode和Linker矫正_
`Barcode`序列有一定几率发生测序错误的情况，在提供有白名单的情况下，`seeksoultools`可以实现`barcode`矫正功能。当`barcode`存在于白名单中时，我们认为它是有效的`barcode`，统计有效`barcode`对应的`reads`数量。当`barcode`不存在于白名单中时，我们认为它是无效的`barcode`。在开启矫正功能时，当无效`barcode`一个碱基错配（一个`hamming distance`）的序列存在于白名单中，我们会进行以下几种处理：

只有唯一一个序列存在于白名单中：我们将这个无效`barcode`矫正为白名单中`barcode`。

有多个序列存在于白名单中，且有至少一个序列`的read`支持数 _大于0_ ：

如果只有一个序列的`read`支持数大于0，我们将这个 _无效_`barcode` 改为这个序列且保留这条`read`。如果有多个序列的`read` 支持数大于0，我们将这个无效barcode 改为read支持数量最多的序列。其余情况：这条read以及对应的R2为 _无效_ read。

`Linker`的处理与`Barcode`相同。

 _接头和PolyA序列剪切_ 在转录组产品中，`Read2`的末端有可能会出现`polyA` `tail`或建库时引入的接头序列。这些序列并没有有效信息。为了节省计算时间和复杂度，我们要这些序列进行切除。剪切完的`read2`长度需要大于设定的最小长度来保证有足够的信息，准确比对到基因组的位置。如果剪切完成后的`read2`长度小于最小长度，我们认为这条`read`为无效`read`。

 _指标统计_
![](../../images/aacbfb49394ba3af.png)

```
total: 总共的reads数目
valid: 不需要矫正和矫正成功的reads数目
B_corrected: 矫正成功的reads数目
B_no_correction: 错误Barcode的reads数目
L_no_correction: 错误Linker的reads数目
no_anchor：不包含anchor的reads数目
trimmed: 进行过剪切的reads数目
too_short: 进行过剪切后长度小于60bp的reads数目
```

指标之间的关系如下：
total = valid + no_anchor + B_no_correction + L_no_correction
输出fastq的reads数：total_output = valid - too_short

  * Step2: 进行比对并找到比对基因
 _序列比对_
使用`STAR`比对软件将处理后的`R2`比对到参考基因组上。使用`qualimap`软件和转录本注释文件`GTF`，统计`reads`比对外显子、内含子和基因间区等的比例。使用`featuresCounts`将比对上的`read`注释到基因上，可以选择不同的注释规则，如链方向性和定量的feature。当使用外显子定量时，当`read`超过`50%`碱基比对到外显子区域时，认为该`read`来源于此外显子以及外显子对应的基因；当使用转录本定量时，当`read`超过`50%`碱基比对到转录本区域时，认为该`read`来源于此转录本以及转录本对应的基因。

 _指标统计_

Hide
```
Reads Mapped to Genome: 能比对到参考基因组上的reads占所有reads的比例（包括只有一个比对位置和多个比对位置的reads）
Reads Mapped Confidently to Genome: 在参考基因组上只有一个比对位置的reads占所有reads的比例
Reads Mapped to Intergenic Regions：比对到基因间隔区reads占所有reads的比例
Reads Mapped to Intronic Regions：比对到内含子reads占所有reads的比例
Reads Mapped to Exonic Regions：比对到外显子reads占所有reads的比例
```

  * Step3: 定量
 _UMI 定量_
为了得到每个`barcode`下基因的表达数据，`seeksoultools`以`barcode`为单位提取`featureCounts`输出的`bam`数据，统计注释到基因的`umi`和`umi`对应的`reads`数：

过滤掉对应`UMI`为单个重复碱基的`reads`， 例如`UMI`为`TTTTTTTT` 过滤掉注释到多个基因的`reads`

 _UMI矫正_
`UMI`序列也有一定概率出现测序错误的情况。`seeksoultools`会尝试对`UMI`进行矫正。当同一个`barcode`中的某一个特定基因对应有两个`UMI`序列只有一个碱基错配时（一个`hamming distance`），`reads`支持数低的`UMI`将被纠正为`reads`支持数高的`UMI`。

 _细胞判定_
在一个细胞群中，我们认为细胞和细胞的`mRNA`的含量不会相差太多。如果一个`barcode`对应的`mRNA`的含量很低，我们认为这个`barcode`的磁珠并没有捕获细胞，`mRNA`来源于背景。 `seeksoultools` 会以上面的规则，进行`barcode`是否为细胞的判定。有以下几个步骤：

对所有`barcode`按照对应的`UMI`数由高到低排序；取预估细胞的`1%`位置的`barcode`的`UMI`数除以`10`为阈值； `barcode`的`UMI`数大于阈值的判定为细胞； `barocde`的`UMI`小于阈值，但大于`300`时，使用`DropletUtils`分析。`DropletUtils`方法先假设UMI数量低于`100`的`barcode`为`empty` `droplet`，然后根据每个`droplet`相同基因的`UMI`数总和为背景`RNA`表达谱中该基因`UMI`数目，进而得到基因`UMI`数目的期望值。再通过将每个`barcode`的`UMI`数进行统计学检验，显著差异的为细胞；不符合上述条件的为背景。

 _指标统计_

```
Estimated Number of Cells：判定的细胞总数
Fraction Reads in Cells: 判定为细胞的reads占所有参与定量的reads的比例
Mean Reads per Cell: 细胞的平均reads数，总reads数/判定的细胞数
Median Genes per Cell: 判定为细胞的barcode对应genes的中位数
Median UMI Counts per Cell: 判定为细胞的barcode对应UMI的中位数
Total Genes Detected: 所有细胞检测到基因数量
Sequencing Saturation: 饱和度，1 - UMI总数/reads总数
```

  * Step4: 后续分析
得到表达矩阵后，我们可以进行下一步的分析。

`Seurat`分析流程 使用`Seurat`计算线粒体含量，细胞中`UMI`总数，细胞中基因总数。之后对矩阵进行归一化、寻找高变基因、降维聚类之后寻找差异基因。当然，我们也会在下面的教程中给大家详解`Seurat`运行过程。

## 3.2 `fast`模块说明

`fast`模块的参数、结果以及算法绝大部分与`rna`模块一致，有如下几点区别 1、`fast`针对全序列数据，保留了`reads1`去除`barcodeUMI`等部分后的数据，进行双端比对，并基于此结果后续进行分析 2、`fast`中增加了一些全序列数据特有指标：（1）核糖体含量 （2）以及数据`biotype`占比饼图: （3）`genebody`图及`ACTB`覆盖度；（4）`lnc`基因数量

## 3.3 `fast`模块使用

### 3.3.1 `rna`模块参数

`rna`模块中的大部分参数在`fast`模块中同样适用，因此需要先掌握此部分内容：

  * \--fq1
R1 fastq数据路径。

  * \--fq2
R2 fastq数据路径。

  * \--samplename
样本名称，会在outdir目录下创建以样本名称命名的目录。仅支持数字，字母和下划线。

  * \--outdir
结果输出目录。默认值：./。

  * \--genomeDir
`STAR`构建的参考基因组路径, 版本需要与`seeksoultools`使用的STAR一致。

  * \--gtf
相应物种的gtf路径。

  * \--core
分析使用的线程数。

  * \--chemistry
试剂类型，每种对应一组`--shift`、`--pattern`、 `--structure`、`--barcode`和`--sc5p`的组合，可选值：`DDV1`，`DDV2`，`DD5V1`，`MM`，`MM-D`，`DD-Q`； `DDV1` 对应DD平台3’转录组V1版本试剂； `DDV2` 对应DD平台3‘转录组V2版本试剂； `DD5V1` 对应DD平台5‘转录组V1版本试剂； `MM` 对应MM平台3’转录组数据； `MM-D` 对应MM大孔径； `DD-Q` 对应DD全序列。

  * \--shift
使用移码设计。

  * \--pattern
移码设计设计中用于锚定起始的碱基。

  * \--structure
⽤于描述`read1`的接头结构，B表示`cellbarcode`，`L`表示`linker`，`U`表示`UMI`，后⾯数字表示碱基⻓度，⽐如`B9L12B9L13B9U8`；如果是`P3CBGB`类的结构，只有`barcode`和`UMI`，没有`linker`，`structure`参数就是`B17U12`。

  * \--barcode
`barcode`文件路径。

  * \--linker
`linker`文件路径。

  * \--skip_misB
`barcode`不允许碱基错配，默认允许一个碱基错配。

  * \--skip_misL
`linker`不允许碱基错配，默认允许一个碱基错配。

  * \--skip_multi
舍弃能纠错为多个白名单`barocde`的`reads`，默认纠错为比例最高的`barcode`。

  * \--sc5p
不启用时，分析5’转录组；启用时，分析5’转录组需。

  * \--expectNum
预估的捕获细胞数目。

  * \--forceCell
当正常分析得到的细胞数⽬不理想时，选⽤此参数，后⾯加⼀个预期的数值`N`，`seeksoultools`软件会按照`UMI`从⾼到低取前`N`个细胞。

  * \--include-introns
不启用时，只会选择`exon reads`⽤于定量；启用时，`intron reads`也会⽤于定量。

  * \--star_path
指定其他版本的`STAR`路径进行比对，版本需要与`--genomeDir`版本兼容，默认的`--star_path`为环境下的`STAR`。

### 3.3.2 `fast`模块使用实战

(1)`fastp`指控原始`fastq`数据
我们采用`trim`的方式截去测序数据的测序接头和低质量片段，从而高效地利用测序数据，后续分析都基于`clean data`。在进行原始数据`Trimming`时我们使用 `fastp`软件（ Chen S，et al. 2018），处理具体如下：①截去低质量`reads`，使用滑动窗口的方式，`4`个碱基为一个窗口，若该窗口的平均碱基质量值低于`10`，则从该处截去`reads`， 参数选择：`–cut_front`, `–cut_front_window_size 4`, `–cut_front_mean_quality 10`；②截去 `reads` 尾部质量低于3或者含N（N 表示无法确定碱基信息）的 `reads`，参数选择: `–cut_tail`, `–cut_tail_window_size 1`, `–cut_tail_mean_quality`；③截去接头序列（`–detect_adapter_for_pe` ）；④经上述处理后，过滤掉短于 `60 bp`的 `reads`，及其`paired reads`。 `-l` or `--length_required` 60 双端测序需要加上： `--detect_adapter_for_pe`

```
fastp -i cellline_test/cellline_R1_001.fastq.gz -I cellline_test/cellline_R2_001.fastq.gz \
-o cellline_test/cellline_R1_001.clean.fastq.gz -O cellline_test/cellline_R2_001.clean.fastq.gz \
--cut_front –-cut_front_window_size 4 --cut_front_mean_quality 10 \
--cut_tail –-cut_tail_window_size 1 –-cut_tail_mean_quality \
--length_required 60 --detect_adapter_for_pe

# 运行提示：
# Detecting adapter sequence for read1...
# No adapter detected for read1
#
# Detecting adapter sequence for read2...
# >Illumina TruSeq Adapter Read 2
# AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
#
# Read1 before filtering:
#   total reads: 18714992
# total bases: 2807248800
# Q20 bases: 2751519892(98.0148%)
# Q30 bases: 2642338596(94.1256%)
#
# Read2 before filtering:
#   total reads: 18714992
# total bases: 2807248800
# Q20 bases: 2693483677(95.9475%)
# Q30 bases: 2530358229(90.1366%)
#
# Read1 after filtering:
#   total reads: 18471287
# total bases: 2760865206
# Q20 bases: 2708982515(98.1208%)
# Q30 bases: 2602928318(94.2794%)
#
# Read2 after filtering:
#   total reads: 18471287
# total bases: 2759509560
# Q20 bases: 2667685071(96.6724%)
# Q30 bases: 2511042682(90.996%)
#
# Filtering result:
#   reads passed filter: 36942574
# reads failed due to low quality: 454502
# reads failed due to too many N: 222
# reads failed due to too short: 32686
# reads with adapter trimmed: 1054560
# bases trimmed due to adapters: 18837617
#
# Duplication rate: 14.048%
#
# Insert size peak (evaluated by paired-end reads): 224
#
# JSON report: fastp.json
# HTML report: fastp.html
#
# fastp -i cellline_test/cellline_R1_001.fastq.gz -I cellline_test/cellline_R2_001.fastq.gz -o cellline_test/cellline_R1_001.clean.fastq.gz -O cellline_test/cellline_R2_001.clean.fastq.gz --cut_front –-cut_front_window_size 4 --cut_front_mean_quality 10 --cut_tail –-cut_tail_window_size 1 –-cut_tail_mean_quality --length_required 60 --detect_adapter_for_pe
# fastp v0.23.4, time used: 157 seconds
```

(2)`fast`模块

```
seeksoultools fast run \
--fq1 /home/biomamba/analysis/xunyin/test_data/cellline_test/cellline_R1_001.clean.fastq.gz \
--fq2 /home/biomamba/analysis/xunyin/test_data/cellline_test/cellline_R2_001.clean.fastq.gz \
--samplename cellline \
--outdir /home/biomamba/analysis/xunyin/cellline_out \
--genomeDir /home/biomamba/analysis/xunyin/seek_ref/GRCh38/star \
--gtf /home/biomamba/analysis/xunyin/seek_ref/GRCh38/genes/genes.gtf \
--include_introns  \
--rRNAgenomeDir /home/biomamba/analysis/xunyin/seek_ref/hg38_rRNA/star \
--rRNAgtf /home/biomamba/analysis/xunyin/seek_ref/hg38_rRNA/genes/delete_rRNA5.8-18-28_in_rRNA45s.gtf \
--core 8
```

输出目录下包含以下文件：
/home/biomamba/analysis/xunyin/cellline_out
├── cellline_report.html
├── cellline_summary.csv
├── cellline_summary.json
├── step1
│ ├── cellline_1.fq.gz
│ ├── cellline_2.fq.gz
│ ├── cellline.cutTSO_1.fq.gz
│ ├── cellline.cutTSO_2.fq.gz
│ └── cellline_stat.fq.gz
├── step2
│ ├── featureCounts
│ │ ├── cellline_SortedByCoordinate.bam.featureCounts.bam
│ │ ├── cellline_SortedByName.bam
│ │ ├── counts.txt
│ │ └── counts.txt.summary
│ └── STAR
│ ├── cellline_Aligned.out.bam
│ ├── cellline_Log.final.out
│ ├── cellline_Log.out
│ ├── cellline_Log.progress.out
│ ├── cellline_SJ.out.tab
│ ├── cellline_SortedByCoordinate.bam
│ ├── cellline_SortedByCoordinate.bam.bai
│ ├── cellline_SortedByName.bam
│ ├── downbam
│ │ ├── cellline.down.0.1.bam
│ │ ├── cellline.down.0.1.bam.bai
│ │ ├── cellline.geneBodyCoverage.curves.pdf
│ │ ├── cellline.geneBodyCoverage.r
│ │ └── cellline.geneBodyCoverage.txt
│ ├── report.pdf
│ ├── rnaseq_qc_results.txt
│ └── rRNA
│ ├── cellline_Aligned.out.bam
│ ├── cellline_Log.final.out
│ ├── cellline_Log.out
│ ├── cellline_Log.progress.out
│ ├── cellline_SJ.out.tab
│ ├── cellline_SortedByName.bam
│ ├── cellline.xls
│ ├── counts.txt
│ ├── counts.txt.summary
│ ├── test.input.1.fq.gz
│ └── test.input.2.fq.gz
├── step3
│ ├── counts.xls
│ ├── detail.xls
│ ├── filtered_feature_bc_matrix
│ │ ├── barcodes.tsv.gz
│ │ ├── features.tsv.gz
│ │ └── matrix.mtx.gz
│ ├── filtered_feature_bc_matrix_
│ │ ├── barcodes.tsv.gz
│ │ ├── features.tsv.gz
│ │ └── matrix.mtx.gz
│ ├── fragment.xls
│ ├── raw_feature_bc_matrix
│ │ ├── barcodes.tsv.gz
│ │ ├── features.tsv.gz
│ │ └── matrix.mtx.gz
│ └── umi.xls
└── step4
├── biotype_FindAllMarkers.xls
├── cellline.rds
├── FeatureScatter.png
├── FindAllMarkers.xls
├── lncgene_FindAllMarkers.xls
├── mito_quantile.xls
├── nCount_quantile.xls
├── nFeature_quantile.xls
├── resolution.xls
├── top10_heatmap.png
├── tsne.png
├── tsne_umi.png
├── tsne_umi.xls
├── umap.png
└── VlnPlot.png

11 directories, 66 files

**
**

**四、Seurat分析及可视化**

![](../../images/1189c1178040d051.png)

`Seurat`可谓是单细胞数据分析及可视化的神包，利用R语言分析单细胞不可不学的利器。这部分内容阅读有障碍的同学可以查看以下我们以往的教程：

[scRNA-Seq学习手册2023_R语言版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500516&idx=1&sn=3c0b9de505fcd232054e38b451fa1742&chksm=9b3cbbb4ac4b32a26b61f3a1f7941fff5852d3e6e744ec680aafd0b84ec976a33bf982fb5f79&payreadticket=HI8u17wlgTEi2y3_eAB6lLoDeKGnv0COS1AuKNQmiMChHdO8OBdB12sH68EgToXBfpGroFY&scene=21#wechat_redirect>)

#### 单细胞测序基础数据分析**保姆级教程** ，代码部分整理在往期推送之中：

[手把手教你做单细胞测序数据分析（一）——绪论](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499776&idx=2&sn=7fc250d94ed88cfd5e2224f071bb1742&chksm=9b3cb950ac4b30467a082527547b91aec15b7d1f40d44e362894aedeb6a99e014518fa5e4743&token=767842863&lang=zh_CN&scene=21#wechat_redirect>)
[手把手教你做单细胞测序数据分析（二）——各类数据结构与读取方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499795&idx=2&sn=68e6298eb43633c71939c146d90230ff&chksm=9b3cb943ac4b3055e09739d77e037d679f3d9ec68780d1aa8c592f806fcc8d2322eaee78752d&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（三）——单样本分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（四）——多样本整合](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（五）——细胞类型注释](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（六）——组间差异分析及可视化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)
[手把手教你做单细胞测序数据分析（七）——基因集富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&scene=21&cur_album_id=2923694853375688706#wechat_redirect>)

## 4.1 数据读取

```
# 设置工作目录
setwd('~/analysis/xunyin/')
# 加载R包
if (!require("Seurat", quietly = TRUE))install.packages("Seurat")
```
```
## Attaching SeuratObject
```

```
if (!require("BiocManager", quietly = TRUE))install.packages("BiocManager")
```
```
## Bioconductor version '3.15' is out-of-date; the current release version '3.17'
##   is available with R version '4.3'; see https://bioconductor.org/install
```

```
if (!require("multtest", quietly = TRUE))install.packages("multtest")
```
```
##
## Attaching package: 'BiocGenerics'
```
```
## The following objects are masked from 'package:stats':
##
##     IQR, mad, sd, var, xtabs
```
```
## The following objects are masked from 'package:base':
##
##     anyDuplicated, append, as.data.frame, basename, cbind, colnames,
##     dirname, do.call, duplicated, eval, evalq, Filter, Find, get, grep,
##     grepl, intersect, is.unsorted, lapply, Map, mapply, match, mget,
##     order, paste, pmax, pmax.int, pmin, pmin.int, Position, rank,
##     rbind, Reduce, rownames, sapply, setdiff, sort, table, tapply,
##     union, unique, unsplit, which.max, which.min
```
```
## Welcome to Bioconductor
##
##     Vignettes contain introductory material; view with
##     'browseVignettes()'. To cite Bioconductor, see
##     'citation("Biobase")', and for packages 'citation("pkgname")'.
```

```
if (!require("dplyr", quietly = TRUE))install.packages("dplyr")
```
```
##
## Attaching package: 'dplyr'
```
```
## The following object is masked from 'package:Biobase':
##
##     combine
```
```
## The following objects are masked from 'package:BiocGenerics':
##
##     combine, intersect, setdiff, union
```
```
## The following objects are masked from 'package:stats':
##
##     filter, lag
```
```
## The following objects are masked from 'package:base':
##
##     intersect, setdiff, setequal, union
```

```r
# 指定数据路径
data_dir <- "cellline_out/step3/filtered_feature_bc_matrix/"
list.files(data_dir)
```
```
## [1] "barcodes.tsv.gz" "features.tsv.gz" "matrix.mtx.gz"
```

```r
#自动读取定量数据，格式为三个tsv或mtx文件
scFAST.data <- Read10X(data.dir = data_dir)

# 创建Seurat对象并初步过滤
# min.cells表示基因至少在几个细胞中表达，min.genes代表每个细胞中至少表达多少基因，细胞的平均reads数量> 5万一般比较好，否则需要补测：
scFAST <- CreateSeuratObject(counts = scFAST.data,
                           project = "cell_line", min.cells = 3,
                           min.features = 200)
```

## 4.2 数据预处理

```r
# 通过线粒体的序列数来对数据进行计算线粒体mRNA百分比：
scFAST[["percent.mt"]] <- PercentageFeatureSet(scFAST,
                                              pattern = "^MT-") # 小鼠数据需要换为mt
# QC的数据存在meta.data里，可以用这个来查看前5行
head(scFAST@meta.data, 5)
```
```
##                   orig.ident nCount_RNA nFeature_RNA percent.mt
## CAGGCCAGCTCACAGCC  cell_line        341          281  0.5865103
## CCGGGTATACGAAGTCC  cell_line        341          285  2.9325513
## GTGTGGCGCTGTACTAC  cell_line        338          258  3.8461538
## TCAGCAACGATCCGCGA  cell_line        341          275  1.1730205
## TCCCATGTACTAGTCCT  cell_line        340          273  2.3529412
```

```
# 用小提琴图来展示QC的结果，展示了每个barcode中基因的数目、UMI数目以及线粒体基因含量的分布情况：
#pdf(file = 'Feature.Count.percent.mt.pdf',height = 6,width = 18)
VlnPlot(scFAST,
        features = c("nFeature_RNA", "nCount_RNA", "percent.mt"),
        ncol = 3)
```

![](../../images/8c037cd35a2e523d.webp)

```r
#dev.off()

# 可视化：
plot1 <- FeatureScatter(scFAST, feature1 = "nCount_RNA", feature2 = "percent.mt")
plot2 <- FeatureScatter(scFAST, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")
```

```
#pdf(file = '判断基因表达趋势.pdf',width = 12,height = 6)
CombinePlots(plots = list(plot1, plot2)) #高变基因，判断趋势及占比
```
```
## Warning: CombinePlots is being deprecated. Plots should now be combined using
## the patchwork system.
```

![](../../images/37534b6be2506e37.webp)

```
#dev.off()
```

```r
# 质控，选子集，RNA数量在200与2500之间的，多的可能是低质量细胞或空drouplets，gene count多的可能是doublets or multiplets:
scFAST <- subset(scFAST, subset = nFeature_RNA > 200 &
                  nFeature_RNA < 2500 & percent.mt < 5)

# 用LogNormalize法对数据进行标准化（乘10000再取对数）数据存在scFAST[["RNA"]]@data.里
# 默认的方法也完成了log1p的操作，得到的结果就类似于TPM的对数:
scFAST <- NormalizeData(scFAST, normalization.method = "LogNormalize",
                       scale.factor = 10000)

# 筛选高变基因（输出2000个），用于下游的PCA及分群:
scFAST <- FindVariableFeatures(scFAST, selection.method = "vst",
                              nfeatures = 2000)

# 输出差异最大的十个基因:
top10 <- head(VariableFeatures(scFAST), 10)
plot1 <- VariableFeaturePlot(scFAST)
plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)
```
```
## When using repel, set xnudge and ynudge to 0 for optimal results
```

```
#输出差异基因散点图（有无标签）:
CombinePlots(plots = list(plot1, plot2))
```
```
## Warning: CombinePlots is being deprecated. Plots should now be combined using
## the patchwork system.
```

![](../../images/b4b881fe5c615beb.webp)

```r
# 将数据进行归一化，为后续的PCA分析做准备，数据存在scFAST[["RNA"]]@scale.data
scFAST <- ScaleData(scFAST, features =  rownames(scFAST))
```
```
## Centering and scaling data matrix
```

```r
#scFAST <- ScaleData(scFAST)#only4VariableFeatures

# 回归计算消除无关的变量（如线粒体的比例）：
scFAST <- ScaleData(scFAST, vars.to.regress = "percent.mt")
```
```
## Regressing out percent.mt
```
```
## Centering and scaling data matrix
```

```r
#scFAST[["RNA"]]@scale.data

# PCA降维分析：
scFAST <- RunPCA(scFAST,
                features = VariableFeatures(object = scFAST))
```
```
## PC_ 1
## Positive:  HBG2, HBG1, PRAME, CPED1, AL713998.1, GLUL, KCNH2, MPP1, PRKCB, RELN
##     AC136431.1, LINC01287, CBFA2T3, FAM178B, NUP214, AC004949.1, AP000547.3, ANK1, AC097528.1, RHAG
##     LYL1, LINC02476, ALDH1A2, CTCFL, SEPTIN5, GYPC, EPB41, AP001531.1, ZEB2, GATA1
## Negative:  ASPH, EGFR, LCN2, KRT18, GAPDH, IGFBP3, CD44, VOPP1, KRT8, JUN
##     LPP, NFKBIZ, SAA1, S100A10, CFB, AREG, CDH1, CDK4, EGR1, PGK1
##     PIP4K2C, CCN1, MUC16, SOD2, KRT19, KRT7, AZGP1, UBC, PGM1, TGFBI
## PC_ 2
## Positive:  FP236383.3, VOPP1, LCN2, EPCAM, SAA1, CDK4, EGFR, AZGP1, RPL7, PIP4K2C
##     KRT19, HIST1H1B, CFB, CDH1, RNASET2, NFKBIZ, LAD1, SERPINB4, CCT6A, MUC16
##     F3, LANCL2, ESRP1, ICAM1, SLC43A3, PDZK1IP1, CHCHD2, CLDN4, CDH3, GNS
## Negative:  ALDH1A1, AKR1C2, CYP24A1, IGFBP4, AKR1C3, AKAP12, AKR1B1, PDE4D, VIM, ALDH3A1
##     TPM2, AKR1B10, G6PD, AHNAK2, CA12, AKR1C1, PGD, TNS4, PDE10A, SERPINE1
##     FTL, PBX1, NQO1, MYO1E, ANXA2, UGDH, CPLX2, THSD4, MAP1B, IGFBP7
## PC_ 3
## Positive:  MKI67, HIST1H1C, RPS6, STMN1, RPL29, HSP90AA1, RPS8, MYH9, HMGB2, FLNA
##     FTL, HIST1H1E, HSPA8, HIST1H2AI, PRRC2A, TUBB4B, RANBP1, SERBP1, INCENP, RPL24
##     LDHB, PLEC, TOP2A, TPX2, CENPF, MRPL16, HSPD1, PPP1R15A, PRAME, ACTN4
## Negative:  GAPDH, PTMA, IGFBP3, TRPC6, AC007325.2, PADI2, FGG, VOPP1, PLAAT4, NTS
##     FGB, PLAAT3, SERPINB4, AZGP1, MUC4, FGA, LCN2, KRT18, SAA4, TCN1
##     SUSD2, PEG10, HMOX1, LIPG, AC093817.2, SEMA3A, NUPR1, SLC16A5, TRIM31, C4orf19
## PC_ 4
## Positive:  FN1, NEAT1, C3, CXCL8, ANXA4, IGFBP3, RCSD1, CD24, INSIG1, PHLDB2
##     TNFAIP2, CFH, PNRC1, NDRG1, CXCL5, ARL15, DLK1, FNDC3B, STXBP5, CD53
##     MAP1A, EPB41, LRMDA, IFNGR1, C1R, ADGRB3, RHAG, RND1, CFB, SOX6
## Negative:  MKI67, KPNA2, TUBB4B, TPX2, TOP2A, CDCA3, ANLN, CENPF, NUSAP1, HIST1H1B
##     AURKA, INCENP, HMGB2, CCNA2, KNSTRN, HIST1H1E, HIST1H2AB, ECT2, HIST1H2AI, RRM2
##     PTMA, CDC20, CDCA8, H2AFX, KIF20A, PSRC1, FAM83D, CCNB1, PLK1, KIF2C
## PC_ 5
## Positive:  KIF20A, RCSD1, CDC20, DLK1, CCNB1, CENPF, DLGAP5, ANXA1, KPNA2, AURKA
##     PSRC1, CCNB2, ADGRB3, TOP2A, TPX2, CDCA3, CD53, ARL6IP1, ANTXR2, STXBP5
##     NUSAP1, SOSTDC1, CALB1, SLAMF6, BUB1, CFH, SOX6, CD24, LYZ, MUC4
## Negative:  HIST1H2AI, HIST1H1E, HIST1H1B, HIST1H2AB, HIST1H1C, HIST2H2AA4, HBG2, HIST2H2AC, HBG1, HIST1H2AJ
##     HIST1H1D, HEMGN, SLC43A3, FAM178B, CA1, RRM2, PKLR, HIST2H2BF, FOSL1, CCN1
##     ATF3, HIST1H2BK, MCM2, CCDC26, ATAD3B, SLC38A5, CDC45, KCNH2, RANBP1, SRM
```

```
# 打印PCA部分结果：
print(scFAST[["pca"]], dims = 1:5, nfeatures = 5)
```
```
## PC_ 1
## Positive:  HBG2, HBG1, PRAME, CPED1, AL713998.1
## Negative:  ASPH, EGFR, LCN2, KRT18, GAPDH
## PC_ 2
## Positive:  FP236383.3, VOPP1, LCN2, EPCAM, SAA1
## Negative:  ALDH1A1, AKR1C2, CYP24A1, IGFBP4, AKR1C3
## PC_ 3
## Positive:  MKI67, HIST1H1C, RPS6, STMN1, RPL29
## Negative:  GAPDH, PTMA, IGFBP3, TRPC6, AC007325.2
## PC_ 4
## Positive:  FN1, NEAT1, C3, CXCL8, ANXA4
## Negative:  MKI67, KPNA2, TUBB4B, TPX2, TOP2A
## PC_ 5
## Positive:  KIF20A, RCSD1, CDC20, DLK1, CCNB1
## Negative:  HIST1H2AI, HIST1H1E, HIST1H1B, HIST1H2AB, HIST1H1C
```

```
#pdf(file = 'PCA_点图.pdf',width = 10,height = 6)
VizDimLoadings(scFAST, dims = 1:2, reduction = "pca")
```

![](../../images/3c5ec41473b61f8f.webp)

```
#dev.off()

# 三种PCA展示方式：
DimHeatmap(scFAST, dims = 1,
           cells = 500, balanced = TRUE)
```

![](../../images/061c3383ae3a3520.webp)

```
#pdf(file = 'PCA.heatmap.pdf',width = 15,height = 12)

# 展示15种PCA：
DimHeatmap(scFAST, dims = 1:15,
           cells = 500, balanced = TRUE)
```

![](../../images/b14397331033f394.webp)

```r
#dev.off()

# 筛选合适的维度：
# 重复计算次数：
scFAST <- JackStraw(scFAST, num.replicate = 100)

# 计算维度这一步花的时间比较久：
scFAST <- ScoreJackStraw(scFAST, dims = 1:20)
#pdf(file = 'jackstrawplot.pdf',width = 6,height = 6)

# JackStrawPlot相当于高级PCA，为挑选合适维度进行下游可视化提供依据：
# 画出1到15个维度：
JackStrawPlot(scFAST, dims = 1:15)
```
```
## Warning: Removed 21504 rows containing missing values (geom_point).
```

![](../../images/d64f7f35e771fcd9.webp)

```
#dev.off()

# 利用ElbowPlot来评价PC，不可为了结果好看而降低PC数
#pdf(file = 'elbow.pdf',width = 6,height = 5)
ElbowPlot(scFAST)
```

![](../../images/613e5a3529cb0bd0.png)

```
#dev.off()
```

## 4.3 降维、分群、注释

```r
scFAST <- FindNeighbors(scFAST, dims = 1:11)
```
```
## Computing nearest neighbor graph
```
```
## Computing SNN
```

```r
# 细胞分群，resolution分辨率在细胞数在3000附近时一般设为0.4-1.2，resolution越大得到的类群越多:
scFAST <- FindClusters(scFAST, resolution = 0.5)
```
```
## Modularity Optimizer version 1.3.0 by Ludo Waltman and Nees Jan van Eck
##
## Number of nodes: 4986
## Number of edges: 165138
##
## Running Louvain algorithm...
## Maximum modularity in 10 random starts: 0.8383
## Number of communities: 6
## Elapsed time: 0 seconds
```

```
# 看前五个分类群ID:
head(Idents(scFAST), 5)
```
```
## CAGGCCAGCTCACAGCC CCGGGTATACGAAGTCC GTGTGGCGCTGTACTAC TCAGCAACGATCCGCGA
##                 2                 2                 0                 1
## TCCCATGTACTAGTCCT
##                 2
## Levels: 0 1 2 3 4 5
```

```r
#非线性降维方法：UMAP、tSNE

# 运行UMAP算法:
scFAST <- RunUMAP(scFAST, dims = 1:11)
```
```
## Warning: The default method for RunUMAP has changed from calling Python UMAP via reticulate to the R-native UWOT using the cosine metric
## To use Python UMAP via reticulate, set umap.method to 'umap-learn' and metric to 'correlation'
## This message will be shown once per session
```
```
## 11:09:52 UMAP embedding parameters a = 0.9922 b = 1.112
```
```
## 11:09:52 Read 4986 rows and found 11 numeric columns
```
```
## 11:09:52 Using Annoy for neighbor search, n_neighbors = 30
```
```
## 11:09:52 Building Annoy index with metric = cosine, n_trees = 50
```
```
## 0%   10   20   30   40   50   60   70   80   90   100%
```
```
## [----|----|----|----|----|----|----|----|----|----|
```
```
## **************************************************|
## 11:09:53 Writing NN index file to temp file /tmp/RtmpBqtxhu/file8bf4d523b90af
## 11:09:53 Searching Annoy index using 1 thread, search_k = 3000
## 11:09:55 Annoy recall = 100%
## 11:09:56 Commencing smooth kNN distance calibration using 1 thread with target n_neighbors = 30
## 11:09:57 Initializing from normalized Laplacian + noise (using irlba)
## 11:09:57 Commencing optimization for 500 epochs, with 199020 positive edges
## 11:10:04 Optimization finished
```

```r
# 运行TSNE算法，TSNE算法运行时间较UMAP更久:
scFAST <- RunTSNE(scFAST, dims = 1:11)
DimPlot(scFAST, reduction = "umap", label = TRUE)
```

![](../../images/2cf8d18e98a2ba43.webp)

```r
# 计算cluster1相较于其它cluster的marker：
cluster1.markers <- FindMarkers(scFAST, ident.1 = 1,
                                min.pct = 0.25)

# roc算法计算cluster1的marker
cluster1.markers <- FindMarkers(scFAST, ident.1 = 0,
                                logfc.threshold = 0.25,
                                test.use = "roc",
                                only.pos = TRUE)

# 查看前五个标记基因：
head(cluster1.markers, n = 5)
```
```
##         myAUC avg_diff power avg_log2FC pct.1 pct.2
## ALDH1A1 0.973 3.584375 0.946   5.171160 0.953 0.052
## CYP24A1 0.924 2.547823 0.848   3.675732 0.890 0.151
## AKR1C2  0.910 3.383152 0.820   4.880857 0.836 0.042
## PKM     0.879 0.872585 0.758   1.258874 0.993 0.881
## IGFBP4  0.863 2.537671 0.726   3.661086 0.747 0.043
```

```r
# 寻找每一个分类群与其他所有细胞之间的标记基因，并只显示positive结果
scFAST.markers <- FindAllMarkers(scFAST, only.pos = TRUE,
                                min.pct = 0.25,
                                logfc.threshold = 0.25)
```
```
## Calculating cluster 0
## Calculating cluster 1
## Calculating cluster 2
## Calculating cluster 3
## Calculating cluster 4
## Calculating cluster 5
```

```r
library(dplyr)
# 筛选出top10：
top10gene <- scFAST.markers %>% group_by(cluster) %>%
  top_n(n = 10, wt = avg_log2FC)
# pdf(file = 'top10marker.pdf',width = 20,height = 100)
VlnPlot(scFAST, features = unique(top10gene$gene),
        pt.size = 0,ncol = 4)
```

![](../../images/2f9fc63a15e206d1.webp)

```
# dev.off()

VlnPlot(scFAST, features = unique(top10gene$gene),
        pt.size = 0,stack = T)
```

![](../../images/7d6ed100d7681e3d.webp)

```
DimPlot(scFAST)
```

![](../../images/bf2beee2f33d100c.webp)

```
# 查看部分marker基因在FeaturePlot(以UMAP作为底图)中的表达情况：
FeaturePlot(scFAST,
            features = unique(top10gene$gene)[1:9])
```

![](../../images/1c3d3ca0805e3784.webp)

```
# 展示cluster标签
FeaturePlot(scFAST,
            features = unique(top10gene$gene)[1:9],
            label = T)
```

![](../../images/5351fbebc08d6675.webp)

```
FeaturePlot(scFAST,
            features = c("ALDH1A1","AKR1C2","AKR1C3","CYP24A1"))
```

![](../../images/e20810a3a9f4352e.webp)

```r
# 展示前10个标记基因的热图
top10 <- scFAST.markers %>% group_by(cluster) %>% top_n(n = 10, wt = avg_log2FC)
DoHeatmap(scFAST, features = top10$gene) + NoLegend()
```

![](../../images/f2ccf2d6ecc77386.webp)

```r
#通过标记基因及文献，可以人工确定各分类群的细胞类型，则可以如下手动添加细胞群名称：

# 重命名方法1：
new.cluster.ids <- c("Celltype_A", "Celltype_B","Celltype_C",
                     "Celltype_B","Celltype_B","Celltype_C")
names(new.cluster.ids) <- levels(scFAST)
scFAST <- RenameIdents(scFAST, new.cluster.ids)
scFAST$celltype <- Idents(scFAST)
```

```r
# 重命名方法2
scFAST$celltype <- scFAST$RNA_snn_res.0.5
scFAST$celltype <- recode(scFAST$celltype,
                  '0'="Celltype_A",
                  '1'="Celltype_B",
                  '2'="Celltype_C",
                  '3'="Celltype_B",
                  '4'="Celltype_B",
                  '5'="Celltype_C")

Idents(scFAST) <- 'celltype'

# 计算重命名后的细胞类型marker
scFAST_rename_markers <- FindAllMarkers(scFAST, only.pos = TRUE,
                                 min.pct = 0.25,
                                 logfc.threshold = 0.25)
```
```
## Calculating cluster Celltype_A
```
```
## Calculating cluster Celltype_B
```
```
## Calculating cluster Celltype_C
```

```r
# 筛选top5 maker
top5_rename <- scFAST_rename_markers %>% group_by(cluster) %>%
  top_n(n = 5, wt = avg_log2FC)

# 利用堆积小提琴图查看表达情况：
VlnPlot(scFAST,
          features = unique(top5_rename$gene),
            stack = T)
```

![](../../images/d8b27f781cb2608c.webp)

```r
# 求各个细胞类型基因的平均表达量：
cell.expr <-
  log1p(AverageExpression(scFAST, verbose = FALSE)$RNA)

head(cell.expr)
```
```
##            Celltype_A  Celltype_B Celltype_C
## AL627309.1 0.00000000 0.000000000 0.28221346
## AL627309.2 0.00000000 0.006774702 0.01673949
## AL627309.5 0.04375944 0.116682264 0.20596967
## AP006222.2 0.01291225 0.013775439 0.56941424
## AL732372.1 0.00000000 0.009998963 0.01746337
## AC114498.1 0.00000000 0.010397461 0.03523540
```

```
DimPlot(scFAST, reduction = "umap",
        label = TRUE, pt.size = 0.5) + NoLegend()
```

![](../../images/b3db492fd88e9de8.webp)

```r
Idents(scFAST) <- 'celltype'

DimPlot(scFAST, reduction = "umap",
        label = TRUE, pt.size = 0.5) + NoLegend()
```

![](../../images/b3db492fd88e9de8.webp)

可以如是完成数据的保存与再次读取：

```r
# 创建目录：
dir.create('scFAST_out')

# 将Seurat对象保存为rds文件输出：
saveRDS(scFAST, file = "./scFAST_out/scFAST_fast.rds")

# 读取rds文件：
scFAST <- readRDS('./scFAST_out/scFAST_fast.rds')
```

##

**
**

**五、mut模块**

![](../../images/1189c1178040d051.png)

5.1 简介

该模块用于分析`panel`数据或者全序列数据中的 _变异信息_ ，可以说是scFAST的特色分析模块。在该模块中，对可靠的突变位点会给出位点所在`cluster`、 `barcode`等信息，所以需要提供`rds`文件(即我们上一步中存出的`scFAST_fast.rds`文件)，因此，需要先利用`seeksoultools`等软件进行定量、分群之后再用此模块进行变异检测。panel的分析也是使用该模块完成的。

## 5.2 模块工作流程

![](../../images/ab476826c676fab7.webp)

突变检测模块流程示意图

在将整体数据变异位点到单细胞维度时，利用了`bam`文件中每条`reads`的`barcode`和`UMI`信息。流程默认将 _非同义突变_ 过滤，并且基于链偏好性对突变进行再一次的过滤。

我们使用 `SOR（Symmetric Odds Ratio）`值评估链偏好性。`snv`小于`1.0`、`indel` 默认小于`10.0`的所有位点进行reads统计，并且每个位点可给出一个中间文件（该文件生成与否根据_tmptype_参数设定），如下

```
BC_UMI  BKGD/CB coverage        alt     ref1    ref2    alt1    alt2
CGTAGTACGAGCACGAA_CCCGCTTTCCTT  cell    35      0       0       35      0       0
TGATCAGATGGTAACAC_ACTCCTTTCCAT  cell    34      1       0       33      0       1
AGGATAATACACTACGA_CTGTCGATCCTT  background      1       1       0       0       0       1
```

该文件记录突变位点中每一条`UMI`的ref alt reads数量，并依据此对位点进行了过滤，过滤条件如下：
（1）只有符合`alt/coverage`>=0.9(`altvaf`参数值)且`coverage reads`>=2(`UMIreads`参数值)的UMI才被认为是支持突变的UMI；
（2）支持突变`的UMI`数目>=2(`umiint`参数值)；
（3）支持突变的`barcode`数目>=2(`bcint`参数值)；
（4）位点总突变`reads`>=2(`ADint`数值)；
（5）位点覆盖`reads`>=2(`DPint`参数值)；
（6）`snv`的`sor`值<=1.0 `indel`的`sor`<=10.0(`sorcut`参数值) ；
（7）`ExAC`数据库中`eas`和`All`频率小于0.01；
（8）突变的`vaf`(alt reads/coverage reads) > 0.03 。经过如上8个步骤过滤的位点认为是最终的突变位点。

## 5.3 运行`mut`模块

### 5.3.1 输入文件准备

panel原始fastq数据（clean data；需要自行用fastp等软件处理下机数据）

  * STAR软件
可以选择本软件环境中的`STAR`，也可以用外部`STAR`

  * 基因组fasta文件

  * `STAR`软件的参考基因组索引文件
需要注意STAR软件版本兼容问题

  * 全序列数据（非panel数据）
处理得到的表达矩阵进行降维分群之后的文件，即我们上文保存的`scFAST_fast.rds`文件

  * `panel`的`bed`文件

  * annovar软件及其`database`
可见2.3.3部分

### 5.3.2 运行`mut`模块

参数解释：

  * \--fq1
panel R1 fastq数据路径。

  * \--fq2
panel R2 fastq数据路径。

  * \--genomeDir
STAR软件构建的索引文件，注意需要与STAR软件版本兼容。

  * \--star_path
STAR软件的路径。

  * \--fasta
参考基因组的fasta文件。注意，fasta文件的染色体名称需要与genomeDir的染色体名称保持一致。

  * \--samplename
样本名称。

  * \--outdir
结果目录。

  * \--rds
全序列RNA表达矩阵的rds文件。

  * \--annovarpl
下载的annovar软件路径。

  * \--annovardb
下载的annovar数据库路径。

  * \--ref
参考基因组版本。

  * \--cellanno
seurat_clusters或者CellType，默认为seurat_clusters，当rds文件是经过手动注释之后的rds文件时，将meta data细胞类型列命名为CellType，并将此参数设置为CellType。

  * \--filted
fsys。默认只保留非同义突变。

  * \--tmptype
参数值为allreads时，每个位点在BC_UMI_reads_tmp路径下生成一个记录详细reads数目的文件。该参数值默认为txt，即不生成详细的文件。

  * \--panel：panel的bed文件。此参数时，只对bed区间内进行变异检测，当不指定此参数的时候，会对全部reads进行变异检测。

```
# 任务比较大，将其丢到后台运行
nohup seeksoultools mut run \
        --fq1 /home/biomamba/analysis/xunyin/test_data/cellline_test/cellline_R1_001.clean.fastq.gz \
        --fq2 /home/biomamba/analysis/xunyin/test_data/cellline_test/cellline_R2_001.clean.fastq.gz \
        --genomeDir /home/biomamba/analysis/xunyin/my_refference/hg38/ \
        --fasta /home/biomamba/ext_data2/analysis/xunyin/my_refference/hg38/hg38.fa \
        --samplename cellline \
        --outdir /home/biomamba/analysis/xunyin/cell_line_mutout \
        --rds  /home/biomamba/analysis/xunyin/scFAST_out/scFAST_fast.rds \
        --annovarpl /home/biomamba/ext_data2/analysis/xunyin/annovar/table_annovar.pl \
        --annovardb /home/biomamba/ext_data2/analysis/xunyin/annovar/humandb \
        --ref hg38 \
        --filted fsys \
        --cellanno celltype \
        --core 4 2>&1 > mut.log &
```

### 5.3.3 输出结果

输出路径中包含的文件为：

```
tree cell_line_mutout
```
```
## [01;34mcell_line_mutout[00m
## ├── celllinebarcodelist.xls
## ├── [01;34mmutation_umap[00m
## │   ├── cellline_add_snv.rds
## │   └── [01;34mSNV_diff[00m
## │       ├── cellline_snv_markers.xls
## │       ├── [01;34mCelltype_A[00m
## │       │   ├── ANLN_chr7-36407745_-_TCT.png
## │       │   ├── ANP32E_chr1-150226713_T_C.png
## │       │   ├── CANX_chr5-179708267_G_T.png
## │       │   ├── CANX_chr5-179726685_A_G.png
## │       │   ├── CPPED1_chr16-12704775_C_G.png
## │       │   ├── CYBA_chr16-88643516_G_C.png
## │       │   ├── DBN1_chr5-177466941_C_T.png
## │       │   ├── FH_chr1-241497970_C_A.png
## │       │   ├── FUS_chr16-31190121_G_A.png
## │       │   ├── H2AC14_chr6-27814513_C_G.png
## │       │   ├── HLA-B_chr6-31356259_T_G.png
## │       │   ├── KIFBP_chr10-69000515_T_C.png
## │       │   ├── KRAS_chr12-25245351_C_T.png
## │       │   ├── NAMPT_chr7-106261662_T_C.png
## │       │   ├── NCOA4_chr10-46010599_C_T.png
## │       │   ├── NUDT3;RPS10-NUDT3_chr6-34293496_T_G.png
## │       │   ├── PCNT_chr21-46334596_A_G.png
## │       │   ├── PMPCB_chr7-103298662_G_A.png
## │       │   ├── PPP4R2_chr3-73065058_C_G.png
## │       │   ├── RALY_chr20-34077059_-_AGC.png
## │       │   ├── REST_chr4-56930473_T_C.png
## │       │   ├── SPTBN1_chr2-54643117_C_A.png
## │       │   ├── TBC1D23_chr3-100296189_C_A.png
## │       │   └── UNC93B1_chr11-67999234_G_A.png
## │       ├── [01;34mCelltype_B[00m
## │       │   ├── ARL6IP1_chr16-18794662_A_G.png
## │       │   ├── BAG3_chr10-119670133_G_A.png
## │       │   ├── CAP1_chr1-40070169_A_T.png
## │       │   ├── CCNDBP1_chr15-43191645_T_C.png
## │       │   ├── CCT8_chr21-29067014_C_T.png
## │       │   ├── CDCA5_chr11-65079463_C_T.png
## │       │   ├── CYBA_chr16-88647125_T_G.png
## │       │   ├── CYP1B1_chr2-38071060_G_C.png
## │       │   ├── DDX3X_chrX-41343348_A_C.png
## │       │   ├── DHX33_chr17-5461073_A_G.png
## │       │   ├── EEFSEC_chr3-128153739_G_A.png
## │       │   ├── GART_chr21-33534717_C_A.png
## │       │   ├── GART_chr21-33534718_A_T.png
## │       │   ├── HAVCR1_chr5-157052561_A_G.png
## │       │   ├── HMGA1_chr6-34243515_-_A.png
## │       │   ├── INO80_chr15-41079889_T_C.png
## │       │   ├── LRRC8D_chr1-89933402_A_G.png
## │       │   ├── MRPS7_chr17-75261947_C_T.png
## │       │   ├── PCIF1_chr20-45940563_G_A.png
## │       │   ├── PLD3_chr19-40378055_G_A.png
## │       │   ├── PLOD1_chr1-11965543_C_T.png
## │       │   ├── POLR1A_chr2-86089889_C_G.png
## │       │   ├── PPP4R3B_chr2-55617200_G_A.png
## │       │   ├── RRBP1_chr20-17616749_C_T.png
## │       │   ├── SERINC1_chr6-122451991_T_G.png
## │       │   ├── VPS35L_chr16-19699568_C_T.png
## │       │   ├── WASHC1_chr9-17843_C_A.png
## │       │   ├── WASHC1_chr9-18081_G_A.png
## │       │   ├── WASHC1_chr9-18143_C_T.png
## │       │   ├── WASHC1_chr9-18481_T_C.png
## │       │   ├── ZNF180_chr19-44479350_G_C.png
## │       │   ├── ZNF280A_chr22-22515221_G_T.png
## │       │   └── ZSCAN25_chr7-99619904_G_A.png
## │       └── [01;34mCelltype_C[00m
## │           ├── ACIN1_chr14-23079588_-_ACGTGA.png
## │           ├── CCAR2_chr8-22615709_G_T.png
## │           ├── CCDC34_chr11-27350364_G_T.png
## │           ├── CCDC74B_chr2-130141240_G_A.png
## │           ├── CDC20_chr1-43362992_G_A.png
## │           ├── DFFA_chr1-10469269_A_G.png
## │           ├── EGLN2_chr19-40807854_C_T.png
## │           ├── EIF3A_chr10-119051224_T_A.png
## │           ├── FAM185A_chr7-102751727_A_G.png
## │           ├── FBXO22_chr15-75904057_C_T.png
## │           ├── HDLBP_chr2-241256379_C_A.png
## │           ├── KIAA0100_chr17-28643219_C_A.png
## │           ├── KMT2D_chr12-49032947_GCT_-.png
## │           ├── LSM12_chr17-44038092_T_C.png
## │           ├── MDC1_chr6-30713191_C_T.png
## │           ├── MRPL20_chr1-1402212_G_C.png
## │           ├── NDUFC2;NDUFC2-KCTD14_chr11-78073109_-_A.png
## │           ├── NEK9_chr14-75124193_C_T.png
## │           ├── NFE2L2_chr2-177231803_G_C.png
## │           ├── NR1H2_chr19-50378574_-_CAG.png
## │           ├── PKP3_chr11-397348_A_G.png
## │           ├── PUS7_chr7-105508236_A_G.png
## │           ├── RAB5B_chr12-55992132_GGA_-.png
## │           ├── RTN3_chr11-63758191_-_A.png
## │           └── TSR2_chrX-54444542_A_G.png
## ├── [01;34mSTAR[00m
## │   ├── cellline_Aligned.out.bam
## │   ├── cellline_Aligned.sortedByCoord.out.bam
## │   ├── cellline_Aligned.sortedByCoord.out.bam.bai
## │   ├── cellline_Log.final.out
## │   ├── cellline_Log.out
## │   ├── cellline_Log.progress.out
## │   ├── cellline_SJ.out.tab
## │   └── [01;34mcellline__STARtmp[00m
## │       ├── readFilesIn.info
## │       ├── [01;32mreadsCommand_read1[00m
## │       ├── [01;32mreadsCommand_read2[00m
## │       ├── [40;33mtmp.fifo.read1[00m
## │       └── [40;33mtmp.fifo.read2[00m
## ├── [01;34mstep1[00m
## │   ├── [01;31mcellline_1.fq.gz[00m
## │   ├── [01;31mcellline_2.fq.gz[00m
## │   ├── [01;31mcellline.cutTSO_1.fq.gz[00m
## │   ├── [01;31mcellline.cutTSO_2.fq.gz[00m
## │   └── [01;31mcellline_stat.fq.gz[00m
## ├── summary.json
## └── [01;34mvarscan[00m
##     ├── [01;34mBC_UMI_reads_tmp[00m
##     ├── cellline.annoCB.varscan.indel.chr10.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr11.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr12.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr13.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr14.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr15.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr16.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr17.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr18.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr19.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr1.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr20.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr21.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr22.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr2.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr3.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr4.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr5.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr6.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr7.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr8.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chr9.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chrX.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.indel.chrY.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr10.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr11.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr12.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr13.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr14.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr15.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr16.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr17.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr18.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr19.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr1.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr20.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr21.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr22.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr2.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr3.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr4.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr5.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr6.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr7.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr8.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chr9.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chrX.hg38_multianno.txt
##     ├── cellline.annoCB.varscan.snp.chrY.hg38_multianno.txt
##     ├── cellline.clusters.varscan.snp_indel.hg38_multianno.xls
##     ├── cellline.filter-nonsys.varscan.indel.chr10.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr11.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr12.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr13.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr14.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr15.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr16.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr17.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr18.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr19.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr1.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr20.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr21.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr22.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr2.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr3.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr4.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr5.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr6.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr7.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr8.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chr9.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chrX.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.indel.chrY.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr10.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr11.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr12.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr13.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr14.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr15.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr16.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr17.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr18.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr19.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr1.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr20.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr21.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr22.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr2.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr3.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr4.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr5.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr6.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr7.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr8.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chr9.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chrX.hg38_multianno.txt
##     ├── cellline.filter-nonsys.varscan.snp.chrY.hg38_multianno.txt
##     ├── cellline.filter.varscan.snp_indel.hg38_multianno.txt
##     ├── cellline.final.varscan.snp_indel.hg38_multianno.txt
##     ├── cellline.hg38.varscan.indel.chr10.vcf
##     ├── cellline.hg38.varscan.indel.chr11.vcf
##     ├── cellline.hg38.varscan.indel.chr12.vcf
##     ├── cellline.hg38.varscan.indel.chr13.vcf
##     ├── cellline.hg38.varscan.indel.chr14.vcf
##     ├── cellline.hg38.varscan.indel.chr15.vcf
##     ├── cellline.hg38.varscan.indel.chr16.vcf
##     ├── cellline.hg38.varscan.indel.chr17.vcf
##     ├── cellline.hg38.varscan.indel.chr18.vcf
##     ├── cellline.hg38.varscan.indel.chr19.vcf
##     ├── cellline.hg38.varscan.indel.chr1.vcf
##     ├── cellline.hg38.varscan.indel.chr20.vcf
##     ├── cellline.hg38.varscan.indel.chr21.vcf
##     ├── cellline.hg38.varscan.indel.chr22.vcf
##     ├── cellline.hg38.varscan.indel.chr2.vcf
##     ├── cellline.hg38.varscan.indel.chr3.vcf
##     ├── cellline.hg38.varscan.indel.chr4.vcf
##     ├── cellline.hg38.varscan.indel.chr5.vcf
##     ├── cellline.hg38.varscan.indel.chr6.vcf
##     ├── cellline.hg38.varscan.indel.chr7.vcf
##     ├── cellline.hg38.varscan.indel.chr8.vcf
##     ├── cellline.hg38.varscan.indel.chr9.vcf
##     ├── cellline.hg38.varscan.indel.chrX.vcf
##     ├── cellline.hg38.varscan.indel.chrY.vcf
##     ├── cellline.hg38.varscan.snp.chr10.vcf
##     ├── cellline.hg38.varscan.snp.chr11.vcf
##     ├── cellline.hg38.varscan.snp.chr12.vcf
##     ├── cellline.hg38.varscan.snp.chr13.vcf
##     ├── cellline.hg38.varscan.snp.chr14.vcf
##     ├── cellline.hg38.varscan.snp.chr15.vcf
##     ├── cellline.hg38.varscan.snp.chr16.vcf
##     ├── cellline.hg38.varscan.snp.chr17.vcf
##     ├── cellline.hg38.varscan.snp.chr18.vcf
##     ├── cellline.hg38.varscan.snp.chr19.vcf
##     ├── cellline.hg38.varscan.snp.chr1.vcf
##     ├── cellline.hg38.varscan.snp.chr20.vcf
##     ├── cellline.hg38.varscan.snp.chr21.vcf
##     ├── cellline.hg38.varscan.snp.chr22.vcf
##     ├── cellline.hg38.varscan.snp.chr2.vcf
##     ├── cellline.hg38.varscan.snp.chr3.vcf
##     ├── cellline.hg38.varscan.snp.chr4.vcf
##     ├── cellline.hg38.varscan.snp.chr5.vcf
##     ├── cellline.hg38.varscan.snp.chr6.vcf
##     ├── cellline.hg38.varscan.snp.chr7.vcf
##     ├── cellline.hg38.varscan.snp.chr8.vcf
##     ├── cellline.hg38.varscan.snp.chr9.vcf
##     ├── cellline.hg38.varscan.snp.chrX.vcf
##     ├── cellline.hg38.varscan.snp.chrY.vcf
##     ├── cellline.simple.varscan.snp_indel.hg38_multianno.txt
##     ├── cellline.snp_indel.all_UMI.matrix
##     ├── cellline.snp_indel.alt_UMI.matrix
##     ├── cellline.varscan.indel.chr10.avinput
##     ├── cellline.varscan.indel.chr10.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr10.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr10.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr11.avinput
##     ├── cellline.varscan.indel.chr11.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr11.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr11.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr12.avinput
##     ├── cellline.varscan.indel.chr12.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr12.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr12.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr13.avinput
##     ├── cellline.varscan.indel.chr13.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr13.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr13.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr14.avinput
##     ├── cellline.varscan.indel.chr14.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr14.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr14.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr15.avinput
##     ├── cellline.varscan.indel.chr15.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr15.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr15.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr16.avinput
##     ├── cellline.varscan.indel.chr16.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr16.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr16.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr17.avinput
##     ├── cellline.varscan.indel.chr17.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr17.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr17.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr18.avinput
##     ├── cellline.varscan.indel.chr18.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr18.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr18.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr19.avinput
##     ├── cellline.varscan.indel.chr19.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr19.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr19.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr1.avinput
##     ├── cellline.varscan.indel.chr1.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr1.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr1.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr20.avinput
##     ├── cellline.varscan.indel.chr20.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr20.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr20.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr21.avinput
##     ├── cellline.varscan.indel.chr21.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr21.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr21.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr22.avinput
##     ├── cellline.varscan.indel.chr22.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr22.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr22.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr2.avinput
##     ├── cellline.varscan.indel.chr2.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr2.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr2.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr3.avinput
##     ├── cellline.varscan.indel.chr3.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr3.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr3.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr4.avinput
##     ├── cellline.varscan.indel.chr4.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr4.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr4.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr5.avinput
##     ├── cellline.varscan.indel.chr5.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr5.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr5.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr6.avinput
##     ├── cellline.varscan.indel.chr6.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr6.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr6.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr7.avinput
##     ├── cellline.varscan.indel.chr7.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr7.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr7.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr8.avinput
##     ├── cellline.varscan.indel.chr8.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr8.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr8.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chr9.avinput
##     ├── cellline.varscan.indel.chr9.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr9.hg38_multianno.txt
##     ├── cellline.varscan.indel.chr9.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chrX.avinput
##     ├── cellline.varscan.indel.chrX.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chrX.hg38_multianno.txt
##     ├── cellline.varscan.indel.chrX.hg38_multianno.vcf
##     ├── cellline.varscan.indel.chrY.avinput
##     ├── cellline.varscan.indel.chrY.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.indel.chrY.hg38_multianno.txt
##     ├── cellline.varscan.indel.chrY.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr10.avinput
##     ├── cellline.varscan.snp.chr10.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr10.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr10.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr11.avinput
##     ├── cellline.varscan.snp.chr11.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr11.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr11.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr12.avinput
##     ├── cellline.varscan.snp.chr12.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr12.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr12.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr13.avinput
##     ├── cellline.varscan.snp.chr13.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr13.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr13.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr14.avinput
##     ├── cellline.varscan.snp.chr14.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr14.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr14.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr15.avinput
##     ├── cellline.varscan.snp.chr15.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr15.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr15.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr16.avinput
##     ├── cellline.varscan.snp.chr16.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr16.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr16.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr17.avinput
##     ├── cellline.varscan.snp.chr17.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr17.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr17.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr18.avinput
##     ├── cellline.varscan.snp.chr18.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr18.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr18.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr19.avinput
##     ├── cellline.varscan.snp.chr19.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr19.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr19.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr1.avinput
##     ├── cellline.varscan.snp.chr1.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr1.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr1.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr20.avinput
##     ├── cellline.varscan.snp.chr20.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr20.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr20.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr21.avinput
##     ├── cellline.varscan.snp.chr21.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr21.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr21.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr22.avinput
##     ├── cellline.varscan.snp.chr22.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr22.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr22.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr2.avinput
##     ├── cellline.varscan.snp.chr2.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr2.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr2.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr3.avinput
##     ├── cellline.varscan.snp.chr3.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr3.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr3.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr4.avinput
##     ├── cellline.varscan.snp.chr4.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr4.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr4.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr5.avinput
##     ├── cellline.varscan.snp.chr5.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr5.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr5.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr6.avinput
##     ├── cellline.varscan.snp.chr6.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr6.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr6.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr7.avinput
##     ├── cellline.varscan.snp.chr7.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr7.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr7.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr8.avinput
##     ├── cellline.varscan.snp.chr8.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr8.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr8.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chr9.avinput
##     ├── cellline.varscan.snp.chr9.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr9.hg38_multianno.txt
##     ├── cellline.varscan.snp.chr9.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chrX.avinput
##     ├── cellline.varscan.snp.chrX.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chrX.hg38_multianno.txt
##     ├── cellline.varscan.snp.chrX.hg38_multianno.vcf
##     ├── cellline.varscan.snp.chrY.avinput
##     ├── cellline.varscan.snp.chrY.filtersor.hg38_multianno.txt
##     ├── cellline.varscan.snp.chrY.hg38_multianno.txt
##     └── cellline.varscan.snp.chrY.hg38_multianno.vcf
##
## 10 directories, 445 files
```

重要输出结果 `*clusters.varscan.snp_indel.hg38_multianno.xls`：是经过barcode UMI vaf 人群频率等过滤的最终位点注释文件

`*.snp_indel.alt_UMI.matrix`：是经过最终过滤的位点在细胞中突变的UMI矩阵，行是突变，列是细胞。
![](../../images/e988adaa1abe64fc.webp)

`*.snp_indel.all_UMI.matrix`：是经过最终过滤的位点在细胞中覆盖的UMI矩阵，行是突变，列是细胞。
![](../../images/36cdfce597993cd9.webp)

`mutation_umap/*_snv_markers.xls`结果如下所示： ![](../../images/9ac89b5181f43af9.webp)
每列的含义为：
`SNV`：突变位点

`p_val`：fisher检验的p值

`ident1_cover`：目标cluster/celltype中有多少细胞覆盖到了这个突变位点但是没发生突变

`ident1_mut`：目标cluster/celltype中有多少细胞带有这个突变

`ident2_cover`: 非目标cluster/celltype中有多少细胞覆盖到了这个突变位点但是没发生突变

`ident2_mut`：非目标cluster/celltype中有多少细胞带有这个突变

`cluster`：目标细胞类型

### 5.3.4 `Seurat`再处理及可视化

```r
library(Seurat)
# 读取处理后的rds文件
scFAST <- readRDS('cell_line_mutout/mutation_umap/cellline_add_snv.rds')

# 与原来一样是一个Seurat对象，可以查看一下细胞类型：
DimPlot(scFAST)
```

![](../../images/7b1593ddec5f35d8.webp)

```
# 比输入的rds文件多出了几列metadata：
colnames(scFAST@meta.data)
```
```
##  [1] "orig.ident"       "nCount_RNA"       "nFeature_RNA"     "percent.mt"
##  [5] "RNA_snn_res.0.5"  "seurat_clusters"  "celltype"         "Sample"
##  [9] "nCount_SNV_all"   "nFeature_SNV_all" "nCount_SNV"       "nFeature_SNV"
## [13] "CellType"         "tmp_mut"
```

```
# 例如nFeature_SNV记录了每个细胞发生SNV的基因数：
FeaturePlot(scFAST,features = 'nFeature_SNV',label = T)
```

![](../../images/d8c8f4bfd73ecd0f.webp)

```r
# 我们也可以读入本地的其它输出文件(例如这里记录snp信息的矩阵)加入Seurat的注释信息中：
snp_matrix <- read.table('/home/biomamba/analysis/xunyin/cell_line_mutout/varscan/cellline.snp_indel.alt_UMI.matrix',sep = '\t',header = T,row.names = 1)

# 这是一个列名为细胞名，行名为突变类型的矩阵：
snp_matrix[1:4,1:4]
```
```
##                         AAACCCACGATCGAAGG AAACCCAGCTCCAGCGT AAACCCAGCTTAACCTG
## MRPL20:chr1-1402212:G>C                 0                 0                 0
## ATAD3C:chr1-1459164:A>G                 0                 0                 0
## ATAD3C:chr1-1459173:G>A                 0                 0                 0
## CDK11A:chr1-1721654:A>G                 0                 0                 0
##                         AAACGAAATGGGAACAA
## MRPL20:chr1-1402212:G>C                 0
## ATAD3C:chr1-1459164:A>G                 0
## ATAD3C:chr1-1459173:G>A                 0
## CDK11A:chr1-1721654:A>G                 0
```

```r
# 转换数据格式
library(dplyr)
snp_matrix <- t(snp_matrix)%>%as.data.frame()

# 查看所有细胞中突变数量最多的三个类型：
apply(snp_matrix, 2, function(x){sum(x)}) %>% sort(decreasing = T)%>% .[1:3]
```
```
##   HMGA1:chr6-34243515:->A HAVCR1:chr5-157052561:A>G   HAT1:chr2-171976274:T>C
##                       178                       115                        94
```

```r
# 将这三种突变类型加入metadata中
scFAST <- AddMetaData(scFAST,
                      metadata = snp_matrix[,c('HMGA1:chr6-34243515:->A', 'HAVCR1:chr5-157052561:A>G','HAT1:chr2-171976274:T>C')])
```
```
## Warning: Invalid name supplied, making object
## name syntactically valid. New object name is
## HMGA1.chr6.34243515...AHAVCR1.chr5.157052561.A.GHAT1.chr2.171976274.T.C;
## see ?make.names for more details on syntax validity
```

```
# 检查meta.data
colnames(scFAST@meta.data)
```
```
##  [1] "orig.ident"                "nCount_RNA"
##  [3] "nFeature_RNA"              "percent.mt"
##  [5] "RNA_snn_res.0.5"           "seurat_clusters"
##  [7] "celltype"                  "Sample"
##  [9] "nCount_SNV_all"            "nFeature_SNV_all"
## [11] "nCount_SNV"                "nFeature_SNV"
## [13] "CellType"                  "tmp_mut"
## [15] "HMGA1.chr6.34243515...A"   "HAVCR1.chr5.157052561.A.G"
## [17] "HAT1.chr2.171976274.T.C"
```

```
# 可视化突变：
VlnPlot(scFAST,features = 'HMGA1:chr6-34243515:->A')
```

![](../../images/eb9366cb7511ea33.webp)

```
FeaturePlot(scFAST,features = 'HMGA1:chr6-34243515:->A')
```

![](../../images/f45a28e19c35d912.webp)

```r
# 如果上述不够直观，可用突变发生的堆积柱状图展示：
# 统计突变数量的比例：
cell.prop<-as.data.frame(prop.table(table(scFAST$HMGA1.chr6.34243515...A, scFAST$CellType)))
colnames(cell.prop)<-c("SNP_Number","Celltype","proportion")
head(cell.prop)
```
```
##   SNP_Number   Celltype  proportion
## 1          0 Celltype_A 0.316445517
## 2          1 Celltype_A 0.003216727
## 3          2 Celltype_A 0.000000000
## 4          0 Celltype_B 0.413751508
## 5          1 Celltype_B 0.020506634
## 6          2 Celltype_B 0.001005227
```

```r
# 可视化
library(ggplot2)
# 可以看出Celltype_B的突变数量略高一些
ggplot(cell.prop,aes(Celltype,proportion,fill=SNP_Number))+
geom_bar(stat="identity",position="fill")+
ggtitle("")+
theme_bw()+
theme(axis.ticks.length=unit(0.5,'cm'))+
guides(fill=guide_legend(title=NULL))+
  theme( axis.text.x.bottom = element_text(angle = 45,hjust = 1,vjust = 1))+
  ggtitle('HMGA1:chr6-34243515:->A')
```

![](../../images/d3bb67bf3ef1046a.webp)

# 更多教程，敬请期待！

**scFAST学习手册**

![](../../images/1189c1178040d051.png)

## ![](../../images/0d65733840fcaed1.gif)

与以往的教程一样，我们给大家准备了数据分析的学习手册，目前分为scFAST绪论、准备工作、fast模块、Seurat分析与可视化、mut模块等五节内容(更多章节持续创作中)及对应测试文件，大家可以添加企业微信回复关键字"**scFAST学习手册** "即领:

![](../../images/a1dbb3a25a832fe1.webp)
