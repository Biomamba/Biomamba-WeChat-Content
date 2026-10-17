---
title: "给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析： Loupe Browser"
date: 2022-04-10
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a#rd
albums: ["单细胞教程全收录"]
---

# 给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析： Loupe Browser

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a#rd
> 合集：单细胞教程全收录

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

往期回顾

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQLiacep1yYD3gtbQrf2SxSiaKTic4fvApxf7HlVskaU0tGia7VJfKuc7kbw/640?wx_fmt=png)

[给你安排一个懂生信的工具人（一）：火山图](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484153&idx=1&sn=68ce6d3499ff7c13fed387bea4fff5a9&chksm=9b3f7ba9ac48f2bfe5ba3e30bca7709e41c2c0f111b9dbfaf703f83d03f107b8589adb1e7792&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（二）：真-工具人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484166&idx=1&sn=7fcaa65879a9ad9564c47ebf4dbbff4d&chksm=9b3f7a56ac48f340e4891de4d911c3776170725abe2900d846d3c94f379605b03b1ec8d23dbe&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人（三）：凌波微课开发的在线版metacoder](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484237&idx=1&sn=e1873cc52566f8002b827568dff99b35&chksm=9b3f7a1dac48f30b533ea87a8e800f6cb77606ace1da700a4324c8c888b0e102d01a20039870&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人（四）：ggplot2"作弊器"](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484259&idx=1&sn=7c6498b0d69e7e7a492014e22c02abba&chksm=9b3f7a33ac48f3254ae190904dbf6798bda1b8fc3a10cd5a72f41543fdf1f89dc4b0a9697f7b&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（五）：手把手教你用在线 pheatmap 绘制热图](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484391&idx=1&sn=6f4369bbb231d946dcb63b399ffe4bfd&chksm=9b3f7ab7ac48f3a1a88a92c03be88e25cf57373f1099961ff1f01ad48faf8d8b94538b3cdd32&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（六）：再也不怕装不上packages了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484429&idx=2&sn=da45138ab6e68e29d373670afe5737a4&chksm=9b3f7d5dac48f44b420c0b940e835996b8d2f4429397a61ae8a5fd4fa1a86cd974f260a360d0&scene=21#wechat_redirect>)

[给你安排一个懂生信的工具人（七）：在线版相关性分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484467&idx=1&sn=762ff5fbb54441633144ed6dead0b096&chksm=9b3f7d63ac48f475071fd62ae6a1c09a23da8036cc2cbd11e7740fdb9def79328e4eab45f4b1&scene=21#wechat_redirect>)

[给你安排一个懂生信的工具人（八）：不会有人真的只会做T检验吧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484505&idx=1&sn=762f80bd6840ec03d5151592679240f9&chksm=9b3f7d09ac48f41f4279fccefeb6e4ca15b6a9c9cdd9a00a0cc23c93174fa2db084032828a74&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（九）：在线PCA分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485571&idx=1&sn=a0497f79fe83ff6b86705f6eb0e1cbf9&chksm=9b3f71d3ac48f8c528efe63261858d1f6ef46acd4af49cc2da2a5b5e85c59ae020ad0ab06a4e&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)“给你安排一个懂生信的工具人”这个系列我们一直致力于给大家**制作** 或分享一些**去代码化的生信工具** ，以方便非生信专业的科研人员将科研时间集中花费在生物学问题上。学习的同时也欢迎大家关注公众号“Biomamba 生信基地”：
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

视频教程

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

教程一共6讲，由**华大基因** 制作，大家跟着B站内的视频看吧：

https://www.bilibili.com/video/BV1MS4y127TV/

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxo7020KVvLWWZICb2NZiaEj889B4iajyVzGnBLeb46tz5EZYpjen1Vz8NCzNQeaw37LNt1RIYH2cqA/640?wx_fmt=png)

总体来说，loupe broswer可以完成几乎所有的单细胞测序**基础分析** 的操作，但是更多进阶的操作还是需要大家有些代码功底自行分析。对于代码学习欲望低、**希望快速上手** 、短期内简单分析数据的人群来说，loupe broswer是最佳选择。当然，看完视频有不明白的问题也别问我，我没用过这个😂。

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif)最近发现后台中有一些消息我没能及时看到并答复，微信后台中超过48h后便不允许回复读者消息，这里还是再给大家留一下答疑的客服号，方便大家随时交流。微信号可以点击**喜欢作者** 后自动回复里有。欢迎大家向我咨询或者提供建议。大家可以阅读完这几篇之后添加我：[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484331&idx=1&sn=94ad9cabc39f13fabf08a31862373093&chksm=9b3f7afbac48f3edc011f3e587920da27e68f7870fcfd119a7269b7053662e8bc85941a58d0b&scene=21#wechat_redirect>)
[答疑公约](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484316&idx=1&sn=9bae98ae031cc9e546c35c4d2e60efd1&chksm=9b3f7accac48f3da7c3ee8ed308de8e52aa92284f6985ba43b59b70b3610cecb01c7295f7521&scene=21#wechat_redirect>)
[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)
