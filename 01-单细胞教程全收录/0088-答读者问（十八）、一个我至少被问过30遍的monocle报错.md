---
title: "答读者问（十八）、一个我至少被问过30遍的monocle报错"
date: 2022-07-24
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25#rd
albums: ["单细胞教程全收录", "答读者问"]
---

# 答读者问（十八）、一个我至少被问过30遍的monocle报错

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490010&idx=1&sn=24c55fa4bd5d7d829625cb67dbaf321a&chksm=9b3f608aac48e99c9f27e3423c8398034a1819d0ccebbf21170b955461d2c335132d6f3cce25#rd
> 合集：单细胞教程全收录 / 答读者问

问题

#### 最近很多同学在学习我们monocle2的教程([单细胞测序数据进阶分析—《拟时序分析》3.monocle2实操：完整版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487400&idx=1&sn=223a96a245c408c31e2c3c16afac88fc&chksm=9b3f76f8ac48ffee769dc76870e15bbd0275647dcfb9bf21bf499b7eaee86121b254e4b2da54&scene=21#wechat_redirect>))时，在运行到orderCells函数时会出现如下报错。几乎每天都会有人问这个问题，从教程发出以来已经被问了数十遍。

![](../../images/bc270cbacb87c72a.png)

怎么解决问题

其实这个问题的答案很简单，我在最开始录这个视频课程的时候就已经说过了，不信大家看，这里的4:00处我已经说过了，如果你的monocle2安装的不是2.18.0的版本，orderCell()的时候就会遇到这种问题:https://www.bilibili.com/video/BV1br4y1x7Hf?p=4

![](../../images/fe2182a92d83d949.webp)

视频(点击文末阅读原文可跳转)中4:00开始到8:00结束主要就是为了给大家解释这个问题如何去解决，这里我们也把代码贴出来再给大家演示一遍：
1、安装conda：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.shbash Anaconda3-5.3.1-Linux-x86_64.sh #安装conda，出现选项选yes
#添加一些镜像conda  config --add channels defaultsconda  config --add channels conda-forgeconda  config --add channels bioconda#增加bioconda，方便安装生信软件
#最近阿里的镜像似乎比较稳定：conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/conda-forge/conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/bioconda/
```

2、创建虚拟环境并安装r-base-4.0.5：

  *   *   *

```bash
conda create -n monocle.2.18.0conda activate monocle.2.18.0conda search r-base#会返回一大堆版本给你，几乎也是所有版本了
```

![](../../images/fcec00c9f78dda7d.webp)

  *

```
conda install r-base==4.0.5
```

3、安装monocle 2.18.0

  *

```
conda install bioconductor-monocle==2.18.0
```

没错！其实大家的问题这一行就可以解决！

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

[答读者问 （十二）ERROR: have no zero exit status](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485290&idx=1&sn=1e77059439342374ea03496cbba08070&chksm=9b3f7e3aac48f72ca08f5e73496e6f8c99c5fd74a39daa626d636ba5a7b0b89873437ebcb6d4&scene=21#wechat_redirect>)

[答读者问 （十三）查看Seurat对象时的ERROR：type='text'](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247485859&idx=1&sn=a014c4cb6034551e57c70820c7781e49&chksm=9b3f70f3ac48f9e52620e3ff197eb98e58836e8bb6baad634387a521fdda1e4a194356517c73&scene=21#wechat_redirect>)

[答读者问 （十四）Seurat中分类变量处理技巧](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486134&idx=1&sn=e581b8ac20bbc968aeef3f9cf56f3a0f&chksm=9b3f73e6ac48faf0f1c81752b0190abc617eb720a71806950e7851c7d19b7e3e092aa97bd005&scene=21#wechat_redirect>)

[答读者问 （十五）稀疏矩阵转matrix, as.matrix函数是下下策](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247486259&idx=1&sn=97de5c9e15e48cb62c8a680376a4ee0d&chksm=9b3f7263ac48fb75a91b40416826fe35b340284cf38255925ac447443a62cdc1df082d20fb61&scene=21#wechat_redirect>)

[答读者问 （十六）做单细胞测序到底需要多少内存](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247487923&idx=1&sn=15043c6d729b0d5493ab875b0e54a259&chksm=9b3f68e3ac48e1f5dae514a01c857f9a56a90e2977dd7862db28d06fe55888cd9bb4afbb14e0&scene=21#wechat_redirect>)

[答读者问 （十七）调用的线程越多就算的越快嘛?](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488995&idx=1&sn=7140e0d037671542fb37dff3a3c94b28&chksm=9b3f6cb3ac48e5a5f54a02be9e6af9f5a4cf8da1de1770f9035130c84dedf059a024964fc15a&scene=21#wechat_redirect>)

![](../../images/56869e2cc75aa830.png)

如何联系我们

![](../../images/7c0febec2249cfa6.gif)公众号后台中消息更新不及时，超过48h后便不允许回复读者消息，这里给大家留一下领取资料、咨询服务器的**微信号** ，方便大家随时交流、提建议（由助理接待）。大家可以阅读完这几篇之后添加[笑一笑也就算了](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484685&idx=1&sn=3b47c0bcad97a265650b5f34c00a6a3c&chksm=9b3f7c5dac48f54be9cde50ab7a1147c55a36b980ffa0e721c02c05cbb88fef41a8fbc13d599&scene=21#wechat_redirect>)[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247488966&idx=1&sn=9e9e7659b4cf00ac3173d21e88e1602b&chksm=9b3f6c96ac48e580efe53f966430f6598785e5c5c6bcc20f5eef019e723e49baaaea6d73fb7b&scene=21#wechat_redirect>)

![](../../images/fdb4c49c78e6216c.webp)
