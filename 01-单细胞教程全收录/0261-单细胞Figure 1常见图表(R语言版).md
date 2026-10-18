---
title: "单细胞Figure 1常见图表(R语言版)"
date: 2026-01-28
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534718&idx=2&sn=0d9bff7b943b6fb3f60c44287e6f1efd&chksm=9b3c312eac4bb8386c3cd3ee369398acf33372c4689e89162a52e0abfddc15f55fb15f4703fe#rd
albums: ["单细胞教程全收录"]
---

# 单细胞Figure 1常见图表(R语言版)

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534718&idx=2&sn=0d9bff7b943b6fb3f60c44287e6f1efd&chksm=9b3c312eac4bb8386c3cd3ee369398acf33372c4689e89162a52e0abfddc15f55fb15f4703fe#rd
> 合集：单细胞教程全收录

![](../../images/399758fa7d6941c2.png)

写在前面

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)近年来随着单细胞测序技术的日益普及，普通的分析及**可视化** 已经越来越不能够满足各位的分析以及可视化需求。信、达、雅的全方位要求使得现在单细胞可视化越来越**卷** ，本文整理了单细胞Figure 1的**常见图表** ，能够展示单细胞数据的质控数据小提琴图、降维图、细胞比例堆积柱状图、富集分析气泡图、marker基因散点图等。更多单细胞可视化教程可参考：[单细胞图片改造计划](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2707677276481814529#wechat_redirect>)更多单细胞相关内容分享可见：[82h视频教程《Python版scRNA-seq分析全流程》](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533067&idx=1&sn=7ef76058cbcf7bd45f58147766c75854&scene=21#wechat_redirect>)[100个小时沉浸式学会scRNA-seq数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531092&idx=1&sn=9968319b84186bb9b717b7b409132d8b&scene=21#wechat_redirect>)
**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

所见即所得

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)一如既往地，我们整理好了测试文件和代码的html文件，供大家翻阅学习：![](../../images/f99d013e9a491b52.gif)
分析输出图片示例，相信足够用作大家的"单细胞Figure 1"：![](../../images/3d411ae0fe9ba3dd.webp)

![](../../images/7d247e6c6ef19f87.png)![](../../images/399758fa7d6941c2.png)

视频教程

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)B站连播更方便：https://www.bilibili.com/video/BV1S44y1b76Z?p=19
![](../../images/7d247e6c6ef19f87.png)
![图片](../../images/c33e327c8d66af99.webp)

更多订阅合辑资料

![图片](../../images/3ff4011fef611c1c.webp)![图片](../../images/00dcbb5df4af21d3.webp)

以下内容可根据终身订阅的用户可直接获得，后续内容我们持续发布中:

**
**

**2026订阅合辑：**

[ 2026订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534690&idx=1&sn=4ff5291b649fb4fe4d703c48a04d37f2&scene=21#wechat_redirect>)

![](../../images/520a869af2c7921a.png)

持续更新中~~

**2025订阅合辑：**

[ 2025订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526751&idx=1&sn=7ca3137d770f23f0c3d6195696618d81&scene=21&token=2143911808&lang=zh_CN&poc_token=HPJ5S2mj1patGAgGn2rvK_cl-hJW1vlWazK5cQHg#wechat_redirect>)

[《Cell》复现|中性粒细胞scRNA-seq图谱阐明抗肿瘤抗原呈递效力](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526776&idx=1&sn=99eb6a16c7bf345445b6ff4b61110138&payreadticket=HC__tGU8L5JA4wSD5JEaMhGrY7HFBRroyAtGo_3uXJgF2t-nj7ILdcOk3g21iGGHpvESIaY&scene=21#wechat_redirect>)

[代码复现|scRNA-seq绘制透明细胞肾癌的免疫微环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527498&idx=1&sn=c8282e9d4175bfb2e572278312073d81&chksm=9b3c151aac4b9c0c2ac7f0c184f5bba183b52a6c9b9f4e30d0494ef752df0cd216afe15dbf2f&scene=21&cur_album_id=3810782335739215872&search_click_id=#wechat_redirect>)

[改造单细胞DoHeatmap](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527762&idx=1&sn=ba7c8a4cb704e71fa86ebfe1f19bffea&chksm=9b3c1402ac4b9d142d99d739a6de3623182488fd6fa1b312e773b39a1a317642ddc4fa422997&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[Slingshot拟时序分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527850&idx=1&sn=f4e2ca5e2e5e71eeaf132375bb8270eb&chksm=9b3c14faac4b9dec4d9a4f90419c0aa9e8ef5630435f9d48ae8022cd91e7a0b46e4ba32f50bb&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《Cancer Cell》|时空单细胞揭示CRC的PD-1治疗免疫细胞动态](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528056&idx=1&sn=73c0da3ff7ff50bafbb9315fd5b60f15&chksm=9b3c1728ac4b9e3ea3d3a35b9a60d5b21f74fe08671da8388c60ed43ba310617e6c48566b54a&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[scRNA-seq数据基础分析手册(2025最新修订)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528199&idx=1&sn=ab75e7d7987ab233c675455188f10f33&chksm=9b3c1657ac4b9f41e312a5f508fa1fb2158dfdbaacfb2d67c3ffa3d134b0c6b5672c062499da&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[代码复现|吞噬作用增强肿瘤中巨噬细胞的氧化代谢和免疫抑制特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528289&idx=1&sn=b56f00f3d8a4b152e54f3acd40aef21d&chksm=9b3c1631ac4b9f27db6577962d2113ae2fa5c3960ac942bf6ee94f58073642eeb6a4d8369212&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文学会scRNA Velocity剪切速率分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528458&idx=1&sn=900357283922571c6294435be409a2f3&chksm=9b3c095aac4b804cecf155daa5a08391536d9f906ab6edb6c6650ec868ad1b14dc7be8bbde36&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文学会四种scRNA-seq轨迹分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528666&idx=1&sn=d29545d296bac3e41de322e43fde80dd&chksm=9b3c098aac4b809c28bb5c36a8a7f045e6e2339342640716763283b4b2e6c948f1d1869bd7df&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文学会四种scRNA-seq细胞通讯分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528770&idx=1&sn=6242bce437a9d60f81a8651ea9b57e0b&chksm=9b3c0812ac4b81040db203fef3e09e40e371f8095981f3cb55b8d9fce13fdba9c8bdc2dc8404&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文学会四种基因共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529410&idx=1&sn=9bbaf955d93ddce60874e1cdc2f16115&chksm=9b3c0a92ac4b8384232b692057cba6acb7dba9c6af666e4ec7fc166e0ff960b18b857b8cfb98&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[肿瘤异质性分析必备| 一文学会四种scRNA-seq拷贝数变异分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529921&idx=1&sn=93f8ad6655ee6d2b036cd557a6a74be6&chksm=9b3c0c91ac4b85876ae4064fe28c95a0629550e29575faca5dcdd5b56aeddf8fae6584937572&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[分子批量对接与亲和力热图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=1&sn=90de71a3b453e635920d309faedb36c7&chksm=9b3c0ffaac4b86ec8f1b8b46d0f76db869e6dfb4e8bb5c64a064a86f19c2dcf606d2e54e5edc&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性与增殖](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530338&idx=1&sn=2d092e76080359f5a169ec14d54d1241&chksm=9b3c0e32ac4b872435a1f4af3c6903c777fdb07f43ad222ccbf08163ae259d56b9e499ee2fe6&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[单细胞免疫组库测序(scTCR+scBCR)学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&chksm=9b3c001aac4b890c144c8a3a37f9c6587f35341cf2090241400dad2e2ef0b08c7b8ccbd7fe2e&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文掌握WGBS分析流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531339&idx=1&sn=83d6e80e24494cc7080188d5c9e695e2&chksm=9b3c021bac4b8b0ddd6b02925ba1c43f965f8e83db7c599032040f27b068334b3601846837cd&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《NC》代码复现|snATAC联合scRNA-seq揭示小鼠肾脏细胞分化程序与疾病靶点](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531908&idx=1&sn=2f094e390621a57853ba17f59f298ebe&chksm=9b3c04d4ac4b8dc26acab20d53b4c9f6cc50132d7ef4da167ff068a49f4801e7c42d96c6c986&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[空间转录组数据基础分析手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532178&idx=1&sn=2cc8f5453765bd68b8ddacf2c2e3d5e7&chksm=9b3c07c2ac4b8ed427f3bdd2c2f275e66110494056574cd7cc18d03a8ad9d9fe0e6eaf1706c5&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[空间转录组|多样本整合分析手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532349&idx=1&sn=59c0f14043906ff50c56dea3b16e9200&chksm=9b3c066dac4b8f7bb9f00c29c0085be4a049064eac8116ddcc7fab9e534b7aa031d90f8b6415&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文学会三种空转数据共表达网络分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=1&sn=cd16d0151ef19c9a2dcfcba6ee09f431&chksm=9b3c0605ac4b8f13ede1e916f40e53c732614acb04c136f7c3f3e0b619dfbc10230c9ed58da0&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文搞定空转数据反卷积分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532458&idx=1&sn=f8ec547187374fe77c38fc1125709b3b&chksm=9b3c06faac4b8feca4a51657dc85b5cd8f176767eb01887702df0abe82e4d933fe0efb8a2cc9&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[三种方法教你搞定空转数据邻域分析：squidpy+stSME+NMF分解](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532641&idx=1&sn=c8422ab7c1cd70751fb3109a84cb64ea&chksm=9b3c3931ac4bb0275fe5fd89712535cce677a308ac5a2c4e85d6f2a8785a4c76359e6612553c&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[空转细胞通讯分析学习手册：CellPhoneDB+Commot+stLearn](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532763&idx=1&sn=f6e4df9242f1341d2dc7e6154c33aa46&chksm=9b3c398bac4bb09d978dddd3f44c04c855ec89f6cd949fccbe497c515a62440f58dca31b4885&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[空间转录组轨迹分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532806&idx=1&sn=7d7ecf4977cb2cc9ace0e4e31941a1ac&chksm=9b3c3856ac4bb140a5f0955158656f458951cfe9bdd0a68d8c8ff74bd1e3f7adcc4da76197f0&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[空间转录组数据拷贝数变异分析学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532924&idx=1&sn=46b87151e30163e393cf2c1751360bac&chksm=9b3c382cac4bb13ad9aecd8783f1c6b0c576b1a25d04c3d15fa95a7e4fd5fdd8090cba7ce027&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《Nature Genetics》文献复写 | 结直肠癌免疫细胞的高清空转分析（Visium HD+Xenium）](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247533068&idx=1&sn=52cbc8d161ec216b5d7a8238a49d47c6&chksm=9b3c3b5cac4bb24a1b5c8ee1304f896c2ccea583e81bda4f9fae26564bc7d77c09a58baef3de&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

**龙年订阅合辑：**

[ 龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)
[单细胞Figure 1常见图表](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509260&idx=1&sn=9ff90a428c3f22d43a31ec864e2d8a94&chksm=9b3cdc5cac4b554a2f7cb2a6368f7df9a9a3f6e406eb070663f53d81841a76e188c0b50727de&scene=21#wechat_redirect>)
[快速上手Seurat V5](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509880&idx=1&sn=3b7cd169ccfe688d10cb1ca70dc91e91&chksm=9b3cde28ac4b573ec6d5f4bceafa4294c0e9a001b7d0c0b64f274a9978b1438eeccc747ca0c0&scene=21#wechat_redirect>)
[机器学习基础手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510121&idx=1&sn=87b53d350d9aedd5b3205d59e51356a0&chksm=9b3cd139ac4b582f23dd0ca65dcc66bed80b4240da76ee5abfbb61ec1bf62674ebfd2c50a45e&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V4修订版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510380&idx=1&sn=0eb2b0c519ef1dc25ee8821b736a0fde&chksm=9b3cd03cac4b592ad93149fb4847e6ba3dd03ab69e1ca594ddc64d323fb7496775789cae245d&scene=21#wechat_redirect>)
[Bulk RNASeq| 转录组实战](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510793&idx=1&sn=bfa69e8f261932d9bea74443fab732f0&chksm=9b3cd259ac4b5b4fd4b3bb80d0210a3396cda777b32ab49be1a45339453db314bb2a17fc438d&scene=21#wechat_redirect>)[scRNA-Seq双细胞过滤手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511622&idx=1&sn=60b35668e569267bab14ec8fbba8bd74&chksm=9b3cd716ac4b5e00122eac47f55085198040a4a0e97c56895bbc39f3a9f1a1eb4eba27048a8f&scene=21#wechat_redirect>)
[CellChat空转细胞通讯合辑](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247512011&idx=1&sn=fbd41832c5995d79fead016931d3bfbd&chksm=9b3cd69bac4b5f8d16e7d8b8eeb5490e4938daf68902b06a8d60e25f150ec4ec459796f3aaac&scene=21#wechat_redirect>)
[scRNA-Seq学习手册Seurat V5更新版](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247519711&idx=1&sn=d25d4f5daf609bda8367f16db676ecf3&chksm=9b3cf48fac4b7d99e65eba6d4c66c63e40b1d187fa1d9e6449d6cd07d5dec5127cff54886f93&scene=21#wechat_redirect>)
[SCENIC转录因子调控网络图](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520750&idx=1&sn=496bead1531a7eddd5c286030d350745&chksm=9b3ce8beac4b61a8589a1f8a66bd0571e09c0646655b6d805348bf6f4a0c7b52851615c22868&scene=21#wechat_redirect>)
[scATAC分析学习手册](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521636&idx=1&sn=208907010f3f7412c1c91343d7dfb0d3&chksm=9b3cec34ac4b6522977cb002919634af5334eec170b32f4961826dafb42f44f611144b159b2b&scene=21#wechat_redirect>)
[单细胞拷贝数变异学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522733&idx=1&sn=4e3a0707fd8f83b5ad9377bc91ee8e53&scene=21#wechat_redirect>)
[microRNA-靶标相互作用及疾病和药物关联分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247523676&idx=1&sn=6dad381e38df9ad63b90ed5935b73bf0&scene=21#wechat_redirect>)[《NC》代码复现| scRNA-seq揭示人纤维化皮肤病中的成纤维细胞异质性和间充质成纤维细胞增加](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247525649&idx=1&sn=6145f50422ef8680be2a7ffd6c66f5f3&scene=21#wechat_redirect>)
[《Nature Communications》| scRNA-seq揭示头颈癌早期转移过程中潜在的免疫逃避机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526011&idx=1&sn=e601b8dedfad86ee6d9ce5b6d6ca8511&scene=21#wechat_redirect>)
[代码复写《Developmental Cell》|利用scRNA-seq对新生儿~成人肝脏发育和成熟的时间分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526426&idx=1&sn=7191649a25332d1b8bf2bd9c797d06a7&scene=21#wechat_redirect>)**2023订阅合辑(含2022年)**

[ 2023年订阅须知](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497382&idx=1&sn=95586ea6dc381f8b8941cbd50f914c34&chksm=9b3c8ff6ac4b06e0a44df58181c3c85ea856fbc1b02e819640f7d9963fb598a4c4abb84f000f&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[2022资料合辑(重置链接)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497402&idx=2&sn=4873b9088938bb39caab6f95ba4c085a&chksm=9b3c8feaac4b06fc88dc2bf696bb728c3d4bd3a4fb5c028ce4d3c9bbadd3aa6dc560510762b9&payreadticket=HNYpQvSInra-3ldTyzGJVm9iyIh-rqIogbBlJgMM3pZQ5wwMMc298D8UYY0f0jk0zv4wgcc&scene=21#wechat_redirect>)

[一文搞定拟时序分析的下游可视化探索](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497634&idx=1&sn=64872660e8ce80ff08c6c0745c2b241b&chksm=9b3c8ef2ac4b07e4a2ef03870c91fdc1c3ded245dcecd5a2049841cb7e9749bd1cd0852133f1&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[Seurat中如何让细胞听你指挥](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497669&idx=3&sn=ac3408c7dd28425426d954f81d283252&chksm=9b3c8e95ac4b0783c12182a960e8158c8a0992a20335f8c70f1dc63855c5984dd22e4dee706d&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[拟时序分析| 3.monocle2实操：完整版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497730&idx=2&sn=930dc0e276219d70c937e943119388ff&chksm=9b3c8152ac4b08446d457cef3ede4a4a17c0ebacaec0c36efe7d7c8706fb4a3d62222d702ee5&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文搞定单细胞基因集评分](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497831&idx=2&sn=82fa51c76a381fba0b444e9b6b23eb5f&chksm=9b3c8137ac4b0821dfb62e9b365ea3c32abbbd80df42df63181c37ad9ed991c0183c2c7981d8&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[改造单细胞降维图| 2.ggplot2中的DIY](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=1&sn=37a539bbd37dafb6cce5cd52dec84f52&chksm=9b3c81dbac4b08cd34b5edab4da14df5d0964a5c6fbe4dbab6f9879bbac9bc3f9e08abe8dd1c&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[改造单细胞降维图| 3.3D降维图与动图绘制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247498080&idx=2&sn=a9bcf65e3ae34ba201e8d49ee33c0728&chksm=9b3c8030ac4b0926c3f059a9a5d23f1bcdbcaf8e5a562eba2b7e3bec3396c44573269bd08e7b&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文搞定单细胞/空间转录组的WGCNA分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499737&idx=1&sn=b3f6174e1908494692d82ac154ce3218&chksm=9b3c8689ac4b0f9fbb0c8ba42172c702ca978683c4de28f9f56bd8e7764fe114ba9a1b9c7dac&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[生信Python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247499921&idx=1&sn=dcd6f95596e3de9bf378d850c217fe78&chksm=9b3cb9c1ac4b30d7bbd44057b181f87541f5904d24f903494ae557e768ae00c208c1b68b45c7&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[手把手教你做单细胞测序数据分析|3.单样本分析(2023年重置)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500010&idx=2&sn=2f9fd1b0101d579bcd250fdc24e98bfc&chksm=9b3cb9baac4b30ac6f0ce28a6dd10470e73d1e1d6defece5636939a32a6db9b2cce0ff8688eb&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[手把手教你做单细胞测序数据分析|4.多样本整合(2023年重置)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500117&idx=2&sn=cef0b0abec6d73a8c2615980ef68aec1&chksm=9b3cb805ac4b3113fdc820b9c9667f9554b2e39f90c45b5806021a415698b0a5141c521c64dc&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[手把手教你做单细胞测序数据分析|7基因集富集分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500357&idx=2&sn=40034079b771c478b482e849ed4b216c&chksm=9b3cbb15ac4b3203d517ff71073ab0520fe144bc108b7a26f6b17e88fb63a78c5777946618e3&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[SCENIC单细胞转录因子预测|2.学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500439&idx=1&sn=d6b4874a8352f5b7a4165629c03058ce&chksm=9b3cbbc7ac4b32d158fd3c5c2f155c54c892d40eaae3718409936fc319f69705da32badf79d6&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[scRNA-Seq学习手册2023_R语言版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500516&idx=1&sn=3c0b9de505fcd232054e38b451fa1742&chksm=9b3cbbb4ac4b32a26b61f3a1f7941fff5852d3e6e744ec680aafd0b84ec976a33bf982fb5f79&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[单细胞复写|3.急性心肌梗塞(AMI)外周血scRNA-Seq分析实战(链接重置)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501145&idx=2&sn=12c2e8d104ad343fc13acb8cda266e6c&chksm=9b3cbc09ac4b351f4ed708a0ed577a21f48ccb0d4173aed94a027b4170147ab85931ee51d1e5&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[SCENIC单细胞转录因子预测|4.精简版流程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501260&idx=1&sn=f1e2a165599e753e2959aad7c8a298cb&chksm=9b3cbc9cac4b358a9499654a2f95fa9010309ee4f408ef8b1f31ceb1a0f263ce22e8b511c430&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《细胞通讯》2.CellChat基础分析教程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501296&idx=2&sn=fb3e252d95ee8b50cd446e71335b1aa0&chksm=9b3cbca0ac4b35b621b4f51d2c3a130f00461faeeff067396222c2fc2eeb53f3544664d7d9bc&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《细胞通讯》2.2CellChat多组别分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501523&idx=2&sn=6fa803f256c2e0b945f93ae7d8245f50&chksm=9b3cbf83ac4b3695b587e9817840f419104c8680f5ef08ee39aa149b79852f48b179f68e3397&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《拟时序分析》3.monocle2实操：完整版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501684&idx=2&sn=45c8b083e1094718d7fc4b97e370b01d&chksm=9b3cbe24ac4b3732e6eb04084fe3af4419c817755e4eb9a11ba1fb9f68488d12fe7bc865ad0b&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[《细胞通讯》CellChat学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501735&idx=2&sn=35fc792961507f4ae1cbae3a2882fba6&chksm=9b3cbef7ac4b37e1417d4108c8bd378c68c3907431ddfc52ad37c916e85649bb450d761a8e19&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[ComplexHeatmap学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503470&idx=1&sn=81b5142c5c4f1af9ae87bdc480d5469b&chksm=9b3cb73eac4b3e285467305c2a8d08b07d8b56d85bce96bd978c422d1f22b2c0dad0ed1dc752&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[沉浸式统计细胞比例](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&chksm=9b3ca933ac4b2025f922a325ec6893e93613f130ff1d4fd609e2d7274f7f1fdb5134092e28ad&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[VlnPlot的ggplot改造](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=1&sn=b795a3e36ae092d8f87abb5a87187828&chksm=9b3caa9bac4b238dd33e905c33924b58aa4ff14e83abbf08046fba7fe765ecb0204163cb6acf&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[scRNA-Seq学习手册Python版](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504877&idx=2&sn=2b56a9cfa19fcc918ee6c2ed88fed017&chksm=9b3caabdac4b23ab6e28425a4a5eb4d40ee3612e51f84f5d1e53ac91bef93f717e9e754398e3&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[空间转录组学习手册合辑](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505088&idx=1&sn=9f60dca1b21f5ba8c32d09595a512134&chksm=9b3cad90ac4b2486820dd335d997d2a96b77beb6ad463b1df6a2f307e47ebe8d7de3304ebf7c&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[Seurat空间转录组学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505213&idx=2&sn=6b9aad43c273009c3d7f80c63bb9f619&chksm=9b3cac6dac4b257b8fca1980fd5437ce131dd26377eeef8614d09c11a7ee22ed771cbf323a60&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[Scanpy空间转录组学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505248&idx=2&sn=18995c7248ca6f13b61edfef24208ae1&chksm=9b3cac30ac4b2526050f91dd431bef96ab3dfbdc1a20b3dac32daa5138c11ceb8781b14a2bcd&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[Stereopy空间转录组学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505686&idx=2&sn=925ce770136ec3e964b954c639eed29e&chksm=9b3cae46ac4b2750f4c9f6d249d82257047334d7a7d5642288f5c2f909c51c934d692032eaa0&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[Squidpy空间转录组学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505844&idx=2&sn=5756c0702d080d6e602c504e7d461013&chksm=9b3caee4ac4b27f268c5f7cd39b6a1cbc138e465a6375c26c9a49b31697b63a4af2f702ec6b2&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[影像组学学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505914&idx=2&sn=c0065d26b1cb1763f03534d808bae713&chksm=9b3caeaaac4b27bca2fd20e9a19492b9d4d20e2adeb1c96f1648afcb29b7b20f9db87aedded1&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[R语言基础学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506720&idx=1&sn=fe897ba3c33a8e63bf6a4e35aeac1896&chksm=9b3ca270ac4b2b66812aa311757bd15f28172a86215537f21a6fe3c7e96215a536bdab025bb8&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[一文搞定空间转录组与单细胞测序的整合分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507210&idx=1&sn=f32037ffefd60b0d1bcca7bf9c3e0823&chksm=9b3ca45aac4b2d4cf0c68299db3a2891130d89d9e0fe2a9ecb34b394736550bcf7d7c51090cc&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[基于深度学习的图像分类任务](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507794&idx=1&sn=c70dd03a962adb3f3b92ffed47e978bb&chksm=9b3ca602ac4b2f1499838f7aa6f02de182921362dff124c98a65079ba900125f7695665ef5cc&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[2023订阅用户反馈调查](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507960&idx=1&sn=5a718d6aabf494a3387292fd5038e88f&chksm=9b3ca6a8ac4b2fbec471a40d42ddf882d752777be474313e625c7a3f7e001a360606de743b14&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

[2023订阅资料已完结~](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247508123&idx=1&sn=5211090a5013a94695d899d844cfe23e&chksm=9b3cd9cbac4b50dd65bbae0f76519bc670acb429b5ae3016d02e0474b19ed9bd2e1035a36b32&token=2143911808&lang=zh_CN&scene=21#wechat_redirect>)

**
**

**终身订阅持续更新中~~~**

![](../../images/7ec68c571f447e25.webp)

**
**

**
**

![图片](../../images/f74ae4c6b8127d36.webp)
解锁前需阅读：[ 龙年订阅须知](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247509093&idx=1&sn=d82ed3738bc25b922a4837016198951e&chksm=9b3cdd35ac4b5423f08cf6ab2f4afc5d815c2321991d880e8b7162e63fd1d7e4695cd7391022&scene=21#wechat_redirect>)![](../../images/399758fa7d6941c2.png)

联系客服微信获取提取码

![](../../images/fbfc4b8be383f432.png)![](../../images/007e970626afa0b7.png)单细胞Figure 1常见图表

链接:https://pan.baidu.com/s/1FcyC_AkC5FZN-fixflxZ5A

提取码请联系客服微信[Biomamba_zhushou]领取

云盘中包含以下内容![](../../images/2423e3ec9dbc5062.png)

**-Biomamba**
![](../../images/7d247e6c6ef19f87.png)
![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532585&idx=1&sn=e265d2846ec66e5faaaf21403d274d2f&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/0afa34cf8c4b5e66.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
