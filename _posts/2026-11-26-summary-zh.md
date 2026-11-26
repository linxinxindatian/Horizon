---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 35 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [1Password 确认安全事件，部分客户账户信息遭窃](#item-tech-news-1) ⭐️ 8.0/10
2. [更短版 GRH Lean 验证发布](#item-tech-news-2) ⭐️ 8.0/10
3. [Minecraft Java 曝高危字体 RCE 漏洞，无官方补丁](#item-tech-news-3) ⭐️ 8.0/10
4. [Aaronson 博文指向“矩阵乘法指数 9/4”论文，引发 AI 争论](#item-tech-news-4) ⭐️ 7.0/10
5. [Ubuntu 安全响应迟缓引发迁移 Debian 讨论](#item-tech-news-5) ⭐️ 7.0/10
6. [pw-loudness-eq：将 Windows 响度均衡逆向移植到 PipeWire](#item-tech-news-6) ⭐️ 7.0/10
7. [SemiAnalysis 发布 GDPx 基准，聚焦 11 个高经济价值领域](#item-tech-news-7) ⭐️ 7.0/10
8. [腾讯开源 Hy4 flash 量化权重，最小版可在 64 GB Mac mini 运行](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [美商务部被曝威胁英特尔：不交出 10% 股权就要承担后果](#item-finance-news-1) ⭐️ 9.0/10
2. [美国拟对中、欧、日、印等 14 个贸易伙伴加征第 301 条关税](#item-finance-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [1Password 确认安全事件，部分客户账户信息遭窃](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password 确认发生安全事件：公司自 11 月 19 日起调查员工企业 GitHub 账户被入侵的迹象，攻击者借该账户访问源代码并向后台服务推送恶意代码，导致部分客户账户信息被下载。泄露信息包括姓名、邮箱地址、账户标识及账户创建和最近登录时间；1Password 表示客户保险库及其内容未受影响，但未披露受影响用户数量。公司已停用涉事账户、轮换或撤销可能暴露的内部凭证，并加强邀请和恢复邮件的验证码；现有用户无需更改账户，但应警惕利用这些信息实施的钓鱼。

hackernews · lxhrstn · 11月25日 17:18 · [社区讨论](https://news.ycombinator.com/item?id=50644817)

**「事件背景」** 1Password 于 11 月 19 日开始调查其员工企业 GitHub 账户被入侵的迹象，随后确认攻击者借该账户访问源代码，并向后台服务推送恶意代码，最终导致部分客户账户信息被下载。这意味着入侵路径落在代码托管与后端部署环节，而非直接攻破用户的加密保险库；公司表示客户保险库及其内容未受影响。对使用托管式在线保险库的用户而言，这次事件的关键区分在于“账户元数据”（姓名、邮箱、账户标识、创建与最近登录时间）与“保险库中保存的凭据内容”这两类资产。

**「精准钓鱼风险」** 受影响客户面临的具体后果是精准钓鱼风险上升：泄露的姓名、邮箱、账户标识及登录时间可被用来伪造可信的账户通知，评论中已有人报告收到包含部分个人信息的钓鱼邮件。1Password 表示用户无需更改账户，但已加强邀请和恢复邮件的验证码，收到此类邮件应通过独立渠道核验。

**「社区讨论」** 评论者把焦点放在从员工 GitHub 账户被入侵，到攻击者向生产服务推送代码这一条攻击路径上：tptacek 称这是 SaaS 公司的标准攻击路径，ctidd 则质疑公告未说明是否缺少分支保护，也未说明分支保护规则如何被绕过。qixxiq 还称收到一封疑似利用本次泄露数据、包含部分个人细节的钓鱼邮件，提醒信息泄露可能引发后续攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>

</ul>
</details>

**标签**: `#security incident`, `#1Password`, `#SaaS security`, `#supply chain`, `#phishing`

---

<a id="item-tech-news-2"></a>
### [更短版 GRH Lean 验证发布](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

一个社区项目在 GitHub 上发布了更短的 GRH Lean 验证版本，目标是让 Anthropic 的大型形式化证明工件更易阅读和审查。有评论者称行数从约 1700 万行降到约 7.6 万行，并指出新版带有“已知数学”与“新数学”的清晰分区及大量人类可读文档；这些数字来自社区讨论，尚未在给定材料中独立核实。现有信息显示这主要是可读性和重构层面的改进，而不是新的数学突破，且条目本身缺少完整技术细节。

hackernews · nb-t · 11月25日 21:48 · [社区讨论](https://news.ycombinator.com/item?id=50648050)

**「背景」** Anthropic 此前公开的 GRH 证明工件并不是一篇论文，而是一个包含 175,187 个文件、约 1,740 万行的 Lean 归档（tool-2-3）；据相关条目记载，发布次日 Lean FRO 与 Mathlib Initiative 宣布独立验证成功（tool-2-1）。此次社区重写把规模压到约 7.6 万行，降幅约 99.56%（tool-2-2），针对的正是原始工件体量过大、人工审阅困难的问题。

**「影响」** 对需要复核该形式化证明的研究者和开发者而言，更短、带分区和文档的版本有助于降低阅读门槛；若要把它当作原始工件的替代品，仍需核对两者在 Lean 中的等价性以及是否完整保留原证明内容。

**「社区讨论」** 有评论者质疑这是否回应了 Tao 此前关于“巨型证明缺乏洞见”的担忧，并认为还需要真正的数学论文来解释核心论证；另一些评论者则强调，清晰的已知/新数学分区和大幅缩减的行数已经有助于消化这份证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Alp%C3%B6ge&#x27;s_proof_of_the_Riemann_hypothesis">Alpöge&#x27;s proof of the Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50648050">Much shorter version of GRH Lean verification from Anthropic</a></li>
<li><a href="https://www.youtube.com/watch?v=aDl7-MWFLVc">17 Million Lines Claim to Prove Riemann. We Ran Them. - YouTube</a></li>

</ul>
</details>

**标签**: `#Lean`, `#formal verification`, `#AI for math`, `#open source`, `#proof engineering`

---

<a id="item-tech-news-3"></a>
### [Minecraft Java 曝高危字体 RCE 漏洞，无官方补丁](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

11 月 22 日公开的 minecraft2shell 项目（含 PoC）披露，Minecraft Java 版服务器资源包中的特制 TrueType 字体可触发 FreeType 2.14.3 及更早版本的原生越界写，并可在 Java 版 26.3 Windows 客户端导致任意代码执行。该项目称 1.20.5 至 1.21.10、26.1 至 26.4 快照受影响，1.20.4 及更早版本和基岩版不受影响。Mojang 仍使用 lwjgl-freetype 3.4.3，暂无官方补丁；社区已于 11 月 24 日发布 m2sfix 1.0.0，通过 Java agent 或 mod 关闭 hinting。投稿人建议在修复前不要添加资源包，将多人游戏服务器资源包权限设为“禁用”，或安装该临时修复 mod。

telegram · zaihuapd · 11月25日 12:46

**「背景」** 该漏洞利用的是 Minecraft Java 客户端的字体解析链路：Windows 客户端通过随附的 FreeType 2.14.3 x64 处理 TrueType 字体，公开 PoC 明确针对 Mojang 签名的 Java 26.3 Windows 构建。服务器资源包可向客户端提供字体文件，因此恶意 TTF 能在多人游戏中进入本地 FreeType 解析并触发越界写，这也是该 PoC 具备远程利用路径的前提。

**「实际影响」** 对使用受影响 Java 版 Windows 客户端的玩家和服务器运营者而言，资源包已成为可触发远程代码执行的输入：在 Mojang 发布补丁前，应把多人服务器资源包权限设为“禁用”，或拒绝添加来源不明的资源包。社区方案 m2sfix 1.0.0 / minecraft2shell-fix 通过 Java agent 或 mod 让字体在不启用 hinting 的情况下加载，以避免执行字体自带字节码；它属于客户端侧临时缓解，并非官方补丁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bikini/minecraft2shell">GitHub - bikini/ minecraft 2 shell : Minecraft to native RCE · GitHub</a></li>
<li><a href="https://freetype.org/">The FreeType Project: a free , high-quality and portable Font engine</a></li>
<li><a href="https://github.com/sunrisemc-tw/minecraft2shell-fix">GitHub - sunrisemc-tw/minecraft2shell-fix: Client-side ...</a></li>
<li><a href="https://www.cyberkendra.com/2026/11/minecraft2shell-minecraft-java-rce-resource-pack.html">Minecraft2Shell RCE in Minecraft Java Still Unpatched</a></li>

</ul>
</details>

**标签**: `#Minecraft`, `#RCE vulnerability`, `#FreeType`, `#security advisory`, `#community patch`

---

<a id="item-tech-news-4"></a>
### [Aaronson 博文指向“矩阵乘法指数 9/4”论文，引发 AI 争论](https://scottaaronson.blog/?p=10379) ⭐️ 7.0/10

Scott Aaronson 发布了一篇以“Holy shit”开头的博文，惊叹“正在发生之事”的量级，并链接到论文《The matrix multiplication exponent is nine fourths》。但所给博文摘录只有这条“另见”链接，没有给出论文作者、算法、证明或独立验证，因此无法确认 9/4 这一矩阵乘法指数是否已被确立，也无法确认该结果与 AI 有何关系。Hacker News 的讨论因此主要围绕 AI 的数学能力能否外推到其他科学领域以及 AGI 风险，而非对论文结果本身的技术核验。

hackernews · Kotlopou · 11月25日 19:11 · [社区讨论](https://news.ycombinator.com/item?id=50646108)

**「背景」** 矩阵乘法的指数 ω 指的是让两个 n×n 矩阵能在 O\(n^ω\) 时间内相乘的最小指数；朴素算法为 n³，自 Strassen 算法以来，学界一直在设法压低这一上界。2026 年 11 月 24 日，OpenAI 的 math 预印本仓库中出现一篇题为《The matrix multiplication exponent is nine fourths》的论文，摘要声称在所有域上证明了该指数为 9/4，即 2.25（tool-2-1、tool-2-2）。Aaronson 的这篇帖子本身只是给出该预印本的链接并表达震惊，而随后已有第三方文章对其证明展开核查，可见这是一项仍处于审读中的声明，而非已获独立验证的结果（tool-2-3）。

**「对矩阵乘法复杂度研究的影响」** 对矩阵乘法算法研究者而言，直接后果是理论基准被改写：据 11 月 24 日的预印本，任意域上方阵乘法的上界与下界已经匹配，指数被确定为 9/4。若该结论成立，指数层面的进一步改进空间即被封住，后续工作只能转向常数因子、实际实现或更受限的计算模型。现有材料只涉及渐近复杂度，没有给出实际运行时间或常数因子数据，因此不能据此推断常用线性代数库会立即加速；关注者应直接查阅 OpenAI math 仓库中的论文原文，核对证明细节与适用范围。

**「社区讨论」** 评论区围绕 AI 的数学能力能否外推展开分歧：jsLavaGoat 认为擅长公理化数学不等于能解决其他领域或构成生存风险，Nevermark 则认为人类普遍低估了变化的量级。utopiah 则追问，若只有 Lean、MathLib 和大量算力而没有 LLM，类似进展是否早已可能发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">math /preprints /The-matrix-multiplication-exponent-is-nine ...</a></li>
<li><a href="https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">The matrix multiplication exponent is nine fourths</a></li>
<li><a href="https://lilting.ch/en/articles/matrix-multiplication-exponent-nine-fourths-openai">Checking OpenAI&#x27;s 9/4 Matrix Multiplication Exponent Paper ...</a></li>
<li><a href="https://interestingengineering.com/culture/openai-exact-2-25-matrix-multiplication-exponent">OpenAI establishes exact 2.25 exponent for matrix multiplication</a></li>
<li><a href="https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">math/preprints/The- matrix - multiplication - exponent -is...</a></li>

</ul>
</details>

**标签**: `#AI and mathematics`, `#AGI debate`, `#matrix multiplication`, `#scientific discovery`, `#Hacker News`

---

<a id="item-tech-news-5"></a>
### [Ubuntu 安全响应迟缓引发迁移 Debian 讨论](https://www.openwall.com/lists/oss-security/2026/11/25/9) ⭐️ 7.0/10

一篇发布在 oss-security 邮件列表的帖子在 Hacker News 上引发讨论，焦点是 Ubuntu 安全更新响应偏慢，以及部分运维人员因此把服务器镜像迁到 Debian。现有材料只有讨论内容和链接标题，没有给出具体漏洞、受影响版本或 Ubuntu 的官方回应。评论中关于“响应慢”的判断和迁移做法属于用户经验与意见，并非经独立验证的测量结果。

hackernews · gslin · 11月25日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=50647181)

**「事件背景」** 这场讨论源自 2026 年 11 月 25 日 oss-security 邮件列表上 Hanno Böck 发起的帖子：帖子指出，一台较新的 Ubuntu LTS 系统运行的是内核 7.0.0-44，并据此推测 Ubuntu 没有直接采用 kernel.org 的长期支持（longterm）内核，而是把补丁回移到较旧的内核版本。因此，讨论的焦点在于 Ubuntu 自行维护内核分支、自行回移修复的这一维护方式。

**「实际影响」** 对运行 Ubuntu 服务器的团队而言，讨论暴露出的操作问题是：有评论者称安全修复会先出现在 -updates 仓库、数小时后才进入 security 仓库，因此只从 security 仓库自动升级可能较晚拿到修复。该评论者表示已改为安装全部更新，并明确接受由此带来的回归或破坏风险；这一取舍尚未得到独立验证。

**「社区讨论」** 有运维人员称已因安全响应问题把服务器镜像从 Ubuntu 迁到 Debian，认为主流发行版在 2026 年出现这种延迟不可接受；也有评论者反驳称，主要发行版会花大量时间做回归测试，Debian 同样可能发生回归。另有用户表示，Ubuntu 以往是通用 Linux 虚拟机的默认选择，但最近因补丁迟缓首次改选 Debian。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openwall.com/lists/oss-security/2026/11/25/9">oss-security - Slow Ubuntu security response times - openwall.com</a></li>
<li><a href="https://www.openwall.com/lists/oss-security/">oss-security mailing list - Openwall</a></li>

</ul>
</details>

**标签**: `#Ubuntu`, `#Linux security`, `#distribution maintenance`, `#vulnerability response`, `#Debian`

---

<a id="item-tech-news-6"></a>
### [pw-loudness-eq：将 Windows 响度均衡逆向移植到 PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

GitHub 项目 pw-loudness-eq 将 Windows 的响度均衡（loudness equalization）行为逆向分析后，移植为 PipeWire 模块，面向希望获得类似 Windows 响度处理的 Linux/PipeWire 用户。项目材料显示作者分析了 Windows 音频组件的行为；但所提供的材料没有给出独立测量、PipeWire 版本兼容范围或性能数据，因此目前只能确认这是一个公开的逆向实现，不能确认其输出与 Windows 逐样本一致。

hackernews · ThrowNotAway · 11月25日 11:34 · [社区讨论](https://news.ycombinator.com/item?id=50641171)

**「背景」** Windows 的共享模式音频输出会在所有流混音后经过 audiodg.exe 中的 CAudioLimiter（位于 AudioEng.dll），对接近峰值的信号做轻微压缩，因此同一素材经共享模式播放与 WASAPI 独占或 ASIO 播放可能略有差异。Audio Science Review 论坛 2021 年的讨论中，已有用户通过注册表禁用 CAudioLimiter 来比较这种处理对听感的影响。

**「影响」** 对希望统一不同音源响度的 PipeWire 用户，这提供了一个可试验的 Linux 侧选项；但采用前应核对项目许可证和与所用 PipeWire 版本的兼容性，并检查其末尾限幅是否改变峰值，因为评论者指出类似算法可能抬高纯音等集中信号，需要额外限制。

**「社区讨论」** 评论区的核心分歧之一是命名与必要性：有评论者强调这不是“均衡”而是响度归一化，并质疑为何要从 Windows DLL 逆向，认为算法并不复杂且可能触及伦理或许可问题。另有评论者称 Windows 在共享模式（WASAPI loopback、DirectSound、MME）会经 audiodg.exe 中的 CAudioLimiter 轻微压缩峰值，而 WASAPI 独占和 ASIO 不受影响；也有人反对把安静与响亮段落压到同一电平，认为动态范围本身是作品的一部分。

<details><summary>参考链接</summary>
<ul>
<li>Windows Loudness Equalization, reverse-engineered and ported to PipeWire | Hacker News</li>
<li>Ending the Windows Audio Quality Debate | Page 41 | Audio Science Review (ASR) Forum</li>

</ul>
</details>

**标签**: `#audio-processing`, `#reverse-engineering`, `#pipewire`, `#linux-audio`, `#dsp`

---

<a id="item-tech-news-7"></a>
### [SemiAnalysis 发布 GDPx 基准，聚焦 11 个高经济价值领域](https://newsletter.semianalysis.com/p/evaluating-recent-model-releases) ⭐️ 7.0/10

SemiAnalysis 于 11 月 1 日发布 GDPx 基准，用于衡量前沿模型在经济价值最高的领域中的表现，覆盖芯片设计、网络安全、生物、金融、法律、量化交易、递归自我改进（RSI）、硬件设计、材料科学、对齐与软件工程 11 个领域，共 206 道题，由 14 家专业数据合作方制作。文章批评 GDPVal、Agent&\#x27;s Last Exam 等试图做全面的基准按 GDP 占比或 O\*NET 职业分类来选题，认为 AI 的经济影响分布极不均衡，跟踪前沿模型应聚焦其影响最大的领域。发布日得分最高的模型 Opus 5.5 仅得 12%，SemiAnalysis 称这一巨大提升空间使其能区分未来模型，而不像已饱和的 Terminal Bench 4.0。文章还提到 Anthropic、OpenAI、Google（Gemini 4 系列）以及阿里巴巴和 Moonshot 近期的密集发布，但所给摘录在排行榜具体数字前截断；文中指出 Fable 5.2 与 GPT-6.2 Astra 因安全分类器拉低了总分，并给出剔除网络安全、生物、对齐三域并对法律、金融改用部分评分的调整榜单。

rss · Semianalysis · 11月26日 00:05

**「背景」** GDPx 是 SemiAnalysis 于 11 月 1 日发布的基准，覆盖芯片设计、网络安全、生物学、金融、法律、量化交易、递归自我改进、硬件设计、材料科学、对齐和软件工程等领域，并由 14 家数据合作伙伴制作了 206 项任务。SemiAnalysis 批评 GDPVal 和 Agent&\#x27;s Last Exam 按 GDP 占比或 O\*NET 分类选择领域，认为 AI 的经济影响并不均匀分布，因此 GDPx 改为聚焦其认为影响最大的领域。

**「影响」** 对打算用 GDPx 排名做选型的团队来说，原始总分混合了模型能力与安全分类器的拒答行为：SemiAnalysis 明确表示 Fable 5.2 和 GPT-6.2 Astra 在网络安全、生物、对齐三个领域因安全分类器触发而被压低分数，并另行给出剔除这三域、对默认二值评分的法律与金融改用部分评分的榜单，因此横向比较模型时应以这一口径为准。

**标签**: `#AI benchmarks`, `#frontier models`, `#model evaluation`, `#agentic AI`, `#AI economics`

---

<a id="item-tech-news-8"></a>
### [腾讯开源 Hy4 flash 量化权重，最小版可在 64 GB Mac mini 运行](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

腾讯混元通过大模型压缩加速工具箱 AngelSlim 开源了 224B 参数模型 Hy4 flash 的 GGUF 量化权重。原权重约 410.27GiB，最小的 IQ2-AH 版本为 125.73GiB，约为原版的 30%；腾讯方面称，配合 Strata offload 框架，64 GB Mac mini 可以运行。来源给出的数据显示，48 GB 显存设备在 10K 上下文下每秒生成 89 个 token，M5 Max 128 GB 运行 Q3\_K、32K 上下文时每秒 47 个 token，Q3\_K 在 DeepSWE v1.1 等评测中与原模型差距不超过 0.4 分；这些性能和精度数据尚未见独立复测结果。

telegram · zaihuapd · 11月25日 09:29

**「背景」** GGUF 是本地推理常用的量化模型文件格式，量化通过降低权重精度来压缩体积。Strata 是纯 Rust 的 GGUF 推理引擎，项目介绍称可在 CUDA、Vulkan 后端运行超出显存的模型；其 offload 思路是把部分模型权重或 KV 缓存从快速显存移到 CPU 内存或存储，以便在显存不足时继续推理。这正是 Hy4 flash 的最小量化权重能借助 64 GB Mac mini 运行的前提。

**「影响」** 对希望本地运行该模型的用户来说，64 GB Mac mini 的可行性依赖 Strata offload，而且最小的 IQ2-AH 权重仍有 125.73GiB，明显超过该机器的内存容量。若更看重精度，可参考 Q3\_K 在 32K 上下文下每秒 47 个 token、评测差距不超过 0.4 分的数据，但部署前应把吞吐和 offload 带来的开销纳入容量规划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/RustingStudio/RustingStrata">GitHub - RustingStudio/RustingStrata: Pure-Rust LLM inference ...</a></li>
<li><a href="https://atlarge-research.com/pdfs/2025-cheops-llm.pdf">An I/O Characterizing Study of Offloading LLM Models and KV...</a></li>

</ul>
</details>

**标签**: `#Tencent Hunyuan`, `#Hy4 flash`, `#GGUF quantization`, `#local LLM inference`, `#Strata offload`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美商务部被曝威胁英特尔：不交出 10% 股权就要承担后果](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 9.0/10

法庭文件显示美国商务部施压英特尔出让 10%股份，特朗普随后称美国政府未付费即拥有并控制该约 110 亿美元股权。

telegram · zaihuapd · 11月25日 13:25

**标签**: `#英特尔`, `#美国政府持股`, `#半导体政策`, `#公司治理`, `#产业政策`

---

<a id="item-finance-news-2"></a>
### [美国拟对中、欧、日、印等 14 个贸易伙伴加征第 301 条关税](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 8.0/10

据报道，美国政府拟依据 1974 年《贸易法》第 301 条，对中国、欧盟、日本、印度等 14 个贸易伙伴加征新关税；这些关税针对因补贴造成的制造业结构性产能过剩，并按国别设定，不采用统一税率。除中国外，新关税不叠加现有关税，且不超过双方在对等贸易框架协议中公布的税率；中国则要在 2018 年已加征的 25%之上再加 20%。报道称，若中国未遵守 2025 年 10 月在韩国釜山达成的贸易休战协议，对华新关税可能升至 40%。

telegram · zaihuapd · 11月25日 13:59

**「背景」** 第 301 条允许美国在调查后对贸易伙伴加征关税；这批拟议关税源于为期八个月的调查，针对受补贴的制造业产能，并旨在替代今年早些时候被最高法院推翻的关税。

**「影响」** 这 14 个经济体的制造业出口商以及进口这些商品的美国企业将直接受到影响，因为它们出口到美国的商品成本会因国别税率不同而发生变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html">U.S. unveils new Section 301 tariffs targeting China , EU and others</a></li>
<li><a href="https://www.foxbusiness.com/fox-news-global-economy/trump-admin-raise-tariffs-china-eu-other-trading-partners">Trump administration proposes sweeping Section 301 tariffs on China ...</a></li>

</ul>
</details>

**标签**: `#US trade policy`, `#Section 301 tariffs`, `#China-US trade`, `#global supply chains`, `#EU-Japan-India trade`

---