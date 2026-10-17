---
title: "UNAGI做个时间序列分析，顺便把药物干扰给预测了"
date: 2026-04-29
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537658&idx=1&sn=a4cb5c4626986f7f78dfa6419b4e7365&chksm=9b3c2aaaac4ba3bc8e76824830dbb2571fd8cf3cedeaf6e103afd5bdf53b5ef6188a45126ed6#rd
albums: ["单细胞教程全收录"]
---

# UNAGI做个时间序列分析，顺便把药物干扰给预测了

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537658&idx=1&sn=a4cb5c4626986f7f78dfa6419b4e7365&chksm=9b3c2aaaac4ba3bc8e76824830dbb2571fd8cf3cedeaf6e103afd5bdf53b5ef6188a45126ed6#rd
> 合集：单细胞教程全收录

**一、写在前面**

UNAGI是一种深度生成神经网络，专门用于分析时间序列单细胞转录组数据。该工具捕捉了疾病进展背后的复杂细胞动态，增强了药物扰动建模和筛查能力。当应用于特发性肺纤维化患者的数据集时，UNAGI学习到疾病知情的细胞嵌入，加深我们对疾病进展的理解，从而识别潜在的治疗药物候选。作者利用蛋白质组学验证了UNAGI细胞动力学分析的准确性，而使用纤维化混合剂的人体精切肺切片也证实了UNAGI关于硝苯地平（一种降压药物）可能对人体组织具有抗纤维化作用的预测。UNAGI的多功能性延伸至包括新冠在内的其他疾病，展现出适应性，并证实其在解码特发性肺纤维化以外复杂细胞动态中的更广泛应用，进一步扩大其在多样病理领域寻求治疗解决方案的应用。简单来说UNGAI可以对单细胞数据进行时间序列分析，并预测时间序列中的药物与基因干扰。 测试文件与学习手册见文末。

原文链接：

https://www.nature.com/articles/s41551-025-01423-7
代码参考：

https://github.com/mcgilldinglab/UNAGI/blob/main/tutorials/run_UNAGI_using_example_dataset.ipynb

更多Python单细胞分析技巧可见：

[![](https://mmbiz.qpic.cn/mmbiz_png/ImlBFVOwwpwt8dqWwuyfAweQtO809MKBzrWa3NBR1wibO6UUsWibmjia0Efw7wDiczrFtJjSAyBia6V6KGtVicx17gNw/640?wx_fmt=png&from=appmsg)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)指导、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469&token=1729645779&lang=zh_CN#wechat_redirect>)、自测数据个性化分析辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]。

**二、实操流程**

```
如果你的计算资源不够用。不妨看看：
```

[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=2&sn=4708fac31ac8f4e347847e4b7f2a4fed&scene=21#wechat_redirect>)

[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21&token=1904068475&lang=zh_CN&poc_token=HF-eN2mj01zsfxe_I4r8D5pfZx80xO2AVYSB6qtT#wechat_redirect>)

[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)

访问链接：https://biomamba.xiyoucloud.net/
```
1.安装
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
conda create -n unagi python=3.10conda activate unagipip install scUNAGI -i https://pypi.tuna.tsinghua.edu.cn/simple# 有一个比较恶心的事情，大家需要修改一下这个脚本的源码# 从github上克隆包相关文件git clone https://github.com/mcgilldinglab/UNAGI.gitcd UNAGI# 在本地安装一遍矫正一些包的冲突pip install ./locate UNAGI_analyst.py # 定位脚本位置# 修改定位到的脚本，下面要换成你自己的路径sed -i '10d' /home/biomamba/miniconda3/lib/python3.9/site-packages/UNAGI/UNAGI_analyst.py # 会用vim的同学也可以手动删除这行内容：from VTK.IO.Xdmf3.Testing.Python.VToXLoop import raiseErrorAndExit# 如果上面这个问题不解决，你会遇到这个报错：ModuleNotFoundError: No module named 'VTK'# 并且，numpy的版本需要<2.0，否则会遇到这个报错：AttributeError: `np.string_` was removed in the NumPy 2.0 release. Use `np.bytes_` instead.pip install numpy==1.26.4 --force-reinstall# 安装特定版本的torch组件，否则会提示显卡驱动版本不兼容pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu128
```

另外还需要依赖`idrem`库完成可视化，我已经在本地给大家下载好了，大家可以随手册一起下载

2\. 测试数据集演示

本章节将逐步介绍如何使用`UNAGI`配置模型架构、调整训练参数以及对时间序列单个数据集进行分析。我们通过将`UNAGI`应用于从snRNA-seq数据，并演示`UNAGI`的基本功能。

  *   *   *   *   *   *   *

```
# 以下包都需要能正常导入：import warningsimport scanpy as scimport oswarnings.filterwarnings('ignore')import warningsfrom UNAGI import UNAGI
```

2.1 初始化并加载数据集

加载好UNAGI之后，第一步就是要设置数据分析参数，UNAGI可以直接加载`h5ad`数据，不明白这部分内容的可以参考[一文了解Python中的单细胞通货：AnnData](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528513&idx=1&sn=1ff1b8bee321f8f5bcac425ce96dc6ff&scene=21#wechat_redirect>)。`UNAGi`需要一个拥有时间序列作为输入的数据，这个数据保存在annData.obs中，这个数据需要包含KNN连接矩阵(单细胞数据处理可见：[告别R依赖！一文搞定Python单细胞基础分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534702&idx=1&sn=f1531163f8f620b59cf63dfaa1c03e67&scene=21#wechat_redirect>))。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
#提交脚本samples=("Amp-3219" "Amp-3588" "Amp-6762_combined")count=1for sample in "${samples[@]}"; do    id="S${count}"    echo "Submitting $sample with ID $id ..."    qsub /data/CRCdata/WES/add_label.bash $sample $id    count=$((count + 1))doneimport warningsimport scanpy as scimport osadata = sc.read_h5ad('./UNAGI-main/UNAGI/data/example/0.h5ad')adata.obs['stage']
```
```
145_94_D__CAACAGTTCCAAGCCG     0
```
```
221_45_Db__TCCATCGAGGCTCACC    0
```
```
248_111_D__GTAACACAGGCTATCT    0
```
```
145_21_Db__ACAGCCGGTGGTCTGC    0
```
```
248_111_D__GGTGTCGCAATACCCA    0
```
```
                                                            ..
```
```
221_35_Db__GTGACGCGTTTACACG    0
```
```
302_11_D__GAAGCCCGTTCATCTT     0
```
```
145_22_D__CTTCGGTCATGTACGT     0
```
```
145_21_Db__AGATGAAAGGGAGGTG    0
```
```
94_124_D__CCCAACTTCGTCGATA     0
```
```
Name: stage, Length: 13550, dtype: int64
```

  *   *

```
# 看一下这个adata的全部注释信息：adata.obs
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnQNWgiaYd0bc8bVJa3hhoMSLWnOQC2NBNpeS1M4hz6vKyzfiaH7MLoaDveSq9OibibribnpJZiciaxu3CKibb0h2IdTbyEOPfPzICrlZg/640?wx_fmt=png&from=appmsg)

13550 rows × 31 columns

  *   *   *

```
# 看一下包含的细胞类型：adata.obs['ident'].unique()# 可以看出这是个肺部的数据
```
```
['VEcapillary', 'VEarterial', 'PericyteAlveolar', 'VEaerocyte', 'VEvenous', 'FibroblastAlveolar', 'SMC', 'FibroblastAdventitial', 'VEaerocyte/VEcapillary/FibroblastAlveolar', 'LymphEndo'] Categories (10, object): ['FibroblastAdventitial', 'FibroblastAlveolar', 'LymphEndo', 'PericyteAlveolar', ..., 'VEaerocyte/VEcapillary/FibroblastAlveolar', 'VEarterial', 'VEcapillary', 'VEvenous']
```

  *   *   *   *   *   *   *   *   *

```
# 实例化unagiunagi = UNAGI()# 预处理h5ad文件：unagi.setup_data('./UNAGI-main/UNAGI/data/example/0.h5ad',# 单细胞的h5ad文件，注意，unagi会在这个路径下生成临时文件夹（样本名文件夹与，model_save文件夹），因此同一时间运行多个unagi，最好放在不同的目录下                 total_stage=4,# 时序结果的总序列数                 stage_key='stage',# 生成的时间序列在adata.obs中的名称                 threads=20# 默认参与计算的线程数                 )unagi
```
```
Fast mode enabled!
```
```
 Cell graphs found, skipping cell graph construction!
```
```
<UNAGI.UNAGI_tool.UNAGI at 0x7f2014bd12d0>
```

2.2 确认模型结构与超参数

`run_UNAGI`的输出日志会很长，用jupyter学习本教程的同学可以点击左侧的导航栏向下跳转。 我的演示设备中CPU是`Intel Xeon Platinum 8383C`、GPU是`RTX5990`，大约花费20min。

  *   *   *   *   *   *   *   *   *   *   *   *

```
# 设置训练参数：unagi.setup_training(task='example',# 任务名称                     dist='ziln',# 当前单细胞数据的分布模式，可选的有：'ziln' (zero-inflated log normal), 'zinb' (zero-inflated negative binomial), 'zig' (zero-inflated gamma), and 'nb' (negative binomial)                     device='cuda:0',# 指定显卡                     GPU=True,# 是否启用GPU加速                     epoch_iter=5,# 第二轮循环开始，每轮的训练epoch数                     epoch_initial=1,# 第一轮的epoch数                     max_iter=3,# 训练三轮大循环                     BATCHSIZE=560 # 最小的批次大小                     )# 训练：unagi.run_UNAGI(idrem_dir = './iDREM')# 需要有idrem库，否则可视化内容无法生成
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwkVsh3NVVAWZ9xsgMqUtOvLJhBAXRDicd5xjiaPAUKrWIUImFSQJarE6brFgiar0hjXvV4paWC7dC1kEPgfYTjKEKv4m6ibCv1jxUU/640?wx_fmt=jpeg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmLnppZ9er0uXbss26318OcIMZdrLvneP63lAKyCKkzU7wJ17gib6nIScWPyFguvbSCeQTpuC1GAdGSvGCPCmNTvHWrojFn8q8I/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkZMIX450LK6Qj3MhQkNMqQvreO1F5VKu6ia9qXZtppicU92mtJCLLlf4FREuXcPAhca7UuJQsicTjv1IcK7ZCuCEic3xIZFibRAGibI/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlyziak2PB3NHuXxMqnichz6GA2D4XtT2SWyPLEzGpGb7u6dhj4es1Y5VdpQl3f7nzhiaNAnESbm0b9ZQDqkhUPBITssd720OfOY0/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnzww9PiaYYupW60qKyrpmpRWGXngdwSZS1icdbbMLSbXwbeiacicAr2gSA3e8q8mozE0K0b2UB3Gf4xTYWsLaicvoibPXkfc9yy5zy8/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwk2BrQFNrMRdHiccm2TuFAV42XJqHkpGyBmxCPzjlgzB0bl2FDb5o5jrH2bBaX0fAnAxYEiaffsLMWtKDpL45kp7fvxrfxjyoTwE/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkpD0dcSfbqQOicrMGlo3NDvAnoAHzaQLjm9jgaJf48vn0494y3yDiaCZ1srNYHwLwysBIFOCbR0NBg2qycYxZhbe8NqeeKtCfibk/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnhZvPqD9Q9MkcsFEiaib9F7qYq259dykDuibXuwk4cUO7Y4jFaOVbTUv7aRFyjZ8xeg5nxCNOKybsMlNEc3gdwyZaDsCIOTurDOU/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlqn4sTaHvHAo2eZniajoBGMcicTXk01F5HicssjhJu6l7ymjresuicy1rhVcmfc0w7QcjmmRDz47GurBTapbW6vuzEmB0r5ibVa2l8/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnPRzUs0GibxmHA62j5lBbdrylgtMlByVI17jdMfyPNEjTCTRWcOUuOBdNariaOHql3RRzFz2SfRVt2HqXhZ3HanPD0xOYqXPdmk/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnq6LqQ98xmtG2bRp5CcCvoNq4RB0bv0xRE840ia3mS03sS84e0JG9r5XOic80eiafsL0ic8GDxdGXw8TU8cYf2y8CdGMI4yhau2KM/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmxdTHDhFYhic6FjibEQ3qrFsEEvjym3ibbgwLianoIBC2NZAMzWiayIftwozzvmt4AlCVyiaohX8MWXNJtsToH5GeuLXVygpNGQRPp0/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnaQl16NB9LF8gDopNmwoYewgiafb25yRHlmUPcZd2pMZyyKcHAwceL8P0ISCP4TzCqsSq1V9ibjuWn5ZHiaq6PvDrJ7OicPZ7MrjY/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwk8ia2UCC9iagb2mmuszE3fCU6hSEU6rOHCbhMyraLoTaAfBJbZsORtuu1gHagNDH6OATHDyI28L3IspoHbd1rcfTdJLSz6iaY4JA/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlSppAqbentXY0NsibAHJicg2N66ESLkXyKfKyDzdxicHIwFJXoibWtTdSj7VjibybuJcBDNmiccjFZujQT3hRsgASeyfjiaZZkibWdqDI/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwktqNFq6Kugqj8LqABjP3o97bgksPEehKhwqXZnYAjySnwXTGpVfbxzqert2tn0FvPBehPaN0ezf8MAMcr6JfnbOvibntjbc9g0/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnB6icBczCDfLYdp3elIwZ3mMam3Yo6cOh5pSOjlLbYqvUCmstDmwgNJxJ9Qu84pqibeo7xEvtdTdhxw3z5viafamgBrfhSXZhR3M/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkialc37MiaicPaGicpN9APwDvfAuLrTibAcjXjricOCxPbjicM4VSI6Ma7FJfOECrXmDGOWgwAeM7erp6TOsuwrSicaSIXY1QXtYLFhYE/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlkq1kWnRRbJ8HxB392A4uuicA38DTf9mCaAZFD8nUyZPHRBHS8JeM7cPT20QZVFXXbnlXk6AMIzSUMUeibf4AZGsnb34ibfAboac/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmSzEakCCqWs2J637WgPJicjHAyic8FMt0jAWM2PLFeF9dbSCvBRGibhdABg13qxo0icqH32DKY3hae31PUT0ia45G3R3ibTCVibUWmDY/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkX7xJPTsTbWtgZfEl4sE4VicWzgUOWs7VJibrpNAPpnWvpNjMNQXXYD1pn317Pd7GaQLDkjFnrN7vOiaAtMIkEGyWmKv74hRvKnY/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkYyUuyc2yAeUdbfLKaFTP9YntkblFet29CsOlBibeECe81vULq9ZCKibBVhTh8vAkicMbfkw2wOdTJOAymkrduFXn1TjrFEadfnk/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlOz9QTSy6ribNYIqTYSCWmlksC28Siaticb349SLAibyqaicLsicADA3EibIyozmeqCtUAwVGr2AC5krmEicz6h3lQZm1NFGoZgqY5KtI/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlEemnftpOyZkHicOMsPINN82Zb1EThZg1bRsw2cw0U2LpGhiaW8rb80wVO3afKbkRWTKolFIjiaKria4nQrOJtfLl04k5uToeGILY/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnGxPAHtCogENqwYOY0zfLnQR5hia04LVaVibwGfUXQENmuq8PZ4TicHLU1v23SlwIxTUVWVvblGBE3cibgWficx85u9oMoe6bXqkKM/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmHtSUWBdabPBSPDfAYEibQYIkNqEqO94tLbwla5m7Am5sVOxcMxsSclk1THzbkcYxF5SoeIAoRpPvgWjt4tywd9ehmbFVFghxI/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnUwgnQxPqiaNrCk9iaXtP6QVbsyPFRWuNtKfkqno9PA8KF8dvyDA8mYcNAibYaWqdVqttHFdXaMI5fpM5MvDRAIFMQ6j2WV2F0cU/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwloYThTDGlt1qLXcOBYiaQqkRq6DNYM8jNAvuJEG4jCqlMcXKgedyBEEZXUgFW6S0a6O8ml1FRpT6rg5uoW8xxkr2iaiaL9b3VHPg/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmPEeicic4ggB97lIQSgYicJpqp6jKl7DeWzWMz3UyS9spE4jQs50siaOiaibsfFgRFJgJDArib9TNJmVoAElcTqhA60biazcxNRSibb4XQ/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnjsUcBqe7u0RsAL6LP2ricZSacsHNO2icywVTFxHWhv43bWvAHxdKblpa13pXEXTl51pue0PFleI7KNZNia9egia3XFs1LTmMjsJY/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmWBDtic8BdMMSdvx65KlQ1mg8O1uwUIwWTASpPcbBM5ak1k9bBn6IJ1X8ZNZDOTtECRFvic0xr96kajm7nXXBR6U7pwCkSxEc74/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlsn7pqiah8NjiaJXeibtwGBkEgempdQLZ5aI2tdS9NeOm7O7G2ez4TL2tfWtx4veBtXdicvvTxlsQt9ttAELY3od2icTzycukJ2tm8/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwls1ZVmVq8ygKcT0hB5fVqDcuqNwfibuWCd1L3Wm6omsae6Ucxv9EiaoOEsTxqIJiacJ9ib0Hxhn4MSIs6Ua03tZzVuPGNIEbOLwmk/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmmLl5N6dRiahYCrnp7zhrMldP8kRTibeKqALHXXcYboX1CD788qvLgYOvQjgbJ4En5umJUicOqKVR5ibm8GBmqo1u8Bjd3BQMIKEU/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnniaibVufZKU6rCjPvIH7rFLfbsxrvvKEKTAPwW1CtrsL4AFh8mU6RAtRv4Omr00UiajwAOqlFdVAYDaYsJmewhmA0zElLuYLWys/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkicAqtjJB0dPuv8D9iaWfO7cIttYYNIsa9MCwRhOyJLNsQKHf8f3r2hJFw7mNYx9njjcL3QNvZ0erTic1lcLwtBKNaSaicB8vFFNc/640?wx_fmt=png&from=appmsg)

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwn7y96eXCKR7zBRvMLaWVqZFPdwia0ibL8Vxj1gpVAwicunHZ5LGTuEcZ1Cl6AfgibSUefDDmwaiagYCpxHrxeic3G9KVbTr9pn2BOUM/640?wx_fmt=png&from=appmsg)

  *   *

```
# UNAGI输出了许多文件，存储在0、1、2、model_savve文件夹中!tree -L 2 UNAGI-main/UNAGI/data/example/
```
```
UNAGI-main/UNAGI/data/example/
```
```
├── 0
```
```
│   ├── averageValues.npy
```
```
│   ├── edges.txt
```
```
│   ├── idremInput
```
```
│   ├── idremModel
```
```
│   ├── idremResults
```
```
│   ├── idremsetting
```
```
│   ├── loss.txt
```
```
│   └── stagedata
```
```
├── 0.h5ad
```
```
 ├── 1
```
```
│   ├── averageValues.npy
```
```
 │   ├── edges.txt
```
```
 │   ├── idremInput
```
```
│   ├── idremModel
```
```
│   ├── idremResults
```
```
│   ├── idremsetting
```
```
│   ├── loss.txt
```
```
│   └── stagedata
```
```
├── 1.h5ad
```
```
├── 2
```
```
│   ├── averageValues.npy
```
```
│   ├── edges.txt
```
```
│   ├── idremInput
```
```
│   ├── idremModel
```
```
│   ├── idremResults
```
```
│   ├── idremsetting
```
```
│   ├── loss.txt
```
```
│   └── stagedata
```
```
├── 2.h5ad
```
```
├── 3.h5ad
```
```
 └── model_save
```
```
    ├── example_0.pth
```
```
    ├── example_1.pth
```
```
    ├── example_2.pth
```
```
    ├── example_dis_0.pth
```
```
    ├── example_dis_1.pth
```
```
    ├── example_dis_2.pth
```
```
    └── training_parameters.json
```

```
  19 directories, 20 files
```

2.3 虚拟干扰分析

在UNAGI模型训练完毕后，时间序列可初步获得四个stage。原输入`h5ad`的路径下训练完成后会生成一个新的 “升级版单细胞数据”，就是这里的`2/stagedata/dataset.h5ad`，其中包含：模型学习到的细胞潜变量空间（z）、UMAP、动态基因、细胞轨迹（Tracks）细胞状态转换图、扰动分析所需的全部信息，可用于执行下游任务。

  *   *   *   *   *   *   *   *   *   *   *   *   *

```
%%timeimport warningswarnings.filterwarnings('ignore')from UNAGI import UNAGIunagi = UNAGI()# 进行药物干扰分析：unagi.analyse_UNAGI('./UNAGI-main/UNAGI/data/example/2/stagedata/dataset.h5ad',# 输入文件                    iteration=2,# 选择第几次迭代计算次数                    random_background_sampling_times=1000,#  寻找动态标记基因时，随机背景基因抽样次数，数值越大，结果越稳定，但跑的会越慢                    target_dir=None, # 目标文件夹，none则输出                    customized_drug='./UNAGI-main/UNAGI/data/cmap_drug_target_genes.npy',# 自定义药物数据库，这里是由作者提供的                    run_perturbation=True# 是否运行基因、药物干扰                   )
```

![](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnhm2iaiahTAEe7zULthGeeRlTEchUYGnEulkqhwZlfKzkLtEMY6nEK2Pm7Jt8GrapFUgmP2CfqLUhxefOazUMIDx1dwkFcuQzzU/640?wx_fmt=png&from=appmsg)

2.4可视化

UNAGI会生成包含`.h5ad`、`.pkl`的心文件夹(为指定的情况下输出的是这里的`example_2`)，可用于后续可视化。

  *   *   *   *   *   *

```
import scanpy as scimport pickle as pkl# 读取输出的h5ad单细胞文件adata = sc.read('./example_2/dataset.h5ad')# 单细胞对象：adata
```
```
AnnData object with n_obs × n_vars = 27647 × 2484
```
```
     obs: 'barcode', 'nUMI', 'nGene', 'percMito', 'percSpliced.v', 'percUnspliced.v', 'percAmbiguous.v', 'Sample.ID', 'Subject.ID', 'Sex', 'Age', 'Surface.Density', 'Percent.Tissue', 'Disease.Ident', 'nCount_RNA', 'final.ident', 'nFeature_RNA', 'nCount_integrated', 'nFeature_integrated', 'name.simple', 'Library.Ident', 'renamedFin', 'integrated_snn_res.2', 'seurat_clusters', 'renamed.2', 'integrated_snn_res.3', 'log10UMI', 'renamed.3', 'stage', 'leiden', 'ident'
```
```
     var: 'features'
```
```
     obsm: 'X_umap', 'embdedding', 'umap', 'z'
```
```
     layers: 'geneWeight'
```
```
     obsp: 'gcn_connectivities'
```

  *   *   *

```
# 读取非结构性注释信息：adata.uns = pkl.load(open('./example_2/attribute.pkl', 'rb'))type(adata.uns)
```
```
anndata.compat._overloaded_dict.OverloadedDict
```

2.4.1 细胞降维可视化

  *   *   *   *   *

```
from UNAGI.plotting import cell_type_composition, plot_stages_latent_representationplot_stages_latent_representation(adata, # 读入的单细胞对象                                  cell_type_key='ident', # 细胞的分类变量                                  stage_key='stage'# 分组变量                                 )
```
```
ARI:  0.6551458869846446
```
```
NMIs:  0.6503782470882618
```
```
silhouette score:  0.22718687453535993
```
```
ARI:  0.680303236781184
```
```
NMIs:  0.7374966525638296
```
```
silhouette score:  0.30596853452442374
```
```
ARI:  0.7884503852215209
```
```
NMIs:  0.7823241013103959
```
```
silhouette score:  0.20378125738231517
```
```
ARI:  0.7709702766822403
```
```
NMIs:  0.7719353736314634
```
```
silhouette score:  0.22769615347172187
```

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlc7B06E9ljVqBNZKz50xwnTXqvntaMczLGZzNKomShYPRBfFNSg626jbYuPhlmv721A2JL1GQ5iaTlanbbJibCfB0jgRgib7jEiag/640?wx_fmt=png&from=appmsg)
```
ARIs:  [0.7237174464173974]
```
```
NMI:  [0.7355335936484877]
```
```
silhouette score:  0.2411582049784552
```

2.4.2 细胞比例可视化

  *

```
cell_type_composition(adata, cell_type_key='ident', stage_key='stage')
```

![No description has been provided for this image](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmYWTHFPLkQvHG3jffia3YEmd2hpbwKyZnvLibibN8VVIUyhjWCHU77NhWBYl2ib3IyVsJZEwPazca3fjibMw3qNhzJNicqvmksABzSQ/640?wx_fmt=png&from=appmsg)

2.4.3 细胞动态发育轨迹

  *   *   *   *   *   *

```
from UNAGI.utils import visualize_dynamic_graphs_by_text# 展示各个stage中各细胞类型的亚群发育轨迹：visualize_dynamic_graphs_by_text(edges=adata.uns['edges'],cell_types=adata.uns['clusterType'])
# 动态轨迹图也可以直接保存为txt格式：# visualize_dynamic_graphs_by_text(edges=adata.uns['edges'],cell_types=adata.uns['clusterType'],write='saved_dynamic_graphs.txt')
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/buxFNhaTGwlh3b7HsUqib2jZIIr7sYArqBCUCrDt6wFZpkgf2dfXTJd4oZ0lJ5bia5kvMHvRcibiasoZMpA3CsRq9hRKAIib06IQntkynYG7tvT8/640?wx_fmt=jpeg)

2.4.4 药物干扰结果可视化

可以看出`ibudilast `的干扰分值非常高，其与纤维化过程中的TGFβ通路相关，其在肺纤维化中具有治疗潜能。

  *   *

```
from UNAGI.perturbations import get_top_compounds, get_top_pathwaysget_top_compounds(adata,perturb_change=0.5,top_n=10)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmBwtgxlbhqWx6dTI7lBHBmaq3poMSph8WBk2ggqgM4OGc8ibBhRsLXnUX16DibdoqEmyeADAeR1MWzlJgjicgnEQJvPttTRupqDM/640?wx_fmt=png&from=appmsg)

2.4.5通路干扰结果

  *

```
get_top_pathways(adata,perturb_change=0.5,top_n=10)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwk5oyB01FYMbbZ1RHfAgXSx09gXxgBgVjFicWnZEicYweqd8k5RsJuOVYGGciciapoIGxA5VjVkibMpsPps2js8ibqict2B4jsNkzQ0a4/640?wx_fmt=png&from=appmsg)

**三、资料领取**

更多编程教程可见：

[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)

[5.5小时掌握R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535038&idx=2&sn=717a8673a8bf82d5ac40af4441a07f65&scene=21#wechat_redirect>)

[8小时掌握生信Python](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537399&idx=1&sn=d14c7987d1384fe133094748844b8d59&scene=21#wechat_redirect>)

本推送的代码文件可以在以下链接中下载：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkccXStic4cPHkxSjYHHjtUiaSQ2Fn1focgLWOxVTDudhr9eIYdpraIS1bh2a0gRI691ZIkEkRiaZuNCIFog7wtJfAtB7Uwnuy0uQ/640?wx_fmt=png&from=appmsg)通过网盘分享的文件链接:

https://pan.baidu.com/s/1No_C678UKW_SWAjS_V13-Q

提取码: 2it8

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlCyXSxibapXIYNacNP7soSrfeYoiaRqFu29eSnfXfuFe7Fa45I5oTnTGR3rWRYFqicgUxJb0pYx9XdBWNajNicL3pwcOV7B8zFLW8/640?wx_fmt=jpeg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgDzj66ZOwl0njbJ30HMFyLcZsxrqT3UCOtf50I0DiaBmLhnRTDiayCiaYq073krS7LYKf3pdaISNvMg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=qywuinol&tp=wxpic#imgIndex=77)

**欢迎致谢**

如果以上内容对你有帮助，欢迎在文章的Acknowledgement中加上这一段，联系客服微信可以发放奖励：
```
Since Biomamba and his wechat public account team produce bioinformatics tutorials and share code with annotation, we thank Biomamba for their guidance in bioinformatics and data analysis for the current study.
```

**欢迎在发文/毕业时向我们分享你的喜悦~**

**已致谢文章**

[ 鼻咽癌的Bulk RNA-Seq与scRNA-Seq联合分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247510548&idx=1&sn=58048c46e837b1d56dffa282272c6d96&chksm=9b3cd344ac4b5a52369e91b4e61fa0a2c951b82cc21165b99f42ba2c2191d4add803bd73c928&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)

[13分+文章利用scRNA-Seq揭示地铁细颗粒物引起肺部炎症的分子机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511886&idx=1&sn=31c712d00377b0f0ed33703b5b4fbfd8&chksm=9b3cd61eac4b5f084fde14a2eb50356f2f40a66c608d38909f12a3d81f48cff029a09ce2ee8c&token=1453608870&lang=zh_CN&scene=21#wechat_redirect>)

[除了铁死亡，还有铜死亡？！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247518144&idx=1&sn=d036f1bb04b09eb73f53e2104d69404c&chksm=9b3cfe90ac4b77862f2f463b42132c7bfdb687a1b61d350dcf656117b1331271e179710fd4fa&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)

[IF14.3| scRNA-seq+脂质组多组学分析揭示宫内生长受限导致肝损伤的性别差异](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520900&idx=1&sn=157134292ffc2e5df730c5ba8a357b61&chksm=9b3cebd4ac4b62c286543c30381e9b4fdb8b44b28d4fa902fb963bbd45b28e1d3f1bc98eb148&scene=21&cur_album_id=3425248581018714114#wechat_redirect>)[银屑病和脂肪肝病中共同病理和免疫特征](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247521069&idx=1&sn=4ef441a885cb2525ee3b5c81001feddf&chksm=9b3cea7dac4b636be9f10ffdf75e13531fccae62129944b21a457db2e08c3f2db1e1b553ac34&scene=21&cur_album_id=3425248581018714114#wechat_redirect>) [《Advanced Science》新型Arf1抑制剂促进癌症干细胞衰老并增强抗肿瘤免疫](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522233&idx=1&sn=287a380de741ff55f0ce78dc9c727985&chksm=9b3ceee9ac4b67ffd925abafeba2cb215a5984e6dc85f0d8607340a07ec9208f1d19eae0e04b&scene=21#wechat_redirect>)

[scRNA-seq揭示脓毒症预后水平预测的关键靶点！](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247522281&idx=1&sn=f95eb12fdc340b8da1123ec6253e6fac&chksm=9b3ceeb9ac4b67afa587e5fa3a2a8960e9bb28a1ad6dc48e49120a76154417a4c8be95af90b0&scene=21#wechat_redirect>)

[机器学习+生信多组学联合构建牙周炎"线粒体功能障碍与免疫微环境"关联网络](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247527168&idx=1&sn=0791d2bf53a9a60015577f892b10d370&scene=21#wechat_redirect>)

[KIF18A在肝细胞癌转移中的双重角色](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528014&idx=1&sn=d285c9ebd415be328fc682d00e6182c0&scene=21#wechat_redirect>)

[bulk+scRNA-seq挖掘BCL2-MAPK14-TXN氧化应激诊断模型，鉴定脓毒症中氧化应激关键基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530000&idx=1&sn=e8ddca4e1b2e60839cdf2a7fe87b3dfe&chksm=9b3c0f40ac4b86562e0e307b9dbb8688159e72b3c19d9ceebf8a4bb2e21638896f005b497b11&scene=21&cur_album_id=3425248581018714114&search_click_id=#wechat_redirect>)

[致谢文章+1，中科院1区，scRNA-seq揭示麻黄-甘草配对治疗呼吸系统症状和多(I:C)诱发肺炎模型机制](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536407&idx=1&sn=4da88e13f112662a02fea89d1b7798e9&scene=21#wechat_redirect>)

[致谢文章又+1，生物信息学+机器学习鉴定驱动糖尿病肾病免疫激活和小管间隙损伤的PANoptosis枢纽基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537544&idx=1&sn=6e5bb738eb11af53173f9fef67b977df&scene=21#wechat_redirect>)

向下滑动查看更多

欢迎大家致谢~

![图片](https://mmbiz.qpic.cn/mmbiz_gif/ImlBFVOwwpx2dVa7tC0UYQRDUr6TnenA8vsST0iaFjDqdO9ecITMbpF2CD5mWr6Z30yXOIcj45qtdIpia3zh8POQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=7lj2ti0t&tp=wxpic#imgIndex=78)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=0)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=1)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&tp=webp#imgIndex=2) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4) 您点的每个赞和在看，我都认真当成了喜欢
