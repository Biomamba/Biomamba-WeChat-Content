---
title: "如何在一张FeaturePlot上同时画多个基因"
date: 2023-05-16
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499801&idx=1&sn=e9022989784d156e73da06640b16e0df&chksm=9b3cb949ac4b305f8a6c070ba7e0c1d94690c8d881af5128a758b2ca422cf5b74560c4c258b8#rd
albums: ["答读者问"]
---

# 如何在一张FeaturePlot上同时画多个基因

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499801&idx=1&sn=e9022989784d156e73da06640b16e0df&chksm=9b3cb949ac4b305f8a6c070ba7e0c1d94690c8d881af5128a758b2ca422cf5b74560c4c258b8#rd
> 合集：答读者问

问题

```r
library(Seurat)
```
```
## Warning: 程辑包'Seurat'是用R版本4.2.2 来建造的
```
```r
scRNA <- readRDS('pbmc.rds')
```

学过我们B站课程的同学想必都很熟悉`FeaturePlot`函数，我们来看看`FeaturePlot`的最简单用法：
```
FeaturePlot(scRNA,'PTPRC')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyUFUuSWofqXEft76QexAvVIjTia6dCl2LWgDL8rKCplf8mowGLev7eNia06UicjaYQZBoInUhkmbiaXw/640?wx_fmt=png) 当输入两个基因时，`FeaturePlot`就会自动将两个基因分别作图：
```
FeaturePlot(scRNA,c('PTPRC','CD3E'))
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyUFUuSWofqXEft76QexAvV9HWplEgcdbrNVuw9NnJs4H3nRib9xSCN2cwHmS6ESmCEWpRMRSTCnpg/640?wx_fmt=png) 问题来了，如何将这两个基因画在**一张图** 上呢？

如何解决问题

  * # **画法一**

其实作者早就想到你们的需求啦，简单的加一个`blend = T`选项，不仅能画在一张图中，甚至还能查看相关性
```
FeaturePlot(scRNA,c('PTPRC','CD3E'),blend = T)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyUFUuSWofqXEft76QexAvVC6JZia7JXJO27rueNG55nZxhHbiacYPNPmPmPbfo5GceUqmvmaAwp5WQ/640?wx_fmt=png)

但是，当基因数量超过2个时，这个函数便会报错，遂有画法二
```
try(FeaturePlot(scRNA,c('PTPRC','CD3E','CD3G'),blend = T))
```
```
## Error in FeaturePlot(scRNA, c("PTPRC", "CD3E", "CD3G"), blend = T) :
##   Blending feature plots only works with two features
```

  * # **画法二**

数据整理：
```r
library(dplyr)
```
```
## Warning: 程辑包'dplyr'是用R版本4.2.2 来建造的
```
```
##
## 载入程辑包：'dplyr'
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
mydata <- scRNA@reductions$umap@cell.embeddings
myexpr <- as.data.frame(scRNA@assays$RNA@data)[c('CD79A','CD3E','GZMB'),]%>%
        t()
mydata <- cbind(mydata,myexpr) %>% as.data.frame()
head(mydata)
```
```
##                     UMAP_1     UMAP_2    CD79A     CD3E     GZMB
## AAACATACAACCAC-1  3.001694   3.751682 0.000000 2.226555 0.000000
## AAACATTGAGCTAC-1  5.673855 -12.254552 1.962726 0.000000 0.000000
## AAACATTGATCAGC-1  5.428529   5.915791 0.000000 1.995416 0.000000
## AAACCGTGCTTCCG-1 -8.592008  -3.628471 0.000000 0.000000 1.566387
## AAACCGTGTATGCG-1  2.763551  -2.193586 0.000000 0.000000 4.815828
## AAACGCACTGGTAC-1  2.877154   5.927556 0.000000 2.326928 0.000000
```

画图：
```r
library(ggplot2)
```
```
## Warning: 程辑包'ggplot2'是用R版本4.2.2 来建造的
```
```r
library(ggnewscale)
```
```
## Warning: 程辑包'ggnewscale'是用R版本4.2.2 来建造的
```
```
ggplot(mydata,aes(x=UMAP_1,y=UMAP_2))+
  geom_point(data = mydata,aes(x=UMAP_1,y=UMAP_2,
                               color=CD79A),size=1)+
  scale_color_gradient('CD79A',low = alpha('grey',0.1),#防止覆盖，把灰色的点透明度设置的高一些
                       high = alpha('#8A2BE2',1))+#喜欢什么颜色大家自己调吧
  new_scale('color')+
  geom_point(data = mydata,aes(x=UMAP_1,y=UMAP_2,
                               color=CD3E),size=1)+
  scale_color_gradient('CD3E',low = alpha('grey',0.1),
                       high = alpha('red',1))+
  new_scale('color')+
  geom_point(data = mydata,aes(x=UMAP_1,y=UMAP_2,
                               color=GZMB),size=1)+
  scale_color_gradient('GZMB',low = alpha('grey',0.1),
                       high = alpha('#228B22',1))+
  theme_bw()
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyUFUuSWofqXEft76QexAvVFic51SGWhFdibhqsH1hib4icOwRBZkuMwIUOozwqIZ48rP737Y2RQFFyDA/640?wx_fmt=png)

链接及测试文件

链接：

https://pan.baidu.com/s/1k9UgBTzGpMLNLWjx3FlSJA?pwd=25s5
提取码：25s5

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyUFUuSWofqXEft76QexAvVicQ1aLY6Uib3dLamIibLAzDzicDhiao6ZicVHlLp4TCohQZPtlZvIQ34b9hg/640?wx_fmt=jpeg)

若链接失效可以文末联系客服领取~

往期回顾

[答读者问（一）单基因究竟能否进行GSEA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484175&idx=1&sn=3e45ad62b045a541874e5ae7ca03f849&chksm=9b3f7a5fac48f349f8893500825d2c6b4ff581fbb0816c1074d88a0dbbb4a612c1e1bb3740bb&scene=21#wechat_redirect>)

[答读者问（二）为什么我的PCA分析报错了？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484248&idx=1&sn=b1fe7174a28562d01422e43609f41709&chksm=9b3f7a08ac48f31e3bbfdb4a9824dadf25a8fa3ff9b78dd15d646ae4c3da5db04e2e4acfba3d&scene=21#wechat_redirect>)

[答读者问（三）单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)

[答读者问（四）如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)

[答读者问（五）如何实现各物种基因的ID/symbol的转换](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484353&idx=2&sn=8fccb88c871a42c803e313be157ab293&chksm=9b3f7a91ac48f387df8b462f7318596fc5c645d6f05eefac2c598ff6875c0a2eeb902aaf5a15&scene=21#wechat_redirect>)

[答读者问（六）Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484376&idx=2&sn=9fda8a5261e86f889a58d607163ce0fd&chksm=9b3f7a88ac48f39ea9c19e256a513c9ae80c6f6dc1724b7783884e23981e2061c78fa67071c9&scene=21#wechat_redirect>)

[答读者问（七）有人问我Biomamba何解](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484550&idx=1&sn=ec4466084c1c9eba7eb292e95f33b5bb&chksm=9b3f7dd6ac48f4c042b4e9df2abd717b1354b4914c3f7510eaf444e97965a0f6622979e710e0&scene=21#wechat_redirect>)

[答读者问（八）为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)

[答读者问（九） 如何将数百个文件整合为一个矩阵](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485032&idx=1&sn=7d4777589fa1f92d26ad05ffe3e02f6a&chksm=9b3f7f38ac48f62e0d2e4d46a13c21e440295aef4cba08214527d7b7d2e1959a0b4cebe4143a&scene=21#wechat_redirect>)

[答读者问（十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)

[答读者问（十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)

[答读者问（十二）ERROR: have no zero exit status](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485290&idx=1&sn=1e77059439342374ea03496cbba08070&chksm=9b3f7e3aac48f72ca08f5e73496e6f8c99c5fd74a39daa626d636ba5a7b0b89873437ebcb6d4&scene=21#wechat_redirect>)

[答读者问（十三）查看Seurat对象时的ERROR：type='text'](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)

[答读者问（十四）Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)

[答读者问（十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)

[答读者问（十六）做单细胞测序到底需要多少内存](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487923&idx=1&sn=15043c6d729b0d5493ab875b0e54a259&chksm=9b3f68e3ac48e1f5dae514a01c857f9a56a90e2977dd7862db28d06fe55888cd9bb4afbb14e0&scene=21#wechat_redirect>)

[答读者问（十七）调用的线程越多就算的越快嘛?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488995&idx=1&sn=7140e0d037671542fb37dff3a3c94b28&chksm=9b3f6cb3ac48e5a5f54a02be9e6af9f5a4cf8da1de1770f9035130c84dedf059a024964fc15a&scene=21#wechat_redirect>)

[答读者问（十八）一个我至少被问过30遍的monocle报错](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25&scene=21#wechat_redirect>)

[答读者问（十九）R语言内存问题-Error: cannot allocate vector of size ** Gb](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492912&idx=1&sn=c721a8d64e621832bf5518ab1f26d9fe&chksm=9b3c9c60ac4b1576ad617ff9f2f13a8d811ce41dab4a178c8e00a940fd1d3c4400c6b39d779e&scene=21#wechat_redirect>)

[答读者问（二十）四个单细胞样本只给了一套文件怎么读](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494879&idx=1&sn=c2287ab3684792747dfac53d6704462b&chksm=9b3c958fac4b1c994a4b075c4f8475816e121966fa8c52cb0a2ce8c14987988ab9bdb49bdf69&scene=21#wechat_redirect>)

[答读者问| 21.申请生信博士需要满足什么条件](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247494904&idx=1&sn=207c0ee573206c5d7f282f8f14680394&chksm=9b3c95a8ac4b1cbe434b0319839f984fcd01eb173cf40193b7213d059aace6fea73499ac2d79&scene=21#wechat_redirect>)

[答读者问| 22.object 'CsparseMatrix_validate' not found](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496273&idx=1&sn=fd5a92dd7fdc349b1624784ca74b1220&chksm=9b3c8b01ac4b0217cf06d89bfea49c3fa0c9b580957338c0cc8f55ede3e8f65d6d7162ae27e3&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息更新不及时，超过48h便不许回复读者消息，这里给大家留一下领取资料及免费服务器的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
