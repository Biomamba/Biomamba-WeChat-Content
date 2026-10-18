---
title: "openClaw+服务器+微信接入=拥有私人生信助理"
date: 2026-04-07
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536883&idx=2&sn=3b7c01eb3a9b7c8234980ee3dea52364&chksm=9b3c29a3ac4ba0b59fc3649a25f6f2d4b67eaf3aae4ce5142f3dd2156b2c59e568db640188c8#rd
albums: ["AI时代，不用就会被淘汰"]
---

# openClaw+服务器+微信接入=拥有私人生信助理

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536883&idx=2&sn=3b7c01eb3a9b7c8234980ee3dea52364&chksm=9b3c29a3ac4ba0b59fc3649a25f6f2d4b67eaf3aae4ce5142f3dd2156b2c59e568db640188c8#rd
> 合集：AI时代，不用就会被淘汰

# 一、Openclaw功能简介

**OpenClaw** （曾用名 **Clawdbot、Moltbot** ，因其图标常被昵称为“**龙虾** ”）是一个开源的**自主人工智能代理（AI Agent）框架** 。它由奥地利开发者Peter Steinberger于2025 年底发布，核心定位是“真正能替你做事的 AI（AI that actually does things）”。OpenClaw目前可以**部署在本地电脑/[ 服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535166&idx=2&sn=431238cb95bd4281424130333f6610c3&scene=21#wechat_redirect>)**，接入**企业微信，飞书** 等聊天工具进行控制，调用大模型（OpenAI,KIMI,MiniMax,Gemini等）进行操作电脑，执行任务。本教程将教大家如何把OpenClaw布置在服务器上，并通过企业微信与OpenClaw对话完成GEO数据库中转录组数据的处理(GSE130437)。当然，如果需要的话，也可以联系我们代为布置OpenClaw。![](../../images/3adc6cb9916709c2.png)![截屏2026-03-13 16.16.13](../../images/e6cc1a897c4962f7.webp)

# 二、服务器获取

openclaw的请求权限过高，使用存在风险(误操作、隐私泄露、设备被黑等)，但使用一个环境独立、具有[root权限的云服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532785&idx=2&sn=c364ab8365a845cd709251c026075e0a&scene=21#wechat_redirect>)部署就可以完美的避开这个问题，这里我们[免费提供2周的服务器使用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528216&idx=2&sn=b7be762860b48931492dad9f4a27017c&scene=21#wechat_redirect>)，足够大家部署使用，大家可以联系客服微信Biomamba_zhushou免费获取。

### 2.1 西柚云账号注册

复制网址(https://biomamba.xiyoucloud.net/)至浏览器，注册账号实名认证。

### 2.2 加购3.0学习版服务器

点击**产品与服务** 下的**订购产品**

![截屏2026-03-16 16.22.09](../../images/ab983d9d466f3c62.webp)

点击进入生信服务器列表，选择**3.0学习版** 的"点击购买"

![截屏2026-03-16 16.13.43](../../images/cf1b6f2a70ce7609.webp)

下拉右侧弹窗，点击加入购物车

![截屏2026-03-16 16.23.31](../../images/86c2fefac617e48f.webp)

点击**前往购物车**

![截屏2026-03-16 16.24.25](../../images/ec61a845aa2afcf2.webp)

###  2.3 输入优惠码

输入并应用优惠码，优惠码联系客服**Biomamba_zhushou** 获取，查看价格是否变成0元。

![截屏2026-03-16 16.28.03](../../images/807d51c6822a03cd.webp)

### 2.4 账户激活

联系上一步客服微信Biomamba_zhushou，发送账号/用户ID，我们为您激活服务器。

![](../../images/fe8ecb8594a1f419.webp)

### 2.5 创建实例

#### 2.5.1 进入控制台创建实例

#### 2.5.2 选择西南二区

进入镜像市场，点击**选择镜像并点击使用**

![截屏2026-03-16 16.34.12](../../images/fe03f7152631a31b.webp)

####  2.5.3 创建服务器实例，设置账户和密码，获取IP和端口

#### 注意：这里的**实例用户名** 和**实例密码** 尽量自定义的复杂一些，避免与他人名称可能重复，导致后续影响使用。

![微信图片_2026-03-17_094457_614](../../images/c0a2e63d88ce4f81.webp)

### 2.6 登录服务器

设置好之后，根据自己的账号密码，就可以用ssh正常远程连接啦，详细的登录步骤可以查看我们之前的[如何连接终端和Rstudio-server](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247524106&idx=3&sn=2a708129b846cbd6bd2fade3495afbd0&scene=21#wechat_redirect>)教程

![5](../../images/b5f1a20a488ce4da.webp)

# 三、服务器按照部署过程

### 3.1 运行安装脚本

首先使用自动化安装脚本
```
curl -fsSL https://openclaw.ai/install.sh | bash
```

安装不上，不使用安装脚本测试一下
```
npm install -g openclaw@latest#npm error CMake Error at CMakeLists.txt:1 (cmake_minimum_required):#npm error   CMake 3.19 or higher is required.  You are running version 3.16.3
#CMake的版本问题，更新一下CMakepip install cmake --upgrade
```

再次运行
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

![截屏2026-03-16 10.02.53](../../images/6ad3dee71f42a363.webp)

安装成功后会跳转到以下配置界面

### 3.2 配置环境

以下开始配置软件，进行基础设置

![截屏2026-03-13 12.47.15](../../images/437b65a5ef5aee17.webp)

接着根据我们的教程逐步的部署基础设置

![截屏2026-03-16 10.17.59](../../images/bd62583b73ae5585.png)

我明白这是默认仅供个人使用的，如果要用于共享/多人使用需要进行锁定（安全设置）。是否继续？选择yes

![截屏2026-03-16 10.18.27](../../images/bda87187c7185aa8.png)

这是选择后续通过`openclaw configure`配置，还是现在手动配置，选择Manual

![截屏2026-03-16 10.20.29](../../images/24bb53b01d5f3265.webp)

询问是否在**当前正在使用的这台电脑** 上直接安装并运行核心网关服务，选择Local getway(this machine)

![截屏2026-03-16 10.24.56](../../images/495e63437fd8f92c.png)

询问安装位置，这里默认即可

![截屏2026-03-16 10.26.55](../../images/20f13435ff191155.webp)

下面就是选择接入的模型了，上述图，**本教程选择MiniMax**

* * *

在https://pinchbench.com/可以查看各个模型的成功率和花费，综合任务执行成功率和花费，最终选择minimax-2.1,大家可以根据需要选取，考察了一下感觉coding-plan更划算，https://platform.minimaxi.com/subscribe/coding-plan，**一个月29块** ，注册订阅coding-plan

![未标题-6](../../images/fb09af4b5148d3cb.webp)

从表中也可以看到Minimax2.1在基准测试中表现比MiniMax2.5要好

* * *

![截屏2026-03-16 10.49.00](../../images/c0e62488c0ddf3fa.webp)

这里是选择国内还是国外,本次教程是coding plan套餐所以选择CN - Oauth

![截屏2026-03-16 10.49.21](../../images/e0f576522ef6a911.webp)

点击红框内容跳转网页**点击授权** 确认

![截屏2026-03-16 10.50.23](../../images/74e0d63e813dfb36.webp)

授权成功后

![截屏2026-03-16 10.52.34](../../images/6035ba14b9b7a01c.webp)

选择手动选取模型

![截屏2026-03-16 10.53.05](../../images/50b21fc9e9594200.png)

在各模型的基准测试中，**2.1结果要优于2.5，所以手动选择2.1**

![截屏2026-03-16 11.00.11](../../images/0ad73ddb58f11f7f.png)![截屏2026-03-16 10.57.26](../../images/8a6f418073c17163.webp)

接着是网关端口配置，我们西柚云给大家预留了三个端口可以自行分配，大家选择其中一个就可以

![截屏2026-03-16 11.01.21](../../images/eb23e9bcb0813b26.png)

设置 **Gateway（网关）绑定地址** 的选项，本质上是在决定：**这个服务要对哪些网络开放访问** 。这里选择第三个Auto就可以

![截屏2026-03-16 11.04.25](../../images/9c578d05619f7232.png)

配置 **OpenClaw** 网关（Gateway）时，系统让你选择**安全认证（登录）方式** ，选择Token

![截屏2026-03-16 11.06.54](../../images/5a429227b6c379ce.png)

通过 **Tailscale** 来配置你的网关网络访问权限,选择serve

![截屏2026-03-16 11.08.02](../../images/2c03f191ab66b2d7.webp)

选择yes

![截屏2026-03-16 11.08.39](../../images/cbac82bc67e1ce77.png)

选择default

![截屏2026-03-16 11.09.47](../../images/5a7d7a6c39e636da.png)

直接留空自动生成

![截屏2026-03-16 11.10.32](../../images/1c21177aca9e590c.png)

这里配置企业微信接入信息，选择yes

![截屏2026-03-16 11.11.34](../../images/c0f5619e4638adc4.webp)

默认没有企业微信，先跳过

![截屏2026-03-16 11.12.17](../../images/618ab57985b3a837.webp)

这里要给模型设置网页搜索功能，先跳过

![截屏2026-03-16 11.13.02](../../images/9908a35774893367.webp)![截屏2026-03-13 14.01.49](../../images/f8d5f3d4c246e5d8.webp)

配置一些ai工具的api，都选择no，都是非必要选项

![截屏2026-03-16 11.16.52](../../images/3e28f3574d04dcd8.webp)

选择"Hooks",相当于“龙虾的记忆”，`session-memory`含义为当你在终端输入 `/new`（开启新对话）或 `/reset`（重置当前对话）时，Hook 会自动提取上一轮对话中的**核心结论和关键信息** ，存入 Agent 的长期记忆库中。

![截屏2026-03-16 11.20.05](../../images/75104de979561278.webp)

是否安装网关服务，yes，Node

![截屏2026-03-16 11.21.33](../../images/ec042f31e0a01fb5.png)

选择Do this later

![截屏2026-03-16 11.21.55](../../images/77217bcf5c7db10d.webp)

yes

选择完之后，基础配置就结束了

### 3.3 接入企业微信

首先下载企业微信客户端，登录后点击工作台

![截屏2026-03-16 11.25.42](../../images/68b0a308a0bc14c3.webp)

点击智能机器人

![截屏2026-03-16 11.27.14](../../images/2536bf5009ee2e66.webp)

点击创建机器人，点击**手动创建**

![截屏2026-03-16 11.28.42](../../images/f17412419a2d6ece.webp)

拖到最下方选择**API模式创建**

![截屏2026-03-16 11.31.11](../../images/f39d776d70dd776c.webp)

按照如上点击设置，获取**bot id** 和**secret** ，拖到到最后点击保存

**接着在linux上配置企业微信插件**
```
#添加环境变量echo'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrcsource ~/.bashrc
#安装企业微信插件npx -y @wecom/wecom-openclaw-cli install
```

![截屏2026-03-16 11.51.30](../../images/865c20bdf0ae767a.webp)

选择手动输入

![截屏2026-03-16 11.52.43](../../images/5ca9be0f5ea04b0c.webp)

输入在企业微信中的**bot id** 和**secret**
```
#我们手动拉起一下，这样可以想停就停openclaw gateway stopopenclaw gateway --port20389
```

![截屏2026-03-13 14.04.50](../../images/4d272a4de1b7c42f.webp)

这样就可以在企业微信里回消息了

![截屏2026-03-16 12.33.19](../../images/22a1fdd42e144972.webp)

### 3.4 安装skills

OpenClaw的**Skills是赋予AI智能体执行实际任务能力的扩展插件** ，使其从单纯的聊天机器人进化为强大的自动化助理。而腾讯的**SkillHub** 则是专为国内优化的本土化技能商店，它不仅提供**高速镜像下载解决网络瓶颈** ，还进行了全中文适配与安全审计，并深度接入了腾讯生态，降低了skills的安装门槛。
```
#大家可以上网站上找一下适合自己的插件https://skillhub.tencent.com/#featured
#安装skillhubcurl-fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash  -s----no-skillscurl-fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
#配置环境变量echo'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrcsource ~/.bashrcskillhub install tavily-search
#注意安装路径，后续还要用到
```

接着我们需要获取tavily的api，在官网上注册登录后就可以进行免费获取，每个月有**1000次的免费额度**

![截屏2026-03-16 12.50.47](../../images/87630444be7060bb.webp)![截屏2026-03-16 12.51.04](../../images/a0a3dc5b6ee35b43.webp)

将api-key写入`~/.openclaw/.env`
```
TAVILY_API_KEY=...
```

重启一下openclaw，将安装skills的位置告诉openclaw启用，这里我还安装了其他的skills。

![截屏2026-03-16 13.05.55](../../images/530d71128abdc47f.webp)

调用一下试一试

![截屏2026-03-16 13.09.48](../../images/b3759ad079fa0ed5.webp)

可以在tavily官网看一下，可以看到已经在使用

![截屏2026-03-16 13.07.04](../../images/d72218f1e4013abc.png)

# 四、使用案例

### 4.1 检索文献

![截屏2026-03-16 15.45.34](../../images/038699c66ca4e5d9.webp)![截屏2026-03-16 15.45.52](../../images/836eb50786423bd5.webp)![截屏2026-03-16 15.46.10](../../images/cce6ac3636a9a110.webp)![截屏2026-03-16 15.46.54](../../images/41e38f93c2b46cb2.webp)

**一共检索了6篇文献还找到了只发了预印本的[ RFdiffusion3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)**

### 4.2 执行简单的生信任务

![截屏2026-03-16 15.18.42](../../images/0b5f022ab1737a4d.webp)![截屏2026-03-16 15.16.01](../../images/9d739aa57eba6a7a.webp)![截屏2026-03-16 15.19.47](../../images/9987b0b20a81f13f.webp)![截屏2026-03-16 15.20.03](../../images/18ebafab65774d01.webp)![截屏2026-03-16 15.20.16](../../images/572b043e000bcc82.webp)![截屏2026-03-16 15.21.15](../../images/67505def2c5f036d.png)![截屏2026-03-16 15.21.31](../../images/9ec1c9d7bca1b9b9.webp)![截屏2026-03-16 15.21.45](../../images/11eed528371f2160.png)![截屏2026-03-16 15.23.42](../../images/9ddea0bfb0128b10.webp)

如果你想让openclaw的发送结果到你的邮箱的话可以提供你邮箱的SMTP码，这样就可以直接发送报告或结果到你的邮箱了

![截屏2026-03-16 15.29.27](../../images/5b1603901f3bb275.webp)![截屏2026-03-16 15.31.43](../../images/38c69991234f789c.webp)![截屏2026-03-16 15.31.27](../../images/79271b0a98647881.webp)

在这一步发现基因名用的不是gene symbol，所以又让openclaw重新绘图了一下

![截屏2026-03-16 15.40.12](../../images/b34c212918fe57aa.png)![截屏2026-03-16 15.40.22](../../images/ece445b0d28cfc83.webp)![截屏2026-03-16 15.40.36](../../images/f55308f3bc0d60cc.webp)![截屏2026-03-16 15.40.47](../../images/b6839e7288941631.webp)

下面是openclaw出图和差异分析结果

![未标题-1](../../images/5e87ebc218f924dc.webp)
![图片](../../images/2b97050f06208e7a.webp)

**如何联系我们**

![图片](../../images/fb7650d03b8755cc.webp)
![图片](../../images/bd69821fb60dc828.gif) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](../../images/eff615a0a49ee4ca.webp)![图片](../../images/2d4f3b9289619e36.gif) 您点的每个赞和在看，我都认真当成了喜欢
