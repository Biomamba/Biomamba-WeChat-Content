---
title: "答读者问 （十三）查看Seurat对象时的ERROR：type='text'"
date: 2022-04-18
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73#rd
albums: ["单细胞教程全收录", "答读者问"]
---

# 答读者问 （十三）查看Seurat对象时的ERROR：type='text'

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73#rd
> 合集：单细胞教程全收录 / 答读者问

往期回顾

[答读者问 （一）单基因究竟能否进行GSEA](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484175&idx=1&sn=3e45ad62b045a541874e5ae7ca03f849&chksm=9b3f7a5fac48f349f8893500825d2c6b4ff581fbb0816c1074d88a0dbbb4a612c1e1bb3740bb&scene=21#wechat_redirect>)

[答读者问 （二）为什么我的PCA分析报错了？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484248&idx=1&sn=b1fe7174a28562d01422e43609f41709&chksm=9b3f7a08ac48f31e3bbfdb4a9824dadf25a8fa3ff9b78dd15d646ae4c3da5db04e2e4acfba3d&scene=21#wechat_redirect>)

[答读者问 （三）单细胞测序前景](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484280&idx=2&sn=844af02070012a1c2681880596ba51a2&chksm=9b3f7a28ac48f33e95eb906121be8953410ca4c572c8035cb801609a56caf9dcff57fa989602&scene=21#wechat_redirect>)

[答读者问 （四）如何分析细胞亚群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=2&sn=e8d02fddc80d1137bb64c55541f1651d&chksm=9b3f7accac48f3da7df7fcad9c996291bc66967c04d16dde92ed391c56e610a7298ac8fb7dbb&scene=21#wechat_redirect>)

[答读者问 （五）如何实现各物种基因的ID/symbol的转换](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484353&idx=2&sn=8fccb88c871a42c803e313be157ab293&chksm=9b3f7a91ac48f387df8b462f7318596fc5c645d6f05eefac2c598ff6875c0a2eeb902aaf5a15&scene=21#wechat_redirect>)

[答读者问 （六）Seurat中如何让细胞听你指挥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484376&idx=2&sn=9fda8a5261e86f889a58d607163ce0fd&chksm=9b3f7a88ac48f39ea9c19e256a513c9ae80c6f6dc1724b7783884e23981e2061c78fa67071c9&scene=21#wechat_redirect>)

[答读者问 （七）有人问我Biomamba何解](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484550&idx=1&sn=ec4466084c1c9eba7eb292e95f33b5bb&chksm=9b3f7dd6ac48f4c042b4e9df2abd717b1354b4914c3f7510eaf444e97965a0f6622979e710e0&scene=21#wechat_redirect>)

[答读者问 （八）为什么Read10X也会报错?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485012&idx=1&sn=6007c8d7cb2a236dd7240a678dac0391&chksm=9b3f7f04ac48f612f811c1df9e9450dc8112d343e4bf245be5149c2e2a073d3e339cd0e3ff61&scene=21#wechat_redirect>)

[答读者问 （九） 如何将数百个文件整合为一个矩阵](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485032&idx=1&sn=7d4777589fa1f92d26ad05ffe3e02f6a&chksm=9b3f7f38ac48f62e0d2e4d46a13c21e440295aef4cba08214527d7b7d2e1959a0b4cebe4143a&scene=21#wechat_redirect>)

[答读者问 （十）整合后的表达矩阵，如何拆分出分组信息？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485134&idx=1&sn=13f5f8c47d8af2beeca4e103a5f5e26d&chksm=9b3f7f9eac48f688b454a1062ee4e41f7072ac9d58e5466fa7ed4bb05018adbfe167bb3a445a&scene=21#wechat_redirect>)

[答读者问 （十一）如何一次性读取一个目录下的cellranger输出文件？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)

[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485145&idx=1&sn=402cb28c16aba0dc647037c9b7aba8f7&chksm=9b3f7f89ac48f69fe27cd427df3eff2e88c240bf20dfe92d8b522eecd7302d132d880bf29047&scene=21#wechat_redirect>)[答读者问 （十二）ERROR: have no zero exit status](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485290&idx=1&sn=1e77059439342374ea03496cbba08070&chksm=9b3f7e3aac48f72ca08f5e73496e6f8c99c5fd74a39daa626d636ba5a7b0b89873437ebcb6d4&scene=21#wechat_redirect>)

问题

我们在“[手把手教你做单细胞测序数据分析（二）——各类输入文件读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484086&idx=1&sn=7346a09ba350d6fb7c806dcb7509a1ef&chksm=9b3f7be6ac48f2f02cb948140381ad2a0e3818cc0eefc53cb7a1ad7459aacdc1e90a1ce0af8b&scene=21#wechat_redirect>)”的文末教过大家如何查看Seurat对象的数据结构，后台中运行最后一行时经常有粉丝报错，集中回答一下。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw3HuwliaGv5qG9MBmltQyjmbiaTQcU3icKRnT1fYIg8L5V3toLiblyj0Oj9u2RoKUbjgybzgQrYsmAPw/640?wx_fmt=png)

怎么解决问题

这个问题发生的根本原因在于mm函数所在的**mindr包** 更新了，在1.2.3版本（左图）中mm中是存在type参数的，而在1.3.3中type函数被拆解为了input_type和output_type（实际上原来的type对应这里的input_type），并且参数的选项也有所更新，很遗憾'text'这一选项不存在了，而更新后的几个选项（"auto", "markdown", "mindmap", "R", "dir"）我也都替大家尝试过了，并不能成功运行。
```
  ,
```

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw3HuwliaGv5qG9MBmltQyjmMSl2gGyZCmuHWgdLd9AmcibEkEbyGCYSumSZ8FJoic272A0kQshiaMq8Q/640?wx_fmt=png) ![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw3HuwliaGv5qG9MBmltQyjmjLxo6S1fEMicJcVXQRAW0ljsBLhvKx9VWl6tIWgyXqDKklBYhAUn4hQ/640?wx_fmt=png)

显然，用新的版本已经无法解决这个问题了，只能按下面的代码下载老版本了。

  *   *   *   *   *   *

```
remove.packages('mindr')#先把原来的卸了require(devtools)install_version("mindr", version = "1.2.3",repos = "http://cran.us.r-project.org")#安装更早的版本packageVersion('mindr')#安装后检查一下版本
```

此外，我也把这个函数生成的文件存成html，需要的同学可以从百度云链接中下载。

链接：https://pan.baidu.com/s/1iMK3xlVU-LQhrOan_qpefQ?pwd=uo8l

提取码：uo8l

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw3HuwliaGv5qG9MBmltQyjmceicufuDfuTIO2ib2kJMTOT7cQZ6FHcyN9EticHAuWfibicGoAzeicvWcB8w/640?wx_fmt=png)

其实R语言中报错的根本原因无非就两种：版本和数据格式。大家只要检查好这两点，很难遇到报错。几乎每次教程的底部我都会附上我所用R包的版本，最好还是保证版本与我一致，避免不必要的麻烦，毕竟代码在我这都是可以跑通的，一些你们遇到的报错我也不曾遇到过（基础报错除外）。除了按照上述的方法去一一安装与我相同的版本，以下还有两种方案供大家选择：
1、超过600种的常用生物信息学package我已经在R3.6、R4.0、R4.1中给大家安装好了，可以直接加载，有需要的同学请自取：[给你安排一个懂生信的工具人（六）：再也不怕装不上packages了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485571&idx=2&sn=1cd39234ea92565fc457c2ec0ab7e9d0&chksm=9b3f71d3ac48f8c5bf3ce59816db1bd8351f37ce3bb3646a12469505486c525d6ae2992ab36a&scene=21#wechat_redirect>)
2、以后的教程都会在西柚云中演示，给你们申请到了免费的版本，大家可以去用免费版跟着学：[给你们申请到了免费的128GB云服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485734&idx=1&sn=32c75f6d07b49084e518af6d18099e8b&chksm=9b3f7076ac48f9600593b319d2e0b36bf5a62399a9835caa5783ad36fbdec6004e04cb656db9&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpw3HuwliaGv5qG9MBmltQyjm7tvC33w1f3cApYd7X4QXSZ01xWAoAibz25ht7hiaFGdOL3XDlerUKmXw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif)最近发现后台中有一些消息我没能及时看到并答复，微信后台中超过48h后便不允许回复读者消息，这里还是再给大家留一下答疑的客服号，方便大家随时交流。微信号可以点击**喜欢作者** 后自动回复里有。欢迎大家向我咨询或者提供建议。大家可以阅读完这几篇之后添加我：[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484331&idx=1&sn=94ad9cabc39f13fabf08a31862373093&chksm=9b3f7afbac48f3edc011f3e587920da27e68f7870fcfd119a7269b7053662e8bc85941a58d0b&scene=21#wechat_redirect>)
[答疑公约](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=1&sn=9bae98ae031cc9e546c35c4d2e60efd1&chksm=9b3f7accac48f3da7c3ee8ed308de8e52aa92284f6985ba43b59b70b3610cecb01c7295f7521&scene=21#wechat_redirect>)
[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)
