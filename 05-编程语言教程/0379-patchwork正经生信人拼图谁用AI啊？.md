---
title: "patchwork:正经生信人拼图谁用AI啊？"
date: 2025-12-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532754&idx=1&sn=7b9e196e20de37fd08bf24ca46cd9a82&chksm=9b3c3982ac4bb094e70a3505b9c01bd13a3fab385f4a4c12cda826d28675861fb6d47dac9bff#rd
albums: ["编程语言教程"]
---

# patchwork:正经生信人拼图谁用AI啊？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532754&idx=1&sn=7b9e196e20de37fd08bf24ca46cd9a82&chksm=9b3c3982ac4bb094e70a3505b9c01bd13a3fab385f4a4c12cda826d28675861fb6d47dac9bff#rd
> 合集：编程语言教程

01

写在前面

![](../../images/0a56fb4f981c0b82.png)最近画了几张热图，准备拿AI拼一拼（没错我就是那个不正经的生信人），无奈图片太大，AI读进去就卡的动不了，被迫只能用R语言拼图，不过patchwork用起来是真香，基本上你在R中可以完成数据分析到排出文章Figure的所有操作，大家可以感受一下。
![](../../images/d9d4bc5a4e8932e2.gif)

02

教学视频

![](../../images/0a56fb4f981c0b82.png)

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

![](../../images/d9d4bc5a4e8932e2.gif)

03

Patchwork

![](../../images/0a56fb4f981c0b82.png)

### 假如我有这么四张图
```r
if(!require(patchwork))install.packages('patchwork')
## 载入需要的程辑包：patchwork
library(ggplot2)
p1 <- ggplot(mtcars) +
  geom_point(aes(mpg, disp)) +
  ggtitle('Plot 1')
p1
```

![](../../images/c2fbbfa4800c627a.png)
```r
p2 <- ggplot(mtcars) +
  geom_boxplot(aes(gear, disp, group = gear)) +
  ggtitle('Plot 2')
p2
```

![](../../images/1c52c99aeb23bb72.png)
```r
p3 <- ggplot(mtcars) +
  geom_point(aes(hp, wt, colour = mpg)) +
  ggtitle('Plot 3')
p3
```

![](../../images/9655ec762aa85a49.png)
```r
p4 <- ggplot(mtcars) +
  geom_bar(aes(gear)) +
  facet_wrap(~cyl) +
  ggtitle('Plot 4')
p4
```

![](../../images/d21a45cf0dafb081.png)

### 最基本的排版用法
```
p1+p2#要加载patchwork，不然会显示数值相加的错误
```

![](../../images/a055e19914d475f6.webp)
```
p1 + p2 + labs(subtitle = 'This will appear in the last plot')#加上副标题
```

![](../../images/5809b7e8028cef01.webp)
```
p1+p2+p3+p4#默认情况下patchwork会让图片尽量的方正一些，所以四张图自然会以2*2的形式呈现
```

![](../../images/34fcd16db7c956b2.webp)
```
p1 + p2 + p3 + p4 + plot_layout(nrow = 3, byrow = FALSE)#设置将图片摆成三行
```

![](../../images/36ec341cad5b21a2.webp)
```
p1 + p2 + p3 + p4 + plot_layout(ncol = 3)#设置将图片摆成三列
```

![](../../images/b49a40d8252053fa.webp)
```
#如果你觉得加号+设置行列的形式不够灵活，你想把某些特定的图片放在一列或一行
p1|p2#放在一行
```

![](../../images/a055e19914d475f6.webp)
```
p1/p2#放在一列
```

![](../../images/f3e62b31774b2f9e.webp)
```
p1|(p2/p3)#组合拳
```

![](../../images/c8d0a75bbe942904.webp)

### 加入标题与文字注释
```
#添加标题
(p1 | (p2 / p3)) +
  plot_annotation(title = '组合拳加标题')#加标题
```

![](../../images/bbbc7d02ec833e9b.webp)
```
p1 + p2 + p3  +
  plot_annotation(title = 'The surprising truth about mtcars',
                  theme = theme(plot.title = element_text(size = 18))) &
  theme(text = element_text('mono'))#调整标题的大小与风格
```

![](../../images/8988c5ebecddf0ff.webp)
```
#添加文字注释的方式有很多

p1 + p2 + p3 +
  plot_annotation(tag_levels = 'I')#比如可以一键式加上Fig legend
```

![](../../images/28dc6d08a28eea52.webp)
```
###下面两个是我猜的，真的有这种功能哈哈哈
p1 + p2 + p3 +
  plot_annotation(tag_levels = 'A')#用字母式的Fig legend
```

![](../../images/1be4cbdf531d9068.webp)
```
p1 + p2 + p3 +
  plot_annotation(tag_levels = 'A') &
  theme(plot.tag = element_text(size = 8))#大小也是可以调整的
```

![](../../images/5ca5155a2c3c9b01.webp)
```
p1 + p2 + p3 +
  plot_annotation(tag_levels = 'A') &
  theme(plot.tag = element_text(size = 18))#大小也是可以调整的
```

![](../../images/e69c7031154d3cda.webp)
```
p1 + p2 + p3 +
  plot_annotation(tag_levels = '1')#用数字式的Fig legend
```

![](../../images/8ea9f76120ed7202.webp)
```
#可以组合式的添加Fig legend，并且可以拥有前缀
p1 + p2 + p3   + plot_annotation(tag_levels = c('A', '1'), tag_prefix = 'Fig. ',
                            tag_sep = '.', tag_suffix = ':')
```

![](../../images/d8063fed6a2c4722.webp)
```
#感受一下title、subtitle、caption有何不同
p1 + p2 + plot_annotation(
  title = 'The surprising truth about mtcars',
  subtitle = 'These 3 plots will reveal yet-untold secrets about our beloved data-set',
  caption = 'Disclaimer: None of these plots are insightful'
)
```

![](../../images/7beef210458aafc7.webp)

### 一些进阶布局的方法
```
#加入空图
p1 + plot_spacer() + p2 + plot_spacer() + p3 + plot_spacer()
```

![](../../images/b38938cc6ed4737f.webp)
```
(p1 + plot_spacer() + p2) / (plot_spacer() + p3 + plot_spacer())#在上面的组合拳中加空图
```

![](../../images/342e312e283ed232.webp)
```
p1 + p2 + p3 + p4 +
  plot_layout(widths = c(2, 1))#图片的不均等布局，左右之间按2：布局
```

![](../../images/5221071ea7b49436.webp)
```
p1 + p2 + p3 + p4 +
  plot_layout(widths = c(2, 1), heights = unit(c(5, 1), c('cm', 'null')))#同理还可以上下之间按比例布局
```

![](../../images/491be49145704fa6.webp)
```r
#如果你有更复杂的需求，你可以自定义布局的样式，记住，layout要写成四方的样子，空的地方用#替代
layout <- "
##BBBB
AACCDD
##CCDD
"
p1 + p2 + p3 + p4 +
  plot_layout(design = layout)
```

![](../../images/46322237402a94b6.webp)
```r
#如果你觉得上面的AABB有些混乱，你不能理解，那么你可以这样指定
layout <- '
A#B
#C#
D#E
'
wrap_plots(D = p1, C = p2, B = p3, design = layout)
```

![](../../images/d9c98b381d7ad8ef.webp)
```r
#布局还可以用这种局部的方式指定，这种方法的好处是图片可以堆叠在同一位置（重叠）
layout <- c(
  area(t = 2, l = 1, b = 5, r = 4),
  area(t = 1, l = 3, b = 3, r = 5)
)
p1 + p2 +
  plot_layout(design = layout)
```

![](../../images/d92a65b7f97d876a.webp)
```
#与两张图片部分区域重叠相类似，你还可以将一张图片插入到另一张图片中
p1 + inset_element(p2, left = 0.6, bottom = 0.6, right = 1, top = 1)
```

![](../../images/f18c9307531842e9.webp)
```
p1 + inset_element(p2, left = 0, bottom = 0.6, right = 0.4, top = 1, align_to = 'full')
```

![](../../images/7171c4faa15d660c.webp)
```
p1 + inset_element(
  p2,
  left = 0.5,
  bottom = 0.5,
  right = unit(1, 'npc') - unit(1, 'cm'),
  top = unit(1, 'npc') - unit(1, 'cm')
)
```

![](../../images/9da82454b0204d5e.webp)
```
#插入一个图注这种需求还是挺常见的
p3 + inset_element(p1, left = 0.5, bottom = 0, right = 1, top = 0.5,
                   on_top = FALSE, align_to = 'full')
```

![](../../images/864cac972be9eaf2.webp)
```
#接下来这个操作有点神奇，可以将图里的图注提取出来展示在大图的右侧
p1 + p2 + p3 + p4 #不提取
```

![](../../images/34fcd16db7c956b2.webp)
```
p1 + p2 + p3 + p4 +
  plot_layout(guides = 'collect')#提取图注
```

![](../../images/ffafce0f40e1ef74.webp)
```
#细节一点，你还可以指定布局中每个元素是否需要提取图注：
((p2 / p3 + plot_layout(guides = 'auto')) | p1) + plot_layout(guides = 'collect')
```

![](../../images/f4d986ec5db67950.webp)
```
#如果你不满足于仅将图注展示在大图右侧，你想给图注一个单独的空间：
p1 + p2 + p3 + guide_area() +
plot_layout(guides = 'collect')
```

![](../../images/6628089735d93500.webp)

![](../../images/d9d4bc5a4e8932e2.gif)

看的出来patchwork的功能还是很强大的，最大的优点是不用忍受AI的卡顿。当然了，该用AI的时候还是用AI，Patchwork有时候操作起来也不是很方面。![](../../images/d9d4bc5a4e8932e2.gif)
![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
