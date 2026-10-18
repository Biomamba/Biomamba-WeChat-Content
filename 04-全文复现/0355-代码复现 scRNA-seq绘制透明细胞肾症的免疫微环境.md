---
title: "代码复现| scRNA-seq绘制透明细胞肾症的免疫微环境"
date: 2025-11-03
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531979&idx=2&sn=4f4b960916888e05dd191fdc4ee1c2a8&chksm=9b3c049bac4b8d8d1e3a82f73a0182c8d900a93518dd4c45b1c9b0233fec39231a9607f3d8e6#rd
albums: ["全文复现"]
---

# 代码复现| scRNA-seq绘制透明细胞肾症的免疫微环境

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531979&idx=2&sn=4f4b960916888e05dd191fdc4ee1c2a8&chksm=9b3c049bac4b8d8d1e3a82f73a0182c8d900a93518dd4c45b1c9b0233fec39231a9607f3d8e6#rd
> 合集：全文复现

****

![](../../images/399758fa7d6941c2.png)

学习手册

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png) 本次教程中，我们复写了题为"Mapping the immune environment in clear cell renal carcinoma by single-cell genomics"的文章(doi: 10.1038/s42003-020-01625-6)。本文表征了Clear cell renal cell carcinoma（ccRCC）的肿瘤免疫微环境，作者对3例ccRCC配对患者的肿瘤和血液组织进行scRNA-seq测序和TCR测序，绘制了CD45+淋巴细胞和髓系细胞图谱。另外还纳入了来自另外四个个体的11,367个来自正常肾脏和外周血的免疫细胞，以促进ccRCC特异性差异的识别和评估。主要发现包括：(1)与正常肾组织相比，肿瘤浸润的免疫细胞中的CD8+T细胞和巨噬细胞总体增加(2)证明了肿瘤浸润性CD8+T细胞的不同细胞转录状态(3)确定了MKI67+增殖亚群是ccRCC进展的潜在罪魁祸首
自学有困难的同学不妨看看：[这可能是全网最全的scRNA-seq分析教程！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)本教程基于Linux环境演示，计算资源不足的同学可参考：
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21#wechat_redirect>)
[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)访问链接：https://biomamba.xiyoucloud.net/欢迎联系客服微信[Biomamba_zhushou]获取帮助
如果你对下面的教程比较迷茫，那么你可以先行学习编程教程：[十小时学会Linux](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&chksm=9b3cae21ac4b2737f5923b246470d699474c041bb78de50d2b71b99d537f9f44ca2938002cda&scene=21#wechat_redirect>)
[生信Linux及服务器使用技巧](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2980604042328702978#wechat_redirect>)[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本教程**复现集锦** ：

![](../../images/f0d1d2164525c819.webp) **-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)

学习手册以html文件格式提供，可在浏览器中打开并翻阅学习

![](../../images/8b13baa618838ad5.gif)

**教程目录** ：

**一、准备工作**

1.1 硬件准备
1.2 单细胞基础

**二、文献解读**

2.1 摘要2.2 主要内容2.3 总结讨论

**三、文章复现**

3.1 复现集锦3.2 数据下载3.3 ccRCC中免疫细胞的单细胞图谱3.4 外周血和肿瘤中CD8+T和CD4+T克隆型比较3.5 ccRCC中CD8+T细胞存在不同亚群转录连续体3.6 ccRCC中CD4+T细胞亚群特征识别3.7 ccRCC中巨噬细胞分化差异

**四、****环境版本信息**

**五、参考**

文末下载链接中包含的内容：

![](../../images/b2facf5d76d85915.webp)

测试文件约**5.39GB** ，大家注意按需下载！

![](../../images/7d247e6c6ef19f87.png)
解锁前需阅读：[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)
![](../../images/f08cdfe212eb6283.png)

文末还可解锁以下内容

![](../../images/2cc9da4d1e6321da.png)![](../../images/556752da2b520ff6.png)

2025订阅合集持续更新中，联系客服微信[**Biomamba_zhushou**]可以219￥获取全部资料(包括今年后面更新的内容)。当然，付费不是目的，以下资料都可以通过**转发领取**(更推荐这种方式)。

[2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21#wechat_redirect>)目前我们还[开放终身订阅~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526967&idx=1&sn=3e4e9acabd6061d7e3dab8cd52924bcc&scene=21#wechat_redirect>)![](../../images/3536da08710707f3.png)

手册下载链接：

![](../../images/fbfc4b8be383f432.png)![](../../images/556752da2b520ff6.png)

学习手册与测试文件链接:

https://pan.baidu.com/s/1dccgha7TuW2LebQqpY7mwQ?pwd

提取码可联系客服微信[Biomamba_zhushou]领取

**-Biomamba**

![](../../images/3536da08710707f3.png)![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528482&idx=1&sn=7cc0715eace4f592a62bdaf157b25c01&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

**![图片](../../images/eff615a0a49ee4ca.webp)**

![图片](../../images/acba43cb3408c3d0.gif)您点的每个赞和在看，我都认真当成了喜欢
