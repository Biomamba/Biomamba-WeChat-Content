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

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWia4SQlpl8xxKTerd4df9TRqfwy6JKwCR3RCMeKpCtBjBicPb4BX6UE2Zye4LHria9t14oxRsfre91WQ/640?wx_fmt=png)最近画了几张热图，准备拿AI拼一拼（没错我就是那个不正经的生信人），无奈图片太大，AI读进去就卡的动不了，被迫只能用R语言拼图，不过patchwork用起来是真香，基本上你在R中可以完成数据分析到排出文章Figure的所有操作，大家可以感受一下。
![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhPmGHfBz7vlEFLwDwiaiaQoC382iaybapNl4WArldyld364eSS3O5EYQvewIcOVDjsYeBCGVib7Dnwcg/640?wx_fmt=gif)

02

教学视频

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWia4SQlpl8xxKTerd4df9TRqfwy6JKwCR3RCMeKpCtBjBicPb4BX6UE2Zye4LHria9t14oxRsfre91WQ/640?wx_fmt=png)

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhPmGHfBz7vlEFLwDwiaiaQoC382iaybapNl4WArldyld364eSS3O5EYQvewIcOVDjsYeBCGVib7Dnwcg/640?wx_fmt=gif)

03

Patchwork

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWia4SQlpl8xxKTerd4df9TRqfwy6JKwCR3RCMeKpCtBjBicPb4BX6UE2Zye4LHria9t14oxRsfre91WQ/640?wx_fmt=png)

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

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutL2RzpJ1JyVQrvyMAhPbcRrRPDffWD1y0e4yM7z3OicchEVAVm3oOtyg/640?wx_fmt=png)
```r
p2 <- ggplot(mtcars) +
  geom_boxplot(aes(gear, disp, group = gear)) +
  ggtitle('Plot 2')
p2
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutLDVBAWRicx0I0rLZicENe4DzTGgiaJtRrM58sialUMBlJFzl945icLUH8Ow/640?wx_fmt=png)
```r
p3 <- ggplot(mtcars) +
  geom_point(aes(hp, wt, colour = mpg)) +
  ggtitle('Plot 3')
p3
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutJVoJZy1zm5wSaNTxAEFDg5wibq8LhtRmVGsvA7WmTyWBB5OLepjNKfQ/640?wx_fmt=png)
```r
p4 <- ggplot(mtcars) +
  geom_bar(aes(gear)) +
  facet_wrap(~cyl) +
  ggtitle('Plot 4')
p4
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutI595ic620rG3EziaD7VKyOlpom9FrkQoHzvv09nVq056aG1EZSI3ibK6g/640?wx_fmt=png)

### 最基本的排版用法
```
p1+p2#要加载patchwork，不然会显示数值相加的错误
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutzEQNQgN8y8Uf1LuRjXoHFqGSzBJr5VrJbkEH7JGqWhgFqhOoNS6vUw/640?wx_fmt=png)
```
p1 + p2 + labs(subtitle = 'This will appear in the last plot')#加上副标题
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutoGXicnN1lle7vCzQqq4QtkZgicWoyAeID7Va9CMBlFvZOXOKlgQD1zPg/640?wx_fmt=png)
```
p1+p2+p3+p4#默认情况下patchwork会让图片尽量的方正一些，所以四张图自然会以2*2的形式呈现
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut4gGowcML1S23giaBpxarat6QogIzTJuRWPicpKoEanypY2SqT2vLEdeg/640?wx_fmt=png)
```
p1 + p2 + p3 + p4 + plot_layout(nrow = 3, byrow = FALSE)#设置将图片摆成三行
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutjReicbmpSgU8arl0TcPF0VOdWU5ar0XaHJZbkpic0rNNREnZGTPkfiaXg/640?wx_fmt=png)
```
p1 + p2 + p3 + p4 + plot_layout(ncol = 3)#设置将图片摆成三列
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutvmZiaTKQuzdqO2q1hX62dYMI9mvhqicT32BvSfIw8ZVpc7YEnJHBv0Bw/640?wx_fmt=png)
```
#如果你觉得加号+设置行列的形式不够灵活，你想把某些特定的图片放在一列或一行
p1|p2#放在一行
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutzEQNQgN8y8Uf1LuRjXoHFqGSzBJr5VrJbkEH7JGqWhgFqhOoNS6vUw/640?wx_fmt=png)
```
p1/p2#放在一列
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutSiaTiaVhtBP1MwfpCkaMgTEODjGm2vcnfaA6Oa4icVdvxL1ibNRmTHwVrg/640?wx_fmt=png)
```
p1|(p2/p3)#组合拳
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutcDS2UaxOVQibAJf0umoMhZUfMHicpkQ6S3KFKHiaViahIqj1uotzfllteA/640?wx_fmt=png)

### 加入标题与文字注释
```
#添加标题
(p1 | (p2 / p3)) +
  plot_annotation(title = '组合拳加标题')#加标题
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut5sia4EG7txHeznrl3nuqK6RyxwlYS2tGOCp6BvEaZ7lFgicIzopPUFyg/640?wx_fmt=png)
```
p1 + p2 + p3  +
  plot_annotation(title = 'The surprising truth about mtcars',
                  theme = theme(plot.title = element_text(size = 18))) &
  theme(text = element_text('mono'))#调整标题的大小与风格
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut3FxYusDG5ickzkJpiccaPIWicKxENEBxibrhN9XWlIqm6JOqmw96rzWpdw/640?wx_fmt=png)
```
#添加文字注释的方式有很多

p1 + p2 + p3 +
  plot_annotation(tag_levels = 'I')#比如可以一键式加上Fig legend
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutFibAPB3FueKLIUqdQs5iaMqp5olSh6G9O30K7sNosXiaibDmmabtdmml4A/640?wx_fmt=png)
```
###下面两个是我猜的，真的有这种功能哈哈哈
p1 + p2 + p3 +
  plot_annotation(tag_levels = 'A')#用字母式的Fig legend
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutYdnWrrK6uxqfibUrSgoMSH180Vx6HibYs2F8vTJL6IUK8j2EnHicMwQIg/640?wx_fmt=png)
```
p1 + p2 + p3 +
  plot_annotation(tag_levels = 'A') &
  theme(plot.tag = element_text(size = 8))#大小也是可以调整的
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutBQ0iahH8WZibN9UuPuicXfoWuIw7P8kahjEv2wRMib1zicrCusDh1fDGcPQ/640?wx_fmt=png)
```
p1 + p2 + p3 +
  plot_annotation(tag_levels = 'A') &
  theme(plot.tag = element_text(size = 18))#大小也是可以调整的
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutGF3fKxUADmeLZlsoz81nTge62tWHF2O3kzRuJXDI7G31Nw0DvWroww/640?wx_fmt=png)
```
p1 + p2 + p3 +
  plot_annotation(tag_levels = '1')#用数字式的Fig legend
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutC2qAaEmxTPLr20BS5JxRJuGrkEgv5fl0keypEYoPD9gfbP6GhZw9eQ/640?wx_fmt=png)
```
#可以组合式的添加Fig legend，并且可以拥有前缀
p1 + p2 + p3   + plot_annotation(tag_levels = c('A', '1'), tag_prefix = 'Fig. ',
                            tag_sep = '.', tag_suffix = ':')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutBcrZibjJ72zed6gia7HWzQLc9icqjD38zPxrlvDxUXvsW6vXdYf7IEYmw/640?wx_fmt=png)
```
#感受一下title、subtitle、caption有何不同
p1 + p2 + plot_annotation(
  title = 'The surprising truth about mtcars',
  subtitle = 'These 3 plots will reveal yet-untold secrets about our beloved data-set',
  caption = 'Disclaimer: None of these plots are insightful'
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut0K5gCc0ic15iajfFWsCVDRuON7S22XzzbAqnGhhTga2OvWpKahd8MwxQ/640?wx_fmt=png)

### 一些进阶布局的方法
```
#加入空图
p1 + plot_spacer() + p2 + plot_spacer() + p3 + plot_spacer()
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutdcJeew3vwgowJhzplIrMOVosZquUUSuYgOIeUibToicCnMNMUZz9jXnA/640?wx_fmt=png)
```
(p1 + plot_spacer() + p2) / (plot_spacer() + p3 + plot_spacer())#在上面的组合拳中加空图
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutcvpfCOfeibkRGK9BEvEQWvzRUJrbyXib5ypNMnDRibBmtPKP8XUfENzvQ/640?wx_fmt=png)
```
p1 + p2 + p3 + p4 +
  plot_layout(widths = c(2, 1))#图片的不均等布局，左右之间按2：布局
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutNsuYbycMwRooG0JAb43tibgRfcTrdejppU7ljPf6C3IOVupgHKQj3Kg/640?wx_fmt=png)
```
p1 + p2 + p3 + p4 +
  plot_layout(widths = c(2, 1), heights = unit(c(5, 1), c('cm', 'null')))#同理还可以上下之间按比例布局
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutQianibKAahRawOJ2cjAQQmdibc5CC9Rib8XHYgstPLYKNgTtGb20xNOj3A/640?wx_fmt=png)
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

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutxt0X09nofltExGSenQ0HqcKqLZB7q84xD0TrIVs1L9IBdH5fvIwZog/640?wx_fmt=png)
```r
#如果你觉得上面的AABB有些混乱，你不能理解，那么你可以这样指定
layout <- '
A#B
#C#
D#E
'
wrap_plots(D = p1, C = p2, B = p3, design = layout)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutCcwRJrLwGdmS4oYS3MBP8mlyyco2QYFyZe9gpEI0auT9JgayBWicX8w/640?wx_fmt=png)
```r
#布局还可以用这种局部的方式指定，这种方法的好处是图片可以堆叠在同一位置（重叠）
layout <- c(
  area(t = 2, l = 1, b = 5, r = 4),
  area(t = 1, l = 3, b = 3, r = 5)
)
p1 + p2 +
  plot_layout(design = layout)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutiau8Aslxf9C0k2UvstqDFvWZRia1dPVs0QIib5wc0CN3DowwxiaCpBctJA/640?wx_fmt=png)
```
#与两张图片部分区域重叠相类似，你还可以将一张图片插入到另一张图片中
p1 + inset_element(p2, left = 0.6, bottom = 0.6, right = 1, top = 1)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut52dIquFFEuI0ia6zxTJibvSHkbBFY2z80JwNMuQiaTibV3uem5dEr6jvpQ/640?wx_fmt=png)
```
p1 + inset_element(p2, left = 0, bottom = 0.6, right = 0.4, top = 1, align_to = 'full')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut6JpLibysA5MT5VUMtXRAvepnW86oFDFYDje2EwzxoTXicMf49NQBNwuQ/640?wx_fmt=png)
```
p1 + inset_element(
  p2,
  left = 0.5,
  bottom = 0.5,
  right = unit(1, 'npc') - unit(1, 'cm'),
  top = unit(1, 'npc') - unit(1, 'cm')
)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutyGwAhAbhdOiaUuC40v77m3TWmXibBqxYdIAHh4E0f5Kta5J8j0ukeThA/640?wx_fmt=png)
```
#插入一个图注这种需求还是挺常见的
p3 + inset_element(p1, left = 0.5, bottom = 0, right = 1, top = 0.5,
                   on_top = FALSE, align_to = 'full')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutXeNL3QBg1OlrqM0icGqmAmw3Fv8aj9Uk3fPIHzMBBG9kMOP0fHHan1w/640?wx_fmt=png)
```
#接下来这个操作有点神奇，可以将图里的图注提取出来展示在大图的右侧
p1 + p2 + p3 + p4 #不提取
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut4gGowcML1S23giaBpxarat6QogIzTJuRWPicpKoEanypY2SqT2vLEdeg/640?wx_fmt=png)
```
p1 + p2 + p3 + p4 +
  plot_layout(guides = 'collect')#提取图注
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzut7SAX4uso8nK7oegdHKlKLlMgRHmRUPettuVrw9oYGSwG1kNAFqZckQ/640?wx_fmt=png)
```
#细节一点，你还可以指定布局中每个元素是否需要提取图注：
((p2 / p3 + plot_layout(guides = 'auto')) | p1) + plot_layout(guides = 'collect')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutP0ibjD2vVIakKdfTicTuv06aIaC8OjAR8gpba74ohuGn6dehucAI2pHA/640?wx_fmt=png)
```
#如果你不满足于仅将图注展示在大图右侧，你想给图注一个单独的空间：
p1 + p2 + p3 + guide_area() +
plot_layout(guides = 'collect')
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxFfibicRWzcLuRuHhicXlwzutibMniawjhIwDyKT6ymicHgmWkAzAUSTcJUYibvJ0sjl95CgUKzyUQW6sUw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhPmGHfBz7vlEFLwDwiaiaQoC382iaybapNl4WArldyld364eSS3O5EYQvewIcOVDjsYeBCGVib7Dnwcg/640?wx_fmt=gif)

看的出来patchwork的功能还是很强大的，最大的优点是不用忍受AI的卡顿。当然了，该用AI的时候还是用AI，Patchwork有时候操作起来也不是很方面。![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhPmGHfBz7vlEFLwDwiaiaQoC382iaybapNl4WArldyld364eSS3O5EYQvewIcOVDjsYeBCGVib7Dnwcg/640?wx_fmt=gif)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=24)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=25)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=26) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=28) 您点的每个赞和在看，我都认真当成了喜欢
