---
title: "如何把Codex装进终端直接调用算力？"
date: 2026-10-08
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542898&idx=1&sn=d0f65e1be8351366d64747ca6edb5e19&chksm=9b3c5122ac4bd83417bf59f001c6119828b99da2cc9baa7eed16e0a1cb44e45046a3f9ee0895#rd
albums: ["AI时代，不用就会被淘汰"]
---

# 如何把Codex装进终端直接调用算力？

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542898&idx=1&sn=d0f65e1be8351366d64747ca6edb5e19&chksm=9b3c5122ac4bd83417bf59f001c6119828b99da2cc9baa7eed16e0a1cb44e45046a3f9ee0895#rd
> 合集：AI时代，不用就会被淘汰

上期[Codex复现单细胞论文实测（基于gpt‑5.6‑sol high）](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247541384&idx=1&sn=483a12dca401717fce52e6c608149851&scene=21#wechat_redirect>)评论区小伙伴需要在终端安装codex，废话不多说，你如果拥有[足够支持你完成硕博生涯的共享服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540790&idx=2&sn=3e34a111e77e0cf29ee21b48a7940a9a&scene=21#wechat_redirect>)，直接上实操：

由于Codex客户端基于JavaScript开发，因此在安装Codex之前，需要先配置 JavaScript运行环境nodejs。

推荐使用[conda](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530994&idx=2&sn=3f3bdf2d06532c0b0ab8c9a477b8332c&scene=21#wechat_redirect>)对nodejs及相关依赖进行独立管理，从而避免不同软件或项目之间出现环境冲突。这种方式尤其适合在命令行中使用AI辅助编程，再通过 RStudio等本地开发环境查看运行效果，并对代码进行进一步调试和优化。

  *   *   *   *   *   *   *   *

```
# 创建一个名为codex的环境，并预装nodejsconda create -n codex nodejs -y -vv
# 激活codex环境conda activate codex
# 检查node以及npm版本node --version && npm --version
```

## 安装Codex本体

Codex是个命令行的工具，我们需要安装codex才能使用其功能。

  *   *   *   *   *

```
# 国内服务器，可以指定源安装npm --registry https://registry.npmmirror.com install -g @openai/codex
# 查看codex版本codex -V
```

## 配置环境

  * Codex是OpenAI公司的，默认情况下，我们没法顺畅访问国外网络，支付也有困难。
  * 这里手动配置~/.codex/目录下的独立配置文件。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 创建配置目录mkdir ~/.codex
# 配置KEYvim ~/.codex/auth.json{"OPENAI_API_KEY": "你的API_KEY"}
# 配置URLvim ~/.codex/config.tomlmodel_provider = "Biomamba"model = "gpt-5.2-codex"model_reasoning_effort = "xhigh"disable_response_storage = truepreferred_auth_method = "apikey"[model_providers.xiyou]name = "Biomamba"base_url = ""wire_api = "responses"
```

## 启动Codex

  * 创建项目工作目录，然后执行codex命令进入codex终端。

  *   *   *   *   *   *   *

```
# 创建项目【可选】mkdir codex_project
# 进入工作目录cd codex_project# 启动Codexcodex
```

  * 选择允许操作当前目录文件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmqu0MAW4WOg8amtsYXhm8scg1qFaBFtibqTUSokwRfWn93re2yIdd09R4SgjLsRicL0aoJl9tpuFozWp0uHibKxhM05VHibrWic5CY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)![图片](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkGxOEGyhL3eia2pySBlouXMHcQicbVfOSd5KOtWaVVxvawCKVR3rVxBymumjrj09JDW973WVuwL2G1a1Ka1WFxhxsYUIkRmW0ic8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

  * 查看配置是否正确

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlaH1morQACCkiccMPIKswn58YVozDLY73kFxo4ziadTo5uRtVjyibr8AbE1lYMrBYficbJRzJf3jTicVkw7C1Kh7WKJueo9VmHcG2w/640?wx_fmt=png&from=appmsg)

  * 输入相关的指令，即可让AI帮我们完成相关工作。

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwko2qrIUQI6X9Nq0Ly5u1Th3x9VvsPwMBX54bic9Lf8XVVambbChiaoQvwiaiauejlr4ALvh6R6JmOOWhgjHZRDLYqspQXBOXSEAUs/640?wx_fmt=png&from=appmsg)

  * 如果需要退出，输入/quit即可。

## AI时代，服务器算力才是真的生产力

短平快，配置与价格见下图，详细介绍见[入手足够完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530226&idx=2&sn=0522eb4eae67efeea2b96404474af611&scene=21#wechat_redirect>)、[独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21#wechat_redirect>)、[低价使用高端显卡RTX5090(32GB)、RTX4090(48GB)、RTX4080S(32GB)、5080S(16GB)、5070(12GB)显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542443&idx=2&sn=6c76a5b422ddf941577c27273b6ad11a&scene=21#wechat_redirect>)。随时滴滴**微信号[Biomamba_yunying]咨询获取[教程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>),也欢迎注册试用：https://biomamba.xiyoucloud.net/**[![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnB3Tc9oK2fKianQIsJF24UOpPJon6n4pGnBU1zOzg7Tfagfhh9iaGzgSeyzUs85dhUfJnGfE0lI6Es8w5p3hyQnaYrLZaD0Qm3Y/640?wx_fmt=png&from=appmsg)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247540790&idx=2&sn=3e34a111e77e0cf29ee21b48a7940a9a&scene=21#wechat_redirect>)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkf9vFf7ze6iarvt9SCz4t2zcNHz55iaIccmRlZB4BcY7icTaUO88zwV9MiaDyEGicPGmjq1kUSspbWclQzTpdfYSSTTHOzSDCsb7JM/640?wx_fmt=png&from=appmsg)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534707&idx=2&sn=2844377758ce00e07435a5dd376b4715&scene=21#wechat_redirect>)[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnNp95nSnbgddx3tgUOyAhWv7ssoESAGgZaiaDOicWBJvKxhGbr5pXlibYIrShH8442bS5ickUzj46iaO9Q805pEicEAg4SfN9reFt3w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247542443&idx=2&sn=6c76a5b422ddf941577c27273b6ad11a&scene=21#wechat_redirect>)给大家组建了AI生信交流群，欢迎入群对线![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkszoWzNfw5RpNiapm2x083MYzIJzuobaVCjOsICjCZdx1W8slVqBjtN92mib5nwBFibzCgSVBl70gOrg2s2CGZDsjdUQrGSnHIYo/640?wx_fmt=png&from=appmsg)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**欢迎交流**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539170&idx=1&sn=ebd269635da35335554c53709fa0a0c0&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的助手[Biomamba_zhushou]，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家一起讨论。![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24)您点的每个赞和在看，我都认真当成了喜欢
