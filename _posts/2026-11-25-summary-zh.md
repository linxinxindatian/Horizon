---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 25 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [OpenAI 预印本声称矩阵乘法指数为 9/4](#item-tech-news-1) ⭐️ 9.0/10
2. [GreyNoise 报告 Check Point 管理服务器遭活跃入侵](#item-tech-news-2) ⭐️ 8.0/10
3. [VMware vCenter 曝 9.8 分 vmdir 免鉴权绕过漏洞](#item-tech-news-3) ⭐️ 8.0/10
4. [OpenAI 称 GPT-6.2 能写代码设计蛋白质结合体](#item-tech-news-4) ⭐️ 7.0/10
5. [Ternary Bonsai 2.5 27B 发布：本地三值量化模型](#item-tech-news-5) ⭐️ 7.0/10
6. [LLM 与编程代理的十二个月三大拐点](#item-tech-news-6) ⭐️ 7.0/10

**财经新闻**
1. [小米三季度经调整净利同比下降 56.8%，汽车交付破 10 万辆](#item-finance-news-1) ⭐️ 7.0/10
2. [SpaceX 放弃 7.38 亿美元联邦宽带补贴，改为免费提供星链设备](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 预印本声称矩阵乘法指数为 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

OpenAI 的 GitHub math 仓库发布预印本《The matrix multiplication exponent is nine fourths》，声称在所有域上证明矩阵乘法指数为 9/4（即 2.25）。该文目前只是未经同行评审的预印本，尚无独立验证，因此应视为作者的证明声明，而不是已确认的定理。对理论计算机科学和算法设计者而言，若证明成立，这将确定矩阵乘法的渐近指数，而不只是给出一个新的上界算法。

hackernews · E-Reverance · 11月25日 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**「背景」** 矩阵乘法的“指数”描述 n×n 矩阵相乘的渐近代价：若代价可写成 O\(n^ω\)，ω 就是该指数，确定其精确值长期是理论计算机科学的核心问题之一。此前已知 9/4 是该指数的上界，即已有算法能以约 n^\{9/4\} 的代价完成乘法；OpenAI 于 2026 年 11 月 24 日公开的预印本进一步声称，对每个域，形式算术电路都需要至少 Ω\(n^\{9/4\}\) 次非标量乘法或除法门，从而把指数钉在 9/4。

**「对算法研究与实践的影响」** 若该预印本被独立验证，通用矩阵乘法的指数就被钉在 9/4，研究者不必再寻找更低的渐近指数，而应转向常数因子和实现优化；但当前依赖矩阵乘法的机器学习系统不会立即受益，因为评论指出达到 O\(n²·²⁵\) 的算法仍远不实用，且该论文尚未经过同行评审。

**「社区讨论」** 评论者 orlp 指出标题中的 O\(n^2.25\) 不准确，应写成 Θ\(n^2.25\)；brandonb 则称论文证明的是 Ω\(n^2.25\) 下界，而 2.25 的上界此前已知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.info/news/openai-matrix-multiplication-exponent-nine-fourths">OpenAI preprint claims exact 9/4 matrix multiplication exponent</a></li>
<li><a href="https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">The matrix multiplication exponent is nine fourths</a></li>
<li><a href="https://theorempath.com/topics/matrix-multiplication-algorithms">Matrix Multiplication Algorithms | TheoremPath</a></li>

</ul>
</details>

**标签**: `#matrix multiplication`, `#algorithms`, `#theoretical computer science`, `#OpenAI`, `#AI for math`

---

<a id="item-tech-news-2"></a>
### [GreyNoise 报告 Check Point 管理服务器遭活跃入侵](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign) ⭐️ 8.0/10

GreyNoise 报告了一起针对 Check Point 安全管理服务器的活跃入侵活动，攻击者通过伪造管理员会话获取管理权限。据其披露，对 HFS 服务器 loginSrp1 端点的每次 POST 都会返回含 sid 的签名会话 Cookie，而 sid 取自 JavaScript 的 Math.random\(\)；攻击者连续登录收集足够输出后，重建 Node.js V8 PRNG 的内部状态，恢复 HFS 的会话 Cookie 签名密钥，并伪造签名的管理员会话 Cookie。现有材料未说明受影响客户数量、攻击者身份或 Check Point 的修复与缓解状态。

hackernews · louiereederson · 11月24日 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50630594)

**「背景」** GreyNoise 的这份报告覆盖 2026 年 10 月 17 日至 11 月 2 日观测到的攻击活动，称至少 22 个组织受到影响，并提到攻击者使用一台被入侵的 HFS 服务器作为中继。该事件的技术前提是会话令牌的随机性：当服务器用 JavaScript 的 Math.random\(\) 生成会话 ID 时，攻击者可通过连续登录收集输出，重建 V8 引擎伪随机数生成器的内部状态，从而预测后续值并伪造签名会话。

**「影响与处置」** 对运行 HFS 的 Check Point 管理服务器而言，已恢复的 Cookie 签名密钥会把一次会话伪造变成管理员级入侵；仅重置管理员密码未必足够，运维方应确认是否轮换或吊销签名密钥、使现有会话失效，并排查 loginSrp1 上的异常连续登录。

**「社区讨论」** 评论者质疑初始访问方式仍不明确，并推测多家 Check Point 客户同时受影响可能与安全管理服务器暴露在互联网上及 CVE-2026-16232 有关；也有人认为应修复 Math.random 这类默认不安全的随机数接口，而不是要求每个应用正确使用。上述内容均为评论者的推测或主张，并非已确认事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign">An Active Intrusion Campaign Against Check Point Security ...</a></li>
<li><a href="https://x.com/DFIR_Radar/status/2124972032077279688">DFIR Radar on X: &quot;GreyNoise tracks GT13, a suspected AI ...</a></li>

</ul>
</details>

**标签**: `#security`, `#exploit`, `#PRNG predictability`, `#Check Point`, `#session hijacking`

---

<a id="item-tech-news-3"></a>
### [VMware vCenter 曝 9.8 分 vmdir 免鉴权绕过漏洞](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html) ⭐️ 8.0/10

Broadcom 为 VMware 产品线发布了一批补丁，共修复 23 个漏洞，其中 vCenter 目录服务（vmdir）的鉴权绕过漏洞 CVE-2026-123903 评分 9.8。据 The Hacker News 报道，只要攻击者能够访问 vCenter，就能绕过认证直接进入系统；该漏洞据称在补丁发布前几天已被作为零日漏洞利用。来源未说明受影响的具体 vCenter 版本、实际利用规模或临时缓解措施，因此受影响范围仍需以 Broadcom 官方公告为准。

telegram · zaihuapd · 11月24日 14:50

**「背景」** vCenter 是 VMware 虚拟化环境的管理平台，vmdir 则是它的目录服务；此次鉴权绕过正好发生在这个服务上。对这类管理平面来说，只要攻击者能访问 vCenter，就可能跳过认证直接进入系统，而不需要有效账号凭据。

**「受影响范围与处置重点」** 受影响的不只是最新的 9.x 分支：公开的漏洞信息显示，vCenter 8.0 U3k 及更早版本，以及低于修复构建的 9.0.x、9.1.x 均在受影响范围内，因此运维团队需要先盘点自有 vCenter 的具体构建号，不能只按大版本判断是否安全。由于该漏洞只需能访问 vCenter 即可绕过鉴权、无需任何凭据，暴露在互联网或跨网段可达的管理接口应优先收敛访问来源，并尽快升级到修复版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/dinosn/CVE-2026-123903">dinosn/ CVE - 2026 - 123903 : CVE - 2026 - 123903 : VMware vCenter vmdir ...</a></li>

</ul>
</details>

**标签**: `#VMware vCenter`, `#security vulnerability`, `#authentication bypass`, `#zero-day`, `#enterprise patching`

---

<a id="item-tech-news-4"></a>
### [OpenAI 称 GPT-6.2 能写代码设计蛋白质结合体](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 7.0/10

OpenAI 报告称，GPT-6.2 在获得五个目标蛋白的三维结构和指定结合位点后，能编写代码生成候选 minibinder（微型结合蛋白）的三维设计，且在设计阶段未使用专门的蛋白质 AI 模型。OpenAI 同时说明，要把这些设计变成可在实验室测试的蛋白质，仍需用 SolubleMPNN 为每个设计建议氨基酸序列，并用其他专用蛋白质模型筛选预计能按设计折叠并在目标位点结合的候选。因此，所谓“内在”能力目前覆盖的是结构设计与代码生成，而非从序列生成到候选筛选的完整蛋白质设计流程；相关结论来自 OpenAI 的表述。

hackernews · acossta · 11月24日 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**「背景」** 蛋白质设计通常不是单一模型完成：先提出三维结构，再用专门模型生成可折叠的氨基酸序列并筛选候选。OpenAI 的页面称 GPT-6 模型用推理和代码设计蛋白质结构与序列，并在五个靶点观察到结合证据；评论则指出序列建议仍由 SolubleMPNN 等专门模型完成，这正是“内在能力”争议的来源。

**「实际影响」** 对做蛋白设计的团队而言，这一流程的实际约束并未改变：GPT‑6.2 产出的是三维骨架，氨基酸序列仍需专门的 SolubleMPNN 等模型补全，能否按设计折叠、是否结合到目标位点也要靠专用预测模型筛选，因此合理的采用方式是把大模型当作写代码、串联各环节的编排层，而不是替换既有设计流水线。可作为对照的是，Anthropic 此前也演示过 Claude 调用多个开源蛋白设计与折叠模型来设计 minibinder 的路线，并给出了实验验证的设计数量（tool-3-1、tool-3-2、tool-3-3），这说明“LLM 做胶水”的做法已有先例，实际差异更多落在工具接入方式与筛选流程上，而非单个模型能否独立完成设计。

**「社区讨论」** 在 Hacker News 讨论中，fabian2k 质疑 GPT-6.2 究竟设计出了什么，理由是氨基酸序列才决定蛋白质结构；plaidfuji 认为更准确的说法是 GPT 充当连接各个专用模型子任务的“胶水层”，称其“超越专用模型”为时过早。joe-esquibel 还指出，现有证据偏重计算探索、实验室对照偏少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT - 6 models demonstrate intrinsic protein - design ... | OpenAI</a></li>
<li><a href="https://www.anthropic.com/research/Claude-accelerates-protein-design">Claude accelerates protein design and analytical chemistry \ Anthropic</a></li>
<li><a href="https://fourweekmba.com/ai-anthropic-claude-protein-design-minibinders-automated-resear/">Anthropic&#x27;s Claude Orchestrated Existing Protein - Design Tools to...</a></li>
<li><a href="https://www.linkedin.com/posts/deniz-kavi_agents-now-do-de-novo-protein-design-but-activity-7496581896878059520-OXiw">Agents now do de novo protein design , but how do I use them?</a></li>

</ul>
</details>

**标签**: `#AI`, `#protein design`, `#LLM capabilities`, `#biotech`, `#code generation`

---

<a id="item-tech-news-5"></a>
### [Ternary Bonsai 2.5 27B 发布：本地三值量化模型](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 7.0/10

Ternary Bonsai 2.5 27B 发布，这是一款面向本地推理的 27B 三值量化模型，社区关注点集中在长上下文和代理式编程。一名用户在 Mac Mini M5 Pro（24GB 内存、512GB SSD）上用 Q2 GGUF 运行，报告生成速度约 22–25 tokens/s，并可轻松容纳 128k 上下文。另一名用户用自建长任务基准比较 Bonsai 2 与 2.5，二者通过数均为 5/8，但 2.5 的步骤少 17%、耗时少 29%；关于其 SWE-bench Verified 表现接近 Opus 4.6 的说法仅来自评论者的不确定推测，尚无独立验证。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**「背景」** Ternary Bonsai 是 PrismML 的三值（ternary）量化模型系列，它通过将权重压缩到三种取值，把 27B 模型的权重大小从原始 Qwen3.8 27B 的约 53.8 GB 降到约 5.9 GB；其 GGUF 发布包含 Q2\_0、PQ2\_0、PTQ1\_0 等基础变体。2.5 版本是在相同 5.9 GB 体积下对 Bonsai 2 的迭代，官方称其重点增强了 agentic 编码、多轮工具调用和多步任务执行；另有第三方报道称，它在三项自主编码测试中的平均分从 Bonsai 2 的 37.9 升至 54.2。

**「影响」** 对希望在消费级内存上运行长上下文本地模型的开发者，这些早期报告说明 24GB 内存配置值得实测，但现有证据仅来自少量用户报告和自建任务；在用于代理式编码前，应复测 128k 上下文下的内存占用、吞吐和任务完成率，并与同尺寸 Q1/Q2 量化模型直接对比。

**「社区讨论」** 评论中的主要分歧是基准可信度：nik\_s 猜测其 SWE-bench Verified 成绩可能与 Opus 4.6 相当，但自己也质疑其中有多少是基准拟合、基准漂移或小模型进步；hatthew 则要求与同尺寸 Q1/Q2 量化模型直接对比。支持者更看重可运行性，ariwilson 报告了 22–25 tokens/s，thepoet 报告自建任务耗时减少 29%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-2-5-27b">PrismML — Introducing Ternary Bonsai 2 . 5 27 B : Powering Agentic...</a></li>
<li><a href="https://huggingface.co/collections/prism-ml/bonsai-25-27b">Release files and model cards for Ternary Bonsai 2 . 5 27 B .</a></li>
<li><a href="https://dzen.ru/b/awYEAzpr1A5OydWA">Bonsai 2 . 5 лучше исправляет код при тех же 5,93 ГБ Ternary ... | Дзен</a></li>

</ul>
</details>

**标签**: `#ternary quantization`, `#local LLMs`, `#model release`, `#inference performance`, `#agentic coding`

---

<a id="item-tech-news-6"></a>
### [LLM 与编程代理的十二个月三大拐点](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 7.0/10

Simon Willison 在 11 月 24 日发表的回顾文章中，把自己眼中过去十二个月 LLM 与编程代理的进展归纳为三个拐点，依据主要是他的个人使用体验，而非独立基准测试；提供的原文在第三部分后截断。第一个拐点是 2025 年 11 月 24 日发布的 Claude Opus 4.5，以及同期发布的 GPT-5.1 Instant、GPT-5.1 Thinking、GPT-5.1-Codex 和 GPT-5.1-Codex-Max：它们让编程代理在他的日常任务中变得可靠可用。第二个是 2026 年 6 月发布的 Claude Fable 5：它是对因网络安全能力过强而未发布的 Mythos 模型做了能力限制后发布的版本，曾受美国出口管制影响，直到 7 月 1 日才恢复；这也促使他提出“给出目标和工具即可暴力求解”的 Fable 级模型标准。后来符合这一标准的模型包括 Fable 5/5.1/5.2、Opus 5.5、GPT-6 Astra，Gemini 4 Neon 可能也算。第三个拐点出现在 2026 年 9 月至 10 月前后：前沿模型在 Blender/Three.js 3D 建模和游戏开发上明显变强，9 月 22 日发布的 Opus 5.5 首次让他觉得模型“理解好玩”，能把游戏从无聊改到有趣。

rss · Simon Willison · 11月24日 23:02

**「背景」** 这篇文章基于 Simon Willison 在 AI Engineer Code Summit 上的主题演讲，他在 2026 年 11 月 24 日——Claude Opus 4.5 发布一周年之际——回顾过去十二个月的能力变化。Claude Code 于 2025 年 2 月 24 日随 Claude 3.7 Sonnet 一同推出，到 Opus 4.5 面世时只有 9 个月；Willison 表示自己此前并未把 Claude Code 作为日常主力工具，因为需要频繁纠正、不足以明显提速。

**「对游戏开发者的影响」** 对把这类模型引入工作流的游戏开发者来说，一个具体后果是：是否披露 AI 参与，已经成为项目层面的现实风险。House House 在《Big Walk》中公开承认曾用 AI 修复一个小 bug 后，这款独立游戏引发了一场争议（Ars Technica，11 月 11 日）；与此同时，前 Take-Two 高管把《GTA VI》称作“最后一款前 AI 时代的大作”。因此，当团队用编码代理产出 3D 资产或玩法代码时，需要事先明确披露口径，而不必等到发布后再回应质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/11/10/grand-theft-auto-vi-last-blockbuster-video-game-before-ai/">Grand Theft Auto VI: the last pre-AI blockbuster video game ...</a></li>
<li><a href="https://arstechnica.com/gaming/2026/11/big-walk-used-ai-to-fix-a-bug-now-the-indie-gaming-world-is-having-a-reckoning/">Big Walk used AI to fix a bug. Now the indie gaming world is ...</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#coding agents`, `#AI engineering`, `#Anthropic Claude`, `#technology analysis`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [小米三季度经调整净利同比下降 56.8%，汽车交付破 10 万辆](https://ir.mi.com/static-files/3d372aaa-8ff8-4e33-ba01-68c8d7975a0b) ⭐️ 7.0/10

小米集团 2026 年第三季度经调整净利润为 48.84 亿元，同比下降 56.8%，但仍略高于市场预期的 47.46 亿元；同期营收 1072.4 亿元，同比下降 5.2%。当季小米汽车交付 100,975 辆，手机出货 3070 万台。

telegram · zaihuapd · 11月24日 10:09

**「背景」** 小米同时经营手机和智能电动车业务；据 Capital.com，2026 年一季度其汽车业务经营亏损 31 亿元，同期存储芯片成本同比约翻倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://capital.com/en-int/market-updates/xiaomi-stock-forecast-02-06-2026">Xiaomi Stock Forecast | EV Losses, $20bn HKD Buyback | Capital.com</a></li>

</ul>
</details>

**标签**: `#Xiaomi`, `#quarterly earnings`, `#net profit decline`, `#EV deliveries`, `#smartphone market`

---

<a id="item-finance-news-2"></a>
### [SpaceX 放弃 7.38 亿美元联邦宽带补贴，改为免费提供星链设备](https://x.com/SawyerMerritt/status/2125314062997467640) ⭐️ 7.0/10

据转述的社交媒体消息，SpaceX 已同意放弃美国 BEAD 宽带补贴计划下的 7.38 亿美元联邦资金，联邦拨付金额因此为 0 美元；作为交换，它须向符合条件的美国家庭免费提供星链终端，并承诺最低 100 Mbps 下载、20 Mbps 上传、提供低价月费套餐，以及维持 10 年服务。

telegram · zaihuapd · 11月25日 02:17

**「背景」** BEAD 是美国联邦政府用于补贴欠发达地区宽带建设的计划；据 Benton Institute 和 PCMag 报道，美国国家电信与信息管理局（NTIA）为此设计了一种不含财务拨付、但保留最低服务要求和网络性能测试的新合同模式。

**「影响」** 对符合条件的美国农村家庭而言，直接后果是星链终端免费，但仍需支付月费，并受 100 Mbps 下载、20 Mbps 上传和 10 年服务承诺约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.benton.org/headlines/spacex-declines-bead-awards">SpaceX Declines BEAD Awards | Benton Institute for Broadband ...</a></li>
<li><a href="https://www.pcmag.com/news/spacex-to-feds-well-offer-starlink-for-free-in-bead-areas-if-you-drop-oversight">SpaceX to Feds: We&#x27;ll Offer Starlink for Free in BEAD Areas ...</a></li>
<li><a href="https://www.basenor.com/blogs/news/spacex-walks-away-from-738m-bead-subsidy-promises-free-starlink-kits-instead">SpaceX Walks Away From $738M BEAD Subsidy, Promises Free ...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#BEAD`, `#broadband subsidy`, `#US telecom policy`

---