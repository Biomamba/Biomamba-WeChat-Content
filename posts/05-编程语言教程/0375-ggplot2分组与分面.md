---
title: "ggplot2分组与分面"
date: 2025-10-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531405&idx=1&sn=7fc338d49d4b740fc45c73063526d108&chksm=9b3c02ddac4b8bcb1e8a00c59fa9ae7d03c217ff5bffb9b47522373c85d1376aa47186e0499f#rd
albums: ["编程语言教程"]
---

# ggplot2分组与分面

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531405&idx=1&sn=7fc338d49d4b740fc45c73063526d108&chksm=9b3c02ddac4b8bcb1e8a00c59fa9ae7d03c217ff5bffb9b47522373c85d1376aa47186e0499f#rd
> 合集：编程语言教程

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

ggplot2分组与分面

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

在ggplot2中，分组（Grouping）和分面（Facetting）是处理多类别数据可视化的两种核心方法，用于在同一图表中展示不同组别的数据关系，帮助发现数据中的模式和差异。

1、分组（Grouping）

分组用于将数据按某个类别变量拆分，并在同一坐标系中用不同视觉属性（颜色、形状、线条类型等）区分各组，适合比较组间趋势或分布。通过 aes()映射分组变量来实现分组操作

2、分面（Facetting）

分面将数据按类别变量拆分成多个子图（小面板），每个子图对应一个组别，共享坐标轴或独立缩放，适合展示组间差异或复杂分组。主要函数为facet_wrap()、facet_grid()

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

视频教程

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

"R语言入门课"是我们认为**生信小白入门** 不得不听的一个课程，我们也为这个课程准备了许多**干货** 。R语言的精髓便是数据处理，在本节课中，我们详细介绍了向量、矩阵、数据框、数组、因子、列表的创建方法与数据访问方式，为以后的生物信息学数据处理打下牢固的基础！

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=8)

本次课程代码

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)

大家可以跟着视频练习如下代码：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
###### 4.1.3 分组与分面 ######### 分组 ####将变量值映射到颜色、形状、大小、透明度、线条样式和几何对象的其它视觉特征，#使得多组观测值在单个图形中叠加，这一过程称为分组。 library(ggplot2)library(mosaicData)head(CPS85)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  geom_smooth(method=lm,se=FALSE)#例如，我们添加sex变量，并用color，shape和linetype表示该变量。ggplot(data = CPS85,mapping = aes(x=exper,y=wage,                                  color=sex,shape=sex,linetype=sex))+  geom_point(color="blue",alpha=0.5,size=1.5)+  geom_smooth(method=lm,se=FALSE)# 1. 按性别 (sex) 分组的散点图 + 回归线ggplot(CPS85, aes(x=exper, y=wage, color=sex)) +  geom_point() +  geom_smooth(method=lm, se=FALSE)# 2. 按婚姻状况 (married) 分组的箱线图ggplot(CPS85, aes(x=married, y=wage, fill=married)) +  geom_boxplot()# 3. 按行业 (sector) 分组的点图ggplot(CPS85, aes(x=sector, y=wage, color=sector)) +  geom_point(position=position_jitter(width=0.2))# 4. 按工会成员 (union) 和性别 (sex) 双重分组ggplot(CPS85, aes(x=educ, y=wage, shape=union, color=sex)) +  geom_point()# 5. 按地区 (south) 分组并分面展示ggplot(CPS85, aes(x=age, y=wage)) +  geom_point() +  facet_wrap(~south)  # 按地区分面# 6. 按种族 (race) 分组的密度图ggplot(CPS85, aes(x=wage, fill=race)) +  geom_density(alpha=0.5)### 分面 #### 下一个问题是：对于每个职业来说，工资年薪、薪资和性别之间的关系又具体如何？# 分面可以帮我们解决这一问题# # 分面为给定的某个变量（或变量组合）的每一个水平分别绘制一张图。# # 语法：# # +----------------------------+------------------------------------------------------------+# | 语法                       | 结果                                                       |# +============================+============================================================+# | facet_wrap(~var,ncol=n)   | 将每个var水平排列为n列的独立图                             |# +----------------------------+------------------------------------------------------------+# | facet_wrap(~var,nrow=n)   | 将每个var水平排列为n行的独立图                             |# +----------------------------+------------------------------------------------------------+# | facet_grid(rowvar~colvar) | rowvar和colvar组合的独立图，其中rowvar表示行，colvar表示列 |# +----------------------------+------------------------------------------------------------+# | facet_grid(rowvar~.)      | 每个rowvar水平的独立图，配置成一个单列                     |# +----------------------------+------------------------------------------------------------+# | facet_grid(.~colvar)      | 每个colvar水平的独立图，配置成一个单行                     |# +----------------------------+------------------------------------------------------------+# # var,colvar,rowvar表示因子。# # 例如，在本数据框中，研究不同职业的工资年薪、薪资和性别三者之间的关系：ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)# 当然你也可以按照多个分类变量去拆分数据，例如我们这里按照married与sector进行分面ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)+  facet_wrap(married~sector)ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)+  facet_wrap(~sector,ncol = 4)ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)+  facet_wrap(~sector,ncol = 2)# 结果显示了每种职业的工资年薪、薪资和性别三者之间的关系# 试试其他的写法与输出的格式-# facet_wrap(~var,ncol=n):每行的列数ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)+  facet_wrap(~sector,ncol = 1)#facet_grid(.~colvar):输出单行ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)+  facet_grid(.~sector)#facet_grid(rowvar~.)：输出单列ggplot(data = CPS85,mapping = aes(x=exper,y=wage,color=sex,shape=sex,linetype=sex))+  geom_point(alpha=0.5)+  geom_smooth(method="lm",se=FALSE)+  facet_grid(sector~.)
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

R语言入门课

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=13)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=14)

1、课程简介

[生信基地](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522649&idx=1&sn=a3a3df860fd162691403281356dcbf1d&chksm=9b3ce009ac4b691fc8679c43988a0a36e176760d3e21b2489b43184f0248b6409cbe8dcbb96a&scene=21#wechat_redirect>)希望能够给大家提供**系统性** 、**形成性** 、**规范性** 的生信教学。前面几次活动中同学们表示希望能够有线下集中学习以及**针对性的指导、答疑** 。所以，此次我们已推出"生信**R语言入门课** "，分为"R介绍"、"R语言数据对象"、"基本数据管理"、"图形初级(ggplot2)"四个模块共12节课。当然，我们也**不做生信快餐** ，本次活动回放已剪辑完毕，方便错过活动的小伙伴加入。后续我们会**持续拉群** 在群里进行**课程内容** 的答疑。

2、R语言介绍R语言是一种专门为统计分析、数据可视化和计算而设计的编程语言，广泛应用于各个领域。R语言支持各种统计分析方法，如线性回归、方差分析、聚类分析等，同时也能够进行复杂的图形和数据可视化。R语言凭借其开源、免费、工具包丰富、数据处理能力强、可视化丰富的特性在**生物信息学中被广泛应用** 。例如RNA-Seq差异分析常用的DESeq2、edgeR的引用次数多达数万次。我们制作的[单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522475&idx=1&sn=84dd9a65348528be9aa2b8d2711d776c&scene=21#wechat_redirect>)教程几乎也全是基于R语言环境。很多同学找我们学习单细胞的时候都表示不想学习R语言，直接学习单细胞分析，[不积跬步无以至千里](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=2&sn=f77d7ad73e7cb9c76ea2fb7fbf7a5cd1&scene=21#wechat_redirect>)，这显然是不现实的，所以，欢迎大家来参加此次的课程。

**报名二维码：**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyZBGOXDqRYHpgiczxr9PX8gliblp8giaPGsr7w6IeoU6lExTAeEjx48Ke4LEJQfbdiarzXwUGvoRFvyA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=15)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=16)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=17)

资料&课表

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=18)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=19)本次课程的学习资料可以联系文末客服微信领取:
![图片](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpxtWyh2oFbkW2gT4k8lvFeXnI6JzN8xM8RWSXTJPtry2H5QSUWJibTYSfMGpAso9qicgN8M7rAI617g/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

目前12节总计5.5h的视频课程回放已剪辑完毕，方便错过直播的同学随时加入学习：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxPGbgxeKtcc5DibsheFewicmia5jPx1Jic18ZUJqYpNs4cvxLhCgricA2YjPPjbqo5SpE6MEibz9OgSAEw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)

除了学习视频外，还给大家准备了学习资料，包括学习手册、课后习题。大家人手一份资料可以跟着视频联系：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxPGbgxeKtcc5DibsheFewicmicfPruB2l20gdfdRoAM8Aj1ULhAhgM1ZQibjBMq2UkO7ugkiagmxL5TLg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

课程目录：

**1 、R介绍**

1.1 R 下载与安装

1.1.1 RStudio1.1.2 R的帮助函数1.1.3 用于管理R工作区的函数

1.2 包（Packages)

1.2.1 包的基本函数1.2.2 包处理大型数据集的示例展示

**2、 R语言数据对象**

2.1 理解数据集

2.2 数据结构

2.2.1 向量(vector)2.2.2 矩阵(matrix)2.2.3 数组(array)2.2.4 数据框(data)2.2.5 因子(factor)2.2.6 列表(list)

2.3 数据输入

2.3.1 从带分隔符的文本文件导入数据2.3.2 导入Excel数据

**3、基本数据管理**

3.1 创建新变量

3.2 变量的重编码(recoding)

3.3 变量的重命名

3.4.缺失值（NA）

3.5 类型判断和转换

3.6 数据排序

3.7 数据集的合并

3.8 选取变量

3.9 选取观测值

3.10 subset()函数选择观测值或变量

3.11 剔除变量

3.12 dplyr包

3.13 使用管道操作符对语句进行串接

**4、图形初级(ggplot2)**

4.1 使用ggplot2包创建图形

4.1.1 函数ggplot2()4.1.2 geom()函数4.1.3 分组4.1.4 标尺4.1.5 刻面4.1.6 标签4.1.7主题

4.2 ggplot2包的详细信息

4.2.1 放置数据和映射选项4.2.2 将图形作为对象使用4.2.3 保存图形![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=23)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=24)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=25)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=26) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_yunying]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyZBGOXDqRYHpgiczxr9PX8gliblp8giaPGsr7w6IeoU6lExTAeEjx48Ke4LEJQfbdiarzXwUGvoRFvyA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=jttzxlfu&tp=webp#imgIndex=27)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=28) 您点的每个赞和在看，我都认真当成了喜欢
