---
title: "这下真手把手教你做scRNA-seq数据基础分析"
date: 2025-03-18
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528175&idx=1&sn=f1e4b73fcdb4e1ee9dfa8bfc641b1474&chksm=9b3c17bfac4b9ea9f4436fc8f3e82b225b17adb3aa2da784cb02407b9f4ff6ae87ac130f4277#rd
albums: ["单细胞教程全收录", "生信基地"]
---

# 这下真手把手教你做scRNA-seq数据基础分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528175&idx=1&sn=f1e4b73fcdb4e1ee9dfa8bfc641b1474&chksm=9b3c17bfac4b9ea9f4436fc8f3e82b225b17adb3aa2da784cb02407b9f4ff6ae87ac130f4277#rd
> 合集：单细胞教程全收录 / 生信基地

![图片](../../images/c33e327c8d66af99.webp)

手把手教你做scRNA-seq数据基础分析

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)离我们最开始做单细胞教程已经过去四五年，现在已经收获了40w+的阅读量。一共940min的教程相信足够大家完成单细胞的学习与文章发表，我们也陆陆续续收到小伙伴们的发文致谢：[致谢合辑](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3425248581018714114#wechat_redirect>)。![](../../images/febe34fb2a90ca52.webp)
一方面随着时间飞逝，原先教学中的一些内容已然过时，毕竟我们最初的演示是基于Seurat V3，而现在V5上线都已经快两年了。另一方面很多同学由于缺少编程、单细胞、文章套路等基本知识，跟着视频并不能完全自学掌握单细胞分析技能。因此，基于最新的R环境与Seurat版本，我们重新组织、修订了《手把手教你做单细胞测序数据分析》课程。04月12日~13日在[生信基地](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526229&idx=1&sn=0718f1702150ba77a7f7e3beadd6e0ba&scene=21#wechat_redirect>)（线上/线下均可参与，错过直播也可以加入录播/答疑+循环开课）也希望真的能够做到“手把手”的带大家完成单细胞测序数据分析的学习，当然，我们拒绝生信快餐，课后欢迎大家随时在群里对课程内容提问~报名即送[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)回放与答疑服务。自学能力强的小伙伴也可以直接跟B站教程：
https://www.bilibili.com/video/BV1S44y1b76Z/
参与此次课程你将获得：1、单细胞数据分析教学指导与答疑2、开箱即用(我们已经布置好了环境)的单细胞分析环境：[学习版上架啦~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)3、[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)回放、答疑群、讲义4、scRNA-seq基础分析手册、代码、测试文件
教程图片集锦：![](../../images/b97cf6158fafd79a.webp)

**报名联系方式**

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/19b4ec51a30e79aa.webp)![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

课表

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)![](../../images/2553c7a252a7a46f.webp)![图片](../../images/3ea5072afd1f3798.webp)![图片](../../images/c33e327c8d66af99.webp)

学习资料

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家报名后可入群领取：

![](../../images/d768e9095bef652c.gif)

![](../../images/bfbd27dbaedc735d.webp)

测试文件，总大小5.1GB：

├── GSE139107

│ ├── GSE139107_MouseIRI_12hours.dge.txt.gz

│ ├── GSE139107_MouseIRI_14days.dge.txt.gz

│ ├── GSE139107_MouseIRI_2days.dge.txt.gz

│ ├── GSE139107_MouseIRI_4hours.dge.txt.gz

│ ├── GSE139107_MouseIRI_6weeks.dge.txt.gz

│ └── GSE139107_MouseIRI_control.dge.txt.gz

├── GSE139107_MouseIRI.metadata.txt.gz

├── MonacoImmuneData.rds

├── bcell.marker.CSV

├── cg.rds

├── color.Rdata

├── data.txt

├── filtered_gene_bc_matrices

│ └── hg19

│ ├── barcodes.tsv

│ ├── genes.tsv

│ └── matrix.mtx

├── iri.intergrate.harmony.rds

├── iri.intergrate.harmony.rename.rds

├── iri.intergrate.havebatch.rds

├── iri.intergrate.havebatch.v5CCA.rds

├── iri.intergrate.rds

├── iri.obj4.rds

├── iri.obj5.rds

├── my.pbmc.tar.gz

├── mycount.txt

├── panc8.rds

├── pbmcrenamed.rds

└── single_cell_datamatrix.txt

3 directories, 27 files

![图片](../../images/f74ae4c6b8127d36.webp)
![图片](../../images/c33e327c8d66af99.webp)

报名费用

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

2天满满的课程（算上R语言就是四天课程啦）只要799￥，相信比小学生补课班还便宜。支持对公。

![图片](../../images/f74ae4c6b8127d36.webp)
![图片](../../images/c33e327c8d66af99.webp)

线下学习环境

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)**地点** ：南京市江宁区，详细地址报名咨询**
****往期活动现场：****![图片](../../images/3f74e0867146793e.webp)**

![图片](../../images/12c0fb2583392c36.webp)

除了知识之外，现场还能够给大家提供：

**茶水吧、咖啡机、零食柜**![图片](../../images/cfb629a079c6214b.webp)

**各类饮料、零食小吃**

![图片](../../images/e865bd94adee0a2e.webp)

![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([免费两周学习版上架啦~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流（别问在么，添加时直接说来意）。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/19b4ec51a30e79aa.webp)![图片](../../images/acba43cb3408c3d0.gif) 您点的每个赞和在看，我都认真当成了喜欢
