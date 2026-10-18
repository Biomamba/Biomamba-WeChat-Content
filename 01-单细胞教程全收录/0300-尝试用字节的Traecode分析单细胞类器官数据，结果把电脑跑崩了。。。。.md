---
title: "尝试用字节的Traecode分析单细胞类器官数据，结果把电脑跑崩了。。。。"
date: 2026-09-05
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541665&idx=1&sn=4787aababe5ca9cd8e4ddd38e20d26e8&chksm=9b3c5af1ac4bd3e7cb3a2570b44d23148aa4bbc448169a23915fb52cbbdc7bd784344dd8aec2#rd
albums: ["单细胞教程全收录"]
---

# 尝试用字节的Traecode分析单细胞类器官数据，结果把电脑跑崩了。。。。

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541665&idx=1&sn=4787aababe5ca9cd8e4ddd38e20d26e8&chksm=9b3c5af1ac4bd3e7cb3a2570b44d23148aa4bbc448169a23915fb52cbbdc7bd784344dd8aec2#rd
> 合集：单细胞教程全收录

起因是[DS涨价](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541071&idx=1&sn=568a89e05cc332b242fbed2b8db928e8&scene=21#wechat_redirect>)实在肉疼，价格调整后费用指数级增长，开始找其它出路了。不过跑着跑着我的工作站就崩了，也不是Traecode的锅，还是[不推荐用自己的电脑做生信](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533659&idx=2&sn=8e7b9243228fa6531fb7549399f21d95&scene=21#wechat_redirect>)，记得考虑[足够支持你完成硕博生涯的共享服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540790&idx=2&sn=3e34a111e77e0cf29ee21b48a7940a9a&scene=21#wechat_redirect>)。![](../../images/37b598ca89bfb680.png)
这是个windows的IDE，下载安装步骤想必不用教了，值得一提的是，Traecode支持通过宇宙第一IDE——[Vs code](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528883&idx=2&sn=9d0b262d04667d22d97ff1583e136660&scene=21#wechat_redirect>)导入偏好设置![](../../images/17feb373a1626689.png)

分为solo模式和IDE模式，前者就跟豆包对话APP类似，后者类似IDE可以管理项目和代码![](../../images/ecda75ae4b266e0e.webp)

大家可以通过通过这个链接注册登录，新注册用户可一次性获得 5000 积分：

https://www.trae.cn/work-fission/JKENX6ND9MFN?utm_source=copy_link&utm_medium=friends_invite

难道说不能即时联网检索，是从语料库里扒的？其它数据都太老了，选个类器官吧

![](../../images/8cf2565d0333a8cc.webp)

选python，效率高一些，毕竟是在工作站上跑

![](../../images/81a70c3a4e337b69.webp)

自动执行：

![](../../images/eae2d1852d1d0a8a.webp)

用起来感觉像有IDE版本的claude，执行任务的途中还是会反复跟你确认一些基础命令。只不过从命令行换成了确认窗口。有没有用过的同学交流下如何能像claude一样绕过频繁的请求：[一招教你跳过Claude频繁请求确认，实测安全有效](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541434&idx=1&sn=17b7dd5922f5092d774a373f585dea8e&scene=21#wechat_redirect>)

![](../../images/de316043bc085bd9.png)

缺少扩展也会提示你：

![](../../images/bae85f5a9f61ca39.png)

配置好环境后就可以自动在IDE里生成脚本、打开脚本到IDE(只是给你看)并且运后台行：

![](../../images/e2e2f1daafa831c0.webp)

然后我的电脑就死机了。。。重启后意识到我的电脑只有96GB内存，不敢太狂，还是让它监控下内存（[不推荐用自己的电脑做生信](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533659&idx=2&sn=8e7b9243228fa6531fb7549399f21d95&scene=21#wechat_redirect>)）

![](../../images/f9101c256c6dbb42.png)

随后开始监控内存并运行任务，任务结束后会提示我们进行审查

![](../../images/ad0dfaa6afc18ce1.webp)

AI比人还会偷懒，v1输出的图片完全就没有什么内容：

![](../../images/a56adccfe04a2047.webp)

果然，指望零交互完成这个分析还是比较困难的，下一个新指令强调下必须和原文一样：

  *   *

```
请你阅读原文，按照参考严格复现，你现在做的分析与原文完全不一致：Comparative analysis and refinement of human PSC-derived kidney organoid differentiation with single cell transcriptomics - PMC
```

给他出点难题吧，毕竟本地的内存不太够，不敢用R的[Seurat](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540715&idx=2&sn=3cd1ae2f3bb66978317dc04097eef826&scene=21#wechat_redirect>)去挑战，python会节省一些内存，并且计算效率更高。这里选择用python环境的[scanpy](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)去对齐原文的参数。

![](../../images/bad07dfefeea40d0.webp)

好消息是它自动帮我解决了很多奔溃问题，但问题是我自己跑[python单细胞](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)的时候也没遇到过这么多bug呀

![](../../images/0396b419913f5676.webp)

上述一共花了一千多积分吧，生成了新一轮的脚本和结果，总体细胞注释和marker结果可视化做的比较拉，肾小管和肾小球的细胞类型几乎无法区分，甚至注释的细胞类型还有概念上的混淆，应该是不能直接放在文章中了。

![](../../images/3b863b111ff29be0.webp)

给大家上传到百度云了：

![](../../images/c2d9c84d1c5d8cf4.png)

通过网盘分享的文件：Traecode分析单细胞类器官数据

链接: https://pan.baidu.com/s/1KShKyK_AHolniwfJuzNucA

提取码可联系客服微信Biomamba_zhushou获取

![](../../images/307da21250195105.webp)

![图片](../../images/2b97050f06208e7a.webp)

**欢迎交流**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家一起讨论。![图片](../../images/e43581b4f5118aad.webp)![图片](../../images/4ccf87cacd1143af.gif)您点的每个赞和在看，我都认真当成了喜欢
