---
title: "珍爱生命，远离Excel"
date: 2022-03-18
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485346&idx=1&sn=ecd0a44225640f377a8b8bfc03facf31&chksm=9b3f7ef2ac48f7e4d486e8945b9c95f789706d1964d71fa49cac714dbc022f7c146250fcc4d9#rd
albums: ["漫谈胡侃"]
---

# 珍爱生命，远离Excel

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485346&idx=1&sn=ecd0a44225640f377a8b8bfc03facf31&chksm=9b3f7ef2ac48f7e4d486e8945b9c95f789706d1964d71fa49cac714dbc022f7c146250fcc4d9#rd
> 合集：漫谈胡侃

最近一直在从事线粒体相关的研究，从Mouse.mitoCarta数据库中下载了一个**excel** ，把GSVA和WGCNA分析了一通。本想着把这些基因都删除研究研究数据库外的基因，发现怎么也无法删除，定睛一看，原来数据之中包含**空格** 。要命的是，后续的GSVA居然都没有报错，并且成功的运行了下去。。。这就是Excel隐藏特殊字符带来的弊端，Linux里的cat -A才是照妖镜。

![](../../images/f92d0acbbd9053f4.png)

别给我律师函警告，Excel是个好东西，但是生信工作者应该远离。最经典的bug就是Excel中的一些基因名会被自动转换为日期：

![](../../images/6c1d30f60b56bcf2.png)

所以说，大家分析数据的时候，Excel能不用就不用，bug这种东西，只有你想不到，没有它做不到。不说了，我去返工了。

![](../../images/2cc9316bafeedaf7.png)

如何联系我们

![](../../images/9b3df9175ed77a7e.gif)最近发现后台中有一些消息我没能及时看到并答复，微信后台中超过48h后便不允许回复读者消息，这里还是再给大家留一下答疑的扣扣号，方便大家随时交流。微信号可以点击**喜欢作者** 后自动回复里有。欢迎大家向我咨询或者提供建议。大家可以阅读完这几篇之后添加我：[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484331&idx=1&sn=94ad9cabc39f13fabf08a31862373093&chksm=9b3f7afbac48f3edc011f3e587920da27e68f7870fcfd119a7269b7053662e8bc85941a58d0b&scene=21#wechat_redirect>)
[答疑公约](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=1&sn=9bae98ae031cc9e546c35c4d2e60efd1&chksm=9b3f7accac48f3da7c3ee8ed308de8e52aa92284f6985ba43b59b70b3610cecb01c7295f7521&scene=21#wechat_redirect>)
[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)

![](../../images/d3f344df2ff09261.webp)
