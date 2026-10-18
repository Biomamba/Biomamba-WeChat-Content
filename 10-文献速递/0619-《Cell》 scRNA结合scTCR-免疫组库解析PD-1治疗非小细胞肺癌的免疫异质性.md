---
title: "《Cell》| scRNA结合scTCR-免疫组库解析PD-1治疗非小细胞肺癌的免疫异质性"
date: 2025-09-12
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531049&idx=1&sn=f33b115a5abeffcbeb12ed75427e6951&chksm=9b3c0379ac4b8a6ff58146ba47211c7aa52a8252080dd8032dbda05dca78a215a4b692d7ad83#rd
albums: ["文献速递"]
---

# 《Cell》| scRNA结合scTCR-免疫组库解析PD-1治疗非小细胞肺癌的免疫异质性

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247531049&idx=1&sn=f33b115a5abeffcbeb12ed75427e6951&chksm=9b3c0379ac4b8a6ff58146ba47211c7aa52a8252080dd8032dbda05dca78a215a4b692d7ad83#rd
> 合集：文献速递

**一、写在前面**

今天我们要深入剖析这篇发表在《Cell》上的关于抗 PD-1 治疗非小细胞肺癌（NSCLC）免疫异质性的研究，题目为"A single-cell atlas reveals immune heterogeneity in anti-PD-1-treated non-small cell lung cancer"，最新影响因子42.5。这篇文章无论是研究设计、技术应用还是学术结果陈述，都堪称生信与肿瘤免疫交叉领域的教科书式范文，对大家未来的硕博研究和论文发表都有极强的借鉴意义。
该研究由多所国内顶尖院校和医院的团队联合完成——自北京大学、中国医学科学院肿瘤医院、同济大学附属上海肺科医院、广东省人民医院等机构。该作者团队在肿瘤免疫、单细胞测序技术开发与应用、临床样本资源整合等方面具备深厚积累。
这篇文章解决了抗 PD-1 治疗 NSCLC 领域的两个关键科学问题：一是明确了抗 PD-1 治疗后 NSCLC 肿瘤免疫微环境（TIME）的异质性分型及与治疗响应的关联；二是发现了可预测非主要病理缓解（non-MPR）患者复发风险的免疫标志物，为临床患者分层和个体化治疗提供了重要依据。同时，研究采用了scRNA-seq结合 scTCR-seq的前沿技术，整合了 234 例大样本临床数据，研究设计严谨、结果可靠，符合《Cell》对高质量研究的定位。scRNA-seq分析教程可见：[scRNA-seq小学期](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)scTCR&BCR免疫组库教程可见：[单细胞免疫组库测序(scTCR+scBCR)学习手册](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>)
原文链接: https://pubmed.ncbi.nlm.nih.gov/40147443/DOI: 10.1016/j.cell.2025.03.018 ![](../../images/1e3e939bd7f58295.webp)**如果需要[ 单细胞数据分析](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)**教学** 、生信热点**[全文复现](<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAwMzIzOTk5OQ==&action=getalbum&album_id=2981710763847614469#wechat_redirect>)** 、自测数据**个性化分析** 辅导、[常态化实验学习](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530174&idx=1&sn=c3b0499adcc9093546e4ba1cfffba7bd&scene=21#wechat_redirect>)，欢迎联系客服微信[**Biomamba_zhushou**]**

**二、研究思路**

该研究采用 “临床样本 - 单细胞测序 - 多维度分析 - 临床验证” 的研究思路，方法归纳为以下 4 类：

### （一）临床样本与数据收集

  1. **样本筛选** 纳入 334 例新诊断、可切除的 NSCLC 患者（245 例鳞癌 LUSC，89 例腺癌 LUAD），均接受抗 PD-1 联合化疗的新辅助治疗，排除 EGFR 突变或 ALK 重排患者（这类患者更适合靶向治疗）；最终对 234 例患者的术后肿瘤样本进行 [scRNA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)/[TCR-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>) 分析。
  2. **病理评估** 根据术后肿瘤床中残留存活肿瘤（RVT）比例划分患者：RVT≤10% 为主要病理缓解（MPR，含 RVT=0% 的病理完全缓解 pCR），RVT≥10% 为 non-MPR，以此作为治疗响应的核心指标。
  3. **随访数据** 收集 159 例患者的无复发生存期（RFS）数据（中位随访 19.48 个月），用于后续生存分析。

### （二）单细胞测序与数据预处理

  1. **测序技术** 采用 10× Genomics Chromium 平台进行[ scRNA-seq ](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)和 [scTCR-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>)，获取单细胞基因表达数据和 T 细胞受体克隆信息。
  2. **质量控制** 过滤低质量细胞（UMI 计数 1200-40000、检测基因数 600-6000、线粒体基因比例 < 15%），使用 Scrublet 去除双细胞，最终获得 125.4 万个 CD45 + 免疫细胞用于后续分析。
  3. **细胞分型** 基于经典 [marker 基因](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504843&idx=1&sn=b795a3e36ae092d8f87abb5a87187828&scene=21#wechat_redirect>)（如 CD3D/CD3G 标记 T 细胞、CD79A/CD19 标记 B 细胞、NKG7 标记 NK 细胞），结合无监督聚类（Leiden 算法）和 UMAP 降维，将免疫细胞分为 51 个亚型（24 个 T/NK 细胞亚型、10 个 B 细胞亚型、17 个髓系细胞亚型）。

### （三）多维度数据分析

  1. **TIME 分型** 采用非负矩阵分解（NMF）对 222 例患者（排除免疫细胞数 < 500 的 11 例）的免疫细胞亚型比例进行聚类，通过 200 次重采样验证（Down-sampling）确定最优聚类数为 5，最终划分出 5 种 TIME 亚型。
  2. **T 细胞克隆分析** 定义 “克隆扩增 T 细胞” 为同一 TCR 克隆型细胞数≥3；基于 [scTCR-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>) 数据，识别 “Tex 相关细胞”（与终末耗竭 T 细胞 Tex 共享 TCR 的 CD8+T 细胞），并进一步分为 “前体耗竭 T 细胞（Texp）” 和 “终末耗竭 T 细胞（terminal Tex）”；同时分析 CCR8 + 调节性 T 细胞（Treg）的克隆扩增特征。
  3. **生存分析** 采用 Kaplan-Meier 法绘制生存曲线，通过 Log-rank 检验比较不同亚组的 RFS 差异；使用单因素 / 多因素 Cox 比例风险模型分析免疫特征与 RFS 的关联；通过时间依赖 ROC 曲线评估免疫标志物的预测效能。

### （四）实验验证

  1. **免疫组化（IHC）与多重免疫荧光（mIF）** 对 FFPE 样本进行 CD20、CCR8、FOXP3 等标志物染色，验证 B 细胞聚集（三级淋巴结构 TLS）、CCR8+Treg 的丰度等关键结果。
  2. **体外功能实验** 采用 NK92 细胞（人 NK 细胞系）与化疗药物（卡铂、顺铂）预处理的肺癌细胞系（NCI-H460、NCI-H1299）共培养，验证 FGFBP2+NK/NK 样 T 细胞的细胞毒性。
  3. **外部数据集验证** 重新分析已发表的乳腺癌（GSE 数据集）、口腔鳞癌（GSE200996）和晚期 NSCLC（OAK 试验）数据集，验证关键免疫特征（如 FGFBP2 + 细胞、Texp 细胞）的临床意义。

**三、主要结果
**

研究结果围绕 “TIME 异质性 - 治疗响应 - 复发风险” 展开，我们按图逐一解析：

### ●（一）图 1：抗 PD-1 治疗 NSCLC 的肿瘤浸润免疫细胞大规模图谱

#### 1\. 核心目的

建立抗 PD-1 治疗后 NSCLC 的免疫细胞图谱，明确临床样本特征和病理响应分布。

#### 2\. 分析方法与结果解读

  * **图 1A（研究设计流程图）** 展示从 334 例患者入组（接受抗 PD-1 + 化疗）→手术切除肿瘤→病理评估（RVT% 计算）→对 234 例患者样本进行[scRNA](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530022&idx=2&sn=5c6aa081663719ce2f0f9b7f4d173c93&scene=21#wechat_redirect>)/[TCR-seq](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530826&idx=1&sn=f95a284a432695c9b8f6878cd3691bfc&scene=21#wechat_redirect>)的完整流程，清晰呈现研究设计的完整性。
  * **图 1B（H &E 染色图）**对比 MPR（左，残留肿瘤少）和 non-MPR（右，残留肿瘤多）患者的肿瘤床病理特征，直观展示病理评估的依据。
  * **图 1C（病理响应瀑布图）** 展示 334 例患者的 RVT% 分布，整体 MPR 率 57.2%（含 pCR 率 39.2%），说明抗 PD-1 + 化疗在该队列中的良好疗效；同时体现患者响应的异质性（RVT% 从 0 到 100% 均有分布）。
  * **图 1D（免疫细胞亚型 UMAP 图与分类）** 通过 [UMAP 降维](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247497867&idx=1&sn=37a539bbd37dafb6cce5cd52dec84f52&scene=21#wechat_redirect>)展示 51 个免疫细胞亚型的分布，按细胞大类（NK 细胞 /γδT 细胞 / ILC、CD8+T 细胞、CD4+T 细胞、B 细胞、髓系细胞）标注，每个亚型用不同颜色区分并列出各亚型的 marker 基因（如 CD8T_NK-like_FGFBP2、CCR8+Treg），为后续 TIME 分型奠定基础。

#### 3\. 关键结论

成功构建了目前规模最大的抗 PD-1 治疗 NSCLC 单细胞免疫图谱，明确患者病理响应存在显著异质性，为后续分析提供数据基础。

![](../../images/c8cb3486dbcc93f7.webp)

Figure 1

### ●（二）图 2：免疫细胞亚群丰度分析揭示 5 种 TIME 亚型

#### 1\. 核心目的

通过免疫细胞亚型比例聚类，划分 TIME 亚型，并分析各亚型与 MPR 率的关联。

#### 2\. 分析方法与结果解读

  * **图 2A（NMF 聚类热图）** 以 222 例患者的 CD45 + 免疫细胞亚型比例为输入，进行 NMF 聚类（rank=5）；热图中每行代表 1 个患者，每列代表 1 个免疫细胞亚型，颜色深浅表示细胞比例高低；右侧标注 5 种 TIME 亚型对应的 “细胞模块”（如 TIME-NK 对应 NK 细胞富集，TIME-BE 对应 B 细胞富集），清晰展示分型依据。
  * **图 2B（各 TIME 亚型的 MPR 率柱状图）** 统计 5 种 TIME 亚型的患者数量和 MPR 率：TIME-NK（29 例，75.9%）、TIME-BE（51 例，68.6%）、TIME-Teff（86 例，64.0%）的 MPR 率显著较高；TIME-Treg（31 例，6.5%）、TIME-Mye（25 例，36.0%）的 MPR 率显著较低。教程可参考：[沉浸式统计细胞比例](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&scene=21#wechat_redirect>)
  * **图 2C（不同病理类型的 MPR 率对比）** 按 LUSC 和 LUAD 分层分析各 TIME 亚型的 MPR 率，发现仅 TIME-Teff 亚型中，LUSC（75.0%）的 MPR 率显著高于 LUAD（38.5%），其他亚型无显著差异；说明病理类型对治疗响应的影响依赖于 TIME 亚型，为临床个体化治疗提供参考。

#### 3\. 关键结论

首次在抗 PD-1 治疗 NSCLC 中划分出 5 种具有不同免疫特征和治疗响应的 TIME 亚型，其中 NK/B 细胞 / 效应 T 细胞富集的亚型（TIME-NK、TIME-BE、TIME-Teff）治疗响应更佳，Treg / 髓系细胞富集的亚型（TIME-Treg、TIME-Mye）响应较差。

![](../../images/5a687a5b93d9f4ad.webp)

Figure 2

### ●（三）图 3：TIME-NK 患者中富集 FGFBP2+NK/NK 样 T 细胞

#### 1\. 核心目的

解析 TIME-NK 亚型的关键免疫细胞特征，明确其与 MPR 的关联机制。

#### 2\. 分析方法与结果解读

  * **图 3A（NK/NK 样 T 细胞亚型 UMAP 图）** 聚焦 NK 细胞、NK 样 T 细胞和 ILC，通过 UMAP 展示 3 个关键亚型：NK_CD16low_GZMK、NK_CD16hi_FGFBP2、CD8T_NK-like_FGFBP2，每个亚型用不同颜色标注，体现细胞亚群的异质性。
  * **图 3B（FGFBP2 +[ 细胞比例箱线图](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247503971&idx=2&sn=7dafb1e743ebbb95e488d8d1b7024448&scene=21#wechat_redirect>)）**比较 5 种 TIME 亚型中 FGFBP2+NK/NK 样 T 细胞（NK_CD16hi_FGFBP2 和 CD8T_NK-like_FGFBP2）在 CD45 + 细胞中的比例，发现 TIME-NK 亚型中该细胞比例显著最高；采用 Wilcoxon 检验（校正 Benjamini-Hochberg）验证差异，保证统计可靠性。
  * **图 3C（marker 基因表达 UMAP 图）** 展示关键基因在 NK/NK 样 T 细胞中的表达：CD3D/CD8A（CD8+T 细胞 marker）、GNLY/KLRD1（NK 细胞 marker）在 CD8T_NK-like_FGFBP2 中均高表达，证实其 “NK 样 CD8+T 细胞” 身份；PRF1/GZMB（细胞毒性 marker）在 FGFBP2 + 亚型中高表达，PDCD1（PD-1，耗竭 marker）低表达，提示该细胞具有强细胞毒性且不依赖 PD-1 激活。
  * **图 3D（TCR 克隆扩增 UMAP 图）** 通过颜色深浅展示 T 细胞克隆扩增程度，发现 CD8T_NK-like_FGFBP2 细胞的克隆扩增水平显著高于其他 CD8+T 细胞亚型，提示其可能通过克隆扩增发挥抗肿瘤作用。
  * **图 3E（扩增指数箱线图）** 量化比较各 CD8+T 细胞亚型的克隆扩增指数，CD8T_NK-like_FGFBP2 的扩增指数最高，进一步验证其克隆扩增特征。

#### 3\. 关键结论

TIME-NK 亚型的高 MPR 率与 FGFBP2+NK/NK 样 T 细胞富集相关，该细胞具有强细胞毒性、无 PD-1 表达、高克隆扩增的特征，可能通过化疗激活（体外实验证实化疗药物增强 NK 细胞杀伤）发挥抗肿瘤作用。

![](../../images/8a6c4e3e0c97ec5c.webp)

Figure 3

### ●（四）图 4：TIME-BE 患者中存在三级淋巴结构（TLS）

#### 1\. 核心目的

解析 TIME-BE 亚型的关键免疫特征，明确 B 细胞聚集的生物学意义。

#### 2\. 分析方法与结果解读

  * **图 4A（CD20 IHC 染色图）** 对 TIME-BE 亚型的 MPR 患者样本进行 CD20（B 细胞 marker）IHC 染色，低倍镜显示肿瘤床中存在大量 B 细胞聚集，高倍镜清晰观察到 B 细胞的聚集形态，直观展示 B 细胞富集特征。
  * **图 4B（B 细胞聚集数量箱线图）** 统计 5 种 TIME 亚型中 B 细胞聚集的数量（每 5mm×5mm 区域计数），发现 TIME-BE 亚型中 B 细胞聚集数量显著最高，验证 TIME-BE 的 “B 细胞富集” 特征。
  * **图 4C（mIF 染色图）** 采用多重免疫荧光检测 TLS 成熟度，标记 CD3（T 细胞）、CD19（B 细胞）、CD21（滤泡树突状细胞 marker）、DC-LAMP（成熟 DC marker）；左侧为 “成熟 TLS”（CD21 + 且 DC-LAMP+），右侧为 “未成熟 TLS”（CD21 + 但 DC-LAMP-），明确 TLS 的成熟状态定义。
  * **图 4D（成熟 TLS 数量箱线图）** 在有 B 细胞聚集的患者中，比较 MPR 和 non-MPR 患者的成熟 TLS 数量，发现 MPR 患者的成熟 TLS 数量显著更高，提示成熟 TLS 可能促进治疗响应。

#### 3\. 关键结论

TIME-BE 亚型的高 MPR 率与 B 细胞聚集形成的成熟 TLS 相关，TLS 作为 “肿瘤内免疫反应中心”，可能通过协同 Tfh 细胞、DC 细胞增强抗肿瘤免疫，为靶向 TLS 的免疫治疗提供依据。

![](../../images/167627f6b6c13d57.webp)

Figure 4

### ●（五）图 5：TIME-Teff 与 TIME-Treg 亚型的 T 细胞特征差异

#### 1\. 核心目的

对比 TIME-Teff（高 MPR）和 TIME-Treg（低 MPR）的 T 细胞亚型组成与克隆扩增特征，揭示 T 细胞异质性对治疗响应的影响。

#### 2\. 分析方法与结果解读

  * **图 5A（Treg 亚型 UMAP 图与 marker 基因点图）** 左侧 UMAP 展示 3 种 Treg 亚型（prolif Treg、CCR8-Treg、CCR8+Treg）；右侧点图展示关键基因表达：CCR8+Treg 高表达 FOXP3（Treg 核心 marker）、IL2RA（激活 marker）、CTLA4（免疫抑制 marker），证实其强免疫抑制功能。
  * **图 5B（Treg 亚型比例箱线图）** 比较 TIME-Teff 和 TIME-Treg 中 3 种 Treg 亚型在总 Treg 中的比例，发现 TIME-Teff 中 CCR8-Treg 比例高，TIME-Treg 中 CCR8+Treg 和 prolif Treg 比例高，体现 Treg 亚型的分布差异。
  * **图 5C（mIF 验证图）** 对 TIME-Teff 和 TIME-Treg 患者样本进行 FOXP3（红色，Treg）和 CCR8（绿色，CCR8+Treg）mIF 染色，TIME-Treg 中 FOXP3+CCR8 + 细胞数量显著更多，从蛋白水平验证 Treg 亚型分布差异。
  * **图 5D（CCR8+Treg 数量与比例箱线图）** 量化比较 TIME-Teff 和 TIME-Treg 中 CCR8+Treg 的绝对数量和在总 FOXP3 + 细胞中的比例，TIME-Treg 均显著更高（p=5×10-4），进一步证实 CCR8+Treg 与低响应的关联。
  * **图 5E（Tex 相关细胞定义示意图）** 通过 UMAP 展示 “Tex 相关细胞” 的定义：与终末耗竭 T 细胞（terminal Tex）共享 TCR 的 CD8+T 细胞，包括 terminal Tex 和前体耗竭 T 细胞（Texp），明确细胞群体划分依据。

  * **图 5F（差异基因点图）** 对比 Texp 和 terminal Tex 的差异表达基因，Texp 低表达 HAVCR2、TIGIT 等耗竭 marker，高表达 IL7R、GZMK 等激活 / 记忆 marker，说明 Texp 具有 “未完全耗竭、保留增殖和效应功能” 的特征，为后续关联复发风险埋下伏笔。
  * **图 5G（Texp 与 terminal Tex 比例箱线图）** 比较 TIME-Teff 和 TIME-Treg 中 Texp（左）和 terminal Tex（右）在 Tex 相关细胞中的比例，TIME-Teff 中 Texp 比例显著更高，TIME-Treg 中 terminal Tex 比例显著更高，提示 Texp 富集可能与高治疗响应相关。
  * **图 5H（Treg 扩增指数箱线图）** 量化 3 种 Treg 亚型的克隆扩增指数，发现 CCR8+Treg 的扩增指数最高，且在 TIME-Treg 中显著高于 TIME-Teff，说明 CCR8+Treg 的克隆扩增可能是 TIME-Treg 低响应的关键。
  * **图 5I（CCR8+Treg 克隆数量与扩增箱线图）** 对比 TIME-Teff 和 TIME-Treg 中 CCR8+Treg 的克隆数量（左）和扩增指数（右），TIME-Treg 均显著更高，进一步验证 CCR8+Treg 克隆扩增与低响应的关联。
  * **图 5J-K（T 细胞克隆组成堆叠图）** 分别展示 1 例 TIME-Teff（J）和 1 例 TIME-Treg（K）患者的 T 细胞克隆组成，TIME-Teff 中 Texp 克隆占比高，TIME-Treg 中 terminal Tex 和 CCR8+Treg 克隆占比高，通过个体案例直观呈现群体分析结果。

#### 3\. 关键结论

TIME-Teff 与 TIME-Treg 的治疗响应差异源于 T 细胞亚型与克隆扩增的异质性：TIME-Teff 富集 Texp 细胞（保留效应功能），TIME-Treg 富集 CCR8+Treg（强免疫抑制）和 terminal Tex（完全耗竭），且 CCR8+Treg 和 terminal Tex 的克隆扩增进一步加剧低响应。

![](../../images/6b54215c500db26d.webp)

Figure 5

### ●（六）图 6：5 种 TIME 亚型中的 T 细胞扩增特征与 non-MPR 患者分层

#### 1\. 核心目的

分析 T 细胞扩增特征在不同 TIME 亚型和响应状态中的分布，进一步对 non-MPR 患者进行异质性分层。

#### 2\. 分析方法与结果解读

  * **图 6A（T 细胞扩增分析策略示意图）** 展示分析流程：整合 Tex 相关细胞（Texp/terminal Tex）和 CCR8+Treg 的克隆扩增数据→比较不同 TIME 亚型、MPR/non-MPR 患者的扩增特征→基于 CCR8+Treg 克隆数量对 non-MPR 分层，逻辑清晰。
  * **图 6B（Tex 相关克隆数量箱线图）** 比较不同 TIME 亚型（含 LUSC/LUAD 分层的 TIME-Teff）中 Tex 相关克隆的数量，发现 TIME-Treg 中 Tex 相关克隆数量显著最高，non-MPR 的 LUSC TIME-Teff 患者显著低于 TIME-Treg，体现 non-MPR 患者的 T 细胞扩增异质性。
  * **图 6C（CCR8+Treg 克隆数量箱线图）** 趋势与图 6B 一致，TIME-Treg 中 CCR8+Treg 克隆数量显著最高，non-MPR 的 LUSC TIME-Teff 患者显著较低，进一步证实 non-MPR 患者的异质性。
  * **图 6D（Tex 相关克隆与 CCR8+Treg 克隆散点图）** 以 “CCR8+Treg 克隆数量≥9（上四分位数）” 为阈值，将 non-MPR 分为 “Treghi non-MPR”（≥9，红色）和 “Treglow non-MPR”（<9，蓝色），MPR 患者为绿色；可见 Treghi non-MPR 主要集中在高 CCR8+Treg 克隆区域，且 Tex 相关克隆数量也较高。
  * **图 6E（Sankey 图）** 展示 TIME 亚型与 non-MPR 分层的对应关系：Treghi non-MPR 患者来自所有 5 种 TIME 亚型，而非仅 TIME-Treg；Treglow non-MPR 主要来自 TIME-NK、TIME-BE、TIME-Mye，说明 non-MPR 分层不依赖于初始 TIME 亚型，而是基于 T 细胞扩增特征。
  * **图 6F-K（T 细胞扩增特征对比箱线图）** 分别比较 MPR、Treglow non-MPR、Treghi non-MPR 患者的 Tex 相关克隆数量（F）、Tex 相关克隆扩增指数（G）、Texp 比例（H）、CCR8+Treg 扩增指数（I）、CCR8+Treg 比例（J），发现 Treghi non-MPR 患者的 Tex 相关克隆多、Texp 比例低、CCR8+Treg 扩增强，与 MPR 患者差异最显著，Treglow non-MPR 则更接近 MPR 患者。

#### 3\. 关键结论

non-MPR 患者存在显著的 T 细胞扩增异质性，可基于 CCR8+Treg 克隆数量分为 Treghi（高复发风险潜能）和 Treglow（低复发风险潜能）亚群，该分层比初始 TIME 亚型更能反映患者的免疫状态差异。

![](../../images/7eb844550fcdd865.webp)

### ●（七）图 7：Texp 细胞比例与无复发生存期（RFS）相关

#### 1\. 核心目的

验证 T 细胞特征（尤其是 Texp 细胞比例）对患者复发风险的预测价值，解决 “如何识别 non-MPR 中低复发风险患者” 的临床问题。

#### 2\. 分析方法与结果解读

  * **图 7A（不同 TIME 亚型的 RFS Kaplan-Meier 曲线）** 比较 5 种 TIME 亚型的 RFS，TIME-NK 和 TIME-Teff 的 RFS 显著最长，TIME-Treg 和 TIME-Mye 显著最短（Log-rank p=0.016），说明初始 TIME 亚型与长期生存相关，但无法区分 non-MPR 患者的风险。
  * **图 7B（单因素 Cox 分析森林图）** 分析临床和免疫特征与 RFS 的关联，其中 “Texp 在 Tex 相关细胞中的比例” 的风险比（HR）最低，且显著性最高，提示其是最强的 RFS 保护因素；“CCR8+Treg 在总 Treg 中的比例” 是风险因素（HR=1.52，p=0.009）。
  * **图 7C（Texp 比例与 RFS 的 Kaplan-Meier 曲线）** 按 Texp 比例的下 25% 分组，Texp 比例高的患者 RFS 显著更长（Log-rank p<0.0001），直接证实 Texp 比例与复发风险的负相关。
  * **图 7D（CCR8+Treg 比例与 RFS 的 Kaplan-Meier 曲线）** 按 CCR8+Treg 比例的下 25% 分组，CCR8+Treg 比例高的患者 RFS 显著更短（Log-rank p=0.0088），验证其风险因素作用。
  * **图 7E（不同 non-MPR 亚群的 RFS 曲线）** 对比 MPR、Treglow non-MPR、Treghi non-MPR 的 RFS，Treghi non-MPR 的 RFS 最短，Treglow non-MPR 次之，MPR 最长（Log-rank p=0.00004），但 Treglow non-MPR 与 MPR 的差异仍需进一步细分。
  * **图 7F-G（不同 non-MPR 亚群中 Texp 比例与 RFS 的曲线）** 在 Treglow non-MPR（F）和 Treghi non-MPR（G）中，Texp 比例高的患者 RFS 均显著更长（Log-rank p 分别为 0.04、5×10-5），说明 Texp 比例可在不同 non-MPR 亚群中进一步区分风险。
  * **图 7H（MPR 与 Texp 比例联合分层的 RFS 曲线）** 将患者分为 “MPR”“non-MPR 且 Texp≥中位数”“non-MPR 且 Texp < 中位数” 三组，发现 “non-MPR 且 Texp≥中位数” 的 RFS 与 MPR 无显著差异，显著长于 “non-MPR 且 Texp < 中位数”（Log-rank p=0.0011），解决 “non-MPR 中哪些患者复发风险低” 的核心问题。
  * **图 7I（单因素 Cox 分析 HR 对比）** 以 MPR 为参考，“non-MPR 且 Texp≥中位数” 的 HR=1.32（p=0.65，无显著风险），“non-MPR 且 Texp < 中位数” 的 HR=7.73（p=8.26×10-6，显著高风险），进一步量化 Texp 比例的预测价值。

#### 3\. 关键结论

Texp 细胞在 Tex 相关细胞中的比例是预测 NSCLC 患者（尤其是 non-MPR 患者）复发风险的最优免疫标志物：Texp 比例高的 non-MPR 患者复发风险与 MPR 患者相当，其预测效能（时间依赖 ROC 的 AUC=0.736）显著优于传统病理响应指标（PRR，AUC=0.59）。

![](../../images/affaa1c6caa72ba4.webp)

Figure 5

**四、随便聊聊**

这篇文章为硕博研究生在肿瘤免疫与单细胞测序交叉领域的研究提供了 “范式级” 参考，对大家的学术发展有以下 4 点关键启示。

### （一）研究设计：“大样本 + 临床意义” 是顶刊核心门槛

  1. **样本规模** 该研究纳入 234 例测序样本，远超领域内多数研究（通常 <30 例），大样本量保证了结果的统计效力和普适性。对硕博而言，若无法获取如此大的样本，可通过 “多中心合作”“整合公共数据集”（如文中整合 OAK、口腔鳞癌数据集）弥补，避免因样本量不足导致结论局限。
  2. **临床锚点** 研究始终围绕 “治疗响应（MPR）” 和 “复发风险（RFS）” 两个临床核心问题，所有基础分析（如 TIME 分型、T 细胞克隆分析）均回归临床意义。这提示大家在设计研究时，需先明确 “解决什么临床问题”，再选择技术手段，避免 “为了做单细胞而做单细胞” 的误区。

### （二）技术应用：“单细胞多组学 + 功能验证” 提升研究深度

  1. **多组学整合** 文章联合 scRNA-seq（细胞分型与功能）和 scTCR-seq（克隆溯源），揭示了 “细胞功能 - 克隆进化 - 临床响应” 的关联，比单一 scRNA-seq 更具说服力。硕博阶段可尝试整合空间转录组（解析细胞定位）、ATAC-seq（染色质开放状态）等技术，进一步拓展研究维度。
  2. **功能验证闭环** 从 “单细胞数据分析发现现象（FGFBP2 + 细胞富集）→体外实验验证功能（NK 细胞杀伤实验）→临床样本验证（IHC/mIF）→外部数据集验证（乳腺癌、口腔鳞癌）”，形成完整的证据链。这提示大家，生信分析结果需通过实验或临床数据验证，避免 “纯生信预测” 导致的结论可信度不足。

### （三）结果解读：“分层分析 + 标志物挖掘” 增强研究创新性

  1. **异质性分层** 研究不仅划分了 TIME 亚型，还进一步对 non-MPR 患者进行分层（Treghi/Treglow），再通过 Texp 比例细分风险，层层递进地解析异质性，这种 “精细分层” 思路是顶刊研究的常见创新点。大家在分析时，避免对 “响应 / 不响应”“复发 / 未复发” 等群体进行简单二分，需挖掘群体内的亚组差异。
  2. **标志物转化价值** 研究最终提出 “Texp 比例” 这一可临床应用的标志物，比单纯的 “发现新细胞亚型” 更具转化意义。硕博研究中，若能从海量数据中筛选出 “可检测、可预测、可干预” 的标志物（如文中的 Texp、CCR8+Treg），将显著提升研究的临床价值和发表潜力。

**五、参考文献**

[1]: Liu Z, Yang Z, Wu J, et al. A single-cell atlas reveals immune heterogeneity in anti-PD-1-treated non-small cell lung cancer. Cell. 2025 May 29;188(11):3081-3096.e19. doi: 10.1016/j.cell.2025.03.018 . Epub 2025 Mar 26. PMID: 40147443.

![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)![图片](../../images/ec72a80f59849127.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247530154&idx=2&sn=e5d0a63646094c3094b7b916350d22ad&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。
大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![图片](../../images/fe8ecb8594a1f419.webp)![图片](../../images/4ccf87cacd1143af.gif) 您点的每个赞和在看，我都认真当成了喜欢
