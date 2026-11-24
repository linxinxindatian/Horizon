---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 38 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [Ladybird 进入 Alpha：独立引擎可安装，但仍有兼容缺口](#item-tech-news-1) ⭐️ 8.0/10
2. [Codex2api 疑似供应链投毒，3.1.10–3.1.12 含后门](#item-tech-news-2) ⭐️ 8.0/10
3. [Arm 要求关闭非官方文档站，站点将于 2026 年 12 月 4 日停运](#item-tech-news-3) ⭐️ 7.0/10
4. [Stalwart 宣称可即插即用替代 Microsoft Exchange](#item-tech-news-4) ⭐️ 7.0/10
5. [Z.ai 发布 GLM-5.4：首个循环 Transformer 编码模型](#item-tech-news-5) ⭐️ 7.0/10
6. [NariQ 发布 Qwen3.8-27B 的 10GB 低比特 GGUF](#item-tech-news-6) ⭐️ 7.0/10
7. [SpaceX 据报向 Anthropic 和 Google 出租算力](#item-tech-news-7) ⭐️ 7.0/10
8. [4.5 万欧盟组织联名促对苹果 iPhone 浏览器限制立案](#item-tech-news-8) ⭐️ 7.0/10
9. [黄循财：新加坡不会成为规避美国芯片管制的通道](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic 称 Claude 发现 VP≠VNP 并公开 Lean 4 证明](#item-tech-news-10) ⭐️ 7.0/10

**科技博客**
1. [vLLM 插件首日支持 ERNIE 5.5 Flash](#item-tech-blog-1) ⭐️ 6.0/10

**财经新闻**
1. [AI 抛售冲击中国 AI 公司上市计划](#item-finance-news-1) ⭐️ 8.0/10
2. [上海地铁将实施 21 年来首次票价调整](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Ladybird 进入 Alpha：独立引擎可安装，但仍有兼容缺口](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

Ladybird 项目发布了首个 Alpha，macOS 和 Linux 用户现在可以直接下载安装，无需自行编译。该项目从零实现独立浏览器引擎，HTML 解析、CSS、布局、JavaScript 和 WebAssembly 大多自研，仅使用 HarfBuzz、Skia、ffmpeg 和 SQLite 等外部组件。官方提醒 Alpha 阶段部分网站无法工作且浏览器会崩溃，用户可从浏览器内报告破站或崩溃。作者实测 ffmpeg、Pyodide 等 WebAssembly 工具可运行，但依赖 Service Worker 的 Datasette Lite 因 startMessages 尚未实现而失败；十月更新还称 Web 平台测试通过数增加 75,650，达到 2,184,722，超过 Safari 但仍低于 Firefox。

hackernews · janvdberg · 11月23日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**「背景」** Ladybird 最初是 SerenityOS 的浏览器组件，后来发展为独立浏览器引擎；它自行实现 HTML 解析、CSS、布局、JavaScript 和 WebAssembly，只复用 HarfBuzz、Skia、ffmpeg、SQLite 等外部基础库。此次 alpha 之前，项目在 2026 年 10 月的更新中已把样式与布局移到独立线程、引入新的 JavaScript JIT 和基于 Cranelift 的 WebAssembly 引擎，并在约 225 万项 web-platform-tests 子测试中超过 Safari。

**「影响」** 对尝试 Alpha 的用户来说，这提供了在真实网站上测试独立引擎并直接提交崩溃或破站报告的入口，但依赖 Service Worker 的 Web 应用目前可能直接失败，因此还不能假定它可以替代日常浏览器。

**「社区讨论」** 多名评论者报告常规网站乃至 Proxmox、NoVNC 渲染正常，其中一人称 NoVNC 比 Firefox 更流畅，但也有人提到页面滚动略有卡顿。另一组讨论关注 Ladybird 改用 SQLite、Skia 等成熟依赖是否牺牲了早期自研的“黑客精神”，并希望项目未来认真处理浏览器指纹识别问题。

**标签**: `#web browsers`, `#browser engines`, `#open source`, `#Ladybird`, `#software engineering`

---

<a id="item-tech-news-2"></a>
### [Codex2api 疑似供应链投毒，3.1.10–3.1.12 含后门](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

据 Telegram 安全投稿，Codex2api 维护者账号被黑后，攻击者绕过 main 分支直接推送 tag，使 3.1.10–3.1.12 的 Release 被构建为带后门版本；其中 v3.1.11 被指移除鉴权，相当于无需密码即可远程执行命令。同一事件中还有 workflow 外传仓库的 16 个 GitHub Actions secrets，据报波及同账号下至少 21 个仓库。该信息来自转述的安全报告，仍以“疑似”表述，并非第一方确认公告。已安装或更新至 3.1.10–3.1.12 的用户被建议立即停用、退回 3.1.9，并轮换 GitHub token、SSH key、数据库和 DeepSeek 等相关密钥。

telegram · zaihuapd · 11月23日 11:21

**「背景」** GitHub 的分支保护通常只约束 main 等分支，不自动覆盖 tag；而 Release 可以直接从 tag 构建，因此只保护主干并不能阻止用新 tag 发布未经审查的代码。GitHub Actions 工作流又能读取仓库 secrets，工作流被改动后，这些凭据可能在构建过程中被外传。

**「影响」** 据该报告，运行过 v3.1.11 的部署应视为主机可能已遭未授权远程命令执行，需在回滚之外进行入侵排查；同账号下使用 GitHub Actions 的仓库因 16 个 secrets 被外传，应轮换对应的 GitHub token、SSH key、数据库和 API 密钥。标签绕过主分支也意味着，仅检查 main 分支代码不足以确认已发布 Release 的安全性。

**标签**: `#supply-chain-security`, `#github-actions`, `#open-source-security`, `#ci-cd`, `#security-advisory`

---

<a id="item-tech-news-3"></a>
### [Arm 要求关闭非官方文档站，站点将于 2026 年 12 月 4 日停运](https://arm.jonpalmisc.com/) ⭐️ 7.0/10

非官方 Arm 文档站点 arm.jonpalmisc.com 宣布将于 2026 年 12 月 4 日停运。站长 jonpalmisc 表示，Arm 以该站托管其文档、使用其商标和知识产权为由要求移除内容，他认为在不影响站点实用性的前提下很难规避。该站此前为开发者提供 Arm 架构文档的在线访问；站长称正考虑镜像、法律咨询，以及在不含 Arm IP 的前提下公开源码等方案，但这些选项尚未落地。

hackernews · tech234a · 11月23日 19:17 · [社区讨论](https://news.ycombinator.com/item?id=50617499)

**「背景」** Arm 官网设有商标使用指南，并要求在使用其标识或版权材料前申请许可；此次涉及的站点并非 Arm 官方文档，而是个人重新托管 Arm 文档的第三方项目。Arm 另外发布机器可读架构规范（MRA），为开发者提供官方规范入口，这与第三方整站镜像的授权边界并不相同。

**「影响」** 依赖该站查阅 Arm 架构文档的开发者将在 2026 年 12 月 4 日后失去这一在线入口，需要转向 Arm 官方文档或其他镜像；替代站点或生成工具能否出现仍不确定，因为站长仅表示会研究相关方案。

**「社区讨论」** 评论者质疑 Arm 以商标和 IP 为由要求下架是否合理，有人认为公开售卖的硬件应当可以被文档化，并有评论者指出 Arm 的机器可读架构规范采用 BSD 风格许可。也有人将该站与斯坦福托管的类似页面比较，追问内容是否由同一类转换工具生成；另有评论批评这一法务决定给真正为 Arm 生态提供价值的开发者增加了障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.arm.com/company/policies/trademarks/guidelines-trademarks">Trademark use guidelines – Arm®</a></li>
<li><a href="https://www.arm.com/company/policies/trademarks">Trademarks – Arm®</a></li>
<li><a href="https://alastairreid.github.io/dissecting-ARM-MRA/">Dissecting ARM &#x27;s Machine Readable Specification – Alastair Reid...</a></li>

</ul>
</details>

**标签**: `#ARM`, `#documentation`, `#trademark/IP`, `#hardware`, `#legal takedown`

---

<a id="item-tech-news-4"></a>
### [Stalwart 宣称可即插即用替代 Microsoft Exchange](https://stalw.art/blog/microsoft-exchange-replacement/) ⭐️ 7.0/10

开源邮件服务器 Stalwart 在博客中宣称可成为 Microsoft Exchange 的即插即用替代品，目标是让组织在自托管环境中继续使用现有邮件客户端和工作流。该说法目前只是项目方的兼容性主张，所给材料没有说明具体支持哪些 Exchange/Outlook 版本、迁移路径或可用时间表。对考虑替代 Exchange 的团队来说，这仍是一个需要自行验证兼容性与合规要求的候选方案，而不是已获独立确认的成品能力。

hackernews · shaunpud · 11月23日 22:32 · [社区讨论](https://news.ycombinator.com/item?id=50620349)

**「背景」** Exchange 长期是企业邮件服务器的代名词，Outlook 则是最常见的客户端；对已经深度使用 Microsoft 365 与 Outlook/MAPI 日历集成的组织来说，迁移门槛主要来自协议和客户端生态。Stalwart 本身是用 Rust 编写的邮件与协作服务器，支持 JMAP、IMAP、SMTP、CalDAV、CardDAV 和 WebDAV；此次兼容性主张随 1.2.0 版本发布提出。

**「迁移前需验证兼容性与归档」** 对计划用 Stalwart 替换本地 Exchange 的组织来说，迁移前应把 Outlook/MAPI 兼容性和邮件归档列为验收项：评论指出，德国 GoBD 要求邮件最长十年内不可篡改留存，而 Stalwart 的常规/开源版本不含该能力，需另配归档系统。Stalwart 自身也把 Exchange 2016/2019 已停止支持、Outlook 逐步转向 Exchange Online 列为迁移背景，因此“直接替换”不能替代客户端与合规测试。

**「社区讨论」** 评论者对“即插即用”说法看法不一：有德国从业者指出，GoBD 要求邮件不可篡改归档并供税务部门访问最长 10 年，而 Stalwart 的常规方案或开源版本不含该功能；也有人以 Outlook 将只支持云端 Exchange 的说法为前提，质疑 Stalwart 如何承接现有客户端，并指出 MAPI/Outlook 集成仍是难点。还有评论认为，支持 MAPI 等微软协议虽能降低授权成本，却可能固化客户端锁定并削弱开放邮件生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stalw.art/blog/microsoft-exchange-replacement/">Stalwart is now a drop - in replacement for Microsoft Exchange</a></li>
<li><a href="https://senn-tech.com/en/blog/mail-stalwart-axigen-vs-exchange">Mail without Exchange : Stalwart with ActiveSync · senn-tech</a></li>
<li><a href="https://hub.docker.com/r/stalwartlabs/stalwart">stalwartlabs/ stalwart - Docker Image</a></li>
<li><a href="https://stalw.art/blog/microsoft-exchange-replacement/">Stalwart is now a drop-in replacement for Microsoft Exchange | Stalwart</a></li>

</ul>
</details>

**标签**: `#open-source email`, `#Microsoft Exchange`, `#mail servers`, `#interoperability`, `#self-hosting`

---

<a id="item-tech-news-5"></a>
### [Z.ai 发布 GLM-5.4：首个循环 Transformer 编码模型](https://z.ai/blog/glm-5.4) ⭐️ 7.0/10

Z.ai 发布 GLM-5.4，称这是其首个循环 Transformer 模型，面向通用编码：一组共享权重的层在一次前向传播中会迭代多次，从而在不增加参数量的情况下加深网络。该模型目前未开放权重，也不能通过常规 API 套餐直接调用；用户需要订阅 Coding Plan，其 API 密钥可在 \`https://api.z.ai/api/v1\` 的 OpenAI 兼容 Responses API 上访问新模型。Simon Willison 用该接口生成了低、高、最高三档“骑自行车鹈鹕”测试图，认为 GLM-5.4 与 GLM-5.3 质量相近，且这两代风格已明显不同于 GLM-5.1/5.2；这属于个人试用手感，而非基准评测。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「背景」** 传统 Transformer 的每一层在一次前向传播中只执行一次；所谓循环 Transformer 则让一组共享权重的层反复运行，在多次迭代中细化隐藏状态，从而在不增加参数量的情况下加深有效网络。就在 11 月 20 日，Thinking Machines Lab 的 Inkling 2 Mini 也采用了循环 Transformer，并称其中间层会对每个 token 运行三次，以提升推理和智能体编程任务的表现。

**「接入与部署影响」** GLM-5.4 目前未开放权重，且常规 API 与 OpenRouter 均不提供该模型，开发者必须先订阅 Z.ai 的 Coding Plan 才能调用；希望自托管的团队暂时没有可用路径。该套餐签发的密钥可直接用于 Z.ai 的 OpenAI 兼容 Responses API，已有 OpenAI 兼容客户端只需调整 base URL 和密钥即可接入，但这也把试用与计费绑定在订阅套餐上，厂商所称的 2T-3T 级能力仍需自行验证。

**「社区讨论」** 评论中，有人赞赏 Z.ai 公开了较多技术细节，认为循环 Transformer 是明显方向，但仍有问题待解决；也有用户抱怨部分中国模型在简单任务上仍长时间反复思考，导致完成时间明显长于前沿模型。另有评论把循环结构解释为减少层权重在 HBM 与芯片之间搬移、缓解推理内存带宽瓶颈的办法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM-5.4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.datacamp.com/blog/glm-5-4">GLM-5.4: Z.ai&#x27;s First Loop Transformer and the Push Toward ...</a></li>

</ul>
</details>

**标签**: `#GLM-5.4`, `#loop transformer`, `#coding models`, `#LLM architecture`, `#model release`

---

<a id="item-tech-news-6"></a>
### [NariQ 发布 Qwen3.8-27B 的 10GB 低比特 GGUF](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 7.0/10

NariQ 在 Hugging Face 发布 Qwen3.8-27B 的 GGUF 低比特量化，提供 3-bit、2.5-bit 和 2-bit 档，宣称能以 10GB 文件在 agentic、数学、多语言和图像任务上接近 BF16 质量。团队称这是首个在长程 agentic 任务上保持 BF16 水平表现的 3-bit 或更低量化；其自报的 BF16/3-bit/2.5-bit/2-bit 得分为 DeepSWE 39.8/41.0/41.9/28.6、Terminal-Bench 2.1 62.6/63.8/60.2/52.4、AIME 25+26 97.7/98.3/96.5/86.0。在 RTX PRO 6000 上，3-bit/2.5-bit/2-bit 的 4K 解码速度为 88.9/99.2/111.7 tok/s、64K 为 70.7/77.5/85.0 tok/s，3-bit 略低于 Unsloth UD-IQ3\_XXS 的 94.7/74.8，且 2-bit 在 DeepSWE、Terminal-Bench 和 AIME 上明显掉点。运行这些量化目前需要 Nari Labs 的 nari-llama.cpp 分支，而不是直接使用上游 llama.cpp。

hackernews · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

**「背景」** GGUF 是 llama.cpp 生态常用的模型格式，低比特量化通过降低权重精度来压缩文件与显存占用，BF16 则是通常用来对照的 16 位浮点基线。NariQ 所量化的 Qwen3.8-27B 是 Qwen 的开放权重稠密视觉语言模型；据第三方模型页记录，它于 2026 年 8 月发布，并支持 262K token 上下文。

**「影响」** 对现有 llama.cpp 部署，这些文件目前不能直接替换：必须改用 nari-llama.cpp 分支，增加构建和后续升级的维护成本。对 agent 等可靠性敏感负载，2-bit 在 DeepSWE、Terminal-Bench 和 AIME 上的明显回退意味着应优先选用 3-bit 或 2.5-bit。

**「社区讨论」** rao-v 认为这类高算力量化容易对基准过拟合，但肯定该项目使用留出集并覆盖多种长程任务；WithinReason 则称从图表看多数提升来自测试框架差异，Retro\_Dev 追问低比特到底丢失了哪些信息。jedbrooke 报告在 18GB M3 Pro 上 3.0bpw 文件约 3.8 tok/s、2.0bpw 约 4.9 tok/s，远慢于 CUDA，并希望能放进 16GB Mac。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/qwen/qwen3.8-27b">Qwen 3 . 8 27 B - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://llm-stats.com/models/qwen3.8-27b">Qwen 3 . 8 - 27 B Benchmarks, Pricing &amp; Context Window</a></li>
<li><a href="https://lmstudio.ai/models/qwen/qwen3.8-27b">qwen/ qwen 3 . 8 - 27 b • LM Studio</a></li>

</ul>
</details>

**标签**: `#quantization`, `#LLM inference`, `#GGUF`, `#Qwen`, `#benchmarking`

---

<a id="item-tech-news-7"></a>
### [SpaceX 据报向 Anthropic 和 Google 出租算力](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html) ⭐️ 7.0/10

据《纽约时报》11 月 23 日报道，SpaceX 自今年 5 月起每月从其数据中心向 Anthropic、Google 等公司出租 AI 算力，月收入达数十亿美元；相关数字来自报道援引的三名知情人士。报道还称，马斯克向员工表示 SpaceX 在 AI 上落后，出租算力比自用更赚钱，并在 8 月一度将部门群聊改名为“Sell compute because we can&\#x27;t compete”。他还警告，浪费 GPU 的员工将被要求离开。

telegram · zaihuapd · 11月24日 02:06

**「背景」** 据 Fortune 2026 年 7 月报道，SpaceX 当时已在悄然建立 AI 算力租赁业务，与 Google、Anthropic 等客户的交易据称每年可带来 260 亿美元收入；雅虎财经 2026 年 10 月又报道，Anthropic 可能在 SpaceX 算力上花费最高 845 亿美元。也就是说，向外部公司出租数据中心容量在马斯克此次内部表态前已是 SpaceX 的一项业务，《纽约时报》11 月 23 日的报道补充的是马斯克对自研 AI 竞争力的判断及该业务的内部优先级。

**「对 SpaceX 自身 AI 进度的牵制」** 《纽约时报》同一篇报道指出，把数据中心算力出租给 Anthropic 等竞争对手，正在让 SpaceX 自己的 AI 工作更难推进：已经对外承诺的 GPU 容量无法同时用于内部训练。与之相应，马斯克警告浪费 GPU 的员工将被要求离开，说明算力分配已成为公司内部的硬性约束，而非可以随意扩大的资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/07/19/spacex-ai-compute-renting-business-google-anthropic-pentagon-deals-revenue-valuation-elon-musk-colossus-data-centers/">SpaceX is quietly building an AI compute business that may ...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/spacex-bags-massive-ai-compute-133405035.html?fr=sycsrp_catchall">SpaceX Bags Massive AI Compute Deal With Anthropic. What That ...</a></li>
<li><a href="https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html">Elon Musk Faces an A . I . Dilemma at SpaceX - The New York Times</a></li>

</ul>
</details>

**标签**: `#AI compute`, `#SpaceX`, `#Anthropic`, `#Google`, `#data centers`

---

<a id="item-tech-news-8"></a>
### [4.5 万欧盟组织联名促对苹果 iPhone 浏览器限制立案](https://appleinsider.com/articles/26/11/23/eu-urges-to-challenge-apples-grip-on-iphone-browsers?utm_source=rss) ⭐️ 7.0/10

一个联名阵营已致信欧盟委员会，要求对苹果在 iPhone 上的浏览器限制正式立案；联署方包括 Mozilla 和 Shopify，并称合计代表约 4.5 万至 5.5 万家欧盟企业组织，签名征集持续至 2026 年 12 月 3 日。信方称，苹果虽依《数字市场法》允许欧盟竞品浏览器使用自有引擎，但现有技术和法律要求使厂商无法把既有欧盟用户迁出 WebKit，企业仍需依赖 App Store 触达用户。联名方测算，若半数原生 iOS 应用转向 Web，欧盟企业每年可节省 110 亿欧元开发成本和 13 亿欧元 App Store 费用；这是联名方的主张，并非监管机构核定结果。

telegram · zaihuapd · 11月24日 03:02

**「背景」** 欧盟《数字市场法》（DMA）要求苹果在欧盟范围内允许第三方应用商店和非 WebKit 浏览器引擎。苹果于 2024 年 3 月正式落实这一要求，并在 iOS 17.4 中从技术上允许竞品浏览器使用自有引擎。

**「开发者仍受制于 WebKit 与 App Store」** 对在欧盟分发 iOS 应用的开发者来说，即便《数字市场法》已允许竞品浏览器使用自有引擎，现有用户仍难迁出 WebKit，触达用户也仍依赖 App Store，这是联名信要求立案的直接理由。联名方还测算，若半数原生 iOS 应用转为 Web 应用，欧盟企业每年可节省 110 亿欧元开发成本和 13 亿欧元 App Store 费用；该数字是联名方的估算，并非已经实现的节省。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gigadgets.com/2025/07/15/apples-browser-choice-on-ios-is-an-illusion/">Apple &#x27;s Browser &quot;Choice&quot; on iOS Is an Illusion</a></li>
<li><a href="https://reclaimthenet.org/apple-browser-competition-eu-dma-owa-accusations">Apple Accused of Blocking Browser Competition on iOS in EU</a></li>
<li><a href="https://www.macrumors.com/">MacRumors: Apple News and Rumors</a></li>

</ul>
</details>

**标签**: `#Apple`, `#EU DMA`, `#browser competition`, `#WebKit`, `#platform regulation`

---

<a id="item-tech-news-9"></a>
### [黄循财：新加坡不会成为规避美国芯片管制的通道](https://www.bloomberg.com/news/articles/2026-11-24/singapore-won-t-be-conduit-to-skirt-us-chip-curbs-wong-says) ⭐️ 7.0/10

新加坡总理黄循财表示，新加坡不会被用作企业规避美国芯片出口管制的通道。当局正在调查 Megaspeed 采购英伟达芯片的交易。此前一天，美国商务部将 Megaspeed 及另外六家东南亚企业列入贸易黑名单，称这些实体存在向未获授权用户转移先进计算产品的“重大风险”，名单还包括其在马来西亚和泰国的关联实体。路透社报道，阿里巴巴新加坡子公司 Apex Enterprise Solutions 也在名单中；阿里巴巴称从未转移受管制的先进计算芯片。

telegram · zaihuapd · 11月24日 05:03

**「背景」** 这轮风波在此前已经发酵：Megaspeed 是一家总部位于新加坡、因采购英伟达先进 AI 芯片而受美方审视的公司；11 月中旬，美国财政部长贝森特公开将商务部未及时把该公司列入黑名单归咎于该部门，相关拖延受到批评。此后，美国商务部将 Megaspeed 及多家东南亚关联实体列入实体清单，黄循财的表态就发生在这一执法行动之后。

**「直接影响」** 对于在新加坡和东南亚经手英伟达等先进计算芯片的企业来说，直接影响是它们需要更严格地核验并记录最终用户和最终用途；被列入黑名单的 Megaspeed 及六家东南亚企业面临美国出口限制，阿里巴巴的新加坡子公司也须应对名单带来的合规压力。

<details><summary>参考链接</summary>
<ul>
<li>Bessent Blames Commerce for Nvidia Export-Control Delay | Zeniteq</li>
<li>Lutnick faces pressure over Nvidia spy scandal and delayed Megaspeed ...</li>

</ul>
</details>

**标签**: `#export controls`, `#AI chips`, `#Nvidia`, `#Singapore`, `#semiconductor industry`

---

<a id="item-tech-news-10"></a>
### [Anthropic 称 Claude 发现 VP≠VNP 并公开 Lean 4 证明](https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md) ⭐️ 7.0/10

Anthropic 于 11 月 24 日公开《VP ≠ VNP over every field》论文及 Lean 4 形式化证明，称结果由内部研究用 Claude 发现，论文与代码也由 AI 撰写。论文给出哈密顿圈多项式的超多项式算术电路下界，并据此推出 VP 是 VNP 的真子类；该结果若成立将解决 Valiant 1979 年的代数复杂度猜想，但只涉及算术电路，不涉及 P 与 NP。仓库称经三条标准公理审计和独立内核 nanoda 复核后，除预留文件外没有 sorry。不过尚无人类数学家通读，Lean 也无法确认形式化陈述与标题命题一致，附录 Q 列出出入，结果仍有待独立审阅。

telegram · zaihuapd · 11月24日 06:02

**「背景」** VP 与 VNP 是算术电路模型下的复杂度类，被视为布尔复杂度 P 与 NP 的代数类比；Valiant 在 1979 年提出，能否证明某些显式多项式（如永久式相对行列式）本质上难以计算。它与 P 与 NP 问题相互关联但并不等同。

**「对研究者的影响」** 对代数复杂度研究者来说，目前能核验的只是 Lean 内核接受了某个形式陈述的证明，而这并不等于 VP≠VNP 已被证明；因此短期内任何引用都应把它标注为未经独立人类审阅的 AI 自报结果。据 alphaXiv 摘要，该下界针对哈密顿圈多项式，并在特征 2 以外的域上也针对永久式，所以在通读论文并核对附录 Q 所列形式陈述与标题命题的出入之前，不应把结论直接用于后续推导或教学材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.proofatlas.ai/collaboration/vp-versus-vnp-permanent-vs-determinant/">VP versus VNP — Permanent versus Determinant | ProofAtlas</a></li>
<li><a href="https://www.alphaxiv.org/abs/2611.vp-vnp-arithmetic-lower-bounds">VP VNP Over Every Field | alphaXiv</a></li>
<li><a href="https://www.alphaxiv.org/abs/2611.vp-vnp-arithmetic-lower-bounds">VP VNP Over Every Field | alphaXiv</a></li>
<li><a href="https://www.youtube.com/watch?v=UuOiRi9T-9c">Claude&#x27;s VP VNP Proof: 47 Years Open, Still Unchecked... - YouTube</a></li>

</ul>
</details>

**标签**: `#complexity theory`, `#Lean 4`, `#formal verification`, `#AI for mathematics`, `#algebraic complexity`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM 插件首日支持 ERNIE 5.5 Flash](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview) ⭐️ 6.0/10

rss · vLLM Blog · 11月24日 00:00

**「背景」** ERNIE 5.5 Flash Preview 是 280B 总参数、每 token 激活 14B 的稀疏 MoE 模型，支持 100 万 token 上下文、思考与工具调用。作者指出，过去让这类新模型在发布日进入 vLLM，往往要维护分支、构建专用镜像或等待 nightly wheel。

**「方案」** 作者介绍的方案是独立插件 vLLM-ERNIE：在与官方 vllm==0.32.0 同一环境安装后，vLLM 通过 vllm.general\_plugins 入口自动注册模型架构、配置、分词器和解析器；插件只提供 ERNIE 模型代码与内核优化，注意力、KV 缓存、投机解码、并行和服务端能力仍来自 vLLM 核心，其他模型不受影响。针对新结构，作者将 VHA 跨头混合、Multi-Router Latent MoE、MultiMax 输出头和门控注意力等做成融合内核，并预折叠可静态计算的权重，称单内核比朴素实现快 1.55×–6.53×；FlashIndexer 通过动态头路由和阈值预过滤降低稀疏索引成本，在 1M 上下文下报告约 1.4×（40%）加速。模型默认将路由专家存为 MXFP4（W4A8，经量化感知训练）、其余权重 FP8，KV 缓存 FP8；随权重发布的 3 层 DSpark 草稿模型每步最多提出 7 个 token，作者称在真实编码和智能体负载上平均接受长度超过 4.0。部署还支持注意力张量并行、专家并行、PD 分离和 KV 卸载。

**「启示」** 作者的核心论点是：把模型特定代码放在独立 vLLM 插件中，可以在不维护分支、不等待上游发版的情况下实现发布日支持，同时继续继承核心调度与并行能力。不过，文中加速与接受长度数据均为厂商自述，缺少独立基准与权衡分析，读者应将其视为部署方向而非已验证的普适结论。

**标签**: `#vLLM plugins`, `#mixture-of-experts`, `#kernel fusion`, `#quantization`, `#speculative decoding`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [AI 抛售冲击中国 AI 公司上市计划](https://www.bloomberg.com/news/articles/2026-11-23/china-s-next-ai-deals-clouded-by-selloff-after-anthropic-ipo) ⭐️ 8.0/10

在 Anthropic 完成创纪录的 1195 亿美元 IPO 后，全球 AI 股加速下跌；这给 DeepSeek、月之暗面和阶跃星辰正在筹备或考虑的上市计划增添了不确定性。中国科技股自 6 月底以来市值累计蒸发 1.7 万亿美元。

telegram · zaihuapd · 11月23日 09:31

**「背景」** Anthropic 于 11 月 19 日完成首次公开募股（IPO），募资 1195 亿美元，创下纪录；其股价首日上涨 17%，次日即下跌 8.5%，这轮抛售随后波及全球 AI 股。

**「影响」** 对拟上市公司及其早期投资者而言，已经上市的同行提供了更低的估值参照：智谱较 6 月高点下跌超过 85%（此前半年曾上涨 2000%），MiniMax 本月跌破发行价，这直接影响新一轮 AI 公司上市的定价和融资环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wsws.org/en/articles/2026/11/21/qnyf-n21.html">Anthropic ’s record IPO : Wall Street bets on AI as company warns of...</a></li>

</ul>
</details>

**标签**: `#AI selloff`, `#China tech stocks`, `#IPO market`, `#Anthropic`, `#DeepSeek`

---

<a id="item-finance-news-2"></a>
### [上海地铁将实施 21 年来首次票价调整](https://weibo.com/1699432410/5368461393397183) ⭐️ 7.0/10

上海地铁宣布实施 21 年来首次票价调整，新起乘价为 3 元、起乘间距 0 至 4 公里，新票价自 12 月 1 日起执行。同步推出 190 元至 390 元四档计次票，并对同一支付渠道当月累计满 90 元的乘客给予 9 折优惠，以减轻对高频出行者的影响。

telegram · zaihuapd · 11月23日 10:45

**「背景」** 上海地铁上一轮票价机制已沿用 21 年；据媒体报道，2026 年 9 月的票价听证会上，多数参会者支持“起乘价 3 元不变”的第一套方案。

**「影响」** 高频通勤者可购买 11 月 26 日开售的四档计次票，或使用同一支付渠道当月累计满 90 元后的 9 折优惠，以降低调价带来的支出影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260908A05NH700">news.qq.com/rain/a/20260908A05NH700</a></li>

</ul>
</details>

**标签**: `#上海地铁`, `#公共交通票价`, `#票价调整`, `#计次票`, `#民生政策`

---