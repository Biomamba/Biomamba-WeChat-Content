---
title: "代码复写| 胶质瘤相关巨噬细胞scRNA图谱"
date: 2024-01-09
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507096&idx=1&sn=98e42a5768074d2766f2ce64214ac391&chksm=9b3ca5c8ac4b2cdebe68a8519a087e41a4c88a7e465c5ddc107f633a5fbf3fcc8bbff6aa8821#rd
albums: ["单细胞教程全收录", "全文复现"]
---

# 代码复写| 胶质瘤相关巨噬细胞scRNA图谱

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507096&idx=1&sn=98e42a5768074d2766f2ce64214ac391&chksm=9b3ca5c8ac4b2cdebe68a8519a087e41a4c88a7e465c5ddc107f633a5fbf3fcc8bbff6aa8821#rd
> 合集：单细胞教程全收录 / 全文复现

评审环节开始！

** _写在前面_**

首届“[寻因杯](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506477&idx=2&sn=155b83716930e4ae956604f7745a6fe4&chksm=9b3ca37dac4b2a6b57d1467eb4dff2c1d425b5150e6eaf384fd2232e105a597f3c3887bc9807&scene=21#wechat_redirect>)”单细胞代码复写大赛正在展开评审环节，这次带来的是08号作品。本作品复写了题为"Single-cell RNA sequencing reveals functional heterogeneity of glioma-associated brain macrophages"的论文.**文章链接** ：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7895824/**数据链接：** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136001**复现图片集锦** ：

![](../../images/fe822e5e858f9f8e.webp)

**文献解读** ：揭示不同髓系细胞在胶质瘤中功能上的异质性，单细胞转录组取Naive and GL261胶质瘤小鼠CD11b+的髓细胞得到小胶质细胞，滤过型单核细胞/巨噬细胞，和神经系统边缘性巨噬细胞。找到了一群高表达MHCII的小胶质细胞，并且在人类胶质瘤中得到了证实。找到了性别特异性基因在胶质瘤激活小胶质细胞中发挥作用，也就是说有一些性别差异性表达的基因参与激活小胶质细胞。目的：揭示CD11b+的髓系细胞在为处理组和GL261处理肿瘤样本中的异质性。

一、复写内容

原文Figure1：**Single-cell RNA-seq identifies myeloid cells with distinct expression profiles among CD11b+ cells from naive and glioma-bearing brains.****![](../../images/7a1e7f375f36e88d.webp)**单细胞取样图：取不同性别 GL261肿瘤细胞（种植14天后），流式CD11b+的细胞做筛选，然后做单细胞转录组测序，所以从这里能得到**有效信息为：样本为不同性别的 GL261种植的肿瘤组织的CD11b+的组织细胞。****![](../../images/9ce1d7ccf42ccab6.webp)**

图 b：不同性别，健康样本和肿瘤样本的Tsne降维聚类图，揭示在性别和肿瘤疾病两个维度上细胞上的差异。**一共得到 40401个细胞，14618个基因，对于CD11b+细胞，从UMAP图上可以看到，女性得到了9个细胞群，男性样本得到了8个细胞群，其中他们大都表达Microglia的marker，所以在图上作者就用Microglia+数字的形式进行区分，其中****Microglia_1****高表达****Crybb1, Cst3, P2ry12, and Pros1****，这群小胶质细胞可能是 homeostatic microglia自我平衡小胶质细胞中的一个亚群细胞群其实就是****传统的小胶质细胞****。****MG2****则高表达****Jun, Junb, Jund, Fos, Egr1, Klf6, and Aft3****这些转录因子，则认为是****转录因子激活态的小胶质细胞****，这群****MG2****还高表达****Nfkbia****基因作为****NF****κ****B****的抑制子****。****MG3****则高表达信号抑制因子****Bmp2k****和****转录抑制因子Bhlhe41,Ncoa3,Notch2****的表达。其中****Bhlhe40,Bhlhe41则直接抑制肺泡巨噬细胞的表达****。****Ncoa3****是一种核受体****抑制炎症因子的表达，以及激活抗炎的基因表达****。还有一些小的MG小群，比如MG4,MG5,MG6这三个小的MG亚群在雌性CD11b+细胞中特异性存在，其中MG4没有特异性的基因，****MG5****则倾向于表达****Plp1,Pltp,Mbp等髓系基因****，****MG6****则高表达****Cd63,Cd9****这些****细胞外囊泡相关蛋白****上。在对照组的不同性别我们都得到了一群****preMG****细胞，也就是****小胶质细胞的前体细胞****，这群细胞高表达胶质细胞的基因：****Tmem119, P2ry12, and Crybb1****。****不成熟的状态相关基因****：****Csf1, Mcm5, and Ifit3****。还高表达****半胱氨酸抑制剂****：****Cst7****,****细胞因子：Mif,Csf1****，****趋化因子Ccl12,Ccl3, and Ccl4****。以及对****干扰素反应****的相关基因：****Ifit1, Ifit3, Ifit3b, Ifitm3, and Irf7。****还有一些参与到****泛素化乙酰化****的基因比如****Isg15/Usp18****也在MG前体细胞中高表达。这群MG细胞可能在****稳态障碍****的时候发挥重要作用。**

**在对肿瘤组织的 CD11b+的细胞进行UMAP分析的时候结果我们发现了在不同性别中均得到了13个细胞群，其中包括了在对照组中存在的MG1,MG2两群Microglia。除此之外，我们还发现了一群高表达****MHC I****类****的****B2m,H2-D1,H2-K1****基因****和****MHC II****类****的****H2-Oa****和 H2-DMa****，和在疾病相关 MG中高表达的****Bst2****和 Lgals3bp基因****以及对****CCR2+****单核细胞****募集十分相关的细胞因子基因****Ccl2****。****在男性胶质瘤样本中我们还富集到了一群与增殖相关的蛋白基因比如****Stmn1,Tubb5,Tuba1b,Cdk1,Top2a****基因。在胶质瘤中的小胶质细胞还相对高表达****Timp2,Serpine2,Cst7,Cstd****基因，这些基因编码蛋白酶以及参与细胞外基质的组织中，所以可能揭示这些小胶质细胞可能参与支持入侵的特性。**

原文图c：不同细胞基因表达差异的气泡图。

![](../../images/a161eb3450970dcb.webp)

****

图 d：不同类型的细胞在不同性别，不同疾病状态下细胞的占比。

**在对照组样本中，其中****90%****左右 CD11b+的细胞为MG细胞****在不同性别中，****BAM****细胞占比 6%左右****，并且在男性 CD11b+样本中，我们还发现****一小部分单核细胞****（ Ly6c2,Ccr2）和自然杀伤细胞（Ncam1），和DC细胞（Cd24a）。**

**在胶质瘤样本中发现，****MG仍然是胶质瘤中最主要的细胞群****，大约占比****65%左右****，其中出现了一群****单核巨噬细胞相关细胞群****，在女性中有23%，男性有28%，在不同性别中，我们均发现了三个单核细胞亚群包括****Ly6c2 high, Ccr2 high, andTgfbi low的传统单核细胞群****，以及****处于单核细胞和巨噬细胞****中间的****Ly6c2 high and Tgfbi high****，以及****巨噬细胞相关特征****的****Ly6c2low, Ifitm2high, Ifitm3- high, and S100a6high****的细胞群，并且还发现了一小部分NK细胞，DC细胞，NKT细胞以及B,T细胞相关的细胞群。**

![](../../images/e0d62a3fa67b8a38.webp)

![](../../images/9f7c3a59b3b13ed0.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
DimPlot(F_CTRL,label =T,cols =c("#A7EFFB","#53649A","#9C48BA","#7FBAE2","#F5BD07","#18CDA8","#504286","#F5BBA7","#FCEE28","#683C9E","#3A5E81","#C49B74","#D071A0","#FEE6F0","#3BA2C1","#FFF1E2"),group.by= "celltype")+ggtitle("CTRL_F")

Figure2_F_CTRL <- subset()View(F_CTRL)F_Tumor <- subset(Glia,idents ="F_Tumor" )DimPlot(F_Tumor,label = T,cols =c("#A7EFFB","#53649A","#9C48BA","#7FBAE2","#F5BD07","#18CDA8","#504286","#F5BBA7","#FCEE28","#683C9E","#3A5E81","#C49B74","#D071A0","#FEE6F0","#3BA2C1","#FFF1E2"),group.by= "celltype")+ggtitle("F_Tumor")
M_CTRL <- subset(Glia,idents ="M_CTRL" )DimPlot(M_CTRL,label = T,cols =c("#A7EFFB","#53649A","#9C48BA","#7FBAE2","#F5BD07","#18CDA8","#504286","#F5BBA7","#FCEE28","#683C9E","#3A5E81","#C49B74","#D071A0","#FEE6F0","#3BA2C1","#FFF1E2"),group.by= "celltype")+ggtitle("CTRL_M")

M_Tumor <- subset(Glia,idents ="M_Tumor" )DimPlot(M_Tumor,label = T,cols =c("#A7EFFB","#53649A","#9C48BA","#7FBAE2","#F5BD07","#18CDA8","#504286","#F5BBA7","#FCEE28","#683C9E","#3A5E81","#C49B74","#D071A0","#FEE6F0","#3BA2C1","#FFF1E2"),group.by= "celltype")+ggtitle("M_Tumor")         ctrl_gene_panel <- c("Cd14", "Tmem119","P2ry12", "Csf1", "Crybb1", "Mcm5","Ifit3", "Tgfbi",                      "Ifitm2","Ifitm3", "S100a6", "Ly6c2", "Ccr2","Mrc1", "Cd163", "Cd24a",                      "Ncam1")DotPlot(F_CTRL, features =DotPlot(sex_condition_objects$f_ctrl, features =            rev(annot[match(ctrl_gene_panel, annot$Gene.name),"Gene.stable.ID"])) +         RotatedAxis() +       theme(legend.position="top")           ctrl_gene_panel) +   RotatedAxis() +  theme(legend.position="top")
```

![](../../images/d19de8406a001fbc.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
Idents(F_CTRL) <-F_CTRL$RNA_snn_res.0.3F_CTRL <-RenameIdents(F_CTRL,"0"="MG","1"="MG","2"="MG","3"="MG","4"="MO-Ma","5"="BAM","6"="MG","7"="NKT","8"="MO","9"="MG","10"="MG","11"="DCs","12"="B","14"="Pre_MG","15"="Endothelia ")F_CTRL$celltype1 <- Idents(F_CTRL)table(F_CTRL$RNA_snn_res.0.3)freq <- data.frame(celltype = F_CTRL$celltype1)library(dplyr)View(freq)freq <- freq %>%  group_by(celltype) %>%  count() %>%  ungroup %>%  mutate(per = `n`/sum(`n`))freq$cell_type <- factor(freq$celltype, levels= c("MG","MO-Ma", "BAM", "NKT", "MO",                                                  "DCs", "B", "CD8_T","Pre_MG","Endothelia"))freq$label <- scales::percent(freq$per)library(tidyverse)cf<-ggplot(freq,            aes(x="", y=per,fill=celltype))+  geom_bar(stat="identity",width=1, color="white")+  coord_polar("y", start=0)+  scale_fill_manual(values=c(micro,Mo_Mg,BAM, NK,Mo,DC,Bcells, NKT,pre_micro,ncam))+  theme_light()+  geom_label_repel(aes(label = label),size=3, show.legend = F, nudge_x = 1)
Idents(M_CTRL) <- M_CTRL$RNA_snn_res.0.3M_CTRL <-RenameIdents(M_CTRL,"0"="MG","1"="MG","2"="MG","3"="MG","4"="MO-Ma","5"="BAM","6"="MG","7"="NKT","8"="MO","9"="MG","10"="MG","11"="DCs","12"="B","13"="CD8_T","14"="Pre_MG","15"="Endothelia                     ")M_CTRL$celltype1 <- Idents(M_CTRL)table(F_CTRL$RNA_snn_res.0.3)freq_M_CTRL <- data.frame(celltype = M_CTRL$celltype1)library(dplyr)View(freq)freq_M_CTRL <- freq_M_CTRL %>%  group_by(celltype) %>%  count() %>%  ungroup %>%  mutate(per = `n`/sum(`n`))freq_M_CTRL$cell_type <- factor(freq_M_CTRL$celltype, levels=c("MG", "MO-Ma", "BAM", "NKT","MO",                                                 "DCs", "B", "CD8_T","Pre_MG","Endothelia"))freq_M_CTRL$label <- scales::percent(freq_M_CTRL$per)library(tidyverse)cf_M_CTRL<-ggplot(freq_M_CTRL,            aes(x="", y=per,fill=celltype))+  geom_bar(stat="identity",width=1, color="white")+  coord_polar("y", start=0)+  scale_fill_manual(values=c(micro,Mo_Mg,BAM, NK,Mo,DC,Bcells, NKT,pre_micro,ncam))+  theme_light()+  geom_label_repel(aes(label = label),size=3, show.legend = F, nudge_x = 1)
Idents(F_Tumor) <- F_Tumor$RNA_snn_res.0.3F_Tumor <-RenameIdents(F_Tumor,"0"="MG","1"="MG","2"="MG","3"="MG","4"="MO-Ma","5"="BAM","6"="MG","7"="NKT","8"="MO","9"="MG","10"="MG","11"="DCs","12"="B","13"="CD8_T","14"="Pre_MG","15"="Endothelia                     ")F_Tumor$celltype1 <- Idents(F_Tumor)freq_F_Tumor <- data.frame(celltype = F_Tumor$celltype1)freq_F_Tumor <- freq_F_Tumor %>%  group_by(celltype) %>%  count() %>%  ungroup %>%  mutate(per = `n`/sum(`n`))freq_F_Tumor$cell_type <- factor(freq_F_Tumor$celltype, levels=c("MG", "MO-Ma", "BAM", "NKT","MO",                                                               "DCs", "B", "CD8_T","Pre_MG","Endothelia"))freq_F_Tumor$label <- scales::percent(freq_F_Tumor$per)library(tidyverse)cf_M_CTRL <- ggplot(freq_M_CTRL,                   aes(x="",y=per, fill=celltype))+  geom_bar(stat="identity",width=1, color="white")+  coord_polar("y", start=0)+  scale_fill_manual(values=c(micro,Mo_Mg,BAM, NK,Mo,DC,Bcells, NKT,pre_micro,ncam))+  theme_light()+  geom_label_repel(aes(label = label),size=3, show.legend = F, nudge_x = 1)  cfIdents(M_Tumor) <- M_Tumor$RNA_snn_res.0.3M_Tumor <-RenameIdents(M_Tumor,"0"="MG","1"="MG","2"="MG","3"="MG","4"="MO-Ma","5"="BAM","6"="MG","7"="NKT","8"="MO","9"="MG","10"="MG","11"="DCs","12"="B","13"="CD8_T","14"="Pre_MG","15"="Endothelia                     ")M_Tumor$celltype1 <- Idents(M_Tumor)freq_M_Tumor <- data.frame(celltype = M_Tumor$celltype1)freq_M_Tumor <- freq_M_Tumor %>%  group_by(celltype) %>%  count() %>%  ungroup %>%  mutate(per = `n`/sum(`n`))freq_M_Tumor$cell_type <- factor(freq_M_Tumor$celltype, levels=c("MG", "MO-Ma", "BAM", "NKT","MO",                                                                 "DCs", "B", "CD8_T","Pre_MG","Endothelia"))freq_M_Tumor$label <- scales::percent(freq_M_Tumor$per)library(tidyverse)cf_M_Tumor <- ggplot(freq_M_Tumor,                      aes(x="",y=per, fill=celltype))+  geom_bar(stat="identity",width=1, color="white")+  coord_polar("y", start=0)+  scale_fill_manual(values=c(micro,Mo_Mg,BAM, NK,Mo,DC,Bcells, NKT,pre_micro,ncam))+  theme_light()+  geom_label_repel(aes(label = label),size=3, show.legend = F, nudge_x = 1)
```

**根据自己的思路出图：**

**![](../../images/25d5dcdd3e85e36a.webp)**

**样本信息是四个样本分别是雄性胶质瘤样本，雄性正常样本，雌性胶质瘤样本，雌性正常样本经过 CD11b富集的细胞分群。****分群依据根据MG细胞表达：Cx3cr1+/Tmem119+。Monocyte:Ccr2+/Ly6c2+。Macrophage:Mrc1+,T/NKT:Cd3d+,Nkg7，Endothelial：Cldn5+Flt1+. B Cell:Cd79a,还有一群S100a8+S100a9+的细胞.**

**![](../../images/5516d47a47c8504c.webp)**

从图上可以看出**T****细胞会在胶质瘤样本中浸润， 那可以看一下胶质瘤浸润的 CD11b+的T细胞是什么细胞？**

并且我们也可以看出**肿瘤样本组和对照样本 MG群有很大差别**，所以做亚群细分可能能得到在胶质瘤样本中特异性的MG细胞亚群，那这群MG和胶质瘤肯定是比较相关的。巨噬细胞在对照样本和肿瘤样本中好像差异不是很大。S100a8细胞，内皮细胞在两组中都存在，同样单核细胞大都也是胶质瘤中特有产生的，所以，**从这幅图得到的有效信息， CD11b+的细胞群中，T细胞，单核细胞的出现大都和胶质瘤相关，内皮细胞，S100a8以及巨噬细胞在两组样本中变化不大。**

**![](../../images/040b17ad456d8f8e.webp)**

在不同性别中的比较中，我们能得到的结论是两组差异并不大，可能 T细胞分群上女性会多于男性。

![](../../images/d4088f04ebeff125.webp)

对细胞群根据基因表达情况进一步细分：

![](../../images/1c0d07e24f73f89e.webp)

**![](../../images/109cf9c055e5c153.webp)**

**![](../../images/9e9112ebdafa6c0e.webp)**

**比较对照和胶质瘤样本可知，在胶质瘤样本中小胶质细胞表达一些突触呈递相关的小胶质细胞以及 Mi67表达的增殖的小胶质细胞数目增多**，而**Jun,Junb,Fos****高表达的小胶质细胞以及传统的小胶质细胞以及免疫抑制因子 Bmp2k表达的小胶质细胞数目减少**，巨噬细胞数目变化不大，单核细胞数目明显增多，也就是单核细胞-单核巨噬过渡态细胞-巨噬细胞这三类分化过程细胞均明显增加，S100A8-S100A9细胞数，内皮细胞数目变化不大，T细胞数目明显增多，B细胞数目有所增加但是增加不是很多。

**复现Figure2 : Assessment of new and known cell type-specific markers**

**![](../../images/e99338d8c04da85f.webp)**

![](../../images/7d3464cde408caca.webp)

  *   *   *   *   *   *   *   *

```r
aa<-c("#55B1E2","#FAC100","#0CD2AF","grey","grey","grey","grey","grey","grey","grey","grey","grey")DimPlot(F_CTRL,cols = aa)+NoLegend()DimPlot(M_CTRL,cols = aa)+NoLegend()DimPlot(F_Tumor,cols = aa)+NoLegend()DimPlot(Total,cols = aa)+NoLegend()DimPlot(M_Tumor,cols = aa)+NoLegend()
```

**图 a:取除MG，MO/MA和BAM三群细胞进一步分析。即对CD11b+的小胶质细胞，单核细胞，边界巨噬细胞三群细胞分析得到UMAP图。**

**![](../../images/1614fcfea889bea3.webp)**

**图 b：三群细胞的marker基因以热图的形式展示。这些基因可以稍微记一下。****从图上可以得到的有效信息是****Tmem119,Cx3cr1,P2ry12,Gpr34,Olfml3,Sparc****这些基因特异性在小胶质细胞中表达，其中****Cd81****在小胶质细胞和 CNS边界巨噬细胞都会表达，以及****Cst3,Hexb****这两个基因这在三群细胞多多少少都有表达，在****MO/MA****这群除了先前已知会高表达****Ifitm2/S100a6/S100a11****之外，我们还发现他会特异性表达****Ms4a4****， Lgals3,Crip1,Isgl5****基因，从图上可以看到 Ifitm3基因其实是不特意的，从CNS边界巨噬细胞基因表达可以看到其中表达的****Apoe****， Ms4a7，Wfdc17****并不是很特意表达，但是在 CNS边界巨噬细胞特异性表达的基因有****Pf4,Mrc1.Dab2,F13a1****基因。**

**![](../../images/b5d75623dea72601.webp)**

**![](../../images/e7607be2ed134754.webp)**

  *   *   *   *

```
FeaturePlot(MO_MA_MG,features ="Ptprc") + scale_color_gradientn(colors=viridis::viridis(n=50)) +  ggtitle("Ptprc")
```

**图 c,d,e三幅图结果显示结合单细胞转录组信息即RNA信息和流式蛋白信息显示Tmem119即小胶质细胞低表达CD45，而Gal-3即Monocyte高表达CD45。****我们想比较特异的从胶质瘤的 TME中把小胶质细胞和MO/MA细胞提取出来，其中从单细胞转录组上挑出了Tmem119基因作为Microglia的特征性基因，将Lgals3基因作为MO/MA的特征基因，****Lgals3****基因编码 Gal-3蛋白可以调控IL-4的表达，激活巨噬细胞，参与肿瘤免疫抑制中****。从流式结果上可以看到 Tmem119+的细胞占比75.2%，Gal3+的细胞占比15%，同样也还有3.4%的双阳细胞，这些数据结果与单细胞转录组数据结果是一致的，与CD45共标发现，****Tmem119+****的小胶质细胞大都低表达 CD45,而Gal3单核细胞细胞大都高表达CD45。**

**![](../../images/ea5d2266fadd0f08.webp)**

![](../../images/0e87145470f2f23e.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
gene_expression_data<-as.data.frame(MO@assays$RNA@data )metadata <- as.data.frame(MO@meta.data)gene_expression_data <- merge(gene_expression_data,metadata,by.x=0,by.y=0)View(gene_expression_data)View(gene_expression_data)gene_expression_data <- t(gene_expression_data)gene_expression_data <- gene_expression_data[genes,]identical(rownames(gene_expression_data),rownames(MO@meta.data))graphs<-list()for (i in seq_along(genes)){ names<-c("Ccr2","Ly6c2", "Ly6i", "Tgfbi",           "Ccl5","Cd274(PD-L1)", "Ccl22", "Itga4(CD49d)")  plot<- ggplot(gene_expression_data,                aes(x="", fill= celltype)) +   geom_density(aes_string(x=as.name(genes[i])), trim=T, alpha=0.8,size=0.5)+    scale_fill_manual(values= c("#FFDB3F", "orange", "#F0627C"))+    labs(title=names[i], x="",y="")+    ylim(0,1)+    theme_classic()+    theme(legend.title = element_blank())  graphs[[i]] <- plot}ggarrange(plotlist=graphs, ncol=2, nrow=4, common.legend = T, legend ="top")
```

图F，揭示在Monocyte向Macrophage转化过程中基因表达的变化关系。**认为****Ly6c2和Ccr2基因高表达****的细胞是****Monocyte****，而****Ly6c2和TGfbi高表达****则认为是****单核向巨噬细胞转变过程中的中间态细胞****，以及剩余的因为它即表达单核细胞****Ly6c2/Ccr2基因****但是也表达巨噬细胞的特征基因比如****Ifitm2/S100a6/S100a11基因****，所以认为是****巨噬细胞****。从g图上峰峦图可以看出****Ccl5/Ccl22两类趋化因子基因在MA中特异性高表达****，也就是说MA细胞特异性高表达趋化因子和T细胞的循环招募相关，****所以也就是说在胶质瘤中单核细胞向巨噬细胞转变后，转变完成的巨噬细胞表达一些趋化因子可以招募T细胞过来****，还发现它高表达****CD274编码免疫检查点蛋白1即PD-L1蛋白****，这些基因的表达提示我们就是这群MA细胞很可能介导免疫抑制反应，CD274也主要在MA中高表达，所以说这群转化完成的MA介导免疫抑制反应。讲清楚这三类细胞在基因表达上的差异，即为在胶质瘤中转化上的关系，解释清楚胶质瘤中特异性产生的单核细胞在胶质瘤的发生发展过程中执行的生物学功能。**

**![](../../images/14ac01f292f151bc.webp)**

图 h，结合流式分析，揭示CD49d和PD-L1的表达与CD45之间的关系。**结合流式结果反应 PD-L1即免疫检查点蛋白主要在CD11b+CD45高表达的免疫细胞中表达，根据Ly6c基因和PD-L1蛋白在CD45高表达的细胞中表达，那说明胶质瘤免疫浸润细胞和外周髓系细胞有很大差别，其中MO-MA之间的Inte cell，这群细胞会表达Ly6c但是PD-L1表达少，以及PD-L1高表达的MA细胞低表达Ly6c所以通过这两个基因的表达以及流式的验证能较好的将胶质瘤浸润的MO-MA中间态细胞和MA细胞区分开。我们还发现了一些在单核/巨噬细胞中特异性高表达的一些基因比如Itga4/Hp/Emilin2/Sell/Gda基因，其中Itga4基因编码产生CD49d，从单细胞数据上发现他比较特异性在Cd274高表达的MA细胞群中表达，**

**![](../../images/a0957887a6d8ba53.webp)**

图 i,图j揭示在单核细胞群中CD45-PD-L1-CD49d之间的关系，图j对单核细胞分出三个小的亚群。**但是结果不是这样子的，实际用流式分析发现， Cd49d蛋白72.1%在CD11b+CD45高表达细胞群中表达，但是从i图发现大部分蛋白却在Ly6c那群细胞中表达。****Hp,Emilin2,Sell,Gda基因在RNA水平以及蛋白水平均在MO那群细胞中表达。在文献中认为Tgm2/Gpnmb基因在先前研究中主要集中于在不同的胶质瘤中均在GAM中表达，但是在我们数据中发现会在MO/MA中表达。**

**复现Figure3:Distinct gene expression profiles of glioma-associated microglia and monocytes/macrophages.**

**![](../../images/e86aaf94a144bf3f.webp)**

![](../../images/3963898d7676d559.webp)

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```r
DimPlot(MO_MA_MG,group.by ="CT",cols =c("#616974","#F44687"))+ggtitle("CTRL_Tumor")gene_expression_data<- MO_MA_Mgenes_micro01<-c("Tmem119", "P2ry12","Cx3cr1", "Olfml3", "Sparc","Gpr34")gene_expression_data_micro <- MO_MA_MG_d[genes_micro01, ]MO_MA_MG$micro_score <- colMeans(gene_expression_data_micro)
genes_macro01<-c("Ifitm2", "S100a6","S100a11", "Lgals3", "Isg15", "Ms4a4c","Crip1")gene_expression_data_macro <- MO_MA_MG_d[genes_macro01, ]MO_MA_MG$macro_score <- colMeans(gene_expression_data_macro)
# Feature PlotsFeaturePlot(MO_MA_MG, features = "micro_score",cols =c("grey","red"))+ggtitle("MG_score")FeaturePlot(MO_MA_MG, features = "macro_score",cols =c("grey","red"))+ggtitle("MA_score")cell_types_labels <- c("MG", "MA") names(cell_types_labels) <-c("MG", "MA")
scores_data <- data.frame(micro01 = MO_MA_MG$micro_score, macro01 =MO_MA_MG$macro_score,                           condition =MO_MA_MG$CT,                         cell_types_3_groups = Idents(MO_MA_MG))
View(scores_data)MG<-ggplot(scores_data[scores_data$cell_types_3_groups %in%c("MG", "MA"),],            aes(x=condition, y= micro01))+  geom_violin(aes(fill=condition), scale= "area", trim=F, size=0.5)+  facet_grid(.~cell_types_3_groups,labeller = labeller(cell_types_3_groups=cell_types_labels))+  xlab("")+  ylab("MG score")+  scale_fill_manual(values=c(col_CTRL,col_TUMOR))+  theme_classic(base_size=14)MoM<-ggplot(scores_data[scores_data$cell_types_3_groups %in%c("MG", "MA"),],             aes(x=condition, y= macro01))+  geom_violin(aes(fill=condition),scale="area", trim=F, size=0.5)+  facet_grid(.~cell_types_3_groups,labeller = labeller(cell_types_3_groups = cell_types_labels))+  xlab("")+  ylab("MoM score")+  scale_fill_manual(values=c(col_CTRL,col_TUMOR))+  theme_classic(base_size=14)
```

**图 A即是对MG/MO&MA/BAM三群细胞根据实验样本进行分群，结果发现，从图上看出好像正常样本的Control主要是Hom-MG样本，而胶质瘤中的MG主要是Activate MG样本，其中根据MG的marker基因和MO&MA的marker基因构成基因集对不同类型细胞做基因集评分结果可以看到就是对照组和胶质瘤组对传统的MG/MO&MA都是不一样的，其实这里就是想说在胶质瘤中的小胶质细胞也好还是单核巨噬细胞也好是不一样的。**

![](../../images/a262af1203218314.webp)

这个热图是想比较不同时间条件下对照和肿瘤样本和不同的细胞中基因表达上的差异。后面就做了免疫染色验证数据结果。通过Tmem119/Gal-3对胶质瘤进行免疫染色，结果显示Tmem119+的小胶质细胞主要存在于肿瘤组织的边缘，而Gal-3+的单核细胞则主要存在于肿瘤组织内部。尽管小胶质细胞在胶质瘤诱导下会被激活丢失一部分小胶质的特征基因，但是他们其实还是维持小胶质细胞相关特征基因的表达的。

Transcriptional networks induced in microglia by glioma are present and more pronounced in infiltrating monocytes/macrophages.

![](../../images/ba9eaa394d17fe2b.webp)

![](../../images/cb4d80d924475067.webp)

他这里是Act_MG在hom_MG中的特异性基因和MOM基因去作比较。

图a，目前已知一群Act MG以及MO/MA这两群细胞是和胶质瘤十分相关的两群细胞，我们向知道与传统MG相比，ActMG会高表达哪些基因，结果我们发现有非常多的基因在Act MG细胞群和MO/MA群中都高表达，比如H2-Aa/H2-Ab1/H2-D1/H2-K1/这些表达MHCII相关的基因以及Ifitm3干扰素γ以及一些Ccl3/Cc2等细胞趋化因子在Act MG中高表达，而在MO/MA中高表达Ccl5，Ifitm2等。接下去对不同细胞群的差异基因做富集分析，结果显示在ActMG中高表达基因富集在细胞质翻译，其他的一些在两组是相同的，比如在Act MG和MO/MA的高表达基因都会富集在对细菌的反应，对干扰素γ的反应，并且在MO/MA群还富集到对干扰素β的反应。并且与MHCII相关的基因在Act MG中高表达的基因，则富集在对抗原的层递上。

![](../../images/29a14732bc40298a.webp)

![](../../images/8c1a947eda9b7617.webp)

我做的富集是基于在Act MG相对于MO特异性表达的通路和在MO中富集特异性通路，以及两者共同的基因富集的通路，这样子可能更好说明两群细胞之间的关系，这里Act MG是相对于Hom来说的，而MO是相对于Act MG来说的。

![](../../images/c52c7545fc11067d.webp)

![](../../images/29101c90cba3ab0f.webp)

![](../../images/b31c50733fc129c0.webp)

图f作者展示了一些在MO/MA相较于MG特异性高表达的一些基因，其中CD52则对T细胞的激活和增殖的刺激因子。Stat1是干扰素信号的介质，Isgl5则稳定Stat1防止炎症反应过早发生。Usp18负向调控Stat1基因。所以从可以知道这两类类细胞都是免疫反应细胞，但是MO/MA的作用会更强一些，以及在MO/MA中还表达炎症因子白介素1β，以及一些促炎因子抑制分子Il1rn,Il18b基因，还表达PD-L1基因Cd274所以在MO/MA中还会上调免疫抑制相关信号通路。图h是scSVA一种比UMAP定群更能体现单细胞扩散的一种数据降维分析方法，结果显示scSVA结果和之前umap降维结果相似，但是从表达模式上可以得出有MO-MO/MA-MA的转变过程。

01

二、测试文件及代码

如果你也想学习本文的代码和思路，我们给大家准备好了测试文件和代码。

链接：https://pan.baidu.com/s/1OVT0hwCh6ANZ47jPNrmEIA?pwd=3tvj

提取码：3tvj

![](../../images/55364ef3dbf4af47.jpg)

02

三、合作方介绍

****本次活动由**Biomamba生信基地** 组织主办、**北京寻因生物科技** 有限公司独家冠名、科研者之家、西柚云超算联合赞助，设立总价值约**50W** 的科研助力基金。
北京寻因生物科技有限公司：

北京寻因生物科技有限公司（简称寻因生物）成立于2018年，秉承“用技术温暖生命，预见未来”的企业愿景，致力于全球单细胞市场标准普世化发展，推动单细胞技术在早筛、临床、药研等应用方向的深耕落地，为全球科学家、技术公司及药企工业等客户提供可信赖的高品质单细胞技术服务及实验室建设解决方案。

科研者之家：

科研者之家（www.home-for-researchers）是目前国内最知名的科研工具箱平台，以“科研不停，神器不止”为理念，自2019年上线以来，多款工具火爆科研界，如AI写作助手、Figdraw在线绘图平台、生信零代码平台、AI润色、DLP一键改写降重、中文版Pubmed、课题思路助手等。截止目前，包括Nature，Advanced Materials等顶级期刊在内，科研者之家相关科研工具被论文引用已超2300次之多。

西柚云超算：

西柚云是一家专注于科研共享计算的云服务基建型公司。于2022年推出独立研发的大禹共享型计算系统，具有实例动态迁移（拒绝传统型共享服务器单节点卡顿）、开箱即用的生信环境、每个用户拥有[独立的实例和root权限](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503869&idx=1&sn=142f8c7ba8620815a8770773df077f12&chksm=9b3cb6adac4b3fbb1acdf7593df06af5ac77d1fe9c0144c999de7109bd063b76080a33c50e0d&scene=21#wechat_redirect>)等特性。

03

四、往期作品回顾

[干细胞样CD4+ T细胞与自身免疫性血管炎](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506684&idx=1&sn=c27703a05d4fffae6a5e9e54b4fa7dfe&chksm=9b3ca3acac4b2abaa1e5d4f4a7e4d0730f2e5c4d72c7b3d3d29a653c3bae6590d90e31908dde&scene=21#wechat_redirect>)
[结直肠癌免疫图谱中的基因表达程序](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506720&idx=2&sn=4760277df5a7b6f0d6d1698ac734aa3b&chksm=9b3ca270ac4b2b66b0330e822893fa233ba3bdfd45d857097fba6e86561196c1497c20db25b8&scene=21#wechat_redirect>)
[MLP模型鉴定免疫细胞发育和瘤内T细胞耗竭的单细胞染色质图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506754&idx=1&sn=3e3e9b4857bb0371b7c1113df792df2e&chksm=9b3ca212ac4b2b043baf0c72684d186a1c065ff7b3d865c308aff4f3483ab5923638fda8d1ff&scene=21#wechat_redirect>)
[T Cell单细胞参考图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506779&idx=1&sn=dc97a74cfac6caeabaa838160385c3b2&chksm=9b3ca20bac4b2b1da51998764b22ac3c08415298a47ded14283337386f18f9548749de70725e&scene=21#wechat_redirect>)
[小鼠纹状体单细胞基因变化图谱](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506900&idx=1&sn=83774f3062e42ca0eee1df2cf19144f0&chksm=9b3ca284ac4b2b9221736162ac44280d6184c9f8b0cc13bbcc4c914c14b707fe13a850c6418e&scene=21#wechat_redirect>)
[人类肾脏snRNA-seq图谱拟时序分析](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506960&idx=1&sn=9f5913231f9583411e47ccf0dcadedf6&chksm=9b3ca540ac4b2c56a60b5f71ab32e1eacd3194af4bfef819b2de60fc50781360876b45837bf7&scene=21#wechat_redirect>)
[CellRank的教程重现](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247507012&idx=1&sn=fb01cca63326fd6e8c682434a53fc2ea&chksm=9b3ca514ac4b2c02115ae5dea368190ce74997ac16a07fdc29f76cef815600b1e5b813c71163&scene=21#wechat_redirect>)

04

**本次活动最终解释权归主办方所有!********主办方拥有对作品的编辑、宣发权利!**

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
