---
title: "啥分(you)析(xi)做(wan)不了啊"
date: 2024-08-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520888&idx=2&sn=18746c66dc3bde17131dd819a26263bd&chksm=9b3ceb28ac4b623eda41c2cc6f6bc479b0f3c00b04376a4b3cbd28b653a0ffacf6ce4771807b#rd
albums: ["服务器"]
---

# 啥分(you)析(xi)做(wan)不了啊

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520888&idx=2&sn=18746c66dc3bde17131dd819a26263bd&chksm=9b3ceb28ac4b623eda41c2cc6f6bc479b0f3c00b04376a4b3cbd28b653a0ffacf6ce4771807b#rd
> 合集：服务器

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**一、写在前面**

人生苦短，为了加快我分析单细胞与空间转录组的速度(进可生信、AI，退可3A大作)，新配了一台工作站具体配置大家可以参考下面这张配置表和机箱照片。我这套配置的费用在**2w** +。当然大家有自己心仪的配置也可以找客服微信[**Biomamba_kefu**]配置。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzTtSagSa5PLhjIqf3hwSClm0pCiaoscRjsKtfZOXTGjYXslfAzrqCsLRyY5d1oyI6FntyUvrcicj9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzTtSagSa5PLhjIqf3hwSClJiahx2Ff1jtu77S0lbjOeicDf4D34XhMzMmQm5iagWH1BwavjNUAIM6nw/640?wx_fmt=jpeg&from=appmsg)

如果你的计算机不足以支持大规模的计算，且不希望花太多￥在买电脑上，可按需选用适合自己的计算资源：共享(经济实惠)：[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)独享(省电省心)：[生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508226&idx=1&sn=69e0eea720ac6aecc0362bcb9ac339ba&chksm=9b3cd852ac4b51445651a091be0fb6f638bd8cf5eb399af1c54804631fe3047706cf1d4044de&scene=21#wechat_redirect>)

[](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508226&idx=1&sn=69e0eea720ac6aecc0362bcb9ac339ba&chksm=9b3cd852ac4b51445651a091be0fb6f638bd8cf5eb399af1c54804631fe3047706cf1d4044de&scene=21#wechat_redirect>)实体(稳定高效)：[为实验室准备一份生物信息学不动产](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506028&idx=2&sn=3b479a92f0c6119c4584efbc23b8c32a&chksm=9b3ca13cac4b282a9ffe1fc4f4ab1a50b14688c6490f859ef714b84a755c286cb8a585054486&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

更多内容可咨询客服微信[**Biomamba_yunying**]

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**二、系统与配置选择**

系统方面，为了更好的兼容**WSL2** ，我选择了**Win11** ，另外我的Bios中还有一份**Ubuntu的双系统** 。CPU方面选的也比较有性价比(选次顶配就完事了)，i7-14700KF有**20核28线程** ，单线程的计算能力也十分在线，足够我们跑常见的生信流程。唯一比较遗憾的是这块CPU只支持**192GB的内存** ，而4*48GB的内存条是最**不具性价比** 的(如果可以我想把内存拉到384GB，省得在各个服务器之间东奔西走)。显卡方面，考虑到空间转录组和机器学习都会用到显存，因此我选择了**RTX3090**(除了专业炼丹的卡，普通民(you)用(xi)卡最大显存就是24GB的3090和4090，显然我没那么多预算，所以选由于功耗比一般不用于挖矿的前者)。其它比较重要的配置就是我选了2TB的固态+5TB的机械硬盘(单细胞原始数据一个样就一百G，这个容量不过分)。

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**三、工作环境配置**

说完系统和硬件，再记录一下我的环境配置过程吧，我安装了一些我日常工作需要用到的软件与环境，基本都是神器：

WSL2中的jupyter需要这么设置：

  *   *   *   *   *   *

```
# 通过配置文件设置运行端口cat  >> ~/.jupyter/jupyter_notebook_config.py << ENDc.NotebookApp.ip='0.0.0.0'  # 允许任何IP的远程连接c.NotebookApp.open_browser = Falsec.NotebookApp.port = 12345  # jupyter notebook 运行端口，根据实际情况设END
```

更多jupyter使用可见：[码Python神器：jupyter notebook](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499888&idx=1&sn=9b27a668e5b050952ee44a01074bac23&chksm=9b3cb920ac4b3036743dcad804419044ec2da5e8ec8cf7bd9b294be1095cdc25d2ce992fbd2e&scene=21#wechat_redirect>)

Rstudio:

安装以下内容，否则在装R包Cairo时会报错，影响R语言可视化功能的实现

  *

```
sudo apt install libcairo2-dev
```

接下来的安装步骤可参考：

[Rstudio-server的安装、配置、维护](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506225&idx=1&sn=d1d07b46f8bb9d80260224c9524124bb&chksm=9b3ca061ac4b2977ff1678ba31f093b61b47ba8d52efdf17f8777207f8126b1b3b4efdc7edc1&scene=21#wechat_redirect>)[如何连接终端和Rstudio-server](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506371&idx=2&sn=84c5999e37c8f411b13a2aac159649b8&chksm=9b3ca093ac4b29859fce5951ac87f34fbaaef16a5160c427f7d3c3dd06273d9741ee9fa157bc&scene=21#wechat_redirect>)[Rstudio常见使用技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504066&idx=1&sn=9201b659c63c4b428f175d8eb717be58&chksm=9b3ca992ac4b20845a31e70dab05268bd1f6b4d8c2414d03df0cb067e7378af07a84980077a4&scene=21#wechat_redirect>)

安装完毕后本地默认的IP和端口为：localhost:8787

另外还有一些windows下的软件，给大家放在百度云链接里了：

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpzTtSagSa5PLhjIqf3hwSClKquIk1K0wc29WcoibkEqz8wqcNUwBwiazqkI0HuDXEnibdkKgP0PvyOrA/640?wx_fmt=png&from=appmsg)

链接：https://pan.baidu.com/s/138hx1heu4yOc9ISPhUh4Nw?pwd=9i39

提取码：9i39

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyR2Ax0caS3FQIg2UThHW2F4aW2lMhUrK2uF0AcRclibia6j7NVmX5iaosWLz4hic3VIjFdHROA1ibG9OQ/640?wx_fmt=jpeg&from=appmsg)

finalshell不用多说，链接服务器敲代码/传输文件必备([生信分析为什么要使用服务器？](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=2&sn=c2ba75edc0382855cfc914c3bb713e7e&chksm=9b3caa9bac4b238d0690d2aa5a236c18c8ad8f0d7a23421eb63b5236ff1201c9ec99e12efc8f&scene=21#wechat_redirect>))；Everything就相当于windows的locate命令([Linux| 19.文件查找 find, locate, which](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497743&idx=1&sn=f8e9fda7d325262f129a80faf77217dd&chksm=9b3c815fac4b0849c12cfb926cef2eaed8e0c779cb50c92647c48230b99492dc12aed135e03f&scene=21#wechat_redirect>))找文件秒出；360压缩，windows中打包解包必备；QQPC电脑管家，没事可以给你清清文件查查配置，广告相对于竞品几乎是没有；谷歌浏览器几乎也是必备的；Bywave，魔法上网用的，翻github去外边学习必备，大家可以访问这个链接： https://user.by.ltd/aff.php?aff=23313；向日葵，用于远程控制电脑，出差党必备；有道云笔记，同样是出差党必备，能够帮助你随时随地获得自己的代码笔记([进来领有道云笔记会员](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485426&idx=2&sn=278de11dd3e99d2fb9ed336727af3df9&chksm=9b3f7ea2ac48f7b46d1cb9c43f063a39c39edce1c243863714f94fdd907eee04efcdb270f568&scene=21#wechat_redirect>))；AI不用多介绍，绘制流程图用得上；PS我一般用来把AI输出的PDF图片转为TIFF。

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507693&idx=1&sn=d9517a0803ad75cb7be430806834e7b8&chksm=9b3ca7bdac4b2eaba1ad01ed04ab1fbcbafcf4f6ddfe9e4f76ed9229707f545fe7d9c9ffd6ae&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（别问在么，添加时直接说来意）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)您点的每个赞和在看，我都认真当成了喜欢
