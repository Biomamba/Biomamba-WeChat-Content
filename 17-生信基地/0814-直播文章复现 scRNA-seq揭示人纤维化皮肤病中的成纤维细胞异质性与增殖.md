---
title: "直播文章复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖"
date: 2025-08-27
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530696&idx=1&sn=c90298fbe01b150ad7779f77294c6a25&chksm=9b3c0198ac4b888e6a2dd5797a000ce744c5f66049227a4995fb5130c2606fecd1ba18cb9394#rd
albums: ["生信基地"]
---

# 直播文章复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530696&idx=1&sn=c90298fbe01b150ad7779f77294c6a25&chksm=9b3c0198ac4b888e6a2dd5797a000ce744c5f66049227a4995fb5130c2606fecd1ba18cb9394#rd
> 合集：生信基地

![](../../images/399758fa7d6941c2.png)

学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)**纤维化是一种以成纤维细胞增殖和细胞外基质（ECM）过度积累为特征的病理过程，它可影响任何器官，导致组织瘢痕形成和器官功能障碍。新的证据表明成纤维细胞实际上是形态和功能异质的细胞群体。 这篇文章中，作者通过使用[ scRNA-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529961&idx=1&sn=b9f65c76a8776caada786c6d57ace15e&scene=21#wechat_redirect>)探索了皮肤瘢痕中的成纤维细胞异质性，发现瘢痕中成纤维细胞可以被分为4个亚群, 分泌状、分泌网状、间充质和促炎性。这些发现有助于我们更深入地理解纤维化皮肤疾病的病理，并为纤维化治疗提供潜在的靶点。本教程配合[scRNA-seq小学期](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)课程进行了全新修订，用于我们最后的手把手实战教程。本周六、日09:00-17:00进行复现直播，主要内容包括：数据[整合去批次](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&scene=21#wechat_redirect>)、细胞周期计算、[细胞比例可视化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&scene=21#wechat_redirect>)、[细胞降维](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2820794880947159043&from_itemidx=2&from_msgid=2247498080&#wechat_redirect>)、[基因表达小提琴](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=1&sn=b795a3e36ae092d8f87abb5a87187828&scene=21#wechat_redirect>)、[FeaturePlot](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504616&idx=1&sn=f7b4a0e6b25d224380cd803e3463a3e4&scene=21#wechat_redirect>)、[热图可视化](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527762&idx=1&sn=ba7c8a4cb704e71fa86ebfe1f19bffea&scene=21#wechat_redirect>)、[亚群分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&scene=21#wechat_redirect>)、[细胞通讯](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)、[拟时序分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)、[差异计算与富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&scene=21#wechat_redirect>)等。可以说是把**[scRNA-seq小学期](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)** 课程学习的技能融会贯通到实战，完整课表见：**![](../../images/b3a5529a86ba7c71.webp)**
**自学有困难的同学不妨看看：[ scRNA-seq，从小白到文献复现大神！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529435&idx=1&sn=cc7e9ff271f0ce0157008532ef4829c3&scene=21#wechat_redirect>)**优惠 订阅资料或参与课程请联系客服微信[Biomamba_zhushou]****
**复现 集锦，本周咱就画这一模一样的图~![](../../images/65ed6e120f98d610.webp)![](../../images/72c51891a4875189.webp) **-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：

![](../../images/72dc5b2b4d98badc.gif)

‍

**教程目录** ：

**一、文献解读**

**1.0 复现集锦**

**（1）原文集锦**

**（2）代码复现集锦**

**1.1 背景介绍**

**1.2 主要内容**

**（1）scRNA-seq揭示正常瘢痕和纤维性皮肤病真皮组织的细胞异质**

（2）瘢痕疙瘩和正常瘢痕中成纤维细胞形成不同的细胞亚群

**（3）纤维化皮肤病中间充质成纤维细胞特征的鉴定**

**（4）成纤维细胞亚群中的配体-受体相互作用分析**

**（5）间充质成纤维细胞通过POSTN促进瘢痕中胶原蛋白表达**

**（6）sC4 成纤维细胞比 sC1 成纤维细胞更像间充质细胞**

**（7）间充质成纤维细胞在硬皮病中增加**

**1.3 总结讨论**

**二、准备工作**

**2.1 硬件准备**

**2.2 单细胞基础**

**三、数据下载、处理和可视化**

**3.0 数据下载**

**3.1 读取数据（10X标准数据）（barcodes、features、matrix）**

**3.2 数据整合**

3.3 Seurat标准流程（harmony去批次）

**3.4 细胞注释**

**3.5 细胞周期计算**

**3.6 数据可视化**

**（1）分样本细胞比例柱形图**

**（2）分样本细胞比例桑基图**

**（3）UMAP降维图**

**（4）Marker小提琴图**

**（5）Marker FeaturePlot**

**（6）Marker DotPlot**

**（7）Marker热图**

**3.7 成纤维细胞亚群**

**（1）亚群细分**

**（2）分样本细胞比例柱形图**

**（3）亚群分样本降维图**

**（4）基因差异表达提琴图**

**（5）细分注释**

**（6）注释后Marker展示**

**（7）Mesenchymal_Fib组间差异分析**

**（8）Mesenchymal_Fib差异基因富集分析**

**3.8 间充质成纤维细胞在纤维化皮肤疾病中的特性**

**（1）分样本基因表达FeaturePlot**

**（2）分组基因表达箱线图**

**（3）亚群间差异基因热图**

**（4）Mesenchymal_Fib相对其他FIB亚群上调差异基因富集**

**（5）marker基因堆叠小提琴图**

3.9 细胞通讯分析

（1）亚群标签映射回细胞大类

（2）Normal组细胞通讯

（3）Keloid组细胞通讯

（4）细胞通讯热图

3.10 拟时序分析

3.11 Mesenchymal_Fib两个亚群间差异和富集

****四、参考********单细胞教程全收录********欢迎致谢****

文末下载链接中包含以下内容：

![](../../images/7e835104fe823814.webp)

测试文件约**12.17GB** ，大家注意按需下载！

![](../../images/7d247e6c6ef19f87.png)
![图片](../../images/eab31beb8c0e41d2.png)

往期订阅

![图片](../../images/8b04fd62fd8f3d51.png)![图片](../../images/4064a50c19e8ad22.png)

生信基地现已开放终身订阅，现已包含几十篇订阅资料，未来37年持续更新：[那就开放一个终身订阅吧~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)

**2025订阅合辑：**

[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)[《Cell》复现|中性粒细胞scRNA-seq图谱阐明抗肿瘤抗原呈递效力](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526776&idx=1&sn=99eb6a16c7bf345445b6ff4b61110138&scene=21#wechat_redirect>)

[代码复现|scRNA-seq绘制透明细胞肾癌的免疫微环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527498&idx=1&sn=c8282e9d4175bfb2e572278312073d81&scene=21#wechat_redirect>)

[改造单细胞DoHeatmap](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527762&idx=1&sn=ba7c8a4cb704e71fa86ebfe1f19bffea&scene=21#wechat_redirect>)

[Slingshot拟时序分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527850&idx=1&sn=f4e2ca5e2e5e71eeaf132375bb8270eb&scene=21#wechat_redirect>)

[《Cancer Cell》|时空单细胞揭示CRC的PD-1治疗免疫细胞动态](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528056&idx=1&sn=73c0da3ff7ff50bafbb9315fd5b60f15&scene=21#wechat_redirect>)

[scRNA-seq数据基础分析手册(2025最新修订)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)

[代码复现|吞噬作用增强肿瘤中巨噬细胞的氧化代谢和免疫抑制特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528289&idx=1&sn=b56f00f3d8a4b152e54f3acd40aef21d&scene=21#wechat_redirect>)[一文学会scRNA Velocity剪切速率分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528458&idx=1&sn=900357283922571c6294435be409a2f3&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&scene=21#wechat_redirect>)

# [一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&scene=21#wechat_redirect>)

# [一文学会四种scRNA-seq拷贝数变异分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529921&idx=1&sn=93f8ad6655ee6d2b036cd557a6a74be6&scene=21#wechat_redirect>)

# [分子批量对接与亲和力热图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=1&sn=90de71a3b453e635920d309faedb36c7&scene=21#wechat_redirect>)

# [代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&scene=21#wechat_redirect>)

持续更新中~

![图片](../../images/697dd2eb5e60e8d8.png)解锁前需阅读：**[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)**![](../../images/399758fa7d6941c2.png)

订阅后解锁下方学习手册链接：

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

请联系[Biomamba_zhushou]获取文件提取码

链接:

https://pan.baidu.com/s/1h4hHWV4FF7BBkzZthDU9KA

整个订阅合集的百度云下载地址可见:

https://pan.baidu.com/s/1yXzQi0zBqh4ZLR6Hznckiw?

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)
![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
