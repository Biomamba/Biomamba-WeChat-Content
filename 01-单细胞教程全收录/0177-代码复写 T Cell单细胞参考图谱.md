---
title: "代码复写| T Cell单细胞参考图谱"
date: 2024-01-03
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506779&idx=1&sn=dc97a74cfac6caeabaa838160385c3b2&chksm=9b3ca20bac4b2b1da51998764b22ac3c08415298a47ded14283337386f18f9548749de70725e#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写| T Cell单细胞参考图谱

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506779&idx=1&sn=dc97a74cfac6caeabaa838160385c3b2&chksm=9b3ca20bac4b2b1da51998764b22ac3c08415298a47ded14283337386f18f9548749de70725e#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是04号作品。本作品复写了题为"Interpretation of T cell states from single-cell transcriptomics data using reference atlases"的论文，**文章链接** ：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8137700/**物种** ：人。**数据链接** ：https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129785**文章思路** ：

![](../../images/f721b3b1e00d5082.webp)

复现图片集锦：

![](../../images/4bb3fd11ee4ae5d9.webp)

论文基本介绍与解读参赛人未提供.

一、复写内容

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
rm(list = ls())#加载包#library(multtest)library(Seurat)library(dplyr)library(tidyverse)
#读入数据（参考数据）及待分析数据pbmc.data <- Read10X('/home/data/sbc059/xunyin')pbmc <- CreateSeuratObject(counts = pbmc.data, project = "ova", min.cells = 3, min.features = 200)ref <- readRDS("/home/data/sbc059/yyy/ref_TILAtlas_mouse_v1.rds")#ProjectTILs参考数据集
#设置颜色palette <- c("#edbe2a", "#A58AFF", "#53B400", "#F8766D", "#00B6EB", "#d1cfcc", "#FF0000",             "#87f6a5", "#e812dd", "#777777","#0000FF","#8B2323","#CDAA7D")#运行ProjectTILsquery.projected <- Run.ProjecTILs(pbmc, ref=ref)#投影绘图plot.projection(ref, query = query.projected, linesize = 0.5, pointsize = 0.2)#雷达图genes4radar = c('Tox','Ccr7','Cd4','Cd8a','Foxp3','Gzmb','Gzmk',                'Havcr2','Mki67','Pdcd1','Tcf7')plot.states.radar(ref, query = query.projected, genes4radar = genes4radar, min.cells = 5,cols = '#edbe2a')
#提取CD8_TexIdents(query.projected) <- query.projected$functional.clusterCD8_Tex <- subset(query.projected,idents=c('CD8_Tex'))plot.discriminant.3d(ref, query = CD8_Tex,extra.dim = 'cycling.score',labels.col = 'functional.cluster')
```

输出图片：

Fig.2d：

![](../../images/2e22ebc8fabb671b.webp)

Fig.2e：

![](../../images/687fb6f882c0683c.webp)

Fig.2f

![](../../images/7e11a6db998a21bf.webp)

Fig2.g1:

![](../../images/4f024a8f99c7b94d.webp)

Fig.2g2:

![](../../images/e46913b3f2365d09.webp)

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/1SsJ8WWZ9qSsE_3bg5a-QYQ?pwd=btsh

![](../../images/cad1fcec8bfa06da.jpg)

02

三、合作方介绍

****本次活动由**Biomamba生信基地** 组织主办、**北京寻因生物科技** 有限公司独家冠名、科研者之家、西柚云超算联合赞助，设立总价值约**50W** 的科研助力基金。
北京寻因生物科技有限公司：

北京寻因生物科技有限公司（简称寻因生物）成立于2018年，秉承“用技术温暖生命，预见未来”的企业愿景，致力于全球单细胞市场标准普世化发展，推动单细胞技术在早筛、临床、药研等应用方向的深耕落地，为全球科学家、技术公司及药企工业等客户提供可信赖的高品质单细胞技术服务及实验室建设解决方案。

科研者之家：

科研者之家（www.home-for-researchers）是目前国内最知名的科研工具箱平台，以“科研不停，神器不止”为理念，自2019年上线以来，多款工具火爆科研界，如AI写作助手、Figdraw在线绘图平台、生信零代码平台、AI润色、DLP一键改写降重、中文版Pubmed、课题思路助手等。截止目前，包括Nature，Advanced Materials等顶级期刊在内，科研者之家相关科研工具被论文引用已超2300次之多。

西柚云超算：

西柚云是一家专注于科研共享计算的云服务基建型公司。于2022年推出独立研发的大禹共享型计算系统，具有实例动态迁移（拒绝传统型共享服务器单节点卡顿）、开箱即用的生信环境、每个用户拥有[独立的实例和root权限](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)等特性。

03

四、往期作品回顾

[干细胞样CD4+ T细胞与自身免疫性血管炎](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506684&idx=1&sn=c27703a05d4fffae6a5e9e54b4fa7dfe&chksm=9b3ca3acac4b2abaa1e5d4f4a7e4d0730f2e5c4d72c7b3d3d29a653c3bae6590d90e31908dde&scene=21#wechat_redirect>)
[结直肠癌免疫图谱中的基因表达程序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506720&idx=2&sn=4760277df5a7b6f0d6d1698ac734aa3b&chksm=9b3ca270ac4b2b66b0330e822893fa233ba3bdfd45d857097fba6e86561196c1497c20db25b8&scene=21#wechat_redirect>)
[MLP模型鉴定免疫细胞发育和瘤内T细胞耗竭的单细胞染色质图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506754&idx=1&sn=3e3e9b4857bb0371b7c1113df792df2e&chksm=9b3ca212ac4b2b043baf0c72684d186a1c065ff7b3d865c308aff4f3483ab5923638fda8d1ff&scene=21#wechat_redirect>)

04

**本次活动最终解释权归主办方所有!********主办方拥有对作品的编辑、宣发权利!**

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](../../images/f24109c3fc7128df.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
