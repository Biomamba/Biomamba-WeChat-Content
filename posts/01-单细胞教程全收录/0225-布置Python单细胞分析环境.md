---
title: "布置Python单细胞分析环境"
date: 2025-04-22
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528493&idx=2&sn=b8add6f0303ec6032ecc2242f59d8289&chksm=9b3c097dac4b806b5c80b16a5fdbbb9a9bcfea3960b4a5c086c50feb2f91c6fe33db9a38a407#rd
albums: ["单细胞教程全收录"]
---

# 布置Python单细胞分析环境

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528493&idx=2&sn=b8add6f0303ec6032ecc2242f59d8289&chksm=9b3c097dac4b806b5c80b16a5fdbbb9a9bcfea3960b4a5c086c50feb2f91c6fe33db9a38a407#rd
> 合集：单细胞教程全收录

**一、写在前面**

此前我们的单细胞分析教程大都是基于R中的神包Seurat([scRNA-seq数据基础分析手册(2025最新修订)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&scene=21#wechat_redirect>))，现如今面对指数级增长的单细胞数据，基于Python的Scanpy([scRNA-Seq学习手册Python版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&scene=21#wechat_redirect>))其实是一个更好的选择。目前Python具有丰富的科学计算库和活跃的社区支持，在数据处理、可视化和与其他机器学习或生物信息学工具的集成方面展现出巨大的灵活性。即使是R语言一直引以为傲的可视化能力，也被Scanpy迎头赶上：其内置了多种可视化方法，从而利用matplotlib和seaborn等Python可视化库，可以创建高质量的图形，并且能够方便地进行定制和扩展，以满足不同的可视化需求。由于Python在机器学习([机器学习基础手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&scene=21#wechat_redirect>))领域的广泛应用，Scanpy 可以轻松与其他 Python 库和工具集成，如用于深度学习的PyTorch和TensorFlow，以及用于数据处理和分析的 Pandas 和 NumPy 等，便于进行更复杂的多模态数据分析和机器学习任务。不得不提的是，在处理大规模单细胞数据集时，Scanpy通常具有较好计算效率，无论是计算速度还是内存占用上都比基于R的Seurat要好得多，这使得它在处理海量单细胞数据时表现出色。

所以，不得不拥抱未来，让我们把Python中的单细胞内容学起来吧~

本教程基于Linux中的Rstudio环境（[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526504&idx=2&sn=417d07347cebe0a1bd403f6c3e7d9b29&scene=21#wechat_redirect>)）演示，计算资源不足的同学可参考：
[生信分析为什么要使用服务器？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247491007&idx=1&sn=8619c2bad23791b3252a1c4cb1831931&chksm=9b3f64efac48edf9c02f84959aeee9b12480736fce70c5ddb8b41d79cfc22ce590ea2cb60fba&token=1760636281&lang=zh_CN&scene=21#wechat_redirect>)
[足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21#wechat_redirect>)
[独享服务器，生信分析不求人](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503618&idx=1&sn=ca47ca985aa8560f6b38f15f210519e2&chksm=9b3cb652ac4b3f44292560071b7e98e2f6fa6ec03581cd882a4d59b9d7fa063a5b9ac1b923f3&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/

更多内容可咨询客服微信[**Biomamba_zhushou**]

**二、实操**

##  2.1 `Python`基础

首先，你在学习这个教程前，需要有一定得`Python`知识，可以参考[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&chksm=9b3cb9c1ac4b30d7bbd44057b181f87541f5904d24f903494ae557e768ae00c208c1b68b45c7&payreadticket=HFPtvn0Hc_3itk_RHA90ykGyhDmPMGdHlmAWpCN5_JoUcbpyL6P82ctGZm0c2MiiBCZcLU0&scene=21#wechat_redirect>)进行快速学习。

本文依赖的`Python`版本需要 `>= 3.7`

## 2.2 包的安装

Python包的安装有诸多方式，我们提供了主流的几种。无论哪一种，只要正常安装即可，无需重复安装。大家出`bug`时也可多方尝试:

### 2.2.1 终端安装

你需要在终端中完成:

  *   *   *   *   *

```
# [leiden]会自动安装pandas 和 numpy# 安装时间可能会比较久pip install 'scanpy[leiden]'# python-igraph仍需额外安装pip install python-igraph
```

### 2.2.2 conda安装

conda的安装我们反复提到过([生信软件管家——conda的安装、使用、卸载](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506208&idx=1&sn=24d27bc2ff8de340b1f542610b4dc09e&scene=21#wechat_redirect>))：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 本代码框依旧在Linux终端中完成# 1、安装conda：wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.shbash Anaconda3-5.3.1-Linux-x86_64.sh #安装conda，出现选项选yes##安装过程一直敲回车、遇到询问均填写yes后敲击回车即可，安装时间需要花费5~10分钟，如果选择安装 Microsoft VSCode部分，会额外花费一部分时间。# 重启一下环境配置，否则无法直接定位到conda：source ~/.bashrc
# #返回完整路径即为安装成功which conda#添加一些镜像conda  config --add channels defaultsconda  config --add channels conda-forgeconda  config --add channels bioconda#增加bioconda，方便安装生信软件#最近阿里的镜像似乎比较稳定：conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/conda-forge/conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/bioconda/
```

配置好`conda`，真正安装`scanpy`时一行即可搞定：

  *

```
conda install -c conda-forge scanpy python-igraph leidenalg
```

### 2.2.3 R语言调用安装

如果你与我一样是在`Rstudio`中调用`Python`，那么你可以通过`reticulate`调用`pip`进行安装。也可以通过`reticulate`调用`conda`安装。

  *   *   *   *   *   *   *   *   *   *   *

```r
library(reticulate)conda_create("my_scapy",python_version = "3.10.4")# conda_remove('my_scapy')use_condaenv("my_scapy")# install SciPyconda_install(packages = "scanpy")conda_install(packages = "python-igraph")conda_install(packages = "future")conda_install(packages = "leidenalg")# install SciPyuse_python('C:\\Users\\CPU1302\\AppData\\Local\\r-miniconda\\envs\\my_scapy\\python.exe')
```

  *   *   *   *

```
# 或者你也可以在终端中运行python.exe进行安装：C:\\Users\\Username\\AppData\\Local\\r-miniconda\\envs\\my_scapy\\python.exe -m pip install scanpyC:\\Users\\Username\\AppData\\Local\\r-miniconda\\envs\\my_scapy\\python.exe -m pip install python-igraphC:\\Users\\Username\\AppData\\Local\\r-miniconda\\envs\\my_scapy\\python.exe -m pip install leidenalg
```

  *   *   *   *   *

```
# 此代码框在R中运行# reticulate安装# 这一步需要关掉梯子，否则hostname报错reticulate::py_install("scanpy")reticulate::py_install("python-igraph")
```

## 2.3 单细胞相关知识

这个就不用强调啦，熟悉我们的小伙伴应该都学过这些教程了，建议耐心看一遍哦，以备不时之需：

[生信基地122篇单细胞教程全索引](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528470&idx=1&sn=7f3ced59b2b97bed1ac9df560b11ddd6&scene=21#wechat_redirect>)
B站视频:先看一遍视频再去看推送操作，建议至少**看三遍**

后续我们会推出更多的Python单细胞知识，敬请期待！

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 留一个领取资料、[免费两周学习版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527585&idx=1&sn=fa32112c11b215b33096cab43baf08ea&scene=21#wechat_redirect>)服务器的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) 您点的每个赞和在看，我都认真当成了喜欢
