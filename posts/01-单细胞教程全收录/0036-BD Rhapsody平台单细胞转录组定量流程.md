---
title: "BD Rhapsody平台单细胞转录组定量流程"
date: 2023-12-23
source: https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506542&idx=1&sn=99cf7af7fc0d56b0d6fe7ea3596df2b6&chksm=9b3ca33eac4b2a28e6682a7cf0b2091a387a06ecf89ee10737cf2194286ec0bba472ef1c2b90#rd
albums: ["单细胞教程全收录"]
---

# BD Rhapsody平台单细胞转录组定量流程

> 原文：https://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506542&idx=1&sn=99cf7af7fc0d56b0d6fe7ea3596df2b6&chksm=9b3ca33eac4b2a28e6682a7cf0b2091a387a06ecf89ee10737cf2194286ec0bba472ef1c2b90#rd
> 合集：单细胞教程全收录

前段时间粉丝求助BD Rhapsody的fastq文件定量流程，想来我们之前出过10X的[Cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501751&idx=2&sn=a79512f54db7456ea577de40f1a2d286&chksm=9b3cbee7ac4b37f1ce313d5eeb9a9ac9940640ab599ac5ab5d438fa86a8007796b768e4e68c2&scene=21#wechat_redirect>)、Drop-Seq的[dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247501812&idx=2&sn=7feb4d89ebc45ca7d64ad2dd5cd3c832&chksm=9b3cbea4ac4b37b2d2609172d58251076a6ab6a7043600613f0fb2ae0bea427de542b4dcf91e&scene=21#wechat_redirect>)，BD Rhapsody确实没有涉猎。遂探究了一番官方的pipeline[1]，非常折磨，软件安装与流程搭建需要花费一番功夫(如果各位做定量有困难也可以联系文末微信)。当然，如果你具有一定的Linux基础([十小时学会Linux](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505777&idx=1&sn=f3efae390566b838a445ab9f832323c8&chksm=9b3cae21ac4b2737f5923b246470d699474c041bb78de50d2b71b99d537f9f44ca2938002cda&scene=21#wechat_redirect>))，可以自行开展后续的学习。

一、安装并配置docker[2]

以我的Ubuntu为例，安装docker需要拥有root权限([有root权限的共享服务器](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))。

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
# 更新apt库： sudo apt-get update# 安装依赖 sudo apt-get install ca-certificates curl gnupg
# 添加GPG key sudo install -m 0755 -d /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg sudo chmod a+r /etc/apt/keyrings/docker.gpg

# 设置docker仓库： echo \  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# 安装Docker Enginesudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# 测试Docker Engine是否可以成功运行：sudo docker run hello-world
```

大陆的小伙伴大概率在使用docker时会失败，由于长城的问题可能会timeout：

![](../../images/4cb6d76e3b28ff72.webp)

这时就需要借助一下阿里的官方镜像加速链接[3]，注册后在个人实例→镜像仓库→镜像加速器中申请获取加速器地址，完成如下配置(vim教程可见：[Linux| 25. 文件编辑器 vim](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247500900&idx=1&sn=f8e41737d22588beaeb6cfeea8865a7d&chksm=9b3cbd34ac4b3422ded73466e862117a5b4989eb0ca2125f2c1f45b67f9ca3772d40a1bb6835&scene=21#wechat_redirect>))：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
vim /etc/docker/daemon.json
# 写入如下内容：{                 "registry-mirrors": ["你的加速器地址"]}# 保存并退出
# 添加docker组，如已添加可忽略：sudo groupadd docker# 将当前用户添加至用户组sudo usermod -aG docker $USER
# 重启dockersudo systemctl restart docker# 这时docker就可以随时待命了
```

二、安装cwl-tools

首先需要安装conda

  *   *   *   *

```
1、安装conda：wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.shbash Anaconda3-5.3.1-Linux-x86_64.sh #安装conda，出现选项选yes
```

安装过程一直敲回车、遇到询问均填写yes后敲击回车即可，安装时间需要花费5~10分钟，如果选择安装 Microsoft VSCode部分，会额外花费一部分时间。

![](../../images/4759aca6ad90f8f6.webp)

  *   *

```
 source ~/.bashrc#重启一下环境配置，否则无法直接定位到conda which conda#返回完整路径即为安装成功
```

![](../../images/6368a3aeae73b4d3.webp)

  *   *   *   *   *   *   *   *   *   *

```
#添加一些镜像conda  config --add channels defaultsconda  config --add channels conda-forgeconda  config --add channels bioconda#增加bioconda，方便安装生信软件
#最近阿里的镜像似乎比较稳定：conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/conda-forge/conda config --add channels https://mirrors.aliyun.com/anaconda/cloud/bioconda/
```

安装cwlref-runner

  *   *   *   *   *   *   *   *   *   *   *   *

```bash
conda create -name BD_Rhapsody
conda activate BD_Rhapsody# 安装对应版本的pythonconda install python==3.11.3

pip install cwlref-runnersudo apt install nodejs
# check which cwl-runner
```

在这个页面下载yml与cwl文件：

https://bitbucket.org/CRSwDev/cwl/src/master/v1.9.1/

![](../../images/7e5dfbb528a45488.webp)

无法访问的同学可以从我的百度云盘里下载，链接无提取码、不会失效，若无法打开请更换浏览器尝试：

https://pan.baidu.com/s/17NpUin4N0UgcxW7LhCVegQ?pwd=et22

![](../../images/7dcf5e8758148692.jpg)

yml文件中的收录内容为(有#号的代码不用管，直接修改参考基因组路径与fastq文件路径即可使用)：

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *

```
#!/usr/bin/env cwl-runner
cwl:tool: rhapsody
# This is a template YML file used to specify the inputs for a BD Genomics WTA Rhapsody Analysis pipeline run. See the# BD Genomics Analysis Setup User Guide (Doc ID: 47383) for more details. Enter the following information:

## Reads (required) - Path to your read files in the FASTQ.GZ format. You may specify as many R1/R2 read pairs as you want.Reads:
 - class: File   location: "改成你的_R1.fastq文件"
 - class: File   location: "改成你的_R2.fastq文件"

## Reference_Genome (required) - Path to STAR index for tar.gz format. See Doc ID: 47383 for instructions to obtain pre-built STAR index file.Reference_Genome:   class: File   location: "参考基因组位置/GRCm38-PhiX-gencodevM19-20181206.tar.gz"
## Transcriptome_Annotation (required) - Path to GTF annotation fileTranscriptome_Annotation:   class: File   location: "参考基因组位置gencode.vM31.primary_assembly.annotation-filtered.gtf"
## AbSeq_Reference (optional) - Path to the AbSeq reference file in FASTA format.  Only needed if BD AbSeq Ab-Oligos are used.#AbSeq_Reference:# - class: File#   location: "test/AbSeq_reference.fasta"
###################################### Putative Cell Calling Settings ######################################
## Exact cell count - Set a specific number (>=1) of cells as putative, based on those with the highest error-corrected read count#Exact_Cell_Count: 10000
## Disable Refined Putative Cell Calling - Determine putative cells using only the basic algorithm (minimum second derivative along the cumulative reads curve).  The refined algorithm attempts to remove false positives and recover false negatives, but may not be ideal for certain complex mixtures of cell types.  Does not apply if Exact Cell Count is set.## values can be true or false.#Basic_Algo_Only: true
########################## Subsample Settings ##########################
## Subsample (optional) - A number >1 or fraction (0 < n < 1) to indicate the number or percentage of reads to subsample.#Subsample: 0.01
## Subsample seed (optional) - A seed for replicating a previous subsampled run.#Subsample_seed: 3445
######################### Multiplex options #########################
## Sample Tags Version (optional) - Specify if multiplexed run: human, hs, mouse or mm#Sample_Tags_Version: human
## Subsample Sample Tags (optional) -  A number >1 or fraction (0 < n < 1) to indicate the number or percentage of reads to subsample.#Subsample_Tags: 0.05
## Tag_Names (optional) - Specify the tag number followed by '-' and the desired sample name to appear in Sample_Tag_Metrics.csv# Do not use the special characters: &, (), [], {},  <>, ?, |#Tag_Names: [4-mySample, 9-myOtherSample, 6-alsoThisSample]
```

三、下载参考基因组

下载参考基因组与GTF注释文件：

  *   *   *   *   *   *   *   *   *   *

```
# 小鼠GRCm38参考基因组下载：wget https://bd-rhapsody-public.s3.amazonaws.com/Rhapsody-WTA/Pipeline-version1.x_WTA_references/GRCm38-PhiX-gencodevM19/GRCm38-PhiX-gencodevM19-20181206.tar.gz# 小鼠GRCm38GTF下载https://bd-rhapsody-public.s3.amazonaws.com/Rhapsody-WTA/Pipeline-version1.x_WTA_references/GRCm38-PhiX-gencodevM19/gencodevM19-20181206.gtf

# 人类hg19参考基因组下载：wget https://bd-rhapsody-public.s3.amazonaws.com/Rhapsody-WTA/Pipeline-version1.x_WTA_references/hg19/hg19-gencode.tar.gz# 人类hg19 GTF：https://bd-rhapsody-public.s3.amazonaws.com/Rhapsody-WTA/Pipeline-version1.x_WTA_references/hg19/hg19-gencode.gtf
```

也可以直接在这个页面中点击下载：http://bd-rhapsody-public.s3-website-us-east-1.amazonaws.com/Rhapsody-WTA/Pipeline-version2.x_WTA_references/

![](../../images/1b64f0d45b786835.png)

四、运行

真正运行起来非常简单：

  *   *   *   *   *   *   *   *   *   *   *   *

```
# 拷贝yml:cp template_wta_1.9.1.yml my.yml# 按照上述提示修改my.yml
# 提交cwl pipelinenohup  cwl-runner \ # 用nohup挂载至后台运行  --outdir ./scRNA-out \ # 输出路径    rhapsody_wta_1.9.1.cwl \ # cwl路径      CRR152997.yml  \ # yml路径        2>&1 > test.log  & # 运行日志存于test.log        # 如果你前面的步骤都没问题，那么运行完了去./scRNA-out下寻找输出结果即可
```

五、输出文件可参考源文档[1]，所以CRR152994_Expression_Data.st就是我们所需要的稀疏矩阵，可以参考这个教程读入：[没有barcode文件的单细胞数据要怎么读取](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247490952&idx=1&sn=364a3941e59e45234795c906a42fc9ab&chksm=9b3f64d8ac48edcec70384cf5c6a91224d0f7841ce3a7cfcade6513500c13673a6695d6f0299&scene=21#wechat_redirect>)(需要好好理解数据格式)。

![](../../images/55bb9e614053bb4b.webp)![](../../images/31e107f0ee334923.webp)![](../../images/7f2e7d18e11b5551.webp)

**往期回顾**

[ 单细胞分析的最上游——处理Fastq文件：cellranger](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484923&idx=1&sn=b5876af14fbee68d1e9db4b0f70cd1c8&chksm=9b3f7cabac48f5bdb3aac7d20201d89121a83720b41a10017564fedbb8c4a13df0da92daffd7&scene=21#wechat_redirect>)

[Cellranger报错：Unable to distinguish between [SC5P-R2, SC3Pv2] ...](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504739&idx=2&sn=e4e6ad0559b9b6a703d6ab37c2a8fdb0&chksm=9b3caa33ac4b23257424184bda44dd600ad98bc0dfdfa90ab0e3ebaf208e598b0b710fbafa4b&scene=21#wechat_redirect>)

[单细胞分析的最上游——处理Fastq文件：dropseqRunner](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247484937&idx=1&sn=4fe1fa518202bdaf462bb93a2614ed32&chksm=9b3f7f59ac48f64fafaf34bac2c80f06d3a86b6a84ccf12566c7eac25bb71c7edd3d74004cf7&scene=21#wechat_redirect>)

[scFAST分析| 03.fast模块](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247504044&idx=1&sn=d37991280217dcc29280efa344f856bb&chksm=9b3ca9fcac4b20eab124ccd4ba6ad3f5eee640df314e7d8fec0225035f06178e3a51dbe2033f&scene=21#wechat_redirect>)

参考：
[1]:https://www.bdbiosciences.com/content/dam/bdb/marketing-documents/BD_Single_Cell_Genomics_Analysis_Setup_User_Guide_v2.pdf
[2]:https://docs.docker.com/engine/install/ubuntu/[3]:https://help.aliyun.com/document_detail/60750.html

![](../../images/d0a809a43821e1e5.png)

**如何联系我们**

![](../../images/feb9903c31c83e08.png)![](../../images/349b3050f055aa44.gif) 公众号后台消息回复不便，这里给大家留一下领取资料及免费服务器([足够支持你完成硕博生涯的生信环境](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506420&idx=1&sn=6867471200293a24ff3122583585da33&chksm=9b3ca0a4ac4b29b2ea3a3873acbccd80ff7c9ef487baf2865cd3fc5f744beb6881230ec3c1c4&scene=21#wechat_redirect>))的**微信号** ，方便各位随时交流、提建议（科研任务繁重，回复不及时请见谅）。此外呼声一直很高的**交流群** 也建好了，欢迎大家入群讨论：

[永久免费的生信、科研交流群](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247505868&idx=2&sn=20c81313eaef9a7031a84ef3a691d1b5&chksm=9b3cae9cac4b278a42c8de97e864c7664a37e9a4adb5973625fe3f8dd1093e55aeda88d443aa&scene=21#wechat_redirect>)

大家可以阅读完这几篇之后添加[给生信入门初学者的小贴士](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247493329&idx=1&sn=597870b7f7ce10346da3561e7c281627&chksm=9b3c9f81ac4b169794088ce9abbcacb5f18e9fd174fc0d7e28da62d78facadf3100ef38aaf22&scene=21#wechat_redirect>)
[如何搜索公众号过往发布内容](<http://mp.weixin.qq.com/s?__biz=MzAwMzIzOTk5OQ==&mid=2247506266&idx=2&sn=22b1164bc9602c25620d058847785422&chksm=9b3ca00aac4b291c16d738271746ffb90149282a728f484e8a1952463c46a8e7dc4f883ab928&scene=21#wechat_redirect>)

![](../../images/e29532a7f035a4ca.webp)

![](../../images/0694eb4925c4700f.gif)您点的每个赞和在看，我都认真当成了喜欢
