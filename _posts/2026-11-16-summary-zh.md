---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 36 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [Meta FAIR/NYU：视觉编码器预训练可省，视觉专属参数不可省](#item-tech-news-1) ⭐️ 8.0/10
2. [美团开源 LongCat-2.5，称未用英伟达 GPU 训练](#item-tech-news-2) ⭐️ 8.0/10
3. [旧 Bitly 短链接被劫持，引发短链可靠性担忧](#item-tech-news-3) ⭐️ 7.0/10
4. [Protomaps：自托管地图瓦片变得便宜且简单](#item-tech-news-4) ⭐️ 7.0/10
5. [MacBook Pro OLED 屏幕的 PWM 频闪问题](#item-tech-news-5) ⭐️ 7.0/10
6. [理解现代 LLM 中的位置嵌入：实现与群表示视角](#item-tech-news-6) ⭐️ 7.0/10
7. [cudaMemcpy 调优工具在 B300 上报告 5 倍提速](#item-tech-news-7) ⭐️ 7.0/10
8. [华为云 MaaS 上线开源盘古模型 openPangu-2.1-Pro](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [卢特尼克因英伟达出口管制与持股关系受审视](#item-finance-news-1) ⭐️ 8.0/10
2. [中美俄领导人计划在深圳 APEC 场边举行首次三方会晤](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Meta FAIR/NYU：视觉编码器预训练可省，视觉专属参数不可省](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 8.0/10

Meta FAIR 与 NYU 的研究团队从零训练了 200 多个多模态大模型（主要比较采用 Qwen3-1.7B/4B 配置和 0.4B 视觉容量，规模阶梯覆盖 0.6B–6.4B），在相同数据、且把编码器预训练计入总预算的条件下，分别检验视觉编码器三项常被捆绑的选择：独立预训练、仅供视觉 token 使用的参数，以及把编码器置于 LLM 之前的位置。作者报告，独立预训练是可选的：用四种目标预训练的编码器，在算力匹配时最多只能追平随 LLM 从零训练的编码器，即使不计预训练算力也没有帮助；把 MetaCLIP 预训练延长 6.5 倍，只把 ImageNet 线性探针从 80.4% 提高到 84.4%，VQA 没有提升。视觉专属参数则不可省：无编码器模型在 0.6B 到 6.4B 的各个规模上都落后，约需 3 倍算力才能追上；把编码器的参数给 LLM，改善的是文本能力，而不是 VQA。编码器放置位置也可选：所谓 in-fusion 在前 8 层加入零初始化、仅供视觉使用的注意力投影和 FFN，在 1.7B 到 6.4B 上与编码器持平，首 token 时间低约 13%，1.7B 下 VQA 为 45.0，而编码器为 44.4；这些是作者披露的预印本结果，尚非独立复现。

reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「背景」** 常见的多模态大模型沿用「对比学习预训练的视觉编码器 + 投影层 + LLM」三段式结构，其中编码器预训练、视觉专用参数以及把编码器置于 LLM 之前这三项选择通常绑在一起，难以单独评估。已发布模型的做法正在分化：据 Hugging Face 模型卡，Google 的 Gemma 4 12B 取消了独立编码器，用轻量线性层把原始图像 patch 和音频波形直接投影进 LLM 的嵌入空间，而其他 Gemma 4 模型仍用专用编码器先把多模态数据处理好再交给 LLM。

**「影响」** 对 MLLM 架构选型而言，最具体的约束是：无编码器并不等于无视觉专属参数。若移除编码器，应保留仅供视觉 token 使用的分支；该研究在 1.7B 下测得文本共享视觉权重时 VQA 为 42.3，而前 8 层使用视觉专属分支时为 45.0。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/ gemma - 4 - 12 B · Hugging Face</a></li>
<li><a href="https://developers.googleblog.com/gemma-4-12b-the-developer-guide/">Gemma 4 12 B : The Developer Guide - Google Developers Blog</a></li>

</ul>
</details>

**标签**: `#multimodal LLMs`, `#vision encoders`, `#model architecture`, `#pretraining`, `#scaling experiments`

---

<a id="item-tech-news-2"></a>
### [美团开源 LongCat-2.5，称未用英伟达 GPU 训练](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团 LongCat 团队在模型发布一周后公开了 LongCat-2.5 的权重。该模型总参数约 1.6 万亿、每个 token 激活约 480 亿，支持文本、图像和视频输入，并以 MIT 许可证开放商用。官方称其训练全程使用华为升腾加速卡、未使用英伟达 GPU；在 Terminal Bench v2.1 上得分 88.4，略低于 Claude Opus 5 的 89.1，上述训练方式和成绩尚未见到独立验证。

telegram · zaihuapd · 11月15日 11:08

**「前代版本的铺垫」** LongCat 并非首次走非英伟达路线：据外部报道，美团于 2026 年 6 月 30 日开源 1.6 万亿参数的 LongCat-2.0，其训练与推理端到端运行在华为升腾加速卡上、使用华为 HCCL 通信库，全程未使用英伟达硬件，并以 MIT 许可证发布。据同一批报道，升腾、摩尔线程（MetaX）与沐曦在发布后数小时内即宣布推理兼容。因此 LongCat-2.5 是在同一国产算力栈上的继续迭代，区别在于这次明确面向可自主完成多步骤任务的智能体场景，并支持文本、图像与视频输入。

**「影响」** 对希望商用部署的团队，MIT 许可降低了法律障碍，但 1.6T 总参数、每 token 激活约 480 亿的规模仍要求按大规模并行推理来规划资源。若选择在升腾上运行，已有部署实践依赖 CANN 与 vLLM-Ascend 等非 CUDA 软件栈，需提前评估算子兼容性和迁移成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://temperaturezero.com/2026/07/05/meituan-trained-frontier-model-without-nvidia/">Meituan Trained a Frontier Model Without Nvidia – TemperatureZero</a></li>
<li><a href="https://aicodingweekly.datadriftpress.com/p/61-longcat-edges-out-gpt-5-5">#61 - LongCat edges out GPT-5.5 | AI Coding Weekly</a></li>
<li><a href="https://www.ainchina.com/blog/meituan-longcat-2-trillion-domestic-chips-china-ai-independence-2026/">How Meituan Built a Trillion - Parameter AI Model on 50,000 Domestic...</a></li>
<li><a href="https://arxiv.org/pdf/2607.08215">On the Limitations of Non-GPU AI Accelerators for Large-Model ...</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#large language models`, `#AI agents`, `#AI hardware`, `#Huawei Ascend`

---

<a id="item-tech-news-3"></a>
### [旧 Bitly 短链接被劫持，引发短链可靠性担忧](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/) ⭐️ 7.0/10

据 ransomnews.com 报道，一些早年创建的 Bitly 短链接正被他人劫持，点击后不再跳转到原始目标地址。该报道没有说明受影响链接的数量、劫持的具体实现方式，也没有给出 Bitly 的官方回应，因此这目前只是单一来源的报道，其波及范围尚未得到独立核实。对于仍在文档、社交帖子和印刷材料中使用旧短链的组织来说，这意味着链接指向何处已不再由原创建者掌握。

hackernews · hspeiser · 11月15日 22:11 · [社区讨论](https://news.ycombinator.com/item?id=50511395)

**「背景」** URL 短链服务（如 Bitly）会把原始长地址替换成短别名，点击后再重定向到目标页面；如果短链过期、账户被停用或别名被回收再分配，旧网页和帖子里的链接就可能指向新的目标。据《纽约邮报》报道，这次被利用的正是旧 X 帖子中已过期的 Bitly 链接，它们被改为跳转到与 9/11 和希特勒相关的维基百科页面。

**「实际影响」** 依赖短链的网站和机构需要检查仍在流通的旧链接是否仍指向预期页面，并考虑改用自有域名下的跳转服务或直接使用完整 URL；现有报道未说明 Bitly 是否已采取措施阻止此类劫持，因此不能假定平台侧已经修复。

**「社区讨论」** 在 Hacker News 讨论中，评论者 xp84 认为外包的短链服务比自建服务危险得多：链接多年累积后，一旦账号被停用或短链公司倒闭、数据丢失，就会留下无法修复的永久死链。评论者 silisili 则表示意外，没想到一家短链服务商大到需要设立信任与安全团队。这些是评论者的个人判断，且讨论中并未就影响范围达成共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nypost.com/2026/11/15/lifestyle/corporate-social-media-hacked-in-bizarre-bitly-link-hijacking-scheme/">Corporate social media hacked in bizarre Bitly link - hijacking scheme</a></li>

</ul>
</details>

**标签**: `#URL shorteners`, `#link hijacking`, `#web security`, `#link rot`, `#internet infrastructure`

---

<a id="item-tech-news-4"></a>
### [Protomaps：自托管地图瓦片变得便宜且简单](https://bruceroettgers.eu/blog/protomaps/) ⭐️ 7.0/10

这篇实践文章介绍如何用 Protomaps 和 PMTiles 自托管地图瓦片，作者的核心判断是：对开发者而言，这条路径的成本已降到可承受范围，部署也不再复杂。文章面向希望减少对商业地图服务依赖、自己掌握地图基础设施的开发者。由于提供的材料没有给出具体版本、价格、硬件配置或部署步骤，文中的“便宜、简单”属于作者的经验总结，而非独立测量。

hackernews · bcye · 11月15日 19:26 · [社区讨论](https://news.ycombinator.com/item?id=50509837)

**「背景」** Protomaps 的 PMTiles 是一种将切片地图数据打包成单个归档文件的格式，可直接存放在 S3 等通用对象存储上，从而省去自建切片服务器或依赖第三方切片服务。Protomaps 基于 OpenStreetMap 等开放数据构建，目标是让前端开发者无需中间服务器即可提供切片地图，并支持低成本、零维护的“无服务器”地图应用。

**「影响」** 对预算有限的独立开发者，自托管 PMTiles 可把实时地图渲染从按调用量付费的商业服务转为自行承担存储和带宽；有评论者称，若用 Mapbox 或 Google Maps 就不会考虑做自己的 Wikipedia 步行游戏。限制也同样明确：高分辨率卫星影像会随缩放层级快速膨胀，有评论者因存储预估只能做到 z17。

**「社区讨论」** HN 评论中，有人推荐同类项目 OpenFreeMap，称其公共实例不限地图浏览量或请求数；也有评论者分享把 PMTiles 放在 Cloudflare R2 后自行掌控访问控制和隐私的做法。另有评论者提醒，普通底图瓦片容易自托管，但高分辨率卫星影像的存储成本会随缩放层级急剧上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://protomaps.com/about">Protomaps - The open source map in a file</a></li>
<li><a href="https://awesome-repositories.com/repository/protomaps-pmtiles">PMTiles - serve map tiles from cloud storage | Awesome Repos</a></li>
<li><a href="https://github.com/protomaps/PMTiles">GitHub - protomaps / PMTiles : Pyramids of map tiles in a single file on...</a></li>

</ul>
</details>

**标签**: `#Protomaps`, `#self-hosting`, `#map tiles`, `#PMTiles`, `#OpenStreetMap`

---

<a id="item-tech-news-5"></a>
### [MacBook Pro OLED 屏幕的 PWM 频闪问题](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

在采用 OLED 屏幕的 MacBook Pro 上，PWM 调光造成的频闪被文章视为一个实际可用性问题：对频闪敏感的用户，显示参数更好并不等于更好用。文章引用的 240Hz 说法在社区中受到质疑，有评论者称复测后没有得出同一结论，认为最坏情况为 480Hz，甚至可能是 960Hz。该评论者推测，双层串联 OLED 的两层可能都以 480Hz、180 度反相进行 PWM，在两层同时工作时形成约 960Hz 的有效频率。现有材料没有给出可复现的测量细节，因此这些频率判断仍属于讨论中的假设，而非已确认结论。

hackernews · MacAnorak · 11月15日 13:15 · [社区讨论](https://news.ycombinator.com/item?id=50506719)

**「背景：PWM 调光与 240 Hz 测量」** PWM（脉冲宽度调制）调光是 OLED 屏幕调节亮度的常见方式：像素以固定频率快速开关，靠占空比改变主观亮度，而不是连续降低发光强度；频率越低、波动越深，对闪烁敏感的人越容易出现眼疲劳、头痛或眩晕。据 11 月 7 日的报道，Notebookcheck 的实验室测试显示，采用 PROLED XDR 面板的 14 英寸 MacBook Pro 在亮度 99% 及以下时以 240 Hz 调光、波动深度约 56%，而 Mini-LED 版 M4 Pro MacBook Pro 测得 14,880 Hz，两者调制频率相差约 62 倍。围绕这块屏幕的讨论，正是建立在这一测量结果之上。

**「影响」** 对频闪敏感的用户，MacBook Pro 的 OLED 优势可能被 PWM 频闪抵消，选购时应把常用亮度下的主观舒适度与对比度、亮度等规格一起评估，而不是只看屏幕参数。

**「社区讨论」** 评论区的核心分歧在 PWM 频率：legitronics 质疑文章的 240Hz 读数，提出串联 OLED 反相工作可能把有效频率推到 960Hz；achr2 则引用论文称人眼可感知高于显示屏频率两倍以上的闪烁。另有用户报告脑震荡后几乎所有屏幕都会带来不适，显示了个体差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.appleheadlines.com/macbook-pro-oled-eye-strain-pwm-flicker/">MacBook Pro OLED Eye Strain &amp; PWM Flicker: 7 Moves - AH</a></li>
<li><a href="https://daily.dev/posts/the-macbook-pro-s-oled-pwm-problem-when-a-better-display-becomes-worse-to-use-bxu5e2tu9">The MacBook Pro&#x27;s OLED PWM Problem: When a &#x27;Better&#x27;...</a></li>

</ul>
</details>

**标签**: `#OLED`, `#PWM flicker`, `#display technology`, `#MacBook Pro`, `#accessibility`

---

<a id="item-tech-news-6"></a>
### [理解现代 LLM 中的位置嵌入：实现与群表示视角](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 7.0/10

Sebastian Raschka 杂志发表了一篇技术讲解文章《Understanding Positional Embeddings in Modern LLMs》，主题是现代大语言模型中位置嵌入的原理与实现。该文在 Hacker News 上引发讨论，讨论者补充了位置嵌入的群论视角。需要说明的是，本次提供的条目摘要未包含文章正文，因此文中涉及的具体模型、版本或对比结论无法在此核实。可以确认的是，这是一篇面向 AI/ML 从业者的教育性深度文章，而非新模型或新方法的发布。

hackernews · vismit2000 · 11月15日 12:14 · [社区讨论](https://news.ycombinator.com/item?id=50506376)

**「背景」** 位置编码用于让 Transformer 在注意力计算中保留 token 的顺序信息；早期模型常使用可学习的绝对位置编码，而现代 LLM 更普遍采用旋转位置编码（RoPE），因为它更自然地融入注意力，并且比旧的绝对位置方案更能应对超出训练长度的序列。本文所讲的实现与理论背景正建立在这一演变之上。

**「社区讨论」** Hacker News 用户 programjames 认为，文章只讲了位置嵌入的实现层面，而要真正理解位置嵌入必须掌握其理论：位置嵌入本质上是群表示，这既是推导它们的方法，也是把它们参数化为可微分、可学习形式的方法。他举例称，旋转位置嵌入（RoPE）是平移群 ℝⁿ 的表示，而该群是阿贝尔群。上述观点属于评论者的理论主张，不代表原文或独立验证的结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sebastianraschka.com/llms-from-scratch/ch04/10_rope/">Rotary Positional Embeddings ( RoPE ) | Sebastian Raschka , PhD</a></li>
<li><a href="https://www.youtube.com/watch?v=GQPOtyITy54">RoPE ( Rotary positional embeddings ) explained: The... - YouTube</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#positional embeddings`, `#machine learning`, `#transformers`, `#technical deep-dive`

---

<a id="item-tech-news-7"></a>
### [cudaMemcpy 调优工具在 B300 上报告 5 倍提速](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

一位开发者发布了用于调优 cudaMemcpy 的开源工具 cmt，并称在 B300 上把 1 GB uint8 张量的可页内存 CPU→GPU 拷贝从 10.2 GB/s 提升到 51.5 GB/s，约为 5 倍。该结果来自作者自己的基准：连续 5 次拷贝并逐次同步计时，目前只覆盖这一项工作负载，尚无独立验证。工具、博客和代码均已公开，读者可以复现；现有信息不足以判断其他数据规模、数据类型或硬件上的表现。

reddit · r/MachineLearning · /u/makneeee · 11月15日 18:20

**「背景：可分页内存与固定内存」** CUDA 中由 malloc 或普通 PyTorch CPU 张量分配的内存属于“可分页”（pageable）内存，操作系统可以将其换出，因此 GPU 的直接内存访问（DMA）引擎无法安全地直接读写它。传统上，cudaMemcpy 处理这类传输时须先经由驱动内部的固定（pinned）暂存缓冲区中转，这一额外拷贝步骤通常使可分页的 CPU 到 GPU 带宽明显低于固定内存传输。该工具针对的正是这条默认路径。

**「影响」** 对频繁进行可页内存主机到设备传输的 CUDA 用户，这项结果提供了一个可直接试用的调优选项；但在采用前应以自己的张量大小和访问模式复测，因为 5 倍加速仅对应作者在 B300 上的 1 GB 拷贝场景。

**标签**: `#CUDA`, `#GPU memory`, `#performance engineering`, `#ML systems`, `#open-source tooling`

---

<a id="item-tech-news-8"></a>
### [华为云 MaaS 上线开源盘古模型 openPangu-2.1-Pro](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

华为云 MaaS 模型即服务平台于 11 月 15 日上线开源盘古模型 openPangu-2.1-Pro，并围绕 Agent 开发、AI 编码和推理优化升级能力。该模型基于 10 万余条专项数据优化 Skills 触发与工具调用，重点适配鸿蒙 ArkTS 开发和升腾算子生成，并接入智果 AgentArts、码道 CodeArts、果办 OfficeAce。其推理输入、输出和缓存命中输入价格分别为 0.8 元、3.2 元和 0.016 元/百万 tokens；但公告未披露参数规模、开源许可证、基准测试成绩或代码仓库地址，其开源可用范围和自部署条件仍不明确。

telegram · zaihuapd · 11月15日 16:03

**「背景」** 华为云 MaaS 以预置模型 API 的形式提供模型，用户可直接接入，平台侧还提供调用限流、用量统计和性能监控（tool-2-1、tool-2-3）。openPangu-2.1-Pro 属于开源盘古系列，公开模型资料将其描述为该系列的旗舰大语言模型，此次是通过 MaaS 平台上线，而非仅发布模型文件（tool-2-3）。

**「影响」** 对鸿蒙 ArkTS 和升腾算子开发者来说，现在可通过华为云 MaaS 按 token 计费调用该模型，并可在公告所列的 AgentArts、CodeArts、OfficeAce 等产品中使用；若需要自行部署、审计权重或确认商业使用条件，则要等待许可证和代码仓库信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/027/450.htm">开源盘古模型 openPangu-2.1-Pro 上线华为云，围绕 Agent 开发、AI 编...</a></li>
<li><a href="https://www.aihub.cn/ai-model/openpangu-2-1-pro/">openPangu-2.1-Pro - 华为开源盘古旗舰模型，主打Agent与鸿蒙编码 - A...</a></li>

</ul>
</details>

**标签**: `#Huawei Pangu`, `#open-source LLM`, `#AI coding`, `#HarmonyOS ArkTS`, `#Ascend`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [卢特尼克因英伟达出口管制与持股关系受审视](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

美国商务部长霍华德·卢特尼克因英伟达相关的利益冲突和出口管制争议受到审视；CNBC 查阅证券申报文件发现，其子领导的坎托·菲茨杰拉德在 2025 年 9 月至 2026 年 3 月间将申报持有的英伟达股票减少 49%，从约 352 万股降至 178 万股，同期价值从 6.52 亿美元降至 3.10 亿美元，申报文件未说明减持原因。此事发生在英伟达 CEO 黄仁勋周四辞职、以及 Axios 报道卢特尼克多次抵制打击涉嫌向中国转运英伟达芯片的新加坡公司 Megaspeed 之后；CNBC 称，无证据显示其子提前知情或持仓变化与情报警告有关。

rss · CNBC Finance · 11月15日 19:58

**「背景」** 卢特尼克在康托·菲茨杰拉德工作数十年，1991 年起担任总裁兼首席执行官，并于 2025 年离任出任美国商务部长，该公司现由他的两个儿子执掌（tool-1-1、tool-1-2）。商务部正是负责执行对华芯片出口管制、包括把企业列入限制贸易的“实体清单”的部门，而美国已禁止英伟达向中国出售先进芯片（tool-2-2、tool-2-1）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Howard_Lutnick">Howard Lutnick - Wikipedia</a></li>
<li><a href="https://www.britannica.com/money/Howard-Lutnick">Howard Lutnick | Cantor Fitzgerald , 9/11, Donald... | Britannica Money</a></li>
<li><a href="https://www.bbc.com/news/articles/cmdx1vpprk9vo">Suspected China spy linked to Nvidia &#x27;s ex-boss left in 2025...</a></li>
<li><a href="https://www.cbsnews.com/news/howard-lutnick-scott-bessent-nvidia-megaspeed-testimony/">Lutnick agrees to testify as Bessent blames him for not banning Nvidia ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Howard Lutnick`, `#Cantor Fitzgerald`, `#export controls`, `#ethics`

---

<a id="item-finance-news-2"></a>
### [中美俄领导人计划在深圳 APEC 场边举行首次三方会晤](https://apnews.com/article/trump-xi-putin-summit-china-5fe92253ef38100bae913834a9b74d72) ⭐️ 7.0/10

中国外交部发言人宣布，中美俄三国领导人计划于 11 月 19 日（周四）在深圳 APEC 峰会期间举行三方会晤；媒体称这将是三国领导人首次专门举行三方会晤。会晤在 APEC 场边举行，不属于 APEC 正式议程。

telegram · zaihuapd · 11月16日 01:38

**「背景」** 2026 年亚太经合组织（APEC）领导人会议定于 11 月 18 日至 19 日在深圳举行，由东道主中国国家主席习近平主持（tool-1-1、tool-1-2）；中美俄三方会晤安排在会议第二天的场边举行，因此不属于 APEC 正式议程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/APEC_China_2026">APEC China 2026 - Wikipedia</a></li>
<li><a href="https://theworlddata.com/apec-summit/">APEC Summit 2026 | Trump-Xi-Putin Meeting, Date, Location ...</a></li>

</ul>
</details>

**标签**: `#地缘政治`, `#APEC`, `#中美俄关系`, `#政策风险`

---