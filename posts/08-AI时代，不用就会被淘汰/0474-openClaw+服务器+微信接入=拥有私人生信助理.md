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

**OpenClaw** （曾用名 **Clawdbot、Moltbot** ，因其图标常被昵称为“**龙虾** ”）是一个开源的**自主人工智能代理（AI Agent）框架** 。它由奥地利开发者Peter Steinberger于2025 年底发布，核心定位是“真正能替你做事的 AI（AI that actually does things）”。OpenClaw目前可以**部署在本地电脑/[ 服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535166&idx=2&sn=431238cb95bd4281424130333f6610c3&scene=21#wechat_redirect>)**，接入**企业微信，飞书** 等聊天工具进行控制，调用大模型（OpenAI,KIMI,MiniMax,Gemini等）进行操作电脑，执行任务。本教程将教大家如何把OpenClaw布置在服务器上，并通过企业微信与OpenClaw对话完成GEO数据库中转录组数据的处理(GSE130437)。当然，如果需要的话，也可以联系我们代为布置OpenClaw。![](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmvkGp3Iqy9Ql7KzsiaBG3iaI6IWrTYaictWuKtdItC7BficQAn2Xj0WCRoJaJRlTDIR8P0d4LZHzUbOO2GA0R8yxXow3HwZb3HKcA/640?wx_fmt=png&from=appmsg)![截屏2026-03-13 16.16.13](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnqrDA1FmSjVeQHAqZXcNlp5vNs6PF8PkDZcnpYSEJupjthpjU4NeEpjNBSOOQRtfkBwKTw9QHPXOrMSQ1OUcYasicnfg4D0kMI/640?wx_fmt=png&from=appmsg)

# 二、服务器获取

openclaw的请求权限过高，使用存在风险(误操作、隐私泄露、设备被黑等)，但使用一个环境独立、具有[root权限的云服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532785&idx=2&sn=c364ab8365a845cd709251c026075e0a&scene=21#wechat_redirect>)部署就可以完美的避开这个问题，这里我们[免费提供2周的服务器使用](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528216&idx=2&sn=b7be762860b48931492dad9f4a27017c&scene=21#wechat_redirect>)，足够大家部署使用，大家可以联系客服微信Biomamba_zhushou免费获取。

### 2.1 西柚云账号注册

复制网址(https://biomamba.xiyoucloud.net/)至浏览器，注册账号实名认证。

### 2.2 加购3.0学习版服务器

点击**产品与服务** 下的**订购产品**

![截屏2026-03-16 16.22.09](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnicUjdib3Yx6uaEsAL2cgWMq6g4oibk722th1SxxSZyZB78LpSluTkiaYU4CPSHMEsA2o6PeVt5ibe8Gcu5zLuHvjoviaoKt6sA7cHo/640?wx_fmt=png&from=appmsg)

点击进入生信服务器列表，选择**3.0学习版** 的"点击购买"

![截屏2026-03-16 16.13.43](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmVX727cU5MlZkukNLxibsAVMe5gjIRUZ5bKS5doeiaLOgVkRBDJUhyt1ym0nrsLn0tICFF0g9lIGqOqsXs2p1noeV1KPFeLGVh0/640?wx_fmt=png&from=appmsg)

下拉右侧弹窗，点击加入购物车

![截屏2026-03-16 16.23.31](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwl1iaTqFic9zbEVibNxTPURWalqnBPeLlKdMJyRBokZ5fiaoWxAbG6fR4oBDOLbqSc5BmTgeznTFmBqfx7libmcWxzbzm8bdW4soIBk/640?wx_fmt=png&from=appmsg)

点击**前往购物车**

![截屏2026-03-16 16.24.25](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlPzZyjpia1sUiblelicDInibbmHmqKNOceOVNJdn2ZyrBdiboZlenKxbfIP7TTjhDIrWnvt3fdiconKtqe7L47kVc0bIN4PhCfvmwq4/640?wx_fmt=png&from=appmsg)

###  2.3 输入优惠码

输入并应用优惠码，优惠码联系客服**Biomamba_zhushou** 获取，查看价格是否变成0元。

![截屏2026-03-16 16.28.03](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkk2rfic4DNleV9SLIKGmvqzsJgxs84uoZCv18fs6AUNBPMmZMbn6zGv4jLrd3HndPDbgodNBOPyb9zgfPtsgDWoy1wOujneDxo/640?wx_fmt=png&from=appmsg)

### 2.4 账户激活

联系上一步客服微信Biomamba_zhushou，发送账号/用户ID，我们为您激活服务器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/buxFNhaTGwlxxs2EwjbalTy4G7CnEVlvsNkqHWzLq6ocwk7w6JiaDXz3DibHxHBFgw13jzLJEXQIRSQbFsMHgT0SknUlCZsRRAEib0xHWicZ2wM/640?wx_fmt=jpeg&from=appmsg)

### 2.5 创建实例

#### 2.5.1 进入控制台创建实例

#### 2.5.2 选择西南二区

进入镜像市场，点击**选择镜像并点击使用**

![截屏2026-03-16 16.34.12](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnUibrmBYhHBaRlphVMyz9W8ib9yohUUVoSGghHbg2Hed3tSYTGpCPZguYBe1j6PhxIE7Qs2RTZ5LE0SEsL0Q13nb7hdNgWlQ0bI/640?wx_fmt=png&from=appmsg)

####  2.5.3 创建服务器实例，设置账户和密码，获取IP和端口

#### 注意：这里的**实例用户名** 和**实例密码** 尽量自定义的复杂一些，避免与他人名称可能重复，导致后续影响使用。

![微信图片_2026-03-17_094457_614](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmgKVLzwTShhJibYR3kQXgtk39FwjZgb4zU1fH3ThMmHWf0n9ibTQtvGvnrzicC9qehuCtBGnbX9uGxe6VUGKsScVEYHdYBzmib1aU/640?wx_fmt=png&from=appmsg)

### 2.6 登录服务器

设置好之后，根据自己的账号密码，就可以用ssh正常远程连接啦，详细的登录步骤可以查看我们之前的[如何连接终端和Rstudio-server](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247524106&idx=3&sn=2a708129b846cbd6bd2fade3495afbd0&scene=21#wechat_redirect>)教程

![5](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkAVljCEY7YjjJ4QSd8VRAR24kdjKuibfAJAoH3KrxZzXS4IgA1SqdWgRfSFSwgBgftt59PiaQhnXlsWy7icLf7UeiaqogViaGJRfa0/640?wx_fmt=png&from=appmsg)

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

![截屏2026-03-16 10.02.53](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwliaj7G1pOPHXoIkY8V9qVyD2WhynYIwU0NTQjGQkunXO8fRsTAec6cRBChC9xtpicqn476IBOSdu0zYG7h7UGKXVwzpibGppzjDw/640?wx_fmt=png&from=appmsg)

安装成功后会跳转到以下配置界面

### 3.2 配置环境

以下开始配置软件，进行基础设置

![截屏2026-03-13 12.47.15](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnHHibm01aBYHgQ9tWPaIoTOWVQuuicfAutHgDvfO21icm7BFr4v5431icyfhkWzRVut3DeXE7Gw9JwI52apSHKGoBcYNtVD20IA9Q/640?wx_fmt=png&from=appmsg)

接着根据我们的教程逐步的部署基础设置

![截屏2026-03-16 10.17.59](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwk20H46JrylRvNhxJM7mbfiaeJoCgPiapbETE0878icjKoRv1pkqfOGIibRU9P2QwOwCSRrnSaibG9XfbxbQ7iamAuLDib3lickhosKr68/640?wx_fmt=png&from=appmsg)

我明白这是默认仅供个人使用的，如果要用于共享/多人使用需要进行锁定（安全设置）。是否继续？选择yes

![截屏2026-03-16 10.18.27](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkFyebpTe4ykxjYbxk6seTljNkS0Bib9jVx7LuMBOqErcluaO5Icnrq9U6AE8Km4GPffpyxWmJac0rfQRxhjzO5xTSxno1uG0ibQ/640?wx_fmt=png&from=appmsg)

这是选择后续通过`openclaw configure`配置，还是现在手动配置，选择Manual

![截屏2026-03-16 10.20.29](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnDWhwpfeOQogPYTb26NsRW4UCaOgxtHFWmLvWkeW5Ef444qN0oicqS2ibWmnQF54hksZHl0GqvIMMOQicxut8cFQ1M8lsOicZpyZ8/640?wx_fmt=png&from=appmsg)

询问是否在**当前正在使用的这台电脑** 上直接安装并运行核心网关服务，选择Local getway(this machine)

![截屏2026-03-16 10.24.56](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkic2ftwal2caQga8Oj0q4pnPiaWTMvnaVpLgMYicrkJtSJ2rtibX5Bjiac5hlHzCIsm82agiaGuibHJIyop35Dcs9B0A5tdFMlvGWY9c/640?wx_fmt=png&from=appmsg)

询问安装位置，这里默认即可

![截屏2026-03-16 10.26.55](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmUXZ4FxZ9ODtF9jBoYYW3vZg6mnmbbIuXLqcbuN8QzF083TGff3qZxHEZbsuib01ZyLOW8242bC7HVGRaxHcclvZLZgnS5u1SE/640?wx_fmt=png&from=appmsg)

下面就是选择接入的模型了，上述图，**本教程选择MiniMax**

* * *

在https://pinchbench.com/可以查看各个模型的成功率和花费，综合任务执行成功率和花费，最终选择minimax-2.1,大家可以根据需要选取，考察了一下感觉coding-plan更划算，https://platform.minimaxi.com/subscribe/coding-plan，**一个月29块** ，注册订阅coding-plan

![未标题-6](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlI2gNo0VSHhPEEicm8KtmK7icffbeaJywFibib8hE2vQZfaKKwNlibgOCYptkIuK3cDZvb1coBFKDGaRrYOBXrjD7uxEXf0SBB8sCU/640?wx_fmt=png&from=appmsg)

从表中也可以看到Minimax2.1在基准测试中表现比MiniMax2.5要好

* * *

![截屏2026-03-16 10.49.00](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkia0PA7JibzNaKgnp5taXWt7M0IVPQ5pbh3eZicnibo1lmjeLU8BAEEUVez0uAASBoAicfVaUVseAgJoLXgWJv3JMmxyI02ZP0YdaY/640?wx_fmt=png&from=appmsg)

这里是选择国内还是国外,本次教程是coding plan套餐所以选择CN - Oauth

![截屏2026-03-16 10.49.21](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlA3Q5LIsRSxh5cz6UDcRNq6sYmoIp0mELQxGoOtS04GAbIdnnjKZkCtaDRN7tuAqQibRWgl00hOH1nSMRvGQrRCtISCEb2mNH4/640?wx_fmt=png&from=appmsg)

点击红框内容跳转网页**点击授权** 确认

![截屏2026-03-16 10.50.23](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmmwl5XSMraJ5ESUEo75tID9FXJvP1vFJW48eXicZRy3viacSDrsXNTAMlwxJxLNsgukk7V9SdsAnb7ZyFMCZaTHUa9SXQeaT3vw/640?wx_fmt=png&from=appmsg)

授权成功后

![截屏2026-03-16 10.52.34](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkUgzhf2wFMUibRPDW4eBTBF6icicvOFQ4mLJSOkHBnvibOm8ZsUvl8r3R4Ihbic2Aaubpzib5wfjxLxmr1n1IPjdMYswYU8XLdQLZPI/640?wx_fmt=png&from=appmsg)

选择手动选取模型

![截屏2026-03-16 10.53.05](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkFzkHiagkp0QNFoiavbUJKnguIpMM9fEicQelXbp0rUwyvPNo6NCkBpLoA5Fd0wS0Vy2O6amw9Lgibk9DFWFkfmEvkdn01libROpfs/640?wx_fmt=png&from=appmsg)

在各模型的基准测试中，**2.1结果要优于2.5，所以手动选择2.1**

![截屏2026-03-16 11.00.11](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmgK45Lg4Xy6rI2NPtHUvoIctsWs27Br5NVoaU0s6zEjmtpcZYmpkVPaf3XekkgUvD7UAI6TGcjDq3ibI7ZPoIibDg2kR3AMgv60/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 10.57.26](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmQ2vrtK0JUKKdg0tibd5lF0ljkv4fQySYUdTmljefOKOUNfMFl58j1ibccs0W7RTNJPl1f9PRCM7lf3zrqLsciaHb2nT3oAE1Mv0/640?wx_fmt=png&from=appmsg)

接着是网关端口配置，我们西柚云给大家预留了三个端口可以自行分配，大家选择其中一个就可以

![截屏2026-03-16 11.01.21](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlw5CD9PR0YfWngaoxdxGTJrEJV3fmbwHKBlM0VBcTUKx7QSmiamqv6rQaxsGXfcoKCRM6azibv67wYVNk5nyKtLPMuEEbrWND2U/640?wx_fmt=png&from=appmsg)

设置 **Gateway（网关）绑定地址** 的选项，本质上是在决定：**这个服务要对哪些网络开放访问** 。这里选择第三个Auto就可以

![截屏2026-03-16 11.04.25](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmicH2qYBOBZGbicUibmAmteWROwktTnsgwic8icfGDfjK1yb1Cic04rg78esoGKgJRCEC4BBtHtBmQlZKYxyKTyXzTpZFVyFX8WKLVs/640?wx_fmt=png&from=appmsg)

配置 **OpenClaw** 网关（Gateway）时，系统让你选择**安全认证（登录）方式** ，选择Token

![截屏2026-03-16 11.06.54](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlBxgibPZuzyMlb1dEgotIgSkNZs2iaclzHEzh4584VkAGUpy4U5onBZ9icnLib5oYqWMWj2WDeibnibmbcaLb9t2ZFWbxMlcY8NbBlA/640?wx_fmt=png&from=appmsg)

通过 **Tailscale** 来配置你的网关网络访问权限,选择serve

![截屏2026-03-16 11.08.02](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkwzOc8P4cduuNibIpzlahM5w6qS0wmaNoIQppBy3xeT5Ex3DjxpYQEicsUTLx0NOdnZqmpXS5vVNaCV8GV68Q6DdyeFsHGHsH8Q/640?wx_fmt=png&from=appmsg)

选择yes

![截屏2026-03-16 11.08.39](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwm3iawTx3qHiaBpZdFSUQMclSdNFRnkRAicWZSJ8Nr9Mib4Uuysahic5ZZN7wELX9HryCthpXPt3sGpHl6cV1K5A04vW5lLSjlVgqFk/640?wx_fmt=png&from=appmsg)

选择default

![截屏2026-03-16 11.09.47](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwk7qphXYhd40SbsYvemNke1YWzjXUmNImFy5Jf6DlEajichWJUtphpyDpB7usZE8f8Tse8l2NSSrCbD1H66jaVtxk2RPOHc1png/640?wx_fmt=png&from=appmsg)

直接留空自动生成

![截屏2026-03-16 11.10.32](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnA7ajRiauvxUF2RKp4mF9OQqhgUJmvpHQtZzZXVCic7DiceicA2LG2n9mCLJ4ZONpgqSEHmEKy1H4gv6cjYsxbvQwzXnedYHibIqyg/640?wx_fmt=png&from=appmsg)

这里配置企业微信接入信息，选择yes

![截屏2026-03-16 11.11.34](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwl94egIVBEMEjVvMlVlIViapPyicj6Rvm5P2eDtwGUdgxBG21LcAkIS7EvbLb8QzJDGKKwX0mYEv6V1v2XPkcx1qR2vmx1roHIzY/640?wx_fmt=png&from=appmsg)

默认没有企业微信，先跳过

![截屏2026-03-16 11.12.17](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnwWibJiccOwbecLZAHbBYlbiaCY1HXFJvsUdw7CTWjW8Jr2wOgtALl6BCEolffOliaWibOzYaN1eK8kvBLOzHQoce9HqmaGEcRfnPg/640?wx_fmt=png&from=appmsg)

这里要给模型设置网页搜索功能，先跳过

![截屏2026-03-16 11.13.02](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmywA8OXUYAlseJzWEVz2ugeN2vT5tIPLu3AbG6mvDhfSXQWEy2RkbkKFkdNQrKQ1o0rlrDBQ6rPresPvFZzEicpJpicgVhyAIB8/640?wx_fmt=png&from=appmsg)![截屏2026-03-13 14.01.49](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwldq5KJvYacVkwOJM8znjWwGM3oBFXwnCFIHy2HeZPSPzKicJwIXRwZo8QK9GicQ8VIoYLd24JX80JdMBicC2S8vnISPGDxlCkhBw/640?wx_fmt=png&from=appmsg)

配置一些ai工具的api，都选择no，都是非必要选项

![截屏2026-03-16 11.16.52](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnehzicEMArdNNTQAdpKNeOJKYI2MTFl6XYmEuUlxoDjv8lRNFBQWtESqxccjRdmFa1qJqktudIQ4q87atib3vJ6TzKRYCre409E/640?wx_fmt=png&from=appmsg)

选择"Hooks",相当于“龙虾的记忆”，`session-memory`含义为当你在终端输入 `/new`（开启新对话）或 `/reset`（重置当前对话）时，Hook 会自动提取上一轮对话中的**核心结论和关键信息** ，存入 Agent 的长期记忆库中。

![截屏2026-03-16 11.20.05](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnIYT8ptrRbibOiaGic78lpoF49mlLD8kiaMYRibYjONyMe4G6s1nByicwgTIic7gsauBiamHQiafIQ5iciaQtYia68Y3bS7uvUILlsOK37S1s/640?wx_fmt=png&from=appmsg)

是否安装网关服务，yes，Node

![截屏2026-03-16 11.21.33](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwn2p7FD4AQtA4RicqxeD3M20ZTPCkak66nDyHiajfPkPuGee5JKtldicaW7xEnUMC3RjHiaWUzsxLOyoHlMuLJJpD10JQRH1lZS9dA/640?wx_fmt=png&from=appmsg)

选择Do this later

![截屏2026-03-16 11.21.55](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmUso3hP4Oq7JF1RNt4v3z4eyH12XFNwTzpFHS7rRCZJ1UYItZWeb8nBLvSGHlmCTyAE4icavibCwXE3ZdOuTjN8aD6NMhYW7mSo/640?wx_fmt=png&from=appmsg)

yes

选择完之后，基础配置就结束了

### 3.3 接入企业微信

首先下载企业微信客户端，登录后点击工作台

![截屏2026-03-16 11.25.42](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlQkznJDqc7muG4qcUREicNgM791Efh3zdezKvtQxYJJAH26BtPLRricWrja12Pxbrj8KKyougfwtq0PBEAa3nYvDSUREg14O7yw/640?wx_fmt=png&from=appmsg)

点击智能机器人

![截屏2026-03-16 11.27.14](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmgAic1laWTwkMollE93icQiaxp4PKNE4QwRC0ib3fTqVsI8b9UcBick6RsjoMa2I4giaLJIUF44KtzWlWlA4SNbosPicI6xN0t3s96zg/640?wx_fmt=png&from=appmsg)

点击创建机器人，点击**手动创建**

![截屏2026-03-16 11.28.42](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmwkz03QYp3fFcySdjkY17R3oHGzOfKicsDgHAqH7T9oWZW14fgAKzkWiamiadZ11EFgoCnnGcfBe7icdVfwFnlv8DNrrjG40ovfK0/640?wx_fmt=png&from=appmsg)

拖到最下方选择**API模式创建**

![截屏2026-03-16 11.31.11](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwnWiaGk69aOd1PUKbYKwRhkMMM4Q3R5DEUAgnyHDpemFSRxNYiaMxfqMLTPO4CvNHjIRJ5MR01ickjicn4VibAG5ygHEsyXCghQ85Gc/640?wx_fmt=png&from=appmsg)

按照如上点击设置，获取**bot id** 和**secret** ，拖到到最后点击保存

**接着在linux上配置企业微信插件**
```
#添加环境变量echo'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrcsource ~/.bashrc
#安装企业微信插件npx -y @wecom/wecom-openclaw-cli install
```

![截屏2026-03-16 11.51.30](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkuJpREkEzMjbH3Ij5H9iazO99CVSyYxvibNX0jDjRPH6pmPdKKyaFhicWM78X1qsbjfedAtGQl6RbtFtExibExR6ujzqXfV1bw0M4/640?wx_fmt=png&from=appmsg)

选择手动输入

![截屏2026-03-16 11.52.43](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwl4TF65tqkYVPXCkdwsm5cAUuMLBELVRfle0gKrkhycA5C18stRiaCkB9m61PtqKct98mB5n8ibAdB5GZgsXJRtgRia5CfPJP7eIg/640?wx_fmt=png&from=appmsg)

输入在企业微信中的**bot id** 和**secret**
```
#我们手动拉起一下，这样可以想停就停openclaw gateway stopopenclaw gateway --port20389
```

![截屏2026-03-13 14.04.50](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnSMpUutEDlpGyo2ianoibicgaMSedb3fn4aBzZHHrl3jF36cd0ELj1dJVGRqJPlUypoXia84SsXemz9koSxWXlibjzsWWtEEriaodrs/640?wx_fmt=png&from=appmsg)

这样就可以在企业微信里回消息了

![截屏2026-03-16 12.33.19](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlL1WSeSw5DMJmKpb6CW3xz9yRFWVXHn7Z4A6yx89LWGrlF3BEs9vQTfno0V5EUOFXQicVPleibYb7ibw9Kodps3Ijb5icE0XOw7wM/640?wx_fmt=png&from=appmsg)

### 3.4 安装skills

OpenClaw的**Skills是赋予AI智能体执行实际任务能力的扩展插件** ，使其从单纯的聊天机器人进化为强大的自动化助理。而腾讯的**SkillHub** 则是专为国内优化的本土化技能商店，它不仅提供**高速镜像下载解决网络瓶颈** ，还进行了全中文适配与安全审计，并深度接入了腾讯生态，降低了skills的安装门槛。
```
#大家可以上网站上找一下适合自己的插件https://skillhub.tencent.com/#featured
#安装skillhubcurl-fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash  -s----no-skillscurl-fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
#配置环境变量echo'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrcsource ~/.bashrcskillhub install tavily-search
#注意安装路径，后续还要用到
```

接着我们需要获取tavily的api，在官网上注册登录后就可以进行免费获取，每个月有**1000次的免费额度**

![截屏2026-03-16 12.50.47](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwllzvGN4XncicNlSgcMPKWz0MHKup92wqSbwuEYdAodCAAA0ic1XOtZm2oaIibPtZsBfIWkUicJ2LZKYicicmEuTBNv0tAJOIocWSZsg/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 12.51.04](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwncOXa8cGICZFBibudPv4wt6r3PsOwrKnzxZmkic4uAYTTjVgrIeJm8HZ8ObL0609Iqvw090XsaX9BHBxmcKFTWSbyalSmib6Picps/640?wx_fmt=png&from=appmsg)

将api-key写入`~/.openclaw/.env`
```
TAVILY_API_KEY=...
```

重启一下openclaw，将安装skills的位置告诉openclaw启用，这里我还安装了其他的skills。

![截屏2026-03-16 13.05.55](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlJRJSpPhbHCDhMmjP9ViaTT5zx8k2OUX4LKXepLg1xDxggMxtjY8AiboeklyeauC3fevFX1EJh92q2N7udCQyIcVA8pXfePpg44/640?wx_fmt=png&from=appmsg)

调用一下试一试

![截屏2026-03-16 13.09.48](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkUoWLsO0UviauCyoS9YM9N2ibPa6ANZLLv96lVys91fPjRoYoE2S0hRibuiauDzYc8y4d7KCgiabJxNOGiaTOibvKNDYSykBqzafxVWw/640?wx_fmt=png&from=appmsg)

可以在tavily官网看一下，可以看到已经在使用

![截屏2026-03-16 13.07.04](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwl9lSPf75rjicKxbSRCARjEuUCo2gsk8vRiazeVpicvlMS6Qa6C3Cb7vljYibjbicEkudpaZkkMFiakNmXGfSDhkYsEAIgt2ZpWuNqzM/640?wx_fmt=png&from=appmsg)

# 四、使用案例

### 4.1 检索文献

![截屏2026-03-16 15.45.34](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkvTUPE3C9ZlYv7D14w0Jvc0XMgA0WgT3xFvHY7IIAVApYwkicxcutHC8VREtcpOjSJlHSiaic4d4Ut8gyu5x5pAQ2ctK5pvr7gE4/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.45.52](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwn7eZbWemBmhUFmZGlg546rcgnaFKBIXnv86DUhFFWhQ7Fic3vJ8aibXIxt82Faq3BgJ5zAyDE725YPQibqnxpwJ2ianVGXjsfRKc0/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.46.10](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkibPGWJliap91HlpkAZyIgPHfTh2wJAPKmc2ZlcCxTbep7NmcTEsv2GdOmfreAia2wsFBV6VddgqnefdSwd8SOkpiaNu4gbPE1AJ0/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.46.54](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkzQvlvkNygGicfvIQuBZMcCtT73kRCECvFzDRtPn0VM0vFYyVph18cFyaLrTPXLPSBZ6JScIia9OK54CqLtMMnf5Cr7eJaxkqzE/640?wx_fmt=png&from=appmsg)

**一共检索了6篇文献还找到了只发了预印本的[ RFdiffusion3](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535726&idx=1&sn=fa3a01ca6ec0f20d0e9b7ac960712ac3&scene=21#wechat_redirect>)**

### 4.2 执行简单的生信任务

![截屏2026-03-16 15.18.42](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwlwBMnQJKkKkc0MOce4Ha5iaMPBmmhmniac9BmBrVQaNrQ0ADgzd1NFOmjnJC9RdD3TG8W71hSdbYarfE5cHvxNkKnOANwZicDqhU/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.16.01](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkSUpic66jeuuMsCE3Enl18REKZ3XYNPSWsvwG9347kiaTICIgAwYfo1UjKNEoAUrUFEl0ccicGzCX49ssVybaMicwDibXvgIAKL8ps/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.19.47](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkdLy9k1LDgEPj1xsibNz9aoV2KwJjU6VW7uicy423YRFohMAG3IFiaGW2TywgneDqOg0ZqNuQgauTB4s4O1ACTMZTZV57rIIDPHg/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.20.03](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkbK6jhjyoB3qmmj2BPpvyFcacNcl151BzDDJCRfRCNKj1IbFcbfT5QBQAgIdicAyic48gIicqpiaKQlCbKGvwn4S2NWt0BSkzEhws/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.20.16](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkrAkbqAqGAYzgh5dcxIkpJpLaAic4F1RibD2ydAp1PaSscXju8hXwIhvE1mkA22VDQNicNXbAuBvDu7SDKiaREs5DibW9meOg1Un4I/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.21.15](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmtwVYMcH3CEedBkW0EU2CWRmZS2nO4L1QJfGLVVSzXDeWsEadupQUVJLibVFntey2cic0ic7A7lnrF8IomVqLn0z377LqBDe6NicI/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.21.31](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmyZ0SDoHrMk4MxpCwsj1ibe9BhRXhH3ReJ4aBp97b6oqxDgpQqwPup8xyiczSZNQKXKUdJgcFoP2LhibiaoaJ7ahzQibfeSXgLlWXg/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.21.45](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwk7kghnNq4MPsZQd3VGxyVIjDfoPKnYyiafYGfXNEOpxAwxpUlglbdYsPt6jtztjwMQqTverY2ibpDTdOfepgeFXf0lwcVjcGyTs/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.23.42](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkXtRalYDlyKZAX6z8D0rUehQLibFdxics1OzzYPqiboPThcZ6ykJljicVQdvBLSDWCpXbUPnyoYWj9z5VMhFYgUiatgNLuKwHs7VrQ/640?wx_fmt=png&from=appmsg)

如果你想让openclaw的发送结果到你的邮箱的话可以提供你邮箱的SMTP码，这样就可以直接发送报告或结果到你的邮箱了

![截屏2026-03-16 15.29.27](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmYdtLKQUkwYlaPAOBwu3GloCHDfdXbceKHsfIrj8VEATR2rwibhZ81icKicT6V56FZ05uw31h01kttuQSic1wkRrpLd86KoP0svC0/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.31.43](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwkqUFOHBRnZr63tibPcgDIpwribBwWibwfjHHNsDTF18cbibw3LrO0ZKXnEDTR55VOqJe77icwewNoQicCroAksbJlpNgtQJqEIWeAec/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.31.27](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwncb4KpqoJiawT1jMpN05HfkE8XDdceM5R7LKTBMVXHKR4ibSS3GzxIGeVnKYVyCns3qic8ae9tIXLnJzaQgg6MRC33YFOo45LU7s/640?wx_fmt=png&from=appmsg)

在这一步发现基因名用的不是gene symbol，所以又让openclaw重新绘图了一下

![截屏2026-03-16 15.40.12](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwkJicf1XJodTYnLkwTbke9TicgURmnZQzWKSQo8zKpicRqJns7WgC4L5p1759KNcGJHa0omC4Q2gfP9syxPibxpoTklviaeknfib3Kbk/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.40.22](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwlb5L47fpjCRUwwqicMCNiatIQKvheNnM1LE9gtkIsupAAVOmeAXwSp4AJch4HeCOkf5XKA9MltTXEHoMVicic9WSb0DqohQmOydc8/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.40.36](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwnnPFJFW5ib2tiaasun0viatkvyGygP2wP5TUTicBneSoDbtQ3nibc1vJ9fEx0icqdJJIphnGqR42wtFq7ibqxcEDoGqq4C9M7aTFic1S4/640?wx_fmt=png&from=appmsg)![截屏2026-03-16 15.40.47](https://mmbiz.qpic.cn/sz_mmbiz_png/buxFNhaTGwmUDibsNz8DM9QQlwzxlZb3ajZzWnjRkoIfSrwunR852jQQ8QSrmo19hibaNfA6IlE2uC5jBPLtE0keEaqH0y6dNRpHfYsibS7TYQ/640?wx_fmt=png&from=appmsg)

下面是openclaw出图和差异分析结果

![未标题-1](https://mmbiz.qpic.cn/mmbiz_png/buxFNhaTGwmmQ6LcdWaibdlrgd5uR5hEsouLZdpprT9TDQEDTlIQzMZ04pe2nn2pKUVGeC7RLEdGNIZKwL73pfFb7XJPb7KK2pDwovWP2O70/640?wx_fmt=png&from=appmsg)
![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5O8mjlC4kPOluxibs4oDot7AXe0RgoXgMeiaB3KYViadIQqXRoRicyian7KUg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=6yqn0s1k&tp=webp#imgIndex=20)

**如何联系我们**

![图片](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaFyWDMZJ2713X3DwiaQicG5OSxqKNRib39TuLic5NT2iaJaI0mIicuvjMZlRPvlqPfgjzg001qlRJTBDRA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=5w77y1os&tp=webp#imgIndex=21)
![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWiaC0oer2QpXIolHVU3Xibtm9BNWiav660mHaB5qEd1dibMibUicNYmAzBBiadQP2s7HArdUxoWL5cDkTEbQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=5ixl8h41&#imgIndex=10) 留一个领取[资料](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247535983&idx=1&sn=99378a252908b06f56432eb08741d278&scene=21#wechat_redirect>)、[开箱即用的单细胞分析镜像](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528410&idx=2&sn=0f2bac25479cf8d20dab5d82ae986f2e&scene=21#wechat_redirect>)的**微信号[Biomamba_zhushou]**，方便各位随时交流。同时我们也构建了[交流群矩阵](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247528057&idx=1&sn=bb348c2a88c977c7cce67ee6731a3591&scene=21#wechat_redirect>)，欢迎大家入群讨论。

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[没有检索，就没有发言权](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529398&idx=2&sn=5a429852d61721916a405712677d5905&scene=21#wechat_redirect>)

**已有生信基地联系方式的同学****无需重复添加**

![](https://mmbiz.qpic.cn/mmbiz_jpg/ImlBFVOwwpyQnz4vf7GibVdoavE7dBqK3fMn0I2ONlp8LNpd3Pp9sGmfg4SegHNqkP7ZwUKwWP9licLaB3RiabA0Q/640?wx_fmt=jpeg&from=appmsg)![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhFTIP7DCMLPwWh8Yhjs079f1vMqlYdExqbWaZVJyiawKkr21EDSNW740b4yMzkeHxFJULTpZGzYwQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=3hy3u99m&#imgIndex=12) 您点的每个赞和在看，我都认真当成了喜欢
