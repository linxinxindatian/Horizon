---
layout: default
title: "Horizon Summary: 2026-11-19 (ZH)"
date: 2026-11-19
lang: zh
---

> 从 48 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [谷歌发布 Gemini 4 Neon 模型](#item-tech-news-1) ⭐️ 9.0/10
2. [Nginx HTTP/2 曝未认证 RCE，1.31.9 已修复](#item-tech-news-2) ⭐️ 9.0/10
3. [微软发布七款新 AI 模型，主打性价比](#item-tech-news-3) ⭐️ 7.0/10
4. [Energy-Based Reasoners 宣称推理效率提升 385 倍](#item-tech-news-4) ⭐️ 7.0/10
5. [旅行者 1 号硬件交互拆解网站](#item-tech-news-5) ⭐️ 7.0/10
6. [Quad9 退出法国：DNS 不应成为反盗版封锁点](#item-tech-news-6) ⭐️ 7.0/10
7. [从 4004 到 486：x86 早期架构史](#item-tech-news-7) ⭐️ 7.0/10
8. [curl 维护者质疑 AI 生成的 Rust 重写能否跟上修复](#item-tech-news-8) ⭐️ 7.0/10
9. [微信小微测试扩至 3000 万日活，接入聊天与视频号](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [美联储会议纪要：官员预计需进一步加息，并警示 AI 相关风险](#item-finance-news-1) ⭐️ 8.0/10
2. [美联储理事沃勒：12 月可能需要加息 0.5 个百分点](#item-finance-news-2) ⭐️ 8.0/10
3. [腾讯三季报：营收同比增长 8%低于预期，资本开支 814 亿元、自由现金流为负](#item-finance-news-3) ⭐️ 7.0/10
4. [中韩宣布自贸协定服务与投资后续谈判实质性结束](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [谷歌发布 Gemini 4 Neon 模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 9.0/10

谷歌发布 Gemini 4 Neon，主打复杂软件工程、知识型工作和科研工作流的快速端到端执行，已向开发者、企业以及 Google AI Pro/Ultra 订阅用户开放。其定价为每百万输入 token 3 美元（缓存输入 0.15 美元）、输出 15 美元，支持 100 万 token 上下文。谷歌公布的数据显示，该模型在 Artificial Analysis 编程智能体指数上以 58.6 分居首，在智能指数 xhigh 档以 61 分列第三，Terminal-Bench 4.1 得分 65.2%，默认 high 档单任务成本较 Carbon 低 32%。

hackernews · yigitdemirag · 11月18日 21:34 · [社区讨论](https://news.ycombinator.com/item?id=50552424)

**「背景」** Gemini 4 Neon 的发布背景是 Google 在同一代 Gemini 4 产品线中已有 Carbon 这一参照型号：公告用 Carbon 比较单任务成本，社区讨论则把 Carbon 描述为更偏长程任务的型号。理解 Neon 需要看它在这组型号中的分工，而不只是单看某一项榜单名次。

**「影响」** 对需要把大型代码库或长文档放入上下文的团队，100 万 token 上下文和 0.15 美元/百万 token 的缓存输入价格会直接影响其批量调用成本；输出按 15 美元/百万 token 计费，意味着生成量大的任务仍需控制输出长度。

**「社区讨论」** 评论者最集中的抱怨是模型命名越来越难与实际用途对应，认为 Google、Anthropic 和 OpenAI 的新名称增加了选型负担。也有开发者称 Neon 在 OpenRouter 上约 127 token/s、快于 Carbon 的 46 token/s，并指出 Carbon 仍被定位为长程模型、在 CritPt 等研究型评测上更强，因此应按任务而非总榜分数选型。

**标签**: `#Google Gemini`, `#LLM release`, `#generative AI`, `#AI benchmarks`, `#model positioning`

---

<a id="item-tech-news-2"></a>
### [Nginx HTTP/2 曝未认证 RCE，1.31.9 已修复](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) ⭐️ 9.0/10

Xint 披露了 nginx 的五个漏洞，其中最严重的 CVE-2026-123007 是 HTTP/2 流控中的内存破坏，未认证攻击者可在启用 HTTP/2 的服务器上以 worker 进程权限执行命令。nginx 于 11 月 18 日发布 1.30.7 与 1.31.9，共修复 10 个 CVE；Rapid7 已放出 PoC，但暂无在野利用的报告。Xint 同时报告了一个自 Linux 4.15 引入、位于 SCTP 子系统的本地提权内核漏洞，与 nginx 漏洞串联后可在容器部署中取得宿主机 root，该内核补丁尚未发布。HTTP/2 在 nginx 中默认未启用。

hackernews · speedping · 11月18日 15:19 · [社区讨论](https://news.ycombinator.com/item?id=50547374)

**「背景」** NGINX 的 HTTP/2 支持需要在 server 配置中显式开启，并非默认启用；该协议的二进制帧和流量控制机制让 worker 进程直接处理未经认证的客户端输入。SCTP 是 Linux 内核中的一个传输协议模块，许多发行版会在程序首次打开 SCTP socket 时自动加载它，这为本地提权链提供了入口。

**「影响与处置」** 运维方应升级到 1.31.9（或 1.30.7），无法立即升级时需关闭对外 HTTP/2；对不需要 SCTP 的主机应屏蔽该内核模块直至内核修复发布——因为宿主机上的所有容器共享同一内核，容器内的 nginx 一旦被攻破即可波及宿主机和其他容器。

**「社区讨论」** 评论者 black3r 指出，修复提交在公开发布前约一周已进入开源仓库，提交信息还写明由 Xint.io 报告，认为厂商本应更早发布安全公告；userbinator 则把问题归因于 HTTP/2 协议实现复杂度高、攻击面大。另有评论（testtestmetest）称利用需要约 128Gb 的 HTTP/2 流量和特定 CPU 指令，因而视其为非问题，这属于个人判断，与 Xint 的漏洞定级并不一致。

**标签**: `#Nginx`, `#HTTP/2`, `#remote code execution`, `#vulnerability`, `#web server security`

---

<a id="item-tech-news-3"></a>
### [微软发布七款新 AI 模型，主打性价比](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 7.0/10

Microsoft 宣布推出七款新 AI 模型，并以可扩展的性价比作为卖点。现有材料未给出模型名称、参数规模、基准测试、定价、可用时间或开放权重等细节，因此无法核实其实际性能与成本优势。此次发布目前仍属厂商口径，尚待独立评测。

hackernews · gmays · 11月18日 16:08 · [社区讨论](https://news.ycombinator.com/item?id=50548021)

**「背景」** MAI 是微软主推的模型家族；此次 Ignite 2026 发布扩展了这一家族，并同时推出 Maia 200 加速器，以及允许客户获得 MAI 模型权重授权并在自有环境运行的项目。这组信息界定了本次发布的背景：讨论对象不只是模型能力，还包括权重授权和自托管部署选项。

**「对选型的影响」** 对正在挑选编码模型的团队来说，目前可核验的核心依据仍只是微软自己的说法：MAI Code 2 在四项编码基准上达到 Opus 5.5 约 96% 的性能、成本仅为其 5%；而第三方对比文章指出，这个数字“人人引用却无人能独立复核”，且公开的共享基准结果十分有限。因此在把“可扩展的性价比”当作迁移理由之前，应先在自有任务上实测，而不是直接采信厂商口径。

**「社区讨论」** 有 HN 评论者称自己试用了 MAI Code 2，认为其表现大致可与 Opus 或 Sol 相提并论；另一名评论者主张，微软若想赢得市场份额，应开放部分模型的开源或开放权重。也有评论质疑发布会的技术深度以及微软 AI 工程团队的执行力，这些都属于个人体验和观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/microsoft-ignite-2026-mai-keynote/">Microsoft Ignite 2026: MAI keynote transcript | Microsoft AI</a></li>
<li><a href="https://www.linkedin.com/pulse/microsoft-ignite-2026-seven-new-mai-models-chip-your-own-ivana-tilca-hxyef">Microsoft Ignite 2026: Seven New MAI Models, a New Chip, and ...</a></li>
<li><a href="https://www.orcarouter.ai/blog/mai-code-2-vs-claude-opus-5-5">MAI Code 2 vs Claude Opus 5.5: What the 96% Claim Omits</a></li>
<li><a href="https://benchlm.ai/compare/claude-opus-5-5-vs-mai-code-2">Claude Opus 5.5 vs MAI Code 2: Benchmarks &amp; Cost</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#AI models`, `#price-performance`, `#model releases`, `#open weights`

---

<a id="item-tech-news-4"></a>
### [Energy-Based Reasoners 宣称推理效率提升 385 倍](https://energy-based-reasoners.github.io/) ⭐️ 7.0/10

一个名为 Energy-Based Reasoners 的项目页面提出了基于能量模型的推理器，并宣称其推理效率提升 385 倍。该项目面向关注 LLM 替代推理路径的研究者和开发者，但目前可见证据仅为项目页面和演示，尚不是经独立验证的已交付能力，这一数字仍需独立复现。

hackernews · frenchmajesty · 11月18日 09:29 · [社区讨论](https://news.ycombinator.com/item?id=50543989)

**「背景」** 能量模型（EBM）会给某个输入下的候选预测赋予一个标量“能量”，推理时寻找能量更低的候选，而不是像常见 LLM 那样逐个 token 生成文本；讨论中的数独例子就是把冲突和空格作为需要降低能量的状态来处理。此次项目页宣称推理效率达到 385 倍，但页面没有给出可供独立复核的完整训练与规模化结果，评论者的质疑也集中在 EBM 难以训练、以及在数独等约束题之外能否扩展。

**「对约束求解选型的影响」** 对想在约束求解类任务上使用小模型的研究者，项目页给出的直接可行动作是先在 Sudoku-Extreme 上复现其基线：180 万参数模型报告超过 99% 准确率，并在同等准确率下比 EqR 减少最多 345 倍推理 FLOPs。由于站点标题写作 385 倍而项目页写作 345 倍，且公开数据集中在 Sudoku-Extreme，选型时应先对齐准确率与参数规模再比较成本，不能把这一加速直接外推到通用 LLM 推理。

**「社区讨论」** 有评论者推荐关注由 Yann LeCun 等担任主席的 Logical Intelligence，认为能量模型在 LLM 不擅长的特定任务上有潜力；但一位自称研究能量模型一年的评论者认为其训练极难、场景狭窄，Sudoku 求解器难以扩展。另有评论者指出，该方法目前主要适用于特定逻辑谜题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://energy-based-reasoners.github.io/">Energy-Based Reasoners: Your Recurrent Reasoner Should Be an ...</a></li>
<li><a href="https://www.nahraf.tech/blog/energy-based-reasoners-could-make-current-llms-obsolete">Energy-Based Reasoners: 385x Faster Inference | Nahraf</a></li>

</ul>
</details>

**标签**: `#energy-based models`, `#AI reasoning`, `#inference efficiency`, `#constraint solving`, `#LLM alternatives`

---

<a id="item-tech-news-5"></a>
### [旅行者 1 号硬件交互拆解网站](https://rshekhar.com/voyager/) ⭐️ 7.0/10

开发者 raj-shekhar 在 Hacker News 发布了一个交互式网站，让读者查看旅行者 1 号的核电池、数据计算机、单块存储芯片、金唱片封面和深空网络通信，并附有一段 4 分钟影片。网站还显示两艘旅行者号的当前位置，以及实时接收信号的地球天线；作者称发布时旅行者 1 号距地球达到一光日。作者在评论中补充了核电池、数据计算机存储芯片、命令计算机单个存储位和金唱片封面等页面的直接链接，说明这些内容在站点中不易找到。该作品是教育性可视化项目，并非新发布的航天任务结果或经独立验证的工程资料。

hackernews · raj-shekhar · 11月18日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=50548161)

**「背景」** 一光日指光在真空中行进一天的距离，约 160 亿英里（约 260 亿公里）。Voyager 1 发射近 50 年后，于 2026 年 11 月 18 日抵达这一距地球距离，成为首个达到一光日的人造物体；公开距离数据在同年 10 月为 172.52 AU。

**「社区讨论」** 有评论者称赞可视化，并提到可用来回顾 1970 年代的系统设计，同时指出站点缺少一些内容；也有人追问 CMOS 存储芯片出现持续读取错误的具体物理原因。另有评论者直接询问该项目是否主要由 AI 生成、是否做过原创研究并对照权威资料核查，作者尚未在给定评论中回应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voyager_1">Voyager 1 - Wikipedia</a></li>
<li><a href="https://www.aljazeera.com/news/2026/11/18/nasas-voyager-1-hits-record-one-light-day-distance-50-years-after-launch">NASA’s Voyager 1 hits record one light - day distance , 50... | Al Jazeera</a></li>
<li><a href="https://www.theguardian.com/commentisfree/2026/nov/18/nasa-voyager-1-pale-blue-dot">After 49 years, Nasa’s Voyager 1 is one light - day ... | The Guardian</a></li>

</ul>
</details>

**标签**: `#Voyager 1`, `#interactive visualization`, `#space computing`, `#hardware`, `#technical education`

---

<a id="item-tech-news-6"></a>
### [Quad9 退出法国：DNS 不应成为反盗版封锁点](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 因法国的 DNS 封锁命令退出法国市场，使“用 DNS 解析器打击盗版”成为直接争议点。该事件的关键在于公共递归解析器是否应承担版权封锁职能：批评者认为，这类命令会把基础网络设施变成内容审查关口。现有材料未给出封锁命令的具体范围、生效时间或法国以外的影响，相关细节仍需以 Quad9 公告和相关法律文件为准。

hackernews · ritzaco · 11月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50545958)

**「背景」** DNS 解析器负责把域名转换为 IP 地址，位于用户访问网站的入口，因此常被版权执法方当作屏蔽盗版站点的执行点。据 TorrentFreak 和 CyberInsider 报道，巴黎法院此前裁定 Quad9 必须屏蔽被指传播未经授权体育直播的域名，并因未执行而对其按日处以罚款；这家瑞士非营利机构于 2026 年 10 月宣布，将于 11 月 24 日停止为法国用户提供解析服务，成为第二家因此退出法国的 DNS 解析器。

**「对法国用户的影响」** 法国用户和依赖 Quad9 的组织需在 2026 年 11 月 24 日前改用其他解析器，因为 Quad9 届时将同时停止其常规 DNS 解析和恶意域名过滤服务，安全防护能力随之丧失。据报道，Quad9 是第二家因法国盗版屏蔽令而退出该国的 DNS 解析器，这意味着用户转向的替代公共解析器也可能面临类似的法院命令，迁移时需把这一合规风险纳入考虑。

**「社区讨论」** 评论中，有用户认为除直接起诉盗版者外，其他反盗版手段都容易成为政府压制言论的后门，也有人追问问题应归咎于法官错误解释法律还是立法者制定荒诞法律。另有用户主张，提供无 DRM、按片低价的合法下载体验，比 DNS 封锁更能减少盗版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/">DNS Resolver Quad9 Will Leave France After Court Orders ...</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad9 Is Leaving France: Why DNS Resolvers Are the Wrong ...</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/">DNS Resolver Quad9 Will Leave France After Court Orders ...</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#internet-censorship`, `#piracy`, `#internet-governance`, `#Quad9`

---

<a id="item-tech-news-7"></a>
### [从 4004 到 486：x86 早期架构史](https://pikuma.com/blog/history-of-x86-4004-to-486) ⭐️ 7.0/10

这篇技术历史文章按时间线梳理 Intel 从 4004 到 486 的早期处理器谱系，并把这些芯片与 x86 架构的后续演进联系起来。它面向关心 CPU 架构、计算机历史和复古计算的工程师；这不是产品发布，也没有版本或可用性变化，重点在架构背景而非性能测试。现有材料只提供标题与内容摘要，未包含正文的具体章节和论证细节。

hackernews · ibobev · 11月18日 14:47 · [社区讨论](https://news.ycombinator.com/item?id=50546967)

**「背景：早期 Intel 与 x86 的起点」** Intel 4004 于 1971 年 11 月 15 日发布，是 Intel 早期 CPU 产品线的起点，也是这类历史叙述通常的起点。x86 指令集家族则以 8086 及其 8 位外部总线版本 8088 为基础；因此，从 4004 到 486 讲述的是早期 Intel 微处理器谱系，而 x86 架构本身要从 8086/8088 算起。

**「社区讨论」** 评论者总体上认可文章，但集中纠正若干技术细节：有观点认为，2200 采用小端序最初是为了加快数据访问速度，而非算术运算上的便利；8085 的地址/数据总线复用也并非其独有；Intel 工程师确实修改过 8008 指令集。另有评论者强调，4004 与 8008 除部分人员重合外并无直接继承关系；还有人质疑，现代 PC 为何仍以 1978 年的实模式启动，认为改为长模式或 32 位保护模式只会影响 BIOS 开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intel_4004">Intel 4004 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/X86">x86 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#x86`, `#CPU architecture`, `#Intel`, `#computer history`, `#retrocomputing`

---

<a id="item-tech-news-8"></a>
### [curl 维护者质疑 AI 生成的 Rust 重写能否跟上修复](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

curl 维护者 Daniel Stenberg 在 11 月 17 日的博客中回应 AI 代理生成的 Rust 重写：在这些代理把 185,000 行 C 代码转换成 340,000 行 Rust 代码的同一段略超三周时间里，实际的 curl 项目合并了 300 多个提交，完成 200 多项缺陷修复，并修复了几个漏洞。Stenberg 据此追问，这些克隆版本能否跟上 curl 持续的维护和安全修复；他并未宣布 curl 本身改用 Rust。

rss · Simon Willison · 11月18日 15:58

**「背景」** curl 是以 C 语言开发的数据传输工具和库，Daniel Stenberg 是其维护者；当前讨论的 Rust 版本是 AI 代理自动生成的代码克隆，并非 curl 官方代码库的正式迁移。理解这一区别后，Stenberg 的统计才指向关键问题：克隆代码能否在后续持续跟上上游的缺陷修复和安全更新。

**「影响」** 对考虑采用这类 AI 生成 Rust 克隆的开发者而言，直接后果是克隆代码只是某个时间点的快照：若不能持续吸收上游修复，就会缺少 curl 在这三周多内完成的 200 多项缺陷修复和若干安全修复。评估替代品时应看维护与补丁跟进能力，而不只看生成代码的规模。

**标签**: `#AI coding agents`, `#curl`, `#Rust`, `#open source maintenance`, `#security`

---

<a id="item-tech-news-9"></a>
### [微信小微测试扩至 3000 万日活，接入聊天与视频号](https://mp.weixin.qq.com/s/r3NthxJZQJgztyLADwNV4A) ⭐️ 7.0/10

腾讯在 2026 年第三季度财报中表示，微信 AI 助手“小微”的测试范围已扩大，日活跃用户数达到 3000 万。据该财报，小微正逐步融入微信聊天、朋友圈、公众号和视频号等场景，使用的是针对成本效率优化的 WeLM 定制模型。腾讯称其推理成本较低且持续下降，并预计未来部分推理任务将在用户设备端运行；不过上述均为腾讯的单方面说法，未给出具体成本数据，也未见独立验证，端侧推理尚属计划而非已落地的能力。

telegram · zaihuapd · 11月18日 11:35

**「背景」** 小微是微信内嵌的 AI 助手。Pandaily 2026 年 6 月报道称，微信当时刚开始对小微进行有限测试，并把它作为超级应用 AI 集成的一步；这一早期有限测试阶段，是理解本次测试范围扩大的直接前情。

**「影响」** 小微目前仍处于扩大测试范围阶段，并未全量开放，因此不在测试范围内的用户暂时无法使用。若腾讯计划的端侧推理付诸实施，部分计算将从云端转移到用户手机，但腾讯未披露时间表或支持机型，现阶段也还不能据此评估对时延与耗电的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pandaily.com/wechat-ai-xiaowei-agent-challenge-jun2026">WeChat AI Navigates Super App Challenges as Xiaowei Assistant ...</a></li>

</ul>
</details>

**标签**: `#WeChat`, `#Tencent`, `#AI assistants`, `#on-device inference`, `#LLM deployment`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美联储会议纪要：官员预计需进一步加息，并警示 AI 相关风险](https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html) ⭐️ 8.0/10

美联储 10 月会议纪要显示，多数官员预计仍需进一步加息，以使通胀及时回到 2%目标，但本次会议以 10 票赞成、2 票反对，决定将联邦基金利率目标区间维持在 3.75%-4%，两位反对者主张加息 25 个基点。纪要还指出，人工智能（AI）相关债务增长迅速，融资结构复杂且不透明，可能放大 AI 投资回报不及预期时的损失。

rss · CNBC Finance · 11月18日 19:41

**「背景」** 10 月会议后公布的 CPI 数据显示，10 月整体 CPI 上涨 0.4%，剔除食品和能源的核心 CPI 上涨 0.3%，均比预期高 0.1 个百分点，显示通胀压力仍强。

**标签**: `#Federal Reserve`, `#monetary policy`, `#interest rates`, `#inflation`, `#AI financial risk`

---

<a id="item-finance-news-2"></a>
### [美联储理事沃勒：12 月可能需要加息 0.5 个百分点](https://www.cnbc.com/2026/11/18/federal-reserve-governor-christopher-waller.html) ⭐️ 8.0/10

美联储理事克里斯托弗·沃勒 11 月 18 日表示，联邦公开市场委员会（FOMC）在 12 月 8 日至 9 日的会议上可能需要加息 0.5 个百分点（50 个基点），并称应扭转 2025 年三次各 0.25 个百分点的降息。这是沃勒的个人观点，并非 FOMC 已作出的决定；据 CME Group 的 FedWatch 工具，期货市场目前完全计入 12 月加息 0.25 个百分点。

rss · CNBC Finance · 11月18日 15:13

**「背景」** 美联储在 2025 年因担忧就业市场而降息三次，但今年通胀重新升温，多数通胀读数高于 3%，仍高于美联储 2%的目标。

**标签**: `#Federal Reserve`, `#monetary policy`, `#interest rates`, `#inflation`, `#Christopher Waller`

---

<a id="item-finance-news-3"></a>
### [腾讯三季报：营收同比增长 8%低于预期，资本开支 814 亿元、自由现金流为负](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 7.0/10

腾讯公布的第三季度财报显示，营收为 2073 亿元、同比增长 8%，低于市场预期；归母净利润为 636 亿元、同比仅增 0.8%，当季资本开支 814.33 亿元，远超市场预估的 554 亿元，单季自由现金流为负 691 亿元。公司同时称，其 AI 产品 WorkBuddy 日均 Token（大模型处理文本的计量单位）用量超过 100 万亿，为国内大语言模型日均用量最高的 AI 产品。

telegram · zaihuapd · 11月18日 09:20

**「背景」** 腾讯称，WorkBuddy 于 2026 年 3 月推出，目前日活跃用户超过 1000 万，企业版已覆盖中国 500 强中 50% 的企业。

**「影响」** 对腾讯投资者而言，AI 算力投入激增已开始压制利润增长，并使单季自由现金流降至负 691 亿元，短期财务缓冲随之变薄。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/tencent-workbuddy-hits-10m-daily-active-users-100-trillion-daily-token-usage">Tencent WorkBuddy reaches 10 million daily active ... - KuCoin</a></li>
<li><a href="https://todayforai.com/en/story/story-3620e3af-77d">Tencent WorkBuddy Tops 10M Daily Users With 100 Trillion ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-18/tencent-s-sales-miss-estimates-in-setback-for-founder-s-ai-push">Tencent’s Profit Squeeze Exposes China’s AI Spending Dilemma</a></li>
<li><a href="https://cryptobriefing.com/tencent-negative-free-cash-flow-q3-ai/">Tencent reports negative free cash flow of RMB69.1 billion in ...</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#earnings`, `#AI capex`, `#free cash flow`, `#China tech`

---

<a id="item-finance-news-4"></a>
### [中韩宣布自贸协定服务与投资后续谈判实质性结束](https://x.com/Jaemyung_Lee/status/2122988472994791476) ⭐️ 7.0/10

11 月 18 日，中韩宣布自贸协定服务与投资后续谈判实质性结束。中国承诺在电影、游戏等领域给予韩国最惠国待遇，并扩大旅游、法律、建筑、金融等领域开放；双方同意将视听节目共同制作范围从电影扩大到电视剧、动画、综艺和纪录片。谈判自 2018 年 3 月启动，部分技术事项仍待工作层面协商，因此这还不是最终签署的协定。

telegram · zaihuapd · 11月18日 10:02

**「背景」** 这轮服务与投资后续谈判自 2018 年 3 月启动，属中韩自贸协定框架下的补充谈判，历时约 8 年 8 个月才宣布实质性结束，但尚未正式签署生效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://biz.chosun.com/en/en-policy/2026/11/18/3HXWCB2DJJGY5JHJZMFZGGB3CQ/">South Korea and China reach deal on services and investment ...</a></li>
<li><a href="https://www.reuters.com/world/south-korea-says-china-trade-agreement-boost-tourism-entertainment-sectors-2026-11-18/">South Korea says China trade agreement to boost tourism ...</a></li>

</ul>
</details>

**标签**: `#China-South Korea FTA`, `#services trade`, `#investment liberalization`, `#entertainment industry`, `#trade policy`

---