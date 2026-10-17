---
title: "Seurat对象索引 - 什么时候使用 @或$"
date: 2022-07-26
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490048&idx=1&sn=6af8aa7e8f5a35b8b16309f457e502d1&chksm=9b3f6350ac48ea46381c86c2efd14414c6cebfe4dd347a0c760171dd8e0bc9447c4ba9848e5f#rd
albums: ["单细胞教程全收录"]
---

# Seurat对象索引 - 什么时候使用 @或$

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490048&idx=1&sn=6af8aa7e8f5a35b8b16309f457e502d1&chksm=9b3f6350ac48ea46381c86c2efd14414c6cebfe4dd347a0c760171dd8e0bc9447c4ba9848e5f#rd
> 合集：单细胞教程全收录

单细胞分析经常用到`Seurat`包，整个分析过程中的中间结果都在一个Seurat对象中存储。常需要从里面提取对应数据进行后续分析，有时会用`$`，有时会用`@`，怎么选择呢？

`str`函数是我们的好帮手，清晰展示对象层级结构和索引方式，如下，对应名字前出现`@`则用`@`索引（比如`pbmc@assays`）,有`$`则用`$`索引(如`pbmc@assays$RNA`)。
```
>str(pbmc)
Formal class 'Seurat' [package "Seurat"] with 12 slots
  ..@ assays      :List of 1
  .. ..$ RNA:Formal class 'Assay' [package "Seurat"] with 7 slots
  .. .. .. ..@ counts       :Formal class 'dgCMatrix' [package "Matrix"] with 6 slots
  .. .. .. .. .. ..@ i       : int [1:2282976] 29 73 80 148 163 184 186 227 229 230 ...
  .. .. .. .. .. ..@ p       : int [1:2701] 0 779 2131 3260 4220 4741 5522 6304 7094 7626 ...
  .. .. .. .. .. ..@ Dim     : int [1:2] 13714 2700
  .. .. .. .. .. ..@ Dimnames:List of 2
  .. .. .. .. .. .. ..$ : chr [1:13714] "AL627309.1" "AP006222.2" "RP11-206L10.2" "RP11-206L10.9" ...
  .. .. .. .. .. .. ..$ : chr [1:2700] "AAACATACAACCAC" "AAACATTGAGCTAC" "AAACATTGATCAGC" "AAACCGTGCTTCCG" ...
  .. .. .. .. .. ..@ x       : num [1:2282976] 1 1 2 1 1 1 1 41 1 1 ...
  .. .. .. .. .. ..@ factors : list()
  .. .. .. ..@ data         :Formal class 'dgCMatrix' [package "Matrix"] with 6 slots
  .. .. .. .. .. ..@ i       : int [1:2282976] 29 73 80 148 163 184 186 227 229 230 ...
  .. .. .. .. .. ..@ p       : int [1:2701] 0 779 2131 3260 4220 4741 5522 6304 7094 7626 ...
  .. .. .. .. .. ..@ Dim     : int [1:2] 13714 2700
  .. .. .. .. .. ..@ Dimnames:List of 2
  .. .. .. .. .. .. ..$ : chr [1:13714] "AL627309.1" "AP006222.2" "RP11-206L10.2" "RP11-206L10.9" ...
  .. .. .. .. .. .. ..$ : chr [1:2700] "AAACATACAACCAC" "AAACATTGAGCTAC" "AAACATTGATCAGC" "AAACCGTGCTTCCG" ...
  .. .. .. .. .. ..@ x       : num [1:2282976] 1 1 2 1 1 1 1 41 1 1 ...
  .. .. .. .. .. ..@ factors : list()
  .. .. .. ..@ scale.data   : num[0 , 0 ]
  .. .. .. ..@ key          : chr "rna_"
  .. .. .. ..@ var.features : logi(0)
  .. .. .. ..@ meta.features:'data.frame':    13714 obs. of  0 variables
  .. .. .. ..@ misc         : NULL
  ..@ meta.data   :'data.frame':    2700 obs. of  7 variables:
  .. ..$ orig.ident  : Factor w/ 1 level "YSX": 1 1 1 1 1 1 1 1 1 1 ...
  .. ..$ nCount_RNA  : num [1:2700] 2419 4903 3147 2639 980 ...
  .. ..$ nFeature_RNA: int [1:2700] 779 1352 1129 960 521 781 782 790 532 550 ...
  .. ..$ phases      : Factor w/ 3 levels "G1","G2M","S": 1 1 1 1 3 1 1 1 1 1 ...
  .. ..$ G1          : num [1:2700] 0.988 0.568 0.999 0.941 0.432 0.966 0.997 0.95 0.703 0.993 ...
  .. ..$ S           : num [1:2700] 0.216 0.692 0.415 0.091 0.302 0.082 0.034 0.175 0.167 0.004 ...
  .. ..$ G2M         : num [1:2700] 0.002 0.055 0.001 0.079 0.227 0.055 0.274 0.301 0.273 0.333 ...
  ..@ active.assay: chr "RNA"
  ..@ active.ident: Factor w/ 1 level "YSX": 1 1 1 1 1 1 1 1 1 1 ...
  ..@ project.name: chr "YSX"
```

具体操作如下：
```
# 查看metadata文件列信息
> colnames(pbmc@meta.data)
[1] "orig.ident"   "nCount_RNA"   "nFeature_RNA" "phases"       "G1"     "S"     "G2M"

# 查看部分基因在部分细胞的原始reads counts
> pbmc@assays$RNA@counts[11:14,1:30]
Assay data with 13714 features for 2700 cells
First 10 features:
 AL627309.1, AP006222.2, RP11-206L10.2, RP11-206L10.9, LINC00115, NOC2L,
KLHL17, PLEKHN1, RP11-54O7.17, HES4
```

###

### 那么`$`和`@`，到底是什么？有什么区别呢？

首先这两个符号最大的区别在于：它们是两个不同的面向对象系统的提取变量的符号。**S3对象通常是列表，使用****`$`索引；****S4对象的不同slot使用****`@`索引**。

那什么是S3、S4呢？

要想知道S3、S4，首先得了解一下面向对象编程(`object-oriented programming`)，它是一种编程范式，它将对象作为程序的基本单元, 将程序和数据封装 (`encapsulate`) 其中, 以提高软件的重用性, 灵活性和扩展性。

R语言中现有的`S3`类、`S4`类、以及`R6`类等都可以实现面向对象的编程范式。

**与S3不同，S4有更正式的定义和创建对象的统一方法。**

## 如何定义S4类？

### S4类使用`setClass()`函数来定义

用R的术语来说，成员变量被称为属性。当定义一个类时，我们需要设置类的名字和成员变量（以及成员变量的属性）。每个成员变量也会称为一个`slot`。

**例子一** ：定义S4类
```
setClass("student", slots=list(name="character", age="numeric", GPA="numeric"))
```

在上面的例子中，我们定义了一个名为`student`的新类，它有三个`slot`，分别是`name` (字符型), `age` 和 `GPA` (数值型)。

## 如何创建S4对象？

### S4类使用`new()`函数来定义

**例子二** ：创建S4对象
```r
# create an object using new()
# provide the class name and value for slots
s <- new("student",name="John", age=21, GPA=3.5)
s
An object of class "student"
Slot "name":
[1] "John"
Slot "age":
[1] 21
Slot "GPA":
[1] 3.5
```

函数`setClass()`返回一个生成器函数。

这个生成器函数（通常与类同名）可用于创建新对象，它充当构造器。
```r
> student <- setClass("student", slots=list(name="character", age="numeric", GPA="numeric"))
> student
class generator function for class “student” from package ‘.GlobalEnv’
function (...)
new("student", ...)
```

现在我们可以用构造函数创建新对象。

**例子三** ：用构造函数创建S4对象
```
> student(name="John", age=21, GPA=3.5)
An object of class "student"
Slot "name":
[1] "John"
Slot "age":
[1] 21
Slot "GPA":
[1] 3.5
```

## 如何访问和修改属性？

正如使用`$`访问`list`表的组件一样，使用`@`访问对象的属性。

### 访问属性
```
s@name
[1] "John"
s@GPA
[1] 3.5
s@age
[1] 21
```

### 直接修改属性

可以通过直接赋值修改属性
```r
# modify GPA
s@GPA <- 3.7
s
An object of class "student"
Slot "name":
[1] "John"
Slot "age":
[1] 21
Slot "GPA":
[1] 3.7
```

### 用`slot()`函数修改属性
```r
> slot(s,"name")
[1] "John"
> slot(s,"name") <- "Paul"
> s
An object of class "student"
Slot "name":
[1] "Paul"
Slot "age":
[1] 21
Slot "GPA":
[1] 3.7
```

## 方法和泛型函数

与S3类一样，S4类的方法也属于泛型函数，而不是类本身。使用S4泛型与S3泛型非常相似。

可以使用`showMethods()`函数列出所有可用的S4通用函数和方法。

**例子四** ：列出所有泛型函数
```
> showMethods()
Function: - (package base)
Function: != (package base)
...
Function: trigamma (package base)
Function: trunc (package base)
```

在交互模式中输入对象名称将会输出它，用S4通用函数`show()`来达到同样效果。

您可以在上面的列表中看到这个函数，这个函数类似于`S3` `print()`函数。

**例子五** ：判断一个函数是否是泛型函数。
```
> isS4(print)
[1] FALSE
> isS4(show)
[1] TRUE
```

我们可以使用`showMethods(show)`列出show泛型函数所有的方法。

**例子六** ：列出泛型函数的所有方法。
```
> showMethods(show)
Function: show (package methods)
object="ANY"
object="classGeneratorFunction"
...
object="standardGeneric"
(inherited from: object="genericFunction")
object="traceable"
```

## 如何去写你自己的方法？

我们可以使用setMethod()帮助函数写自己的方法。

例如，我们可以实现show()泛型的类方法，如下所示。
```
setMethod("show",
"student",
function(object) {
cat(object@name, "\n")
cat(object@age, "years old\n")
cat("GPA:", object@GPA, "\n")
}
)
```

现在，如果我们像以前一样以交互模式写出对象的名称，就会执行上面的代码。

#### 参考来源

https://www.datamentor.io/r-programming/s4-class/

### R统计和作图

  * [文章用图的修改和排版 (1)](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484434&idx=1&sn=88b56a24270bd8ee34714f58bc0baa2c&scene=21#wechat_redirect>)

  * [文章用图的修改和排版 (2)](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484492&idx=1&sn=10c9b2308065b6260cfc69ea9e8d065f&scene=21#wechat_redirect>)

  * [简单强大的在线绘图](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484624&idx=1&sn=7f97f3cd03d6891f71ac3bb778ad84bb&scene=21#wechat_redirect>)

  * [简单强大的在线绘图-升级版](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484803&idx=1&sn=548b9c908a509b6532b1e69bdf630adc&scene=21#wechat_redirect>)

  * [简单强大的在线绘图-第3版](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485097&idx=1&sn=b25732da52e95ba99cdbf77e1dc45191&scene=21#wechat_redirect>)

  * [论文图表基本规范](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484341&idx=1&sn=edfa3246b21b5b1b6a2968b311d44a24&scene=21#wechat_redirect>)

  * [学术图表的基本配色方法](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484549&idx=1&sn=8363577508b1e895839154cf5fc9211f&scene=21#wechat_redirect>)

  * [数据可视化基本套路总结](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485822&idx=1&sn=240cc5593ddc303d6c5d66edc7841033&scene=21#wechat_redirect>)

  * [Graphpad，经典绘图工具初学初探](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487049&idx=1&sn=4608a0f1d38ae207ec2da9b4f620073a&scene=21#wechat_redirect>)

  * [你的包佩奇了吗？试试新版Rstudio，自动提醒缺失包！](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488401&idx=1&sn=f073614b553deb5c224f9f0028e23581&scene=21#wechat_redirect>)

  * [原来Rstudio还可以这么使用，又方便了一些](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488477&idx=1&sn=1ee62a96d17ca554853df970090759cd&scene=21#wechat_redirect>)

  * [在R中赞扬下努力工作的你，奖励一份CheatShet](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484716&idx=1&sn=eaa138c1eae4aa04057828d89a9534c4&scene=21#wechat_redirect>)

  * [别人的电子书，你的电子书，都在bookdown](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484988&idx=1&sn=b9543625901cf3aabd4e8b0373b52347&scene=21#wechat_redirect>)

  * [R语言 - 入门环境Rstudio](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483882&idx=1&sn=e16903b4b745a1ef51855be3824149f6&scene=21#wechat_redirect>)

  * [R语言 - 热图绘制 (heatmap)](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483889&idx=1&sn=9c9970cb120ac1e976713aca558ac9bf&scene=21#wechat_redirect>)

  * [R语言 - 基础概念和矩阵操作](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483891&idx=1&sn=40daf6435398c4d9a41f332e9bba4915&scene=21#wechat_redirect>)

  * [R语言 - 热图简化](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483921&idx=1&sn=8326bc566e945386cad27250a33a1bf6&scene=21#wechat_redirect>)

  * [R语言 - 热图美化](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483901&idx=1&sn=5770a863352acd8f8aec3e157131bef8&scene=21#wechat_redirect>)

  * [R语言 - 线图绘制](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483937&idx=1&sn=8368c9346ccce10121c8a7b574c12f88&scene=21#wechat_redirect>)

  * [R语言 - 线图一步法](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483947&idx=1&sn=7cf0252efff5433447507b977fcaff97&scene=21#wechat_redirect>)

  * [R语言 - 箱线图（小提琴图、抖动图、区域散点图）](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483964&idx=1&sn=ee52ac37fb9a919f5c75c0abe2a49ad4&scene=21#wechat_redirect>)

  * [R语言 - 箱线图一步法](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483971&idx=1&sn=1b40a1137ccb8b2fa1ab3eb1d0f05de9&scene=21#wechat_redirect>)

  * [R语言 - 火山图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483996&idx=1&sn=9a29d52e78e9acffeb0a78077a14f9f2&scene=21#wechat_redirect>)

  * [R语言 - 富集分析泡泡图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483978&idx=1&sn=e0c158c0e92375553036cc37f4987e40&scene=21#wechat_redirect>)

  * [R语言 - 散点图绘制](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484056&idx=1&sn=f9b2b4f7495b432e9294b7cbf42eaf33&scene=21#wechat_redirect>)

  * [R语言 - 韦恩图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484076&idx=1&sn=fa5af19a2a4db4b0c5c7f145bf93ca57&scene=21#wechat_redirect>)

  * [R语言 - 柱状图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484134&idx=1&sn=ffb41298eae74834af2f5dad05d37921&scene=21#wechat_redirect>)

  * [R语言 - 图形设置中英字体](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484427&idx=1&sn=100d10c09caa47a260df5edc7ac54714&scene=21#wechat_redirect>)

  * [R语言 - 非参数法生存分析](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484489&idx=1&sn=76cc11f3afc6d5bc5cdeeabae0941941&scene=21#wechat_redirect>)

  * [R语言 - 绘制seq logo图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485823&idx=1&sn=becc9729ed8daa76f50cf4274c79a1fb&scene=21#wechat_redirect>)

  * [WGCNA分析，简单全面的最新教程](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485220&idx=1&sn=007188964e7c43d75dcd0b11b880bbfa&scene=21#wechat_redirect>)

  * [psych +igraph：共表达网络构建](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488130&idx=1&sn=dd634aa1cd2c91ff0743b8078059ef4d&scene=21#wechat_redirect>)

  * [一文学会网络分析——Co-occurrence网络图在R中的实现](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488130&idx=2&sn=46fd83ad8ceaa9364573f482889242f1&scene=21#wechat_redirect>)

  * [一文看懂PCA主成分分析](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484036&idx=1&sn=22ee356d0c9680d56dada1b777985ed2&scene=21#wechat_redirect>)

  * [富集分析DotPlot，可以服](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484063&idx=1&sn=f4e93d428e4910b4abbee9c0430cd170&scene=21#wechat_redirect>)

  * [基因共表达聚类分析和可视化](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484779&idx=1&sn=949d6ee4403fabf046d07ae815f9c76e&scene=21#wechat_redirect>)

  * [R中1010个热图绘制方法](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484816&idx=1&sn=24f420c0d8bc341303646e191bce7700&scene=21#wechat_redirect>)

  * [还在用PCA降维？快学学大牛最爱的t-SNE算法吧, 附Python/R代码](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484978&idx=1&sn=07b7f734ad0ad44562186c1ef3663057&scene=21#wechat_redirect>)

  * [一个函数抓取代谢组学权威数据库HMDB的所有表格数据](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484926&idx=1&sn=b555e472e26f6759d3ec266f4cfd0443&scene=21#wechat_redirect>)

  * [文章用图的修改和排版](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484434&idx=1&sn=88b56a24270bd8ee34714f58bc0baa2c&scene=21#wechat_redirect>)

  * [network3D: 交互式桑基图](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485019&idx=1&sn=9cc483aff403163077621dcb82dda132&scene=21#wechat_redirect>)

  * [network3D 交互式网络生成](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485013&idx=1&sn=0252d5f8ef9386a0e63f5e35026d5bd2&scene=21#wechat_redirect>)

  * [Seq logo 在线绘制工具——Weblogo](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485852&idx=1&sn=b6f7d6ebb3a8d4b207c8422bf7a91314&scene=21#wechat_redirect>)

  * [生物AI插图素材获取和拼装指导](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485734&idx=1&sn=cfa1e683c67ca6fac92f3f1af3a49e85&scene=21#wechat_redirect>)

  * [ggplot2高效实用指南 (可视化脚本、工具、套路、配色)](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486262&idx=1&sn=d38221a4063d866b1f10f4c9ebab5f88&scene=21#wechat_redirect>)

  * [图像处理R包magick学习笔记](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486495&idx=1&sn=a33c2195872436778b0e873a771232c0&scene=21#wechat_redirect>)

  * [SOM基因表达聚类分析初探](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486507&idx=1&sn=91f60f8c8da387ff3d0502dd51445afc&scene=21#wechat_redirect>)

  * [利用gganimate可视化全球范围R-Ladies（R社区性别多样性组织）发展情况](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486926&idx=1&sn=3d1db53068b7e4155aef92a491ec8d20&scene=21#wechat_redirect>)

  * [一分钟绘制磷脂双分子层：AI零基础入门和基本图形绘制](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486994&idx=1&sn=1be4aaaaa87f48d0644b02a1177a8035&scene=21#wechat_redirect>)

  * [AI科研绘图（二）：模式图的基本画法](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487083&idx=1&sn=2a2b0f0a11cd7b992018a8eadaa4a6d1&scene=21#wechat_redirect>)

  * [你知道R中的赋值符号箭头(<-)和等号（=）的区别吗？](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487142&idx=1&sn=57ff14d9857fa0430b2e15044253f6a5&scene=21#wechat_redirect>)

  * [R语言可视化学习笔记之ggridges包](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487091&idx=1&sn=1f0d1f8c7b8d215f391f53a99aa73763&scene=21#wechat_redirect>)

  * [利用ComplexHeatmap绘制热图(一)](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487046&idx=1&sn=49c3bddb8f043fe7aa117e41862dd17b&scene=21#wechat_redirect>)

  * [ggplot2学习笔记之图形排列](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487290&idx=3&sn=491847b42ee944402aed1e2c2231b96a&scene=21#wechat_redirect>)

  * [R包reshape2，轻松实现长、宽数据表格转换](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487159&idx=1&sn=7341c4c257cd51167ee82ac237a80202&scene=21#wechat_redirect>)

  * [用R在地图上绘制网络图的三种方法](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487671&idx=1&sn=890274ff80963ec843f149cce2425185&scene=21#wechat_redirect>)

  * [PCA主成分分析实战和可视化 附R代码和测试数据](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487498&idx=1&sn=74c2b3e3f7d5386834f664120fb4f890&scene=21#wechat_redirect>)

  * [iTOL快速绘制颜值最高的进化树！](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487463&idx=1&sn=6164b33c9f46879033302b7a08326413&scene=21#wechat_redirect>)

  * [12个ggplot2扩展包帮你实现更强大的可视化](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247487442&idx=1&sn=79590ad060c4376dc0b720db62df0161&scene=21#wechat_redirect>)

  * [编程模板-R语言脚本写作：最简单的统计与绘图，包安装、命令行参数解析、文件读取、表格和矢量图输出](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247487001&idx=4&sn=552a420f765c5f1a759fd9d9cd6c3805&scene=21#wechat_redirect>)

  * [R语言统计入门课程推荐——生物科学中的数据分析Data Analysis for the Life Sciences](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486560&idx=1&sn=d9718aafbb7f349b2c12b7665c0f4327&scene=21#wechat_redirect>)

  * [数据可视化基本套路总结](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486642&idx=1&sn=2d4352719d066be88c386ef86f875d70&scene=21#wechat_redirect>)

  * [你知道R中的赋值符号箭头`<-`和等号`=`的区别吗？](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485427&idx=1&sn=1839fdcba8c252522e52919cc0bed8f3&scene=21#wechat_redirect>)

  * [使用dplyr进行数据操作30例](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486149&idx=1&sn=c9438a01599660c1e5a9c80c6da0e8c6&scene=21#wechat_redirect>)

  * [交集intersect、并集union、找不同setdiff](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485692&idx=1&sn=a94bf3e0c2f3793b791e1dd9609517b6&scene=21#wechat_redirect>)

  * [1数据类型（向量、数组、矩阵、 列表和数据框）](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485184&idx=1&sn=b2bd8dc8a3b15cf6f3e15090f24fda60&scene=21#wechat_redirect>)

  * [2读写数据所需的主要函数、与外部环境交互](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485188&idx=1&sn=a324172ee1f2617d439a994aa9f10fce&scene=21#wechat_redirect>)

  * [3数据筛选——提取对象的子集](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485219&idx=2&sn=70c605a189d1126c8f03d68da1eaa0db&scene=21#wechat_redirect>)

  * [4向量、矩阵的数学运算](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485224&idx=2&sn=d808b77676a840569c2bbfd0f2c7522e&scene=21#wechat_redirect>)

  * [5控制结构](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485234&idx=2&sn=0161cfb64bdda5491787f58e8275af81&scene=21#wechat_redirect>)

  * [6函数及作用域](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485443&idx=1&sn=2d154a1917256a3ef0f3c7bc8dc4456c&scene=21#wechat_redirect>)

  * [7认识循环函数lapply和sapply](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485545&idx=2&sn=db1879eaef980fe7bb0c8ccbb60118b6&scene=21#wechat_redirect>)

  * [8分解数据框split和查看对象str](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485593&idx=1&sn=495ce404e3f283dd69d9338b7bf208a9&scene=21#wechat_redirect>)

  * [9模拟—随机数、抽样、线性模型](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485621&idx=2&sn=8071c8dbd43ce430157319fa14cdb59e&scene=21#wechat_redirect>)

  * [1初识ggplot2绘制几何对象](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485251&idx=2&sn=2558d158e3251178111eaeb2f208c5e2&scene=21#wechat_redirect>)

  * [2图层的使用—基础、加标签、注释](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485254&idx=1&sn=375af6e8c55ead20df01768dc244b7f3&scene=21#wechat_redirect>)

  * [3工具箱—误差线、加权数、展示数据分布](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485288&idx=2&sn=d2cdf183d609368a3aeeac47d94dd3aa&scene=21#wechat_redirect>)

  * [4语法基础](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485372&idx=3&sn=e5eb09d755363334c1210105c156179b&scene=21#wechat_redirect>)

  * [5通过图层构建图像](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485476&idx=2&sn=b17e36e401f7f12c6bd0950829c77247&scene=21#wechat_redirect>)

  * [6标度、轴和图例](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485636&idx=2&sn=ca356ba8791144a6d3f3fc9b5432049f&scene=21#wechat_redirect>)

  * [7定位-分面和坐标系](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485671&idx=2&sn=35408cdf98a0c71362c2575a4bbe4b15&scene=21#wechat_redirect>)

  * [8主题设置、存储导出](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485689&idx=1&sn=e241233ebaa04bdb3d630ce0f70e417e&scene=21#wechat_redirect>)

  * [9绘图需要的数据整理技术](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485706&idx=1&sn=4b2342c39db259ce77edee5a4e57461e&scene=21#wechat_redirect>)

  * [创建属于自己的调色板](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486641&idx=2&sn=d8b2e30bacbb6445312091afd15ab379&scene=21#wechat_redirect>)

  * [28个实用绘图包，总有几个适合你](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486638&idx=1&sn=b254cabfa9b04b8491cb42405d3b5ca1&scene=21#wechat_redirect>)

  * [热图绘制](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486072&idx=1&sn=28900d8b3f40b5354643bd3b069ca918&scene=21#wechat_redirect>)

  * [R做线性回归](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485622&idx=1&sn=66db644bef7e3d1d3353692ba00dce82&scene=21#wechat_redirect>)

  * [绘图相关系数矩阵corrplot](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485147&idx=1&sn=36bde7eb3b8424eb7f7a8e77804fd4fc&scene=21#wechat_redirect>)

  * [相关矩阵可视化ggcorrplot](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484955&idx=1&sn=f494f3d82253c9e6cdb8d5f25532b409&scene=21#wechat_redirect>)

  * [绘制交互式图形recharts](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485005&idx=1&sn=5ea4cd037d8aac52be8560d5c538ccf7&scene=21#wechat_redirect>)

  * [交互式可视化CanvasXpress](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485053&idx=1&sn=37329bc98bd63d30d261df825182d533&scene=21#wechat_redirect>)

  * [聚类分析factoextra](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484997&idx=1&sn=08487a1db19bf0c1fdf8fc2f298d1dd7&scene=21#wechat_redirect>)

  * [LDA分析、作图及添加置信-ggord](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484846&idx=1&sn=488356de7f985bf929f1e31bc29affe7&scene=21#wechat_redirect>)

  * [解决散点图样品标签重叠ggrepel](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484816&idx=1&sn=cf3f06fa687edaf75b711ec8597229dc&scene=21#wechat_redirect>)

  * [添加P值或显著性标记ggpubr](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485071&idx=1&sn=1df8fe88ff06016955790aff52589992&scene=21#wechat_redirect>)

  * [Alpha多样性稀释曲线rarefraction curve](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484881&idx=1&sn=5ea55e4dba1e847268d37cae584b3ec0&scene=21#wechat_redirect>)

  * [堆叠柱状图各成分连线画法：突出组间变化](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484986&idx=1&sn=5885daab9fd0fd74871e9d22f9043e99&scene=21#wechat_redirect>)

  * [冲击图展示组间时间序列变化ggalluvial](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485074&idx=1&sn=4d4456edf0be14d2b08e335f9641ca39&scene=21#wechat_redirect>)

  * [桑基图riverplot](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485107&idx=1&sn=1a687e0cc673059f5b71b52e385ee7fd&scene=21#wechat_redirect>)

  * [微生物环境因子分析ggvegan](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485256&idx=1&sn=424905c5aa453f8eaedc9348f17fab74&scene=21#wechat_redirect>)

  * [五彩进化树与热图更配ggtree](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247484203&idx=1&sn=a8fda0759648607a24af8b63c400dc2e&scene=21#wechat_redirect>)

  * [多元回归树分析mvpart](<http://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485476&idx=1&sn=908a505054c22faae02a3af5f7d054a8&scene=21#wechat_redirect>)

  * 随机森林randomForest [分类Classification](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485517&idx=1&sn=56a28fd87abd35fe9c931f91ff84f28d&scene=21#wechat_redirect>) [回归Regression](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485545&idx=1&sn=19f43d7478e909c65ea2d7e74b4d46c7&scene=21#wechat_redirect>)

  * [加权基因共表达网络分析WGCNA](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247485516&idx=1&sn=137f9723267dbe6e5037226955b4cbbe&scene=21#wechat_redirect>)

  * [circlize包绘制circos-plot](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486056&idx=1&sn=c210c675f2fd51af5459b4729040a77c&scene=21#wechat_redirect>)

  * [R语言搭建炫酷的线上博客系统](<https://mp.weixin.qq.com/s?__biz=MzUzMjA4Njc1MA==&mid=2247486630&idx=2&sn=eca33e214176f530e9c469b2c2c390da&scene=21#wechat_redirect>)

  * [维恩(Venn)图绘制工具大全 （在线+R包）](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488184&idx=3&sn=f2f0b6c198e128a9e697c0061d31e4e0&scene=21#wechat_redirect>)

  * [R包circlize：柱状图用腻了？试试好看的弦状图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488498&idx=2&sn=0a465823b0e02b2b1698a7ba6930989b&scene=21#wechat_redirect>)

  * [获取pheatmap聚类后和标准化后的结果](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488610&idx=1&sn=3c0c0b5aeffae69f21835a1898a5ae43&scene=21#wechat_redirect>)

  * [增强火山图，要不要试一下？](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488657&idx=1&sn=bc38957415f509b75df0935033881238&scene=21#wechat_redirect>)

  * [一个震撼的交互型3D可视化R包 - 可直接转ggplot2图为3D](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488778&idx=1&sn=82886693cb545847c1d0d8c23e089890&scene=21#wechat_redirect>)

  * [赠你一只金色的眼 - 富集分析和表达数据可视化](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488810&idx=1&sn=a48aef2c5abc5c069e3bef1e3f26baa9&scene=21#wechat_redirect>)

  * [是Excel的图，不！是R的图](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488901&idx=1&sn=76f7388493a96e3caa0544f13c7d7ee6&scene=21#wechat_redirect>)

  * [道友，来Rstudio里面看动画了](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488969&idx=1&sn=f9e05ba6197ec378e347e40c15df8575&scene=21#wechat_redirect>)

  * [用了这么多年的PCA可视化竟然是错的！！！](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489137&idx=1&sn=330f6f206ac80fc0bcaa652dbe2dbf61&scene=21#wechat_redirect>)

  * [万能转换：R图和统计表转成发表级的Word、PPT、Excel、HTML、Latex、矢量图等](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489261&idx=1&sn=ece6af02b48c3414afcab894ce75a955&scene=21#wechat_redirect>)

  * [那天空飘过的梅花月饼，是今年中秋最好的礼物](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489359&idx=1&sn=a8f6614d19d050194408d7178640b687&scene=21#wechat_redirect>)

  * [2019年诺贝尔生理医学奖揭晓 |动图展示历年生理学奖](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489634&idx=1&sn=efc9c6ee656b74699a58435dddbc673d&scene=21#wechat_redirect>)

  * [2019年诺贝尔化学奖揭晓 |八一八，那些年的诺贝尔化学奖](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489659&idx=1&sn=533a2fc61015eae7f2605caeed1413d6&scene=21#wechat_redirect>)

  * [cellassign：用于肿瘤微环境分析的单细胞注释工具（9月Nature）](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489672&idx=1&sn=6407ad0e727f58f0f09edeb1bbbdd8d2&scene=21#wechat_redirect>)

  * [maftools|TCGA肿瘤突变数据的汇总，分析和可视化](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489795&idx=1&sn=6de6b4a25af46e88b0ac628e4a49c070&scene=21#wechat_redirect>)

  * [ggThemeAssist｜鼠标调整主题，并返回代码](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489799&idx=1&sn=06d091d42dcf611e58d8b11c4b8bd10b&scene=21#wechat_redirect>)

  * [ggcor |相关系数矩阵可视化](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489909&idx=1&sn=2ff50984152981605e999e818b2173b5&scene=21#wechat_redirect>)

  * [画图手册 | ImageGP：今天你“plot”了吗？](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489940&idx=1&sn=d50abfa41da8ccf73975ee7efca97426&scene=21#wechat_redirect>)

  * [R语言一键批量完成差异统计和可视化](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489984&idx=2&sn=bafb61bcd2a823be5e4b52c7033f2d8e&scene=21#wechat_redirect>)

  * [gggenes绘制多物种基因结构比较](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247489984&idx=1&sn=0fcc5ae0c4e59f29579cd0e344aaad22&scene=21#wechat_redirect>)

  * [数据可视化完美指南-R-python](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247490012&idx=1&sn=f24072367f1e0e589633d3bb33684f3c&scene=21#wechat_redirect>)

  * [如何使用AI画一个简单的细胞通路图?](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247490018&idx=2&sn=40cd1ce7c256bfb08cdb6b2095ae45ab&scene=21#wechat_redirect>)

  * [Pathview包：整合表达谱数据可视化KEGG通路](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247490244&idx=1&sn=e4fecfad6e7f17be8ca4d4fba8c201c9&scene=21#wechat_redirect>)

  * [Matplotlib绘制的27个常用图(附对应代码实现)](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247490282&idx=1&sn=97d960febe87cb7b86b47c09f21c8898&scene=21#wechat_redirect>)

  * [让你的单细胞数据动起来！|iCellR(一)](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247490302&idx=1&sn=e464ecad39b28ef2755b6687c4a58a1d&scene=21#wechat_redirect>)

## 高颜值免费在线绘图

![](https://mmbiz.qpic.cn/mmbiz_png/BA8CWhHQWPxx0RsLHiaGHiasjyaib7iaURiamrbxqlj1WDgzhVuXr9uejibyOfVhswplf5B3X8jJriaqDpjPVc5YaZ5Gg/640?wx_fmt=png)

### 往期精品

[画图三字经](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484523&idx=1&sn=34b595177cbe0fa8faf34d09d71ac8ec&scene=21#wechat_redirect>) [生信视频](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485004&idx=1&sn=5f9f7b2cb20a191be87c17ab9d9980e4&chksm=ec0dc3c6db7a4ad0718d640bce966f25aa23eee1648e87c784a183ba80a7f8419f32c538d3c1&scene=21#wechat_redirect>) [生信系列教程](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485155&idx=2&sn=73ffb2532846ca4b49bf0e74f11896ca&chksm=ec0dc369db7a4a7fc1494f739fe0a9f7c756d778a6b4d997ec7e385ff421f6f9894b761de95b&scene=21#wechat_redirect>)

[心得体会](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483927&idx=1&sn=23adf2b9d13400f2081f790e674e2cba&chksm=ec0dc79ddb7a4e8b5bb7a413744319a90f425371b30e2c85224b7c183cc4ad4bbd5d9749bb7b&scene=21#wechat_redirect>) TCGA[数据库](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484383&idx=1&sn=09c58de206f409fa375fb7af94d0084c&chksm=ec0dc655db7a4f438cb7e53f281cb5c6bf2484619b3c72d7eafe064ea6a342f69587353531af&scene=21#wechat_redirect>) [Linux](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484606&idx=1&sn=c5f2654e3ede87f534bc352f286a6357&chksm=ec0dc134db7a48228044e720eff4cc39ea2b9258db7d20faafbcae29a47ef7de334678fad35a&scene=21#wechat_redirect>) [Python](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247483866&idx=1&sn=310341a1c8d348958c304df03dfd06a0&chksm=ec0dc450db7a4d46e369637cd2867b0e56389bf4f2e1d0dce409bba38882e61e5063308a13af&scene=21#wechat_redirect>)

[高通量分析](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484034&idx=1&sn=e7680ee935f8603214227b37eeb2c567&chksm=ec0dc708db7a4e1eca4e38845381f328c49c84a90ad6580c3ba3761511772636e5ec0f185931&scene=21#wechat_redirect>) 免费[在线画图](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485097&idx=1&sn=b25732da52e95ba99cdbf77e1dc45191&chksm=ec0dc323db7a4a35a0b4eac9c865b70ebc7ed37c53e4bbe41194e241aa37344ddf2935df8a74&scene=21#wechat_redirect>) [测序历史](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485298&idx=1&sn=36c8024abb89fd5f408578af06ef4313&scene=21#wechat_redirect>) [超级增强子](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485257&idx=1&sn=02000c839eb023a9cb3c5ba07f7d0e4c&scene=21#wechat_redirect>)

生信学习[视频](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485237&idx=1&sn=33dba0d3ddf7cc71d319715722e36c14&scene=21#wechat_redirect>) [PPT](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485139&idx=1&sn=a9b45f10c8722e78e54bfdd93587dc72&scene=21#wechat_redirect>) [EXCEL](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485378&idx=1&sn=970e2a8cec0ee600d71eec2981d385aa&scene=21#wechat_redirect>) [文章写作](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484941&idx=1&sn=799b8a6376d2e17e24fd39d9fc10b3b3&scene=21#wechat_redirect>) [ggplot2](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486262&idx=1&sn=d38221a4063d866b1f10f4c9ebab5f88&chksm=ec0dcebcdb7a47aa03ff27872048304d33be27d1ab8bd3af0aefc320366a4bd3aceb943cb384&scene=21#wechat_redirect>)

[海哥组学](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485782&idx=1&sn=f9b05d0a6b22861a871e062688942b66&chksm=ec0dccdcdb7a45ca9414e53a8977ce834a1074f239885cf150a4a9f93d9a90880569350847da&scene=21#wechat_redirect>) [可视化套路](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485822&idx=1&sn=240cc5593ddc303d6c5d66edc7841033&chksm=ec0dccf4db7a45e24e0db1f84defc3924bc1728a9306e19b74e14e24f59082c4f081712f21d5&scene=21#wechat_redirect>) [基因组浏览器](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485735&idx=1&sn=be17e018bce29190832357c658bb4255&chksm=ec0dccaddb7a45bb37d80f74694dfd6ca8a006b33e16b8907a808204ff480dbdc045077d0ef4&scene=21#wechat_redirect>)

[色彩搭配](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247485182&idx=1&sn=7b5c1d800560eddcf898ed410720a2a3&scene=21#wechat_redirect>) [图形排版](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484492&idx=1&sn=10c9b2308065b6260cfc69ea9e8d065f&scene=21#wechat_redirect>) [互作网络](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247484964&idx=1&sn=32a1f7af15e8a28a224a52beef28ca59&scene=21#wechat_redirect>)

[自学生信](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247486486&idx=1&sn=32960c5a409236f7c808eb3d7e16ec4c&scene=21#wechat_redirect>) [2019影响因子](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488649&idx=1&sn=9a89cd65962c8f91185592255c1375bb&chksm=ec0dd103db7a5815dd5707930ee216daba2b98e924763968d659b22c92ad70cc8b78809794b4&scene=21#wechat_redirect>) [GSEA](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488643&idx=1&sn=2c038708fa553d8c2e085b29ab492987&chksm=ec0dd109db7a581f8710fc48d7b8e6e02846d813b95a808576aa59aa60ef14031f6ab5b6ec30&scene=21#wechat_redirect>) [单细胞](<http://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247488371&idx=2&sn=386cd4ab370eaf188c0da84d91348cd8&chksm=ec0dd6f9db7a5fefd6422dcc5e5a2c7c157970aa4b13da50e4d253d392eed9a6599266d1ae51&scene=21#wechat_redirect>)

后台回复“生信宝典福利第一波”或点击阅读原文获取教程合集

![](https://mmbiz.qpic.cn/mmbiz_png/BA8CWhHQWPyiayoLncWgUZsXIHJt4AM8L3MLmBP9IjfN6ic8iaIz2nFvhyEKG4gXXIiaL6ZKTKBvP3VFS1pKIXDKvw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/BA8CWhHQWPxSTEGicuu4HHziaYbSfFAGxwdqRPIL0tUN1n6mSEnxZ5ibmEzNNnt1C0FRZjJBiagEMaw4y8Mq84eicyw/640?wx_fmt=jpeg)

[](<https://mp.weixin.qq.com/s?__biz=MzI5MTcwNjA4NQ==&mid=2247490302&idx=1&sn=e464ecad39b28ef2755b6687c4a58a1d&scene=21#wechat_redirect>)
