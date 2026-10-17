---
title: "单细胞Figure1的常见图表(Python版)"
date: 2026-05-25
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538071&idx=3&sn=84d7c416ddc32bfd3d1fc740ea0aba9a&chksm=9b3c2cc7ac4ba5d17e438ec0a708f54560138dfe0ba2c39462cd87c3cff57222eb5acd354aa3#rd
albums: ["单细胞教程全收录"]
---

# 单细胞Figure1的常见图表(Python版)

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538071&idx=3&sn=84d7c416ddc32bfd3d1fc740ea0aba9a&chksm=9b3c2cc7ac4ba5d17e438ec0a708f54560138dfe0ba2c39462cd87c3cff57222eb5acd354aa3#rd
> 合集：单细胞教程全收录

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

写在前面

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)《Single-cell RNA-seq reveals fibroblast heterogeneity and increased mesenchymal fibroblasts in human fibrotic skin diseases》一文中，作者通过使用[scRNA-seq](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)探索了皮肤瘢痕中的成纤维[细胞异质性](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530696&idx=1&sn=c90298fbe01b150ad7779f77294c6a25&scene=21#wechat_redirect>)，之前我们也推出过完整的原文复现:[代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&scene=21#wechat_redirect>)。此前我们也制作了一版基于**[R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533722&idx=2&sn=4730e67f215e607e7b6354cbd803b290&scene=21#wechat_redirect>)** 的[单细胞常见Figure 1 视频教程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522008&idx=1&sn=f8c89bf880b66ecc2c5253f31e25b215&scene=21#wechat_redirect>)。这里我们给大家提供基于[Python](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&scene=21#wechat_redirect>)中的[scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&scene=21#wechat_redirect>)的单细胞常见Figure 1教程，大家可以根据自己的常用编程语言，自由选择顺手的教程。**
**自学有困难的同学不妨看看：[ 82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)、[100个小时沉浸式学会scRNA-seq数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531092&idx=1&sn=9968319b84186bb9b717b7b409132d8b&scene=21#wechat_redirect>)优惠订阅资料或参与课程请联系客服微信[Biomamba_zhushou]**更多生信教程可见：[ 为什么我们敢开放终身订阅](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)**
本教程基于Linux中的jupyter环境演示，计算资源不足的同学可参考：[足够支持你完成硕博生涯的共享服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=2&sn=4708fac31ac8f4e347847e4b7f2a4fed&scene=21#wechat_redirect>)[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21&token=1904068475&lang=zh_CN&poc_token=HE0kOWmjseRZXooE5W9Cc2bMHz7i_DtlgPhdLwYn#wechat_redirect>)[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21&token=1904068475&lang=zh_CN&poc_token=HPAkOWmjbC2GPkTlGLA-Kxz5CJDZYGwg5-cRPFt5#wechat_redirect>)访问链接：https://biomamba.xiyoucloud.net/
本教程复现集锦![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyN00o5T0LevX01eJ1e05knoI9pd40h3m3RBDVh7lkkdYDmRAOCH00fSk2hPbkUarU04C0X4xnBEQ/640?wx_fmt=jpeg) **-Biomamba**
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

所见即所得

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

学习手册以html文件格式提供，可在浏览器中打开并翻阅学习：‍

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK31PqRgJstE7r3gyCQxibqckLYvbBdBCBQjufVSjumNqqd3LznzyiatibVw/640?wx_fmt=gif&from=appmsg)

**
**

**教程目录** ：

**一、文献解读**

**1.1背景介绍**

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

**2.1 数据下载**

**2.2 数据读入**

**三、数据处理和可视化**

**3.1 数据质控及可视化**

**3.2 细胞分群**

**3.3 细胞类型注释**

**3.4 降维图**

**3.5 小提琴图**

**3.6 基因表达在降维图展示**

**3.7 细胞比例展示**

**3.8 差异基因相关**

**3.8.1 差异基因计算**

**3.8.2 差异基因点图**

**3.8.3 差异基因热图**

**3.8.4 差异基因热图优化**

**3.9 火山图**

**3.10 差异基因富集分析**

3.11 每个亚群组间差异基因柱形图

3.12 拼图

3.12.1 第一层

3.12.2 完整fig1

3.12.3 小结

****四、软件版本********单细胞教程全收录********欢迎致谢****

文末下载链接中包含以下内容：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3zoSNo67sxlkWQGC1TXTUuE9qZYaBmr7xiaSOBdY4EnR1ncvmc1DGNqw/640?wx_fmt=png&from=appmsg)

测试文件约**15.12GB** ，大家注意按需下载！

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
解锁前需阅读：**[2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)**![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

提取码联系客服领取：

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

本推送教程、测试文件下载链接：

https://pan.baidu.com/s/17xALl_DTfJtFy8lQiqZwwg

提取码请联系客服微信获取：

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
