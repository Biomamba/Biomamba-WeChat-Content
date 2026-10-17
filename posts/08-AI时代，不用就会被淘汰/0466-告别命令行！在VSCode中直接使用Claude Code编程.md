---
title: "告别命令行！在VSCode中直接使用Claude Code编程"
date: 2026-07-06
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539068&idx=2&sn=9ec591f5e91c5e13fe6024f7e99dab29&chksm=9b3c202cac4ba93a30cf1649b305e1b2cc8993cbab43b43857322e39ab88b2d4f33c738c5137#rd
albums: ["AI时代，不用就会被淘汰"]
---

# 告别命令行！在VSCode中直接使用Claude Code编程

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539068&idx=2&sn=9ec591f5e91c5e13fe6024f7e99dab29&chksm=9b3c202cac4ba93a30cf1649b305e1b2cc8993cbab43b43857322e39ab88b2d4f33c738c5137#rd
> 合集：AI时代，不用就会被淘汰

# 前言

在前面的教程里，我们学习了如何在VSCode中通过Codex插件实现AI辅助编程，覆盖本地与远程两种使用场景：[OpenAI编程助手插件，把Codex装进VSCode！](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536883&idx=1&sn=8fbf4b133e87049cdab88571807027ea&scene=21#wechat_redirect>)，也介绍了命令行中使用ClaudeCode：[ClaudeCode基本使用教程](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539059&idx=2&sn=89b483b2951982383f60daf49c1accf3&scene=21#wechat_redirect>)和[skill使用方法](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247539062&idx=2&sn=6fd50e106bf2ebd5fb517a35676097a4&scene=21#wechat_redirect>)。如果不想使用命令行工具，我们还可以在IDE中通过插件来使用ClaudeCode。今天这篇文章向大家介绍在VSCode中通过Claude Code插件使用AI辅助编程（涵盖本地与远程两种场景），一起来学习一下吧~。如果需要Claude Code在[服务器](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247537798&idx=1&sn=558542e091ec6a4d6a8a963efa4e1f65&scene=21#wechat_redirect>)中代为部署，也欢迎联系后台。

另外需要可接入[小龙虾](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247536263&idx=1&sn=18bdb5f3158358be29563575566cbffa&scene=21#wechat_redirect>)和其它AI的服务器？可参考：访问链接：https://biomamba.xiyoucloud.net/

[足够支持你完成硕博生涯的生信环境](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247511780&idx=1&sn=3acc0874f7d2fa75f1abbe7a9a9b4069&chksm=9b3cd7b4ac4b5ea27d4d53964e4a4a9fa8c806a19103729dd4ff0fa72e621411f46a251d269f&scene=21&token=1904068475&lang=zh_CN#wechat_redirect>)

[忘记宣传了，独享用户连技术支持都是独享的](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529475&idx=1&sn=10827e982a637e0fc36e4b6e857736c8&scene=21&token=1904068475&lang=zh_CN&poc_token=HF-eN2mj01zsfxe_I4r8D5pfZx80xO2AVYSB6qtT#wechat_redirect>)

[RTX5090、4080S、5070显卡上机](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21#wechat_redirect>)

# 本地使用

## 安装Claude Code插件

  1. 打开VSCode，本地安装Claude Code插件（认准anthropic）

![](../../images/bc32326eb5c8705f.webp)

  2. 安装完成后，右侧活动栏会出现Claude图标

![](../../images/dd3b220cf862a9ee.webp)

  * 此时点击图标会出现下图界面，由于还未进行环境配置，无法正常使用，我们需要进行下面的环境配置

![](../../images/27ba8b59218a6742.webp)

## 配置环境

  1. 新建settings.json文件

Windows用户可以在C:\Users\你的用户名\\.claude\目录新建settings.json文件，也可以在项目目录下新建.claude\settings.json文件，新建settings.json文件后，填入下面的内容
```
{  "env": {    "ANTHROPIC_AUTH_TOKEN": "sk-xxx 你的令牌",    "ANTHROPIC_BASE_URL": "https://api.0daysci.com"  }}
```

在用户目录下创建

![](../../images/27fabd8f17f2e827.png)

在项目目录下创建

![](../../images/5027c9d7b99baa98.webp)

  2. 保存之后重启VSCode，即可调用成功

![](../../images/642b9243b8868f02.webp)

# 服务器使用

## 使用VSCode连接远程服务器

先按照教程通过VSCode连接服务器：https://blog.csdn.net/zhaxun/article/details/120568402

## 安装Claude Code插件

  1. 在VSCode左侧扩展图标搜索Claude Code并安装，认准anthropic。

![](../../images/05f4f00e9c928cf4.webp)

  * 此安装是在远程主机上安装，安装完成之后会显示已在远程主机启用扩展，且左侧扩展界面会显示远程主机已经安装的插件

![](../../images/ce587835347dc2bf.webp)

  2. 安装完成后，右侧活动栏出现Claude图标

![](../../images/c744ad19b9cb9cec.webp)

  * 点击图标会出现下图界面，由于还未进行环境配置，无法正常使用，服务器使用具体如何配置，请继续往下看

![](../../images/03c009a05f37cecb.webp)

## 配置环境

  * 在远程服务器创建配置文件

```
# 在远程服务器执行mkdir -p ~/.claudevim ~/.claude/settings.json
```

  * 填入如下信息，把令牌替换成你自己的API Key，令牌获取参考本篇后面的内容

```
{  "env": {    "ANTHROPIC_AUTH_TOKEN": "sk-xxx 你的令牌",    "ANTHROPIC_BASE_URL": "https://api.0daysci.com"  }}
```

  * 保存后重启VSCode，使配置生效。

# 使用测试

  * 点击右侧Claude图标→对话框出现

![](../../images/f23b934bef183547.webp)

  * 直接描述任务，例如："请生成一个R脚本，使用DESeq2对一个假想的表达矩阵进行标准化，并输出前10个最差异表达的基因"，生成之后点击Yes可保存该脚本

![](../../images/879600e330ab9fed.webp)

  * 根据提示运行脚本，能够运行成功

![](../../images/442e86f554126d77.webp)

  * 生成的文件也可以正常打开查看（如果有提示需要安装插件，根据提示安装即可）

![](../../images/302dcf85fd44ffdb.webp)![](../../images/a93dcbe25dde7d50.webp)

# 怎么购买Token

## 注册/登录账号

访问链接：https://biomamba.xiyoucloud.net/

## 打开西柚云AI服务平台

![](../../images/44d84f1639bc96ee.webp)

## 充值

  1. 点击右上角个人中心，点击钱包管理。

![](../../images/c51a227ee66f2b14.webp)

  2. 点击跳转购买对应的商品，购买后系统将自动充值Token。

  * 免费体验版：5百万Token。
  * 正式版：1千万Token/18元。

![](../../images/e0f8f4c489f82e37.webp)

## 令牌管理

  1. 进入令牌管理

![](../../images/cdbb0c935e212cc2.webp)

  2. 创建令牌

  * 名称：填便于自己识别的名称
  * 令牌分组：选择默认分组

![](../../images/e89cd196c86f7c85.webp)

  3. 复制令牌配置到对应的配置文件

![](../../images/abdc13537c63547b.webp)

# 西柚云在售算力

我们长期提供GPU、CPU算力，欢迎大家联系后台。访问链接：https://biomamba.xiyoucloud.net/[![](../../images/6e693f923fe6589b.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247532373&idx=2&sn=4708fac31ac8f4e347847e4b7f2a4fed&scene=21&poc_token=HD30QWqjyfz9w8kaP4lTzV2TrwmmFWeikVE7vHza#wechat_redirect>)[![](../../images/7639767d80b412ae.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247534707&idx=2&sn=2844377758ce00e07435a5dd376b4715&scene=21#wechat_redirect>)[![](../../images/18e6a4a68f9e0cb6.webp)](<https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247529840&idx=1&sn=704b0a3d60a17c5bc2445d54c97b834f&scene=21&poc_token=HGz0QWqjtxRcZEO9_FZ7U2waArXDSPexP98oXbem#wechat_redirect>)
