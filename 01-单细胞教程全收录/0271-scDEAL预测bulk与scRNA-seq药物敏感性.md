---
title: "scDEAL预测bulk与scRNA-seq药物敏感性"
date: 2026-04-17
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537240&idx=1&sn=bdeb86c8080deeafc49f23b4e14c93cd&chksm=9b3c2b08ac4ba21e55b1cbd743f3326ffbeeb792043801f7e5c1d09c89ddb44130024daaf4ea#rd
albums: ["单细胞教程全收录"]
---

# scDEAL预测bulk与scRNA-seq药物敏感性

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537240&idx=1&sn=bdeb86c8080deeafc49f23b4e14c93cd&chksm=9b3c2b08ac4ba21e55b1cbd743f3326ffbeeb792043801f7e5c1d09c89ddb44130024daaf4ea#rd
> 合集：单细胞教程全收录

**一、写在前面**

scDEAL能够通过整合[Bulk](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2959853503529910274#wechat_redirect>)和[scRNA-seq](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2168829347397156865#wechat_redirect>)测序数据进行药物敏感性的深度转移学习，该工具最近一次的更新在2023年03月。实际体验感不是很好，算是踩了雷，分析的输入数据不是很明确，输出数据同样找起来费劲；官方教程写的也比较乱，且每次运行似乎只能预测一个药物的敏感性。 因此我们暂不将其大规模纳入教程与实战流程。这大概也是我们亲自上手测试、替大家提前避坑的意义所在。比较好用的工具我们此前整理过，可参考：[scRNA-seq肿瘤细胞药物敏感性预测分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536705&idx=1&sn=7fbfeba5dee45f6c3311bd31082a428c&scene=21#wechat_redirect>)

如果你希望有人真的手把手教你学单细胞：

[R语言scRNA-seq数据分析全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535927&idx=2&sn=86947f0522de0d9785865bd24115b002&scene=21#wechat_redirect>)

[Python版scRNA-seq数据分析全程班](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=2&sn=f1b479a1469dfe46bd8bb0b0bd1b470d&scene=21#wechat_redirect>)

如果需要[单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531388&idx=3&sn=dfaf8cac9db70bb408206fb3da27ffda&scene=21#wechat_redirect>)指导、生信热点[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469&token=1729645779&lang=zh_CN#wechat_redirect>)、自测数据个性化分析辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[Biomamba_zhushou]

**二、实操流程**
```
1.环境配置
```

注意，若你在Jupyter环境中运行此脚本，则下文带"!"的命令会默认在终端运行，直接在终端配置环境时请去除"!"

  *   *   *   *   *

```
!git clone https://github.com/OSU-BMBL/scDEAL.git# 切换工作路径!cd scDEAL!conda install conda-pack!conda install -c conda-forge conda-pack
```

利用conda安装

!conda安装可参考：[生信软件管家——conda的安装、使用、卸载](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530994&idx=2&sn=3f3bdf2d06532c0b0ab8c9a477b8332c&scene=21#wechat_redirect>)

  *   *

```
# conda-pack可以解包并安装conda!conda install -c conda-forge conda-pack
```

  *   *   *   *   *   *

```
# 从github获取克隆!git clone https://github.com/OSU-BMBL/scDEAL.git# 进入文件夹!cd scDEAL# 创建文件夹用于布置环境!mkdir -p scDEALenv
```

我们在本地给大家准备了scDEAL源码包

  *   *   *   *

```
# 解包：!tar -xzf scdeal.tar.gz -C scDEALenv# 激活scDEALenvv，即可让scDEAL的环境添加到PATH中!source scDEALenv/bin/activate
```

激活成功后在你的终端命令行前会多出(scDEALenv)字样：

![image.png](../../images/92cd2e328fed4f7c.webp)

测试数据也在本地给大家准备好了这个包。其中包含的数据概况如下：

![image.png](../../images/586cf560ce53181e.webp)

  *   *   *   *

```
# 解压测试文件!unzip scDEAL.zip# 查看文件目录tree data
```

2.采用预训练

对于scRNA-Seq预测任务，作者为存储在save/models中的模型提供了预训练的检查点，检查点的命名规则如下：

bulk RNA数据集+“data”+scRNA-测序数据集+“药物”+“药物名称+”瓶颈层“+”EDIM“+编码器尺寸+”PDIM“+预测维度+”模型“+编码器模型名称+”dropout“+正则化率阈值+”gene“+show critical genes+”lr“+学习速率+”mod“+模型版本+”sam“+抽样方法（+”_DANN.pkl“仅限最终单细胞模型）

例如这个文件名：

  *

```
integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling_DaNN.pkl
```

在恢复训练时，可以使用scmodel.py和bulkmodel.py的检查点选项，以获得单细胞水平的预测结果：

例如以下教程将演示来源于GSE110894的急性骨髓性白血病细胞的内置测试案例[1]中，调用scDEAL模型，并预测GSE110984输入scRNA-Seq数据中I.BET.762的灵敏度。 获得了

“save/sc_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling_DaNN.pkl”“save/sc_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling_DaNN.pkl”模型

先通过bulk RNA的检查点模型，运行bulkmodel.py

看一下测试数据

data/GSE110894/GSE110894_CellInfo.xlsx

![image.png](../../images/6358287075e8889c.png)

data/GSE110894/GSE110894.csv包含的就是单细胞count矩阵

gene_id RPI1_A3 RPI1_A4 RPI1_A5 RPI1_A6 RPI1_A7 RPI1_A8 RPI1_A9 RPI1_A10 ENSMUSG00000110331 3 5 5 6 5 2 4 10 ENSMUSG00000006281 0 0 0 1 0 0 0 0 ENSMUSG00000040726 0 0 0 0 0 0 0 0 ENSMUSG00000024829 1 2 0 0 1 3 1 1 ENSMUSG00000029007 1 2 1 0 0 0 0 0 ENSMUSG00000032026 2 3 3 6 3 1 0 4 ENSMUSG00000031808 0 1 0 1 0 0 0 0 ENSMUSG00000042549 1 0 0 0 0 0 0 0 ENSMUSG00000024007 3 1 0 1 0 3 0 2 ENSMUSG00000037151 0 0 1 1 0 0 1 0 ENSMUSG00000041538 1 0 0 1 0 0 0 0 ENSMUSG00000063873 1 0 0 0 1 1 0 0 ENSMUSG00000028423 0 0 0 6 0 2 1 4 ENSMUSG00000028044 2 3 5 8 3 2 1 3

脚本介绍： 需要注意的是以下的路径都会有一些前缀是默认的，例如你的数据文件夹会保存在data路径下，输出会保存在save文件夹下 python bulkmodel.py --help optional arguments: -h, --help # 展示帮助文档 --data DATA # bulk RNA表达矩阵的路径 --label LABEL # 经处理后的bulk RNA-seq药物筛选注释的路径 --result RESULT # 训练结果的路径 --drug DRUG # 选择的药物，需要是label参数指定文件中的一列 --missing_value MISSING_VALUE # 药物筛选注释中缺失值的填充值，默认为1 --test_size TEST_SIZE # 测试集大小，默认0.2 --valid_size VALID_SIZE # 验证集大小，默认0.2 --var_genes_disp VAR_GENES_DISP # 预训练中高变基因离散度选择，如果选择None，则所有基因都会选择 --sampling SAMPLING # 训练时的采样方法，可以从upsampling、downsampling、SMOTE，no中选择.默认为no --PCA_dim PCA_DIM # PCA降维的组成数，默认为0，则不执行PCA --device DEVICE # 参与训练的设备，可以选择cpu或gpu。默认为cpu --bulk_encoder BULK_ENCODER, -e BULK_ENCODER # bulk的编码器路径 --pretrain PRETRAIN # 是否对编码器进行与训练，填布尔值，默认为True --lr LR # 学习率，默认为1e-2 --epochs EPOCHS # 训练的轮数，默认为500 --batch_size BATCH_SIZE # 每批次训练数据大小，默认为200 --bottleneck BOTTLENECK # 瓶颈层大小，默认为 32 --dimreduce DIMREDUCE # 编码模型类型. 从AE或VAE中选择，默认为AE --freeze_pretrain FREEZE_PRETRAIN # 预训练模型的填充参数，0：不冻结，1：冻结。默认值：0。 --encoder_h_dims ENCODER_H_DIMS # 编码器的形状。每个数字代表一层中的神经元数量。各层之间用逗号隔开。默认值：512,256 --predictor_h_dims PREDICTOR_H_DIMS # 预测器的形状。每个数字代表一层中的神经元数量。各层之间用逗号隔开。默认值：16,8 --VAErepram VAEREPRAM --data_name DATA_NAME # 测试数据的访问标识，仅支持预设类型数据。 --checkpoint CHECKPOINT # 从检查点文件中加载权重，其值可以为 True、False 或文件路径。检查点文件可以是 --bulk_model BULK_MODEL, -p BULK_MODEL # bulk水平训练模型的路径 --log LOG, -l LOG # 训练日志的路径 --load_source_model LOAD_SOURCE_MODEL # 是否加载已训练的批量级别数据。0：不加载；1：加载。默认值：0。 --mod MOD # 将细胞类型标签嵌入以规范训练过程：new：添加细胞类型信息，ori：不添加细胞类型信息。默认值：new --printgene PRINTGENE # 打印关键基因列表：T：打印。默认值：T --dropout DROPOUT 神经网络Dropout，默认0.3 --bulk BULK bulk数据集的选择integrate（两类数据集同时使用）old对应GDSC. new对应CCLE。默认为integrate

  *   *

```
!source scDEALenv/bin/activate!python bulkmodel.py --drug "I.BET.762" --dimreduce "DAE" --encoder_h_dims "256,128" --predictor_h_dims "128,64" --bottleneck 512 --data_name "GSE110894" --sampling "upsampling" --dropout 0.1 --lr 0.5 --printgene "F" -mod "new" --checkpoint "save/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling"
```

  *   *   *   *   *   *   *   *   *

```
# 运行日志(在我们的机器上大约花费了1min)：python bulkmodel.py --drug "I.BET.762" --dimreduce "DAE" --encoder_h_dims "256,128" --predictor_h_dims "128,64" --bottleneck 512 --data_name "GSE110894" --sampling "upsampling" --dropout 0.1 --lr 0.5 --printgene "F" -mod "new" --checkpoint "save/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling"The new directory is created!The new directory is created!The new directory is created!two databases combinecpubulk_X_allRensor torch.Size([1280, 15962])bulk_model finished
```

  *   *   *

```
# 检查一下模型是否生成成功：!ls -lh /data2/analysis/biomamba_tutor/scDEAL/scDEAL/save/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling# 成功得到了一个17M的与训练模型
```
```
-rw-rw-r-- 1 biomamba_tutorial biomamba_tutorial 17M Mar 18  2023 /data2/analysis/biomamba_tutor/scDEAL/scDEAL/save/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling
```

再运行scmodel.py可获得单细胞级别的预测结果。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 选项参数介绍optional arguments:  -h, --help            # 返回帮助文档  --bulk_data BULK_DATA RNA-Seq # 表达矩阵的路径  --label LABEL        # 经处理的bulk RNA-Seq药物筛选流程注释  --sc_data SC_DATA     # 测试数据的访问标识，仅支持预设类型数据。  --drug DRUG           # 所选药物的名称，应为 "--label" 输入文件中的列名。  --missing_value MISSING_VALUE # 在药物筛查注释中缺失的条目中所填写的数值，默认值为 1 。  --test_size TEST_SIZE # bulk模型训练所用测试集的大小，默认值：0.2  --valid_size VALID_SIZE #  bbulk模型训练所用验证集的大小，默认值：0.2  --var_genes_disp VAR_GENES_DISP # 在对数据进行预处理时，对于高变基因的离散度进行选择。若设置为“None”，则会选取所有基因。默认值为“None”。  --min_n_genes MIN_N_GENES # 用于筛选的最低基因数量要求，即这些细胞中具有 UMI 计数大于 1 的基因数量，建议值：0（默认值）  --max_n_genes MAX_N_GENES# 用于筛选的设定值：对于单个细胞而言，UMI（未修饰转录本计数）大于 1 的基因的最大数量（此设定值旨在提出建议），默认值：2000  --min_g MIN_G         # 细胞所需的最少不为0的基因数量，默认值：200  --min_c MIN_C         # 基因最少在多少基因表达，默认值为3，这两个值其实与Seurat和Scanpy的过滤参数一致  --percent_mito PERCENT_MITO # 用于筛选设定的细胞线粒体基因表达水平的百分比，默认值：100%  --cluster_res CLUSTER_RES # leiden聚类的分辨率设定，默认值：0.3  --mmd_weight MMD_WEIGHT # 迁移学习中 MMD 损失的权重，默认值：0.25  --mmd_GAMMA MMD_GAMMA # 迁移学习中 MMD 损失函数核中的伽马参数，默认值：100  --device DEVICE       #用于训练模型的设备。可以是 CPU 或 GPU。默认值：CPU  --bulk_model_path BULK_MODEL_PATH, -s BULK_MODEL_PATH # 训练好的bulk水平预测器的路径  --sc_model_path SC_MODEL_PATH, -p SC_MODEL_PATH # 训练好的单细胞水平预测器的路径  --sc_encoder_path SC_ENCODER_PATH # 单细胞水平与训练编码器的路径  --checkpoint CHECKPOINT # 从检查点文件中加载权重，其值可以为 True、False 或文件路径。检查点文件可以是paraName1_para1_paraName2_para2... 默认值：True  --lr LR               # 模型训练的学习率. 默认值: 1e-2  --epochs EPOCHS       # 训练轮次，默认值: 500  --batch_size BATCH_SIZE # 训练批次大小：200  --bottleneck BOTTLENECK # 瓶颈层大小，默认: 32  --dimreduce DIMREDUCE # 编码器类型. 可以是AE或VAE. 默认: AE  --freeze_pretrain FREEZE_PRETRAIN #  设置预训练模型中的冻结参数。0：不冻结；1：冻结。默认值：0  --bulk_h_dims BULK_H_DIMS # 源编码器的形状。每个数字代表一层中的神经元数量。各层之间用逗号隔开。默认值：512，256  --sc_h_dims SC_H_DIMS # 编码器的形状。每个数字代表一层中的神经元数量。各层之间用逗号隔开。默认值：512,256  --predictor_h_dims PREDICTOR_H_DIMS # 预测器的形状。每个数字代表一层中的神经元数量。各层之间用逗号隔开。默认值：16,8  --VAErepram VAEREPRAM  --batch_id BATCH_ID  # 测试集的批次ID   --load_sc_model LOAD_SC_MODEL # 是否加载已训练的模型。0：不加载，1：加载。默认值：0  --mod MOD            # 将细胞类型标签嵌入以规范训练过程：new：添加细胞类型信息；ori：不添加细胞类型信息信息。默认：new。  --printgene PRINTGENE # 打印关键基因列表：T：打印。默认值：T  --dropout DROPOUT     # 神经网络Dropout. 默认: 0.3  --logging_file LOGGING_FILE, -l LOGGING_FILE # 训练日志路径  --sampling SAMPLING   # bulk模型训练数据的采样方法训练。可以选择no（不采样）, upsampling（上采样）, downsampling（下采样）, SMOTE。默认值：不进行采样。  --fix_source FIX_SOURCE #  固定bulk水平模型（默认值：0）  --bulk BULK          # 选择bulk数据集，integrate:两个数据集. old: GDSC数据集，new:CCLE数据集. 默认值: integrate
```

  *   *   *   *

```
!python scmodel.py --sc_data "GSE110894" --dimreduce "DAE" --drug "I.BET.762" \  --bulk_h_dims "256,128" --bottleneck 512 --predictor_h_dims "128,64" --dropout 0.1 \  --printgene "F" -mod "new" --lr 0.5 --sampling "upsampling" --printgene "F" -mod "new" \ --checkpoint "save/sc_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling_DaNN.pkl"
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 运行日志(在我们的机器上大约花费了1min)The new directory is created!save/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling... storing 'Plate#' as categorical... storing 'Well position' as categorical... storing 'Sample name' as categorical... storing 'Index-Sort condition' as categorical... storing 'Well index' as categorical... storing 'sensitivity' as categoricalWARNING: It seems you use rank_genes_groups on the raw count data. Please logarithmize your data before calling rank_genes_groups.(1419, 21182)two databases combinePretrain==save/sc_encoder/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsamplingtensor([[ 0.3957, -0.6987,  1.5514,  ...,  0.9161, -0.2885,  1.0257],        [ 0.1534, -0.5537,  2.0089,  ...,  1.3458,  0.2866,  1.5238],        [ 0.6084, -0.5500,  0.5349,  ...,  0.1771, -0.9144,  0.1586],        ...,        [ 0.8015, -0.1076, -1.2609,  ..., -1.5192, -2.3199, -1.5664],        [ 3.9421, -0.7004, -9.6212,  ..., -7.2608, -7.6576, -7.5893],        [ 0.4044, -0.4826,  1.1278,  ...,  0.6754, -0.5466,  0.7907]],       grad_fn=<AddmmBackward0>)predictions (1419, 2)sc model finished
```

  *   *   *

```
# 检查下输出文件：!ls -lh /data2/analysis/biomamba_tutor/scDEAL/scDEAL/save/sc_encoder/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling# 获得了一个14M的训练结果
```
```
-rw-rw-r-- 1 biomamba_tutorial biomamba_tutorial 14M Mar 18  2023 /data2/analysis/biomamba_tutor/scDEAL/scDEAL/save/sc_encoder/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling
```

注意，编码器和预测器的维度应在两个步骤中完全相同（--encoder_h_dims（bulk_h_dims）“256,128”，--predictor_h_dims“128,64”，--bottle 256）。此步骤以bulk RNA-Seq的表达图谱和药物反应注释为输入。它加载了药物敏感性预测器，针对药物“I.BET.762”。输出模型存储在“save/models”目录中。在这种情况下。批量模型的文件名是

“save/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling”。

3.从头训练

这一流程更适合大家用户自己的数据来训练，和上面的bulkmodel.py与scmodel.py设置类似，但需要额外设置--checkpoint “False”：

  *   *

```
python bulkmodel.py --drug "I.BET.762" --dimreduce "DAE" --encoder_h_dims "256,128" --predictor_h_dims "128,64" --bottleneck 512 --data_name "GSE110894" --sampling "upsampling" --dropout 0.1 --lr 0.5 --printgene "F" -mod "new" --checkpoint "False"python scmodel.py --sc_data "GSE110894" --dimreduce "DAE" --drug "I.BET.762" --bulk_h_dims "256,128" --bottleneck 512 --predictor_h_dims "128,64" --dropout 0.1 --printgene "F" -mod "new" --lr 0.5 --sampling "upsampling" --printgene "F" -mod "new" --checkpoint "False" --device GPU
```

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 训练日志：# 从头训练的计算时间会长一些，在我的机器上大约花了3h+(scDEALenv) biomamba_tutorial@biomamba:~/scDEAL/scDEAL$ python scmodel.py --sc_data "GSE110894" --dimreduce "DAE" --drug "I.BET.762" --bulk_h_dims "256,128" --bottleneck 512 --predictor_h_dims "128,64" --dropout 0.1 --printgene "F" -mod "new" --lr 0.5 --sampling "upsampling" --printgene "F" -mod "new" --checkpoint "False" --device GPUsave/bulk_pre/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling... storing 'Plate#' as categorical... storing 'Well position' as categorical... storing 'Sample name' as categorical... storing 'Index-Sort condition' as categorical... storing 'Well index' as categorical... storing 'sensitivity' as categoricalWARNING: It seems you use rank_genes_groups on the raw count data. Please logarithmize your data before calling rank_genes_groups.(1419, 21182)two databases combinePretrain==save/sc_encoder/integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling0.19734515001376470.168184928596019740.13837757458289465.........0.01340903202071786tensor([[-1.5719, -1.0925, 11.3126,  ...,  8.2826,  4.8055,  8.9214],        [-2.0763, -0.8352, 11.8761,  ...,  8.8199,  5.8017,  9.4461],        [-1.6746, -0.7143,  9.7676,  ...,  7.0941,  4.0264,  7.5394],        ...,        [-1.3635, -0.3674,  7.7419,  ...,  5.3487,  2.3854,  5.7012],        [ 2.1760, -0.6789, -3.6282,  ..., -2.9403, -3.5837, -3.0230],        [-1.8449, -0.8331, 10.7891,  ...,  7.9166,  4.8163,  8.5025]],       grad_fn=<AddmmBackward0>)predictions (1419, 2)sc model finished
```

4.输出文件

scDEAL可以直接输出可由scanpy包读取的[AnnData对象](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528513&idx=1&sn=1ff1b8bee321f8f5bcac425ce96dc6ff&scene=21#wechat_redirect>)（.h5ad文件）。文件将存储在目录“scDEAL/adata/data/”中。药敏预测将存储在adata.obs[“sens_label”]中（如果你加载名为adata的AnnDdata对象），其中0代表电阻，1代表灵敏度。输出的进一步分析可以通过Scanpy包进行。该对象可以通过函数scanpy.read_h5ad加载到Python中。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 输出路径scDEAL|   ...└───data│   │   ...└───save│   └───adata│   |    ││   |    └───data│   │        GSE110894[a timestamp].h5ad   │   │    ...   |   └───models│   │    save/bulk_encoder│   │    save/bulk_pre│   │    save/sc_encoder│   │    save/sc_pre│   │    ...
```

如果你有自己的药敏矩阵数据，也可以如此进行训练

python bulkmodel.py --drug [_Your selected drug_] --data [_Your own bulk level expression_] --label [_Your own bulk level drug resistance table_] ...
python scmodel.py --sc_data [_Your own data path_] ...

  *   *   *   *

```
# 药物耐药表可参考：scDEAL/data/ALL_label_binary_wf.csv# 表达矩阵格式可参考：scDEAL/data/ALL_expression.csv
```

5.查看训练好的h5ad

  *   *

```bash
pip install ipykernelpython -m ipykernel install --user --name scDEALenv --display-name "scDEALenv"
```

  *

```
!pip install scanpy
```

  *   *   *   *   *   *   *

```
import pandas as pdimport scanpy as scimport globimport numpy as npimport seaborn as sns; import matplotlib.pyplot as pltimport scipy as sp
```

  *   *

```
import os os.chdir('scDEAL/')
```

读取关键基因名

此步骤的输入是一个由Captum计算得出的综合梯度的txt格式矩阵文件。只有在上面运行scmodel.py脚本时设置--printgene 'T'才会生成该文件。

  *   *

```
adata = sc.read_h5ad('scDEAL/save/adata/GSE110894integrate_data_GSE110894_drug_I.BET.762_bottle_512_edim_256,128_pdim_128,64_model_DAE_dropout_0.1_gene_F_lr_0.5_mod_new_sam_upsampling.h5ad')adata
```
```
AnnData object with n_obs × n_vars = 1419 × 6644
```
```
     obs: 'Plate#', 'Well position', 'Sample name', 'Index-Sort condition', 'Well index', 'sensitive', 'sensitivity', 'Resistant_score', 'Sensitive_score', 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mt-', 'pct_counts_mt-', 'total_counts_rps', 'pct_counts_rps', 'total_counts_rpl', 'pct_counts_rpl', 'leiden', 'leiden_origin', 'sens_preds_pret', 'sens_label_pret', 'sens_preds', 'sens_label', 'rest_preds'
```
```
     var: 'n_cells', 'mt-', 'rps', 'rpl', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
```
```
     uns: 'hvg', 'leiden', 'log1p', 'neighbors', 'pca', 'rank_genes_groups', 'umap'
```
```
     obsm: 'X_pca', 'X_pre', 'X_umap', 'X_umap_origin'
```
```
     varm: 'PCs'
```
```
     obsp: 'connectivities', 'distances'
```

  *   *

```
# 查看adta的注释信息：adata.obs.head()
```

![](../../images/89bfff1788df8e60.webp)

  *

```
sc.pl.umap(adata,color='sensitivity')
```

![No description has been provided for this image](../../images/a8459742c2c4461b.webp)

  *

```
sc.pl.umap(adata,color='Sensitive_score')
```

![No description has been provided for this image](../../images/387cd1421cf56da6.webp)

  *   *   *   *   *   *   *   *   *   *

```
# 检查是否已对数化（避免重复处理）if "log1p" not in adata.uns.keys():    # 步骤1：标准化（按细胞归一化总计数）    sc.pp.normalize_total(adata, target_sum=1e4)    # 步骤2：对数化（解决rank_genes_groups的原始计数警告）    sc.pp.log1p(adata)    adata.uns["log1p"] = {"base": np.exp(1)}  # 标记已对数化    print("数据已完成标准化+对数化")else:    print("数据已对数化，跳过预处理")
```

数据已对数化，跳过预处理

  *   *

```
# 数据没有提前log1p，需要额外处理一下sc.pp.log1p(adata)  # 无需手动设置base，Scanpy会自动填充
```
```
WARNING: adata.X seems to be already log-transformed.
```

  *   *   *   *   *   *   *   *   *   *   *

```
# -------------------------- 执行 Resistant vs Sensitive 差异分析基因分析 --------------------------# groups=["Sensitive"] 表示以Resistant为参照，找Sensitive中高表达的基因；反之则groups=["Resistant"]sc.tl.rank_genes_groups(    adata,    groupby="sensitivity",       # 分组列    groups=["Sensitive"],        # 关注的分组    reference="Resistant",       # 参照分组    method="wilcoxon",           # 威尔科克森秩和检验（单细胞常用）    corr_method="benjamini-hochberg", # 矫正方式，排除一类错误    n_genes=adata.shape[1]       # 输出所有基因的结果)
```

  *

```
de_genes_all.head()
```

![](../../images/c86afc84b7f1d34d.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# -------------------------- 提取并筛选差异基因 --------------------------# 差异基因筛选阈值log2fc_cutoff = 0.5  # 对数倍变化阈值pvals_cutoff = 0.05    # 校正后p值阈值# 可视化配色colors = {"Resistant": "#e74c3c", "Sensitive": "#3498db"}# 提取所有差异基因结果de_genes_all = sc.get.rank_genes_groups_df(adata, group="Sensitive")# 筛选显著差异基因（上调：Sensitive高表达；下调：Resistant高表达）de_genes_up = de_genes_all[    (de_genes_all["logfoldchanges"] > log2fc_cutoff) &     (de_genes_all["pvals"] < pvals_cutoff)].copy()de_genes_down = de_genes_all[    (de_genes_all["logfoldchanges"] < -log2fc_cutoff) &     (de_genes_all["pvals"] < pvals_cutoff)].copy()# 整理结果de_genes_up["regulation"] = "Up (Sensitive)"de_genes_down["regulation"] = "Down (Resistant)"de_genes_significant = pd.concat([de_genes_up, de_genes_down], axis=0)# 输出统计信息print(f"\n差异基因统计：")print(f"Sensitive中上调基因数：{len(de_genes_up)}")print(f"Resistant中上调基因数（即Sensitive下调）：{len(de_genes_down)}")print(f"前5个上调基因：\n{de_genes_up[['names', 'logfoldchanges', 'pvals']].head()}")# -------------------------- 提取并筛选差异基因 --------------------------
```
```
差异基因统计： Sensitive中上调基因数：1798 Resistant中上调基因数（即Sensitive下调）：0 前5个上调基因：
```
```
                                names   logfoldchanges                 pvals
```
```
0  ENSMUSG00000026581             3.563323  3.611420e-175
```
```
1  ENSMUSG00000053477             5.125850  8.907271e-163
```
```
2  ENSMUSG00000051367             2.353388  4.814196e-146
```
```
3  ENSMUSG00000033685             1.499222  2.272169e-129
```
```
4  ENSMUSG00000020717             3.840188  2.147006e-127
```

  *

```
sc.pl.violin(adata,  'ENSMUSG00000026581',groupby='sensitivity')
```

![No description has been provided for this image](../../images/1e802f71c516708b.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# -------------------------- 5. 可视化差异基因 --------------------------plt.rcParams["font.size"] = 10 # 设置字体大小plt.rcParams["figure.figsize"] = (10, 8)# 设置图片大小# 5.1 火山图fig, ax = plt.subplots(1, 1, figsize=(10, 8))# 绘制所有基因ax.scatter(    de_genes_all["logfoldchanges"],    -np.log10(de_genes_all["pvals_adj"].fillna(1)),  # 填充NA为1，避免log(0)    s=10, c="lightgray", alpha=0.5, label="Non-significant")# 绘制上调基因ax.scatter(    de_genes_up["logfoldchanges"],    -np.log10(de_genes_up["pvals_adj"]),    s=20, c=colors["Sensitive"], alpha=0.8, label=f"Up ({len(de_genes_up)})")# 绘制下调基因ax.scatter(    de_genes_down["logfoldchanges"],    -np.log10(de_genes_down["pvals_adj"]),    s=20, c=colors["Resistant"], alpha=0.8, label=f"Down ({len(de_genes_down)})")# 标注阈值线ax.axvline(x=log2fc_cutoff, c="black", linestyle="--", lw=1)ax.axvline(x=-log2fc_cutoff, c="black", linestyle="--", lw=1)ax.axhline(y=-np.log10(padj_cutoff), c="black", linestyle="--", lw=1)# 美化ax.set_xlabel("Log2(Fold Change) (Sensitive / Resistant)")ax.set_ylabel("-Log10(Adjusted P-value)")ax.set_title("Resistant vs Sensitive Differential Genes", fontsize=12)ax.legend()ax.grid(alpha=0.2)plt.tight_layout()plt.show()plt.savefig("volcano_plot_Resistant_vs_Sensitive.pdf", dpi=300, bbox_inches="tight")plt.close()
```

![No description has been provided for this image](../../images/f3b5884bde4f19ea.webp)

有点诡异，没有发现下调基因，大家有更多关于scDEAL的使用心得，欢迎在评论区交流。

**三、参考**
```
[1]https://doi.org/10.1038/s41467-019-10652-9
```

**四、资料领取**

更多编程教程可见：

[十小时学会Linux](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&scene=21#wechat_redirect>)

[5.5小时掌握R语言](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535038&idx=2&sn=717a8673a8bf82d5ac40af4441a07f65&scene=21#wechat_redirect>)

[生信python速查手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247520999&idx=2&sn=7f6aa90c2ffa786bd660aa40b109de49&scene=21#wechat_redirect>)

一切不给测试文件和分析环境版本的教程都是耍流氓，本推送的代码和测试文件可以在以下链接中下载：

![](../../images/c1f71d9f2c745eff.png)

链接: https://pan.baidu.com/s/1v5xKSRMsBrHpf94RuD6ryw

提取码: 24ix

![](../../images/ba3ec1a57ffd77d7.webp)![图片](../../images/cb4255ab8010219d.gif)

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

向下滑动查看更多

欢迎大家致谢~

![图片](../../images/4ec66ccdb832fd05.gif)

![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=1&sn=8d03259be06f54521aac5251dec988d5&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536307&idx=2&sn=2d030173f51d24a4fee43bd0d83da03b&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/acba43cb3408c3d0.gif) 您点的每个赞和在看，我都认真当成了喜欢
