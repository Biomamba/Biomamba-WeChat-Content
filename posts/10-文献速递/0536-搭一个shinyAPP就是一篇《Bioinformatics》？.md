---
title: "搭一个shinyAPP就是一篇《Bioinformatics》？"
date: 2023-04-14
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498668&idx=1&sn=0882e6eb06e6522208c8fedc705af342&chksm=9b3c82fcac4b0beaa34f62a4079c7a51cd98005badcaf699aacb6adb93ae45faa8f25d0bd033#rd
albums: ["文献速递"]
---

# 搭一个shinyAPP就是一篇《Bioinformatics》？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498668&idx=1&sn=0882e6eb06e6522208c8fedc705af342&chksm=9b3c82fcac4b0beaa34f62a4079c7a51cd98005badcaf699aacb6adb93ae45faa8f25d0bd033#rd
> 合集：文献速递

**写在前面**

原本想引用一番shiny，结果并没有检索出shiny研发团队所发表的论文，倒是有诸多**shiny爱好者** 搭建shinyApp所发表的文章。例如这篇题为“ShinyGO: a graphical gene-set enrichment tool for animals and plants”、于2020年发表于《Bioinformatics》上的文章[1]。其实本来想吐槽一番，这UI界面比我做的App还丑：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyQN56BBl3BnkFxiaGLLoKm7HC9rMib8Vibl16s79TF9xVKNRVk3w0zaTzzXgicEibUoo4qR3Oqaic1XACA/640?wx_fmt=png)
况且shiny团队都没有发过文章，仅以shinyApp为主题的文章未免。。。毕竟我也写过一些生信垃圾：
[给你安排一个懂生信的工具人（七）：在线版相关性分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484467&idx=1&sn=762ff5fbb54441633144ed6dead0b096&chksm=9b3f7d63ac48f475071fd62ae6a1c09a23da8036cc2cbd11e7740fdb9def79328e4eab45f4b1&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人（八）：不会有人真的只会做T检验吧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484505&idx=1&sn=762f80bd6840ec03d5151592679240f9&chksm=9b3f7d09ac48f41f4279fccefeb6e4ca15b6a9c9cdd9a00a0cc23c93174fa2db084032828a74&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（九）：在线PCA分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485571&idx=1&sn=a0497f79fe83ff6b86705f6eb0e1cbf9&chksm=9b3f71d3ac48f8c528efe63261858d1f6ef46acd4af49cc2da2a5b5e85c59ae020ad0ab06a4e&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人（十）：不学编程 零代码完成单细胞测序数据分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485730&idx=1&sn=42b9b35026bec5359ac34750dea3bf44&chksm=9b3f7072ac48f964970f673a86e27ecd453a80b953168dc110e0ea6bfa4110eeed3350c9601a&scene=21#wechat_redirect>)
[我把之前的在线工具都挪了个窝](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487051&idx=1&sn=c161c002171a61be28172e155c492cd7&chksm=9b3f771bac48fe0db73f68316bdda0a9ebc9fe9e10c867f540aba7b6ef3d1d86b2ab9e8dcbb9&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人（十一）：在线查询KEGG中通路与基因对应关系](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490119&idx=1&sn=f6f9a7f901c6fc1623552614d4ab8085&chksm=9b3f6317ac48ea01e67015d72a3079574b765889635cd6d5b99b5919a58935117a152a6fee5f&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人（十二）：KEGG通路、基因查询2.0](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490795&idx=1&sn=65dbe1a8e026466d0c5ce391c823c215&chksm=9b3f65bbac48ecad55381edd2f7221ccc910178c5c378877d49762e2e1606c02be407db61c98&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人|13. 火山图绘制2.0](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497142&idx=1&sn=a3dc3cac8845ae5013394f8407cf5725&chksm=9b3c8ce6ac4b05f071ba9d196b1d462edb610f4672bd5a7ad22cee339212375c215989fcb041&scene=21#wechat_redirect>)[给你安排一个懂生信的工具人|14. 富集分析App](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497621&idx=1&sn=cf1b6b70d60b3c406303b78086ac041f&chksm=9b3c8ec5ac4b07d318c0d8a2d486ee288799d5729eb1e2a8d0b8fcec396f90f0b8bb6809ad53&scene=21#wechat_redirect>)
[给你安排一个懂生信的工具人|15. 高阶韦恩图 UpSetR App](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497730&idx=1&sn=1b0a7b0235a5c23b1c357a73a4291f98&chksm=9b3c8152ac4b08447985b22d7589957416703a8ad2e545c6a05178a0da6c11f333c2944ef1c4&scene=21#wechat_redirect>)
但仔细一瞧，这篇文章发表在《Bioinformatics》上的原因是其**集天下之富集分析之大成** ，基本可以满足各位对富集分析的所有幻想。肝代码不易，**给作者点赞** ，值得诸位一试。

**ShinyGO**

作者整理了Ensembl、STRING-db、KEGG、NCBI、UniProt、Biocarta、REACTOME、MSigDB、GeneSetDB等大型数据库中的共59种植物、265种动物、115种弧菌与1678种细菌。其可以执行富集分析结果并完成可视化。相比于PlantGSEA这样专注于15种植物物种的富集分析来说，ShinyGO显然功能丰度的多。除了富集分析之外，ShinyGO还可以展示基因通路图、蛋白质互作网络图、基因共表达等可视化结果与基因类型、长度、GC含量、染色体分布等信息。页面功能多多，大家可以尽情探索：http://bioinformatics.sdstate.edu/go/。![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyQN56BBl3BnkFxiaGLLoKm7KB72eJic2zkjd8rxfgpd5vJiafMeytYd4M0sHHic8OO3hBCic6nrhPENBQ/640?wx_fmt=png)感兴趣的同学也可以学一学shiny：https://mastering-shiny.org/。欢迎大家带着自己的App来投稿，我可以给予大家一点我的愚见，并且将你的作品部署在我们的服务器中。
[1]Ge SX, Jung D, Yao R. ShinyGO: a graphical gene-set enrichment tool for animals and plants. Bioinformatics. 2020 Apr 15;36(8):2628-2629.
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器的**微信号** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpx6Htt0YEibg4Pn7N7fFUdclZQH9RX6YAUqQG98l3jcz9XjCiatucDpyE0o10sotnD7jiaEIFDOmv8Yw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
