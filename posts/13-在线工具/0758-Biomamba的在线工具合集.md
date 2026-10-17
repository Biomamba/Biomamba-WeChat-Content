---
title: "Biomamba的在线工具合集"
date: 2023-10-29
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504403&idx=1&sn=43e081157d0f6623955a19f691f679ac&chksm=9b3cab43ac4b2255af9cf7e0e3f2c97f8d28b5bb7dca82c99822046015d6556dd1cf127ce358#rd
albums: ["在线工具"]
---

# Biomamba的在线工具合集

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504403&idx=1&sn=43e081157d0f6623955a19f691f679ac&chksm=9b3cab43ac4b2255af9cf7e0e3f2c97f8d28b5bb7dca82c99822046015d6556dd1cf127ce358#rd
> 合集：在线工具

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

前言

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

之前的推送中发布过一些简单的在线小工具，此前都是把APP直接部署在shinyapps.io里，一方面shinyapps.io挂在墙外，导致大家的访问速度很慢；另一方面shinyapps.io有上传文件大小的限制，很多粉丝都反映自己的数据超标了；再者shinyapps.io有发布数量的限制，目前我的额度已经用完。并且shinyapps.io基本不支持中文，之前发布的工具也都是通过英文界面实现的。束缚过多，索性就配置了一台服务器([有root权限的共享服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>))装在shiny-server里，上述的缺点也就不存在了。以后访问速度和数量就都不限制啦，当然大家也别拿几十G的数据来我这跑，谁给我跑崩了我以后可就要限流了![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpyUNnHOn8es4zIE8EU8PJ0wDOicyxX7LyO6jZ16Stg9bTOc5tiaCZjncbgsCTkrq08kLcWTvH0l2a4w/640?wx_fmt=png)。所以更推荐大家下载百度云的打包软件在本地电脑上运行。

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

1、在线相关性分析

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)推送/教程：
[给你安排一个懂生信的工具人（七）：在线版相关性分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484467&idx=1&sn=762ff5fbb54441633144ed6dead0b096&chksm=9b3f7d63ac48f475071fd62ae6a1c09a23da8036cc2cbd11e7740fdb9def79328e4eab45f4b1&scene=21#wechat_redirect>)
视频教学：

csv文件准备，表头需要为![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpywyyFIVR5bTsyUnFJa0t9XAZ9XQcDLZxXoibycYmz7jibDicnibgE5ibIy29heqicaOBXrqIYKDmWQuj8Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

App新网址：http://xiyoucloud.22ip.net:34038/ggcorrplot.chinese/

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

2、富集分析App

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

富集分析可以说是生物信息学中最常用的分析之一，可以帮助大家判断自己所感兴趣基因集的生物学意义。这里我制作了一个App，可以支持KEGG、GO、Wiki、Reactome、Disease ontology数据库的富集分析。大家如果对界面/功能有任何修改的想法，欢迎联系我们。

在线版链接：

http://biomamba.com:34038/enrichment.App/

本地exe程序版下载链接：

链接：https://pan.baidu.com/s/1BZE99nmAeo0Wq9_eHhnjbg?pwd=e60t

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyBw0bDbfyYb8MJUHjKRropItoTrX02ObmU6s9iaMabNVBE1ANgP5gBx8lJsQjFuJGPkkdTEteNM5w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

具体使用起来很简单，本地版打开exe文件后与在线版同理:

B站同步播出，欢迎来三联:

https://www.bilibili.com/video/BV1334y197Pw?p=9

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

3、在线火山图

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

这里我重新写了一个App([ 火山图绘制2.0](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497142&idx=1&sn=a3dc3cac8845ae5013394f8407cf5725&chksm=9b3c8ce6ac4b05f071ba9d196b1d462edb610f4672bd5a7ad22cee339212375c215989fcb041&scene=21#wechat_redirect>))，大家如果对界面/功能有任何修改的想法，欢迎联系我们。

在线版链接：

http://biomamba.com:34038/vocalnoplot2.0/

本地exe程序版下载链接：

https://pan.baidu.com/s/1dshXmiP8Xa-D2cw5TMWx6Q?pwd=ji9k

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpywyyFIVR5bTsyUnFJa0t9XP9NECx6icicWcYsZVCicxpTEbPXdsjOIcIBSmXpa2OyNARib0Vk2pHib9Xw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

具体使用起来很简单，本地版打开exe文件后与在线版同理:

B站同步播出，欢迎来三联:

https://www.bilibili.com/video/BV1334y197Pw?p=8

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

4、在线UpSetR高阶韦恩图

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

在生信分析的实战中，我们经常需要探究多个基因集、多个组别的一些特征基因的相互包含关系，这时就会需要韦恩图或高阶韦恩图的介入。此前我们已经把UpSetR的代码教程发布完毕，UpSetR功能强大，几乎能完成高阶韦恩图的所有操作。若同学们觉得UpSetR的语法复杂，也可以用我们今天要介绍的在线版本。

代码教程：

[UpSetR高阶韦恩图| 1.基本用法](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495565&idx=1&sn=e098568d1f1d4c377c8daa8048205839&chksm=9b3c96ddac4b1fcb2fa1239ae270dca4a38db484199543d70fdd8321d4b7ef96b4ede2814243&scene=21#wechat_redirect>)

[UpSetR高阶韦恩图| 2.标注与图注](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247495752&idx=1&sn=25aeb8d267c1b5d168d94637cb2c08e7&chksm=9b3c8918ac4b000e9164433a4893a015ee549b6d70d735780f7b6479eac6d37ec74086af3354&scene=21#wechat_redirect>)

[UpSetR高阶韦恩图| 3.图形组合注释](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247496700&idx=1&sn=b197ff50a3555d935a37716dbafec088&chksm=9b3c8aacac4b03ba8ba236321232d159db69edf5e214c2383bc98dd0178a5111f72fc9964ba5&scene=21#wechat_redirect>)

[UpSetR高阶韦恩图| 4.注释及图片调整](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497682&idx=1&sn=b4436a156fea5c2071f8b2dc68e3054d&chksm=9b3c8e82ac4b079407b1c00238fc3a88fe76395b2aae3e3999da70871ca5a156de6588ccd5fd&scene=21#wechat_redirect>)

App在线版链接：

http://biomamba.com:34038/UpSetR

本地exe程序版下载链接：

链接：

https://pan.baidu.com/s/1TRTfGemASJL0mrZrjBkvmw?pwd=cgea

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyUjBUdYedwGR4wEiasDXz2TeibibWLe6xup9hhWibENzrA09o8lXWzm0ic6cjU4tdWbuZJnCAicZrGpiahA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

具体使用起来很简单，本地版打开exe文件后与在线版同理:

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

5、在线PCA分析

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)推送/教程：
[给你安排一个懂生信的工具人（八）：在线PCA分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485571&idx=1&sn=a0497f79fe83ff6b86705f6eb0e1cbf9&chksm=9b3f71d3ac48f8c528efe63261858d1f6ef46acd4af49cc2da2a5b5e85c59ae020ad0ab06a4e&scene=21#wechat_redirect>)

视频教学：

App新网址：http://xiyoucloud.22ip.net:34038/PCA.chinese/

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

6、在线KEGGE查询

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

上次顺手写了个能够查询KEGG中对应物种对应通路基因名及信息的App([给你安排一个懂生信的工具人（十一）：在线查询KEGG中通路与基因对应关系](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490119&idx=1&sn=f6f9a7f901c6fc1623552614d4ab8085&chksm=9b3f6317ac48ea01e67015d72a3079574b765889635cd6d5b99b5919a58935117a152a6fee5f&scene=21#wechat_redirect>))，考虑到时间因素我们的在线工具一般都做的比较简单实用，大家如果有需要添加的功能也可以通过文末客服告诉我们。这里我们对这个在线工具进行了更新，不仅可以输入通路名查找包含基因，也可以通过输入基因名查找对应通路，此外还添加了玉米(Zea mays)这一物种(这类没有orgDB的非模式物种需要通过AnnotationHub()获取对应信息)，大家如果有需要的物种也可以通过文末客服告诉我们。

在线版链接：

http://biomamba.com:34038/KEGG.Pathway.Query/

本地exe程序版下载链接：

https://pan.baidu.com/s/1a0yYeOEqLmWW-UVdP_5U8Q?pwd=gf44

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpy6vyDXWoFD2IdqAdhrt5oBQGokxYL8wOScibJNZQKYOLTPJNeCwqKJbeKok8h2XygiahdKTa1mE83A/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

具体使用起来很简单，本地版打开exe文件后与在线版同理:

B站同步播出，欢迎来三联:

https://www.bilibili.com/video/BV1334y197Pw?p=7

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)

7、在线统计推断

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWh2NFJDBiafvwwKurdL1kViaQZNVj4LpuVDSuXYukibmBxmSxibaA1GglIllTSLWKnRfa20fALeV7MpGw/640?wx_fmt=png)推送/教程：
[不会有人真的只会做T检验吧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484505&idx=1&sn=762f80bd6840ec03d5151592679240f9&chksm=9b3f7d09ac48f41f4279fccefeb6e4ca15b6a9c9cdd9a00a0cc23c93174fa2db084032828a74&scene=21#wechat_redirect>)

视频教学：

App新网址：http://xiyoucloud.22ip.net:34038/statisticalinference/
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**如何联系我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 公众号后台消息更新不及时，超过48h便不许回复读者消息，这里给大家留一下领取资料及免费服务器([有root权限的共享服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpwcHwaYgTDhqNg4hlJKR8HwvI9245ZYFHUETVz0nWvgeIficicsu9Y7U0xeO6F1UibHwUia5BHuyZVHBQ/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
