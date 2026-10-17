---
title: "Claude code会话中断是可以重启的哦"
date: 2026-06-02
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538520&idx=2&sn=76e8ea7695a438c720723249dcefa0d1&chksm=9b3c2e08ac4ba71e99babd1cda2432b9c5e5ecdd2bdee396c8c4d5639bb1e3d9038074857ac5#rd
albums: ["AI时代，不用就会被淘汰"]
---

# Claude code会话中断是可以重启的哦

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247538520&idx=2&sn=76e8ea7695a438c720723249dcefa0d1&chksm=9b3c2e08ac4ba71e99babd1cda2432b9c5e5ecdd2bdee396c8c4d5639bb1e3d9038074857ac5#rd
> 合集：AI时代，不用就会被淘汰

由于要执行代码并不断交互，Claude code的实际运行时间一般会很长，这就不可避免地会遇到掉线地问题。好在Claude code是有进程记忆功能的。即使掉线或程序终止也不用担心，claude code有记忆系统(甚至可以在不同的会话中记录你的使用习惯，也可以在CLAUDE.md中输入一些全局的上下文)，可以直接输入claude --continue就可以恢复最近一次的claude会话。![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkeP7IYEM2KjQry6C5r4r7Vd1JI3eTJFyTmDuuS9MkPs991OozmR7IQNMzzyVrtb7MnBHqEtLsKZicHNB8q3hvWib47iaVBReJhQQ/640?wx_fmt=png&from=appmsg)
如果是你手动Ctrl+C终止了Claude，那么Claude会返回一个类似于上面截图的编号，那么你以下面的形式，就可以通过这个编号来重启claude对话：

  *

```
claude --resume 编号
```

当然，[程序可以自己跑的，不用盯着，你也可以通过](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511096&idx=1&sn=14191291fa6fbdb625b9601d230509f7&scene=21#wechat_redirect>)[利用Tmux高效管理终端会话](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528249&idx=2&sn=a3603d5ef77ae9aceb181e59d8b067ff&scene=21#wechat_redirect>)[来防止掉线。](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511096&idx=1&sn=14191291fa6fbdb625b9601d230509f7&scene=21#wechat_redirect>)
Claude code还有以下快捷键，感兴趣的同学可以试一试：![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnhU4dC8Nz3OOtzHWfC2HKmv8JgSg7Q2H5KmLibibndQHkib00FibFicfDchJon6nfl7Jo3vg6fC8KRGBDJormrwb8epZxmINPcfHcg/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=35)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24) 您点的每个赞和在看，我都认真当成了喜欢
