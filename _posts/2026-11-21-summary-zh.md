---
layout: default
title: "Horizon Summary: 2026-11-21 (ZH)"
date: 2026-11-21
lang: zh
---

> 从 40 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [Alpöge 声称与 Claude 证明广义黎曼猜想并给出 Lean 形式化](#item-tech-news-1) ⭐️ 8.0/10
2. [Linux KVM 漏洞致 AMD 宿主机内存可被虚拟机读取](#item-tech-news-2) ⭐️ 8.0/10
3. [Signal 着手限制移动 OS 上的 AI 代理抓取数据](#item-tech-news-3) ⭐️ 7.0/10
4. [Inkling 2 Mini：开放权重与循环 Transformer 的本地测试](#item-tech-news-4) ⭐️ 7.0/10
5. [Aaronson 谈 AI 证明黎曼猜想之说](#item-tech-news-5) ⭐️ 7.0/10
6. [美 SEC 对英伟达的调查据称涉及潜在会计问题](#item-tech-news-6) ⭐️ 7.0/10
7. [GitHub 仓库声称纳维-斯托克斯方程有限时间爆破](#item-tech-news-7) ⭐️ 7.0/10
8. [陶哲轩讨论无外力纳维-斯托克斯奇点与广义黎曼猜想](#item-tech-news-8) ⭐️ 7.0/10
9. [Ravi Vakil 匆忙公布 Masullo 的广义黎曼猜想证明草案](#item-tech-news-9) ⭐️ 7.0/10
10. [台积电暂停对中国企业 16nm 及以下订单](#item-tech-news-10) ⭐️ 7.0/10

**科技博客**
1. [为什么输出缓存难以降低 LLM 成本](#item-tech-blog-1) ⭐️ 6.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Alpöge 声称与 Claude 证明广义黎曼猜想并给出 Lean 形式化](https://alpo.ge/remark.pdf) ⭐️ 8.0/10

Levent Alpöge 在 alpo.ge 发布短文，声称与 Claude 合作发现了黎曼猜想的证明，并表示该方法可直接推广、从而解决广义黎曼猜想（GRH），预计再花时间还能覆盖扩展黎曼猜想；他同时称两人已在 Lean 中「无假设」地完成形式化。这目前仍是作者本人的声明，尚无独立验证。评论者 djoldman 贴出的下载步骤显示该 Lean 工件约 1.3GB、约 1500 万行；另有评论者链接了同日一篇题为「Hurried Announcement: Alessandro Masullo GRH」的博文，称其为完全由人类给出的证明。

hackernews · iamronaldo · 11月20日 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**「背景」** 黎曼假设提出于 1859 年，断言黎曼 ζ 函数的非平凡零点全部位于临界线 Re\(s\)=1/2 上；广义黎曼假设则把这一断言推广到 Dirichlet L 函数等更广泛的一类函数。Levent Alpöge 是数论与算术统计方向的研究者，曾任哈佛学会初级研究员，后加入 Anthropic 担任技术人员。此次声明还称，相关论证已在 Lean 定理证明器中在无额外假设的情况下完成形式化，而形式化检查与数学界对证明本身的同行评审属于两套不同的验证过程。

**「影响」** 对数学界和形式化验证社区而言，最直接的检验路径是让这份 Lean 开发在不引入额外假设的情况下通过编译，而不是逐行审阅上千万行代码；在完成这一步之前，引用该结果时应将其视为未经核实的声明。

**「社区讨论」** 评论者 djoldman 给出了抓取该 Lean 归档的命令，并指出其规模为 1.3GB、约 1500 万行；Jaxan 则补充说另有一份据称完全由人类完成的证明。怀疑一方引用 Terence Tao 一个月前的说法——AI 公司私下投入的时间远超公开程度却仍无法触及黎曼猜想，「需要超越当前 AI 的东西」；synapsomorphy 则更关注此类结果出现的速度，并由此谈到对 AI 治理与暂停的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://www.nacionale.com/en/articles/has-riemann-hypothesis-been-proved-levent-alpoge-claude-anthropic-claim-lean">Riemann hypothesis proof claimed with Claude , unverified</a></li>

</ul>
</details>

**标签**: `#Riemann Hypothesis`, `#Lean`, `#formal verification`, `#AI for mathematics`, `#research claims`

---

<a id="item-tech-news-2"></a>
### [Linux KVM 漏洞致 AMD 宿主机内存可被虚拟机读取](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 8.0/10

Linux 内核 KVM 中的 CVE-2026-99312 允许虚拟机读取宿主机内存，但仅影响启用了嵌套虚拟化的 AMD 主机。研究人员在 DigitalOcean 上从虚拟机内读取到约 127 GB 宿主内存。上游修复已于 11 月 18 日随 7.3.5 等稳定内核发布，而 Debian、Ubuntu 等发行版内核尚未修复；在补丁可用前，可关闭嵌套虚拟化作为缓解措施。

telegram · zaihuapd · 11月20日 14:23

**「背景」** 嵌套虚拟化允许虚拟机内部再运行 hypervisor，因而 AMD 主机上的 KVM 需要额外维护嵌套页表与 MMU 状态。Red Hat 对该 CVE 的说明指出，KVM 在启用嵌套虚拟化时模拟 INIT 处理器重置，却没有正确重置 MMU 上下文；后续分析认为，客机可借此让处理器使用伪造的嵌套页表，从而触及宿主内存。

**「影响」** 在 AMD 主机上启用嵌套虚拟化的虚拟化环境中，虚拟机可能读取宿主机内存；使用尚未修复的 Debian、Ubuntu 发行版内核时，运维方需关闭嵌套虚拟化，或改用已包含上游修复的内核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://access.redhat.com/security/cve/cve-2026-99312">CVE-2026-99312 - Red Hat Customer Portal</a></li>
<li><a href="https://dev.to/etairos/cve-2026-99312-linux-kvm-flaw-let-a-guest-vm-read-127-gb-of-host-memory-on-amd-hosts-4460">CVE-2026-99312: Linux KVM Flaw Let a Guest VM Read 127 GB of ...</a></li>

</ul>
</details>

**标签**: `#KVM`, `#Linux kernel`, `#CVE-2026-99312`, `#AMD virtualization`, `#security vulnerability`

---

<a id="item-tech-news-3"></a>
### [Signal 着手限制移动 OS 上的 AI 代理抓取数据](https://signal.org/blog/protecting-your-privacy/) ⭐️ 7.0/10

据现有信息，Signal 正着手限制移动操作系统平台上的 AI 代理抓取用户数据，目标是收紧 AI 应用对用户数据的访问边界。具体机制、覆盖平台和发布时间尚未披露；因此这目前应视为正在推进的限制措施，而不是已经发布的完整功能。

hackernews · dotcoma · 11月20日 09:42 · [社区讨论](https://news.ycombinator.com/item?id=50572348)

**「背景」** Signal 在博客中称，保护隐私是其使命，因此正在限制移动操作系统内置的最新 AI 代理，避免它们可能捕获和存储 Signal 数据。这里的“内置”指由操作系统本身提供的 AI 代理，而非 Signal 应用内部的独立功能；Signal 针对的正是这类系统级代理接触并留存应用内数据的风险。公开博客未说明涉及哪些操作系统版本、代理名称或具体技术限制方式。

**「社区讨论」** HN 评论中，有人援引 Meredith Whittaker 的访谈称，问题不只在用户自己安装了什么 AI 应用：联系人安装后也可能让 Signal 聊天被读取。另有评论要求 Signal 公开其“取证调查”结果供其他开发者复用，并批评 Windows 端禁止截图和 VPN 下频繁触发验证码给需要隐私保护的用户带来实际障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal &gt;&gt; Blog &gt;&gt; Signal is Serious About Protecting Your Privacy</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI agents`, `#mobile OS`, `#Signal`, `#security`

---

<a id="item-tech-news-4"></a>
### [Inkling 2 Mini：开放权重与循环 Transformer 的本地测试](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

Hacker News 评论者将 Inkling 2 Mini 描述为一个采用循环 Transformer（looped transformer）架构的开放权重小模型，并称其基准表现接近 Qwen3.8-27B；由于原始文章内容缺失，这些说法尚无法由原文或独立结果核实。早期本地测试给出的数字包括：在 Ryzen 395 上通过 llama.cpp Vulkan 解码达到 27 tokens/s，以及在 32GB M1 Pro 上使用 Q4 XL 量化、同时运行浏览器等任务时约 10 tokens/s。一位评论者称简单的 Python CSV 排序任务完成得不错，但“识别硬币类型和年份”的测试在约 12,000 tokens 后放弃；另有评论指出可通过 GGUF 在 Ollama/llama.cpp 中运行。以上均为社区经验，模型的实际基准和兼容性仍需以官方材料核实。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「背景」** Inkling 2 Mini 是 Thinking Machines Lab 发布的开源权重模型；Unsloth 文档将其规模标为 26.4B 参数的 MoE、约 5.4B 激活参数，面向编程、智能体与视觉任务，Artificial Analysis 记录其发布于 2026 年 11 月。评论中所说的“looped transformer”通常指让同一组 Transformer 层循环复用多次，而不是单纯堆叠更多独立层，这也是社区认为其架构值得关注的原因。

**「对本地推理用户的影响」** 对打算本地部署的用户来说，运行路径已经存在（评论提到可用于 Ollama/llama.cpp 的 GGUF 版本），但目前要发挥性能仍需额外操作：一位实测者指出，除了若干尚未合并的 llama.cpp PR（32694、32657、32429、32704）外，还需打一个小补丁才能获得约 30% 的解码提速。同一批评论给出的实测结果为 M1 Pro 32GB 上 q4 量化约 10 tok/s、Ryzen 395 配 llama.cpp Vulkan 约 27 tok/s，说明消费级 CPU 和核显可以运行，但吞吐量有限；这些数字来自社区测试，原文缺失，基准结论仍待验证。

**「社区讨论」** 讨论焦点不只是跑分，而是循环架构是否会成为开放模型的下一波方向；有评论者认为，若该架构确实有效且以开放权重提供，可能带动更多开放模型转向循环设计，但这只是推测。实测报告则褒贬不一：简单编码任务获得好评，复杂的硬币识别任务失败，显示早期基准与真实使用场景之间仍有差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unsloth.ai/docs/models/inkling-2-mini">Inkling 2 Mini - Run Locally Guide | Unsloth Documentation</a></li>
<li><a href="https://artificialanalysis.ai/models/inkling-2-mini">Inkling 2 Mini - Intelligence, Performance &amp; Price... | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#looped transformers`, `#local inference`, `#llama.cpp`, `#model benchmarks`

---

<a id="item-tech-news-5"></a>
### [Aaronson 谈 AI 证明黎曼猜想之说](https://scottaaronson.blog/?p=10344) ⭐️ 7.0/10

Scott Aaronson 的一篇博客文章在 Hacker News 上引发讨论，文章审视了“随机鹦鹉”式 AI 系统似乎证明了黎曼猜想的说法，以及这对“机器理解”意味着什么。现有材料没有提供证明过程、验证结果或具体技术细节，因此无法确认存在数学突破。按目前信息，这更像是一篇关于 AI 认识论、可解释性和数学发现可靠性的评论，而非已确认的证明。

hackernews · stratos123 · 11月20日 20:03 · [社区讨论](https://news.ycombinator.com/item?id=50581084)

**「背景」** “随机鹦鹉”（stochastic parrot）一词源自 2021 年对大型语言模型的批评；此次争议的直接起因是数论学者 Levent Alpöge 声称与 Anthropic 的 Claude 合作得到了黎曼猜想的证明，并且该证明仅以 Lean 代码形式发布（据转述约 1740 万行，发布时尚未经过验证）。随后社交平台上出现“这些所谓的随机鹦鹉证明了黎曼猜想”之类的说法，Aaronson 的博文正是对这一说法作出回应。

**「影响」** 对尝试用 LLM 辅助数学研究的开发者而言，直接后果是必须把模型给出的“证明”当作待验证对象：需要独立检查、形式化验证或专家审阅，而不能因为输出流畅就视为黎曼猜想已被证明。现有讨论也把可解释性问题摆在同等位置——即使计算给出答案，回答“为什么”仍可能是另一回事。

**「社区讨论」** 评论区用国际象棋引擎作类比：Stockfish 的评估看似提供解释，实际是大量计算与 NNUE 评估器的汇总，仍难以回答人们想要的“为什么”。也有评论者担心人类会越来越依赖自己无法理解的结果，并追问若数学家拥有近乎无限算力会带来什么。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scottaaronson.blog/?p=10344">Shtetl-Optimized » Blog Archive » The stochastic parrots have ...</a></li>
<li><a href="https://agihunt.info/en/p/1a1faf3ca85035bde600331be64">Scott Aaronson: Alpöge claims Anthropic models… · AGI Hunt</a></li>
<li><a href="https://www.youtube.com/watch?v=Lrle6EiXqfs">Major happening: AI May Have Proved the Riemann Hypothesis .</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLMs`, `#mathematics`, `#AI epistemology`, `#Hacker News`

---

<a id="item-tech-news-6"></a>
### [美 SEC 对英伟达的调查据称涉及潜在会计问题](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627) ⭐️ 7.0/10

据 MarketScreener 援引未具名消息人士的报道，美国证券交易委员会（SEC）对英伟达的调查正在审查该公司可能存在的会计问题。该报道未说明调查的具体范围、所涉财务期间，也未说明英伟达是否作出回应；目前 SEC 与英伟达均未公开确认这一调查方向。因此，这一说法目前仍属于基于匿名信源的报道，而非已确认的执法结论。

hackernews · ftchd · 11月20日 20:22 · [社区讨论](https://news.ycombinator.com/item?id=50581438)

**「背景」** 路透社援引两名知情人士报道，美国证券交易委员会（SEC）执法人员正在审查 Nvidia 的会计实务，关注的是潜在会计问题；该报道基于匿名消息源。Cryptobriefing 将这项调查描述为民事调查，并称其距 Nvidia 在 2022 年就加密挖矿相关事项达成和解已有数年。

**「社区讨论」** 有评论者将此事与此前围绕英伟达的“循环融资”质疑联系起来，并推测其与 neocloud 客户重新谈判算力采购协议的做法可能影响后续业绩；另一些评论则质疑，董事会若担心存在会计问题，为何让首席财务官 Colette Kress 出任临时 CEO，并推测财务部门难以对相关芯片销售收入不知情。这些均为评论者的推测与观点，未在报道中得到证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/us-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-2026-11-20/">EXCLUSIVE: Nvidia&#x27;s accounting is a focus of US SEC ...</a></li>
<li><a href="https://money.usnews.com/investing/news/articles/2026-11-20/exclusive-us-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say">Exclusive-Nvidia&#x27;s Accounting Is a Focus of US SEC ...</a></li>
<li><a href="https://cryptobriefing.com/sec-probes-nvidia-potential-accounting-issues/">SEC opens civil probe into Nvidia over potential accounting ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#SEC investigation`, `#accounting`, `#AI hardware`, `#tech industry`

---

<a id="item-tech-news-7"></a>
### [GitHub 仓库声称纳维-斯托克斯方程有限时间爆破](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 7.0/10

一个 GitHub 仓库（tristanbuckmaster/navier-stokes）声称给出了纳维-斯托克斯方程的有限时间爆破，并在 Hacker News 上引发集中讨论。所提供的材料只有仓库链接，没有摘要、证明结构或独立验证，因此目前只能将其视为未获确认的数学声明，而不能当作已经成立的结果。对流体力学和计算科学读者而言，该声明是否成立，取决于后续的同行评审与独立核查。

hackernews · trotro · 11月20日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=50576232)

**「背景」** Navier–Stokes 存在性与光滑性问题是千禧年大奖难题之一，核心问题是三维不可压流在光滑初值下是否可能于有限时间失去正则性。2026 年 9 月 8 日，OpenAI 曾提出一个带光滑外力的解法；据维基百科条目，Buckmaster 在 OpenAI 公布前约 12 小时代表自己和 Alpöge 发表了声明。当前仓库对应 Alpöge 与 Buckmaster 的论文《Finite-time blow-up for the Navier–Stokes equations》，包含 79 页论文 PDF 和 Lean 4 形式化包；论文摘要声称，在 R^3 上紧支集光滑数据与 T^3 周期条件下，无外力解会在有限时间爆破，论证依赖区间算术检验的近似自相似 profile 证书。

**「社区讨论」** 评论者把该声明称作“无外力”版本，并与所谓 OpenAI 用精心设计的外力构造反例的说法作对比，认为前者在某种意义上更接近真实情形；也有人希望看到数值模拟直观展示爆破过程。这些比较和背景均来自评论，未在所提供的材料中得到证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy">Navier–Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://hotrepo.ai/tristanbuckmaster/navier-stokes">tristanbuckmaster/navier-stokes: Lean 4 formalization of a ...</a></li>
<li><a href="https://aixiv.online/abs/2611.02204">[2611.02204] Finite-time blow-up for the Navier–Stokes ...</a></li>

</ul>
</details>

**标签**: `#Navier-Stokes`, `#mathematics`, `#fluid dynamics`, `#research`, `#Hacker News`

---

<a id="item-tech-news-8"></a>
### [陶哲轩讨论无外力纳维-斯托克斯奇点与广义黎曼猜想](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 7.0/10

陶哲轩在 2026 年 11 月 20 日的博客文章中讨论无外力纳维-斯托克斯奇点与广义黎曼猜想，文章链接还标出无外力欧拉奇点。条目摘要没有给出具体定理陈述、证明步骤或形式化验证细节，也没有软件版本、API 或基准数据；对技术读者，这是一篇纯数学讨论，而非可直接评估的系统发布。

hackernews · archon1410 · 11月20日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**「背景」** Tao 在 2026 年 10 月 4 日的文章中已讨论 OpenAI 2026 年 9 月 8 日公布的两项主张：带光滑强迫的 Navier–Stokes 爆破解，以及无强迫 Euler 方程从光滑初值出发的爆破解；若在所述假设下得到验证，前者将对应 Millennium 问题允许的 breakdown 情形。当前这篇 11 月 20 日的文章把无强迫 Euler/Navier–Stokes 奇点与广义 Riemann 猜想联系起来，并提到 Levent Alpöge、Tristan Buckmaster、Matei Coiculescu 及大量 AI 辅助；相关报道也提示原文被截断，完整方法与验证仍待确认。同一日，Alpöge 发布的、借助 Claude 得到的约 1700 万行 Lean 代码的 Riemann 猜想证明由 Andrew Sutherland 用两个独立证明检查器 nanoda 和 con-leche 验收，其中 con-leche 还按单独指定的陈述检查了五个最终定理。

**「影响」** 对使用 Lean 等证明助手的研究者，可操作的检查点是形式化陈述是否忠实对应目标定理，以及证明脚本和内核是否经过独立审查；构建通过本身不能替代这一步。

**「社区讨论」** 评论者一方面追问 AI 能否创造新的数学抽象，而不只是用算力和现有概念搜索证明；另一方面有人称两个独立 Lean 内核接受了相关证明，因而内核漏洞利用的可能性较低。另一些人则关注验证的语义缺口：约 1500 万行 Lean 代码构建通过，仍不能保证形式化陈述就是目标命题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">Unforced Euler singularity, unforced Navier-Stokes ...</a></li>
<li><a href="https://terrytao.wordpress.com/2026/10/04/on-classical-solutions-and-singularity-formation-in-incompressible-fluids/">On classical solutions and singularity formation in ...</a></li>
<li><a href="https://todayforai.com/en/items/art-87f06889-96c">Tao Reports AI-Assisted Proofs on Euler and Navier-Stokes ...</a></li>
<li><a href="http://www.rhverify.com/">Verifying a Riemann Hypothesis Formalization in Lean</a></li>
<li><a href="https://www.youtube.com/watch?v=d-ANPBNcTd8">Just in: The Riemann Hypothesis Proof Passed an Independent ...</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#Navier-Stokes`, `#generalized Riemann hypothesis`, `#formal verification`, `#AI for mathematics`

---

<a id="item-tech-news-9"></a>
### [Ravi Vakil 匆忙公布 Masullo 的广义黎曼猜想证明草案](https://simonwillison.net/2026/Nov/20/ravi-vakil/) ⭐️ 7.0/10

Ravi Vakil 于 11 月 20 日在其博客发布「匆忙公告」，称 Alessandro Masullo 已有一份广义黎曼猜想（GRH）的证明草案，Brian Conrad 已仔细审阅数月并给出大量反馈，相关修改正在并入，目前「看起来不错」。Vakil 强调这项工作完全由人类完成、没有使用 AI。原计划是先把 Masullo 请到斯坦福一年打磨写作、并让足够多的人过目后再公布，现在改为直接放出当前草案。该公告本身没有给出论文链接或任何技术细节，证明尚未经过验证。

rss · Simon Willison · 11月20日 19:21

**「背景」** 广义黎曼猜想（GRH）是黎曼猜想的推广，把关于零点分布的结论从黎曼ζ函数扩展到狄利克雷 L 函数，属于数论中长期悬而未决的核心问题之一。据维基百科条目及媒体报道，就在同一天（2026 年 11 月 20 日），数学家 Levent Alpöge 也公布了一份借助 AI 得出、仅以 Lean 代码形式发布的 GRH 证明，Vakil 的这篇公告在数小时后发出。Vakil 在公告中特别强调 Masullo 的工作「完全是人做的，没有用 AI」，这一表述与同日出现的 AI 辅助证明形成对照。

**「影响」** 对关注数论的研究者而言，这意味着要在常规的打磨与圈内传阅流程完成前就面对一份未定稿：公告未附论文链接，判断只能等草案公开后由读者自行审查，而 Vakil 也明确表示原本计划中的一年打磨期被取消。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/dueling-claims-of-riemann-hypothesis-proofs-emerge/">Dueling claims of Riemann hypothesis proofs emerge</a></li>
<li><a href="https://officechai.com/ai/hours-after-alpoges-ai-assisted-riemann-hypothesis-proof-ams-president-ravi-vakil-rushes-out-a-rival-all-human-proof-by-alessandro-masullo/">Hours After Alpöge’s AI-Assisted Riemann Hypothesis Proof ...</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#number-theory`, `#riemann-hypothesis`, `#research-announcement`, `#cryptography`

---

<a id="item-tech-news-10"></a>
### [台积电暂停对中国企业 16nm 及以下订单](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 7.0/10

据 AppleInsider 报道，台积电已通知客户暂停接受中国企业的 16nm 及以下制程订单；按照收紧后的美国半导体出口规定，除非事先取得美国出口许可或豁免，否则不得供货。此前台积电可自行评估客户设计是否满足豁免条件，现在客户须提前申请；美国获批名单包括苹果、AMD 和英伟达，尚无中国公司。台积电表示将遵守新规，受影响的中国企业只能使用 28nm、40nm 等较旧制程，也无法使用 AI 数据中心所需的高带宽内存。

telegram · zaihuapd · 11月21日 02:01

**「背景」** 美国对华半导体出口管制按制程和最终用途设限，16nm 及以下先进制程的供货需事先取得许可或豁免。此前台积电可自行评估客户设计是否符合豁免条件，收紧后的规则改为由客户提前申请；美国获批名单中有苹果、AMD、英伟达，尚无中国公司。

**「影响」** 对依赖台积电 16nm 及以下制程的中国芯片设计公司而言，当前可行的合规路径是逐案申请美国许可或豁免，或将产品转到 28nm、40nm 等成熟制程；原先由台积电自行评估豁免的做法已不再适用。

**标签**: `#TSMC`, `#export controls`, `#semiconductors`, `#AI chips`, `#China`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [为什么输出缓存难以降低 LLM 成本](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月21日 00:00

**「背景」** LLM 推理经济性通常依赖缓存输入（KV cache），以免每轮重算完整对话历史；输出缓存看起来也能省掉代理反复引用代码和证据文档的 token，而输出 token 又因逐个生成而比输入 token 更贵。

**「方案」** 作者先设想一种机制：微调或提示模型用“文件:行号”或对对话历史的引用来代替复述，再由 harness 自动展开，使用户无感。但他指出，这只能优化可见输出。据其自身代理历史的粗略估计，可见输出仅占总输出 token 约 6%，推理 token 约占 50%，工具调用约占 44%。按 Amdahl 定律，即使乐观地省掉可见输出的三分之二，总输出也只减少约 4%。真正的大头是不可见 token，而减少它们更依赖模型智能：更强的模型需要更少推理和工具调用，甚至可能出现单价贵 5 倍、但因 token 少 6 倍而总成本更低的倒挂。作者也承认，自己无法读取前沿模型的思维链，关于其内部很少重复的判断只有中等信心。

**「启示」** 作者的核心结论是，输出缓存并非降低 LLM 代理成本的主要杠杆；与其去重可见输出，不如依靠更聪明的模型（以及更好的 harness）压缩不可见 token，尽管他认为 harness 的长期比较优势有限。

**标签**: `#LLM inference economics`, `#output caching`, `#token costs`, `#agent workflows`, `#Amdahl&\#x27;s law`

---