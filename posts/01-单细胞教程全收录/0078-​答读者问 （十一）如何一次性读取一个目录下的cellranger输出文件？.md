---
title: "​答读者问 （十一）如何一次性读取一个目录下的cellranger输出文件？"
date: 2022-03-05
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047#rd
albums: ["单细胞教程全收录", "答读者问"]
---

# ​答读者问 （十一）如何一次性读取一个目录下的cellranger输出文件？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047#rd
> 合集：单细胞教程全收录 / 答读者问

往期回顾

[答读者问 （一）单基因究竟能否进行GSEA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484175&idx=1&sn=3e45ad62b045a541874e5ae7ca03f849&chksm=9b3f7a5fac48f349f8893500825d2c6b4ff581fbb0816c1074d88a0dbbb4a612c1e1bb3740bb&scene=21#wechat_redirect>)

[答读者问 （二）为什么我的PCA分析报错了？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484248&idx=1&sn=b1fe7174a28562d01422e43609f41709&chksm=9b3f7a08ac48f31e3bbfdb4a9824dadf25a8fa3ff9b78dd15d646ae4c3da5db04e2e4acfba3d&scene=21#wechat_redirect>)

[答读者问 （三）单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)

[答读者问 （四）如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)

[答读者问 （五）如何实现各物种基因的ID/symbol的转换](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484353&idx=2&sn=8fccb88c871a42c803e313be157ab293&chksm=9b3f7a91ac48f387df8b462f7318596fc5c645d6f05eefac2c598ff6875c0a2eeb902aaf5a15&scene=21#wechat_redirect>)

[答读者问 （六）Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484376&idx=2&sn=9fda8a5261e86f889a58d607163ce0fd&chksm=9b3f7a88ac48f39ea9c19e256a513c9ae80c6f6dc1724b7783884e23981e2061c78fa67071c9&scene=21#wechat_redirect>)

[答读者问 （七）有人问我Biomamba何解](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484550&idx=1&sn=ec4466084c1c9eba7eb292e95f33b5bb&chksm=9b3f7dd6ac48f4c042b4e9df2abd717b1354b4914c3f7510eaf444e97965a0f6622979e710e0&scene=21#wechat_redirect>)

[答读者问 （八）为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)

[答读者问 （九） 如何将数百个文件整合为一个矩阵](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485032&idx=1&sn=7d4777589fa1f92d26ad05ffe3e02f6a&chksm=9b3f7f38ac48f62e0d2e4d46a13c21e440295aef4cba08214527d7b7d2e1959a0b4cebe4143a&scene=21#wechat_redirect>)

[答读者问 （十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)

问题

在“[答读者问 （九） 如何将数百个文件整合为一个矩阵](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485032&idx=1&sn=7d4777589fa1f92d26ad05ffe3e02f6a&chksm=9b3f7f38ac48f62e0d2e4d46a13c21e440295aef4cba08214527d7b7d2e1959a0b4cebe4143a&scene=21#wechat_redirect>)”中我们谈过类似的问题，这篇推送主要是将这个方法运用到我们的单细胞数据读取中。

怎么解决问题

比如我有这么个文件夹，其中有四个子文件夹

![](../../images/3ac3b79f5b1bc5cc.png)

每个子文件夹中包含的都是cellranger的输出文件

![](../../images/2dfb98b217a8c4f7.png)

我们来操作一下：

读入文件
```r
samples=list.files('data')#列出路径中的样本
samples
## [1] "Control1" "Control2" "Model1"   "Model2"
dir <- file.path('data',samples)#得到样本路径
names(dir) <- samples
dir
##        Control1        Control2          Model1          Model2
## "data/Control1" "data/Control2"   "data/Model1"   "data/Model2"
if(!require(Seurat))install.packages('Seurat')
## Loading required package: Seurat
## Warning: package 'Seurat' was built under R version 4.0.5
## Attaching SeuratObject
counts <- Read10X(data.dir = dir)
```

创建Seurat对象
```r
scRNA1 = CreateSeuratObject(counts,min.cells = 3, min.features = 200)
unique(scRNA1$orig.ident)#变量就存在这里
## [1] Control1 Control2 Model1   Model2
## Levels: Control1 Control2 Model1 Model2
scRNA1$sample <- scRNA1$orig.ident#你也可以转存一下
```

接下来走这两讲的内容就可以分析啦

[手把手教你做单细胞测序（三）——单样本分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484099&idx=1&sn=7825de19a42e220d8ff61db9e4ca669b&chksm=9b3f7b93ac48f28509c644f7ed6700ba6fed532e17cb82bdc7b6ee7032c02bfa9567cf050cbb&scene=21#wechat_redirect>)

[手把手教你做单细胞测序（四）——多样本整合](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484121&idx=1&sn=69f7ed1331c1d628b7b022bb47441926&chksm=9b3f7b89ac48f29f56daadcce0cb0b192e6ebc35802a09f1ecfc82b03d8dd992847adbc6d7d6&scene=21#wechat_redirect>)

![](../../images/2cc9316bafeedaf7.png)

如何联系我们

![](../../images/9b3df9175ed77a7e.gif)最近发现后台中有一些消息我没能及时看到并答复，微信后台中超过48h后便不允许回复读者消息，这里还是再给大家留一下答疑的扣扣号，方便大家随时交流。微信号可以点击**喜欢作者** 后自动回复里有。欢迎大家向我咨询或者提供建议。大家可以阅读完这几篇之后添加我：[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484331&idx=1&sn=94ad9cabc39f13fabf08a31862373093&chksm=9b3f7afbac48f3edc011f3e587920da27e68f7870fcfd119a7269b7053662e8bc85941a58d0b&scene=21#wechat_redirect>)
[答疑公约](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=1&sn=9bae98ae031cc9e546c35c4d2e60efd1&chksm=9b3f7accac48f3da7c3ee8ed308de8e52aa92284f6985ba43b59b70b3610cecb01c7295f7521&scene=21#wechat_redirect>)
[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)

![](../../images/d3f344df2ff09261.webp)
