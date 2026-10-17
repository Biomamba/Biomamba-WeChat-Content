---
title: "零代码复现《Genome Medicine》|scRNA-seq解析CXCL16/CXCR6驱动驻留T细胞促进突触消除"
date: 2025-04-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528493&idx=1&sn=d7e31fc84bef96bbad9e9fde06e55726&chksm=9b3c097dac4b806bce7b76a87c03c966b167acaec87729f64dbc5703fb4ff8a9a5360dcb131b#rd
albums: ["单细胞教程全收录", "单细胞云平台", "粉丝来稿"]
---

# 零代码复现《Genome Medicine》|scRNA-seq解析CXCL16/CXCR6驱动驻留T细胞促进突触消除

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528493&idx=1&sn=d7e31fc84bef96bbad9e9fde06e55726&chksm=9b3c097dac4b806bce7b76a87c03c966b167acaec87729f64dbc5703fb4ff8a9a5360dcb131b#rd
> 合集：单细胞教程全收录 / 单细胞云平台 / 粉丝来稿

**写在前面**

当今基因测序数据量在爆炸性增加，生信分析面临着**算力要求高** 、**代码** 软件**繁多** 、科研人员**协作分析困难** 等一系列痛点。为解决这些问题，各种生信云平台应运而生，它提供了一系列生物信息学工具和资源，用于支持科研人员在生物学数据的分析、可视化和解释方面的需求。SeekSoul Online便是其中一个，相信对于想要快速上手单细胞数据分析的你来说会是个惊喜：

云平台地址：

https://seeksoul.online/t_static/Biomamba/Biomamba.html

使用教程可见：

[一文学会零代码单细胞分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511007&idx=1&sn=e7be3d9775890e5717889714629cfaf5&chksm=9b3cd28fac4b5b9936428d5f74d8b581b5cddc18d0fc42e2a5d75604cce080588d50f1304a17&scene=21#wechat_redirect>)

[零代码单细胞视频教程](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=3403706694394970115&scene=173&subscene=&sessionid=svr_2095d655e3b&enterid=1715838775&from_msgid=2247510401&from_itemidx=1&count=3&nolastread=1#wechat_redirect>)

活动可见：

![](../../images/71a3919441ae550e.webp)

**文章介绍**

复现文章标题：

《Single-cell RNA transcriptome analysis of CNS immune cells reveals CXCL16/CXCR6 as maintenance factors for tissue-resident T cells that drive synapse elimination》

**发表日期和杂志：** 2022年发表在Genome Medicine上

复现集锦：

![](../../images/9841ab7f55b8faae.webp)

**在线阅读链接：** https://doi.org/10.1186%2Fs13073-022-01111-0

#### 研究背景

针对中枢神经系统(CNS)的新兴RNA病毒会导致幸存者的认知后遗症。西尼罗河病毒(WNV)是一种与学习和记忆障碍有关的重新出现的RNA病毒。

对感染西尼罗河病毒的人类和小鼠的研究显示，小胶质细胞介导的突触消除在海马体内。此外，中枢神经系统驻留记忆T(TRM)细胞激活小胶质细胞，限制突触恢复，并导致WNV恢复小鼠的空间学习障碍。

**单细胞实验设计**

使用单细胞RNA测序检测了西尼罗河病毒恢复的小鼠前脑内的免疫细胞，以确定参与T细胞和小胶质细胞之间细胞间通讯的可能的配体-受体对。对感染后25天(DPI)的C57BL/6模拟和WNV感染的小鼠的前脑组织(皮质和海马区)进行了scRNA-seq分析

![图片](../../images/fd6d6824ce291806.webp)

**WNV感染后中枢神经系统细胞聚集的scRNA-seq分析**

![图片](../../images/ce1955b0ede0d217.webp)

  * b. 在模拟和西尼罗河病毒感染的动物中分析的所有免疫细胞的tSNE图，显示9个簇，用密度簇标记，并在括号中用细胞类型身份和细胞数量注释。
  * c. 模拟感染小鼠（左图）和西尼罗河病毒感染小鼠（右图）中分析的所有细胞的tSNE图，按治疗组分开，以密度聚类着色。
  * d. 基因表达热图，表示用于每个集群细胞鉴定的前三个已知基因的表达水平。
  * e. 免疫细胞Cxcr6 mRNA（左图）和Cxcl16 mRNA（右图）的tSNE图。
  * f. 小提琴图显示在0-5簇中含有Cxcr6 mRNA（左图）或Cxcl16 mRNA（右图）的免疫细胞。

**seeksoul云平台分析复现**

学完了1.5d的课程([1.5天，学会单细胞分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247523411&idx=2&sn=142574b00dd351fae0b76831cd2d2f19&scene=21#wechat_redirect>))后，这位同学已经可以输出以下内容啦，其实很多复现的内容相差无几，甚至图片要比原文更加美观~

具体分析方法可参考[一文学会零代码单细胞分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511007&idx=1&sn=e7be3d9775890e5717889714629cfaf5&scene=21#wechat_redirect>)推文，或者根据对应的视频讲解学习![图片](../../images/91ebb5794654cdae.webp)

### 1.数据上传及分析

可以选择上传**标准分析的结果数据** ——但是需要**注意上传的是seurat V4版本得到的降维聚类的rds文件，且要包含UMAP和TSNE的降维结果**

![图片](../../images/789323b43dabe75a.webp)

也可以选择上传**单样品数据** ——这时候就可以**上传matrix、h5或者h5ad格式的文件**

![图片](../../images/9394859fb14d0e30.webp)

这里复现的文章提供的数据集是**GSE212199** ，提供的是10X标准matrix格式的三文件，下载需要的数据整理好之后按照对应的样品上传即可。

![图片](../../images/0d38ef90c983cdfc.webp)

然后可以在**资源总览的我的数据中找到需要的数据** ，选择需要的数据集之后选择快速创建流程

![图片](../../images/dee79297ef2cf1d3.webp)

**填写好需要的信息，然后即可创建需要的项目**

![图片](../../images/6eefd08e50982368.png)

**可以在创建好项目之后，对数据进行分组，在已选数据旁边添加分组信息即可**

![图片](../../images/8a0e32da2e8f7cc0.webp)

**准备就绪之后，就可以提交进行分析，点击` 开始分析`即可**

### 2\. 基础分析流程

**首先会基于统计好的结果进行质控过滤，主要是nfeature、ncounts以及mito线粒体基因的占比**

![图片](../../images/79b0737040d07248.webp)

**可以在过滤中选择调整过滤参数，或者使用默认的参数设置进行过滤即可**

![图片](../../images/3476bf4e4ac08411.webp)![图片](../../images/59b7da252d9031a0.webp)

**如果不需要调整过滤参数，检查一下质控结果之后，就可以对多样品的数据进行整合**

![图片](../../images/94985631a23683d8.png)

**高变基因选择的是前两千个高变基因，然后整合方法用的harmony**

![图片](../../images/03746bdc42a11f83.png)

**整合结果**

![图片](../../images/f9972ae9cd5d337c.webp)

**对细胞进行聚类分群时候，可以选择不同分辨率进行可视化**

![图片](../../images/b5e9c6aec3d25174.webp)

**这里选择0.1分辨率用于后续的亚群注释**

![0.1分辨率](../../images/e6b90d62cd47fd9f.webp) 0.1分辨率

**确定好之后，即可选择完成分析，跳转到注释及高级分析页面**![图片](../../images/137a29e14769ba87.webp)

###  3\. 细胞亚群注释及可视化

**细胞亚群注释一直是较为复杂的部分，seeksoul平台提供了多种注释方式——singleR自动注释以及singleR+AI注释**

![图片](../../images/62e600cc919da235.png)

**如果觉得自动注释的结果不符合预期，也可以基于每个亚群的top基因，进行手动注释，然后修改注释结果即可**

![图片](../../images/dda0525e98d01a62.webp)

**选择` 修改注释`，找到需要修改的内容，选择编辑，然后将手动注释的结果，修改到对应的位置即可**

![图片](../../images/9d419844e3156ef1.webp)

**最终注释结果，自动选择配色就看起来很高级！**

![图片](../../images/dae5ad134ca43beb.webp)

###  4\. 关键基因展示

**提供了气泡图、小提琴图和热图展示top基因**

![图片](../../images/95aa3753233f6166.webp)![图片](../../images/901dc4debb7f31f0.webp)

**并且可以直接可视化细胞亚群比例的柱状图**

![图片](../../images/08c19f6b1499b1c8.webp)

也可以选择展示关注的基因，比如文献中的`Cxcr6和Cxcl16`

![图片](../../images/d453e555be621f7b.webp)

Seeksoul 单细胞平台使用感受

  1. 整体而言分析较为简便快捷，上传好数据之后，创建好对应的分析项目，然后进行分析即可
  2. 上传的数据有格式要求，暂时不支持文本格式比如txt或者csv.gz格式的压缩文件上传，以及不支持V5版seurat得到的结果数据
  3. 除了基础的降维聚类分群注释分析功能外，还有很多高级分析，可以再后续使用看看

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

**![图片](../../images/24794c2caf22d5d9.webp)**

![](../../images/cc4e5397f7d7fd7c.webp)![图片](../../images/519a89eaf5a008c9.png)

**如何联系我们**

![图片](../../images/74dcf0f66a3cbe22.png)![图片](../../images/8b292dc18fbad271.gif) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/fe8ecb8594a1f419.webp)![图片](../../images/265f0c51518f165d.gif) 您点的每个赞和在看，我都认真当成了喜欢
