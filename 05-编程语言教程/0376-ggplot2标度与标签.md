---
title: "ggplot2标度与标签"
date: 2025-11-15
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532105&idx=1&sn=27c7374577711ed2c15a67163e587919&chksm=9b3c0719ac4b8e0fe5a13dc6a2aa97bc2cbf190cb8d1e37e341135d9971c8f13523caf6d5c61#rd
albums: ["编程语言教程"]
---

# ggplot2标度与标签

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532105&idx=1&sn=27c7374577711ed2c15a67163e587919&chksm=9b3c0719ac4b8e0fe5a13dc6a2aa97bc2cbf190cb8d1e37e341135d9971c8f13523caf6d5c61#rd
> 合集：编程语言教程

![图片](../../images/c33e327c8d66af99.webp)

刻度与标签

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

在 ggplot2 中，控制刻度与标签的核心思路是使用标度（Scale）函数。这些函数通常以 scale_开头，后接对应的美学属性（如 x_continuous, y_discrete, color, fill等），最后是修改的类型（如 breaks, labels, limits）。

1\. 主要设置：Breaks, Labels, Limits

breaks（刻度线位置）： 决定在坐标轴的什么位置显示刻度线（和对应的标签）。例如，在 x 轴上为 1, 2, 3, 4, 5 这些点。

labels（刻度标签）： 对应每个 break点所显示的文本。你可以将数字 1的标签显示为 "一月"。

limits（坐标轴范围）： 定义坐标轴的显示范围，超出此范围的数据将被剔除（默认为 NA，即不剔除，但会不显示）。

2\. 针对不同类型的坐标轴 A. 连续型坐标轴 用于数值型数据。主要使用 scale_x_continuous()和 scale_y_continuous()。

![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

视频教程

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

"R语言入门课"是我们认为**生信小白入门** 不得不听的一个课程，我们也为这个课程准备了许多**干货** 。R语言的精髓便是数据处理，在本节课中，我们详细介绍了向量、矩阵、数据框、数组、因子、列表的创建方法与数据访问方式，为以后的生物信息学数据处理打下牢固的基础！

![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

本次课程代码

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
###### 4.1.4 标度与标签 ####### 标度# 标度/标尺是指定每个映射是如何进行的，以scale开头的系列函数，# 下面为一些常用函数：# # +----------------------+---------------------------------------------------------------------------------------------------------------------+# | 函数                 | 描述                                                                                                                |# +======================+=====================================================================================================================+# | scale_x_continuous() | 标度连续性变量的x轴。选项包括用于指定刻度标记的breaks，用于指定刻度标记标签的labels,# |                      | 和用于控制显示的值的范围的limits # |                      |                                                                                                                     |# | scale_y_continuous() | 标度连续性变量的y轴                                                                                                                    |# +----------------------+---------------------------------------------------------------------------------------------------------------------+# | scale_x_discrete()   | 标度分类变量的x轴                                                                                    |# |                      |                                                                                                                     |# | scale_y_discrete()   |                                                                                                                     |# +----------------------+---------------------------------------------------------------------------------------------------------------------+# | scale_color_manual() | 标度代表分类变量层级的颜色。values选项指定颜色                                                                      |# +----------------------+---------------------------------------------------------------------------------------------------------------------+# # **举例**library(ggplot2)library(mosaicData)head(CPS85)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(alpha=0.5,size=1.5)# 将x轴范围设置为0-60，每个格子为10；y轴范围设置为0-30，# 刻度间隔为5：ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+#注：seq(0,60,10)**表示可以生成一个数值向量，从0-60，按10递增。  scale_y_continuous(breaks = seq(0,30,5))# 调整刻度极限，设置标签ggplot(CPS85, aes(x=exper, y=wage)) +  geom_point() +  # 限制x轴范围为0-40，自定义刻度标签  scale_x_continuous(    limits = c(0, 40),    breaks = c(0, 10, 20, 30, 40),    labels = c("0年", "10年", "20年", "30年", "40年")  ) +  # 调整y轴刻度和标签  scale_y_continuous(    breaks = c(5, 10, 15, 20),    labels = c("$5", "$10", "$15", "$20")  )##为x或y轴设置labels#例如这里的y轴上的单位是美元，我们可以使用**scales**包更改，这个包提供美元，欧元，百分比等标签格式：install.packages("scales")library(scales)ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+  scale_y_continuous(breaks = seq(0,30,5),                     labels = scales::dollar)#除了使用labels = scales::dollar将刻度标签设置为货币格式之外，scale_y_continuous()函数还可以接受其他参数来设置刻度标签的格式。#下面是一些常见的选项：#scales::percent：将刻度标签设置为百分比格式，例如 50%。ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+  scale_y_continuous(breaks = seq(0,30,5),                     labels = scales::percent)#scales::comma：将刻度标签设置为千位分隔符格式，例如由1000变为1,000。CPS85$wage1000 <- CPS85$wage*1000ggplot(data = CPS85,mapping = aes(x=exper,y=wage1000))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+  scale_y_continuous(labels = scales::comma)#scales::scientific：将刻度标签设置为科学计数法格式，例如 1e+03。**ggplot(data = CPS85,mapping = aes(x=exper,y=wage1000))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+  scale_y_continuous(labels = scales::scientific)ggplot(data = CPS85,mapping = aes(x=exper,y=wage1000))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+  scale_y_continuous(labels = scales::scientific,                     breaks = c(1000,2000,10000))#scales::dollar_format(prefix = "", suffix = "")：#将刻度标签设置为带有自定义前缀和后缀的货币格式。#你可以通过设置prefix参数和suffix参数来指定前缀和后缀的文本。ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(alpha=0.5,size=1.5)+  scale_x_continuous(breaks = seq(0,60,10))+  scale_y_continuous(breaks = seq(0,30,5),                     labels =                       scales::dollar_format(prefix = "收入：",                                             suffix = "(单位：万美元)")                     )# 调整分类变量坐标轴：ggplot(CPS85, aes(x=sector, y=wage)) +  geom_boxplot() +  # 调整分类x轴的顺序和标签  scale_x_discrete(    limits = c("const", "sales", "clerical"),  # 指定显示顺序    labels = c("建筑", "销售", "文书")         # 替换分类标签  )# . 自定义分组颜色（scale_color_manual/scale_fill_manual）：# 点的颜色分组ggplot(CPS85, aes(x=exper, y=wage, color=sex)) +  geom_point() +  scale_color_manual(    values = c("pink", "green"),  # 自定义颜色    labels = c("女性", "男性")   # 自定义标签  )# 填充色分组ggplot(CPS85, aes(x=married, fill=married)) +  geom_bar() +  scale_fill_manual(    values = c("lightgreen", "pink")  )# 使用预设颜色方案（scale_color_brewer）library(RColorBrewer)RColorBrewer::brewer.pal(n = 9, name = "Set1")# [1] "#E41A1C" "#377EB8" "#4DAF4A" "#984EA3" "#FF7F00" "#FFFF33" "#A65628" "#F781BF"[9] "#999999"ggplot(CPS85, aes(x=exper, y=wage, color=race)) +  geom_point() +  # 使用RColorBrewer包的预设调色板  scale_color_brewer(palette = "Set1")# 双重标度设定示例（结合分类与连续变量）ggplot(CPS85, aes(x=educ, y=wage, color=union)) +  geom_point() +  # 连续x轴调整  scale_x_continuous(breaks = seq(10, 16, 2)) +  # 分类颜色调整  scale_color_manual(values = c("black", "orange"),                     labels = c("非工会", "工会"))### 标签 ####labs()函数为坐标轴和图例提供了自定义标签。可以自行添加主标题、副标题和说明文字。ggplot(data = CPS85,        mapping = aes(x = exper, y = wage,                      color = sex, shape = sex,                      linetype = sex)) +  geom_point(alpha = 0.5) +  geom_smooth(method = "lm", se = FALSE) +  # 基础标签设置  labs(    title = "Relationship between wages and experience",  # 主标题    subtitle = "Current Population Survey (1985)",        # 副标题    caption = "Data source: CPS85 dataset from alr4 package",  # 图表注释（通常放来源）    x = "Years of Experience",         # x轴标签    y = "Hourly Wage (USD)",           # y轴标签    color = "Gender_color",                  # 颜色图例标题    shape = "Gender_shape",                  # 形状图例标题    linetype = "Gender_line"                # 线图例标题  )# ggtitleggplot(CPS85, aes(x = exper, y = wage)) +  geom_point() +  ggtitle(label = "Wage vs Experience",  # 主标题          subtitle = "CPS 1985 Data")  # 副标题（ggplot2 3.0+支持）# guidesggplot(CPS85, aes(x = exper, y = wage, color = sex, shape = sex)) +  geom_point() +  # 进一步调整图例细节  guides(    color = guide_legend(      title = "Gender_color",  # 覆盖labs()的设置      title.position = "bottom",  # 图例标题位置,'left' 'right' 'bottom'      label.hjust = 0.5,       # 标签水平居中      ncol = 2                 # 图例分2列显示    ),    shape = guide_legend(title = "Gender_shape")  # 保持与颜色图例一致  )ggplot(CPS85, aes(x = exper, y = wage, color = sex)) +  geom_point() +  labs(title = "Wage Distribution by Experience") +  # 添加文本注释  annotate("text",            x = 20, y = max(CPS85$wage),  # 注释位置           label = "Higher experience\ncorrelates with higher wages",           color = "red",           size = 3.5) +  # 添加箭头指向特定区域  annotate("segment",            x = 20, y = 25, xend = 15, yend = 20,           arrow = arrow(length = unit(0.2, "cm")))
```

![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

R语言入门课

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

1、课程简介

[生信基地](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522649&idx=1&sn=a3a3df860fd162691403281356dcbf1d&chksm=9b3ce009ac4b691fc8679c43988a0a36e176760d3e21b2489b43184f0248b6409cbe8dcbb96a&scene=21#wechat_redirect>)希望能够给大家提供**系统性** 、**形成性** 、**规范性** 的生信教学。前面几次活动中同学们表示希望能够有线下集中学习以及**针对性的指导、答疑** 。所以，此次我们已推出"生信**R语言入门课** "，分为"R介绍"、"R语言数据对象"、"基本数据管理"、"图形初级(ggplot2)"四个模块共12节课。当然，我们也**不做生信快餐** ，本次活动回放已剪辑完毕，方便错过活动的小伙伴加入。后续我们会**持续拉群** 在群里进行**课程内容** 的答疑。

2、R语言介绍R语言是一种专门为统计分析、数据可视化和计算而设计的编程语言，广泛应用于各个领域。R语言支持各种统计分析方法，如线性回归、方差分析、聚类分析等，同时也能够进行复杂的图形和数据可视化。R语言凭借其开源、免费、工具包丰富、数据处理能力强、可视化丰富的特性在**生物信息学中被广泛应用** 。例如RNA-Seq差异分析常用的DESeq2、edgeR的引用次数多达数万次。我们制作的[单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522475&idx=1&sn=84dd9a65348528be9aa2b8d2711d776c&scene=21#wechat_redirect>)教程几乎也全是基于R语言环境。很多同学找我们学习单细胞的时候都表示不想学习R语言，直接学习单细胞分析，[不积跬步无以至千里](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=2&sn=f77d7ad73e7cb9c76ea2fb7fbf7a5cd1&scene=21#wechat_redirect>)，这显然是不现实的，所以，欢迎大家来参加此次的课程。

**报名二维码：**

![图片](../../images/eff615a0a49ee4ca.webp)![图片](../../images/f74ae4c6b8127d36.webp)![图片](../../images/c33e327c8d66af99.webp)

资料&课表

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)本次课程的学习资料可以联系文末客服微信领取:
![图片](../../images/96696a6d9529ab11.gif)

目前12节总计5.5h的视频课程回放已剪辑完毕，方便错过直播的同学随时加入学习：

![图片](../../images/ca85d25b2cf710a2.webp)

除了学习视频外，还给大家准备了学习资料，包括学习手册、课后习题。大家人手一份资料可以跟着视频联系：

![图片](../../images/05f73ea769c50b09.webp)

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

![图片](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
