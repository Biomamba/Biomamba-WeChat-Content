---
title: "Rstudio-server为什么总是登不进去"
date: 2023-07-17
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501818&idx=1&sn=38d86cbe80bb0b496afd952014eff46f&chksm=9b3cbeaaac4b37bc2134c58aba8a84d9d5b016abbccf485750b4734fa4737db12a189869c109#rd
albums: ["答读者问"]
---

# Rstudio-server为什么总是登不进去

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501818&idx=1&sn=38d86cbe80bb0b496afd952014eff46f&chksm=9b3cbeaaac4b37bc2134c58aba8a84d9d5b016abbccf485750b4734fa4737db12a189869c109#rd
> 合集：答读者问

**写在前面**

![](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn5RYeZyo5amnOAgOiaRia5pTmJkLwBXH0J3icajPObPVuj8C5TeYLc8fI9KZickXDnsa1EvhSibltJv7VQ/640?wx_fmt=png) 相信大家在使用Rstudio-server时都经历过死亡转圈，这种情况一般发生于网络断开后需要重新连接至Rstudio-server的页面。这是个Rstudio**-serve****r** 固有的bug，有说法认为是由于Rstudio需要通过**RSession → C++ → Java → WebSocket → html+js** 的传递链将R的内核与大家可交互式操作的Rstudio进行信息传递[1]。换句话说，一切的可视化都是有代价的。所以推荐大家在合上自己的笔记本前先**save.image()** ，然后再**q()****退出** ，这样再下一次登入时无需加载额外的内容，自然也不会卡在这个界面，需要用到此前的数据直接**l****oad(.Rdata)** 即可。

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpz3q2VYQ2c7axy4QkGbsmONSEeY8EMOP9aaRgMDHlfkEIRlV2UbibTO0qXiafSadA4MZAhwmRyN8h6Q/640?wx_fmt=png)

**解决方法**

![](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn5RYeZyo5amnOAgOiaRia5pTmJkLwBXH0J3icajPObPVuj8C5TeYLc8fI9KZickXDnsa1EvhSibltJv7VQ/640?wx_fmt=png) 如果你已经遇到了死亡转圈，首先推荐用无痕模式打开浏览器，若上面的三个按钮均不能让你登入Rstudio界面，这时需要考虑以下方法：**1、杀死rsession对应的用户进程**

可以杀死当前的session进程，然后尝试重新登陆 rstudio-server。杀死进程可能会导致 workspace 中计算产生的结果丢失，因此要养成经常将计算结果保存在本地磁盘中的好习惯（保存为Rdata或rds文件），下次使用时直接从磁盘中加载就好了。

  *

```
COPYps -ef | grep "/usr/lib/rstudio-server/bin/rsession -u $(whoami)" | grep -v grep | awk '{print $2}' | xargs kill -15
```

**2、清除用户rsession**

一个 rsession 对应一个 rstudio-server 的会话，用户与 rstudio-server 建立一个连接后，会话信息会保存在一个文件中，如果出现 rstudio 卡住、不能登陆等情况时，在杀死进程后还是没有解决问题，可以清除 session 文件再重新登陆。这一操作通常要搭配杀死rsession对应的用户进程使用，因此*可能会导致 workspace 中计算产生的结果丢失***。

  *   *   *   *   *   *   *   *   *   *   *   *

```
COPY# 新版 rstudio 的 session 文件的存放位置ls ~/.local/share/rstudio/sessions/active# 如果有内容，则删除rm -rf ~/.local/share/rstudio/sessions/active
# 旧版 rstudio 的 session 文件的存放位置ls ~/.rstudio/sessions/active/session-*# 如果有内容则删除rm -rf ~/.rstudio/sessions/active/session-*
# 这里也可能有大量的临时文件需要删除：rm /tmp/
```

参考
[1]https://blog.csdn.net/zergskj/article/details/82880970[2]https://xiyoucloud.github.io/2023/01/28/rstudio%E4%BD%BF%E7%94%A8%E6%8A%80%E5%B7%A7/
![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4EiaLjQXteia730VKnC0j8Tkgu6hkTs7ZO0JRFyw8riaczdNlQQKsOnfIQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

如何联系我们

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWjsU2VMXgI8TRjfwVeo0Aj4z284kwxMryKUBLBbNicjxYMDvWxmosNGHmIW66jtmJuia0pe51q8hFzQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)公众号后台消息更新不及时，超过48h便不允许回复读者消息，这里给大家留一下领取资料、免费服务器([有root权限的共享服务器,注册即送200￥](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500273&idx=1&sn=f600f10077f6298ea957e459b5f8a375&chksm=9b3cb8a1ac4b31b702838076dbceb077e9c8980d9cffe5c4ab10ebbeceaf5fe3e658003e66c4&scene=21#wechat_redirect>))的**微信号[Biomamba]** ，方便各位随时交流、提建议(科研任务繁重，回复不及时请见谅，**备注来意会优先通过**)。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：[永久免费的千人生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247492981&idx=1&sn=aed903c4b853113d8c89e13848ea3365&chksm=9b3c9c25ac4b1533feb5f42f94ab4b6023a160313db4bc6a2f142e54d26627e3ea94b53e9031&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxD2E7IWhoq4ufKkicBibrsZDOgj4GOibMq3okeKsrLGaNeWVOKL2lxyx5UrDR8sV4lCC2RkibjAq722g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)您点的每个赞和在看，我都认真当成了喜欢
