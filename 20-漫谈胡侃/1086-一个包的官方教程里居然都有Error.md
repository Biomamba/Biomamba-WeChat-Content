---
title: "一个包的官方教程里居然都有Error"
date: 2026-02-08
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534978&idx=1&sn=fd5e5f25883faba6717bfeb2dc858b53&chksm=9b3c30d2ac4bb9c4d82d88b75764254152098fe99d1d5e90d61f33ac2d76586db36f1563b7cf#rd
albums: ["漫谈胡侃"]
---

# 一个包的官方教程里居然都有Error

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534978&idx=1&sn=fd5e5f25883faba6717bfeb2dc858b53&chksm=9b3c30d2ac4bb9c4d82d88b75764254152098fe99d1d5e90d61f33ac2d76586db36f1563b7cf#rd
> 合集：漫谈胡侃

相信各位和Biomamba一样，经常会有[糟糕的学习体验](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503524&idx=1&sn=e7afa36766a3a3504d084d3adad47459&scene=21#wechat_redirect>)，今天又踩雷了。contrastiveVI是一种生成模型，旨在从一组“目标”细胞（例如来自患有特定疾病的样本）中分离出特定的变异因素，与一组“背景”细胞（例如来自健康样本的细胞）中共享的变异因素区分开来[1]。本想着给大家做个教程，丰富一下生信基地的[python单细胞生态](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534702&idx=1&sn=f1531163f8f620b59cf63dfaa1c03e67&scene=21#wechat_redirect>)。谁曾想官方的实例中居然还包含error。作者都解决不了依赖关系，那我们读者不是更困难![](../../images/68bac71b484f05d6.png)。
![](../../images/ef0960891ba66c40.webp)

我当然可以一个个的查询每行命令无法运行的解决办法、解决各软件的版本依赖问题，只是这样有些索然无味。作者没有义务服务于用户，但对于我们来说，一个包的优秀程度不单限于其背后支撑的文章、强大的功能、计算性能，还在于它是否便于安装、是否有能让其他用户方便落地的教程。所以很遗憾，这个优秀的作品不能为我所用。我们在制作教程时也会留意大家是否能“跟着跑通”，因此我们做了几方面的努力：

1、用[Rmarkdown](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528272&idx=1&sn=e15d3d613cba725451ea8feade54de08&scene=21#wechat_redirect>)、[Jupyter](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531443&idx=3&sn=0930f54959a9bd13b99780d8f26a1155&scene=21#wechat_redirect>)等具有编译/标记功能的语法或者IDE去制作教程，而不是简单的往公众号里复制，确保每个教程至少在我们的手里可以跑通。

2、教程结尾都会附上版本环境信息与测试文件，例如[挑战用Python分析一百万个单细胞数据](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534670&idx=1&sn=7178b77f1efe4ca253f90b9121231204&scene=21#wechat_redirect>)的文末。甚至我们还做过[Biomamba的单细胞分析环境大公开！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529901&idx=1&sn=3e9cb1075a3b0b4c253ca19addf8b387&scene=21#wechat_redirect>)

![](../../images/f66f391f84674acb.png)3、针对[共计251小时视频教程，保姆级单细胞&空转教学](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534674&idx=2&sn=864480ec769a9932da5fdc7f20ee34ba&scene=21#wechat_redirect>)，我们还封装打包了镜像，能够做到[开箱即用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533721&idx=2&sn=ff2f23c988bb2e96038671f713f62807&scene=21#wechat_redirect>)，感兴趣的小伙伴可以联系我们领取。![](../../images/8be751ae0a95ac97.webp)![](../../images/6d70d03152b03a9e.webp)

[1]https://github.com/suinleelab/contrastiveVI

[2]https://colab.research.google.com/drive/1z0AcKQg7juArXGCx1XKj6skojWKRlDMC?usp=sharing

![图片](../../images/95968d673495ca4c.png)

**如何联系我们**

![图片](../../images/b36f05f29bee05ab.png)![图片](../../images/0667abfe3cfb054d.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/8fc0ebc5e462a3e8.webp)![图片](../../images/735cbbf3b51b2cbf.gif) 您点的每个赞和在看，我都认真当成了喜欢
