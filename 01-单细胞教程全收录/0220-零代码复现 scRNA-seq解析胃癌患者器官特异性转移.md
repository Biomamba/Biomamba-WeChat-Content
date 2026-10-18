---
title: "零代码复现| scRNA-seq解析胃癌患者器官特异性转移"
date: 2025-04-03
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528326&idx=1&sn=1979536cb00756f263031d5e640177d3&chksm=9b3c16d6ac4b9fc0259d5d48daf533e8c39c2d3736f99ec452a5016b82b178255c4d84eace95#rd
albums: ["单细胞教程全收录", "单细胞云平台", "粉丝来稿"]
---

# 零代码复现| scRNA-seq解析胃癌患者器官特异性转移

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528326&idx=1&sn=1979536cb00756f263031d5e640177d3&chksm=9b3c16d6ac4b9fc0259d5d48daf533e8c39c2d3736f99ec452a5016b82b178255c4d84eace95#rd
> 合集：单细胞教程全收录 / 单细胞云平台 / 粉丝来稿

**
**

**写在前面**

当今基因测序数据量在爆炸性增加，生信分析面临着**算力要求高** 、**代码** 软件**繁多** 、科研人员**协作分析困难** 等一系列痛点。为解决这些问题，各种生信云平台应运而生，它提供了一系列生物信息学工具和资源，用于支持科研人员在生物学数据的分析、可视化和解释方面的需求。SeekSoul Online便是其中一个，相信对于想要快速上手单细胞数据分析的你来说会是个惊喜：

云平台地址：

https://seeksoul.online/t_static/Biomamba/Biomamba.html

使用教程可见：

[一文学会零代码单细胞分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511007&idx=1&sn=e7be3d9775890e5717889714629cfaf5&chksm=9b3cd28fac4b5b9936428d5f74d8b581b5cddc18d0fc42e2a5d75604cce080588d50f1304a17&scene=21#wechat_redirect>)

[零代码单细胞视频教程](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_2095d655e3b&enterid=1715838775&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1#wechat_redirect>)

各位同学需要**联系您的专属在线客服，获取demo数据后，进行操作学习。**

**![图片](../../images/239ea5459d709578.webp)**

**
**

**文章介绍**

**复现文章****标题：** 《Revealing the transcriptional heterogeneity of organ‐specific metastasis in human gastric cancer using single‐cell RNA Sequencing》复现集锦：![](../../images/988ed1cea6a3683b.webp)

**发表日期和杂志：** 2022年发表在Clinical and Translational Medicine上

**在线阅读链接：** https://doi.org/10.1002/ctm2.730

![图片](../../images/efe8fb58e1168743.webp)

**单细胞实验设计：** 使用了单细胞RNA测序技术评估了来自6名患者的10个新鲜人体组织样本，共计42,968个细胞。

![图片](../../images/a8601ed9df78590f.webp)

**数据链接是：** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE163558

**样品详情：**

  * 来自6名患者的10个新鲜人体组织样本，包括3个原发性肿瘤样本(PT)、1个邻近非肿瘤样本(NT)和6个转移样本(M)
  * 转移样本包括 2个肝脏转移样本(Li)、2个淋巴结转移样本(LN)、1个腹膜转移样本(P)和1个卵巢转移样本(O)

**主要分析结果：**

单细胞数据来自6名患者的10个新鲜人体组织样本，包括3个原发性肿瘤样本(PT)、1个邻近非肿瘤样本(NT)和6个转移样本(M)

![图片](../../images/81d215e581ddffd3.webp)

经过质量过滤，共检测到42 968个细胞，在降维和无监督细胞聚类之后，鉴定出七个细胞亚群：

  * 上皮细胞(1743;EPCAM, KRT19, CLDN4)
  * 基质(1288;PECAM1, CLO1A2, VWF)
  * 增生细胞(1089;Mki67, stmn1, pcna)
  * T细胞 (24 448;Cd3d, cd3e, cd2)
  * B细胞 (7708;CD79A, IGHG1, MS4A1)
  * NK细胞(NK, 1173;KLRD1, GNLY, KLRF1)
  * 髓系(5519;CSF1R、CSF3R、CD68)

![图片](../../images/045a3acf439f93ce.webp)

在不同的原发肿瘤和转移瘤中，每种细胞系的比例差异很大，揭示了一种异质性的细胞状态。

![图片](../../images/7fe0259115f64d02.webp)

恶性与非恶性上皮细胞分析通过特定的恶性和非恶性评分，系统定义了1615个恶性上皮细胞和128个非恶性上皮细胞，分析发现其中83%的非恶性上皮细胞来源于非肿瘤样本(NT)

![图片](../../images/c8ebd743e8e07869.webp)

**seeksoul云平台分析复现**

学完了1.5d的课程后，这位同学已经可以输出以下内容啦，其实很多复现的内容相差无几，甚至图片要比原文更加美观~

具体分析方法可参考[一文学会零代码单细胞分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511007&idx=1&sn=e7be3d9775890e5717889714629cfaf5&scene=21#wechat_redirect>)推文，或者根据对应的视频讲解学习

### 1.数据上传及分析

使用云平台分析

首先是将下载整理好的原始数据上传到云平台，选择**数据上传——单样品数据——matrix矩阵格式，然后上传对应的三个文件即可**

![图片](../../images/fb7012a4b7db38ca.webp)

上传好数据后，选择需要进行分析的数据，点击**快速创建流程** ，填写好需要的信息，即可上传数据进行分析，可以再已选数据中整理需要的分组信息

![图片](../../images/412e047a1c9c63d8.webp)![图片](../../images/8474a4a5c103448f.webp)

然后就是初始化数据，会统计`nferture、ncount以及mito线粒体基因占比`，然后进行过滤、整合等基本分析流程即可

![图片](../../images/e0ec571c657f6321.webp)

**细胞注释：使用是0.5的分辨率，基于singleR自动注释+AI注释，结果较为准确**

![0.5分辨率](../../images/e8033f6b850cd60b.webp) 0.5分辨率![Figure1C](../../images/045a3acf439f93ce.webp)Figure1C![注释结果](../../images/37fca0399b4be4d3.webp)注释结果

**当运行完基础分析，以及进行细胞注释之后，可以使用画图工具，基于需要展示的分组信息进行可视化**

画图工具使用

**打开画图工具之后，可以使用右下角的添加图组——添加一块新的画布，比如新建一个新的tsne结果，用于展示文献的Figure1B**

![图片](../../images/833d0ccf0903be72.webp)

**添加好图组之后，在打开图组的情况下，选择` 添加模块`，即可新建新的图表，可以展示的图表类型有小提琴图、降维图、FeaturePlot、Dotplot、分组统计图以及热图**

![图片](../../images/7934dc8511c1c4f7.webp)

**文献中的figure1B就是展示了不同分组的tsne结果，所以我们在图组里面选择需要的分组进行展示即可**![图片](../../images/f9865f086d3cd5e0.webp)

![Figure1B](../../images/81d215e581ddffd3.webp) Figure1B![复现结果](../../images/43c8c1e588c2b965.webp)复现结果

**top基因集热图展示**

![图片](../../images/bea3d6a1c2ee5503.webp)

**细胞比例图**

![图片](../../images/54d5f471c71870ca.webp)

**文献中是汇总了两个分组的细胞比例堆叠柱状图，所以可以选择不同的分组进行展示**

![Figure1F](../../images/61ed46a436529bf5.webp) Figure1F

**添加模块之后，选择分组统计图进行展示，这时候要注意选择分组因子为celltype的注释信息，拆分因子为需要展示分组信息**

![图片](../../images/bdb4796128720ea3.webp)![图片](../../images/c9868c3bddb4660a.webp)
差异富集分析

**在差异富集分析选项中，可以选择全部的细胞亚群作为细胞分组，在比较组合里面可以选择需要的分组信息，这边选择是PT、NT以及转移M的分组**

![图片](../../images/9caa381717f5fd96.webp)

选择全部细胞亚群进行分组，会依次基于B细胞亚群，在PT和NT之间的差异，PT和M之间的差异，选择好需要的分组信息

![图片](../../images/e9d718df4e8e3e10.webp)

选择展示哪一群就会高亮哪一群，可以使用火山图等展示差异基因

![图片](../../images/93c94d2d225cd725.png)![图片](../../images/f79318b489ef1e0c.webp)![图片](../../images/8cbc41b580a6ab25.webp)![图片](../../images/2a479f245c514ba3.webp)

### 高级分析系列

**在seeksoul云平台上面提供了很多可供选择的高级分析系列，比如拟时序分析，可以选择moncle3或者monocle2，还有infercnv分析和copyKAT分析**

![图片](../../images/f3943e72c49940d7.png)

在FAQ帮助文档里面有详细的介绍

![图片](../../images/3d75cc2e37e8e347.webp)

#### infercnv分析

尝试了使用infercnv去分析上皮细胞，选择的是B细胞和mast细胞作为参考，提交后15分钟完成了分析，速度较快

![图片](../../images/3645b8611910339b.webp)

**分析完后，提供了可以下载的分析报告**

![图片](../../images/49340fa64072b9cd.png)

**结果中有完整的分析结果报告的html文档**

![图片](../../images/7c0fc2abb79a4471.webp)![图片](../../images/5a608b1c13c8effc.webp)

**高级分析可选择内容较多，就没有一一尝试啦，但整体分析耗时较少，可供选择内容较多，对分析有很大的帮助**

**
**

Seeksoul 单细胞平台使用感受

  1. 整体而言分析较为简便快捷，上传好数据之后，创建好对应的分析项目，然后进行分析即可
  2. 提供多种可以选择的高级分析，在差异富集分析选项中，能很方便的选择需要的细胞亚群以及分组信息进行比较
  3. 在画图工具里面，可以基于不同的分组信息进行可视化，对应到seurat分析中的group.by和split.by参数
  4. 除了基础的降维聚类分群注释分析功能外，还有很多高级分析系列，一个分析提供了不同版本和软件的选择，可以多运行选择需要的结果

**整体而言对于新手较为友好，配色选择也很合适，能不使用代码就完成分析，对于新手而言非常nice！**

**最后，感谢Biomamba，师兄带领Biomamba生信基地联合Seeksoul寻因生物，提供学习分析平台的机会，以及在培训过程中的耐心解惑。希望 Biomamba生信 基地和寻因生物做大做强，越来越好！**

**视频教程**

本系列视频我们将进行拆解动作，完整视频教程可见合集：

[SeekSoul® Online单细](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_1006a9b5456&enterid=1729128003&from_msgid=2247522176&from_itemidx=2&count=3&nolastread=1#wechat_redirect>)

[胞云平台](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_1006a9b5456&enterid=1729128003&from_msgid=2247522176&from_itemidx=2&count=3&nolastread=1#wechat_redirect>)

总是有小伙伴在学我们的单细胞**代码** 教程(**[两百篇单细胞知识帖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522475&idx=1&sn=84dd9a65348528be9aa2b8d2711d776c&scene=21#wechat_redirect>)**)时深感头疼，密密麻麻的代码、繁琐的流程、巨大的数据量，这些都是劝退大家的门槛。这对这一现象，**Biomamba** 联合**寻因生物** 发布了科研利器——**[SeekSoul Online单细胞云平台](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_69f8cb7b2da&enterid=1713928791&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1&token=1053256417&lang=zh_CN#wechat_redirect>)** 及对应的**《[ 2周教你学会单细胞生信全套分析](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_69f8cb7b2da&enterid=1713928791&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1&token=1053256417&lang=zh_CN#wechat_redirect>)》**课程，准备好**零代码** 发单细胞文章吧！

云平台访问链接：https://seeksoul.online/t_static/Biomamba/Biomamba.html

往期云平台使用视频教程可参考：[单细胞云平台教程全收录](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_69f8cb7b2da&enterid=1713928791&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1#wechat_redirect>)

体验反馈问卷链接：https://www.wjx.cn/vm/QIX0xRI.aspx#

各位同学需要**联系您的专属在线客服，获取demo数据后，进行操作学习。**

**![图片](../../images/239ea5459d709578.webp)**

![图片](../../images/68adda3cdb14540f.webp)

**如何联系我们**

![图片](../../images/3b8e21da777157f9.webp)![图片](../../images/7a5130b05d387a24.gif) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_yunying]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/19b4ec51a30e79aa.webp)![图片](../../images/acba43cb3408c3d0.gif) 您点的每个赞和在看，我都认真当成了喜欢
