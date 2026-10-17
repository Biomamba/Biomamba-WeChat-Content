---
title: "R语言绘图神器| ggplot2与其基本用法介绍"
date: 2025-10-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531330&idx=1&sn=d4eef89d16e8d4ba1c18f7a66bafb7ce&chksm=9b3c0212ac4b8b04b71e1805b176393741760a07188562dc051cc8ec753e395d6f93d374a264#rd
albums: ["编程语言教程"]
---

# R语言绘图神器| ggplot2与其基本用法介绍

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531330&idx=1&sn=d4eef89d16e8d4ba1c18f7a66bafb7ce&chksm=9b3c0212ac4b8b04b71e1805b176393741760a07188562dc051cc8ec753e395d6f93d374a264#rd
> 合集：编程语言教程

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

ggplot2

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

ggplot2是R语言中的可视化神包，由Hadley Wickham开发。其本质是一套基于“图层化、模块化”的绘图语法体系。它彻底改变了传统R 绘图（如grid）的 “命令式” 逻辑，通过将数据、图形元素、美学映射拆解为独立组件，让用户能像“搭积木”一样灵活构建复杂可视化，同时保证代码的可读性和可复现性。目前，ggplot2已成为数据科学、学术研究、商业分析中最主流的绘图工具之一，尤其擅长生成发表级别的高质量图表。我们给大家演示过的[CellChat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512011&idx=1&sn=fbd41832c5995d79fead016931d3bfbd&scene=21#wechat_redirect>)、[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>)、[monocle](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&scene=21#wechat_redirect>)等包的可视化内核其实均是ggplot2。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

视频教程

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

"R语言入门课"是我们认为**生信小白入门** 不得不听的一个课程，我们也为这个课程准备了许多**干货** 。R语言的精髓便是数据处理，在本节课中，我们详细介绍了向量、矩阵、数据框、数组、因子、列表的创建方法与数据访问方式，为以后的生物信息学数据处理打下牢固的基础！

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

本次课程代码

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=5)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

大家可以跟着视频练习如下代码：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
#### 4 图形初级(ggplot2) ###### 写在前面# ggplot2 是 R 语言中一款功能强大且广受欢迎的数据可视化包，# 由 Hadley Wickham 基于 Grammar of Graphics（图形语法） 开发，# 其核心思想是将数据可视化拆解为多个独立且可组合的组件，# 让用户能灵活、高效地创建专业级图表，广泛应用于数据分析、学术研究、商业报告等场景。# 核心设计理念：图形语法# ggplot2 的精髓在于 “图形语法”，它将一张图表抽象为以下几个核心组件，用户可通过组合这些组件构建任意类型的可视化：# # 数据（Data）：可视化的基础，需传入结构化数据（如 data.frame 格式），所有图形元素都围绕数据展开。# 映射（Aesthetics, 简称 aes）：定义数据列与图形视觉属性的关联，例如将 “销售额” 映射到 y 轴、“地区” 映射到颜色（color）、“产品类别” 映射到形状（shape）等。# 几何对象（Geometric Objects, 简称 geom）：图表的核心视觉元素，决定了图表的类型，如点（geom_point，散点图）、线（geom_line，折线图）、柱状（geom_bar，柱状图）、箱线（geom_boxplot，箱线图）等。# 标度（Scales）：控制视觉属性的 “尺度”，例如调整坐标轴的范围（scale_x_continuous）、颜色的配色方案（scale_color_brewer）、图例的显示方式等，确保视觉映射的合理性和美观性。# 坐标系（Coordinate Systems）：定义图表的坐标体系，默认是笛卡尔坐标系（coord_cartesian），还支持极坐标（coord_polar，用于饼图、雷达图）、翻转坐标（coord_flip，用于横向柱状图）等。# 分面（Facets）：按数据的某个类别将图表拆分为多个子图（类似 “小 multiples”），例如按 “年份” 分面展示不同年份的地区销售额，常用函数为 facet_wrap 或 facet_grid。# 主题（Themes）：控制图表的非数据相关外观，如背景颜色、坐标轴标签字体、图例位置等，ggplot2 提供默认主题（theme_grey），也支持自定义主题（如 theme_minimal、theme_bw，或通过 theme() 函数精细调整）。#1.  本章学习使用**mosaicData**包中的**CPS85**数据框#2.  探讨ggplot2的部分用法##### 4.1 使用ggplot2包创建图形 ###### 测试数据包if(!require(mosaicData))install.packages('mosaicData')# ggplot2本体：if(!require(ggplot2))install.packages('ggplot2')?ggplot()# ggplot测试数据，长格式数据：head(CPS85)# 宽格式数据不利于ggplot输入：expr <- matrix(1:100,ncol = 10,nrow = 10)colnames(expr) <- paste('cell_',1:10)rownames(expr) <- paste('gene_',1:10)expr###### 4.1.1 函数ggplot2() #######需要2个参数#1)设置数据框，这里为data=CPS85#2)一组映射，是数据框中的变量到图形中的可视属性的映射，放置在函数aes()中，aes()函数表示美化或你能看见的东西head(CPS85)ggplot(data=CPS85,mapping = aes(x=exper,y=wage))#这里的图是空白的，是因为我们还未指定要放置什么在图上，# 仅指定来exper(工作年限)映射到x轴，wage(工资)映射到y###### 4.1.2 geom()函数 ####### (1) 函数选项# 该函数是规定在图形上放置什么样的几何对象(点、线、条、阴影区域)，常用选项为：# # +------------------+---------------+-----------------------------------------+# | 函数             | 添加的图形    | 选项                                    |# +:=================+:==============+:========================================+# | geom_bar()       | 条形图        | color,fill,alpha                        |# +------------------+---------------+-----------------------------------------+# | geom_boxplot()   | 箱线图        | color,fill,alpha,notch,width            |# +------------------+---------------+-----------------------------------------+# | geom_density()   | 核密度图      | color,fill,alpha,linetype               |# +------------------+---------------+-----------------------------------------+# | geom_histogram() | 直方图        | color,fill,alpha,linetype,binwidth      |# +------------------+---------------+-----------------------------------------+# | geom_hline()     | 水平线条      | color,alpha,linetype，size              |# +------------------+---------------+-----------------------------------------+# | geom_jitter()    | 抖动点        | color,size,alpha,shape                  |# +------------------+---------------+-----------------------------------------+# | geom_line()      | 线图          | colorvalpha,linetype,size               |# +------------------+---------------+-----------------------------------------+# | geom_piont()     | 散点图        | color,alpha,shape,size                  |# +------------------+---------------+-----------------------------------------+# | geom_rug()       | 地毯图        | color,side                              |# +------------------+---------------+-----------------------------------------+# | geom_smooth()    | 拟合曲线      | method,formula,color,fill,linetype,size |# +------------------+---------------+-----------------------------------------+# | geom_text()      | 文本注解      | 选项很多，详见帮助信息                  |# +------------------+---------------+-----------------------------------------+# | geom_violin（）  | 小提琴图      | color，fill,alpha,lintype               |# +------------------+---------------+-----------------------------------------+# | geom_vline()     | 垂线          | color，alpha,linetype,size              |# +------------------+---------------+-----------------------------------------+# # **注解** # # color表示颜色，可以用名称或十六进制代码指定,几何图形外框颜色# # alpha表示透明度，0（完全透明）-1（完全不透明）# # fill表示几何图形填充颜色# (2) 举例#对刚刚的数据（工作年限和工资）做散点图，用geom_piont()library(ggplot2)library(mosaicData)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+geom_point()#图片中显示出一个异常值，可以对其删除后再做图：library(ggplot2)library(mosaicData)CPS85 <- CPS85[CPS85$wage<40,]ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point()#利用geom_smooth()函数在图片中添加一条趋势线ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point()ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="red",alpha=0.5,size=1.5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="red",alpha=0.1,size=1.5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="red",alpha=0.1,size=5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  geom_smooth(method = "lm")+  theme_bw()
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=8)

R语言入门课

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)

1、课程简介

[生信基地](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522649&idx=1&sn=a3a3df860fd162691403281356dcbf1d&chksm=9b3ce009ac4b691fc8679c43988a0a36e176760d3e21b2489b43184f0248b6409cbe8dcbb96a&scene=21#wechat_redirect>)希望能够给大家提供**系统性** 、**形成性** 、**规范性** 的生信教学。前面几次活动中同学们表示希望能够有线下集中学习以及**针对性的指导、答疑** 。所以，此次我们已推出"生信**R语言入门课** "，分为"R介绍"、"R语言数据对象"、"基本数据管理"、"图形初级(ggplot2)"四个模块共12节课。当然，我们也**不做生信快餐** ，本次活动回放已剪辑完毕，方便错过活动的小伙伴加入。后续我们会**持续拉群** 在群里进行**课程内容** 的答疑。

2、R语言介绍R语言是一种专门为统计分析、数据可视化和计算而设计的编程语言，广泛应用于各个领域。R语言支持各种统计分析方法，如线性回归、方差分析、聚类分析等，同时也能够进行复杂的图形和数据可视化。R语言凭借其开源、免费、工具包丰富、数据处理能力强、可视化丰富的特性在**生物信息学中被广泛应用** 。例如RNA-Seq差异分析常用的DESeq2、edgeR的引用次数多达数万次。我们制作的[单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522475&idx=1&sn=84dd9a65348528be9aa2b8d2711d776c&scene=21#wechat_redirect>)教程几乎也全是基于R语言环境。很多同学找我们学习单细胞的时候都表示不想学习R语言，直接学习单细胞分析，[不积跬步无以至千里](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=2&sn=f77d7ad73e7cb9c76ea2fb7fbf7a5cd1&scene=21#wechat_redirect>)，这显然是不现实的，所以，欢迎大家来参加此次的课程。

**报名二维码：**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=13)

资料&课表

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=14)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=15)本次课程的学习资料可以联系文末客服微信领取:
![图片](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpxtWyh2oFbkW2gT4k8lvFeXnI6JzN8xM8RWSXTJPtry2H5QSUWJibTYSfMGpAso9qicgN8M7rAI617g/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

目前12节总计5.5h的视频课程回放已剪辑完毕，方便错过直播的同学随时加入学习：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxPGbgxeKtcc5DibsheFewicmia5jPx1Jic18ZUJqYpNs4cvxLhCgricA2YjPPjbqo5SpE6MEibz9OgSAEw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

除了学习视频外，还给大家准备了学习资料，包括学习手册、课后习题。大家人手一份资料可以跟着视频联系：

![图片](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxPGbgxeKtcc5DibsheFewicmicfPruB2l20gdfdRoAM8Aj1ULhAhgM1ZQibjBMq2UkO7ugkiagmxL5TLg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

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

4.2.1 放置数据和映射选项4.2.2 将图形作为对象使用4.2.3 保存图形![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=19)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24) 您点的每个赞和在看，我都认真当成了喜欢
