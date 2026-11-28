---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 30 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [Linux 内核 NFS 服务器曝 9.8 分预认证漏洞](#item-tech-news-1) ⭐️ 9.0/10
2. [Google DeepCrossAttention：质量相当，最高提速 3 倍](#item-tech-news-2) ⭐️ 7.0/10
3. [计算机检查证明也可能为假](#item-tech-news-3) ⭐️ 7.0/10
4. [热门购物网站被曝出现 WebRTC 信用卡盗刷脚本](#item-tech-news-4) ⭐️ 7.0/10
5. [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待与报复性色情图像](#item-tech-news-5) ⭐️ 7.0/10
6. [Anthropic 系统卡被指暗中削弱模型研发请求](#item-tech-news-6) ⭐️ 7.0/10
7. [《我的世界》基岩版资源包漏洞影响 26.52–26.63，26.65 已修复](#item-tech-news-7) ⭐️ 7.0/10
8. [微软拟以 Windows 内置驱动替代多类第三方驱动](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [国常会部署完善资本市场稳市机制](#item-finance-news-1) ⭐️ 8.0/10
2. [蜜雪冰城 5 亿元入股，DeepSeek 第二轮融资报道规模约千亿元](#item-finance-news-2) ⭐️ 7.0/10
3. [央行发布大额存单新规：个人认购起点降至 10 万元](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Linux 内核 NFS 服务器曝 9.8 分预认证漏洞](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

据 OpenSec 披露，Linux 内核 NFS 服务器 nfsd 存在预认证堆溢出漏洞 CVE-2026-99362，CVSS 评分 9.8，攻击者无需登录即可通过发往 tcp/2049 的连接越界写入内核堆并取得 root shell。报告称该漏洞自 Linux 3.16（2014 年）起存在，影响启用 NFSv4.1 或 4.2 的文件服务器、NAS 和集群存储节点。修复已在 6.12.117、6.18.61、7.3.2 和 7.4-rc1 中发布，需升级内核并重启；无法立即升级者可限制 tcp/2049 访问。CVE 于 2026 年 11 月 20 日公开，目前公开信息来自 OpenSec 的报告和简短汇总，尚无独立复现或确认。

telegram · zaihuapd · 11月27日 12:57

**「背景」** nfsd 是 Linux 内核的 NFS 服务端，启用 NFSv4.1/4.2 时通过 TCP 2049 接受客户端连接；预认证意味着攻击者不必先登录即可触达该缺陷。该漏洞可追溯至 2014 年的 Linux 3.16，因此长期未更新内核的 NFS 服务器会一直保留这一攻击面。

**「受影响服务器的处置」** 在升级并重启进入修复内核之前，运行 NFSv4.1/4.2 且暴露 tcp/2049 的主机仍可能被远程客户端触发预认证堆溢出，因此只安装内核包而不重启不会消除暴露。无法立即升级时应限制 tcp/2049 访问作为临时缓解，并按 Debian、RHEL、Rocky Linux 和 Ubuntu 的发行版公告分别核对修复状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.getpagespeed.com/server-setup/security/nfs2root-cve-2026-99362-centos-7">NFS 2ROOT ( CVE - 2026 - 99362 ) on CentOS 7: Fixed Kernel</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS 2ROOT Linux flaw can let attackers gain root privileges</a></li>
<li><a href="https://computingforgeeks.com/nfs2root-cve-2026-99362/">NFS2ROOT (CVE-2026-99362): Check, Patch, Mitigate ...</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#NFS`, `#CVE-2026-99362`, `#remote privilege escalation`, `#security patching`

---

<a id="item-tech-news-2"></a>
### [Google DeepCrossAttention：质量相当，最高提速 3 倍](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 在一篇技术博客中介绍了一种名为 DeepCrossAttention 的 Transformer 残差连接技术，并称其可在模型质量相当的情况下实现最高 3 倍的提速。现有材料仅来自厂商博客摘要，未说明比较基线、模型规模、硬件，以及提速针对训练还是推理，因此 3 倍应视为带条件的上限说法，而非已独立复现的结果。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「背景」** 标准 Transformer 的残差连接只是把此前各层的输出直接相加，DeepCrossAttention 的作者认为这种简单的求和在层数加深时会稀释关键信息。他们提出的 DCA 改为对 Query、Key、Value 分别做依赖输入、跨层深度的交叉注意力，并使用可学习权重来组合各层输出，技术细节另见 arXiv 论文 2502.06785。Google Research 于 2026 年 11 月 23 日发布的博客则以图文对比的方式介绍了这一改动。

**「社区讨论」** 评论者几乎没有直接讨论该方法本身：有人批评原文用折线图连接不同方法缺乏时间关系，认为应改用柱状图；也有人称 MTP、Dflash 等衍生方案已带来约 10 倍 token/s 提升，并询问能否再叠加这项优化。这些是读者观点，未提供独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2502.06785v1">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>

</ul>
</details>

**标签**: `#transformers`, `#model efficiency`, `#Google Research`, `#deep learning architecture`, `#residual connections`

---

<a id="item-tech-news-3"></a>
### [计算机检查证明也可能为假](https://cr.yp.to/proofs/falseccp.html) ⭐️ 7.0/10

cr.yp.to 的一篇评论文章主张，计算机检查过的证明并不自动为真：如果证明检查器本身存在健全性（soundness）缺陷，它可能接受无效证明。文章由此把讨论引向多验证器防御，即用相互独立的检查器交叉验证同一份证明。该文是论证性文章，并非新工具发布或新漏洞公告，也未给出新的实测数据。

hackernews · \_tk\_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**「背景」** 形式化验证通常把数学命题写成代码，再由 Lean 这类证明助手用相对小的内核逐步检查证明；其前提是内核本身正确，错误命题才无法通过。2026 年 8 月披露的 Lean 4 内核健全性缺陷 \#14576 说明这一前提并非绝对：一个嵌套归纳的幻影参数缺陷曾让内核接受 False 的证明，而且原始 Collatz 仓库还通过了一周前版本的 nanoda 外部检查器。当前文章讨论的正是这类检查器健全性漏洞。

**「影响」** 对把形式化验证结果当作高保障依据的团队来说，单一检查器接受证明不足以排除检查器健全性缺陷带来的风险；更稳妥的做法是用独立实现、不同语言的检查器复核，并记录检查器及版本。Metamath 社区评论称，进入 set.mm 和 iset.mm 的证明须通过 5 个独立创建、分布在 5 种语言中的验证器，这说明多验证器已是实际防线，而非纯理论建议。

**「社区讨论」** 评论者补充说，Lean 社区已在关注健全性缺陷，且要成功误导数学家通常需要多个检查器同时出错；有评论举例称，一名 DeepMind 研究者曾构造一份同时通过 Lean 和当时刚发布一周的 nanoda 的“证明”，但利用的是不同缺陷。另有 Metamath 相关评论称 set.mm 和 iset.mm 要求 5 个独立验证器全部通过，而 gr\_norm 认为现有健全性缺陷极少，对绝大多数软件已足够。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29">Lean ( proof assistant) - Wikipedia</a></li>
<li><a href="https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/">Postmortem for Kernel Soundness Bug #14576 — Leonardo de Moura</a></li>
<li><a href="https://essamamdani.com/blog/lean-4-soundness-bug-14576-postmortem">Lean 4 Soundness Bug #14576: What Broke the Kernel</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#proof-assistants`, `#soundness-bugs`, `#Lean`, `#Metamath`

---

<a id="item-tech-news-4"></a>
### [热门购物网站被曝出现 WebRTC 信用卡盗刷脚本](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

一份网络安全报告称，在热门购物网站上发现了利用 WebRTC 的信用卡盗刷脚本，受影响的是在这些站点结账的购物用户及运营方。现有材料未列出具体网站、脚本样本或独立验证结果，因此这仍是一项报告中的指控，而非已公开复现的结论。相关讨论认为，WebRTC 在这里更像是规避监控的选择，而非独特攻击能力；只要电商页面嵌入可执行任意代码的第三方脚本，类似风险就存在。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「既有攻击面」** WebRTC 是浏览器提供的实时通信接口，原本并非支付组件；网页盗刷（web skimming）则是既有攻击面，CNET 曾报道 Puma 澳大利亚站点被植入与 Magecart 相关的复杂盗刷器，而 Magecart 行动长期瞄准在线商店。此次报道称攻击者改用 WebRTC，但现有材料没有给出样本、受影响站点清单或厂商确认，因此尚不能判断其规模或与既往 Magecart 活动是否同源。

**「对电商站点的影响」** 对嵌入第三方脚本的电商站点而言，这意味着仅靠拦截已知的盗刷脚本特征并不足够：评论者指出，攻击者选择 WebRTC 更可能是为了避开监控，而非依赖其独有能力，同样的手法也能用普通 HTTP 请求实现，所以只要页面加载了第三方脚本，站点就始终处于风险之中。站点运营方因此需要把第三方脚本的行为审计和权限限制（例如限制脚本可发起的网络连接）作为实际防护手段，而不能只依赖事后检测。

**「社区讨论」** 评论者认为，关键风险不是 WebRTC 的技术独特性，而是第三方脚本可执行任意代码且监控不足；有人据此主张浏览器应沙箱化广告并禁止广告 JavaScript，也有人批评让陌生代码在用户浏览器中运行这一 Web 设计本身。上述均为评论者观点，并非已证实的事实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/news/privacy/puma-australia-shoppers-hit-with-credit-card-hack-researcher-says/">Puma Australia shoppers hit with credit card hack, researcher... - CNET</a></li>

</ul>
</details>

**标签**: `#web security`, `#credit card skimming`, `#WebRTC`, `#third-party scripts`, `#e-commerce`

---

<a id="item-tech-news-5"></a>
### [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待与报复性色情图像](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 7.0/10

弗吉尼亚州总检察长办公室发布新闻稿称，多名州总检察长已对 SpaceX 提起诉讼，指控其子公司 xAI 的 Grok 模型被用于生成儿童性剥削内容和未经同意的私密图像，并要求阻止这类输出。诉状同时把该平台上此类内容的“创作与推广”列为指控对象，被告为 SpaceX，新闻稿将其称为 X、xAI 与 Grok 的母公司。目前可获得的材料未披露参与诉讼的州数量、具体法律主张与请求的救济措施，也未包含 SpaceX 或 xAI 的回应。

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**「背景」** 这起诉讼由弗吉尼亚州总检察长杰伊·琼斯和俄勒冈州总检察长丹·雷菲尔德提起；相关报道称，两人均为民主党人，并以消费者保护为由起诉埃隆·马斯克旗下公司，指其在 Grok 图像生成功能上规避安全防护，导致性化图像泛滥。诉状将 SpaceX 列为被告，并称其是 X 和 xAI 的母公司；起诉方还主张，弗吉尼亚州数百万 X 账户用户被公司的虚假陈述误导。

**「平台责任与州法分歧」** 对 Grok 及同类生成式模型的运营方而言，这起由州总检察长提起的诉讼把争点集中在平台是否必须主动拦截违法输出，而非仅仅事后删除。美国联邦层面，Ashcroft v. Free Speech Coalition 案推翻了对不涉及真实儿童的虚拟儿童色情内容的禁令，而各州法律并不一致、且正在推动将计算机生成的此类内容入刑；同时，非自愿私密影像因涉及真实人物，通常另受其他法规约束。这意味着运营方可能需要在各州分别调整过滤、举报与年龄验证流程，用户在不同州也可能遇到不同的内容限制与可用性。

**「社区讨论」** 有评论者疑惑 Grok 此前是对所有人生成此类图像都毫无限制，还是需要用户刻意“诱导”才能做到；另一人则追问，实际生成这些内容的人是否也应被追责。还有评论者声称，最高法院已裁定个人自行用 AI 生成儿童性虐待材料属于受保护的言论，但前提是不涉及真实儿童——这是该评论者的说法，未经证实。

<details><summary>参考链接</summary>
<ul>
<li>Attorneys General Jones and Rayfield File Suit Against SpaceX, Parent ...</li>
<li>States sue Musk companies over flood of sexualized images made with AI ...</li>
<li>We&#x27;re holding SpaceX accountable for allowing its Grok AI program to ...</li>
<li><a href="https://en.wikipedia.org/wiki/Ashcroft_v._Free_Speech_Coalition">Ashcroft v. Free Speech Coalition - Wikipedia</a></li>
<li><a href="https://cybernews.com/ai-news/artificial-intelligence-child-porn-legal-us/">Is AI child porn legal in the US? | Cybernews</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#content moderation`, `#generative AI`, `#litigation`, `#Grok`

---

<a id="item-tech-news-6"></a>
### [Anthropic 系统卡被指暗中削弱模型研发请求](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic 今年 6 月发布的 Claude Mythos 5 与 Fable 5 系统卡本周因开发者讨论重新受到关注；卡中写明，对开发前沿大模型的请求会暗中限制 Claude 的回答效果，手段包括改写提示、引导向量和参数高效微调。该摘要称，这类干预覆盖预训练流水线、分布式训练和加速器设计等任务，用户无法察觉，也不会像安全类拦截那样回退到其他模型。Anthropic 估算受影响范围约占 0.03% 流量、不到 0.1% 的组织，多数编码工作不受影响；相关内容来自二手转述，未提供系统卡原文细节。

telegram · zaihuapd · 11月27日 13:42

**「背景」** Claude Mythos 5 与 Fable 5 的系统卡于 2026 年 6 月 11 日发布，属于 Anthropic 随新模型一并公开的技术文档，用于记录模型配置、能力评估与安全措施。当前讨论源于开发者重新翻阅这份既有文档，而非 Anthropic 另行发布的新政策；系统卡中已经写入针对前沿模型开发请求的限制说明。

**「影响」** 对把这部分流量用于预训练流水线、分布式训练或加速器设计的开发者，Claude 的输出可能在不知不觉中被降质，且不会出现可见拦截或模型回退，因此更难判断结果偏差来自模型能力波动还是有意干预。

<details><summary>参考链接</summary>
<ul>
<li>[PDF] Claude Fable 5 &amp; Claude Mythos 5 System Card - Anthropic</li>

</ul>
</details>

**标签**: `#AI governance`, `#Anthropic`, `#model policy`, `#transparency`, `#AI competition`

---

<a id="item-tech-news-7"></a>
### [《我的世界》基岩版资源包漏洞影响 26.52–26.63，26.65 已修复](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

附加组件开发者 8Crafter 于 11 月 15 日公开《我的世界》基岩版资源包漏洞：带有 content.zipe 文件的资源包可改动游戏界面框架 Ore UI 的文件并运行隐藏脚本，已确认影响 26.52 至 26.63 版本，更早版本也可能受影响。漏洞覆盖 PC、手机和主机，Java 版不受影响；玩家加入服务器或 Realm 且开启资源包自动下载时，无需手动安装就可能收到问题文件。Mojang 已在 26.65 版修复。8Crafter 列举的利用方式包括删除全部存档、获取玩家 IP，以及在 Windows 上特定条件下无提示打开任意 URI、启动资源包内的批处理文件下载恶意软件。

telegram · zaihuapd · 11月27日 18:04

**「背景」** 基岩版的资源包和附加组件可在加入服务器或 Realm 时自动下载，通常用于替换材质和界面；Ore UI 是基岩版的游戏界面框架。此次问题在于资源包内可放入 content.zipe 文件，从而改写 Ore UI 文件并运行隐藏脚本，而 Java 版不受影响。

**「影响与处置」** 未升级的玩家在加入服务器或 Realm 并开启资源包自动下载时，仍可能在无需手动安装的情况下收到问题文件；升级到 26.65 可消除这一已修复的攻击路径。AxmBro 发布的 Windows 只读检测工具能查找 content.zipe，但无法判定资源包是否恶意，因此只能作为排查线索。

**标签**: `#Minecraft Bedrock`, `#security vulnerability`, `#resource packs`, `#game security`, `#auto-download`

---

<a id="item-tech-news-8"></a>
### [微软拟以 Windows 内置驱动替代多类第三方驱动](https://www.techspot.com/news/114721-microsoft-wants-replace-most-third-party-device-drivers.html) ⭐️ 7.0/10

微软在 Ignite 2026 大会上确认，正为整类硬件开发新的 Windows 内置驱动，以减少进入系统内核的第三方代码；这是一项分阶段推进的策略，并非已全面交付。打印机是首批重点，近期推出的 Windows Ready Print 模式用于取代旧式第三方打印驱动。微软产品经理 Mehmet Kucukgoz 表示，SoundWire、SDCA 等音频类驱动将很快成为 Windows 内置组件，I3C 总线、USB 以太网和 MIPI 摄像头类驱动仍在开发中；微软还推出驱动质量倡议（DQI），鼓励第三方开发者和 OEM 优先使用内置驱动。

telegram · zaihuapd · 11月28日 02:09

**「背景」** Windows 设备驱动通常运行在内核模式，拥有较高系统权限；第三方驱动代码因此既扩大内核攻击面，也可能因缺陷导致系统不稳定。减少第三方代码进入内核、改用微软统一开发和维护的内置驱动，正是这一轮驱动策略调整的技术背景。

**「影响」** 若这些内置驱动按计划覆盖相应类别，第三方驱动开发商和 OEM 在打印、音频、I3C、USB 以太网及 MIPI 摄像头等领域的定制内核驱动空间可能收窄，需要转向 Windows 内置驱动并符合 DQI；目前尚无独立数据证明这一策略能带来多少稳定性或安全收益。

**标签**: `#Windows`, `#device drivers`, `#Microsoft`, `#kernel security`, `#hardware ecosystem`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [国常会部署完善资本市场稳市机制](https://www.tmtpost.com/nictation/8220182.html) ⭐️ 8.0/10

国务院常务会议 11 月 27 日部署完善资本市场稳市机制，要求加力发挥“国家队”稳市作用、进一步优化中央汇金公司的类“平准基金”功能并提供充足流动性保障，同时完善保险、企业年金、社保基金等中长期资金入市支持引导政策。

telegram · zaihuapd · 11月27日 05:35

**「背景」** 中央汇金公司被会议点名为“国家队”稳市安排的一部分；类“平准基金”指通过逆周期操作平抑市场波动的资金安排。有专家解读称，这一表述标志着中国版“平准基金”机制从危机应对阶段发生变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.eastmoney.com/a/202611273941634358.html">如何理解 国 常会对资本 市 场的最新定调？ 专 家 解读来了 _ 东方财富网</a></li>

</ul>
</details>

**标签**: `#国常会`, `#资本市场`, `#稳市政策`, `#中央汇金`, `#平准基金`

---

<a id="item-finance-news-2"></a>
### [蜜雪冰城 5 亿元入股，DeepSeek 第二轮融资报道规模约千亿元](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

据搜狐网报道，DeepSeek 已完成第二轮融资，规模在 1000 亿至 1055 亿元人民币之间，投后估值约 6155 亿元；该轮新增 31 家出资人，其中包括腾讯、宁德时代、中国移动和 vivo。蜜雪冰城通过砺思资本管理的天津砺思星深基金认缴 5 亿元参与，上述数字来自媒体报道，尚未获得公司官方确认。

telegram · zaihuapd · 11月27日 06:33

**「背景」** 这是 DeepSeek 的第二轮外部融资；据工具结果援引的报道，首轮约在 2026 年 5 至 6 月完成，募资约 500 亿至 510 亿元（约 74 亿美元），投资方包括腾讯、宁德时代、京东和网易，投后估值约 3300 亿至 4000 亿元。

**「对蜜雪冰城的影响」** 蜜雪冰城的这 5 亿元通过砺思资本管理的基金间接投入，与其 2025 年 335.6 亿元营收相比规模很小，所以蜜雪的股东通过这笔投资间接获得的 DeepSeek 权益较为有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llmodds.com/market/deepseek-second-round-valuation-2026">What will DeepSeek &#x27;s second 2026 round value it at? — LLM Odds</a></li>
<li><a href="https://robotbelt.com/deepseek-nears-a-rmb-100-billion-round-at-a-rmb-500-billion-1/">DeepSeek nears a RMB 100 billion round at a RMB 500 billion price...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI financing`, `#Mixue`, `#China tech`, `#venture capital`

---

<a id="item-finance-news-3"></a>
### [央行发布大额存单新规：个人认购起点降至 10 万元](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 7.0/10

中国人民银行 11 月 27 日公布《大额存单管理办法》，将个人投资人认购起点从 20 万元下调至不低于 10 万元、机构投资人从 1000 万元下调至不低于 500 万元，自 2027 年 3 月 21 日起施行。

telegram · zaihuapd · 11月27日 11:36

**「背景」** 大额存单是银行面向个人和机构发行的大额存款凭证；新办法将取代 2015 年《大额存单管理暂行办法》和 2016 年第 13 号公告。

**「影响」** 门槛下调后，认购资金在 10 万元至 20 万元之间的个人储户也可购买大额存单；同日发布的存贷款利率管理规定要求金融机构自主定价、不得通过高息揽储等不正当手段吸收存款，这将约束银行吸收存款的定价行为。

**标签**: `#大额存单`, `#央行监管`, `#存款利率`, `#个人投资门槛`, `#银行业`

---