---
title: "《Nature Methods》: NiCheNet, 能够考虑到胞内转录调控的细胞通讯软件"
date: 2023-09-24
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503617&idx=1&sn=18389ffe1d201b1c0592ebc923aac851&chksm=9b3cb651ac4b3f4777cb0a6282ad99cd2aad711050d1590f20f970d843f05fb42f8cc02833e2#rd
albums: ["单细胞教程全收录", "文献速递"]
---

# 《Nature Methods》: NiCheNet, 能够考虑到胞内转录调控的细胞通讯软件

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503617&idx=1&sn=18389ffe1d201b1c0592ebc923aac851&chksm=9b3cb651ac4b3f4777cb0a6282ad99cd2aad711050d1590f20f970d843f05fb42f8cc02833e2#rd
> 合集：单细胞教程全收录 / 文献速递

**一、写在前面**

今天分享的这篇文献题为"NicheNet: modeling intercellular communication by linking ligands to target gene"，于2020年发表在《Nature Methods》上[1]，彼时细胞通讯的工具诸如CellChat、Italk、CellphonDB都已经问世，但像NicheNet这样在计算细胞通讯的同时还兼顾到胞内的**转录调控** 的软件还几乎不存在。时至今日，主流软件的思路依旧是评估胞外配受体的表达量是否存在关联。因此，NicheNet的出现打破了这一格局，为单细胞转录组测序中细胞通讯分析提供了新的方法。

**二、主要内容**

为了在细胞通讯计算时能够考虑到**胞内的转录调控** ，作者构建了**人类** 与**小鼠**(目前还不支持其它物种)的先验模型矩阵(Figure 1a)，收录了**配体→受体→转录调控→靶基因的完整通路信息**[2]。当然，这个**先验模型** 也经过了PPI、IPA等多种数据库的矫正与优化。因此NicheNet执行时第一步考虑的即为其它细胞中ligand的活性评估与排序，其次为受体细胞内部靶基因的**转录调控变化** ，而非像其它软件那样仅考虑**配受体** 的**互作** 关系。为了证明自己的模型有效，作者分别利用自己的先验模型与随机网络对配体活性、靶基因活性进行了AUROC评估，显然NicheNet的模型具有**最高的准确性**(Figure 1b-c)。与Ingenuity Pathway Analysis、CCCexploer等调控分析相比，NicheNet依旧在配体活性预测上拥有更好的表现(Figure 1d-f)。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpziaAtoFc7CiaflyiaQibkq4fiaL4UKRv7PvbVPgfFysXeJMfasFEsJicw7lVqZ1oyhNub6dHFfrsrL3KWA/640?wx_fmt=png)
与其它软件的构建过程一样，作者利用了一个cancer-associated fibroblasts (CAFs)用于软件效果的实测，目的为发现该数据原作者发现的partial epithelial-to-mesenchymal transition (p-EMT)相关的信号通路差异。首先作者利用NicheNet的pipeline获得了**配体活性**(Figure 2a)及其与每种配体调控的30种靶基因表达量间的**调控可能性**(Figure 2b)。而这些靶基因也的确随着pEMT score的变化而呈现出特定的差异，这些靶基因的大多数与p-EMT score呈正相关的关系(Figure 2c-d)。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpziaAtoFc7CiaflyiaQibkq4fiaLUkqPzvtGyMV6cPmDC1T9et1jvYjY2ReicGffBeLDkNegrVzkPSMXesQ/640?wx_fmt=png)
当然，该篇文章的内容与NicheNet的分析结果不止这些，该文的**Methods与补充材料**[3]具有极长的篇幅，适合做计算生物学或软件开发的人员细品。而我们后面将会给大家带来NicheNet的**实操教程** ~
参考：
[1]:Browaeys R, Saelens W, Saeys Y. NicheNet: modeling intercellular communication by linking ligands to target genes. Nat Methods. 2020 Feb;17(2):159-162. [2]:https://github.com/saeyslab/nichenetr[3]:https://static-content.springer.com/esm/art%3A10.1038%2Fs41592-019-0667-5/MediaObjects/41592_2019_667_MOESM1_ESM.pdf
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503225&idx=1&sn=d07afe8ff1787f6226c2d64cc72508f9&chksm=9b3cb429ac4b3d3f06513c5b7e3a5e03b6dc347c3e4edff0544225b57e7f98e8425dff5242f3&scene=21#wechat_redirect>))的**微信号[Biomamba_kefu]** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅，**备注来意会优先通过**)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
