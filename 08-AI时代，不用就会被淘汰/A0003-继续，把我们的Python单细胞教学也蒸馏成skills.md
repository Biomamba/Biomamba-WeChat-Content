---
title: "继续，把我们的Python单细胞教学也蒸馏成skills"
date: 2026-10-20
source: https://mp.weixin.qq.com/s/2f-j07etXKw3FLoYnej9xg
albums: ["AI时代，不用就会被淘汰"]
---

# 继续，把我们的Python单细胞教学也蒸馏成skills

> 原文：https://mp.weixin.qq.com/s/2f-j07etXKw3FLoYnej9xg

* * *

写在前面

省流，先看下分析集锦：
Skill 是按需加载的领域知识包：平时不占上下文，被触发时才把「工作流程 + 参数白名单 + 踩坑记录 + 可执行脚本」注入会话。对生信分析而言，它解决三个问题：
1. 流程不走样：每个分析模块顺序、每步的参数取值范围，来自课程实操沉淀而非模型即兴发挥；
2. 坑不重复踩：每个skill的references/pitfalls.md是真实事故的固化），不会因为频繁纠错而浪费token；
3. 产出可复现：参数表+版本号+中间文件落盘，换机器能重跑。

![图1](../images/A0003_01.jpg)

继续开蒸

继
听说你想蒸馏我？
中我们把大家订阅内容给蒸馏出来后，我们进一步，基于我们的课程”
就是为了快，82h搞定scRNA-seq分析全流程(Python版)
“蒸馏了Python单细胞分析的全部内容，希望能够帮助大家更高效的分析单细胞数据。蒸馏的资料是我们教学时的课件与学习手册：
├──
html
文件
│   ├── AI_module
.html
│   ├──
article
.html
│   ├── cell_communication
.html
│   ├── cnv
.html
│   ├── gene_co_expression_network
.html
│   ├── pseudotime
.html
│   └── scanpy
.html
└── notebook文件
├── AI_module
.ipynb
├──
article
.ipynb
├── cell_communication
.ipynb
├── cnv
.ipynb
├── gene_co_expression_network
.ipynb
├── pseudotime
.ipynb
└── scanpy
.ipynb
这次的提示词就比较多了，毕竟要求越多，AI乱搞产生幻觉的机会就越少：
向下滑动查看完整内容：
Biomamba 学习手册 → Skills 蒸馏 · 专业提示词套件
配套物料：《就是为了快，82h搞定scRNA-seq分析全流程(Python版)》学习手册 + 代码 + 测试文件（约 490 个文件 / 7 大模块）
用途：把散落在手册里的实操经验，蒸馏成可被 Agent 直接调用的分析技能（skills），用于日常数据分析提效
版本：v1.0 · 2026-10-14
一、总体设计
1.1 设计目标
目标
判定标准
经验可复用
手册里的流程/参数/避坑变成 Agent 的默认行为，而不是每次重新摸索
零幻觉
版本号、参数默认值、QC 阈值必须能在物料里找到原文，找不到一律标"原文未披露"
代码不走样
抽取出的代码片段逐字保留，禁止"顺手优化"成等价写法
冲突不吞
同一参数在不同模块推荐值不一致时，两个都留，标注冲突，不擅自裁决
可验收
每个技能包有明确的文件清单和验收 checklist
1.2 五段式流水线
物料清单
│
▼
┌──────────────────┐
│ Stage 0 清点切片  │  提示词 1 → units.json（单元清单 + 分片计划）
└──────────────────┘
│
▼
┌──────────────────┐
│ Stage 1 单元抽取  │  提示词 2 → kb_XXXX.json（每单元一份结构化知识）
└──────────────────┘
│
▼
┌──────────────────┐
│ Stage 2 合并消解  │  提示词 3 → merged_kb.json + conflicts.json + coverage.md
└──────────────────┘
│
▼
┌──────────────────┐
│ Stage 3 技能生成  │  提示词 4 → <skill>/SKILL.md + references/ + scripts/
└──────────────────┘
│
▼
┌──────────────────┐
│ Stage 4 质检红队  │  提示词 5 → qa_report.json（不通过则回炉 Stage 1/3）
└──────────────────┘
│
▼
┌──────────────────┐
│ Stage 5 使用态    │  提示词 6 → 日常分析时粘贴，Agent 按技能执行
└──────────────────┘
1.3 三条铁律（全流程强制）
铁律一：有出处。
任何版本号、参数默认值、QC 阈值、路径，必须能在物料原文中定位到；定位不到 → 该字段填
"原文未披露"
，禁止用通用知识补全。每条知识必须带
evidence
（章节号/页码/文件名）。
铁律二：代码逐字。
code_pattern.snippet
必须是物料原文代码，含注释；不得改写变量名、不得删"看起来冗余"的行、不得替换成等价 API。
铁律三：不裁决。
不同模块对同一参数给出不同推荐值时，两值都保留并标
"conflict": true
，由人或更高层技能在使用时按数据规模选择。禁止静默丢弃。
1.4 物料画像（已按推送目录核对）
模块
核心工具
预计单元数
技能域归属
基础分析
Scanpy、anndata
12 章
core
多样本/批次
BBKNN、ingest、harmony、scVI
5 节
batch
细胞注释
手动 + marker 库 + 自动
6 节
core / annotation
差异与富集
scanpy、gseapy、GO/KEGG/GSEA
5 节
de-enrich
细胞比例
matplotlib
6 节
de-enrich / viz
可视化
matplotlib、scanpy.pl
12 节
viz
轨迹分析
Palantir、PAGA、scVelo
3 工具
trajectory
细胞通讯
CellPhoneDB
3 方法
communication
共表达网络
相关性、KMeans、pyscenic
3 方法
network
拷贝数变异
infercnvpy、copykat
6 节
cnv
AI 自动注释
CellTypist、scVI、scANVI
4 工具
annotation
去双细胞/去污染
SOLO、scrublet、SCAR、kneeplot
5 节
qc-extra
文献复现
上述组合
11 节
reproduce
二、提示词 0：总控提示词（粘贴一次，贯穿全程）
把下面整段作为
会话第一条
粘贴，之后所有 Stage 都受它约束。
你现在担任「Biomamba scRNA-seq Python 全流程 · 技能蒸馏工程师」，负责把我投喂的
Biomamba 生信基地《82h Python scRNA-seq 全流程》学习手册物料，蒸馏为可被 Agent
直接调用的结构化分析技能（skills）。
【你的双重身份】
1. 知识抽取器：只做抽取，不做创造。物料里没有的知识一律标 "原文未披露"。
2. 技能工程师：把抽取结果工程化为 SKILL.md + references + scripts 的技能包。
【全程三条铁律，任何阶段不得违反】
铁律一 · 有出处：版本号、参数默认值、QC 阈值、文件路径，必须能在物料原文定位；
定位不到，该字段填 "原文未披露"，禁止用通用知识补全。
每条知识必须带 evidence 字段（章节号 / 页码 / 源文件名）。
铁律二 · 代码逐字：代码片段必须是物料原文逐字内容（含注释），禁止改写变量名、
禁止删除"看起来冗余"的行、禁止替换为等价 API。
铁律三 · 不裁决：同一参数在不同章节推荐值不一致时，两值都保留并标 "conflict": true，
由使用方按数据规模选择。禁止静默丢弃任何一方。
【流水线（我会按阶段给你下指令，你只执行当前阶段）】
Stage 0 清点切片   → 输出 units.json
Stage 1 单元抽取   → 输出 kb_<unit_id>.json（一次一个或几个单元）
Stage 2 合并消解   → 输出 merged_kb.json / conflicts.json / coverage.md
Stage 3 技能生成   → 输出 <skill-domain>/SKILL.md + references/ + scripts/
Stage 4 质检红队   → 输出 qa_report.json，不通过则指出回炉点
Stage 5 使用态     → 输出给日常分析用的调用提示词
【输出格式约定】
- 结构化数据一律输出纯 JSON，不要 markdown 解释，不要包裹 ``` 代码块。
- 自然语言部分用简体中文；工具名 / 函数名 / 参数名 / 文件路径保留英文原文。
- 每次输出末尾附一行「本批处理单元：<unit_id 列表>；待人工确认：<条数>」。
【禁止事项】
- 禁止编造版本号、引用文献、 benchmark 数字。
- 禁止引入物料之外的"更优做法"作为推荐值（可在 caveat 里作为提示，但必须标注
"物料外建议，需人工确认"）。
- 禁止把个人隐私信息写入任何产物。
- 遇到物料损坏 / 编码乱码 / 图片无法解析，停止该单元并在 needs_review 中记录，
禁止猜测内容继续。
现在请回复：已进入技能蒸馏工程师角色，请投喂物料清单或单元内容。
三、提示词 1：Stage 0 — 物料清点与切片规划
【Stage 0 任务】对下列物料做清点与切片规划，只规划，不抽取知识。
投喂内容：<粘贴文件清单：每行一个文件，格式 路径|类型|大小|章节号>
要求输出纯 JSON，结构如下：
{
"inventory": {
"total_files": 0,
"by_type": {"md": 0, "ipynb": 0, "py": 0, "r": 0, "html": 0, "other": 0},
"binary_or_unparsable": ["<无法解析需人工处理的文件>"]
},
"units": [
{
"unit_id": "U001",
"title": "<单元标题，取自手册章节名>",
"source_files": ["<构成该单元的文件>"],
"module": "<基础分析|轨迹分析|细胞通讯|共表达网络|拷贝数变异|AI注释|文献复现|可视化|差异富集>",
"tool_stack": ["<该单元涉及的工具，从物料标题/章节名识别，未出现不猜>"],
"estimated_tokens": 0,
"priority": "P0|P1|P2",
"depends_on": ["<前置单元 unit_id>"],
"notes": "<异常：乱码/缺页/图片为主/纯配置>"
}
],
"sharding_plan": {
"batch_size_rule": "每批 1-3 个单元，单批不超过 6 万字节原文",
"batch_order": [["U001"], ["U002", "U003"]]
},
"dedup": [
{"files": ["<内容高度重复的文件组>"], "action": "保留最新版，其余仅作交叉验证"}
],
"needs_review": ["<需要我人工确认的问题>"]
}
规划规则：
1. 一个单元 = 一个可独立理解的知识闭环（有输入、有处理、有输出/图）。
2. 章节号一律采用手册原编号，不要重排。
3. priority：P0 = 基础分析主流程 + 各模块首个工具实操；P1 = 进阶与下游；
P2 = 前言/文献解读/软件版本/致谢。
4. 纯图片页、纯安装说明、纯目录页 → priority P2 且 notes 说明原因。
5. 不得遗漏任何可解析文件；binary_or_unparsable 必须显式列出。
四、提示词 2：Stage 1 — 单元知识抽取（核心工作马）
这是使用频率最高的提示词，
每个单元粘贴一次
。
4.1 抽取提示词
【Stage 1 任务】对下面这一个单元做知识抽取。只抽取物料中明确存在的内容。
单元元信息：unit_id = <UXXX>，module = <模块名>，source_files = <文件列表>
──────────────── 物料原文开始 ────────────────
<粘贴该单元的原文：markdown 正文 / notebook 的 markdown cell + code cell / .py 源码>
──────────────── 物料原文结束 ────────────────
请严格输出如下结构的纯 JSON（不要 markdown、不要代码块包裹）：
{
"unit_id": "UXXX",
"title": "",
"module": "",
"source_files": [],
"analysis_stage": "<数据准备|预处理|单样本|多样本|注释|差异|富集|可视化|轨迹|通讯|网络|CNV|复现>",
"summary_zh": "<120 字内，说明这个单元解决什么问题、怎么解决>",
"tool_stack": [
{"name": "scanpy", "version": "<原文写的版本或 原文未披露>",
"version_source": "<章节号或 无>", "role": "<在该单元中的作用>"}
],
"workflow": [
{"step": 1, "goal": "<这一步要达成什么>", "action": "<做什么>",
"code_ref": "<对应原文代码位置，如 cell 3 / 行 12-40>",
"input": "<输入数据或对象>", "output": "<输出数据或对象>",
"depends_on_step": 1}
],
"code_pattern": [
{"name": "<范式名，如 h5ad 读取并备份 X>",
"language": "python",
"snippet": "<物料原文逐字代码，含注释，不省略关键行>",
"when_to_use": "<什么场景用>",
"why": "<为什么这样写，物料有解释则引原文，没有则填 原文未解释>",
"evidence": "<章节号>"}
],
"param_suggest": [
{"function": "sc.pp.normalize_total",
"param": "target_sum",
"default_value": "<物料写明的默认值或 原文未披露>",
"recommended_value": "<物料实际使用的值>",
"impact": "<物料说明的影响>",
"evidence": "<章节号>",
"confidence": "high|medium|low"}
],
"qc_thresholds": [
{"metric": "nFeature_RNA", "operator": ">", "value": 200,
"applies_to": "<基因数|线粒体比例|双细胞分数>",
"rationale": "<物料给的理由或 原文未给理由>", "evidence": "<章节号>"}
],
"io_schema": {
"inputs": [{"name": "", "format": "", "where": "<物料给的路径或 原文未披露>"}],
"outputs": [{"name": "", "format": "", "naming_rule": ""}]
},
"figure_spec": [
{"name": "质控小提琴图",
"purpose": "<回答什么问题>",
"function": "sc.pl.violin",
"key_args": ["<关键参数>"],
"style_notes": "<物料里的改造要点：配色/旋转/排序/拼图方式>",
"evidence": "<章节号>"}
],
"pitfall": [
{"issue": "<坑点标题>", "symptom": "<什么现象>", "cause": "<物料给的原因>",
"fix": "<物料给的解法>", "severity": "high|medium|low", "evidence": "<章节号>"}
],
"error_case": [
{"error_msg": "<原文报错关键行>", "cause": "", "solution": "", "evidence": "<章节号>"}
],
"best_practice": [{"text": "", "evidence": "<章节号>"}],
"caveat": [{"text": "<局限/注意事项/物料明确说不要这么做>", "evidence": "<章节号>"}],
"external_suggestion": [
{"text": "", "reason": "<为何物料外补充>", "status": "需人工确认"}
],
"needs_review": ["<你不确定或物料缺失的点>"],
"confidence_overall": "high|medium|low"
}
填写规则：
1. snippet 必须是原文逐字，含注释；一行都不许改。原文缺行的位置用
"# ...（原文此处省略，见 <位置>）" 标注，禁止自己补代码。
2. 版本号：物料写了就抄，没写填 "原文未披露"，禁止按经验填。
3. 物料没提到的字段，数组留空 []，不要填 null，不要编。
4. 原文若同时给出多种方法（如 CellPhoneDB 三种方法），每种单独成条，
在 name 里加序号区分。
5. 图片只说明"此处有图 X，展示 Y"，不得描述你没看到的图内容。
6. 全部填完后，自查一遍：每个非空字段是否都能在原文找到对应句子？
找不到的，改成 "原文未披露" 或移入 needs_review。
4.2 九类高频知识的抓取口诀
知识类型
抓取信号词
落到哪个字段
流程顺序
"首先/然后/接着/最后/下一步"
workflow
代码范式
可复用 cell、函数封装、
def
code_pattern
参数选择
"默认/建议/推荐/设为/调大/调小"
param_suggest
阈值
"大于/小于/至少/不超过/比例/阈值"
qc_thresholds
踩坑
"注意/坑/不要/否则/报错/失败"
pitfall
报错
Error
/
Traceback
/ 异常类名
error_case
图表
图题、"如下图所示"、
sc.pl.*
figure_spec
最佳实践
"推荐/更好/习惯/规范"
best_practice
局限
"但是/然而/不适用/仅支持/尚未"
caveat
五、提示词 3：Stage 2 — 跨单元合并与冲突消解
【Stage 2 任务】把下列多个 kb_<unit_id>.json 合并为统一知识库。只做合并与登记，
不做新知识创造。
投喂内容：<粘贴多份 Stage 1 输出的 JSON>
输出三个文件内容，用 ===FILE: <文件名>=== 分隔：
===FILE: merged_kb.json===
{
"schema_version": "1.0",
"source": "Biomamba 82h Python scRNA-seq 学习手册",
"units_merged": ["U001", "U002"],
"tool_stack": [
{"name": "", "version": "", "version_source": "", "used_in_units": []}
],
"workflow_master": [
{"stage": "", "steps": [
{"step": 1, "goal": "", "action": "", "code_ref": "", "units": ["U001"]}
]}
],
"code_pattern": [{"name": "", "language": "", "snippet": "", "units": []}],
"param_suggest": [
{"function": "", "param": "", "values": [
{"value": "", "units": ["U001"], "context": "<该值适用的数据规模/场景>"}
], "conflict": false}
],
"qc_thresholds": [{"metric": "", "rules": [{"value": 0, "units": []}]}],
"figure_spec": [],
"pitfall": [],
"error_case": [],
"best_practice": [],
"caveat": [],
"coverage": {"modules_covered": [], "modules_missing": []}
}
===FILE: conflicts.json===
[
{"topic": "", "unit_a": "U001", "unit_b": "U003",
"a_value": "", "b_value": "",
"difference_type": "参数值|版本号|流程顺序|阈值",
"resolution_hint": "<物料中是否有线索可判断，没有则填 需人工确认>",
"impact_if_wrong": "high|medium|low"}
]
===FILE: coverage.md===
（用 markdown 写一份覆盖度报告：每个模块抽到多少条知识、哪些章节没覆盖、
哪些字段大量为"原文未披露"——这些是物料缺口，需人工补充或接受）
合并规则：
1. 同名工具版本：取"明确写了版本"的值；多个版本并列则全部列出并标 conflict。
2. 同名参数多值：合并为 values 数组，每条带 units 和 context，设 conflict 标志。
3. 相同代码范式在不同单元重复出现：合并为一条，units 列全，snippet 取
信息量最全的那版，并在 name 后标注 "[N 处出现]"。
4. 频率统计：同一 best_practice / pitfall 出现 ≥2 次的，在 merged_kb 对应条目
加 "frequency": 2 —— 高频经验是技能约束的最高优先级来源。
5. 严禁把 external_suggestion 混入正式字段；单独留待人工审。
6. 冲突一律进 conflicts.json，不得在 merged_kb 里悄悄选一个。
六、提示词 4：Stage 3 — SKILL.md 生成
6.1 技能域划分（建议产出 10 个技能）
#
skill 名
覆盖内容
优先级
1
biomamba-sc-core
adata 结构、QC、单样本、分群、基础注释
P0
2
biomamba-sc-batch
多样本、BBKNN/ingest/harmony/scVI
P0
3
biomamba-sc-viz
降维/气泡/小提琴/矩阵/热图/track/拼图
P0
4
biomamba-sc-de-enrich
差异分析、GO/KEGG/GSEA、细胞比例图
P0
5
biomamba-sc-annotation
手动/marker 库/CellTypist/scVI/scANVI
P1
6
biomamba-sc-qc-extra
SOLO/scrublet 去双细胞、SCAR/kneeplot 去污染
P1
7
biomamba-sc-trajectory
Palantir/PAGA/scVelo
P1
8
biomamba-sc-communication
CellPhoneDB 三方法
P1
9
biomamba-sc-network
相关性/KMeans/pyscenic
P2
10
biomamba-sc-cnv
infercnvpy/copykat/与 R 版对比
P2
6.2 生成提示词
【Stage 3 任务】基于 merged_kb.json 生成 <skill-name> 的 SKILL.md。
投喂内容：<merged_kb.json 全量或该 skill 域相关切片>
SKILL.md 必须严格按以下骨架输出（markdown，YAML frontmatter 开头）：
---
name: <skill-name>
description: <一句话说明用途 + 触发词，触发词至少 4 个，含中文与工具名>
agent_created: true
---
# <技能标题>
## 用途
（两三句话：这个技能让 Agent 在什么场景下按什么经验做事）
## 适用 / 不适用
- 适用：<数据规模、组学类型、前置条件>
- 不适用：<物料明确说不适用的场景；没说不适用就写 物料未明确限定>
## 任务行为约束（固定流程顺序）
1. 第一步必须……
2. 然后……
（顺序来自 workflow_master，禁止 Agent 自行调整顺序；每步后必须自查对应 pitfall）
## 代码输出约束
- 语言与风格：<物料里的代码风格，逐字保留的范式名>
- 禁用写法：<物料里明确说不要用的写法；没有就写 物料未列出禁用写法>
- 强制写法：<code_pattern 里 frequency ≥2 的范式>
## 参数白名单
| 函数 | 参数 | 推荐值 | 物料出处 | 备注 |
|---|---|---|---|---|
（只收 param_suggest；有 conflict 的写两个值并标注"按数据规模二选一"；
版本写 "原文未披露" 的就是未披露，不许填数）
## 强制检查清单（每完成一步必须逐条打勾）
- [ ] <来自 pitfall 的自查项>
- [ ] <来自 qc_thresholds 的达标项>
- [ ] <来自 error_case 的预防项>
## 报错处理约束
遇到报错时的优先级：先查 error_case 匹配 → 再查 pitfall → 都不中才用通用知识，
且必须在回复里注明"该解法来自物料外"。
## 可视化规范
<figure_spec 汇总：用什么函数、哪些关键参数、物料改造要点>
## 交付物规范
- 必须产出：<io_schema.outputs>
- 命名规则：<naming_rule>
- 附带：本步 QC 指标值 + 使用的参数表（可复现）
## 参考成品
<物料里的示例输出；没有就写 物料未附成品示例>
## 姊妹技能
<与其他 skill 的衔接关系，如 sc-core → sc-batch → sc-viz>
生成规则：
1. frontmatter 的 description 必须包含触发词，用户说这些词时应命中本技能。
2. 所有数字/版本/阈值必须来自 merged_kb，逐条可追溯；不许出现无出处的数字。
3. 语言简体中文，工具/函数/参数保留英文。
4. 不得写入任何个人隐私信息。
5. 物料没覆盖的点，写"物料未覆盖，建议人工补充后启用"，禁止用通用知识填成正式约束。
6.3 技能包目录规范
skills/<skill-name>/
├── SKILL.md                      # 主文件，Agent 每次调用必读
├── references/
│   ├── workflow.md               # 完整流程（来自 workflow_master）
│   ├── params.md                 # 参数白名单全表 + 冲突说明
│   ├── pitfalls.md               # 坑点与报错手册
│   ├── figures.md                # 图表规范与改造要点
│   └── coverage-gaps.md          # 物料缺口清单（待人工补）
└── scripts/
├── <可复用函数>.py            # 从 code_pattern 函数化，逐字保留逻辑
└── mwe_minimal.py            # 最小可运行示例（用测试文件跑通）
七、提示词 5：Stage 4 — 质检与红队
【Stage 4 任务】以红队视角审查 <skill-name> 的技能包，只挑错，不表扬。
投喂内容：<SKILL.md + references/*.md + 对应 merged_kb 切片 + 原始 kb JSON>
逐项检查并输出纯 JSON：
{
"skill": "<skill-name>",
"verdict": "PASS|FAIL",
"issues": [
{"id": 1, "severity": "blocker|major|minor",
"category": "幻觉版本|无源参数|代码被改写|自相矛盾|超出物料|格式违规|隐私泄漏|术语不一致",
"location": "<文件 + 章节>",
"found": "<你看到的内容>",
"expected": "<物料里实际是什么>",
"fix": "<具体怎么改>"}
],
"stats": {
"params_total": 0, "params_with_source": 0,
"params_undisclosed": 0,
"code_patterns_total": 0, "code_verbatim_ok": 0,
"pitfalls_total": 0, "pitfalls_with_evidence": 0
},
"rerun_stage": "Stage1|Stage3|null"
}
检查项（每条都要查，不许跳过）：
1. 幻觉版本：SKILL.md / params.md 里每个版本号能否在 kb JSON 的 tool_stack 找到？
2. 无源参数：参数白名单每行的"物料出处"是否非空？空的 → blocker。
3. 代码被改写：把 code_pattern.snippet 与原始物料逐字比对（含注释与空行），
任何字符差异 → blocker。
4. 自相矛盾：SKILL.md 内部、SKILL.md 与 references 之间、与 conflicts.json 之间
是否有未标注冲突的取值不一致？
5. 超出物料：是否有物料里完全没有的"更优做法"被写成了正式约束？
（external_suggestion 必须隔离在需人工确认区，不得混入约束）
6. 格式违规：frontmatter 是否有 name/description；description 是否含触发词；
是否有个人隐私信息。
7. 术语不一致：同一函数/参数在不同文件里写法是否统一（如 normalize_total 与
normalize-total 混用）。
8. 空转检查：是否存在空章节、TODO、占位符未替换。
判定：出现任一 blocker → FAIL，并给出 rerun_stage。major ≥3 → FAIL。
PASS 也必须列出 minor 供人工决定是否修。
八、提示词 6：Stage 5 — 使用态提示词（日常分析时粘贴）
蒸馏完成后，每次做分析粘贴这段，Agent 就会按技能执行。
你现在是 Biomamba scRNA-seq Python 全流程分析助手，已加载以下技能：
biomamba-sc-core / biomamba-sc-batch / biomamba-sc-viz / biomamba-sc-de-enrich /
biomamba-sc-annotation / biomamba-sc-qc-extra / biomamba-sc-trajectory /
biomamba-sc-communication / biomamba-sc-network / biomamba-sc-cnv
【我的数据】
<描述：物种、样本数、分组、数据格式与路径、已知问题>
【我要做的分析】
<目标，如：多样本整合 + 注释 + 差异 + 富集 + 一张拼图>
【执行要求】
1. 先输出执行计划：按技能里的固定流程顺序列出步骤，每步标注将用哪个技能、
预计产出什么文件。等我确认后再动手。
2. 严格使用参数白名单里的推荐值；物料标 conflict 的参数，先问我的数据规模
（细胞数/样本数）再选，不许默认。
3. 每完成一步，先跑强制检查清单，把结果（通过/未过/未过怎么处理）告诉我，
再进入下一步。QC 不达标时停下来给方案，不许带病往下跑。
4. 报错时：先匹配技能 error_case → 再匹配 pitfall → 都不中才用通用知识，
并注明"物料外解法"。
5. 可视化一律按技能的可视化规范执行（函数、关键参数、改造要点）。
6. 每步都要落盘：中间文件按 io_schema 命名规则保存；最后给我参数表 +
代码 + 产出文件清单，保证可复现。
7. 涉及大内存步骤（如 scVI、copykat），先估算内存并给出守护方案再运行。
8. 物料未覆盖的情况，明确说"技能未覆盖，按通用方案处理并已标注"，
不许假装技能里有。
请先给执行计划。
九、附录 A：喂料规范（决定蒸馏质量）
项
规范
文件命名
统一改为
U<三位数>_<章节名>.<ext>
，如
U004_数据质控与可视化.md
每批数量
1–3 个单元；单批原文不超过 6 万字节，超出按章节再切
保留原文
不删注释、不删空行、不改格式；乱码不要"猜修"，原样投喂并说明
Notebook
投喂 markdown cell + code cell 的
原文
（含输出可省略，但报错输出要留）
二进制
.rds / .h5ad / .png / .pdf 不投喂，只投喂说明性文本；图片只报"此处有图"
版本信息
优先投喂"软件版本"章节，这是版本号的唯一合法来源
结束声明
每批末尾加一行「本批物料到此为止」，防止我续编
交叉验证
同一内容在多个文件出现时，全部投喂，用于 Stage 2 频率统计
十、附录 B：产物清单与验收标准
10.1 最终产物树
Biomamba-scRNA-skills/
├── merged_kb.json            # 统一知识库（单一事实源）
├── conflicts.json            # 冲突登记表（人工裁决入口）
├── coverage.md               # 覆盖度报告 + 物料缺口
├── qa_report.json            # 红队质检报告
└── skills/
├── biomamba-sc-core/SKILL.md + references/ + scripts/
├── biomamba-sc-batch/...
├── biomamba-sc-viz/...
├── biomamba-sc-de-enrich/...
├── biomamba-sc-annotation/...
├── biomamba-sc-qc-extra/...
├── biomamba-sc-trajectory/...
├── biomamba-sc-communication/...
├── biomamba-sc-network/...
└── biomamba-sc-cnv/...
10.2 验收 checklist
[ ] 10 个技能的
SKILL.md
frontmatter 均含 name + description + 触发词
[ ]
params.md
中每个参数的"物料出处"列非空
[ ]
code_pattern
与原文逐字一致（抽查 ≥5 条）
[ ]
conflicts.json
中每条冲突都能在
merged_kb.json
找到双值记录
[ ]
qa_report.json
verdict 为 PASS（blocker = 0，major ≤ 2 且已说明）
[ ] 任一技能中不出现物料外版本号 / benchmark 数字 / 个人隐私
[ ]
mwe_minimal.py
在测试文件上实际跑通（至少 core + 一个进阶模块）
[ ] 使用态提示词（提示词 6）在真实数据上试跑一次，确认能命中技能
生成的skills结构：
biomamba_sc_distill/
├── README.md                   本文件
├── coverage.md                 覆盖度报告 + 物料缺口 + 验收 checklist
├── merged_kb.json              统一知识库（单一事实源，129 参数 / 11 QC / 9 最佳实践 / 7 局限）
├── conflicts.json              冲突登记表（36 条，前 5 条人工核实）
├── skills/                     9 个技能包
│   ├── biomamba-sc-core/       P0 基础分析主流程（12 步）
│   ├── biomamba-sc-batch/      P0 多样本整合（BBKNN / ingest / harmony）
│   ├── biomamba-sc-viz/        P0 可视化（降维/气泡/小提琴/矩阵/热图/track/拼图）
│   ├── biomamba-sc-de-enrich/  P0 差异分析与 GO/KEGG/GSEA
│   ├── biomamba-sc-trajectory/ P1 Palantir / PAGA / scVelo
│   ├── biomamba-sc-annotation/ P1 CellTypist / scVI / scANVI / SOLO / scrublet / SCAR
│   ├── biomamba-sc-cnv/        P2 infercnvpy / copykat / 肿瘤细胞鉴定
│   ├── biomamba-sc-communication/ P1 CellPhoneDB
│   └── biomamba-sc-network/    P2 相关性 / KMeans / pyscenic
│       └── <每个技能>/SKILL.md + references/{workflow,params,pitfalls}.md + scripts/
├── mcp/sc_kb_server.py         零依赖 MCP 知识库服务（8 个工具，stdio JSON-RPC）
├── prompts/sc_analysis_prompt.md  会话启动/查询/分场景/质检提示词
├── shards/                     中间产物：7 个单元的 markdown+code 文本分片
├── md/                         中间产物：各单元 markdown 教学正文
└── out/calls.json              中间产物：125 个函数调用及参数的程序化抽取结果
生成的skills大概长这样：
biomamba_sc_distill/
├── README.md                   本文件
├── coverage.md                 覆盖度报告 + 物料缺口 + 验收 checklist
├── merged_kb.json              统一知识库（单一事实源，129 参数 / 11 QC / 9 最佳实践 / 7 局限）
├── conflicts.json              冲突登记表（36 条，前 5 条人工核实）
├── skills/                     9 个技能包
│   ├── biomamba-sc-core/       P0 基础分析主流程（12 步）
│   ├── biomamba-sc-batch/      P0 多样本整合（BBKNN / ingest / harmony）
│   ├── biomamba-sc-viz/        P0 可视化（降维/气泡/小提琴/矩阵/热图/track/拼图）
│   ├── biomamba-sc-de-enrich/  P0 差异分析与 GO/KEGG/GSEA
│   ├── biomamba-sc-trajectory/ P1 Palantir / PAGA / scVelo
│   ├── biomamba-sc-annotation/ P1 CellTypist / scVI / scANVI / SOLO / scrublet / SCAR
│   ├── biomamba-sc-cnv/        P2 infercnvpy / copykat / 肿瘤细胞鉴定
│   ├── biomamba-sc-communication/ P1 CellPhoneDB
│   └── biomamba-sc-network/    P2 相关性 / KMeans / pyscenic
│       └── <每个技能>/SKILL.md + references/{workflow,params,pitfalls}.md + scripts/
├── mcp/sc_kb_server.py         零依赖 MCP 知识库服务（8 个工具，stdio JSON-RPC）
├── prompts/sc_analysis_prompt.md  会话启动/查询/分场景/质检提示词
├── shards/                     中间产物：7 个单元的 markdown+code 文本分片
├── md/                         中间产物：各单元 markdown 教学正文
└── out/calls.json              中间产物：125 个函数调用及参数的程序化抽取结果

分析实战

看下实战效果，告诉你的任何AI Agent：”帮我用新生成的skills，分析一遍GSE131907这个数据集，需要skills的每个模块都用一遍“。那么它大概率会给你返回这么个分析过程手册：
GSE131907 · 单细胞肺癌转移九模块全流程学习手册
基于 Biomamba《82h Python scRNA-seq 全流程》9 个蒸馏 Skill 的端到端实战复盘
数据集：GSE131907（Kim et al., 2019，肺腺癌 LUAD 多部位转移 scRNA-seq，58 个 10x 文库 / 208,506 细胞 / 29,634 基因）
scanpy 1.11.4
9 模块
100k 分层抽样
含一次全量返工
含诚实的未跑通清单
目录
数据集与学习目标
全流程架构
铁律：矩阵与注释必须按 barcode 对齐
M1 基础分析（core）
M2 批次校正（batch）
M3 注释与双细胞（annotation）
M4 差异与富集（de-enrich）
M5 可视化（viz）
M6 拟时序（trajectory）
M7 细胞通讯（communication）
M8 拷贝数变异（cnv）
M9 共表达网络（network）
诚实的一半：未完全跑通项的处理
复现命令总表
技能索引与参考
一、数据集与学习目标
为什么要做这个数据集？它几乎集齐了单细胞实战的全部坑。
GSE131907 是一项肺腺癌（LUAD）研究，对
同一批患者
的多个部位取样：原发性肿瘤（tLung）、正常肺（nLung）、肿瘤旁（tL/B）、正常淋巴结（nLN）、转移淋巴结（mLN）、转移脑（mBrain）、胸腔积液（PE）。 共 58 个 10x Genomics 文库、208,506 个细胞、29,634 个基因。它天然适合练习：多样本整合、转移 vs 原发比较、肿瘤细胞鉴定。
学习目标（读完本手册应掌握）
单样本 QC → 归一化 → HVG → PCA → 分群 → marker 的完整闭环（M1）；
三种批次校正方法的选择与结果判读（M2）；
自动注释（CellTypist）+ 双细胞检测的正确姿势（M3）；
差异分析与 GO/KEGG/GSEA 富集，以及「富集结果必须按显著性排序」的细节（M4）；
五类 marker / diff 可视化与细胞比例图（M5）；
PAGA + Palantir 拟时序，以及 RNA 速率的数据前提（M6）；
CellPhoneDB 受体-配体通讯（M7）；
infercnvpy / copyKAT 两种 CNV 推断与肿瘤细胞鉴定（M8）；
相关性共表达网络 + KMeans 模块（M9）；
最关键的：外部矩阵与注释表必须按 barcode 对齐，否则全量返工
（见第三章）。
本手册的实证数字
全部来自本次实际运行（scanpy 1.11.4、celltypist 1.7.1、infercnvpy 0.6.1、CellPhoneDB v5.0.0），不是教程示例值。所有坑都是真实踩过并修复的。
二、全流程架构
9 个模块对应 9 个 Skill，串联成一条可复现流水线。
M1 基础
core
M2 批次
batch
M3 注释
annotation
M4 差异
de-enrich
M5 可视化
viz
下游分支
M6/M7/M8/M9
⚠ 铁律闸门：M1a 读入时必须 anno.loc[cell_names] 对齐
说明：M1→M5 为通用主线；M6(拟时序)/M7(通讯)/M8(CNV)/M9(网络) 为四路下游，互不依赖可独立运行。
图 0 · 九模块流水线（含对齐铁律闸门）
三、铁律：外部矩阵与注释表必须按 barcode 对齐
本次全流程最严重的一次返工，值得每一个做单细胞的人记住。
事故经过
第一遍 9 个模块全部跑完后，我用组织特异 marker 做交叉验证，发现
每个细胞的注释都被挂到了另一个细胞上
。PLP1（少突胶质细胞标记）在 mBrain 与其它组织均值几乎相同（0.018~0.020）；SFTPB 在 tLung/nLung 相同（0.390/0.395）；CellTypist 在纯免疫子集里预测出 9,600 个上皮细胞。
根因
注释文件
GSE131907_Lung_Cancer_cell_annotation.txt.gz
的行序与
raw_umi.tsv
的列序
完全不同
——逐位比对同位置 barcode 一致仅
1 / 208,506
。读取脚本只断言了
len(anno)==len(cell_names)
（长度相等但顺序无关），而
sc.AnnData(X, obs=anno)
会按
anno.index
的顺序挂注释。
全程没有任何报错。
修复（只需重排 obs，不必重读 12.4 GB 矩阵）
# ❌ 错误写法（M1a 第一版）：只比较长度，顺序无关
adata = sc.AnnData(X, obs=anno)          # 按 anno.index 顺序挂注释，静默错位
# ✅ 正确写法：按矩阵列序重排，并断言逐位相等
anno_aligned = anno.loc[cell_names]       # cell_names = 矩阵的列名（barcode）
assert (anno_aligned.index == cell_names).all(), "注释表与矩阵列序不一致！"
adata = sc.AnnData(X, obs=anno_aligned)
修复后自检（组织特异性应显著）
marker
PLP1（少突胶质）
SFTPB / SFTPA1（肺泡上皮）
PTPRC / MS4A1（免疫细胞）
修复前
各组织 0.018~0.020（无差别）
tLung 0.390 / nLung 0.395（无差别）
—
修复后
仅 mBrain 高
仅肺组织高
淋巴结最高
修复后细胞组成与 Kim et al. 图谱完全吻合：nLN 无上皮、mLN/mBrain 出现转移性上皮（14.2% / 53.2%）、nLung 髓系 38.8%（肺泡巨噬细胞）、CellTypist 免疫子集里的上皮细胞从 9,600 降到
10
。旧结果已归档到服务器
archive_invalid_alignment_20261015/
。
通用规则
：任何「外部表达矩阵 + 独立注释/元信息表」的拼接，都必须
anno.loc[cell_names]
并按 barcode 断言逐位相等，再挂 obs。这是单细胞分析的第一条铁律。
四、M1 基础分析 · biomamba-sc-core
技能来源：U001 · 单样本基础分析主流程
目的
读入矩阵 → QC 过滤 → 归一化 → 高变基因 → PCA → 邻居图 → leiden 分群 → UMAP → marker。这是所有下游的前提。
关键参数（白名单摘录）
步骤
参数
本次取值
出处
QC
n_genes_by_counts
200~9750；pct_mt<20
按数据分布调整（作者已预过滤）
归一化
normalize_total(target_sum)
1e4
U001 / U006
HVG
n_top_genes / flavor
2000 / seurat_v3（作用在 counts 层）
U001 4.4
PCA
svd_solver
arpack
U001 4.4
邻居图
n_neighbors / n_pcs
10 / 40
U001 4.4
分群
leiden resolution
1.0
U001 4.4
本次实证结果
输入：29,634 基因 ×
208,506
细胞；QC 后保留
208,500
；
HVG 2000 个；leiden(resolution=1.0) 得到
43 个簇
；
按分布调整后的 QC 阈值：n_genes 中位数 1103、pct_mt 中位数 3.5%。
踩坑与对策
坑 1（critical）
：见第三章——外部注释表必须按 barcode 对齐，否则 43 个簇全是错的。
坑 2
：
sc.pp.highly_variable_genes
的
flavor="seurat_v3"
作用在
counts
层而非 log 层，装
scikit-misc
才不报错。
坑 3
：归一化后不要再执行
adata.layers['counts']=adata.X.copy()
，会把 log 数据写回 counts 层导致下游二次归一化（见 M4 影响）。
结果图
图 M1-a · QC 小提琴 + 散点（n_genes / total_counts / pct_mt）
图 M1-b · 全量 208k 细胞的 UMAP（按 leiden 着色）
图 M1-c · 经典 marker 的 UMAP 表达分布
五、M2 批次校正 · biomamba-sc-batch
技能来源：U001 5.4 · 多样本整合与批次效应去除
目的
58 个 10x 文库天然存在批次效应。标准做法是
先做「不去批次」基线确认批次存在
，再按场景选方法：BBKNN（中等批次/大数据）、ingest（有明确参考集）、harmony（强批次/无参考）。
本次实证
抽样
100,000
细胞 / 58 个 Sample，按
Sample_Origin
分 6 类（Tumor/Normal/Metastasis/Effusion…）；
baseline / BBKNN / harmony 三法全部产出对比图；
ingest 本环境修复
：scanpy 1.11.4 + numpy 2.x 下
sc.tl.ingest
因 pynndescent 内部
all input arrays must have the same shape
卡死。改用「参考集拟合 PCA → 查询集投影到同一 PCA 空间 → 合并后用
method='gauss'
（sklearn 邻居，不走 pynndescent）→ UMAP」的等价实现，参考集 LUNG_N01（1,524 细胞）锚定 tLung 查询集（20,000 细胞）。
踩坑与对策
harmonypy 2.x
的
Z_corr
已是 (n_obs, n_pcs)，scanpy 1.11.4 的
harmony_integrate
会再转置一次导致错位——需直接调
run_harmony
且不转置。
ingest 替代
：见上，pynndescent 0.6.0 是可用版本上限，无法靠升级修复，必须绕过。
结果图
图 M2-a · 不去批次 vs BBKNN vs harmony（按 Sample_Origin 着色）
图 M2-b · harmony 整合后 UMAP（按 Sample_Origin / leiden）
图 M2-c · ingest（修复版）：查询集锚定到正常肺参考 PCA 空间
六、M3 注释与双细胞 · biomamba-sc-annotation
技能来源：U006 · AI 自动注释与双细胞/污染去除
目的
CellTypist 自动注释（Immune_All_Low 模型 + majority voting）+ 手动 marker 复核 + scrublet 去双细胞。
细胞类型标签以 GEO 原文注释 Cell_type.refined 为权威
（见下文回填规则）。
本次实证
CellTypist 1.7.1 在 60,000 细胞上注释成功，免疫子集细分出
29 个亚型
；
手动 9 类 marker 注释计数：T_cell 25,258 / Epithelial 16,605 / B_cell 16,432 / Myeloid 14,502 …；
GEO 官方 7 大类直接赋值：T/NK 30,869 / Myeloid 20,268 / Epithelial 17,490 / B 13,258 / Fibroblasts 1,831 / MAST 1,597 / Endothelial 1,011（refined 列为空的 13,676 个细胞按 GEO Cell_type 原文回填，见下表）。
GEO 原始注释（权威标签）
GEO 原始注释：以原文为准
GEO 为 GSE131907 提供了三列注释：
Cell_type
（粗粒度 10 类）、
Cell_type.refined
（7 大类）与
Cell_subtype
（细亚型）。
本手册以
Cell_type.refined
为权威标签
。该列只对填了细亚型的细胞赋值，10 万个抽样细胞中
13,676
个为空——这些细胞的
Cell_type
（同为 GEO 原始列）标识为 T/NK 淋巴细胞、少突胶质细胞（Oligodendrocytes）或未定细胞（Undetermined），因此按原文粗粒度列
回填
，而不是丢弃或笼统标成 Unassigned。回填后 100,000 个细胞全部有权威归属：T/NK 30,869 →
43,791
，另补回 Fibroblasts +97、Endothelial cells +39、Oligodendrocytes 331、Undetermined 287。
GEO 原始注释（权威标签）
细胞数
占比
T/NK cells
43,791
43.79%
Myeloid cells
20,268
20.27%
Epithelial cells
17,490
17.49%
B lymphocytes
13,258
13.26%
Fibroblasts
1,928
1.93%
MAST cells
1,597
1.60%
Endothelial cells
1,050
1.05%
Oligodendrocytes
331
0.33%
Undetermined
287
0.29%
合计
100,000
100%
图 M3-d · GEO 原始注释 UMAP（Cell_type.refined 为主，缺失按 Cell_type 原文回填）
双细胞检测（关键修正）
第一版把 58 个文库
混在一起
跑 pooled scrublet，因
threshold_minimum
在混合文库上返回近 0 阈值，导致
100% 误判为双细胞
。修正为
按 Sample（10x 文库）逐样本
运行（scanpy 1.11.4 支持
batch_key
），自动阈值 >25% 时回退
quantile(1-0.05)
：
# ❌ 错误：pooled 跑，混合文库阈值退化 → 100% 双细胞
sc.pp.scrublet(adata, expected_doublet_rate=0.05)
# ✅ 正确：按文库逐样本跑
sc.pp.scrublet(adata, expected_doublet_rate=0.05, batch_key='Sample')
修正后：58 个文库全部成功，
669 个双细胞（0.669%）
，每文库中位数 0.47%；
仅 2 个文库触发了回退阈值——说明逐样本自适应非常必要。
结果图
下图是 CellTypist（Immune_All_Low 模型，60,000 个免疫细胞，majority voting）预测亚型与 GEO 官方注释的一致性比对：纵轴为预测亚型（按 GEO 参考组排序），横轴为 4 个官方免疫大类；
点大小 = 该参考组内的细胞占比，颜色 = 平均预测概率
。对角线上的大点即主要对应关系（Memory / Naive B cells ↔ B lymphocytes、Tcm/Naive helper T cells ↔ T/NK cells、Alveolar macrophages / Macrophages ↔ Myeloid cells、Mast cells ↔ MAST cells）；偏离对角线的零星小点，即被官方注释为免疫、却被预测为上皮 / 内皮等其它谱系的污染细胞。
图 M3-a · CellTypist 预测 vs GEO 官方注释一致性 dotplot（celltypist 1.7.1）
图 M3-b · 逐样本 scrublet 双细胞打分分布
图 M3-b2 · 双细胞分数直方图（逐文库修正后，中位数 0.046）
图 M3-c · 按文库的双细胞率（修正后）
七、M4 差异与富集 · biomamba-sc-de-enrich
技能来源：U001 8.x · 差异分析与富集
目的
肿瘤（tLung）vs 正常（nLung）的差异基因，再做 GO/KEGG/GSEA 富集。
本次实证
差异组合：Tumor 21,653 细胞 vs Normal 20,621 细胞，wilcoxon；
显著 DEG（p_adj<0.05）
2,509
个（上 1,222 / 下 1,287）；
按细胞类型批量差异：Epithelial 4,610、Myeloid 1,636、Fibroblasts 1,090、T/NK 685、B 224、Endothelial 222、MAST 106；
富集：KEGG_up 首项为
Pathways in cancer / PI3K-Akt / ECM-receptor / Small cell lung cancer
。
踩坑与对策
富集结果排序
：enrichr / gseapy 默认输出按 Term 字母序，直接
head(5)
拿到的是字母靠前的通路而非最显著者。
必须按校正 p 值 / FDR 排序后再取 top
（本次已修复）。
counts 层被 log 覆盖的连锁反应
：若归一化后误执行
layers['counts']=X.copy()
，下游二次归一化会把 fold change 压缩到只剩 3 个基因 p<0.05——这正是返工前 M4 的诡异现象。
结果图
M4 的富集结果以表格/条形图数据落盘为 CSV（共 18 个文件），例如
de_enrich/M4_KEGG_up.csv
、
M4_GSEA_GO.csv
、
M4_deg_Epithelial_cells.csv
等，可直接用 Excel/Python 读取做下游解读；条形图可由这些 CSV 二次绘制。
八、M5 可视化 · biomamba-sc-viz
技能来源：U001 4.x / 11.x · 单细胞可视化规范
目的
统一画布
set_figure_params(dpi=300, facecolor='white')
，输出：降维展示（可切 counts/scaled 层）、marker 五类图（dotplot/violin/matrixplot/heatmap/tracksplot）、diff 五类图、相关性、dendrogram、细胞比例图。
本次实证
共
18 张图
；marker 与 diff 各出五类（10 张）；
UMAP 三视角：默认 / counts 层 / scaled 层对比；
细胞比例图按 Sample_Origin 展示各细胞类型占比。
踩坑与对策
sc.pl.stacked_violin(rotation=)
在新版 seaborn/matplotlib 下报
unexpected keyword argument 'rotation'
——去掉该参数即可。
sc.pl.umap(layer=...)
切层时确认该层存在。
中文字体被 scanpy 静默清掉（本轮最隐蔽的坑）
：
sc.set_figure_params()
内部的
set_rcParams_scanpy()
会把
rcParams['font.sans-serif']
覆盖为
['Arial','Helvetica','DejaVu Sans',...]
（无 CJK）。无论 matplotlibrc 里怎么配、无论在 import 后多久设置，只要在这之前设都会被清掉——中文标题全部变成豆腐块。且
warnings.filterwarnings('ignore')
会把 matplotlib 的 "Glyph missing from font" UserWarning 一并吞掉，日志一片干净、图全是豆腐。
正确做法：set_figure_params() 调用之后再显式设置
plt.rcParams['font.sans-serif']=['WenQuanYi Micro Hei','DejaVu Sans']
，并用
font_manager.findfont()
断言解析到 .ttc 文件；出图脚本不要全局 suppress UserWarning。
结果图
图 M5-a · UMAP 默认层
图 M5-b · marker 气泡图（五类之一）
图 M5-c · marker 热图（GEO 权威分组 + 按基因 z-score，特异 marker 精选）
图 M5-d · 各组织来源的细胞比例
九、M6 拟时序 · biomamba-sc-trajectory
技能来源：U002 · Palantir / PAGA / scVelo
目的
PAGA 图抽象 + Palantir 扩散映射拟时序 + （scVelo）RNA 速率。
本次实证
PAGA：以 leiden 为分组得到
31 个簇
的图抽象；
Palantir：n_components=5、num_waypoints=500、定义 2 个终点，
对 17,490 个上皮细胞
跑通，识别分化轨迹；
scVelo：
跳过
——本数据集是 10x 3' 表达矩阵，
无 spliced/unspliced 分层
（无 bam/loom），RNA 速率动力学建模不适用。
踩坑与对策
scVelo 数据前提
：RNA 速率需要内含子/外显子分层计数（10x 5' + velocyto，或 spliced/unspliced loom）。GSE131907 只提供表达矩阵，强跑会得到无意义结果，故诚实跳过。
PAGA 规模
：在 10 万细胞上 PAGA 的 fr 布局无法收敛，需先做细胞类型级抽象或限定子集。
结果图
图 M6-a · PAGA 图抽象（leiden 分组）
图 M6-b · PAGA draw_graph 布局
十、M7 细胞通讯 · biomamba-sc-communication
技能来源：U003 · CellPhoneDB v5
目的
CellPhoneDB 受体-配体互作：下载并构建 v5 数据库 → 准备 counts+meta → 三种方法（analysis / statistical_analysis / degs_analysis）→ 解读与可视化。
本次实证
分层抽样至
30,000
细胞（10 万细胞直接跑置换检验不可行），分 4 组：Normal 38,581 / Tumor 27,443 / Metastasis 24,238 / Effusion 9,738；
analysis / statistical 方法全通，
2,432 条互作
（Tumor 子集 2,209 / Normal 子集 2,016）；
另对 Tumor vs Normal 单独跑了对比分析。
踩坑与对策
v5 API 变化
：CellPhoneDB v5 是文件路径式 API（
cpdb_file_path/meta_file_path/counts_file_path
），
无 log2 参数
，且不再有 v4 的命令行；数据库需先下载构建到本地。
规模
：30k 细胞已是内存/时间上限，原始 100k 需先抽样。
结果图
图 M7-a · 细胞对互作数量（全部）
图 M7-b · Tumor vs Normal 差异互作
十一、M8 拷贝数变异 · biomamba-sc-cnv
技能来源：U005 · infercnvpy / copykat
目的
用 CNV 推断鉴定肿瘤细胞：参考集取免疫细胞（T/NK、B、Myeloid、MAST），对上皮细胞等做 infercnvpy，再算 cnv_score、CNV 谱聚类、UMAP。
本次实证（infercnvpy）
infercnvpy 0.6.1，取 60,000 细胞、5 类子集；基因染色体位置来自
UCSC ncbiRefSeq (hg38)
，
19,061/29,634
基因匹配到染色体；
infercnv 状态 ok（window_size=100、chunksize=5000 防内存爆）；UMAP + cnv_score 完成；
5 张 CNV 图（染色体热图、cnv_leiden 热图、高/低 score、UMAP）。
本次新增：copyKAT（R 直跑，绕过 rpy2）
infercnvpy 内嵌的
cnv.tl.copykat
依赖 rpy2 + R 包，本环境未部署。改用
系统 R 直跑 copyKAT v1.1.0
（已安装）：Python 端导出上皮细胞（12,022 个，按 Sample 分层抽样）的
基因×细胞 counts 稀疏矩阵
，R 端读入后
转稠密矩阵
再跑（copyKAT v1.1.0 无法处理稀疏三元组矩阵）。输出每个细胞的 aneuploidy 判读 + 热图。
踩坑与对策
infercnvpy 染色体名
：必须保留
chr
前缀（源码
x.startswith('chr')
），剥掉前缀会让染色体列表为空。
UCSC 列名
：ncbiRefSeq 表头需含
name
列，漏写会让
chrom/name2
整体错位。
copyKAT 输入
：稀疏三元组矩阵（dgTMatrix）会触发
as.data.frame
报错，需
as.matrix()
转稠密。
肿瘤占比
：本数据肿瘤占比极高（~88%），inferCNV 在肿瘤占比过高样本可能不可靠，需结合 copyKAT 互证。
结果图
图 M8-a · infercnvpy 染色体热图（按细胞类型）
图 M8-b · cnv_score 的 UMAP 分布
copyKAT 判读结果（R v1.1.0，稠密矩阵输入）
共判读
12022
个上皮细胞，整体分布：aneuploid
7134
· diploid
3993
· not.defined
895
。aneuploid（非整倍体）通常对应恶性/肿瘤细胞，diploid 为正常上皮，tetraploid 为四倍体异常；可与 infercnvpy 的 cnv_score 互为正交证据。
Sample（10x 文库）
aneuploid
diploid
not.defined
BRONCHO_11
21
44
8
BRONCHO_58
27
97
34
EBUS_06
165
162
76
EBUS_10
34
76
16
EBUS_12
11
69
4
EBUS_13
31
72
24
EBUS_15
41
29
18
EBUS_19
5
66
5
EBUS_28
1545
0
34
EBUS_49
31
0
8
EBUS_51
51
367
28
EFFUSION_06
31
30
18
EFFUSION_11
9
18
2
EFFUSION_12
1
9
0
EFFUSION_13
20
0
0
EFFUSION_64
1
0
2
LUNG_N01
72
0
3
LUNG_N06
51
0
2
LUNG_N08
84
0
3
LUNG_N09
138
0
1
LUNG_N18
122
0
7
LUNG_N19
51
0
1
LUNG_N20
86
0
8
LUNG_N28
75
0
4
LUNG_N30
99
0
12
LUNG_N31
175
0
11
LUNG_N34
185
0
14
LUNG_T06
42
0
0
LUNG_T08
13
0
0
LUNG_T09
33
0
1
LUNG_T18
109
215
17
LUNG_T19
93
0
2
LUNG_T20
45
114
12
LUNG_T25
75
0
3
LUNG_T28
100
295
10
LUNG_T30
262
0
16
LUNG_T31
40
40
11
LUNG_T34
797
0
33
NS_02
17
41
8
NS_03
1
880
33
NS_04
76
278
39
NS_06
12
9
12
NS_07
1570
1
85
NS_12
345
480
112
NS_13
134
215
102
NS_16
22
0
1
NS_17
92
250
32
NS_19
94
136
23
红色 = 该文库的 aneuploid（非整倍体）上皮细胞数，通常对应恶性/肿瘤细胞。
图 M8-c · copyKAT 染色体拷贝数热图（按细胞，aneuploid/diploid 分列）
十二、M9 共表达网络 · biomamba-sc-network
技能来源：U004 · 相关性网络 / KMeans / pyscenic
目的
基于表达相关性的共表达网络 + KMeans 模块划分；pyscenic 转录因子调控网络（grn→ctx→aucell）为进阶。
本次实证
相关性网络（pearson）：取上皮 17,490 细胞的 120 个高变基因，top |r| =
0.692
，导出 top 相关基因对；
KMeans 模块划分（8 类）：模块大小 0:1 / 1:16 / 2:4 / 3:1 / 4:89 / 5:1 / 6:1 / 7:7；
输出模块热图、模块 UMAP、top 基因 JSON。
踩坑与对策
pyscenic 环境冲突
：技能要求严格按
numpy==1.19.5 → pandas==1.3.5 → numba==0.56.4 → pyscenic==0.12.1
顺序安装，与 scanpy 1.11.4 的依赖不兼容，本环境未单独隔离。已记录为「skipped」并保留可复现路径（见第十五章）。相关性网络 + KMeans 是可独立使用的替代方案。
结果图
图 M9-a · 共表达网络（top 相关基因对）
图 M9-b · KMeans 模块在 UMAP 上的分布
十三、诚实的一半：未完全跑通项的处理
哪些修好了、哪些仍受限、为什么。
项
状态
说明
ingest（M2）
✅ 修复
pynndescent 0.6.0+numpy2 卡死 → 改用「PCA 投影 + gauss 邻居 + 合并 UMAP」等价实现，图已产出。
copyKAT（M8）
✅ 已实现
绕过 rpy2，用系统 R 直跑 copyKAT v1.1.0（稠密矩阵输入），作为 infercnvpy 的第二种正交 CNV 判读，并已产出判读表 + 染色体热图。
pyscenic（M9）
⚠ 受限
依赖严格版本顺序与 scanpy 1.11.4 冲突，需独立虚拟环境 + 下载 ~100MB GRN/motif 数据库；本次以相关性网络 + KMeans 替代，并保留复现路径。
scVelo（M6）
⛔ 数据不支持
数据集为 10x 3' 表达矩阵，无 spliced/unspliced 分层，RNA 速率动力学无输入；非代码问题，强行跑会得到无意义结果。
原则
：能在合理成本内修复的（ingest、copyKAT）我们修复了；属于环境/数据硬限制的（pyscenic、scVelo）如实标注，而不是用本地 mock 伪装跑通。这是本手册与「一遍过」教程的本质区别。
十四、复现命令总表
服务器路径：/data3/biomamba/analysis/ST_shengtai/GSE131907_skills
所有模块脚本位于
scripts/
，结果位于
result/
。按依赖顺序：
# 0) 环境（scanpy 1.11.4 虚拟环境 ./env）
cd /data3/.../GSE131907_skills
# 1) 基础 + 对齐铁律（务必先 anno.loc[cell_names]）
./env/bin/python scripts/M1a_read.py          # 读入 + 对齐（返回 208,500 细胞 h5ad）
./env/bin/python scripts/M1b_core.py          # QC/归一化/HVG/PCA/leiden/UMAP/marker
./env/bin/python scripts/M2_batch.py          # 批次校正（baseline/BBKNN/harmony）
./env/bin/python scripts/M2b_ingest.py        # ingest 修复版（PCA投影+gauss UMAP）
# 2) 注释与双细胞
./env/bin/python scripts/M3_annotation.py     # CellTypist + marker 注释
./env/bin/python scripts/M3c_scrublet.py       # 按文库逐样本 scrublet
# 3) 下游四路（互不依赖，可并行）
./env/bin/python scripts/M4_de_enrich.py       # 差异 + GO/KEGG/GSEA
./env/bin/python scripts/M5_viz.py             # 可视化
./env/bin/python scripts/M6_trajectory.py      # PAGA + Palantir
./env/bin/python scripts/M7_communication.py   # CellPhoneDB
./env/bin/python scripts/M8_cnv.py              # infercnvpy
./env/bin/python scripts/M9_network.py         # 相关性网络 + KMeans
# 4) copyKAT 旁路（R 直跑）
./env/bin/python scripts/M8b_copykat_export.py # 导出上皮细胞 counts（稀疏）
Rscript scripts/M8b_copykat_run.R              # R 端 copyKAT（稠密矩阵）
全程最贵的步骤是 M1b（~18 min）与 M2 harmony（~22 min）；M3/M4/M5/M7/M8/M9 多为 2~11 min；M6 Palantir 约 11 min。重跑前若已修正对齐，所有下游脚本无需改路径。
十五、技能索引与参考
9 个蒸馏 Skill（学习路径）
biomamba-sc-core（M1）
biomamba-sc-batch（M2）
biomamba-sc-annotation（M3）
biomamba-sc-de-enrich（M4）
biomamba-sc-viz（M5）
biomamba-sc-trajectory（M6）
biomamba-sc-communication（M7）
biomamba-sc-cnv（M8）
biomamba-sc-network（M9）
关键参考文档
每个 Skill 的
references/pitfalls.md
：本次把 15 条实测坑（含对齐铁律、scrublet 不能 pooled、counts 层被 log 覆盖、harmonypy 不转置、infercnvpy 需 chr 前缀、UMAP rotation 参数等）已回填进 9 个 Skill；
知识库
merged_kb.json
（units=EMPIRICAL-GSE131907，与教材 U00x 分开标记）；
原始文献：Kim et al., 2019（GSE131907，LUAD 多部位转移 scRNA-seq）。
本手册定位
：它是上面 9 个 Skill 的「实战串联版」——用一份真实数据的完整跑通 + 一次真实返工，把分散在教材单元 U001/U002/U003/U004/U005/U006 的知识点连成一条可复现的流水线。建议配合各 Skill 的
SKILL.md
与
params.md
白名单对照阅读。

![图2](../images/A0003_02.png)

![图3](../images/A0003_03.png)

![图4](../images/A0003_04.png)

![图5](../images/A0003_05.png)

![图6](../images/A0003_06.png)

![图7](../images/A0003_07.png)

![图8](../images/A0003_08.png)

![图9](../images/A0003_09.png)

![图10](../images/A0003_10.png)

![图11](../images/A0003_11.png)

![图12](../images/A0003_12.png)

![图13](../images/A0003_13.png)

![图14](../images/A0003_14.png)

![图15](../images/A0003_15.png)

![图16](../images/A0003_16.png)

![图17](../images/A0003_17.png)

![图18](../images/A0003_18.png)

![图19](../images/A0003_19.png)

![图20](../images/A0003_20.png)

![图21](../images/A0003_21.png)

![图22](../images/A0003_22.png)

![图23](../images/A0003_23.png)

![图24](../images/A0003_24.png)

![图25](../images/A0003_25.png)

解读报告

我们课程中的文献解读重要性就体现出来了，本skills可以直接帮你整理分析结果的解读报告，直接就能上组会汇报！
GSE131907 转移性肺腺癌：按生物学逻辑重组的单细胞解读
从「九模块工具账本」到「六个生物学问题」——按原文章叙事链组织全部真实分析结果
原文章锚点：Kim N, et al.
Single-cell RNA sequencing demonstrates the molecular and cellular reprogramming of metastatic lung adenocarcinoma.
Nat Commun 2020;11:2285（PMID 32385277，DOI 10.1038/s41467-020-16164-1）
208,506 细胞 · 58 样本 · 44 患者
7 个组织部位
scanpy 1.11.4 · celltypist 1.7.1 · infercnvpy 0.6.1
分析子集 100,000 细胞
全部数字来自本次实跑
问题链目录
基线：数据、质控与权威注释
Q1 组织部位如何重塑免疫构成？（原文 Fig 1）
Q2 恶性上皮细胞在哪些部位占主导？（原文 Fig 2）
Q3 髓系如何从 resident 转向 mo-Mac？（原文 Fig 4）
Q4 T/NK 如何走向耗竭？（原文 Fig 5）
Q5 间质与血管如何被重编程？（原文 Fig 3）
Q6 通讯网络的枢纽是谁？（原文 Fig 6）
系统对照：原文结论 × 我们的证据
增量、局限与复现索引
导读：为什么需要一次「逻辑重组」
配套的《九模块学习手册》按工具链组织内容（M1 基础 → M9 网络），回答的是「每个模块怎么跑、坑在哪」。 但模块顺序
不等于生物学逻辑
：把 QC 参数、批次校正、scrublet、CellPhoneDB 平铺给读者，得到的是账本而非结论。 本报告换一条主线——
原文章的科学问题链
：
问题链
：① 不同组织部位的免疫构成差在哪 → ② 恶性上皮细胞在哪些部位占主导 → ③ 髓系如何从 resident 巨噬细胞换成单核细胞来源 → ④ T/NK 如何走向耗竭 → ⑤ 间质与血管如何被重编程 → ⑥ 谁在通讯网络中心。 每一章的结构统一为：
原文问了什么 → 我们用现有数据找到什么 → 与原文的一致性
。
新增的五张证据图（
gse131907_results/story/S*.png
）与全部汇总表，由
scripts/_story_numbers.py
从既有 h5ad/CSV
轻量计算
（8.2 秒，不重跑流水线）， 字体配方与出图校验沿用修复轮标准（零缺字形警告 + 非空白断言）。
一、基线：数据、质控与权威注释
后续所有章节的地基——细胞从哪来、注释凭什么可信
208,506 个细胞来自 44 例未治疗 LUAD 患者的 58 个样本，覆盖 7 个组织部位：正常肺（nLung）、 原发瘤（tLung）、EBUS/支气管活检晚期原发瘤（tL/B）、正常淋巴结（nLN）、转移淋巴结（mLN）、 脑转移（mBrain）、胸腔积液（PE）。为控制计算量，后续分析在
按组织来源分层抽样的 100,000 细胞子集
上进行。
图 0 · GEO 原文注释的细胞图谱（100,000 细胞子集，回填后九大类）
注释凭什么可信
GEO 原文注释列为权威标签
：
Cell_type.refined
缺失的 13,676 个细胞按同为原文列的
Cell_type
回填，最终九大类：T/NK 43,791 · Myeloid 20,268 · Epithelial 17,490 · B 13,258 · Fibroblasts 1,928 · MAST 1,597 · Endothelial 1,050 · Oligodendrocytes 331 · Undetermined 287。
CellTypist 独立交叉验证
：Immune_All_Low 模型在 60,000 个免疫细胞上预测出 29 个亚型， 与官方注释呈清晰对角线（Memory/Naive B↔B lymphocytes、Tcm/Naive helper T↔T/NK cells、 Alveolar macrophages/Macrophages↔Myeloid cells、Mast cells↔MAST cells）， 免疫子集里的「上皮细胞」预测从错位版的 9,600 降到
10
个。
双细胞按 58 个 10x 文库逐样本 scrublet
（修正 pooled 100% 误判后）：669 个（0.669%）， 每文库中位数 0.47%。
口径提醒
：本报告的比例数字除特别说明外均基于 100,000 细胞子集；免疫亚型分布基于 60,000 免疫细胞子集； copyKAT 恶性判定基于 12,022 个上皮细胞；infercnvpy 基于 60,000 细胞（上皮 + 髓系参照）。
Q1
组织部位如何重塑免疫构成？
对应原文 Fig 1——「组织解离导致免疫细胞比例被高估；mLN 含大量髓系；肿瘤 T/B 富集而 NK/髓系下降」
图 1 · GEO 权威注释细胞构成 × 组织部位（列内占比 %）
我们的发现
观察
数字（100k 子集）
原文对照
正常肺由髓系主导（肺泡巨噬细胞）
nLung：Myeloid 46.1%、T/NK 31.4%、上皮仅 10.0%
一致（正常肺髓系占比最高）
转移淋巴结髓系富集
mLN 髓系
27.3%
vs nLN
4.1%
（相差 6.7 倍）
✅ 原文 Fig 1 明确报道「mLN 含有大量 myeloid 细胞」
原发瘤 B 细胞扩增、NK 枯竭
B：nLung 1.7% → tLung
13.3%
；CD16+ NK（T/NK 内）：14.9% →
1.3%
✅ 原文「tLung 中 T、B 淋巴细胞富集而 NK、myeloid 下降」
转移部位由上皮（恶性）细胞主导
mBrain 上皮
59.2%
、tL/B 59.5%，而 nLung 仅 10.0%
一致（转移灶肿瘤细胞占比高）
淋巴结是 T/B 的海洋
nLN：T/NK 61.6% + B 34.3%，无上皮
一致
一句话
：同一套细胞类型，七种组织部位给出七种构成——「部位」本身就是一个强烈的生物学变量， 这正是原文全篇的出发点。
Q2
恶性上皮细胞在哪些部位占主导？
对应原文 Fig 2——「tS2 癌细胞状态完全偏离正常分化程序，随进展与转移富集」
图 2 · 恶性上皮细胞比例 × 部位：copyKAT（左）与 infercnvpy 高 CNV（右）
我们的发现（infercnvpy，以上皮+髓系 60k 子集、髓系为二倍体参照）
部位
上皮 CNV score 中位数
CNV score 前 25% 占比
上皮细胞 n
mBrain（脑转移）
0.0179
97.6%
5,398
tL/B（晚期原发瘤）
0.0151
90.8%
2,302
tLung（原发瘤）
0.0088
66.0%
2,476
mLN（转移淋巴结）
0.0081
44.5%
1,073
nLung / PE
0.0068 / 0.0065
0% / 0%
1,219 / 151
CNV 信号强度随恶性程度单调递增：
正常肺 ≈ 胸腔积液 < 原发瘤 ≈ 转移淋巴结 < 晚期原发瘤 < 脑转移
， 脑转移灶 97.6% 的上皮细胞 CNV 信号位于全部分析细胞的前 25%——与原文「转移由 aggressive 癌细胞主导」方向一致。
图 2b · infercnvpy CNV UMAP（染色体臂水平 CNV 状态）
实测方法学坑：pooled copyKAT 在本数据上失效。
R 端 copyKAT（12,022 个上皮细胞 pooled 跑， GMM 自定二倍体参照）把
正常肺 11 个样本的 89–99% 判为 aneuploid
，与 infercnvpy 的 0% 直接矛盾； 其二倍体模式落到了个别样本（如 NS_03 的 880/881 个细胞）而非正常组织——典型的
批次效应压倒生物学信号
。 这从反面印证了 infercnvpy「髓系/免疫细胞作参照」设计的价值。
结论：恶性判定以 infercnvpy 为准， copyKAT 结果仅作方法对照留存。
与原文的差距（诚实清单）
：原文用 Monocle 2 构建恶性-正常上皮联合轨迹，识别出完全偏离正常分化程序的
tS2 癌细胞状态
（28 个 signature 基因，晚期/转移富集，TCGA LUAD 中预测不良生存，IHC 标志物 IGFBP3/S100A2/CK19/AG2）。 本次未复现该分析（需要癌细胞拟时序 + 外部 bulk 生存数据），已列入局限。
Q3
髓系如何从 resident 转向 mo-Mac？
对应原文 Fig 4——「正常肺由 resident 肺泡巨噬细胞主导；肿瘤与转移的 TAM 主要由单核细胞来源巨噬细胞（mo-Macs）构成」
图 3 · CellTypist 免疫亚型 × 组织部位（60,000 免疫细胞子集，行内占比 %）
我们的发现（以 CellTypist 亚型为代理指标）
部位
resident 肺泡巨噬细胞（髓系内 %）
mo-Mac 代理（Macrophages+单核细胞，%）
nLung
73.7
17.4
tLung
29.8
53.6
（首次反超）
tL/B
9.3
74.2
nLN
42.6
12.5
mLN
1.7
88.6
mBrain
8.3
86.8
PE
0.1
76.1
「resident → 单核细胞来源」的替换在原发瘤即完成（29.8% vs 53.6%，
首次反超
）， 在转移部位走向极致（mLN 88.6%、mBrain 86.8%）；其中 Macrophages 亚型本身从 nLung 的 3.1% 升至 mBrain 的
45.6%
、mLN 的 25.6%，而肺泡巨噬细胞从 nLung 的 41.6% 跌到 mLN 的 0.6%。 这与原文 Fig 4 的核心结论逐条对应。
图 3b · CellTypist 预测 vs GEO 官方注释一致性（对角线=互证）
口径说明
：我们没有原文的 monocle 拟时序来直接证明「单核细胞 → TAM」的本体发生学路径， 此处以「resident 标志亚型 vs 单核/巨噬亚型的此消彼长」作为代理证据，方向与原文一致； pDC 在肿瘤/转移中的免疫抑制表型（原文 Fig 4）因 pDC 占比过低（≤0.5%）未能定量。
Q4
T/NK 如何走向耗竭？
对应原文 Fig 5——「NK 在原发瘤耗竭；Treg 出现；exhausted CD8 来自肿瘤、cytotoxic 来自正常肺、naive 来自 nLN 和 PE」
图 4 · T/NK 功能与耗竭 marker × 部位（点大小=表达细胞比例，颜色=平均表达）
我们的发现（43,791 个 T/NK 细胞，按部位平均表达）
marker 组
nLung
tLung
tL/B
mLN
mBrain
PE
解读
细胞毒 NKG7 / GZMB / PRF1
3.04/1.96/1.41
1.22/0.74/0.41
2.26/1.09/0.89
1.58/0.83/0.74
1.46/0.78/0.70
1.11/0.23/0.30
正常肺 T/NK 细胞细胞毒程序最强，肿瘤中系统性下调
耗竭 PDCD1 / TIGIT / CTLA4
0.05/0.27/0.04
0.19/0.49/0.23
0.18/0.63/0.27
0.16/0.56/0.23
0.18/0.48/0.17
0.07/0.30/0.06
PD-1 在肿瘤/转移升高 3–4 倍，TIGIT 在 tL/B 最高
Treg FOXP3
0.02
0.07
0.11
0.08
0.10
0.05
Treg 程序在肿瘤/转移出现（原文：Treg 出现并持续至晚期）
naive/记忆 IL7R / CCR7 / SELL
0.47/0.08/0.14
0.93/0.34/0.23
0.70/0.18/0.35
0.86/0.51/0.53
0.72/0.14/0.23
1.11/0.69/0.67
naive 程序在
nLN（1.25/0.75/0.82）与 PE
最高，肿瘤中最低
亚型构成给出同向证据：naive 样
Tcm/Naive helper T 细胞在 nLN 占 44.3%
、PE 27.0%，而 tLung 仅 4.4%； 耗竭-效应样
Tem/Trm cytotoxic T 细胞从 nLung 2.8% 升至 tLung 11.5%、mBrain 12.8%、PE 15.7%
； Regulatory T 从 nLung 1.1% 升至 tLung 7.3%；CD16+ NK 从 nLung 14.9% 跌至 tLung 1.3%。
原文 Fig 5 五条结论，我们复现了五条
：① NK 原发瘤耗竭 ✅ ② Treg 出现并持续 ✅ ③ exhausted CD8 主要来自肿瘤/转移 ✅ ④ cytotoxic effector 主要来自正常肺 ✅ ⑤ naive CD8 主要来自 nLN 与 PE ✅。
Q5
间质与血管如何被重编程？
对应原文 Fig 3——「肿瘤内皮激活 VEGF/Notch、INSR 过表达；肌成纤维细胞仅来自肿瘤组织，逐步替代 matrix fibroblasts」
本次未对内皮/成纤维细胞做独立亚群分型（原文为 8 个 EC cluster + 12 个 FB cluster）， 以 marker 均值按部位比较（1,928 个成纤维细胞 + 1,050 个内皮细胞）：
marker
细胞类型
nLung
tLung
tL/B
mLN
mBrain
解读
ACTA2
（肌成纤维细胞标志）
Fibroblasts
0.67
1.29
1.60
1.04
1.68
肌成纤维程序在肿瘤/转移显著升高（原文：myofibroblasts 仅来自肿瘤组织）
COL1A1 / COL13A1 / COL14A1
Fibroblasts
1.99/0.07/0.60
2.61/0.11/0.60
2.93/0.18/0.20
3.33/0.10/0.34
2.78/0.22/0.19
基质重塑程序广泛升高
PECAM1 / VWF（内皮标志）
Endothelial
1.72/1.58
1.84/2.05
1.57/2.00
1.98/2.31
1.60/2.21
各部位内皮身份稳定（作内部对照）
INSR
（胰岛素受体）
Endothelial
0.13
0.61
0.81
0.00
1.42
与原文「INSR 在肿瘤血管过表达、潜在治疗靶点」方向一致
与原文的差距
：原文报道肿瘤 EC 特异性激活 VEGF/Notch 并下调免疫激活基因（68 基因签名）， 我们只有 bulk marker 均值，未做 EC 亚群的差异签名——列入局限。
Q6
通讯网络的枢纽是谁？
对应原文 Fig 6——「tS2 与髓系/间质 crosstalk 主导；mo-Macs 是通讯枢纽；VEGF-VEGFR 贯穿血管生成」
图 6 · 关键配体-受体轴：肿瘤 vs 正常肺（CellPhoneDB mean，取该轴最强细胞对）
我们的发现（CellPhoneDB analysis 方法，Tumor vs Normal）
配体-受体轴
生物学功能
Tumor mean
Normal mean
最强细胞对
原文对照
VEGFA–FLT1
血管生成
1.124
0.432
上皮→内皮
✅ 2.6 倍上调，方向一致
VEGFA–KDR
血管生成
0.948
0.424
上皮→内皮
✅ 2.2 倍上调
VEGFB–FLT1
血管生成
0.705
0.339
上皮→内皮
✅ 一致
EREG–EGFR
肿瘤自分泌生长
1.070
—
上皮→上皮
✅ 一致（原文 mLN 中显著）
TNF–TNFRSF1A
炎症/存活
0.906
—
髓系→上皮
✅ 一致
CSF1–CSF1R
巨噬细胞存活
0.736
—
MAST→髓系
✅ 一致
LGALS9–HAVCR2
免疫抑制（T 细胞）
1.392
1.580
髓系→髓系
🔶 方向相反但绝对值高，需亚群分辨率
血管生成轴（VEGFA/VEGFB → VEGFR1/2）在肿瘤中
2.2–2.6 倍
上调，与 Q3（mo-Mac 扩张）、 Q5（INSR 过表达）互相印证：
髓系重编程与血管重编程是同一场「促瘤微环境」的两个侧面
。 NECTIN2–TIGIT 轴在 means 表中未达显著（我们未做逐对的置换检验筛选），列入局限。
图 6b · 全图谱 Top30 细胞对互作强度（CellPhoneDB analysis 方法）
图 6c · 肿瘤 vs 正常肺细胞对互作强度差异
八、系统对照：原文结论 × 我们的证据
原文核心结论
我们的证据
一致性
mLN 髓系富集（与 nLN 截然不同）
mLN 27.3% vs nLN 4.1%（Q1）
✅ 复现
肿瘤 T/B 富集、NK 与 resident 髓系下降
B 1.7%→13.3%；CD16+ NK 14.9%→1.3%；AM 73.7%→29.8%（Q1/Q3）
✅ 复现
tS2 癌细胞状态偏离正常程序、预测不良生存
未做癌细胞拟时序与 TCGA 生存（Q2 局限）
❌ 未覆盖
肿瘤/转移 TAM 以 mo-Macs 为主（本体发生学不同于 resident）
mo-Mac 代理 17.4%→53.6%→88.6%（Q3）
✅ 复现（代理指标）
NK 原发瘤耗竭、Treg 出现并持续、exhausted CD8 来自肿瘤
NKG7 3.04→1.22；FOXP3 0.02→0.07；PDCD1 0.05→0.19（Q4）
✅ 复现
cytotoxic CD8 来自正常肺、naive 来自 nLN/PE
NKG7/GZMB nLung 最高；Tcm/Naive nLN 44.3%、PE 27.0%（Q4）
✅ 复现
肌成纤维细胞仅来自肿瘤；肿瘤 EC 激活 VEGF/Notch、INSR 过表达
ACTA2 0.67→1.68；INSR 0.13→1.42（Q5）
🔶 部分（无亚群签名）
mo-Macs 是通讯枢纽；VEGF-VEGFR 贯穿各阶段
VEGFA-FLT1/KDR 肿瘤 2.2–2.6 倍上调（Q6）
✅ 复现（轴级）
exhausted CD8/mo-Mac 比例与 tS2 比例正相关
未做逐样本相关（缺 tS2 定义）
❌ 未覆盖
九、增量、局限与复现索引
相对公开复现的增量
GEO 原文注释作为金标准 + CellTypist 独立交叉验证
：29 个免疫亚型预测与官方注释呈对角线， 并在 barcode 错位事故后把「免疫子集里的上皮细胞」从 9,600 修正到 10；
58 个 10x 文库逐样本 scrublet
：修正 pooled 100% 误判（669 个双细胞，0.669%）；
infercnvpy 与 copyKAT 双 CNV 方法互证
：并实证了 pooled copyKAT 在多样本数据上的失效模式 （正常肺 89–99% 误判 aneuploid），反证参照设计的必要性；
真实机时总账
：有效 Python 计算 1h46m + copyKAT 5.6h（R），含返工全程约 13.5 小时机器占用。
局限（诚实清单）
分析基于
100,000 细胞分层子集
，非 208,506 全量；亚型比例为 60,000 免疫子集口径；
未复现原文的癌细胞 Monocle 轨迹 / tS2 状态 / TCGA 生存关联（需外部 bulk 数据）；
未做 EC/FB 亚群分型与差异签名、未做逐样本 TMB 关联；
scVelo（无 splicing 数据）与 pyscenic（依赖冲突）按技能规范记为「不适用」并跳过；
copyKAT pooled 结果失效（见 Q2），恶性判定以 infercnvpy 为准；CNV score 为相对量纲，跨数据集不可比。
复现索引
产物
位置
逻辑版新增证据图 + 汇总 CSV
gse131907_results/story/
（S1–S6，由
scripts/_story_numbers.py
生成，8.2s）
九模块完整流水线
scripts/M1_core.py … M9_network.py
（服务器
GSE131907_skills/scripts/
）
乱码修复与 CellTypist 修复
scripts/_fix_tofu.py
、
scripts/_fix_celltypist_dotplot.py
中间数据
服务器
result/GSE131907_*.h5ad
（core / batch_100k / annotated_100k / de / traj / cnv / network / viz_100k）
工具视角手册
《GSE131907_九模块单细胞全流程学习手册.html》
Biomamba 生信基地 · GSE131907 逻辑版解读 · 全部数字来自 2026-10 实跑（scanpy 1.11.4 / celltypist 1.7.1 / infercnvpy 0.6.1 / CellPhoneDB v5）

skills使用技巧

相应的，你在使用这个skills时，最好能够了解各个模块的功能和一句话使用方法
向下滑动查看完整内容
了解九模块的一句话使用方式，功能介绍：
M1 · 单细胞基础分析（biomamba-sc-core）
一句话
：从原始矩阵到一张干净的 UMAP——单细胞分析的地基，全程实测拆解。
介绍
：读矩阵 → QC → 归一化 → 高变基因 → PCA → Leiden 分群 → UMAP → marker，一步不落。 QC 阈值不抄教程，先看小提琴图分布再定；高变基因必须在原始 counts 上算——这两个细节错了， 后面全部白跑。学完你能独立把任何一个 10x 数据集从原始矩阵带到可注释的分群结果。
核心产出
：core.h5ad + QC/HVG/PCA/UMAP/marker 全套图 + 参数表
适合谁
：第一次上手 scanpy 的人；想把流程跑规范再谈下游的人
实战背书
：GSE131907 208,506 细胞全量跑通，18 分钟出全部结果
M2 · 多样本整合（biomamba-sc-batch）
一句话
：BBKNN / harmony / ingest 三招去批次，放在同一数据上对比给你看。
介绍
：多样本的批次效应是注释错乱的万恶之源。先跑 baseline 确认问题存在，再让三种方法 逐一上场，最后用 UMAP 判读谁把 58 个文库真正揉在了一起。学完你能按数据规模和样本结构 选对方法，而不是三种都跑一遍看哪个顺眼。
核心产出
：四方法对比 UMAP + 整合后 h5ad + 方法选择决策依据
适合谁
：手头有多个样本/多个批次数据的人；被"整合后样本还是分开"困扰的人
实战背书
：58 个文库整合；ingest 被上游兼容性问题卡死后，用手工 PCA 投影兜底成功——真实排障过程全记录
M3 · 细胞注释与双细胞（biomamba-sc-annotation）
一句话
：AI 自动注释 + 金标准交叉验证，注释不再靠猜。
介绍
：CellTypist 一键预测加 majority voting，再拿数据集自带的官方注释做金标准—— 对角线对得上，注释才敢往下用。双细胞检测必须按 10x 文库逐样本跑：混在一起跑会把 100% 的细胞误判成双细胞，这是我们实测踩过的坑，修正过程就是本模块的教案。
核心产出
：免疫亚型自动注释 + 预测/官方一致性矩阵 + 逐文库双细胞判定
适合谁
：分完群不知道每个簇是什么细胞的人；担心注释不靠谱的人
实战背书
：29 个免疫亚型与 GEO 官方注释对角线互证；scrublet 修正后双细胞率 0.669%
M4 · 差异与富集（biomamba-sc-de-enrich）
一句话
：差异基因只是开始，GO/KEGG/GSEA 才把基因列表翻译成生物学。
介绍
：按细胞类型批量跑 wilcoxon——把 T 细胞和巨噬细胞的差异混在一起是常见错误。 差异结果接 gseapy 的 enrichr 与 GSEA，回答"哪些通路在肿瘤里被激活"。富集结果按显著性 排序输出，这个细节决定了图表能不能直接放进汇报。
核心产出
：各细胞类型 DEG 表 + GO/KEGG/GSEA 结果 + 可视化图件
适合谁
：手上有多组样本要比较的人；差异结果不会解读的人
实战背书
：肿瘤 vs 正常 × 7 类细胞批量差异，一次跑完全部对比
M5 · 单细胞可视化（biomamba-sc-viz）
一句话
：五类图覆盖九成展示需求，附中文字体配方和出图自检流程。
介绍
：降维展示、marker 五件套（气泡/小提琴/矩阵/热图/track）、差异基因展示、 相关性与树图、细胞比例图——每类图的适用场景和参数都有实测范例。特别地：scanpy 会悄悄 清掉你设的中文字体，出图脚本还会吞掉缺字形的警告——本模块给出验证过的字体配方和 出图后三重校验（非空白 + 零乱码 + 与存档对账）。
核心产出
：17 张规范图件 + 中文字体配方 + 出图自检脚本
适合谁
：图总是差一口气的人；要出论文/汇报级图的人；被中文乱码折磨过的人
实战背书
：一次产出 17 张图；乱码问题从"抽查"升级为"三条件审计"根治方案
M6 · 拟时序分析（biomamba-sc-trajectory）
一句话
：Palantir + PAGA 给细胞排时间线——也讲清楚什么时候不该做。
介绍
：拟时序不是万能钥匙：临床样本没有发育时序，硬跑出来的"伪时间"没有意义。 本模块讲清楚适用边界，再用 Palantir 扩散映射算拟时间、PAGA 把复杂分群抽象成一张拓扑图。 RNA 速率需要 splicing 数据，没有就如实标注"不适用"——不硬跑、不编结果。
核心产出
：拟时间排序 + PAGA 拓扑图 + draw_graph 布局 + 适用性判断清单
适合谁
：研究细胞分化/演进/状态转换的人；想知道自己数据能不能做轨迹的人
实战背书
：走上皮亚群演进；scVelo 因缺 bam 数据明确跳过并在参数表记录原因
M7 · 细胞通讯（biomamba-sc-communication）
一句话
：CellPhoneDB：谁在给谁发信号，肿瘤里发了什么变了。
介绍
：受体-配体互作全流程：v5 数据库怎么装、三种计算方法（analysis / statistical / degs）怎么选、结果怎么读。10 万细胞直接跑置换检验不可行——按细胞类型分层抽样到 3 万是 实测可行的折中。最后把通讯表翻译成生物学结论：比如血管生成轴在肿瘤里上调了几倍。
核心产出
：细胞对互作表（means/statistical）+ Top30 强度图 + 分组对比图
适合谁
：想知道微环境里细胞间"对话"内容的人；差异结果需要机制解释的人
实战背书
：VEGFA-FLT1 轴肿瘤 2.6 倍于正常，与原文章结论互证
M8 · CNV 与肿瘤细胞鉴定（biomamba-sc-cnv）
一句话
：从表达矩阵揪出恶性细胞——infercnvpy + copyKAT 双方法互证。
介绍
：肿瘤样本里哪些上皮细胞是恶性的？靠表达矩阵推断染色体水平的拷贝数变异。 infercnvpy 用免疫/髓系细胞做阴性参照，copyKAT 走 R 旁路，两个方法互相验证。 基因位置从哪来、pooled copyKAT 为什么在多样本数据上会失效——这些坑我们都踩过， 修正后的判读规则直接给你。
核心产出
：染色体热图 + CNV UMAP + 各部位恶性细胞比例 + 方法选择依据
适合谁
：做肿瘤样本分析的人；需要把"恶性上皮"和"正常上皮"分开的人
实战背书
：脑转移 97.6% 上皮细胞高 CNV vs 正常肺 0%；copyKAT 失效模式实证记录
M9 · 共表达网络（biomamba-sc-network）
一句话
：从相关矩阵到基因模块——哪些基因程序在哪些部位活跃，一张图回答。
介绍
：上皮细胞高变基因的相关性矩阵不只是一张热图：取强相关对建网络、KMeans 划分 基因模块、按组织来源看模块富集。pyscenic 转录因子调控网络是进阶选项，依赖严格， 装不上就如实记录跳过，不假装跑过。模块 × 组织来源热图能直接写进结果讨论。
核心产出
：相关矩阵热图 + 基因网络图 + KMeans 模块划分 + 模块功能注释
适合谁
：想从"差异基因列表"再进一步找基因程序/模块的人
实战背书
：上皮 120 基因划分 8 模块；肌成纤维程序在脑转移显著富集
代码教程蒸馏（biomamba-code-distill）
一句话
：把任何生信代码教程，拆成九模块可复现笔记。
介绍
：教程元信息、学习目标、环境版本、核心代码（分步骤 + 完整可运行 + 预期输出）、 调参指南、可视化、常见报错、扩展示例、总结。重点是把"能跑的代码"和"为什么这样调参" 分开写，读者既能复现也能迁移。
适合谁
：教程作者、课程教研、需要把散代码整理成体系文档的人
文献阅读蒸馏（biomamba-literature-distill）
一句话
：高分文献八模块结构化笔记，从科学问题一路拆到方法迁移。
介绍
：元信息（联网核实，不凭记忆）→ 科学问题 → 实验设计 → 分析流程 → 结果解读 → 数据代码 → 方法迁移 → 局限。结果解读必须落到数字和基因名，不写"作者分析了 T 细胞" 这种空转。
适合谁
：组会汇报前要拆文献的人；做课题设计需要方法学参考的人

skills下载

通过网盘分享的文件：Python全程班单细胞skills

![图26](../images/A0003_26.png)

链接
:
https://pan.baidu.com/s/1Eha1ZktFZfuGiMrxQ2jJXA

提取码: 本内容属
2026订阅合集
，请订阅后请联系客服微信[Biomamba_zhushou]领取并
开通官网权限：www.biomamba.cn
