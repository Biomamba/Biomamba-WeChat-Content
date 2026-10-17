---
title: "尝试用字节的Traecode分析单细胞类器官数据，结果把电脑跑崩了。。。。"
date: 2026-09-05
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541665&idx=1&sn=4787aababe5ca9cd8e4ddd38e20d26e8&chksm=9b3c5af1ac4bd3e7cb3a2570b44d23148aa4bbc448169a23915fb52cbbdc7bd784344dd8aec2#rd
albums: ["单细胞教程全收录"]
---

# 尝试用字节的Traecode分析单细胞类器官数据，结果把电脑跑崩了。。。。

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541665&idx=1&sn=4787aababe5ca9cd8e4ddd38e20d26e8&chksm=9b3c5af1ac4bd3e7cb3a2570b44d23148aa4bbc448169a23915fb52cbbdc7bd784344dd8aec2#rd
> 合集：单细胞教程全收录

起因是[DS涨价](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541071&idx=1&sn=568a89e05cc332b242fbed2b8db928e8&scene=21#wechat_redirect>)实在肉疼，价格调整后费用指数级增长，开始找其它出路了。不过跑着跑着我的工作站就崩了，也不是Traecode的锅，还是[不推荐用自己的电脑做生信](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533659&idx=2&sn=8e7b9243228fa6531fb7549399f21d95&scene=21#wechat_redirect>)，记得考虑[足够支持你完成硕博生涯的共享服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540790&idx=2&sn=3e34a111e77e0cf29ee21b48a7940a9a&scene=21#wechat_redirect>)。![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkVVCDZ1g05ntexJzcBXMUFniaPlgHA585gIYZfqJ7fVK9bHeKuymY5TjW0iakic7vRnaicozIEYAAspic9uibaD3FnQGKZ5RJluM6ak/640?wx_fmt=png&from=appmsg)
这是个windows的IDE，下载安装步骤想必不用教了，值得一提的是，Traecode支持通过宇宙第一IDE——[Vs code](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528883&idx=2&sn=9d0b262d04667d22d97ff1583e136660&scene=21#wechat_redirect>)导入偏好设置![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkYGhEMGZiaUxoYettWPGLAumEbD25s6Uq8CnOuasVqq1mSruqgYNicT1qM9f6TpDELC2aXQqfmeEOa0haLOPWq1aiaibTAzTs85lM/640?wx_fmt=png&from=appmsg)

分为solo模式和IDE模式，前者就跟豆包对话APP类似，后者类似IDE可以管理项目和代码![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwniatB7qG6UlticHwY8s6aPCDEfDgCiaE5vDosvicMSJdHjmrdjW5aukkjZC5wdHaEFUOR86RibqwX9ia3CtzWcqsGCSJekTwqWR4kkM/640?wx_fmt=png&from=appmsg)

大家可以通过通过这个链接注册登录，新注册用户可一次性获得 5000 积分：

https://www.trae.cn/work-fission/JKENX6ND9MFN?utm_source=copy_link&utm_medium=friends_invite

难道说不能即时联网检索，是从语料库里扒的？其它数据都太老了，选个类器官吧

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlPNXbvffwZVuN5m5s9dmsXmM1JKwLuyFT1NtnF7jYLocUZBSmFTcF2ANp9Wy8wicMGic4HngZJOj1xmxiaf82lyBs9ybt6ZygRibg/640?wx_fmt=jpeg)

选python，效率高一些，毕竟是在工作站上跑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmVca20G5AOgT6pMAQNzMcIeu4OhlE2NvJeE2MuZTlwCTjtNuxN5ahRnicPRVclkqwusXSGqZVGFWQiafR2QHicQPdlIngicTbLorg/640?wx_fmt=png&from=appmsg)

自动执行：

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmaOgmEqoL0PNkkUg1cJriazMkgoeKftRCTDBJzL7dU4vWicicE0AtCd2Zia0q794OdEic3bQxj6ibkkkAnM4UO8fh0RuJ8ia3re39cZo/640?wx_fmt=png&from=appmsg)

用起来感觉像有IDE版本的claude，执行任务的途中还是会反复跟你确认一些基础命令。只不过从命令行换成了确认窗口。有没有用过的同学交流下如何能像claude一样绕过频繁的请求：[一招教你跳过Claude频繁请求确认，实测安全有效](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541434&idx=1&sn=17b7dd5922f5092d774a373f585dea8e&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwn8aNAPiaaGFOVoUMs3cHz6xOyUDA3AcphAkTCicrvd0gSyrd8EYET9wpyqJh0CasSmgQia5vVfZWvaq88tI8ia9icEgQMFhfnf1oS4/640?wx_fmt=png&from=appmsg)

缺少扩展也会提示你：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmIfsdjkpSMKic28pxdUjnUks6aAVhyOOvEq99Pv9XRlM7lFeCkHMZeQonBfmT14iboCAUllCBkUNicaEf7vZCpOEC2wNDsP9QhTU/640?wx_fmt=png&from=appmsg)

配置好环境后就可以自动在IDE里生成脚本、打开脚本到IDE(只是给你看)并且运后台行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlicqgfEz4WibwUHP3W9GkGs2DW0TPILc4dBia2BGVK0GBXYdfjIAyGotULJ3Zad49jtSgN5JWTViaABHsBicnyjL8v702OQQqXowtA/640?wx_fmt=png&from=appmsg)

然后我的电脑就死机了。。。重启后意识到我的电脑只有96GB内存，不敢太狂，还是让它监控下内存（[不推荐用自己的电脑做生信](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533659&idx=2&sn=8e7b9243228fa6531fb7549399f21d95&scene=21#wechat_redirect>)）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwm86XhmfJVRmhG4XibEMgGnCGRNS5lfwjSwIvYEJsC8icVVbZLVkRu22M5QSG59AV0eAFeOvD3ibJKXvBOq9yGGrnR895RBK9Ng5g/640?wx_fmt=png&from=appmsg)

随后开始监控内存并运行任务，任务结束后会提示我们进行审查

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmmibIPGYBzBCdpb3S8PgZmtYCmBWkZL6kv1tdypGwYJeEn7RayUPmfSZqhQeV5cWz5uwQLw1xPia4kU096NatXbjx7gG1tS2NZM/640?wx_fmt=png&from=appmsg)

AI比人还会偷懒，v1输出的图片完全就没有什么内容：

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmPCrfbJlhj0DsmS1fjEL3N5fgaibcGzgDHUFGMWQSSEPKuMWYqzwedgiaibGsRcIoW9nB0QqjiaLHHxHiaq9cPKyBtulfHRiafxUNR4/640?wx_fmt=png&from=appmsg)

果然，指望零交互完成这个分析还是比较困难的，下一个新指令强调下必须和原文一样：

  *   *

```
请你阅读原文，按照参考严格复现，你现在做的分析与原文完全不一致：Comparative analysis and refinement of human PSC-derived kidney organoid differentiation with single cell transcriptomics - PMC
```

给他出点难题吧，毕竟本地的内存不太够，不敢用R的[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&scene=21#wechat_redirect>)去挑战，python会节省一些内存，并且计算效率更高。这里选择用python环境的[scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)去对齐原文的参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlUh1GocAkDWzSKRszKgVPNqibWpgez99U9gdrCnWrJichm0pWiaclC0vg751dn9ic5CaPbwmN7HplKgkh4BsJMy1W2xnySKpdlE90/640?wx_fmt=png&from=appmsg)

好消息是它自动帮我解决了很多奔溃问题，但问题是我自己跑[python单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)的时候也没遇到过这么多bug呀

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnp2pZd4PeUgtK1VFliafLqhNx0ox3iaPJC9gCDVzCzkDNDhrq1Mzfx1pzDibjKmDahHxIwLTdwP6SKZDEibTkodiba4ruvreK1WvFk/640?wx_fmt=png&from=appmsg)

上述一共花了一千多积分吧，生成了新一轮的脚本和结果，总体细胞注释和marker结果可视化做的比较拉，肾小管和肾小球的细胞类型几乎无法区分，甚至注释的细胞类型还有概念上的混淆，应该是不能直接放在文章中了。

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkqaHy0bwVFdwUpn97kp4mibqqRh5Ila9TBic2zzs7QRgeggvSjheUbglfU2iaRW8XqFVPHG6Yu9hH1duBrNBtgCibEKMjkXjCBH2w/640?wx_fmt=png&from=appmsg)

给大家上传到百度云了：

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkiatp48R8ibonLxJaxTnW73JoPJ9yJCicD65Nu7r9W9pSraCBe9vlVh03JolJt5vMKDMccq4XFLLyxn5UZSWVSkiaYjpScdhXQPZI/640?wx_fmt=png&from=appmsg)

通过网盘分享的文件：Traecode分析单细胞类器官数据

链接: https://pan.baidu.com/s/1KShKyK_AHolniwfJuzNucA

提取码可联系客服微信Biomamba_zhushou获取

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/buxFNhaTGwkBoUtPWUWI7wx2zMRvZHJBvEia1ofRxTML4jKYgicb5YqSdarBgozxGjPsArd86NYKrusyG3nz2opXUw1Micicrt01LtsbOeCntGM/640?wx_fmt=jpeg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**欢迎交流**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家一起讨论。![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24)您点的每个赞和在看，我都认真当成了喜欢
