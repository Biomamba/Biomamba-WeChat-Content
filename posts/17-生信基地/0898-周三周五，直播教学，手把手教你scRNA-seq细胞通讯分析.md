---
title: "周三周五，直播教学，手把手教你scRNA-seq细胞通讯分析"
date: 2026-05-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537798&idx=2&sn=48981453ec35e01d6f1af4fd1ed5ada6&chksm=9b3c2dd6ac4ba4c055cedf28333448addc3cf152a4a783d731841eb21148b12b0771cf469e6a#rd
albums: ["生信基地"]
---

# 周三周五，直播教学，手把手教你scRNA-seq细胞通讯分析

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537798&idx=2&sn=48981453ec35e01d6f1af4fd1ed5ada6&chksm=9b3c2dd6ac4ba4c055cedf28333448addc3cf152a4a783d731841eb21148b12b0771cf469e6a#rd
> 合集：生信基地

这周三、周五09:00进行[R语言scRNA-seq细胞通讯分析专题](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535877&idx=4&sn=847ec896b51c5c1571e31a54f198ebc2&scene=21#wechat_redirect>)教学，详细介绍与课程大纲可见：[视频介绍，学单细胞你应该按照这个节奏](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536612&idx=1&sn=19032a541a2b5a9f07d64981cc22069f&scene=21#wechat_redirect>)，还没有报名的同学，可联系客服微信[Biomamba_zhushou]报名参加课程哦~![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)课程直播链接：https://meeting.tencent.com/dm/PuxBsb3i3vyd![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

单细胞细胞通讯分析教学内容

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=23)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：

# ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzcvib4lWCZoOrFXfrQ3ssc2mhibicDFV8liciayrEdP3sXpUibyvicibw2wvL1zn9fhiaCSFiaqZznVPDguTfg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1)

# **
**

# ****细胞通讯分析学习手册****

# ****![](https://mmbiz.qpic.cn/sz_mmbiz_gif/buxFNhaTGwnBxXia62yVHz4UQmDYgZtghhia6GaulXVfyaFbB585K9NlVT2kb6QY6mrO3icckIfoxTDoYTosqRyvZ2WcgxhHeyrtiaha3CPpcog/640?wx_fmt=gif&from=appmsg)****

细胞通讯分析教程目录：

一、写在前面

二、可视化集锦

三、绪论

3.1 定义

3.2 不同细胞通讯软件的比较

（1）互作预测过程

（2）主要研究成果

3.3 实验追踪细胞间相互作用

3.4 总结

四、cellchat

4.1 简介

4.2 安装并加载R包

4.3 下载、读取、创建cellchat对象

4.4 载入数据库并开始计算

4.5 可视化

4.6 进阶可视化

4.7 配受体展示

4.8 通路展示

4.9 多个细胞通讯通路气泡图可视化

4.10 多组别细胞通讯

（1）准备工作

（2）可视化

五、nichenetr

5.1 准备工作

（1）安装并加载R包

（2）表达矩阵获取

（3）下载先验模型

5.2 细胞通讯分析

（1）定义sender与receiver

（2）定义一组感兴趣的基因集

（3）获取配受体基因表达矩阵

（4）配体活性分析

（5）推断受体以及配体潜在调控靶基因与配体的调控活性

（6）sender中配体的组间差异log fold change值

（7）可视化拼盘

5.3 差异细胞通讯分析

（1）准备工作

（2）定义niches

（3）计算niches的差异基因

（4）定义感兴趣的基因组

（5）计算配体活性并推断配受体对

（6）计算配体、受体、target的表达量

（7）通过受体表达量评估配受体对互作强度

（8）计算配受体对权重

（9）差异可视化

六、cellcall

6.1 软件安装和加载

6.2 数据准备

6.3 创建cellchat对象

6.4 推断细胞-细胞通讯得分

6.5 通路活动分析

6.6 可视化

（1）圈图

（2）热图

（3）桑葚图

（4）TF富集分析图

（5）山脊图

6.7 结果保存

七、icellnet

7.1 软件安装和加载

7.2 数据准备

7.3 数据预处理

7.4 在感兴趣的集群上应用icellnet管道

7.5 计算细胞通讯分数

7.6 结果可视化

（1）热图

（2）柱形图

7.7 在TME内识别ccRCC2特定的通信信道

（1）计算

ccRCC2的特定相互作用

（2）可视化

7.8 结果保持

八、环境版本信息

九、参考

十、单细胞教程全收录

十一、欢迎致谢

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwneiaN6M1eicaPtwtZZKbktCb5yEia7KEd4LRdl5K6Hicd7t4Z7bS0mwiaTALsqczMSpWDWk31wiaxqwx6sC28k4NwdQ9Op1HU6G3FiaA/640?wx_fmt=png&from=appmsg)**

测试文件，总大小 6.05GB

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=27)还想要了解更多单细胞/空转课程：[共计251小时视频教程，保姆级单细胞&空转教学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536399&idx=2&sn=6c73155a0393ed9c246fee69cb06341f&scene=21#wechat_redirect>)，都欢迎找我们聊聊~
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532717&idx=2&sn=eb98e578098b9f432ea6ecbdc3c0d74b&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
