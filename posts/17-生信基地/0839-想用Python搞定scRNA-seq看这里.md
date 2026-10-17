---
title: "想用Python搞定scRNA-seq看这里"
date: 2025-10-29
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531916&idx=3&sn=0650f170de65704821a1e5bd478d0934&chksm=9b3c04dcac4b8dcae2f86cf93fbfc715d1cca8f8f971a13a65da2c3a2c7a771bf9a7cb6f3d3f#rd
albums: ["生信基地"]
---

# 想用Python搞定scRNA-seq看这里

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531916&idx=3&sn=0650f170de65704821a1e5bd478d0934&chksm=9b3c04dcac4b8dcae2f86cf93fbfc715d1cca8f8f971a13a65da2c3a2c7a771bf9a7cb6f3d3f#rd
> 合集：生信基地

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=0)

写在前面

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=1)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=2)还在用 [R 做单细胞分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=2&sn=04d3798dc60958af2c9020fe7c4bd9b8&scene=21#wechat_redirect>)？[还在用R语言硬干一百万单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531160&idx=1&sn=ecf56af3b929ec2b241854c89d25c671&scene=21#wechat_redirect>)？现在你有更高效、节省内存与时间的选择！Biomamba生信基地现推出[scRNA-seq数据分析 Python 全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531221&idx=1&sn=2346109f4cf6d3398dd15351474edf95&scene=21#wechat_redirect>)——更强大的生态，更易扩展的工具包，还能无缝衔接机器学习与可视化。从基础到进阶，带你解锁Scanpy、scVI、PyTorch等前沿库，深入掌握真正高效的单细胞分析工作流。
2025.10.20~12.11，为期两个月（线上/线下均可参与，错过直播也可以加入录播/答疑+循环开课）。[生信基地](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247526229&idx=1&sn=0718f1702150ba77a7f7e3beadd6e0ba&scene=21#wechat_redirect>)希望能够做到“手把手”的带大家完成数据分析学习，当然，我们拒绝生信快餐，课后欢迎大家随时在群里对课程内容提问~后台回复关键词“全程班”，可以获得最新培训集锦
参与此次课程你将获得：1、为期两个月单细胞转录组数据分析教学。2、加入全程班群聊，三年内当前课程的指导、答疑、回放、直播复听，相信足够覆盖你的硕博生涯学习。2、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)，256GB内存、512GB硬盘、20线程服务器3个月使用权。4、课程对应分析手册、代码、测试文件。
通过两个月的学习，你能够绘制上百种单细胞转录组图表，以下为部分图片集锦：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxm0gibfGROlnrHmxiaCX4yspXzKLvp5qlmmkjhTKibQrzU6D4iaUljak5pLXK5y8Qfv5WgVic9Sy11ebw/640?wx_fmt=png&from=appmsg)

**报名联系客服微信[ Biomamba_zhushou]：**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=6)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=7)

内容计划&大纲

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=8)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=9)以下是我们此次课程的时间安排：![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpxm0gibfGROlnrHmxiaCX4ysp58qmwPl9URaRUEz1kWmn6IeWadU1C8zXTnx1G9Kpzic9ffib7jGdQdlg/640?wx_fmt=png&from=appmsg)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=13)

**所见即所得**

通过这次全程学习，你将获得并掌握以下学习手册与资料：

Linux基础课学习手册

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=14)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=15)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4s9ld2icJKcIxyuzEeia8VPPo6vgribeVU5VYkXquccov1QAGtoGOiaUAOWQ/640?wx_fmt=gif&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=17)

Python基础课学习手册

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=18)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=19)同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4sIvegmIUAoK2BvTM5SMwF35oLRu21nUhQR1zyiaXtISvNwK5wm2y8XAg/640?wx_fmt=gif&from=appmsg)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=21)

单细胞-基础分析学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=22)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=23)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4FnOtCWYc7G4QxnX2coj0v8VrdhOsy59Hq3Jut6PRchZLoQ0CLOcUvHRg/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4sQ9yXDJsOB0RV6aCRoS7tUsuzwj3e5sR8ib2pXpynK8zoq7iamK6smJUQ/640?wx_fmt=gif&from=appmsg)

教程目录：零、欢迎关注一、准备工作1.1 jupyter安装1.2 python库安装1.3 结果导出二、不同类型单细胞数据提取2.1 10x标准三个文件格式2.2 单个表达矩阵2.3 h5ad文件三、认识adata3.1 X数据槽3.2 Layers数据槽3.3 obs数据槽3.4 vars数据槽3.5 obsm多维注释信息3.6 obsp配对数据的存储与操作3.7 非结构化数据的存储四、单样本分析4.1 数据下载4.2 加载库4.3 数据读入和对象创建4.4 数据质控与可视化4.5 细胞分群4.6 差异计算4.7 细胞注释4.8 分群后的可视化五、多样本分析5.1 数据读入和对象创建5.2 数据质控及可视化5.3 细胞分群5.4 批次效应 5.4.1 不去批次 5.4.2 BBKNN去批次 5.4.3 ingest去批次 5.4.4 harmony去批次六、细胞注释6.1 手动注释6.2 常见marker数据库6.3 自动注释 6.3.1 库加载 6.3.2 数据读入 6.3.3 自动注释七、分类变量处理八、差异分析8.1 数据读入8.2 两组之间差异计算8.3 批量差异分析8.4 差异基因可视化8.5 提取基因表达量，用matplotlib 绘制箱线图九、富集分析9.1 数据准备9.2 GO富集分析9.3 KEGG富集分析9.4 GSEA富集分析 十、细胞比例统计10.1 数据准备10.2 饼图10.3 甜甜圈图10.4 柱形图10.5 堆积柱状图10.6 箱线图十一、可视化11.1 降维展示11.2 marker基因展示 11.2.1 气泡图 11.2.2 小提琴图 11.2.3 矩阵图 11.2.4 热图 11.2.5 track图 11.2.6 拼图11.3 diff基因展示 11.3.1 气泡图 11.3.2 小提琴图 11.3.3 矩阵图 11.3.4 热图 11.3.5 track图11.4 聚类及相关性十二、软件版本十三、单细胞教程全收录十四、欢迎致谢

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=27)

单细胞-进阶分析-轨迹分析学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=28)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=29)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4FnL43yFicwCw1b2AFqZCZTy22tD0X3E8vlMEdduMD1icGaKh8LOMV0r6cQ/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4spDEOgwJNnOMAyicsYYartxicsyEWd2ib7B6HMgKZPBrB8AD2nlhjC0Otg/640?wx_fmt=gif&from=appmsg)**教程目录** ：零、欢迎关注一、前言1.1 定义1.2 拟时序分析作用1.3 不同拟时序软件的比较1.3.1 总体评价结果1.3.2 准确性1.3.3 可扩展性1.3.4 稳定性1.3.5 软件、文档和手稿方面的可用性二、准备工作2.1 环境准备 2.2 库准备三、palantir3.1 文献解读 3.1.1 摘要 3.1.2 结果 3.1.3 小结3.2 数据读入3.3 预处理3.4 可视化 3.5 运行Palantir 3.5.1 获取细胞坐标 3.5.2 定义分化起点和终点 3.5.3 拟时间推断3.6 下游分析 3.6.1 细胞分化概率统计 3.6.2 展示不同细胞分支 3.6.3 基因随轨迹变化趋势分析 3.6.4 基因表达模式聚类3.7 联合scanpy分析 3.7.1 表达模式聚类结合富集分析 (1) 差异基因鉴定 (2) 表达模式聚类 (3) 富集分析 3.7.2 降维图 3.7.3 小提琴图 3.7.4 细胞比例展示 3.7.5 密度分布图四、PAGA4.1 文献解读
4.1.1 摘要 4.1.2 结果 4.1.3 小结4.2 pbmc3k数据实操 4.2.1 数据读入 4.2.2 数据预处理 4.2.3 运行PAGA 4.2.4 可视化 4.2.5 重新定义发育起点4.3 人骨髓数据实操 4.3.1 数据读入 4.3.2 数据预处理 4.3.3 运行PAGA 4.3.4 可视化 4.3.5 重新定义发育起点4.4 联合scanpy分析 4.4.1 拟时间降维图 4.4.2 小提琴图 4.4.3 细胞比例展示 4.4.4 密度分布图4.5 小鼠髓系数据实操五、RNAvelocity5.1 文献解读 5.1.1 摘要 5.1.2 结果 5.1.3 小结5.2 数据下载 5.2.1 bam文件 5.2.2 repeatmask文件 5.2.3 gtf文件5.3 loom文件准备5.4 RNA速率分析 5.4.1 导入loom文件 5.4.2 导入细胞降维坐标和分群文件
5.4.3 轨迹推断 (1) 数据过滤和归一化 (2) 计算表达均值和方差 (3) 计算RNA速率 (4) 构建RNA速率图 (5) 在UMAP降维空间可视RNA速率方向 (6) 在UMAP降维空间以流场形式展示RNA速率方向5.5 下游数据挖掘 5.5.1 关注基因可视化 5.5.2 鉴定重要基因 5.5.3 细胞周期分析 5.5.4 RNA速率的置信度 5.5.5 潜在时间(latent time)分析 5.5.6 Cluster-specific top-likelihood 基因六、软件版本七、单细胞教程全收录八、欢迎致谢

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=33)

单细胞-进阶分析-细胞通讯分析学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=34)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=35)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：

![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4FncanWicNhXgkM0l45icYfhFbibM2kd0q0S2GzY8uMlXqDjR3etAWZrV7vA/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4sX8Nx9srUjkBSVEzSEbdODtyy6SwKdR9uq6AiaRibHXldLRqsTwp9NJNg/640?wx_fmt=gif&from=appmsg)

**教程目录** ：

**零、欢迎关注**

**一、前言**

**1.1 定义**

**1.2 互作预测过程**

**1.3 不同细胞软件的比较**

**1.3.1 基于规则的工具**

**1.3.2 基于数据的工具**

**1.3.3 混合模型**

**1.3.4 其他分支**

**1.3.5 实验追踪细胞间相互作用**

**二、CellPhoneDB文献解读**

**2.1 摘要**

**2.2 数据库概述**

**2.3 分析方法概述**

**2.4 实际应用**

**2.5 小结**

**三、准备工作**

**3.1 环境准备**

**3.2 库准备**

**四、cellphonedb**

**4.1 下载数据库**

**4.2 构建数据库**

**4.3 输入数据详情**

**4.4 计算方法介绍**

**4.4.1 cpdb_analysis_method.call**

**4.4.2 cpdb_statistical_analysis_method.call**

**4.4.3 cdpb_degs_analysis_method.call**

**4.5 示例代码**

**4.6 示例数据-方法1**

**4.6.1 输入文件**

**4.6.2 互作对预测**

**4.6.3 结果解读**

**4.6.4 思考？**

**4.7 示例数据-方法2**

**4.7.1 输入文件****4.7.2 互作对预测****4.7.3 结果解读****4.7.4 探索CellphoneDB结果****4.7.5 可视化**

**4.8 示例数据-方法3**

4.8.1 输入文件 4.8.2 互作对预测 4.8.3 结果解读 4.8.4 探索CellphoneDB结果 4.8.5 可视化

**4.9 人纤维化皮肤病单细胞数据实操**

**4.9.1 输入文件**

**4.9.2 准备文件**

**4.9.3 互作对预测**

**4.9.4 结果解读**

**4.9.5 探索CellphoneDB结果**

**4.9.6 可视化**

****五、软件版本********
********六、单细胞教程全收录********七、欢迎致谢********
****![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=39)

单细胞-进阶分析-共表达网络分析学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=40)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=41)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：

![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4Fn8eIovYicGkGvV2EfUyIDpFDTE2sKBx9Bsx72lgqn1rwbN2wjLV78Uog/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4sc1qjsgl77f6LUA46VtsnpHQ5VGMxI0ktE9ibBAmoJ02l9BvbUicCJgWA/640?wx_fmt=gif&from=appmsg)

**教程目录** ：

**零、欢迎关注**

**一、前言**

**1.1 研究背景**

**1.2 主要结果**

**1.3 小结**

**二、准备工作**

2.1 环境准备2.2 库准备

**三、基于表达相关性**

3.1 数据准备3.2 相关性计算3.3 图形可视化

**四、基于Kmeans聚类**

4.1 数据准备4.2 模块划分4.3 图形可视化

**五、基于pyscenic******
****

****5.1 文献解读****

****5.1.1 SCENIC工作流程****

****5.1.2 在小鼠脑组织的应用****

****5.1.3 在复杂癌症中的应用****

****5.1.4 在黑色素瘤中的应用****

****5.1.5 小结****

****5.2 数据库下载****

****5.3 loom文件准备****

****5.4 运行pyscenic****

****5.5 下游分析****

****5.5.1 基因aucell降维****

****5.5.2 vlnplot****

****5.5.3 umap****

****5.5.4 dotplot****

****六、软件版本********七、单细胞教程全收录********八、欢迎致谢****
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=45)

单细胞-进阶分析-拷贝数变异分析学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=46)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=47)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：

![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4FnxMO9tfhRhh1rbUGgkITfgB73Y5FAvia6QkTdk8yw99JR5yBcicchWyTA/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4spshfw4RwXYibM9cjVJMEh7gmTRrOfibSSM5g7nKfibVM3bLFA32M5PWPg/640?wx_fmt=gif&from=appmsg)

**教程目录** ：

**零、欢迎关注**

**一、前言**

1.1 研究背景1.2 主要结果1.3 小结

**二、准备工作**

2.1 环境准备2.2 库准备

**三、infercnvpy**

3.1 数据下载 3.2 参数详解3.3 运行infercnvpy3.4 计算每个细胞的cnv分数3.5 可视化

**四、通过CNV谱进行聚类并识别肿瘤细胞**

4.1 cnv聚类分群**
**

**4.2 cnv展示umap**

**4.3 scanpy展示cnv结果**

**4.4 肿瘤细胞分类**

**4.5 肿瘤和正常细胞分开绘制热图**

**五、内嵌copykat**

**5.1 数据读入**

**5.2 参数详解**

**5.3 运行copycat**

**5.4 计算每个细胞的cnv分数**

**5.5 可视化**

**5.6 通过cnv谱进行聚类并识别肿瘤细胞**

**5.7 肿瘤和正常细胞分开绘制热图**

**六、**对比R版本的infercnv****

**七、如何获取基因在染色体上的位置**

****八、软件****版本************九、单细胞教程全收录********十、欢迎致谢****

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=51)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=52)

单细胞-文献复现学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=53)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=54)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

原文集锦：

![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4Fn2ELrN1qMONvpZNmQcMBlPcMaaph8LhlGrLpJpDaBMcLyrOpxGibIvHg/640?wx_fmt=png&from=appmsg)

复现图片集锦：

![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4FnpCgNgSk9H2ofZ8WKJbpJdcib598WnUjwrhshpbRfASzSbZDxjb2OFibw/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4sHkOo3Vdrfn4f4qXajVCedDCpnWzqFI9zzGPmQHAgKrhAzdP2WGtdfA/640?wx_fmt=gif&from=appmsg)

**教程目录** ：

**零、欢迎关注**

**一、文献解读**

**1.1 背景介绍**

**1.2 主要内容**

**1.3 总结讨论：**

**二、数据下载**

**三、数据整理**

**四、细胞注释**

**4.1 降维图**

**4.2 小提琴图**

**五、降维展示**

**六、细胞比例统计**

**6.1 整体统计**

**6.2 免疫细胞**

**6.3 非免疫细胞**

**七、上皮细胞肿瘤细胞鉴定**

**7.1 数据准备**

**7.2 参数详解**

**7.3 运行infercnvpy**

**7.4 计算每个细胞的cnv分数**

**7.5 可视化**

**7.6 通过CNV谱进行聚类并识别肿瘤细胞**

**7.6.1 cnv聚类分群**

**7.6.2 cnv展示UMAP**

**7.6.3 scanpy展示cnv结果**

**7.6.4 肿瘤细胞分类**

**7.6.5 单独绘制肿瘤细胞**

**八、上皮细胞轨迹分析**

**8.1 降维分群**

**8.2 预处理**

**8.3 可视化**

**8.4 运行Palantir**

**8.4.1 获取细胞坐标**

**8.4.2 定义分化起点和终点**

**8.4.3 拟时间推断**

**九、上皮细胞EMT评分**

**十、CD8T轨迹分析**

**10.1 T细胞注释**

**10.2 CD8 T细胞注释**

**10.3 预处理**

**10.4 可视化**

**10.5 运行Palantir**

**10.5.1 获取细胞坐标**

**10.5.2 定义分化起点和终点**

**10.5.3 拟时间推断**

**十一、上皮细胞互作分析**

**11.1 数据预处理**

**11.2 互作对预测**

**11.3 结果解读**

**11.4 探索cellphonedb结果**

**11.5 可视化**

**十二、软件版本**

**十三、单细胞教程全收录**

**十四、欢迎致谢**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=59)

单细胞-AI自动注释学习资料

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=46)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=47)

同我们以前的课程一样，我们给大家准备了学习手册和学习资料，大家可联系客服微信[Biomamba_zhushou]领取：

教程图片集锦：

![](https://mmbiz.qpic.cn/mmbiz_png/7sbgt88Kkk41tzbGZGZdcaK2gicZlH4FnznnmNiauYqibJ7iaM0lS3GPfwnOEhBkbfJYE5RtdrOBFIZvZibzE46tzCQ/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpyWickSUZ4vtVVheYIHtmib4sMwHYac5PYPDmDTTgAm7whGanlkG5hibU6kMia11GPwlWf1Fdxc1ClemA/640?wx_fmt=gif&from=appmsg)

**教程目录** ：

**零、欢迎关注**

**一、准备工作**

**1.1 环境准备**

**1.2 加载库**

**二、CellTypist**

**2.1 下载测试数据**

**2.2 CellTypist内置模型注释**

2.2.1 模型下载 2.2.2 模型选择 2.2.3 参数解读 2.2.4 开始预测 2.2.5 结果查看 2.2.6 一致性比较

**2.3 自定义模型进行注释**

2.3.1 准备训练集和查询集 2.3.2 参数解读 2.3.3 模型训练 2.3.4 开始预测 2.3.5 结果查看 2.3.6 结果一致性比较 2.3.7 查看模型驱动基因

**2.4 CellTypist进行多标签分类**

**2.4.1 数据下载**

**2.4.2 内置模型+best match模式**

**2.4.3 内置模型+prob match模式**

**2.4.4 自定义模型+prob match模式**

**2.4.5 检查模型驱动基因**

**2.5 大规模跨数据集应用**

**2.5.1 数据下载**

**2.5.2 数据预处理**

**2.5.3 训练集的特征选择**

**2.5.4 开始预测**

**2.5.5 结果一致性比较**

**三、scVI**

3.1 基础设置3.2 功能介绍3.3 滤泡性淋巴瘤细胞 3.3.1 数据下载 3.3.2 模型预测 3.3.3 结果查看 3.3.4 一致性比较3.4 HGSC数据 3.4.1 数据下载 3.4.2 模型预测 3.4.3 结果查看 3.4.4 一致性比较3.5 scANVI种子标记 3.5.1 数据下载 3.5.2 根据marker注释部分细胞 3.5.3 模型预测 3.5.4 一致性比较3.6 外部数据验证 3.6.1 数据准备 3.6.2 准备二值化矩阵 3.6.3 模型预测 3.6.4 结果查看 3.6.5 一致性比较****四、****环境版本信息************五、单细胞教程全收录********六一、欢迎致谢****

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=51)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=60)

报名费用

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=61)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=62)

两个月的课程，单个只要4999￥！详情咨询客服微信[Biomamba_zhushou]

有其它任何想法的同学也欢迎随时联系我们，更欢迎看看我们的价值观：[想钱想疯了？](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529315&idx=1&sn=df2cf4c0fa3411889c558229f4068a8c&scene=21#wechat_redirect>)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=63)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT4fWv4qtNOib05eia9YjiaabjHRtwFYQOf0ed7ZbssruN898rzEHiciaFN3g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=64)

线下学习环境

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTZ0PAotm6HriciaNkJfsbicJA31YqibhSZOAIfxNibE0blibyPGNkLiadxwzMg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=65)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJTEibOfQmUibFo1TWGFrZ8LI3j3ZN9qAx7HgOkrkI8sgwEbqpVH4MBDESg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=66)**地点** ：南京市江宁区，详细地址咨询客服微信[Biomamba_zhushou]**
****往期活动现场：****![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpzlCHzM8BicyYndroTyAQWjdruGL35Ag8TpUeJAQzletw5eYbMYeTOyyQSF3t55PV3YyjZZqMa2aFg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=67)**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpxibFIAuWYlaOkdLntmib4WaTJBFK3VicGPmAqicxO5qvVOTRU3llPCjgBw09FkStwTSCPS6siaOgWzibmQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=68)

除了知识之外，现场还能够给大家提供：

**茶水吧、咖啡机、零食柜**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyJTurcWOC9GGd5VvBqk9u2PaQSvDhnu7UJibZ5RibWO6RpkHjQH9kAtbU9miaGlhuZRQlqDYRwa3yTA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=69)

**各类饮料、零食小吃**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpznttzoqtuQBeRAM4tHRweMzv4icM7ia0OzZS1VashvPOYmuWOVuGhpvRsGibakVZPf6HQjMgEXagiaxQ/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=70)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiadRtBxBtRH1nZ4ZpFgkFJT9Zzd1lKB0SwRxGa2K2TFUMTLxa4y2FeHzUy5ARvwyD3mVwFloGqhww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=71)![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=22) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&tp=webp#imgIndex=24) 您点的每个赞和在看，我都认真当成了喜欢
