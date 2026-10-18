---
title: "R语言绘图神器| geom函数"
date: 2025-10-08
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531369&idx=1&sn=cbd56bbf14a224aa53a1fe25cc6defb5&chksm=9b3c0239ac4b8b2fb88e5b8f6f7fe86057fcd0c09282e5be68d20d877f9dd237d046d22a89c2#rd
albums: ["编程语言教程"]
---

# R语言绘图神器| geom函数

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531369&idx=1&sn=cbd56bbf14a224aa53a1fe25cc6defb5&chksm=9b3c0239ac4b8b2fb88e5b8f6f7fe86057fcd0c09282e5be68d20d877f9dd237d046d22a89c2#rd
> 合集：编程语言教程

![图片](../../images/c33e327c8d66af99.webp)

geom系列函数

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

在 R 语言的ggplot2包中，`geom_*`系列函数是用于数据可视化的核心，它们用于指定绘图的几何对象（图形元素），决定了数据将以何种形式（如点、线、柱状等）呈现。以下是一些常用的`geom_*`函数及其用途：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
###### 4.1.2 geom()函数 ####### (1) 函数选项# 该函数是规定在图形上放置什么样的几何对象(点、线、条、阴影区域)，常用选项为：# # +------------------+---------------+-----------------------------------------+# | 函数             | 添加的图形    | 选项                                    |# +:=================+:==============+:========================================+# | geom_bar()       | 条形图        | color,fill,alpha                        |# +------------------+---------------+-----------------------------------------+# | geom_boxplot()   | 箱线图        | color,fill,alpha,notch,width            |# +------------------+---------------+-----------------------------------------+# | geom_density()   | 核密度图      | color,fill,alpha,linetype               |# +------------------+---------------+-----------------------------------------+# | geom_histogram() | 直方图        | color,fill,alpha,linetype,binwidth      |# +------------------+---------------+-----------------------------------------+# | geom_hline()     | 水平线条      | color,alpha,linetype，size              |# +------------------+---------------+-----------------------------------------+# | geom_jitter()    | 抖动点        | color,size,alpha,shape                  |# +------------------+---------------+-----------------------------------------+# | geom_line()      | 线图          | colorvalpha,linetype,size               |# +------------------+---------------+-----------------------------------------+# | geom_piont()     | 散点图        | color,alpha,shape,size                  |# +------------------+---------------+-----------------------------------------+# | geom_rug()       | 地毯图        | color,side                              |# +------------------+---------------+-----------------------------------------+# | geom_smooth()    | 拟合曲线      | method,formula,color,fill,linetype,size |# +------------------+---------------+-----------------------------------------+# | geom_text()      | 文本注解      | 选项很多，详见帮助信息                  |# +------------------+---------------+-----------------------------------------+# | geom_violin（）  | 小提琴图      | color，fill,alpha,lintype               |# +------------------+---------------+-----------------------------------------+# | geom_vline()     | 垂线          | color，alpha,linetype,size              |# +------------------+---------------+-----------------------------------------+# # **注解** # # color表示颜色，可以用名称或十六进制代码指定,几何图形外框颜色# # alpha表示透明度，0（完全透明）-1（完全不透明）# # fill表示几何图形填充颜色
```

![图片](../../images/f74ae4c6b8127d36.webp)

视频教程

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

"R语言入门课"是我们认为**生信小白入门** 不得不听的一个课程，我们也为这个课程准备了许多**干货** 。R语言的精髓便是数据处理，在本节课中，我们详细介绍了向量、矩阵、数据框、数组、因子、列表的创建方法与数据访问方式，为以后的生物信息学数据处理打下牢固的基础！

![图片](../../images/f74ae4c6b8127d36.webp)

本期代码

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
# (2) 举例#对刚刚的数据（工作年限和工资）做散点图，用geom_piont()library(ggplot2)library(mosaicData)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+geom_point()#图片中显示出一个异常值，可以对其删除后再做图：library(ggplot2)library(mosaicData)CPS85 <- CPS85[CPS85$wage<40,]ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point()#利用geom_smooth()函数在图片中添加一条趋势线ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point()ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="red",alpha=0.5,size=1.5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="red",alpha=0.1,size=1.5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="red",alpha=0.1,size=5)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  geom_smooth(method = "lm")+  theme_bw()#注意，lm是字母l，不是数字1head(CPS85)# a. 箱线图 - 按行业(sector)展示工资分布ggplot(data = CPS85, mapping = aes(x = sector, y = wage)) +  geom_boxplot(fill = "lightblue", color = "darkblue", alpha = 0.3) # b. 直方图 - 工资分布ggplot(CPS85, aes(x = wage)) +  geom_histogram(binwidth = 2, fill = "orange", color = "black", alpha = 0.7) ggplot(CPS85, aes(x = wage)) +  geom_histogram(binwidth = 10, fill = "green", color = "white", alpha = 0.7) # c. 核密度图 - 工作经验的密度分布ggplot(CPS85, aes(x = exper)) +  geom_density(fill = "green", color = "darkgreen", alpha = 0.5) # d. 抖动点图 - 按性别展示工资与经验关系ggplot(CPS85, aes(x = exper, y = wage, color = sex)) +  geom_jitter(alpha = 0.6, size = 2) # geom_point()# e. 条形图 - 不同行业的平均工资ggplot(CPS85, aes(x = sector, y = wage)) +  geom_bar(stat = "summary", fun = "mean", fill = "purple", alpha = 0.7) # f. 小提琴图 - 按婚姻状况展示工资分布ggplot(CPS85, aes(x = married, y = wage)) +  geom_violin(fill = "pink", color = 'blue', alpha = 0.6)
```

![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

R语言入门课

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

1、课程简介

[生信基地](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522649&idx=1&sn=a3a3df860fd162691403281356dcbf1d&chksm=9b3ce009ac4b691fc8679c43988a0a36e176760d3e21b2489b43184f0248b6409cbe8dcbb96a&scene=21#wechat_redirect>)希望能够给大家提供**系统性** 、**形成性** 、**规范性** 的生信教学。前面几次活动中同学们表示希望能够有线下集中学习以及**针对性的指导、答疑** 。所以，此次我们已推出"生信**R语言入门课** "，分为"R介绍"、"R语言数据对象"、"基本数据管理"、"图形初级(ggplot2)"四个模块共12节课。当然，我们也**不做生信快餐** ，本次活动回放已剪辑完毕，方便错过活动的小伙伴加入。后续我们会**持续拉群** 在群里进行**课程内容** 的答疑。

2、R语言介绍R语言是一种专门为统计分析、数据可视化和计算而设计的编程语言，广泛应用于各个领域。R语言支持各种统计分析方法，如线性回归、方差分析、聚类分析等，同时也能够进行复杂的图形和数据可视化。R语言凭借其开源、免费、工具包丰富、数据处理能力强、可视化丰富的特性在**生物信息学中被广泛应用** 。例如RNA-Seq差异分析常用的DESeq2、edgeR的引用次数多达数万次。我们制作的[单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522475&idx=1&sn=84dd9a65348528be9aa2b8d2711d776c&scene=21#wechat_redirect>)教程几乎也全是基于R语言环境。很多同学找我们学习单细胞的时候都表示不想学习R语言，直接学习单细胞分析，[不积跬步无以至千里](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=2&sn=f77d7ad73e7cb9c76ea2fb7fbf7a5cd1&scene=21#wechat_redirect>)，这显然是不现实的，所以，欢迎大家来参加此次的课程。

**报名二维码：**

![图片](../../images/fe8ecb8594a1f419.webp)![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

资料&课表

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)本次课程的学习资料可以联系文末客服微信领取:
![图片](../../images/f94ff1279b2a77aa.gif)

目前12节总计5.5h的视频课程回放已剪辑完毕，方便错过直播的同学随时加入学习：

![图片](../../images/784fdfd3a0834115.webp)

除了学习视频外，还给大家准备了学习资料，包括学习手册、课后习题。大家人手一份资料可以跟着视频联系：

![图片](../../images/391e1fc5efca5fed.webp)

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

4.2.1 放置数据和映射选项4.2.2 将图形作为对象使用4.2.3 保存图形![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/fe8ecb8594a1f419.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
