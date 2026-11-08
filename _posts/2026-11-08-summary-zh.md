---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08
lang: zh
---

> 从 41 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [MaxxBench 检验 DeepSWE 分数是否稳健](#item-tech-news-1) ⭐️ 8.0/10
2. [SemiAnalysis 探访内蒙古 800MW AI 数据中心园区](#item-tech-news-2) ⭐️ 8.0/10
3. [GitHub 推出面向 AI 智能体并发的 Rubicon 存储架构](#item-tech-news-3) ⭐️ 8.0/10
4. [微软研究院 AI Frontiers 团队据报结束，Langford 离职](#item-tech-news-4) ⭐️ 7.0/10
5. [Claude Code 本地设置被指致 1,122 个公开文件泄露密码](#item-tech-news-5) ⭐️ 7.0/10
6. [Coldframe：伪装超市制冷控制器的蜜罐](#item-tech-news-6) ⭐️ 7.0/10
7. [Asahi Linux 7.3 进展：代码转 GPLv2 并同步 Fedora 45](#item-tech-news-7) ⭐️ 7.0/10
8. [分析称 macOS 暗藏构建个人关系图谱的守护进程](#item-tech-news-8) ⭐️ 7.0/10
9. [Amutable OS 技术概览：无 shell、无 SSH 的镜像化 Linux](#item-tech-news-9) ⭐️ 7.0/10
10. [Claude Code 被指联网请求泄露登录邮箱](#item-tech-news-10) ⭐️ 7.0/10
11. [苹果披露 HALO 人形机器人系统，采用双 Qwen 模型](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [软银与 ABB 考虑分拆中国业务，以挽救被叫停的 54 亿美元机器人收购](#item-finance-news-1) ⭐️ 8.0/10
2. [伯克希尔第三季度回购翻倍至 96 亿美元，经营利润下降 5.8%](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [MaxxBench 检验 DeepSWE 分数是否稳健](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 8.0/10

MaxxBench 发布了一项针对 DeepSWE 基准的分析，通过改变任务规格来检验模型分数是否随之大幅波动。该分析指出 DeepSWE 存在若干基准 bug，并讨论了任务规格敏感性和模型规模对结果的影响；核心问题是，漂亮的 DeepSWE 分数是否真实、能否泛化。上述结论来自 MaxxBench 的测试与分析，而非独立第三方复现。

hackernews · antiuniverse · 11月7日 17:19 · [社区讨论](https://news.ycombinator.com/item?id=50406222)

**「背景」** DeepSWE 是一个包含 113 个原创、长周期软件工程任务的基准，用于评测编程智能体；其方法上的核心主张是验证器质量——验证器应判断提交的代码是否实现任务要求，而不应绑定某一种具体实现方式。MaxxBench 此次测试正是在此基础上改变任务规格，检查 DeepSWE 分数是否随规格变化而保持稳定。

**「实际影响」** 对使用 DeepSWE 这类长周期仓库实现基准做选型或验收的团队，MaxxBench 的扰动测试意味着单一分数不足以支撑决策：任务规格一变，分数和排名就可能变化，讨论中还有人指出该基准存在多处 bug。更稳妥的做法是在自己的代码库上改写任务描述复测，并把榜单名次只当作初筛信号；有评论者认为小模型在规格扰动下失分更明显，但这仍是讨论中的观察，不是已确认结论。

**「社区讨论」** kqr 称赞这种“改变一个参数、观察分数变化”的泛化检验思路，并建议把任务规格作为默认变量之一；peri-cl 则指出，图中带“-flash”的小模型分数下滑最明显，但提醒 GLM-5.3 与 GLM-5.3-flash 属于不同模型谱系，不能按同一规律解读。Systemerror7A69 把 DeepSWE 的 bug 视为对基准可信度的警示，并从中读出“不要使用 max 模式”的实践结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.07946">[2607.07946] DeepSWE: Measuring Frontier Coding Agents on ...</a></li>
<li><a href="https://arxiv.org/pdf/2607.07946">DeepSWE: Measuring Frontier Coding Agents on Original, Long ...</a></li>
<li><a href="https://zhongzhoutan-coder.github.io/benchmarks/agent-eval/deepswe/">DeepSWE: Long-Horizon Software Engineering Benchmark</a></li>
<li>Construct Validity of Coding Benchmarks for LLM-based Agentic ...</li>

</ul>
</details>

**标签**: `#LLM benchmarks`, `#benchmark validity`, `#DeepSWE`, `#model evaluation`, `#software engineering benchmarks`

---

<a id="item-tech-news-2"></a>
### [SemiAnalysis 探访内蒙古 800MW AI 数据中心园区](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) ⭐️ 8.0/10

SemiAnalysis 在实地探访内蒙古乌兰察布后报告称，由远景集团拥有的 Galaxy 园区规划 IT 容量最高达 800MW，规模约为美国 Stargate Abilene 核心园区的水平，其中首期 120MW 在一年内交付，成本仅为美国同类项目的五分之一。该园区四期均为两家互联网巨头定制建设，探访时其余部分仍在施工；当地查哈尔高科技区据引述报道聚集了 22 个数据中心项目和近 3 万名施工人员。SemiAnalysis 还称，远景的垂直整合覆盖风电、专用输电线路、叶片工厂、800V 低压电源模块、储能和预制变电站。上述建设速度、成本和整合程度来自该机构的单次实地报道，未提供可供独立核验的详细数据。

rss · Semianalysis · 11月7日 19:01

**「背景」** 远景集团（Envision）原本是可再生能源系统集成商，全球风电装机超过 100GW，近年在能源管理业务基础上切入数据中心领域，银河园区正是这一转型的落地项目。2026 年 11 月 2 日，远景宣布银河园区的一体化 800V 直流供电系统已投入带载运行，并称这是大型 AI 数据中心首次商业部署此类系统。SemiAnalysis 此前发布过中国数据中心市场的入门报告，本次实地探访是对该主题的跟进。

**「影响」** 对想复制“一年交付 120MW”节奏的开发商来说，Galaxy 案例表明电源安排是关键：Envision 自建风电场、专用线路和电池储能；而欧美主要枢纽的并网等待为 7–10 年，依赖公共电网排队的项目更难按同一时间表推进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datacentremagazine.com/news/envisions-800v-dc-data-centre-world-first-in-ulanqab-china">Envision’s 800V DC Data Centre World-First in Ulanqab, China</a></li>
<li><a href="https://www.unite.ai/envision-deploys-sst-based-800v-dc-power-at-ulanqab-ai-data-center/">Envision Deploys SST-Based 800V DC Power at Ulanqab AI Data ...</a></li>
<li><a href="https://allinhyperscale.com/">Hyperscale Data Center Campus Planner | allinHYPERSCALE</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#datacenters`, `#China tech`, `#compute scaling`, `#cost efficiency`

---

<a id="item-tech-news-3"></a>
### [GitHub 推出面向 AI 智能体并发的 Rubicon 存储架构](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 8.0/10

GitHub 推出代号 Rubicon 的新 Git 存储架构，目标是支持大量 AI 智能体并发操作同一仓库。该架构将 Git 对象存入 Azure Blob Storage，由 Ref-CAS 管理引用状态，并用虚拟副本处理读写、后台节点压缩数据包。GitHub 称内部测试中 5000 个智能体同时协作、每秒处理 7200 次推送，读取延迟保持较低水平；这些是内部测试数据，并非已公开可用的性能指标。该架构目前处于有限私有预览，后续将逐步扩大范围。

telegram · zaihuapd · 11月7日 14:12

**「背景」** Git 仓库的数据分为两部分：不可变的对象（打包成 pack 文件）和指向这些对象的可变引用；每当有人推送，就会新增一个 pack，而这些分散的 pack 需要定期压缩合并，写入越密集，存储与计算耦合的瓶颈就越明显。GitHub 的 Rubicon 方案把 pack 放进 Azure Blob Storage，把引用放进单独的 Ref-CAS 复制日志，并用一次性虚拟副本承接请求、独立后台节点负责压缩，从而把存储与计算解耦。

**「影响」** 目前只有有限私有预览，GitHub 尚未公布开放条件、定价或现有仓库迁移的兼容性细节，普通用户仍按现有 Git 工作流使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub &#x27;s new Git storage architecture - The GitHub Blog</a></li>
<li><a href="https://dzen.ru/a/au6qec3gh2vpaVUH">GitHub описала Rubicon , новое хранилище Git для... | Дзен</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Git storage architecture`, `#distributed systems`, `#AI agents`, `#Azure Blob Storage`

---

<a id="item-tech-news-4"></a>
### [微软研究院 AI Frontiers 团队据报结束，Langford 离职](https://hunch.net/?p=13764006) ⭐️ 7.0/10

据 Hacker News 条目链接的报道，微软研究院（Microsoft Research）的 AI Frontiers 研究团队被宣告结束，研究员 John Langford 离职。现有条目只包含链接和社区讨论，没有微软官方声明、团队规模、结束日期或成员去向等细节，因此这一团队是否已正式解散仍应视为报道说法，而非已确认事实。

hackernews · srean · 11月7日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50406563)

**「背景」** AI Frontiers 是微软研究院在 2023 年 ChatGPT 发布后成立的研究组，规模约 50 人，曾开发用于协调 AI 智能体的 Autogen 框架，以及可操作电脑执行任务的 Fara。该组部分成员还研究不依赖单纯扩大模型规模的模型改进方法。

**「影响」** 若报道准确，最直接的后果是微软研究院内部从事探索性 AI 研究的人员失去 AI Frontiers 这一组织载体；但源材料没有说明相关项目是否延续、成员是否转岗或预算如何调整。

**「社区讨论」** 评论中有人将此解读为大型公司正把资源集中到 transformer 训练与规模化上，并 discouraging 探索其他 AI 方法；也有人强调探索研究与规模化不应互相挤压，并对巨额资金集中于单一方向表示担忧。另有评论指出，标题容易把“AI Frontiers 团队”误读为“AI 的前沿”，建议明确写成“Microsoft Research 的 AI Frontiers 团队”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/microsoft-researcher-john-langford-exits-ai-frontiers-group-declared-finished-t8nprypt6">Microsoft Researcher John Langford Exits. AI Frontiers Group ...</a></li>

</ul>
</details>

**标签**: `#Microsoft Research`, `#AI research`, `#transformer models`, `#industry trends`, `#research funding`

---

<a id="item-tech-news-5"></a>
### [Claude Code 本地设置被指致 1,122 个公开文件泄露密码](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 7.0/10

Apiiro 的博客文章称，在 1,122 个公开 GitHub 文件中发现了密码等秘密，并将问题指向 Claude Code 的 \`.claude/settings.local.json\` 本地设置。文章标题容易被理解为按下“Don&\#x27;t Ask Again”就会泄露，但实际条件是开发者把该设置文件提交到仓库，且其中保存了含明文凭据的手动批准命令。Claude Code 团队的 Boris 回应称，该文件本应留在本地，Claude 创建时会自动加入 \`.gitignore\`；此次涉及的文件是手动创建并提交的，团队过去未做秘密清理，正在研究预防措施。

hackernews · shmulc · 11月7日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=50407882)

**「背景」** Claude Code 的配置分为用户、项目和本地等层级，其中 \`.claude/settings.local.json\` 是项目根目录下的本地设置文件，用来保存只对当前开发者或当前机器生效的会话行为，并在配置优先级中处于较高位置。该文件按设计应被 Git 忽略、不纳入版本控制；一旦有人手动创建并提交它，其中的内容，包括被批准执行的命令，就会随仓库一起公开。

**「影响」** 使用 Claude Code 的开发者应检查 \`.claude/settings.local.json\` 是否已被提交，并轮换已暴露的密码或密钥；在官方防护措施落地前，不能依赖工具自动阻止此类泄露。

**「社区讨论」** 评论中，Aurornis 认为标题误导：仅按“Don&\#x27;t Ask Again”不会泄露，只有把包含明文密钥的本地设置提交并公开才会暴露。tsergiu 和 binarymax 则分享了降低风险的做法，前者用隔离网络中的临时虚拟机配合权限受限的 API 代理，后者让 Claude 通过 1Password CLI 取用凭据并需指纹确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/rulestack/claude-code-settings-precedence-which-of-your-five-settings-files-actually-wins-5133">Claude Code settings precedence: which of your... - DEV Community</a></li>
<li><a href="https://docs.megallm.io/en/cli/claude-config">Claude Code Configuration - MegaLLM</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#security`, `#secret leakage`, `#AI coding agents`, `#GitHub`

---

<a id="item-tech-news-6"></a>
### [Coldframe：伪装超市制冷控制器的蜜罐](https://github.com/hedgerow-dev/coldframe) ⭐️ 7.0/10

Coldframe 是一个新发布的 Show HN 蜜罐，伪装成 Danfoss AK-SM 800A 和 Dixell XWEB 超市制冷控制器，用来观察真实攻击流量。作者称实现只有一个 Python 文件且仅用标准库，并借助真实设备的 Shodan 记录匹配 nginx 头顺序、页面标题、证书字段和 TLS 版本；这两种伪装在 Shodan 上被识别为真实设备而非蜜罐。它能识别 CVE-2025-41450（Danfoss“当日代码”登录绕过）并记录提交的代码对当天是否正确，也会标记针对另外三个 Danfoss CVE 和 XWEB 漏洞的尝试。默认登录会进入带除霜按钮的假门店面板，以便观察第二步操作；两个实例上线一天，目前只记录到通用扫描器和名为 refrigerator.census.shodan.io 的 Shodan 爬虫。

hackernews · hedgerow-dev · 11月7日 17:27 · [社区讨论](https://news.ycombinator.com/item?id=50406292)

**「背景」** Danfoss 在 2025 年 3 月发布的安全公告 DSA-2025-03-01 指出，AK-SM8xxA 系列存在身份验证不当漏洞，可导致认证绕过，需安装编号 4.2 的补丁修复；该问题对应 CVE-2025-41450，NVD 记录显示该 CVE 未被优先纳入富化处理。Coldframe 将这类“code of the day”登录绕过纳入识别规则，用来判断针对其仿冒 AK-SM 800A 的登录尝试是否命中真实漏洞。

**「影响」** 对 ICS 安全研究者而言，Coldframe 的用处是把观测从单次扫描推进到默认登录后的交互，并记录针对 CVE-2025-41450 等漏洞的尝试；但它是研究诱捕工具，不修补或阻断真实制冷控制器上的攻击。

**「社区讨论」** 评论中，supriyo-biswas 提醒不要过度依赖 Shodan 指纹，称互联网上许多同类设备本身已是蜜罐或遭入侵，建议用自己掌握的真实漏洞设备来校准；xrd 则追问此前大规模制冷设备被黑是否有定论，提到也有人认为可能只是大量设备同时收到软件更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01/">DSA-2025-03-01 | Danfoss</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/cve-2025-41450">NVD-CVE-2025-41450</a></li>

</ul>
</details>

**标签**: `#honeypots`, `#ICS security`, `#refrigeration controllers`, `#vulnerability research`, `#Shodan`

---

<a id="item-tech-news-7"></a>
### [Asahi Linux 7.3 进展：代码转 GPLv2 并同步 Fedora 45](https://asahilinux.org/2026/11/progress-report-7-3/) ⭐️ 7.0/10

Asahi Linux 在第 7.3 期进展报告中宣布，已启动将所有代码仓库从 MIT 许可迁移到 GNU GPLv2 或更高版本的工作，理由是有人利用宽松许可攫取并商业化其开发中的代码。报告同时称，Fedora Linux 45 于 11 月 3 日发布当天，Fedora Asahi Remix 也同步推出，这是该项目首次实现与上游同日发布。报告还涉及硬件支持限制；有用户指出，USB-C 外接显示器支持仍是其安装 Asahi Linux 的主要障碍。

hackernews · ackyshake · 11月7日 05:20 · [社区讨论](https://news.ycombinator.com/item?id=50401867)

**「背景」** Asahi Linux 是社区主导的逆向工程与驱动开发项目，目标是把 Linux 带到 Apple Silicon Mac 上；Fedora Asahi Remix 则是基于该项目、面向最终用户的旗舰发行版。该项目此前以 MIT 许可证公开代码，这种宽松条款允许他人复用甚至商业化衍生，成为此次宣布全面转向 GPLv2+ 的直接背景。

**「影响」** 对下游发行版和再分发者而言，若修改并再分发 Asahi Linux 代码，将需要遵守 GPLv2 或更高版本的 copyleft 条款并公开相应源码，不能再沿用 MIT 许可下的闭源分发方式；但项目仅表示已启动迁移，尚未给出完成时间。

**「社区讨论」** 评论中，一名长期资助者称赞 Fedora Asahi Remix 首次与 Fedora 45 同日发布；另一名用户则表示，缺少 USB-C 外接显示器支持仍是其不愿安装的关键原因，并质疑项目为何优先支持更新的 CPU。还有人追问许可变更是否针对 Omarchy，但未获证实；另有开发者宣传自己的 Gravity Linux 项目，其 Vulkan 1.4、M4/M5 和休眠支持等说法未在来源中核实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asahilinux.org/2026/11/progress-report-7-3/">Progress Report: Linux 7.3 - Asahi Linux</a></li>
<li><a href="https://news.lavx.hu/article/asahi-linux-brings-m3-macs-to-general-availability-and-moves-all-code-to-gpl">Asahi Linux brings M3 Macs to general availability and moves ...</a></li>

</ul>
</details>

**标签**: `#Asahi Linux`, `#Linux on Apple Silicon`, `#Fedora Asahi Remix`, `#open-source licensing`, `#hardware support`

---

<a id="item-tech-news-8"></a>
### [分析称 macOS 暗藏构建个人关系图谱的守护进程](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 7.0/10

一篇第三方逆向分析称，自 2022 年起每台 Mac 都随系统附带一对未见于 Apple 文档的守护进程，其用途是构建关于用户本人及周围人的关系图谱：你是谁、你认识谁、这些人彼此如何关联、你如何与他们通讯、去过哪里、和谁、做了什么、何时做的。作者将这套机制与 Apple Intelligence 联系起来，并把它作为隐私与系统设计问题提出。该结论目前来自单一分析文章，Apple 未予确认，现有材料也未提供可供读者独立复核的进程名、系统版本或数据存放位置等细节，因此应视为待验证的第三方发现而非已证实的能力。

hackernews · infwhispers · 11月7日 09:46 · [社区讨论](https://news.ycombinator.com/item?id=50403097)

**「背景：设备端个人知识图谱」** 报道所指的“个人知识图谱”建立在 macOS 一组并非新增的组件之上：据逆向分析，自 macOS 13（2022 年）起，knowledgeconstructiond 与 intelligenceplatformd 两个后台守护进程会把通讯录、信息和照片等本地数据整理成可查询的实体关系库，相关文件位于 ~/Library/IntelligencePlatform，并受 TCC 完全磁盘访问权限保护。这类图谱的作用是让设备端模型完成实体消解，例如分清“给 James 发消息”指的是哪一位 James、或识别“我的老板”是谁，这也是评论中 aetherspawn 给出的解释。苹果并未公开说明这些守护进程的用途与数据处理方式，因此其能力边界目前仍来自第三方逆向分析而非官方文档。

**「影响」** 若该分析成立，受影响的主要是过去几年购入 Mac 的普通用户：就现有材料看，并没有一份公开的系统级说明可供他们核对这些联系人、位置与通讯元数据被关联到什么程度、保存在何处。文章把知情与同意列为核心争议，意味着在 Apple 作出说明前，想弄清状况的用户只能依赖第三方逆向分析或自行检查本地数据。

**「社区讨论」** 有评论者从社交层面提出异议：如果日常对话中的内容总被系统记住，人们交谈时所依赖的“并非一切都会被记住”的氛围就会被削弱，他把这视为伦理之外的社会问题。另一位评论者则认为这类图谱是本地模型解析指代的必要上下文，例如让 Siri 判断“给 James 发消息”指的是哪一位 James；还有人引用乔布斯 2010 年关于隐私要“用平实的语言、反复告知并征得同意”的表态来质疑当前做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/every-mac-comes-with-an-undocumented-family-member-classifier-s3lfxwdun">Every Mac comes with an (undocumented) family member classifier</a></li>
<li><a href="https://techplanet.today/post/apples-hidden-personal-knowledge-graph-understanding-macoss-undocumented-family-classifier">Apple&#x27;s Hidden Personal Knowledge Graph: Understanding macOS ...</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#privacy`, `#macOS`, `#personal knowledge graph`, `#reverse engineering`

---

<a id="item-tech-news-9"></a>
### [Amutable OS 技术概览：无 shell、无 SSH 的镜像化 Linux](https://lwn.net/Articles/1105934/) ⭐️ 7.0/10

Lennart Poettering、Michael Vogt 与 Joaquim Rocha 联合发布了一份关于 Amutable Operating System（AOS）及其配套基础设施的技术概览。AOS 采用镜像式操作系统设计，其安全策略要求默认不安装 UNIX shell、不提供 SSH 远程访问，也不预装 Python、Perl 等常用语言解释器。系统只允许激活带有 Verity 数据的镜像，且这些数据必须由 Verity keyring 中列出的签名密钥签署。该概览称 AOS 具备七项核心安全属性，但目前可见的摘录只展示了前两项，其余内容尚未披露；这份材料介绍的是设计蓝图，并未说明系统已经发布或经过独立验证。

rss · LWN.net · 11月7日 09:32

**「背景」** 镜像式操作系统把整套系统作为只读、可校验的镜像交付，而不是依赖运行时逐包安装和修改；因此系统可以先验证镜像完整性，再决定是否激活。Amutable 的技术概览把这一模型与签名 Verity 数据绑定：只有签名密钥位于 Verity keyring 中的镜像才允许激活。

**「影响」** 按照这一设计，习惯通过 shell 排查故障或依赖 SSH 远程登录的运维流程在 AOS 节点上将无法直接使用；需要使用 Python、Perl 等解释器的应用，也必须自行引入相应运行时，不能假定系统默认提供。同时，自定义构建的镜像只有经 Verity keyring 中登记的密钥签名后才能被激活，因此镜像构建与签名流程需要纳入密钥管理。

**标签**: `#Linux`, `#operating systems`, `#system security`, `#image-based OS`, `#open source`

---

<a id="item-tech-news-10"></a>
### [Claude Code 被指联网请求泄露登录邮箱](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 7.0/10

有开发者报告，Claude Code 在联网搜索时会把用户登录邮箱填入请求并发送，导致其每天收到大量诈骗邮件。Anthropic 工程师表示，邮箱原本是为解决模型乱填作者名而放入模型上下文；该问题今年 7 月已有人报告，邮箱曾被发送给 Wikipedia、美国证券交易委员会等站点。2.1.317 版已加入拦截，但可用 Python 脚本绕过，公司计划在下一版本把登录邮箱从模型上下文中移除。

telegram · zaihuapd · 11月7日 08:09

**「背景」** 问题根源在于 Claude Code 联网搜索时会把模型上下文随请求一并提交；按该问题中的说法，Anthropic 工程师曾为阻止 Claude 在引用网页时乱填作者名，把账户登录邮箱放进了这个上下文。该做法自今年 7 月起就有人报告会把邮箱带到 Wikipedia、美国证券交易委员会等站点，表明敏感信息需要在请求构造层过滤，而不能只靠提示模型不要发送。

**「影响」** 在修复完成前，使用 Claude Code 联网功能的用户仍可能把账号邮箱暴露给第三方站点，并因此面临定向诈骗邮件；升级到 2.1.317 只能挡住常规路径，不能防止脚本绕过。

**标签**: `#Claude Code`, `#privacy leak`, `#AI coding tools`, `#security vulnerability`, `#Anthropic`

---

<a id="item-tech-news-11"></a>
### [苹果披露 HALO 人形机器人系统，采用双 Qwen 模型](https://weibo.com/1642634100/RqjjGllvw) ⭐️ 7.0/10

苹果研究团队在 11 月 4 日提交至 arXiv 的预印本中披露人形机器人控制系统 HALO，并称已在宇树 G1 上把仿真环境学到的动作迁移到陌生真实房间执行。HALO 分为三层：上层由 Qwen3.6-35B-A3B 负责任务编排，中层由 Qwen3.5-2B 生成动作，底层是经强化学习训练的动作跟踪器。团队还公开了数据生成、模型训练与部署代码。该成果目前仍是未经同行评审的预印本，来源摘要未提供基准对比或独立验证。

telegram · zaihuapd · 11月7日 13:35

**「背景」** 仿真到现实（sim-to-real）指把仿真环境中训练出的控制策略迁移到真实机器人，主要难点在于感知、摩擦和动力学差异。分层控制则把较慢的任务规划与较快的动作生成、底层跟踪分开处理。此次验证使用的宇树 G1 是宇树科技公开销售的人形机器人平台，官方页面标注其关节数为 23–43 个。

**「影响」** 对机器人与开源 AI 开发者而言，公开的数据生成、训练和部署代码提供了在宇树 G1 上复现 HALO 流程的入口；但实际迁移效果仍需独立测试，因为现有信息仅来自论文摘要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shop.unitree.com/">UnitreeRobotics-More than Wisdom, Be with You</a></li>

</ul>
</details>

**标签**: `#humanoid robotics`, `#robot learning`, `#sim-to-real`, `#Qwen`, `#open-source research`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [软银与 ABB 考虑分拆中国业务，以挽救被叫停的 54 亿美元机器人收购](https://www.bloomberg.com/news/articles/2026-11-07/softbank-abb-weigh-china-carve-out-to-salvage-robotics-deal) ⭐️ 8.0/10

据彭博社援引知情人士报道，软银与 ABB 正考虑将 ABB 机器人业务的中国部分分拆为独立实体，以挽救这笔已被中国外商投资安全审查机制办公室于本周四叫停的 54 亿美元收购；该中国业务估值可能为 20 亿至 30 亿美元。报道称该方案可能失败，ABB 同时也在评估包括另寻买家在内的其他选项，两家公司均拒绝置评。

telegram · zaihuapd · 11月7日 11:24

**「背景」** 中国外商投资安全审查工作机制办公室本周四叫停软银对 ABB 机器人业务 54 亿美元的收购；中国是 ABB 机器人业务最大市场，且面向中国客户的机器多数在当地生产。

**「交易影响」** 若分拆方案失败，ABB 或需为该机器人业务另寻买家，软银借助这笔 54 亿美元交易推进“物理 AI”布局的计划也将受阻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swissinfo.ch/eng/workplace/china-blocks-softbanks-5-4bn-takeover-of-abbs-robotics-division/92331403">China blocks SoftBank ’s $ 5 . 4 bn takeover of ABB ’s robotics division</a></li>
<li><a href="https://www.nytimes.com/2026/11/05/business/softbank-robotics-china-block.html">China Blocks SoftBank ’s $ 5 . 4 Billion Robotics Takeover, Impeding...</a></li>
<li><a href="https://www.nytimes.com/2026/11/05/business/softbank-robotics-china-block.html">China Blocks SoftBank ’s $5.4 Billion Robotics Takeover, Impeding...</a></li>
<li><a href="https://www.swissinfo.ch/eng/workplace/china-blocks-softbanks-5-4bn-takeover-of-abbs-robotics-division/92331403">China blocks SoftBank ’s $5.4bn takeover of ABB ’s robotics division</a></li>

</ul>
</details>

**标签**: `#cross-border M&amp;A`, `#China investment screening`, `#robotics`, `#SoftBank`, `#ABB`

---

<a id="item-finance-news-2"></a>
### [伯克希尔第三季度回购翻倍至 96 亿美元，经营利润下降 5.8%](https://www.cnbc.com/2026/11/07/berkshire-hathaway-q3-2026-earnings-buybacks.html) ⭐️ 7.0/10

伯克希尔-哈撒韦第三季度回购了 96 亿美元自家股票，是第二季度 45 亿美元回购额的两倍多，使 2026 年累计回购约达 144 亿美元；同期经营利润为 127.05 亿美元，较上年同期的 134.85 亿美元下降 5.8%。包含股票投资组合的整体利润下降 28%，从上年同期的 307.96 亿美元降至 221.12 亿美元，其中投资利得减少近 50%至 94.07 亿美元。

rss · CNBC Finance · 11月7日 15:23

**「背景」** 柏克希尔于 2026 年 1 月完成管理层交接，格雷格·阿贝尔接替沃伦·巴菲特出任首席执行官。该公司没有固定的回购计划，只有在首席执行长与董事长共同判断股价明显低于内在价值时才会授权回购，因此单季回购规模骤增本身被视为一种信号。

**「影响」** 对留存股东而言，回购直接减少流通股数量，因此即使总利润下滑，每位股东对应的每股收益份额也会相应提高；同期公司现金储备增至 3774.35 亿美元，高于第二季度的 3655.14 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Greg_Abel">Greg Abel - Wikipedia</a></li>
<li><a href="https://www.fool.com/investing/2026/01/02/with-warren-buffett-no-longer-ceo-at-berkshire-hat/">With Warren Buffett No Longer CEO at Berkshire Hathaway , Greg ...</a></li>
<li><a href="https://nai500.com/blog/2026/03/is-greg-abel-sending-a-buy-signal-berkshire-ceo-buys-15m-in-stock-and-restarts-buybacks/">Is Greg Abel Sending a Buy Signal? Berkshire CEO Buys ... | NAI 500</a></li>

</ul>
</details>

**标签**: `#Berkshire Hathaway`, `#share buybacks`, `#earnings`, `#insurance`, `#cash reserves`

---