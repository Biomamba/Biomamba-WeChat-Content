---
title: "ggsci，搞定你的SCI绘图配色"
date: 2025-12-13
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532785&idx=1&sn=f38558755961700d588e038e548e934f&chksm=9b3c39a1ac4bb0b7a820019bd062883f6e1c22e2fee9bdb3f25b428236c4895bac651f6bc6cf#rd
albums: ["编程语言教程"]
---

# ggsci，搞定你的SCI绘图配色

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532785&idx=1&sn=f38558755961700d588e038e548e934f&chksm=9b3c39a1ac4bb0b7a820019bd062883f6e1c22e2fee9bdb3f25b428236c4895bac651f6bc6cf#rd
> 合集：编程语言教程

# **一、视频教程：**

![](../../images/90fab1387787746b.gif)

前段时间分析数据绘图时总为选图片的**配色** 而烦恼，经人提醒学习了一手`ggsci`，果然药到病除。`ggsci`中收录了来自于**科研文献** ，**可视化数据库** 、**科幻电影** 、**电视节目** 的配色方案。此外 **ColorBrewer** 和**viridis** 也能提供优秀的配色方案，感兴趣的同学可以试一试。

大家可以先做一做[R语言基础小测验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528153&idx=1&sn=a6e1015ac93a6e1d310039f91230e14a&scene=21#wechat_redirect>)，看看自己是否需要跟我们[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)的课程。

先上教程视频，B站同步播出：

https://www.bilibili.com/video/BV1miNVeWEkw

完整视频回放和答疑服务可见：[5.5h入门R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528126&idx=2&sn=668c2709891956b567b316f9f2fb26ea&scene=21#wechat_redirect>)

本节课程视频：

# **二、离散型数据**

![](../../images/90fab1387787746b.gif)

ggsci具体收录的配色方案有：

![](../../images/e2d292b0b685828f.webp)

## **2.0 装包**

  *   *   *   *   *

```
#安装并加载包if(!require(ggsci))library("ggsci")if(!require(ggplot2))library("ggplot2")if(!require(gridExtra))library("gridExtra")#又一个调整data("diamonds")#测试数据
```

## **2.1 准备离散型数据**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
p1 = ggplot(subset(diamonds, carat >= 2.2),       aes(x = table, y = price, colour = cut)) +  geom_point(alpha = 0.7) +  geom_smooth(method = "loess", alpha = 0.05, size = 1, span = 1) +  theme_bw()+  labs(title = 'ggplot2配色')
p2 = ggplot(subset(diamonds, carat > 2.2 & depth > 55 & depth < 70),       aes(x = depth, fill = cut)) +  geom_histogram(colour = "black", binwidth = 1, position = "dodge") +  theme_bw()+  labs(title = 'ggplot2配色')library(patchwork)p1|p2#ggplot2的配色其实也还不错
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/2ab6f8db3f51ab95.webp)

## **2.1 离散型数据可视化**

## **2.2.1 NPG主题配色**

**NPG全称Nature Publishing Group，即Nature系的配色. 在ggplot2中可以用` scale_color_pal`和`scale_fill_npg`直接更改配色(`pal`替换为主题名称即可)**

  *   *   *

```
p1_npg = p1 + scale_color_npg()+labs(title = 'npg配色')p2_npg = p2 + scale_fill_npg()+labs(title = 'npg配色')grid.arrange(p1_npg, p2_npg, ncol = 2)#这个拼图包看起来也很好用，下次出个教程
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/953cf9df3f5802ad.webp)

## **2.2.2 AAAS**

**AAAS全称American Association for the Advancement of Science，来感受一下画风：**

  *   *   *

```
p1_aaas = p1 + scale_color_aaas()+labs(title = 'aaas配色')p2_aaas = p2 + scale_fill_aaas()+labs(title = 'aaas配色')grid.arrange(p1_aaas, p2_aaas, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/4c76102c108936f5.webp)

## **2.2.3 NEJM**

**New England Journal of Medicine**

  *   *   *

```
p1_nejm = p1 + scale_color_nejm()+labs(title = 'nejm配色')p2_nejm = p2 + scale_fill_nejm()+labs(title = 'nejm配色')grid.arrange(p1_nejm, p2_nejm, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/27a8838acf1378a2.webp)

## **2.2.4 Lancet**

  *   *   *

```
p1_lancet = p1 + scale_color_lancet()+labs(title = 'lancet配色')p2_lancet = p2 + scale_fill_lancet()+labs(title = 'lancet配色')grid.arrange(p1_lancet, p2_lancet, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/697a14b76f77d0e9.webp)

**2.2.5 JAMA**

**The Journal of the American Medical Association**

  *

```
p1_jama = p1 + scale_color_jama()+ scale_color_lancet()+labs(title = 'jama配色')
```

  *   *

```
## Scale for 'colour' is already present. Adding another scale for 'colour',## which will replace the existing scale.
```

  *   *

```
p2_jama = p2 + scale_fill_jama()+labs(title = 'jama配色')grid.arrange(p1_jama, p2_jama, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/21583cf69f75a2aa.webp)

**2.2.6 JCO**

**Journal of Clinical Oncology**

  *   *   *

```
p1_jco = p1 + scale_color_jco()+labs(title = 'jco配色')p2_jco = p2 + scale_fill_jco()+labs(title = 'jco配色')grid.arrange(p1_jco, p2_jco, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/70193c11cade4739.webp)

**2.2.7 USCGB**

**UCSC Genome Browser for representing chromosomes**

  *   *   *

```
p1_ucscgb = p1 + scale_color_ucscgb()+labs(title = 'ucscgb配色')p2_ucscgb = p2 + scale_fill_ucscgb()+labs(title = 'ucscgb配色')grid.arrange(p1_ucscgb, p2_ucscgb, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/69f54264e408e626.webp)

## **2.2.8 LocusZoom**

  *   *   *

```
p1_locuszoom = p1 + scale_color_locuszoom()+labs(title = 'locuszoom配色')p2_locuszoom = p2 + scale_fill_locuszoom()+labs(title = 'locuszoom配色')grid.arrange(p1_locuszoom, p2_locuszoom, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/e814b2d44de2cd19.webp)

## **2.2.9 D3**

D3是一个依赖java的可视化库:https://d3js.org/

  *   *   *

```
p1_d3 = p1 + scale_color_d3()+labs(title = 'd3配色')p2_d3 = p2 + scale_fill_d3()+labs(title = 'd3配色')grid.arrange(p1_d3, p2_d3, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/6618f6cf1dc98c4b.webp)

## **2.2.10 IGV**

**Integrative Genomics Viewer**

  *   *   *

```
p1_igv_default = p1 + scale_color_igv()+labs(title = 'igv_default配色')p2_igv_default = p2 + scale_fill_igv()+labs(title = 'igv_default配色')grid.arrange(p1_igv_default, p2_igv_default, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/993e77ef7fea81df.webp)

## **2.2.11 UChicago**

**University of Chicago**

  *   *   *

```
p1_uchicago = p1 + scale_color_uchicago()+labs(title = 'uchicago配色')p2_uchicago = p2 + scale_fill_uchicago()+labs(title = 'uchicago配色')grid.arrange(p1_uchicago, p2_uchicago, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/16a4020a2226c790.webp)

## **2.2.12 Star Trek**

**星际迷航**

  *   *   *

```
p1_startrek = p1 + scale_color_startrek()+labs(title = 'startrek配色')p2_startrek = p2 + scale_fill_startrek()+labs(title = 'startrek配色')grid.arrange(p1_startrek, p2_startrek, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/ca8ce70e97a4e550.webp)

## **2.2.13 Tron Legacy**

  *   *   *   *   *   *   *   *

```
p1_tron = p1 + theme_dark() + theme(    panel.background = element_rect(fill = "#2D2D2D"),    legend.key = element_rect(fill = "#2D2D2D")) +  scale_color_tron()+labs(title = 'tron配色')p2_tron = p2 + theme_dark() + theme(    panel.background = element_rect(fill = "#2D2D2D")) +  scale_fill_tron()+labs(title = 'tron配色')grid.arrange(p1_tron, p2_tron, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/671731da7aaa6906.webp)

## **2.2.14 Futurama**

**来自Futurama**

  *   *   *

```
p1_futurama = p1 + scale_color_futurama()+labs(title = 'Futurama配色')p2_futurama = p2 + scale_fill_futurama()+labs(title = 'Futurama配色')grid.arrange(p1_futurama, p2_futurama, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/6ef0ed03c3f1a58a.webp)

## **2.2.15 Rick and Morty**

  *   *   *

```
p1_rickandmorty = p1 + scale_color_rickandmorty()+labs(title = 'rickandmorty配色')p2_rickandmorty = p2 + scale_fill_rickandmorty()+labs(title = 'rickandmorty配色')grid.arrange(p1_rickandmorty, p2_rickandmorty, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/e172bcf6afca2a47.webp)

## **2.2.16 The Simpsons**

**《辛普森一家人》**

  *   *   *

```
p1_simpsons = p1 + scale_color_simpsons()+labs(title = 'simpsons配色')p2_simpsons = p2 + scale_fill_simpsons()+labs(title = 'simpsons配色')grid.arrange(p1_simpsons, p2_simpsons, ncol = 2)
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/87813d247a1b10d3.webp)

# **三、连续性数据**

![](../../images/90fab1387787746b.gif)

## **3.1 准备工作**

  *

```r
library("reshape2")
```

  *

```
## Warning: package 'reshape2' was built under R version 4.0.5
```

  *   *   *   *

```
data("mtcars")cor = cor(unname(cbind(mtcars, mtcars, mtcars, mtcars)))cor_melt = melt(cor)head(mtcars)
```

  *   *   *   *   *   *   *

```
##                    mpgcyldisphpdratwtqsecvsamgearcarb## MazdaRX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4## MazdaRX4Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4## Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1## Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1## HornetSportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2## Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
```

  *   *   *   *   *   *   *

```
p3 = ggplot(cor_melt,            aes(x = Var1, y = Var2, fill = value)) +  geom_tile(colour = "black", size = 0.3) +  theme_bw() +  theme(axis.title.x = element_blank(),        axis.title.y = element_blank())p3#看看原图
```

![](../../images/8247eb3878cf5f3c.webp)

## **3.2 连续性数据可视化**

## **3.2.1 GSEA**

这一配色由GSEA GenePattern (https://www.genepattern.org/)[https://www.genepattern.org/]启发而来

  *   *   *

```
p3_gsea     = p3 + scale_fill_gsea()p3_gsea_inv = p3 + scale_fill_gsea(reverse = TRUE)grid.arrange(p3_gsea, p3_gsea_inv, ncol = 2)
```

Hide

![](../../images/a7cd70292680f5c5.webp)

### **Material Design**

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
library("reshape2")set.seed(42)k = 9x = diag(k)x[upper.tri(x)] = runif(sum(1:(k - 1)), 0, 1)#upper.tri返回一个上三角是TRUE的布尔值矩阵，runif指定最大值与最小值生成一些列均匀分布的值x_melt = melt(x)
p4 = ggplot(x_melt, aes(x = Var1, y = Var2, fill = value)) +  geom_tile(colour = "black", size = 0.3) +  scale_x_continuous(expand = c(0, 0)) +  scale_y_continuous(expand = c(0, 0)) +  theme_bw() + theme(    legend.position = "none", plot.background = element_blank(),    axis.line = element_blank(), axis.ticks = element_blank(),    axis.text.x = element_blank(), axis.text.y = element_blank(),    axis.title.x = element_blank(), axis.title.y = element_blank(),    panel.background = element_blank(), panel.border = element_blank(),    panel.grid.major = element_blank(), panel.grid.minor = element_blank())p1
```

  *

```
## `geom_smooth()` using formula 'y ~ x'
```

![](../../images/fcb13a8328ec875a.webp)
Material Design主要用于生成色系：

  *   *   *   *   *   *   *   *   *   *   *   *

```
grid.arrange(  p4 + scale_fill_material("red"),         p4 + scale_fill_material("pink"),  p4 + scale_fill_material("purple"),      p4 + scale_fill_material("deep-purple"),  p4 + scale_fill_material("indigo"),      p4 + scale_fill_material("blue"),  p4 + scale_fill_material("light-blue"),  p4 + scale_fill_material("cyan"),  p4 + scale_fill_material("teal"),        p4 + scale_fill_material("green"),  p4 + scale_fill_material("light-green"), p4 + scale_fill_material("lime"),  p4 + scale_fill_material("yellow"),      p4 + scale_fill_material("amber"),  p4 + scale_fill_material("orange"),      p4 + scale_fill_material("deep-orange"),  p4 + scale_fill_material("brown"),       p4 + scale_fill_material("grey"),  p4 + scale_fill_material("blue-grey"),  ncol = 6)
```

![](../../images/4b4afa8c31d88833.webp)

# **四、****非ggplot2图形**

# ****

![](../../images/90fab1387787746b.gif)

上面我们用` scale_fill_pal`和`scale_fill_pal`调整图片的色系，若需要在其它可视化软件中使用`ggsci`，则可使用`pal_pal名`的形式生成rgb颜色调用

  *   *

```
mypal = pal_npg("nrc", alpha = 0.7)(9)#调整透明度mypal
```

  *   *

```
## [1] "#E64B35B2" "#4DBBD5B2" "#00A087B2" "#3C5488B2" "#F39B7FB2" "#8491B4B2"## [7] "#91D1C2B2" "#DC0000B2" "#7E6148B2"
```

  *   *

```r
library("scales")show_col(mypal)
```

![](../../images/c4899525c3017415.webp)

**大家更喜欢哪一款呢**

![](../../images/90fab1387787746b.gif)

  *   *   *   *

```r
library(patchwork)p1+p1_npg+p1_aaas+p1_nejm+p1_lancet+p1_jama+p1_jco+  p1_ucscgb+p1_locuszoom+p1_d3+p1_igv_default+  p1_uchicago+p1_startrek+p1_tron+p1_futurama+p1_rickandmorty+p1_simpsons
```

![](../../images/48e7a6fafc39a7fc.webp)

![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/eff615a0a49ee4ca.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
