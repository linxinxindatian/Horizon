---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 39 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [Lovable 应用被曝泄露护照信息与 20 余万条私信](#item-tech-news-1) ⭐️ 8.0/10
2. [星舰第 15 次试飞：飞船首次完成轨道级塔捕](#item-tech-news-2) ⭐️ 8.0/10
3. [PyPI 新版项目页上线，强化安全与来源信号](#item-tech-news-3) ⭐️ 7.0/10
4. [EFF：科技公司再次试图重新定义隐私](#item-tech-news-4) ⭐️ 7.0/10
5. [Show HN：约 200 行纯 JAX 实现 DeepSeek V3](#item-tech-news-5) ⭐️ 7.0/10
6. [Project Zero 拟分阶段缩短漏洞披露窗口](#item-tech-news-6) ⭐️ 7.0/10
7. [Cloudflare 开源无状态 AI 代理浏览器 Kitesurf](#item-tech-news-7) ⭐️ 7.0/10
8. [意大利因 Facebook 违规读取相册罚 Meta 8.05 亿欧元](#item-tech-news-8) ⭐️ 7.0/10
9. [特斯拉 Cybercab 协议：月租 299 美元方可运行](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [黄仁勋辞职后英伟达承压，AI 交易可能转向大型科技股与 AMD、博通](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Lovable 应用被曝泄露护照信息与 20 余万条私信](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

一项安全研究披露，部分由 Lovable 生成并公开上线的应用暴露了敏感用户数据，包括护照信息和超过 20 万条私信；研究者将原因指向行级安全（RLS）配置不足。Lovable 安全负责人回应称，这些应用的根因正是 RLS 不足，平台会在发布前自动扫描每个应用，并提供免费的深度 SAST 扫描、修复和自动修复选项。

hackernews · armcat · 11月14日 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**「背景：Supabase 的行级安全（RLS）」** Supabase 在 Postgres 之上自动生成 API，并通过 Row Level Security（行级安全）按登录用户限制每一行数据的读取与写入；如果某张表未启用 RLS，那么针对该表的 API 访问就不会受到行级约束（tool-2-1、tool-2-2）。Lovable 这类 AI 应用构建器会连同前端一起生成 Supabase 后端，因此平台默认是否开启策略、生成代码里的策略是否写对，直接决定了应用数据对外的可见范围。

**「对已发布应用的影响」** 对已用 Lovable 发布应用的用户和开发者而言，直接后果是：若 Supabase 后端数据表未启用行级安全（RLS），持有公开匿名密钥的人就可能直接读取表内数据，因此需要逐表确认 RLS 已开启，并复核对外可读的接口。Lovable 安全负责人表示，平台会在发布前自动扫描每个应用，并提供免费的深度 SAST 扫描、一键修复、后台自动修复以及阻止发布等选项；有评论者则指出，Supabase 相关默认值调整（据称 10 月 30 日修复）对既有项目可能仍未生效，这一说法尚未获得独立证实。

**「社区讨论」** 评论区的核心分歧在于责任归属：有评论者认为 Supabase 当年为降低接入门槛而采用宽松默认设置，并称相关默认值虽在 10 月 30 日宣称修复，现有项目可能仍沿用旧配置；也有人强调 AI 生成应用数量多、攻击门槛低，平台应默认拒绝并实行最小权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/orgs/supabase/discussions/6765">message: &#x27;new row violates row - level security policy for table...</a></li>
<li><a href="https://supabase.com/">Supabase | The Postgres Development Platform</a></li>
<li><a href="https://lovable.dev/">App &amp; Website Builder | Build Software in Minutes | Lovable</a></li>

</ul>
</details>

**标签**: `#security`, `#data exposure`, `#Supabase`, `#Row-Level Security`, `#AI app builders`

---

<a id="item-tech-news-2"></a>
### [星舰第 15 次试飞：飞船首次完成轨道级塔捕](https://www.spacex.com/launches/starship-flight-15) ⭐️ 8.0/10

SpaceX 于当地时间 11 月 13 日发射星舰第 15 次试飞；据 SpaceX 公布，飞船在约 22.5 小时飞行、绕地球约 14 圈后返回得州 Starbase，并首次由发射塔机械臂直接捕获，完成轨道级飞船的塔捕回收。飞船部署了全部 26 颗 Starlink V3 卫星，其中 3 颗带摄像头用于检查隔热瓦。但超重型助推器因技术问题中止返场，在墨西哥湾受控溅落并爆炸，具体原因未公布，因此两级同时回收未实现。上述回收结果为 SpaceX 公布，来源未提供独立验证或飞船回收后的状态细节。

telegram · zaihuapd · 11月14日 03:03

**「背景」** 在此前的试飞中，SpaceX 已多次用发射塔机械臂捕获 Super Heavy 助推器；第 15 次试飞把目标提升为在同一任务中先后回收助推器和飞船，因此助推器中止返场后，“双塔捕”未能实现。更早的第 13 次试飞首次部署了 Starlink V3 卫星，本次部署 26 颗属于该系列卫星的后续应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_Starship_launches">List of Starship launches - Wikipedia</a></li>
<li><a href="https://www.basenor.com/blogs/news/starship-flight-15-6-details-that-matter-for-todays-launch">Starship Flight 15 : 6 Details That Matter for Today&#x27;s Launch</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#reusable launch`, `#Starlink V3`, `#aerospace engineering`

---

<a id="item-tech-news-3"></a>
### [PyPI 新版项目页上线，强化安全与来源信号](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 7.0/10

PyPI 已上线重新设计的项目页面，把软件包的安全与来源（provenance）信息更清楚地展示出来。此次更新主要是界面和信号呈现层面的调整，并非推出新的签名机制。对 Python 开发者和依赖方来说，项目页面现在更容易看出某个发布是否带有 provenance 等安全标记。

hackernews · rbanffy · 11月14日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50497892)

**「背景」** PyPI 在此次改版之前已经通过“可信发布”（Trusted Publishing）和文件级来源证明（provenance attestation）收集了签名与构建来源数据；评论中提到的 dlt 与 datasette 的对比（前者无 provenance、后者有）说明这些信息挂在每个项目的文件列表页上，是否具备取决于维护者是否采用该发布方式。此次改版主要是把这些既有信号在项目页上更醒目地呈现，而非引入新的签名机制。

**「实际影响」** 对依赖 PyPI 的开发者而言，项目文件列表中的 provenance 标记只在包通过 Trusted Publishing 发布时出现：PyPI 会在上传时校验 attestation 中的身份是否与维护者此前为该包配置的 Trusted Publishing 身份一致（tool-2-2）。这意味着未走该流程的项目不会显示这一信号，用户需要逐文件判断来源；希望获得该标记的维护者则需把发布切换到受支持的 CI 信任发布流程，因为注册表正是借助每次上传时收到的已验证工作流身份来降低 provenance 的生成门槛（tool-2-3）。

**「社区讨论」** 评论中，time4tea 担心把信任建立在中心化服务和大型云厂商上会带来锁定效应，认为这不太符合 Python 社区的风格；cowlevel 则指出，这类来源信号更擅长发现原本正常、后来被入侵的项目，而无法识别一开始就恶意的项目。也有用户用 dlt（无 provenance）和 datasette（有 provenance）作为页面上信号差异的实例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pypi.org/using-pypi/package-security/provenance/">Checking Provenance (package origin) - PyPI User Documentation</a></li>
<li><a href="https://nesbitt.io/2026/10/30/signing-and-attestations-across-package-registries.html">Signing and Attestations Across Package Registries | Andrew Nesbitt</a></li>

</ul>
</details>

**标签**: `#PyPI`, `#software supply chain security`, `#package provenance`, `#Python packaging`, `#open source`

---

<a id="item-tech-news-4"></a>
### [EFF：科技公司再次试图重新定义隐私](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

电子前沿基金会（EFF）发文审视科技公司再次试图重新定义隐私概念的做法。由于抓取内容未提供文章正文，报道没有给出具体公司、政策提案或法律条款，因此目前只能确认这是一篇评论分析，而非已经落地的产品变更或监管决定。

hackernews · gslin · 11月14日 12:45 · [社区讨论](https://news.ycombinator.com/item?id=50496602)

**「背景」** EFF 的 Thorin Klosowski 将这场争论描述为隐私焦点从“个人选择”转向“旁观者问题”：可穿戴设备让佩戴者之外的周围人也进入记录范围。文中举例包括可拍摄并用 AI 描述画面的 Meta、Google 智能眼镜，把 Apple Watch 变成转写设备的 Apple Audio Intelligence，以及可录制并转写环境的 Amazon Bee 设备。

**「合规影响」** 对企业来说，部署 Otter.ai、Fireflies 等 AI 会议记录工具会使常规会议产生隐私、同意和证据开示风险；美国各州对录音同意的规定并不一致，相关工具已引发集体诉讼，因此组织应在会前取得明确同意，并制定转录内容的保留与删除规则。

**「社区讨论」** Hacker News 评论中，有人称如今连一对一会议也常被 AI 记录并上传，担心无法在不影响就业的情况下退出，并询问能否把“本次会议不需要转录”变成常态；另一名评论者则强调实时转录眼镜对聋人和重听者可能有变革性作用，认为本地模型不必保存或导出数据，并对一刀切禁令提出质疑。其他评论还援引《世界人权宣言》第 12 条讨论隐私保护，并建议用公开身份、一次性身份和气隙等做法降低暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.my/items/46520/tech-companies-are-trying-to-shift-the-concept-of-privacy-again">Tech Companies Are Trying to Shift the Concept of Privacy (Again)</a></li>
<li><a href="https://www.forbes.com/sites/timbajarin/2026/08/21/ai-note-takers-turn-routine-meetings-into-potential-legal-evidence/">AI Note-Takers Turn Routine Meetings Into Potential Legal ...</a></li>
<li><a href="https://www.recordinglaw.com/us-laws/ai-meeting-recording-laws/">AI Meeting Recording Laws by State: Complete Guide (2026)</a></li>
<li><a href="https://mslawgroup.com/is-that-bot-in-your-meeting-breaking-the-law/">Is That Bot in Your Meeting Breaking the Law? - Mac Murray ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#AI notetakers`, `#tech policy`, `#digital rights`

---

<a id="item-tech-news-5"></a>
### [Show HN：约 200 行纯 JAX 实现 DeepSeek V3](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) ⭐️ 7.0/10

开发者 VaibhaavTiwari 在 Hacker News 的 Show HN 展示了一个约 200 行、纯 JAX 的 DeepSeek V3 实现，面向希望从第一性原理理解模型推理与训练的开发者。现有信息不足以确认该项目覆盖完整训练流程或已通过正确性验证；不过有评论者称，这是其 RX 7600 XT 16GB 上首个在 Fedora 与 ROCm 环境中端到端跑通本地训练的项目。

hackernews · VaibhaavTiwari · 11月14日 15:04 · [社区讨论](https://news.ycombinator.com/item?id=50497589)

**「背景」** DeepSeek V3 是一个混合专家（MoE）语言模型：其 Hugging Face 模型卡显示总参数为 671B，但每个 token 仅激活约 37B 参数。这种“总参数量大、单 token 激活量小”的结构是理解其推理实现的关键前提，也让用少量代码复现模型结构的教学型项目更容易被逐层拆解和讨论。

**「影响」** 对没有 CUDA、使用 ROCm 的开发者，这个项目提供了一条可直接尝试的 JAX 本地实验路径；但该评论者报告，RX 7600 XT 需要设置两个环境变量，其中之一是 HSA\_OVERRIDE\_GFX\_VERSION=11.0.0，具体兼容性仍取决于本机 GPU 与 JAX 的 ROCm 插件配置。

**「社区讨论」** 评论区整体反应积极，armcat 和 itsthecourier 等读者表示想借此从零复现模型或重新学习 JAX；mattfrommars 则询问系统理解推理实现的路线图，但可见评论中尚未给出完整答案。最有实质性的反馈来自 joebarbere，他报告了在 Fedora 与 ROCm 上使用 RX 7600 XT 16GB 跑通端到端训练的体验，并提醒需要两个环境变量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3-Base">deepseek -ai/ DeepSeek - V 3 -Base · Hugging Face</a></li>

</ul>
</details>

**标签**: `#JAX`, `#DeepSeek V3`, `#LLM inference`, `#ROCm`, `#open-source ML`

---

<a id="item-tech-news-6"></a>
### [Project Zero 拟分阶段缩短漏洞披露窗口](https://projectzero.google/2026/11/disclosure-policy.html) ⭐️ 7.0/10

根据现有材料，Google Project Zero 在公告发布时采用“报告后 90 天”的漏洞披露窗口，并计划在 2027 年和 2028 年分别缩短至 60 天和 30 天；评论中引述的生效日期为 2027 年 2 月 2 日和 2028 年 1 月 3 日。该时限适用于 Project Zero 向厂商报告漏洞后的公开披露，但当前材料只有政策转述，尚无公告原文或独立确认。

hackernews · hacb · 11月14日 11:13 · [社区讨论](https://news.ycombinator.com/item?id=50496051)

**「背景」** 此前，Project Zero 自 2021 年起实行“90 + 30”漏洞披露政策：厂商最多有 90 天修复漏洞，并可额外获得 30 天用于推送补丁。此次改为“Full 90”，即在报告后第 90 天公开漏洞，取消额外的 30 天缓冲，并计划于 2027 年 2 月 2 日和 2028 年 1 月 3 日分别缩短至 60 天和 30 天；Project Zero 称，AI 辅助的漏洞发现与利用改变了威胁格局。

**「影响」** 对收到 Project Zero 报告的厂商而言，公开披露前的修复窗口将从 90 天逐步压缩到 60 天和 30 天；依赖较长协调周期的项目需要相应调整补丁开发和发布流程，否则可能在新时限到达时仍无法提供修复。

**「社区讨论」** 评论中有人质疑 30 天窗口对 Ubuntu 等大型发行版过于紧迫，也有人主张应尽快甚至立即公开，认为只有披露压力才会迫使厂商修复。另有评论把话题延伸到漏洞发现方是否应向厂商提供对等的研究工具访问，但这与披露时限本身关系较弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://projectzero.google/2026/11/disclosure-policy.html">Policy and Disclosure: 2026 Edition - Project Zero</a></li>

</ul>
</details>

**标签**: `#vulnerability disclosure`, `#Project Zero`, `#security policy`, `#coordinated disclosure`, `#software security`

---

<a id="item-tech-news-7"></a>
### [Cloudflare 开源无状态 AI 代理浏览器 Kitesurf](https://www.phoronix.com/news/Cloudflare-Kitesurf-Open-Source) ⭐️ 7.0/10

Cloudflare 已以 Apache 2.0 协议开源 Kitesurf，这是一个面向 AI 代理的无状态浏览器，代码发布在 GitHub。它构建于 Cloudflare Workers，无需浏览器容器即可解析 HTML、处理 CSS 并执行 JavaScript。Cloudflare 称其相比 Chromium 占用更少 CPU 和内存，并可在全球 Workers 网络上按需扩展，但这些性能和扩展性说法尚未附基准测试或独立评测。

telegram · zaihuapd · 11月14日 09:33

**「背景」** Cloudflare 将 Kitesurf 定位为面向 AI 代理的实验性浏览器引擎，并称其不依赖 Chromium；其 GitHub 仓库说明，Kitesurf 需要 Cloudflare Dynamic Workers 为每个页面创建隔离 Worker，而 Dynamic Workers 属于 Workers 付费计划。也就是说，Kitesurf 的“无浏览器容器”方案依赖 Workers 的隔离运行时，使用前需具备相应的付费计划。

**「对代理开发者的影响」** 对在 Cloudflare Workers 上构建浏览型 AI 代理的开发者而言，Kitesurf 提供了 Chromium 之外的引擎选择，并可在 Browser Run 中作为默认引擎的替代项使用，返回 HTML、截图和 PDF。实际迁移时需先验证目标页面兼容性：已有评测提到它存在速度取舍和功能边界，不能假定所有依赖完整 Chromium 行为的页面都能直接运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/kitesurf-open-source/">Kitesurf is now open source | Cloudflare Blog</a></li>
<li><a href="https://github.com/cloudflare/kitesurf">GitHub - cloudflare / kitesurf : Kitesurf is an experimental browser ...</a></li>
<li><a href="https://www.eesel.ai/blog/cloudflare-kitesurf">Cloudflare Kitesurf : the agent browser that trades speed... | eesel AI</a></li>
<li><a href="https://www.therundown.ai/tools/kitesurf">Kitesurf Review: Cloudflare Agent Browser , Pricing &amp; Limits</a></li>
<li><a href="https://pinggy.io/blog/cloudflare_kitesurf_ai_agent_browser/">Inside Kitesurf : Cloudflare Built a Browser Engine Just for AI Agents</a></li>
<li><a href="https://groundingpage.com/facts/kitesurf/">Kitesurf : Cloudflare &#x27;s Browser Engine for AI Agents in Browser Run</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#AI agents`, `#open source`, `#browser automation`, `#Cloudflare Workers`

---

<a id="item-tech-news-8"></a>
### [意大利因 Facebook 违规读取相册罚 Meta 8.05 亿欧元](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10321080) ⭐️ 7.0/10

意大利隐私监管机构 Garante Privacy 对 Meta 处以 8.05 亿欧元罚款，原因是 Facebook 的 Android 应用在未获具体同意的情况下读取了约 2000 万意大利用户的相册照片、视频及元数据。涉事的相册推荐功能于 2023 年上线，默认开启且授权提示笼统。监管机构要求 Meta 在 60 天内将该功能改为默认关闭并单独征得用户同意，否则不得对未有效授权的用户启用。

telegram · zaihuapd · 11月14日 14:37

**「背景」** 涉事功能是 Facebook Android 应用中的相册推荐（“Get suggestions from…”），于 2023 年上线时默认开启，授权提示为笼统的一揽子说明。意大利数据保护局（Garante）是 GDPR 框架下负责该国隐私执法的独立监管机构，其本次裁决要求该功能改为默认关闭，并在单独征得用户同意后才可启用。

**「实际影响」** 对意大利约 2000 万 Facebook Android 用户而言，相册推荐功能须在 60 天内改为默认关闭，并在启用前单独取得同意；Meta 若未完成调整，就不得向未有效授权的用户开放该功能。这也意味着 Meta 需要重做该功能的授权提示和默认设置，不能继续依赖原有的笼统授权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://abcnews.com/Technology/wireStory/meta-fined-887-million-italy-android-gallery-photos-138145127">Meta fined $887M in Italy over Android gallery photos, videos ...</a></li>
<li><a href="https://www.reuters.com/world/italy-fines-meta-887-million-over-android-users-data-access-2026-11-14/">Italy fines Meta $887 million over Android users&#x27; data access</a></li>
<li><a href="https://www.politico.eu/article/italy-hits-meta-with-e805m-fine-over-privacy-law-violation/">Italy hits Meta with €805m fine over privacy law violation</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/15/italy-fines-meta-887m-for-accessing-android-users-photos-and-videos">Italy fines Meta $887m for accessing Android users’ photos ...</a></li>

</ul>
</details>

**标签**: `#privacy regulation`, `#Meta`, `#Android permissions`, `#consent`, `#Italy`

---

<a id="item-tech-news-9"></a>
### [特斯拉 Cybercab 协议：月租 299 美元方可运行](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 7.0/10

该条目披露的特斯拉 Cybercab 订阅协议显示，车辆售价为 29,990 美元，车主须每月支付 299 美元订阅费，否则车辆无法运行；特斯拉可提前一个月通知调价。欠费或违规使用可能导致订阅暂停或取消，累计三次警告将停用自动驾驶一周。协议还把运行范围限制在指定区域，并禁止未经授权接入网约车、配送或租赁平台。Electrek 指出，Cybercab 与用于 Robotaxi 的 Model Y 均采用 AI4 硬件并运行相同的自动驾驶软件，但面向普通车主的 FSD 仍需人类监督。

telegram · zaihuapd · 11月15日 01:10

**「背景」** Cybercab 是特斯拉为无人驾驶场景设计的专用车型；据 ZeroHedge 报道，该车没有方向盘和踏板，个人购买最初只向受邀的“部分客户”开放（tool-2-3）。由于车辆本身不提供人工驾驶作为替代，Autonomy Subscription 不再只是可选的车机功能，而是车辆能否投入个人使用的前置条件。

**「影响」** 对车主而言，购车并不等于可自由使用：订阅中断会直接让车辆无法运行，指定区域和平台接入限制也会压缩把车辆用于营运或租赁的空间。购车前需要把每月 299 美元的长期支出和潜在停用风险计入总成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/technology/tesla-opens-cybercab-orders-select-customers-personal-use">Tesla Opens Cybercab Orders To &quot;Select Customers...&quot; | ZeroHedge</a></li>

</ul>
</details>

**标签**: `#特斯拉`, `#Cybercab`, `#自动驾驶订阅`, `#商业模式`, `#智能汽车`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [黄仁勋辞职后英伟达承压，AI 交易可能转向大型科技股与 AMD、博通](https://www.cnbc.com/2026/11/14/nvidia-ai-trade-data-centers-congress.html) ⭐️ 7.0/10

英伟达创始人兼 CEO 黄仁勋辞职后，公司股价出现 2012 年以来最长周线连跌；CNBC“ETF Edge”嘉宾称，AI 交易可能转向大型科技股以及 AMD、博通等替代芯片供应商。Yorkville Ives 将英伟达目标价从 300 美元下调至 225 美元、维持买入评级，该股周五收于 162.85 美元；该机构还估计，民主党控制国会后，可能有 10%至 20%的计划数据中心无法落地。

rss · CNBC Finance · 11月14日 15:50

**「背景」** 英伟达董事会于周三接受了黄仁勋的辞任，并任命首席财务官科莱特·克雷斯为临时 CEO，直到找到正式继任者。此前在 11 月 3 日中期选举后，民主党取得国会控制权，一些当选者主张限制 AI 发展和数据中心建设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/12/nvidias-jensen-huang-resigns-chipmaker-names-cfo-colette-kress-as-interim-ceo/">Nvidia &#x27;s Jensen Huang resigns , chipmaker names CFO Colette ...</a></li>
<li><a href="https://foreignpolicy.com/2026/11/05/midterm-results-ai-data-centers-texas-georgia-ohio/">Midterm Results Reflect AI , Data Center Concerns</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI trade`, `#ETFs`, `#US politics`, `#semiconductors`

---