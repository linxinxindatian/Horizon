---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 52 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Optimizely CDN 被入侵，向客户站点投放恶意脚本](#item-tech-news-1) ⭐️ 8.0/10
2. [Jiff 1.0 发布：Rust 日期时间库](#item-tech-news-2) ⭐️ 8.0/10
3. [vLLM v0.34.0：KV 缓存默认扩展，Model Runner V1 移除](#item-tech-news-3) ⭐️ 7.0/10
4. [卡内基梅隆大学在 YouTube 免费上线完整 CS 课程讲座](#item-tech-news-4) ⭐️ 7.0/10
5. [报告称 Windows 11 收集开发工具与编码代理使用数据](#item-tech-news-5) ⭐️ 7.0/10
6. [Linux 拟增第三类 futex：futex PING](#item-tech-news-6) ⭐️ 7.0/10
7. [Marimba：单次冻结 ASR 编码器回答语音查询](#item-tech-news-7) ⭐️ 7.0/10
8. [美国与九国签署《旧金山宣言》协调超级智能供应链安全](#item-tech-news-8) ⭐️ 7.0/10
9. [亚马逊称 Artex 驱动 AI 代理窃取 API 密钥自我供血](#item-tech-news-9) ⭐️ 7.0/10
10. [美国拟将 AI 芯片出口管制延伸至远程访问](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [美国商务部长卢特尼克因英伟达相关往来面临利益冲突质疑](#item-finance-news-1) ⭐️ 8.0/10
2. [英特尔及 CEO 陈立武遭股东集体诉讼](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Optimizely CDN 被入侵，向客户站点投放恶意脚本](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely 的 CDN 被用于在多个客户站点投放攻击者提供的恶意脚本，受影响站点包括 Zoom、GitLab，以及 Optimizely 自身的 www.optimizely.com 和 login.optimizely.com。攻击者据报获得了多个 Optimizely 客户项目的写入权限，但初始入侵途径仍未查明，可能是 Optimizely 系统被攻破、拥有跨客户访问权限的凭据泄露，或其他原因。现有说明强调 CDN 只是分发了交给它的内容，并非 CDN 缓存投毒。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景」** Optimizely 通过 CDN 向客户网站提供可嵌入的第三方 JavaScript，这类脚本通常在页面加载时直接执行。正因如此，攻击者一旦获得 Optimizely 项目侧的写入权限，恶意代码就能随共享脚本出现在所有嵌入站点上，而无需逐一入侵这些站点。

**「实际影响」** 据 Gizmodo 报道，此次事件波及 178 个组织，被注入的 JavaScript 被用于加密货币盗取、支付卡信息侧录乃至 iOS 漏洞利用，受影响站点的访客应据此把账号凭据与支付信息视为可能已暴露。由于报告明确指出攻击者如何取得跨客户项目的写权限仍未查清，依赖 Optimizely 的站点在原因查明前难以判断自身是否被波及，需要直接核查自己项目下发的脚本内容。

**「社区讨论」** 评论者把矛头指向营销驱动的第三方 JavaScript：有人以 Google Tag Manager 为例，认为它让营销部门无需工程介入即可添加标签，导致页面脚本膨胀，并希望此次事件促使企业重新评估这种做法；也有人批评 Optimizely 和大型站点缺乏发布审核、分阶段上线等问责机制。另有评论者追问，若受影响站点并不在同一页面处理加密货币或信用卡，恶意脚本为何仍构成风险，并怀疑解释中是否遗漏了关键环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/sprawling-malware-attack-reportedly-affects-zoom-cnn-fox-news-peacock-and-170-others-2000840831">Sprawling Malware Attack Reportedly Affects Zoom and Other Major...</a></li>

</ul>
</details>

**标签**: `#supply-chain-security`, `#third-party-javascript`, `#web-security`, `#cdn-security`, `#security-incident`

---

<a id="item-tech-news-2"></a>
### [Jiff 1.0 发布：Rust 日期时间库](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Rust 日期时间库 Jiff 发布了 1.0 版本，作者 burntsushi 在项目页面公布了这一版本，目标用户是需要在 Rust 中处理日期与时间的开发者。现有材料没有披露具体的 API 变更、性能数据或与既有库的兼容性细节，因此目前只能确认 1.0 发布这一事实，还不能据此判断它的功能或性能优势。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** Jiff 是 Andrew Gallant（burntsushi）为 Rust 编写的日期时间库，设计上把时区处理放在 API 的核心位置，目标是提供难以误用的高级日期时间原语，同时保持合理性能。据其文档介绍，在 1.0 发布时，Jiff 已在 Cargo、uv、Starship 和 Nushell 等工具的生产环境中使用。

**「对 Rust 项目集成的影响」** 对打算采用的 Rust 开发者来说，接入只需执行 \`cargo add jiff\`，但实际集成方式由 crate features 决定：可以配置是否使用 Rust 标准库、是否启用 serde 支持，以及是否将时区数据库（Time Zone Database）一并编入二进制文件；最后一项会直接影响产物体积，并在离线环境下决定时区数据是否可用，因此需要在构建配置阶段确认并固定下来。

**「社区讨论」** 曾维护 chrono 的开发者表示，chrono 的 API 改进因用户对稳定性的需求而遇到阻力，自己最终因看不到改进路径而停止维护，并对 Jiff 表示肯定；另有评论赞赏 Jiff 明确说明自己并非所有场景都适用，同时询问 TAI、UT1 等时间尺度该如何处理。这些属于社区观点与使用期待，并非对 Jiff 1.0 能力的独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant&#x27;s Blog</a></li>
<li><a href="https://elsolitario.org/en/2026/11/16/jiff-1-0-rust-datetime-library/">Rust Datetime Library: Jiff 1.0 Explained - elsolitario.org</a></li>
<li><a href="https://docs.rs/jiff/latest/jiff/">jiff - Rust</a></li>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/ jiff : A datetime library for Rust that encourages...</a></li>

</ul>
</details>

**标签**: `#Rust`, `#datetime library`, `#open source`, `#API design`, `#time handling`

---

<a id="item-tech-news-3"></a>
### [vLLM v0.34.0：KV 缓存默认扩展，Model Runner V1 移除](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 7.0/10

vLLM 发布 v0.34.0，包含 1,061 个提交和 412 位贡献者；该版本默认启用可扩展 KV 缓存，按预热及 CUDA 图捕获后实际空闲显存确定大小（如 MiniMax-M3 在 H200 上从 43.3 万增至 67.2 万 token），并移除 Model Runner V1，使 V2 成为唯一 GPU runner。新增模型包括 Mistral Large 4、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe 等 10 个。项目自报在 Blackwell 和 MI355X 上最高 1.95× decode、1.6× 吞吐提升，但也说明新缓存策略在部分 H200 模型、并发 128 时可能使 TPOT 上升 6–18%。升级者需处理默认 block size 由 16 改为 64、ROCm 7.2 镜像停止发布、huggingface\_hub &gt;= 2.0.0 依赖，以及移除 VLLM\_USE\_V2\_MODEL\_RUNNER=0 等破坏性变更。

github · khluu · 11月16日 23:22

**「背景」** vLLM 是开源的大语言模型推理引擎，其 KV cache 用于保存注意力计算的键值状态，直接影响可服务的上下文长度和并发吞吐。此前默认的 KV cache 容量按预留显存比例估算，且 GPU 推理仍保留 Model Runner V1 与 V2 两条路径；v0.34.0 改为依据预热后实际空闲显存计算并默认启用，同时只保留 V2。

**「影响」** 对现有部署而言，升级前应检查启动参数和环境变量：设置 VLLM\_USE\_V2\_MODEL\_RUNNER=0 会直接在启动时报错，依赖旧 16 block size 或旧显存估算的配置需显式传 --block-size 16、--gpu-memory-utilization 0.9 或 --no-enable-extensible-kv-cache。ROCm 用户必须切到 10.0 的 wheel/镜像，使用 fp\_quant、Marlin W4A8 或 Keye-VL 的部署则需先迁移或继续留在旧版本。

**标签**: `#vllm`, `#llm-inference`, `#open-source`, `#performance`, `#kv-cache`

---

<a id="item-tech-news-4"></a>
### [卡内基梅隆大学在 YouTube 免费上线完整 CS 课程讲座](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学推出 CS Learn，在 YouTube 免费发布来自当前 CMU 计算机科学课程的完整学期讲座，覆盖多个主题。项目负责人 Phillip Compeau 表示，本周每天首播一门课程，明年 1 月还会上线更多课程；这些内容由在校学生开发的工具协助自动化部分制作流程。目前公开的是课程视频，面向公众开放，定位为完整的开放课程资源。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 开放课程并非新概念：该项目负责人 Phillip Compeau 在讨论中承认，MIT 大约 25 年前就已开展类似工作。据他介绍，CMU 此次的不同之处在于让学生开发工具来自动化大量课程视频的制作流程，并以每天上线一门课的方式发布当前课程完整学期的讲座。

**「影响」** 对想系统自学计算机科学的人来说，这些视频提供了按完整学期组织的免费课堂材料；但课程作业、项目和反馈是否能同步获得，将直接影响它能否支撑完整的学习体验。

**「社区讨论」** 有 CMU 校友在评论中点名期待 15-259 概率与计算、Tianqi Chen 的机器学习系统等课程。也有评论强调，讲座若没有项目、讲义和反馈就容易落空，并提醒不应只发布 CS1 而缺少研究生课程；另有评论认为，在 AI 时代学好基础仍能让 AI 成为工具。

**标签**: `#open educational resources`, `#computer science education`, `#CMU`, `#YouTube`, `#online learning`

---

<a id="item-tech-news-5"></a>
### [报告称 Windows 11 收集开发工具与编码代理使用数据](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 7.0/10

有报告称，Windows 11 会收集用户运行哪些编码代理和开发工具的数据，涉及使用这些工具的开发者。由于原文内容未提供，具体收集字段、触发条件、是否可关闭及适用范围目前无法核实，应视为待确认的报告而非微软已确认的事实。相关讨论集中在遥测边界、AI 代理沙箱和迁移 Linux。

hackernews · cwaffles · 11月16日 22:58 · [社区讨论](https://news.ycombinator.com/item?id=50524736)

**「背景」** 这里的关键背景是 Windows 11 的可选诊断数据机制：系统通过 ETW 诊断报告汇总组件状态，而 Xusheng Li 的逆向分析称，MissionControlAggregator 会把开发者工具和编程代理是否运行记录为一个紧凑的使用位图，而不是保存提示词或完整会话。该分析于 2026 年 11 月 16 日发布，并称这些信息可通过可选诊断上报排队发送给微软。

**「对开发者的实际影响」** 对在 Windows 11 上运行编码代理的开发者来说，更直接的后果出现在隔离能力上，而不是遥测本身：微软的 Microsoft Execution Containers（MXC）于 2026 年 10 月 7 日发布，提供 .NET、TypeScript 和 Rust SDK，让代理开发者自行接入沙箱权限策略，其中会话容器和 WSL 容器仅支持 Windows 11。在具体代理工具完成接入之前，用户要么以未沙箱方式运行代理，要么改用 WSL；有评论者称 Claude Code 目前尚未支持 MXC，这属于社区说法，尚待官方确认。

**「社区讨论」** 评论中，herf 认为 Windows 对 AI 代理的沙箱支持进展缓慢，并称 MXC 于 10 月 7 日才推出且 Claude Code 尚未支持，因此希望以非侵入式遥测帮助确定优先级；dannyw 则指出显卡驱动和浏览器等也会收集可执行文件名、路径或浏览记录。另有 s\_dev 和 dead\_hn\_theory 讨论迁移 Linux 的可行性，前者称单机游戏大多可用而多人游戏仍有问题，后者认为以 Web 工作为主者约一周即可适应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/windows-coding-agent-telemetry/">Windows 11 Is Collecting Data on Which Coding Agents and ...</a></li>
<li><a href="https://windowsforum.com/news/windows-11-optional-telemetry-can-report-coding-agent-usage-research-finds.452631/">Windows 11 Optional Telemetry Can Report Coding Agent Usage ...</a></li>
<li><a href="https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/">Microsoft Execution Containers: Policy-driven containment for ...</a></li>
<li><a href="https://ccleaks.com/news/how-to-use-microsoft-execution-containers-mxc-oct-2026">How to Use Microsoft Execution Containers to Sandbox AI Agents</a></li>

</ul>
</details>

**标签**: `#Windows telemetry`, `#developer privacy`, `#AI coding agents`, `#platform policy`

---

<a id="item-tech-news-6"></a>
### [Linux 拟增第三类 futex：futex PING](https://lwn.net/Articles/1102988/) ⭐️ 7.0/10

LWN 报道，Suleiman Souhlal 提交了一组补丁，计划为 Linux 内核加入第三种 futex 类别“futex PING”，定位为“下一代优先级继承”，目标是让 futex 更快。现有 futex 实现已提供两种基本变体，但报道指出部分用户仍认为速度不够。该系列目前只是提案，来源未给出合并状态、完整设计细节或独立性能数据。

rss · LWN.net · 11月16日 15:06

**「背景」** futex 是用户空间实现快速互斥锁的机制，通常只在发生竞争时才进入内核；目前内核已有两种基本 futex 变体。Suleiman Souhlal 提出的 RFC 补丁系列（共 12 个补丁）增加第三类 FUTEX\_PING：它不同于经典 PI futex，允许从等待队列顶部“偷取”，内部用 Proxy Execution 取代 rtmutex，并包含乐观自旋等机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lkml.org/lkml/2026/9/17/386">LKML: Suleiman Souhlal: [RFC PATCH 00/12] FUTEX_PING: A ...</a></li>
<li><a href="https://lwn.net/Articles/1094994/">FUTEX_PING: A stealable futex using Proxy Execution. - lwn.net</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#futexes`, `#concurrency`, `#priority inheritance`, `#real-time`

---

<a id="item-tech-news-7"></a>
### [Marimba：单次冻结 ASR 编码器回答语音查询](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Reddit 帖子介绍了一篇 arXiv 论文中的 Marimba：对每个 8 秒音频窗口只运行一次冻结的 Qwen3-ASR-0.6B 编码器，再通过类型化问题（是/否、选项或分数）返回校准后的概率，覆盖词项、语种、话轮结束、说话人变化与说话人数。帖子报告，在相同的 1000 个公开问题上，Marimba 在 9 项测试中的 6 项追平或超过 30B-A3B 的 Qwen3-Omni，但在 Speech Commands 上仍落后；语种识别在 300 条 FLEURS 片段上达到 100%，AMI 和 VoxConverse 的说话人变化 AUROC 为 0.966–0.980，说话人数计数优于 pyannote 3.1。局限也明确：话轮结束 AUROC 为 0.930，低于 Smart Turn v3.2 的 0.982，在 ICSI 上以 0.716 对 0.712 基本打平，且该读出在 Smart Turn 数据上训练，属于分布内结果；在 CochlScene 场景分类上所有头都只有随机水平。代码、Apache-2.0 权重和 pip 包已发布。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** Qwen3-ASR 家族包含 0.6B 与 1.7B 两个版本，覆盖 52 种语言和方言，并借助 Qwen3-Omni 的音频理解能力。Marimba 因此不再为每个问题单独训练模型，而是冻结 Qwen3-ASR-0.6B 编码器，在每段 8 秒音频的一次前向表示上接出术语、语种、话轮结束和说话人变化等读出器，并与规模大得多的 Qwen3-Omni（30B-A3B）比较。

**「影响」** 对开发者而言，最直接的能力是用同一个冻结编码器的一次前向结果服务多类查询，并可通过 \`pip install marimba-audio\` 和 Apache-2.0 权重接入；但它在 CochlScene 上仅达随机水平，说明新任务仍需专门验证或训练读出层，不能当作通用音频分类器直接使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3-ASR">GitHub - QwenLM/Qwen3-ASR: Qwen3-ASR is an open-source series ...</a></li>

</ul>
</details>

**标签**: `#speech recognition`, `#audio question answering`, `#model efficiency`, `#calibration`, `#speaker diarization`

---

<a id="item-tech-news-8"></a>
### [美国与九国签署《旧金山宣言》协调超级智能供应链安全](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

11 月 15 日，美国与澳大利亚、印度、以色列、日本、韩国、卡塔尔、新加坡、阿联酋和英国签署《旧金山宣言》，确认经济安全是国家安全的基础，并承诺共同保护支撑超级智能（SI）供应链的敏感技术与关键基础设施。宣言为后续合作设立了五个工作组，分别覆盖创新政策框架、SI 在关键领域的应用、SI 全栈供应链协作、安全港与供应链安全枢纽、以及 SI 安全与韧性。目前公开内容仅为一份宣言，未披露各工作组的具体成员、时间表、约束性义务或执行机制。

telegram · zaihuapd · 11月16日 10:40

**「背景」** 宣言的保护对象是支撑超级智能（SI）的供应链，即从芯片、算力设施到模型与关键基础设施的整条技术栈；参与国把这条链条上的敏感技术视为经济安全与国家安全交汇的政策着力点。文件以「宣言」而非条约形式发布，五个工作组仅列出职责范围（创新政策框架、关键领域应用、全栈供应链协作、安全港与供应链安全枢纽、安全与韧性），具体执行机制和时间表尚未公布。

**「影响」** 对在美国、澳大利亚、印度、以色列、日本、韩国、卡塔尔、新加坡、阿联酋和英国运营的 AI 与半导体企业来说，最直接的后果是供应链安全协调进入政府间工作组轨道：五个工作组中的“SI 全栈供应链协作”和“安全港与供应链安全枢纽”将涉及跨境供应与关键设施保护。公开信息目前只列出工作组分工，未公布统一认证、出口管制清单或企业合规时间表，因此相关企业应跟踪工作组产出，而不能假定已出现新的自动适用合规义务。

**标签**: `#AI governance`, `#AI supply chain`, `#geopolitics`, `#technology policy`, `#superintelligence`

---

<a id="item-tech-news-9"></a>
### [亚马逊称 Artex 驱动 AI 代理窃取 API 密钥自我供血](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

亚马逊称，攻击者利用开源渗透测试框架 Artex 驱动 AI 代理，窃取 LiteLLM、Dify 等公网暴露 AI 应用的 API 密钥。密钥经有效性验证后被汇入共享池，用于支付更多大模型调用，形成“自我供血”循环；该活动自 10 月 3 日开始，11 月 5 日被亚马逊诱饵网络 MadPot 截获并阻断。亚马逊以“中等信心”将行动归因于一个中国相关威胁组织，并表示并非所有被列目标都已失陷，已通知可能受影响的 AWS 客户。上述说法来自亚马逊单方披露，现有摘要未提供独立验证或技术细节，实际受影响范围尚不明确。

telegram · zaihuapd · 11月16日 13:00

**「背景」** Artex 是开源代理式 AI 渗透测试框架，MadPot 是亚马逊分布式的诱饵传感器网络；亚马逊称，其记录了 2026 年 10 月 3 日至 11 月 5 日期间由 Artex 代理发往诱饵的请求。LiteLLM、Dify 等公网暴露的 AI 应用会在内部保存上游模型 API 密钥，因此这些密钥成为此类自动化活动可直接搜寻和窃取的目标。

**「对暴露 AI 网关的直接影响」** 对运行 LiteLLM、Dify、One API 等公网可访问 AI 应用的组织来说，这一事件的实际后果是：被盗的模型供应商密钥并非只造成数据泄露，还会被攻击者直接用来支付自身的模型调用费用，账单方仍是密钥的合法持有者。亚马逊称并非所有被列出的目标都已失陷，并已通知可能受影响的 AWS 客户；因此这些应用的运维方应将对外暴露的模型密钥视为可能已泄露，检查异常调用量与费用突增，收紧密钥权限并轮换凭据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/">Amazon Threat Intelligence observes threat actors running ...</a></li>
<li><a href="https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/">AI credential theft campaign used stolen API keys to scale</a></li>
<li><a href="https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html">Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify ...</a></li>
<li><a href="https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html">Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#cybersecurity`, `#API keys`, `#cloud security`, `#threat intelligence`

---

<a id="item-tech-news-10"></a>
### [美国拟将 AI 芯片出口管制延伸至远程访问](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 7.0/10

据科技资讯账号转述，美国商务部于 11 月 16 日发布一项临时最终规则，把先进 AI 芯片与服务器的出口管制范围延伸到远程访问，目标是阻止通过第三国数据中心远程调用算力来规避限制。转述还援引 The Verge 称，新规要求向印尼、马来西亚、新加坡、泰国和巴西再出口 AI 芯片时须申请许可，并称规则由财政部和国家安全委员会主导起草。上述内容来自一条简短聚合帖，引用的是二手来源，所附路透社链接的日期也晚于当前时间，因此规则的具体条文、生效时间与适用范围尚待美国工业与安全局（BIS）原文核实。

telegram · zaihuapd · 11月16日 14:44

**「背景」** 美国原有的先进 AI 芯片出口管制针对实物出口与再出口，但企业仍可通过设在第三国的数据中心远程调用算力，形成规避空间。美国工业与安全局（BIS）在 11 月 16 日的临时最终规则中明确要处理对先进“超级智能”（SI）芯片和服务器的远程访问，并将印尼、马来西亚、新加坡、巴西和泰国列为存在“不可接受的转用风险”的国家。

**「对云服务商与海外算力租用的直接影响」** 最直接受影响的是在印尼、马来西亚、新加坡、泰国和巴西等地提供 AI 算力或转口服务器的运营商：向受限方再出口先进 AI 芯片需先申请许可，这意味着相关云服务和托管业务在签约前要先做终端用户与用途核查，否则可能触及管制红线。此前已有报道称中国 AI 企业通过在海外租用英伟达算力绕开限制，远程访问被纳入管制后，这类“算力在境外、调用在境内”的模式不再处于灰色地带，依赖海外集群训练或推理的团队需要评估现有合约是否仍可执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China&#x27;s Access To Advanced Chips Via Singapore ...</a></li>
<li><a href="https://reason.com/2026/11/16/trumps-new-chip-export-rule-targets-china-but-exempts-tiktoks-parent-company/">Trump’s new chip export rule exempts TikTok’s parent company</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>
<li><a href="https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/">US to curb China&#x27;s access to AI chips as Trump heads to Asia</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#US policy`, `#semiconductors`, `#remote access`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国商务部长卢特尼克因英伟达相关往来面临利益冲突质疑](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

CNBC 报道，美国商务部长霍华德·卢特尼克因其子经营的坎托·菲茨杰拉德与英伟达的往来，在英伟达对华芯片出口管制审查中面临利益冲突质疑；证券文件显示，该行申报的英伟达持股（不含期权）从 2025 年 9 月的约 350 万股降至 2026 年 3 月的 178 万股，降幅 49%。坎托称这些申报持仓与客户互换交易有关、单独自营仓位并不重大，报道也称没有证据表明持仓变化与情报警告有关，或该公司的商业利益影响了卢特尼克的决定。

rss · CNBC Finance · 11月16日 12:14

**「背景」** 美国商务部负责执行出口管制，包括拟定限制外国企业获取美国技术的“实体名单”；Lutnick 于 2025 年 2 月离开华尔街投行 Cantor Fitzgerald 出任商务部长，该公司目前由他的儿子 Brandon 和 Kyle 掌管。围绕被怀疑将英伟达先进人工智能芯片转运至中国的新加坡公司 Megaspeed，Lutnick 被指数月来一直抵制收紧限制的努力，而财政部等其它部门此前已支持将该公司列入名单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.firstpost.com/world/bessent-blames-lutnicks-commerce-department-over-delay-in-curbing-nvidia-chip-exports-to-china-14059908.html">Bessent blames Lutnick&#x27;s Commerce Department over delay in ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#U.S.-China tech`, `#export controls`, `#conflict of interest`, `#Commerce Department`

---

<a id="item-finance-news-2"></a>
### [英特尔及 CEO 陈立武遭股东集体诉讼](https://www.investing.com/news/stock-market-news/intel-sued-by-shareholders-following-29-stock-plunge-5028171) ⭐️ 7.0/10

英特尔及其 CEO 陈立武、CFO 津斯纳被股东提起集体诉讼，股东指控公司在 2026 年 7 月 23 日至 10 月 29 日期间隐瞒 PC 需求疲软和库存积压的影响。公司 10 月 29 日发布的第四季度营收和利润预测不及预期，次日股价下跌 28.6%，市值蒸发约 1400 亿美元。

telegram · zaihuapd · 11月16日 11:10

**「背景」** 这起拟议的股东集体诉讼由一家密歇根州养老基金牵头，上周五在圣何塞联邦法院提起，寻求代表 2026 年 7 月 23 日至 10 月 29 日买入英特尔股票的投资者。诉讼指称英特尔未披露 PC 需求疲软和库存积压的影响，并将 CEO 陈立武和 CFO 津斯纳列为被告；诉状未列明具体索赔金额。

**「影响」** 在诉讼所指的 2026 年 7 月 23 日至 10 月 29 日买入英特尔股票的投资者可能成为集体成员，但案件刚提起，索赔结果尚未确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/intel-ceo-lip-bu-tan-named-defendant-class-action-lawsuit-pc-sales-slowdown/">Intel CEO Lip - Bu Tan Named As Defendant In New Class - Action ...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#securities class action`, `#earnings guidance`, `#stock plunge`, `#PC demand`

---