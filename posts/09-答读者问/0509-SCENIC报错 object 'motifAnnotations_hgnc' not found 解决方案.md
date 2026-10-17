---
title: "SCENIC报错  object 'motifAnnotations_hgnc' not found 解决方案"
date: 2026-04-19
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537452&idx=1&sn=931d71c9dcfdd64feca3f099c258cc3e&chksm=9b3c2a7cac4ba36a14d198f5ccefa796069658ce883cbf9297021fe1e282467596c601c3915f#rd
albums: ["答读者问"]
---

# SCENIC报错  object 'motifAnnotations_hgnc' not found 解决方案

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537452&idx=1&sn=931d71c9dcfdd64feca3f099c258cc3e&chksm=9b3c2a7cac4ba36a14d198f5ccefa796069658ce883cbf9297021fe1e282467596c601c3915f#rd
> 合集：答读者问

**一、遇到问题解决问题**

有群友跑SCENIC教程时遇到了如下报错，怎么说呢，千错万错都是[版本的错](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535577&idx=1&sn=d38e5da6971ad77d0b5cb83a7026f2c6&scene=21#wechat_redirect>)。应该是[SCENIC](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528198&idx=2&sn=86d1324d8f65c91f1221acfb1f984520&scene=21#wechat_redirect>)和RcisTarget的版本没协调好，现在的情况是这个内置版本不能自动加载了，需要显式的手动加载出来才能使用。![](../../images/72bf8b5268528f4f.webp)
手动加载这个数据就好：

  *   *   *   *

```r
library(RcisTarget)library(SCENIC)data(list="motifAnnotations_hgnc_v9", package="RcisTarget")motifAnnotations_hgnc <- motifAnnotations_hgnc_v9
```

如果是分析小鼠的数据，需要换一下物种：

  *   *   *

```r
data(list="motifAnnotations_mgi_v9", package="RcisTarget")motifAnnotations_mgi <- motifAnnotations_mgi_v9   # 赋值给通用变量名
```

**二、打铁还需自身硬**

[ SCENIC](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528198&idx=2&sn=86d1324d8f65c91f1221acfb1f984520&scene=21#wechat_redirect>)是[R语言scRNA-seq基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)的核心软件之一，往期针对SCENIC出来不少技术贴，可按需查阅：

[SCENIC单细胞转录因子预测|1.学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)

[SCENIC单细胞转录因子预测|2.绪论](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500098&idx=1&sn=8c31241bd259e303a6ac3c9740f298d9&chksm=9b3cb812ac4b31046fd298c8ee5f0bc0de445df62b234bd934c34ca655e61de3da54d81e2053&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)

**[SCENIC单细胞转录因子预测|3.软件安装与数据准备](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500631&idx=1&sn=5d73db4dcc74b66de07dee9db910bb83&chksm=9b3cba07ac4b3311d1820bb305778aea707294f19fd6ff2631cd003da80bdcff8f8bc8ed34de&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)****[SCENIC单细胞转录因子预测|4.精简版流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)****[SCENIC单细胞转录因子预测|5.step1+step2构建共表达网络与regulon](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501692&idx=1&sn=3f7e263a93942ad03faa1ba5f8694ec4&chksm=9b3cbe2cac4b373af9db74a50ffb08a9b8a3b958fc6385c937385f0f7323bc935cdb0fe5275c&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)****[SCENIC单细胞转录因子预测|6.Step3 利用AUCell对Regulon评分](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501989&idx=1&sn=2700bf779d7d261a4d751d1635fdce2c&chksm=9b3cb1f5ac4b38e3014476242fe956cf510cc45b9f4cef86070af8094fd5f884f9d5c3a3363f&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)****[SCENIC单细胞转录因子预测|7.Step4 二元矩阵的计算与可视化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503995&idx=1&sn=26c7e9ec56af434e62b02853cfe667d6&chksm=9b3ca92bac4b203d7986645ab5a3fb574f44185c7ced8bd47957fa237d436a95bfa2579d052a&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)****[SCENIC单细胞转录因子预测|8.Step5 regulon聚类、分群、降维](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504024&idx=1&sn=143c0ec4d94b8fca0a4a47d3dc24415b&chksm=9b3ca9c8ac4b20de70a87acb2d3f810b0e1497071b1c6f14f1882a6d844fff016e9ba5581eb3&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)****[SCENIC单细胞转录因子预测|9.下游探索](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505276&idx=1&sn=949c753feb85d5877121433caaa33013&chksm=9b3cac2cac4b253affb587a937d3f5e0576851a4f4e1570cb7510a594d155873961bbd91758d&scene=21&token=2143911808&lang=zh_CN#wechat_redirect>)**[ SCENIC转录因子调控网络图](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530488&idx=2&sn=cc79762d4d7aa42673871b2472808852&scene=21&token=2143911808&lang=zh_CN&poc_token=HENKTmmj0Cx7WBCzELeDx6YKH9OBvrd8SfGcxKAA#wechat_redirect>)**[比R版本快几十倍| Pyscenic单细胞转录因子预测](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528198&idx=1&sn=2bdac420c143423d8a7012d028473573&scene=21&token=2143911808&lang=zh_CN&poc_token=HFtKTmmjNq6m1a_gdOq7CBnds8Nb1O9z899DxoXz#wechat_redirect>)****[非模式物种PySCENIC分析流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528411&idx=1&sn=efa4ace804c343379073dea63de64b4e&scene=21#wechat_redirect>)**[ R+Python组合拳可能是分析SCENIC最好的方式](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530488&idx=1&sn=e0c57d42b1ecb73e8b7b9f6caecbb81d&scene=21#wechat_redirect>)

# [一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)

# [scRNA-seq基因共表达网络分析合辑](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530020&idx=2&sn=a41e26954103818eaa409f854f61dcb7&scene=21#wechat_redirect>)

#

如果你想彻底吃透[SCENIC转录因子调控网络图](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528198&idx=2&sn=86d1324d8f65c91f1221acfb1f984520&scene=21#wechat_redirect>)或者[一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)全套内容、跟着老师系统学习，可以报名参加我们的专题课程班：[R语言scRNA-seq基因共表达网络分析专题](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535877&idx=5&sn=23f42e58509a93e1f91c09cad53ccbdf&scene=21#wechat_redirect>)

[![](../../images/2d7a4a8961be90ec.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535877&idx=5&sn=23f42e58509a93e1f91c09cad53ccbdf&scene=21#wechat_redirect>)

#

![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/e43581b4f5118aad.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
