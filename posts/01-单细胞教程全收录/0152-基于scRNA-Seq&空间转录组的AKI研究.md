---
title: "基于scRNA-Seq&空间转录组的AKI研究"
date: 2023-09-27
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503664&idx=1&sn=39519d9cfa54e2d5b757f6c249ccbc86&chksm=9b3cb660ac4b3f768c8cfb708d8355c426b2d4ad39538acd5584aa9741ccdf1076b7112492df#rd
albums: ["单细胞教程全收录", "空间转录组", "文献速递"]
---

# 基于scRNA-Seq&空间转录组的AKI研究

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503664&idx=1&sn=39519d9cfa54e2d5b757f6c249ccbc86&chksm=9b3cb660ac4b3f768c8cfb708d8355c426b2d4ad39538acd5584aa9741ccdf1076b7112492df#rd
> 合集：单细胞教程全收录 / 空间转录组 / 文献速递

**一、写在前面**

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwqtuwUnAm4tv0c12m7ZW8q6BfWJFkvu4uI9mEEqLxcAPBYBK5ytO9guyTonaanFWVVUuLjf49r5Q/640?wx_fmt=png)

**单细胞测序** 已经被广泛的应用于各类生物、医学研究之中，长期以来，由于其在解离建库过程中**丢失空间信息** 的特性，从而造成对临近细胞通讯、基因区域表达模式识别的不足，但**空间转录组** 的问世让这些问题迎刃而解。本次介绍的文章题为"Spatially Resolved Transcriptomic Analysis of Acute Kidney Injury in a Female Murine Model"，于2021年11月发表在《JOURNAL OF THE AMERICAN SOCIETY OF NEPHROLOGY》上(**IF=10.1**)，算是比较早期的空转作品。基于10X Genomics的**Visium** 空间转录组技术，揭示了小鼠在急性肾损伤(Acute Kidney Injury, AKI)损伤与恢复过程中的细胞互作动态过程。有趣的是，考虑到**雄鼠与雌鼠在肾损伤方面的敏感性有差异** ，作者还做了一个雌雄对立对比的part。结合scRNA-Seq的联合分析，作者最终揭示了AKI进程中巨噬细胞与淋巴细胞的参与过程。另外，作者还将这个数据以可视化的形式布置在了网页中，网址为：http://humphreyslab.com/SingleCell/(感觉现在搭一个网页是生信文章的传统艺能了，比如这一篇:[scRNA&DKD](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247489823&idx=1&sn=6a5dddd53870395316d2b2e904c6ce72&chksm=9b3f604fac48e959e97e4b0317643efdcf117da7f8b75f1edbcd64dd8e2f07149e6031a94dd4&scene=21#wechat_redirect>))。值得注意的是，这篇文章的发表形式为RAPID COMMUNICATIONS，并不是Article，这意味着文章的篇幅有限，分析内容也较少，给各位留下了广阔的数据挖掘空间。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwqtuwUnAm4tv0c12m7ZW8qZPUmBXtG6BOG5Z968hdcFgMiaLOh98HhPu7qK4dURRYWCrrfYN4VfEQ/640?wx_fmt=png)

交互工具网址

**二、主要结果**

首先，作者对小鼠进行了AKI模型的构建，分别对雌性小鼠进行34分钟、对雄性小鼠进行22分钟双侧肾缺血操作(Figure 1A)，并收集4h、12h、2d、6w的血浆用于BUN与肌酐的测定。显然，BUN在AKI模型构建后明显上升(4h~2d)，在恢复期后明显回落(6w)；肌酐水平则在12h时明显上升。根据GFR的测定结果，可初步判断雌性小鼠的**34分钟** 造模效果约等于对雄性小鼠进行**22分钟** 的造模(Figure 1D)。对于Havcr1、Lcn2这两种肾脏损伤因子的水平而言，含量曲线与BUN基本一致(Figure 1E)。即，AKI损伤与恢复模型构建成功！

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwqtuwUnAm4tv0c12m7ZW8qlzm1jbbZr7bPgAOnm71dAsINBMR4UicGQtM4TKgPypa74rCWZ8KricMg/640?wx_fmt=png)

Figure 1

由于10X Visium的分辨率水平相对较低，在没有scRNA-Seq数据的辅助下，很难获得细胞类型的注释。作者首先查看了空转数据中**皮质(Lrp2)、髓质(Aqp2)、肾小球(Nphs1)** 的分布情况(Figure 2A)，并通过**免疫荧光** 加以验证(Figure 2B)。由于大部分肾脏疾病的研究都是基于雄性，因此作者对比了雌性模型动物与雄性模型动物间的基因表达特征，发现Cyp7b1、Cyp4a14、Slco1a6存在明显的性别差异(Figure 2D)。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwqtuwUnAm4tv0c12m7ZW8qZUl4acAzy5zYCdebdVBqFScicqzkhWU8xuowUBGhDxJ4ovnLAHib59Zw/640?wx_fmt=png)

Figure 2

考虑到10X Visium每个spot的直径为**55 μm** ，算上每个spot之间还有一些距离，实际上每个spot反应出的信息可能包含**10~50个细胞** 。因此作者通过Giotto(浅记一下，后续我们出个教程)及前期研究获得的个细胞类型marker的list利用PAGE富集对scRNA-Seq数据和空转数据进行整合，对Spot进行了Pod、PTs1、PTs2、TL、CNT、TAL的分值评估。值得一提地是，在这一步里作者同样将**雄性与雌性分开分析** 。利用Leiden clustering，作者最终获得了细胞大类的注释(Figure 3A)。在AKI进程与恢复过程中，许多基因发生了特定模式的变化，例如与近曲小关相关的基因Aadat在AKI进程中快速下调而在恢复过程中上调。而肾脏损伤marker Lcn2则在AKI进程的髓质中快速上调(Figure 3C)，而在皮质中上调趋势较为缓和。Cryab的趋势与Lcn2类似。Cfh这种具有肾脏保护作用的基因则在2d与6w中表达明显上升，可能与**防止AKI转向CKD** 的过程有关。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwqtuwUnAm4tv0c12m7ZW8qu1ia0xzcYt2aZ3LoKQib0k41viboOyiboLzSpSHIiaaiaoMXb2CBJZ0nzKzA/640?wx_fmt=png)

**Figure 3**

此后，作者利用SPOTlight对每个**spot当中占据的具体细胞类型比例**(共26种细胞类型)进行了预测(Figure 4A)，用于后续的细胞通讯计算。可以明显发现的是受损的近曲小管细胞(InjPT)在12h、2d、6w时与**T Cell** 具有强烈的**互作关系**(Figure 4B)。并且巨噬细胞的Marker F4/80与肾脏损伤因子Kim-1具有一定程度的共表达关系(Figure 4D)。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwqtuwUnAm4tv0c12m7ZW8qnMhUgIUcZ5P6k11PlRJrKv3XoIFEVybbMDeUZoqwZvz90d718ew4og/640?wx_fmt=png)**Figure 4**

**最后聊聊**

这篇文章总体来说比较简单，可能是限于RAPID COMMUNICATIONS文体的篇幅。但手术造模(Bilateral IRI)、生物检定(BUN、肌酐、GFR)、QPCR、免疫荧光、scRNA-Seq与空转是一个没落。总体来说这是一篇非常干练的文章，想要入门空转的同学可以阅读一下原文。后续我们也会出一些空转数据的分析教程。

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息更新不及时，超过48h便不许回复读者消息，这里给大家留一下领取资料及免费服务器([有root权限的共享服务器,注册即送200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499707&idx=1&sn=1b1bb35069f6a86e50bc0866a22502b7&chksm=9b3c86ebac4b0ffd55d3cd9d8247eab6110481f1bf53e7fede84c0db29366910df8bd79dcc41&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
