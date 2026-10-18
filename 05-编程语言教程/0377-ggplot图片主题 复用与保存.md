---
title: "ggplot图片主题 复用与保存"
date: 2025-11-29
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532461&idx=1&sn=7269ba89278dd67470b4aa0a3e30918b&chksm=9b3c06fdac4b8febd4a15a4efe63959302cf11de93e3363cdf0a7b27683219b781f4eb0c6849#rd
albums: ["编程语言教程"]
---

# ggplot图片主题 复用与保存

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532461&idx=1&sn=7269ba89278dd67470b4aa0a3e30918b&chksm=9b3c06fdac4b8febd4a15a4efe63959302cf11de93e3363cdf0a7b27683219b781f4eb0c6849#rd
> 合集：编程语言教程

![图片](../../images/c33e327c8d66af99.webp)

图片主题、复用与保存

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

1、themme函数

ggplot2 中的 `theme()` 函数是 **控制图表非数据部分外观的核心工具** —— 它不改变图表的核心数据映射（如点、线、柱状图的位置 / 大小 / 颜色，这些由 `aes()` 和几何对象 `geom_*` 控制），而是负责调整图表的 “装饰性元素”，比如标题样式、坐标轴标签、图例位置、背景颜色、网格线等，最终实现图表的个性化美化和风格统一。常用的主题设置有：

element_text()：控制文本样式（字体、大小、颜色、加粗 / 斜体、对齐方式）；

element_line()：控制线条样式（颜色、粗细、线型：实线solid/ 虚线dashed等）；

element_rect()：控制矩形区域样式（填充色、边框颜色、边框粗细）；

element_blank()：隐藏对应元素（比如 panel.grid = element_blank() 隐藏所有网格线）。

2、图片复用

ggplot2 的核心设计是「图层叠加」，图表本质是一个可修改、可扩展的 ggplot 类对象。你可以将基础图表（如数据映射、核心几何对象）保存为变量，后续通过叠加图层、修改主题 / 标签等方式复用，无需重复写基础代码。

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

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
###### 4.1.5 theme主题与图片的复用、保存 ######  #theme_主题可以控制背景、颜色、字体、网格线、图例位置、及其他与数据无关的图形特征。ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)# theme_bw()函数将灰色背景变为白色ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  theme_bw()ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  theme_grey()ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  theme_dark()ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(color="blue",alpha=0.5,size=1.5)+  theme_light()#前面用到的theme_bw()就是将背景颜色设置为白色，# 这里我们展示一个简约主题(**theme_minimal()**):ggplot(data = CPS85,mapping = aes(x=exper,y=wage))+  geom_point(alpha=0.5)+  theme_minimal()# 基础图形（你的原始示例）p_base <- ggplot(data = CPS85,                  mapping = aes(x = exper, y = wage,                                color = sex, shape = sex, linetype = sex)) +  geom_point(alpha = 0.5) +  geom_smooth(method = "lm", se = FALSE) +  theme_minimal() +  labs(title = "工作经验与工资关系",        x = "工作经验（年）",        y = "工资（美元/小时）",       color = "性别", shape = "性别", linetype = "性别")print(p_base)# 1. 调整标题和轴标签样式p1 <- p_base +  theme(    plot.title = element_text(size = 16, face = "bold",                               color = "green", hjust = 0.5),    axis.title.x = element_text(size = 12, color = "orange", face = "italic"),    axis.title.y = element_text(size = 12, color = "orange", face = "italic")  )print(p1)# 2. 自定义刻度文本和网格线p2 <- p1 +  theme(    axis.text.x = element_text(size = 10, color = "orange"),    axis.text.y = element_text(size = 10, color = "orange"),    panel.grid.major = element_line(color = "purple", linewidth = 0.5),# 主网格线    panel.grid.minor = element_line(color = "red", linewidth = 0.3,                                     linetype = "dashed")# 次网格线  )print(p2)# 3. 调整图例样式和位置p3 <- p2 +  theme(    legend.position = "right",  # "right" "bottom" "left" "top" "none"     legend.box = "vertical",# "horizontal",   # 图例水平排列, 垂直排列"vertical"     legend.key.width = unit(2, "cm")  # 增加图例符号宽度  )print(p3)# 4. 添加绘图区边框和背景p4 <- p3 +  theme(    panel.border = element_rect(color = "white", fill = NA, linewidth = 1),    plot.background = element_rect(fill = "grey", color = NA),    plot.margin = margin(t = 15, r = 15, b = 15, l = 15, unit = "pt")  # 调整边距  )print(p4)### 4.2.3 保存图形 ####1）直接在viewer中点击处理#2）**ggsave()**函数ggsave(file="mygragh.png",plot = p4,width = 5,height = 4,dpi = 300)# dots per inch#这里的file=是设置图片名和格式，plot=是针对哪张图保存，宽度和高度单位是英寸# 3) pdf函数pdf(file="mygragh.pdf",width = 5,height = 4)print(p4)dev.off()tiff(file="mygragh.tiff",width = 5,height = 4)print(p4)dev.off()png(file="mygragh.png",width = 5,height = 4)print(p4)dev.off()svg()jpeg()#图片格式有以下几种：pdf,jpeg,tiff,png,svg,
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
