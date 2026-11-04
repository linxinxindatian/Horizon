---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04
lang: zh
---

> 从 53 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [Postman 被指静默安装 AI 插件并共享 API 数据](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen 3.8 27B 在笔记本上复现权重解读示例](#item-tech-news-2) ⭐️ 8.0/10
3. [Honnibal 指 Astra 读写 Qwen 权重提升说法误导](#item-tech-news-3) ⭐️ 8.0/10
4. [Stringman：800 美元的开源房间级线缆抓取机器人](#item-tech-news-4) ⭐️ 7.0/10
5. [在数据中心规模化运行 Mac 的运维变通方案](#item-tech-news-5) ⭐️ 7.0/10
6. [现代引擎跑在 90 年代硬件上，能击败 1996 年的卡斯帕罗夫吗？](#item-tech-news-6) ⭐️ 7.0/10
7. [Colsto 演示用飞机声与 ADS-B 定位视频地点](#item-tech-news-7) ⭐️ 7.0/10
8. [Debian 新队列试用 LLM 包审查引发争议](#item-tech-news-8) ⭐️ 7.0/10
9. [十年 ML 论文被整理成按主题索引的图谱](#item-tech-news-9) ⭐️ 7.0/10
10. [普京要求俄私营数据中心预留 10%算力](#item-tech-news-10) ⭐️ 7.0/10
11. [传英伟达要求数据中心中企新合同占比不超 49%](#item-tech-news-11) ⭐️ 7.0/10
12. [OpenAI 称 ChatGPT 搜索查询量达 Google 两成](#item-tech-news-12) ⭐️ 7.0/10

**财经新闻**
1. [黑石总裁称 AI 基础设施建设需更多股权融资](#item-finance-news-1) ⭐️ 7.0/10
2. [广州拟禁止房东加收租房水电费](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Postman 被指静默安装 AI 插件并共享 API 数据](https://github.com/postmanlabs/postman-app-support/issues/14370) ⭐️ 8.0/10

一则发布在 Postman GitHub 支持仓库的问题报告指控，Postman 会静默安装 AI 插件，并尝试共享全部 API 数据，涉及使用该工具管理请求和密钥的开发者。相关讨论随后在 Hacker News 发酵，但现有材料仅为问题报告与社区评论，尚无独立验证，材料中也未见 Postman 的公开回应。指控的具体范围、触发条件和受影响版本仍不清楚。

hackernews · sidgarimella · 11月3日 17:22 · [社区讨论](https://news.ycombinator.com/item?id=50354960)

**「背景：MCP 插件与启动钩子机制」** Postman 桌面版此前已通过本地插件（skills）和远程 MCP 连接，把 API 调用能力接入 Codex、Claude Code 等编码代理；这类插件需要写入启动钩子，并在本机留下“信任记录”才能自动执行。据 issue \#14370 的描述，触发安装的是 \`auto-existing-upgrade\` 升级流程，涉及 Postman 桌面版 12.33.4、Codex 插件 1.1.0 等组件——换言之，争议发生在一个由应用自身管理插件安装与钩子信任的既有机制之上，而非一次独立的外部入侵。

**「合规团队的应对选择」** 按照该 issue 与评论描述的行为，凡是用 \{\{secret\}\} 这类模板变量注入密钥的团队，其明文秘密都可能随请求日志一并发出；而评论者称，一旦阻断该出站端点，整个应用就无法正常工作，因此团队难以做到只在本地保留敏感数据。对需要满足合规要求的组织（如医疗健康行业），现实选项是审计出站流量或迁移到请求定义保存在本地、不上传云端的工具——Bruno 即以本地、开源、集合存入 git 且不做云同步作为 Postman 的替代方案。

**「社区讨论」** 评论中，primitivesuave 声称 Postman 会记录每次 API 请求（包括查询参数），模板变量 \{\{some\_secret\}\} 的真实值也会被发往 Postman 服务器，阻断该日志端点还会使应用无法正常工作，并称这是调查 HIPAA 合规时发现的。bottombutton 表示其医疗机构的网络安全团队因此将 Postman 除名、团队转用 Bruno；这些是个人经验和指控，未获独立核实，其他评论则主要批评 Postman 臃肿并肯定 Bruno 的 Git 存储方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/postmanlabs/postman-app-support/issues/14370">[SEVERE] Desktop auto-installs Codex/Claude plugins ... - GitHub</a></li>
<li><a href="https://aiweekly.co/alerts/postman-desktop-silently-installs-plugins-into-codex-claude-code">Postman Desktop Silently Installs Plugins Into Codex, Claude ...</a></li>
<li><a href="https://www.usebruno.com/">Bruno - The Git-Native API Client</a></li>

</ul>
</details>

**标签**: `#Postman`, `#privacy`, `#API tooling`, `#security`, `#developer tools`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B 在笔记本上复现权重解读示例](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10

Simon Willison 报告，他在笔记本上以 17GB 的 Q4\_K\_M 量化版运行 Qwen 3.8 27B，复现了 Rikiya Takehi 等人一项被作者归为博客文章、但形式接近论文的研究中的一个无工具示例：只输入一个 10x10 游戏策略网络的原始浮点权重，让模型判断它训练自哪款游戏。该模型在调高 LM Studio 上下文后运行了 46 分 12 秒、消耗 43,506 个推理 token，识别出 Pac-Man 并给出 72% 置信度；Willison 称它还识别出了 Pong。该研究还声称 GPT-6 Astra 能直接修改权重，例如无需梯度、只编辑 Qwen3.5-0.8B 的 0.016% 权重，就把 MATH-500 从 7.9% 提升到 48.1%。不过 Matthew Honnibal 认为论文把无工具解读与借助代码修改两类能力混在一起，因而有误导性；Sean Goedecke 则拆解了 Qwen3.5-0.8B 的改权重示例，指出其步骤与人类研究者会做的一致；Willison 的复现本身只是单个示例的轶事，不能独立验证这类解读或修改是否普遍可靠。

rss · Simon Willison · 11月3日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50355251)

**「背景」** 所谓“权重空间编程”（Weight-Space Programming），是指 LLM 不运行代码、不调用工具，仅阅读以文本浮点数形式给出的神经网络权重，来判断网络被训练来做什么，或直接修改权重。该说法出自 Rikiya Takehi 等人一篇被作者归类为博客、但结构接近论文的文章；文章称 GPT-6 Astra 能凭原始权重识别网络功能，并通过改动 Qwen3.5-0.8B 的 0.016% 权重把 MATH-500 从 7.9% 提升到 48.1%。论文同时混合了“无工具读权重”和“借助代码改权重”两类任务，这也成为外界质疑其结论的焦点。

**「影响」** 对想在本地复现这类实验的开发者，直接限制是上下文和等待时间：LM Studio 默认 8192 上下文会报错，需要调高，单次 Pac-Man 判断耗时 46 分钟并产生 4.3 万推理 token，还需调高请求超时，因此它更适合作为验证性实验而非交互式工具；同时应把模型输出视为待核验的假设，而不是权重分析结论。

**「社区讨论」** 评论者对“能解读权重”是否等于“解读正确”提出质疑：variaga 借用莎士比亚《亨利四世》的台词反问，任何人都可以声称自己能解读权重，但关键是这些解读会不会应验；data-ottawa 则追问 Qwen 3.8 能否修改同代 Qwen 3.8 的权重，以及其中有多少是训练所得、多少是真正理解。zkmon 称赞 Qwen 3.8 27B 在人类充当架构师时能完成接近前沿模型的工作，但这属于使用体验，不是对上述复现的验证。

**标签**: `#weight-space programming`, `#LLM interpretability`, `#model weights`, `#Qwen`, `#AI research`

---

<a id="item-tech-news-3"></a>
### [Honnibal 指 Astra 读写 Qwen 权重提升说法误导](https://honnibal.dev/blog/astra-read-write-misleading) ⭐️ 8.0/10

Matthew Honnibal 发表文章，批评“Astra 能读写 Qwen 权重并借此提升 Qwen”的说法具有误导性。Hacker News 讨论中，一位自称从事机制可解释性研究的读者称，原结果实际只是减少推理循环，而非让 Qwen 更擅长数学，并认为这可以通过简单的 steering 方法处理 &lt;/think&gt; token 概率过低的问题。另有评论者指出，原帖正文其实说明了相关限制，问题更多出在标题和摘要；也有人认为该做法是对既有技术的再包装。

hackernews · syllogism · 11月3日 12:21 · [社区讨论](https://news.ycombinator.com/item?id=50351111)

**「背景」** 这里所说的“权重编辑”是指不经梯度下降或完整训练循环而直接修改模型参数；被批评的原始文章声称，Astra 能直接读写 Qwen 的权重，并通过一次约 0.016% 的“循环方向”参数修改，在不重新训练的情况下提高 MATH-500。该文将这套做法称为 Weight-Space Programming，还称 Astra 可仅凭原始权重判断网络训练目标，并能从零写出小型游戏网络。

**「影响」** 对评估权重编辑的开发者来说，应把“减少推理循环”与“数学能力提升”分开测试，并加入简单 steering 或未编辑基线；否则容易把修复 &lt;/think&gt; 生成概率误判为模型能力改进。

**「社区讨论」** 一位自称从事机制可解释性研究的评论者认为，原结果只是降低推理循环，而 &lt;/think&gt; 概率过低可用简单 steering 修复；另一位评论者则称原帖正文已说明这些限制，真正误导的是标题和摘要。还有评论者认为 Astra 的做法只是对既有权重编辑或 steering 技术的再包装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explore.n1n.ai/blog/astra-read-write-weights-improve-qwen-2026-11-03">Astra Can Read and Write Weights to Improve Qwen</a></li>
<li><a href="https://www.qwe.edu.pl/tutorial/astra-read-write-weights-improve-qwen/">Astra Reads Qwen Weights: How to Apply the Fix</a></li>
<li><a href="https://daily.dev/posts/astra-can-read-and-write-weights-to-improve-qwen-swdnk0yoe">Astra can read and write weights to improve Qwen - daily.dev</a></li>

</ul>
</details>

**标签**: `#mechanistic-interpretability`, `#llm-weight-editing`, `#research-critique`, `#qwen`, `#ai-research-integrity`

---

<a id="item-tech-news-4"></a>
### [Stringman：800 美元的开源房间级线缆抓取机器人](https://neufangled.com/) ⭐️ 7.0/10

Stringman 是一个标价 800 美元的开源房间级线缆驱动机器人，末端为夹爪，项目在 Hacker News 上发布后由创作者 Nathaniel（用户名 nhnifong）出面答疑。它目前属于创客/DIY 项目，而非已量产的商业机器人；创作者称，拉力超过限制时系统会放线，遇到天花板风扇时通常可以降低工作区上限来避开。

hackernews · nharada · 11月3日 16:47 · [社区讨论](https://news.ycombinator.com/item?id=50354358)

**「背景」** Stringman 属于缆索驱动并联机器人（CDPR）：绞盘固定在房间高处，多根缆索共同悬挂并定位末端夹爪，因此不必像桌面机械臂那样受固定工作半径限制，也不需要移动底盘。项目方称，这种结构在单位成本可获得的工作空间体积上优于桌面机械臂和最简单的移动机器人。

**「影响」** 对想尝试房间级线缆机器人的 DIY 开发者，800 美元的开源方案提供了一个低成本参考平台；但创作者设定的张力放线限制也意味着复刻者需按有限拉力来规划抓取任务，不能把它当作可无限拉拽的起重设备。

**「社区讨论」** 评论区的实质讨论集中在扩展用途：一位用户描述了自己用两个高速绞盘和 USB 手柄搭的花园线缆升降装置，另一位则设想给这类机器人加上计算机视觉和小型旋转刀片来除草，并指出避开高秆植物和承受刀片作用力是难点。创作者本人也回应了安全性、天花板风扇和家庭使用等提问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neufangled.com/">Stringman from Neufangled Robotics</a></li>
<li><a href="https://neufangled.com/stringman">Stringman | Neufangled Robotics</a></li>

</ul>
</details>

**标签**: `#open-source hardware`, `#robotics`, `#cable-driven robots`, `#DIY maker`, `#Hacker News`

---

<a id="item-tech-news-5"></a>
### [在数据中心规模化运行 Mac 的运维变通方案](https://namespace.so/blog/mac-at-any-scale) ⭐️ 7.0/10

一篇面向 Mac CI/CD 与基础设施从业者的技术文章，梳理了在数据中心规模化运行 Mac 时，为绕过 Apple 平台限制而采用的运维变通方案。文章讨论的是规模化环境下的实际运维问题，而不只是单机使用。现有材料没有给出具体机型、macOS 版本或可复现的性能数据，因此相关结论仍应视为经验性总结。

hackernews · anner\_ · 11月3日 14:53 · [社区讨论](https://news.ycombinator.com/item?id=50352758)

**「背景」** 为 Apple 平台搭建 CI/CD 时，构建、测试和代码签名都依赖 xcodebuild 与 macOS Keychain 等只能在苹果原生系统上运行的组件，因此团队通常要部署专用 Mac 机器或云端 Mac 实例，很难用 Linux 容器直接替代（tool-1-2）。随着并行测试和多系统版本矩阵的需求增长，团队需要在 GitHub Actions 之类托管 macOS runner 与自建 Mac 节点之间，权衡 Xcode 控制权、缓存、签名和运维成本（tool-1-3）；苹果开发者论坛上也有团队在咨询如何搭建大规模 macOS 测试农场（tool-1-1）。

**「影响」** 有社区经验指出，Mac 启动后可能停在需要密码解锁的界面，因此运行 macOS CI/CD 的团队必须把自动登录或远程解锁纳入节点运维流程，并在安全策略上做取舍。

**「社区讨论」** 有评论者认为，Apple 缺少面向数据中心的服务器产品，团队为平台限制支付了高昂的运维成本，并批评其自动化工具不足。另有评论者用十多前年 iOS 代码审查依赖一台 MacBook、以及家用 Mac mini 服务器启动后必须解锁的经历，补充了类似限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/forums/thread/830383">Scalable macOS CI/CD infrastructur… | Apple Developer Forums</a></li>
<li><a href="https://totaltech.blog/macos-continuous-integration-delivery-guide">macOS for Continuous Integration and Delivery [CI/CD Guide]</a></li>
<li><a href="https://zilmac.com/en/blog/articles/github-actions-macos-26-self-hosted-mac-ci-guide.html">GitHub Actions macOS-26 or Self-Hosted Mac? 2026 CI Selection ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#macOS`, `#infrastructure`, `#data centers`, `#CI/CD`

---

<a id="item-tech-news-6"></a>
### [现代引擎跑在 90 年代硬件上，能击败 1996 年的卡斯帕罗夫吗？](https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html) ⭐️ 7.0/10

Nicholas Carlini 的文章提出一个反事实问题：如果把现代国际象棋引擎放到 1990 年代的硬件上运行，它能否在 1996 年击败卡斯帕罗夫。文章借此考察现代引擎的棋力有多少来自评估函数、搜索算法等算法层面的进步，而非单纯的计算能力。这是一篇分析性推演，并非发布新引擎或给出实测对局结果，因此它提出的是论证而非可验证的比赛结论。

hackernews · markusw · 11月3日 07:56 · [社区讨论](https://news.ycombinator.com/item?id=50349276)

**「背景」** 1996 年 2 月 10 日，IBM 的 Deep Blue 在一局比赛中首次击败卫冕世界冠军 Garry Kasparov，但最终输掉整场对抗；1997 年，它以 3.5 比 2.5 赢得重赛。为达到这一水平，IBM 投入数百万美元研发专用硬件，这也正是 Carlini 文章反事实问题的起点：若把现代引擎的算法放到 1990 年代的 Pentium 级硬件上，结果会如何。

**「影响」** 对试图在低算力设备上部署棋类引擎的开发者而言，相关讨论强调现代引擎的评估与搜索是在大量算力条件下调优的；按比例削减搜索深度并不会自动保留同等棋力，而需要重新平衡评估与搜索的取舍。

**「社区讨论」** 评论者 k2052 认为文章关于算法进步的主论点成立，但指出低算力下现代引擎的评估与搜索取舍会暴露明显弱点，卡斯帕罗夫团队很可能加以利用。FartyMcFarter 质疑文中关于特级大师与业余棋手分析着法数量相近的说法；Sharlin 则纠正了文中对 Pentium Pro 与 Pentium MMX 的定位，指出 Pro 是首个 P6 乱序架构，而 MMX 只是加大 L1 并加入 MMX 指令集的 P5。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html">Could a modern chess engine on a Pentium have defeated ...</a></li>

</ul>
</details>

**标签**: `#chess engines`, `#algorithmic improvements`, `#hardware vs software`, `#AI history`, `#Hacker News discussion`

---

<a id="item-tech-news-7"></a>
### [Colsto 演示用飞机声与 ADS-B 定位视频地点](https://simonwillison.net/2026/Nov/3/a-sound-that-leaks-your-exact-location/) ⭐️ 7.0/10

Simon Willison 在博客中推介了 Colsto 的一段 YouTube 演示：从视频音轨中提取几乎听不见的飞机背景声，分析其多普勒曲线，再与 ADS-B 航班数据交叉比对。演示称，结合飞机的速度、距离以及不同航班之间的间隔，可以推断视频的精确拍摄地点。按其描述，该方法依赖视频中可提取的飞机噪声和可用的 ADS-B 数据；Willison 的条目只是简短推介，未展开完整技术细节。

rss · Simon Willison · 11月3日 05:32

**「背景」** 该方法依赖两个公开可得的基础条件：一是多普勒效应，即声源与录音点相对运动会使音调发生可测量的偏移；二是 ADS-B，飞机持续公开广播自身位置、高度和速度等飞行数据。据相关报道，创作者 colsto 于 2026 年 11 月 2 日发布的视频演示了如何从音频频谱图中提取螺旋桨飞机的音调特征，再将其与当天的 ADS-B 航迹比对来缩小录音地点范围。

**「影响」** 对隐私与安全读者而言，这意味着即使画面或文件元数据没有暴露地点，音轨中的环境声也可能成为定位线索；处理敏感视频时，应把环境音纳入发布前审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=UytYrhYLOKI">I discovered a sound that leaks your exact location (and it&#x27;s ... Planes Leak Your Location: Doppler Audio Geolocation Explained I discovered a sound that leaks your exact location (and it&#x27;s ... YouTuber Reveals How Sounds Humans Cannot Hear Can Expose a ... YouTuber discovers aircraft noise trick that can geolocate ... New Technique Pinpoints Video Locations Using Airplane So... colsto - YouTube</a></li>
<li><a href="https://maxintel.org/aircraft-doppler-audio-geolocation-2026.html">Planes Leak Your Location: Doppler Audio Geolocation Explained</a></li>

</ul>
</details>

**标签**: `#OSINT`, `#privacy`, `#geolocation`, `#audio-forensics`, `#ADS-B`

---

<a id="item-tech-news-8"></a>
### [Debian 新队列试用 LLM 包审查引发争议](https://lwn.net/Articles/1103674/) ⭐️ 7.0/10

Debian 的 DFSG、许可与新软件包团队（DFSG 团队）已开始使用 LLM 生成对进入 Debian 新队列（new queue）的软件包的审查意见。这一做法发生在 Debian 今年 8 月就 LLM 使用举行全面决议投票之后：项目选出了八项选项中的第五项，即“负责任地使用生成式 AI”，为 LLM 的使用打开了空间。相关实践已引发反对意见，并带出应如何划定 LLM 生成内容使用边界的问题。由于来源为付费内容且摘录缺少技术细节，LLM 在审查流程中的具体使用方式、披露要求和适用范围尚不明确。

rss · LWN.net · 11月3日 16:28

**「背景」** Debian 对生成式 AI 的使用已争论多年，并在 2026 年 8 月通过一般决议，从八个选项中选择了第五项“负责任地使用生成式 AI”，为项目内使用 LLM 打开了政策空间。所谓“新队列”（new queue）是新软件包获准进入 Debian 归档前接受审查的等待队列；相对较新的 DFSG、许可与新软件包团队负责相关审查，这次争议正是该团队开始在审查中引入 LLM 之后出现的。

**「影响」** 对向 Debian 新队列提交软件包的贡献者而言，他们收到的审查意见可能包含 LLM 生成的内容，而目前项目尚未明确这类内容应如何标注、由谁复核以及责任如何界定；这使提交者与审查团队都需要面对审查结论可信度和申诉依据的问题。

**标签**: `#Debian`, `#LLM governance`, `#open source policy`, `#package review`, `#AI in software engineering`

---

<a id="item-tech-news-9"></a>
### [十年 ML 论文被整理成按主题索引的图谱](https://www.reddit.com/r/MachineLearning/comments/1xmk8rx/we_turned_10_years_of_ml_papers_into_one_page_per/) ⭐️ 7.0/10

一项名为 Scime Atlas 的研究导航工具在 Reddit 上发布，将 ICML、NeurIPS、ICLR、CVPR 和 AAAI 自 2016 年以来约 10.9 万篇被接收论文归入约 1,260 个主题，并从其中 7.9 万篇论文全文中提取结果表格与消融实验。每个主题页展示按时间排列的各基准最佳报告数值及对应论文、近期论文的消融结果（包括效果变差的实验）、近期论文用作对比的基线，以及相关 arXiv 预印本和 BibTeX 文件。开发者明确说明提取并不完美、不同论文的数字未必可比，应将其视为起点而非排行榜，且 2026 年论文的基准数值与消融结果尚未纳入，当前记录主要反映截至 2025 年的论文。工具免费、无需注册。

reddit · r/MachineLearning · /u/latenticlabs · 11月3日 05:09

**「背景」** 在机器学习研究中，要判断某个方向“做到哪一步”，通常需要跨大量论文比对基准成绩和消融实验，而顶级会议逐年增长的接收论文量让这件事越来越费力。据 scime 站点介绍，其 atlas 已按研究领域和主题对 ICML、NeurIPS、ICLR、CVPR、AAAI 2016–2026 年的 108,967 篇接收论文做分组展示，并能根据一句话描述定位研究想法所属的主题与最接近的论文。此次发布的新增部分是：每个主题页从论文全文中抽取结果表与消融记录，而不只是显示主题分组。

**「影响」** 对需要快速了解某个 ML 子领域进展的研究者，该图谱把分散在数万篇论文中的基准记录、基线选择与消融结论集中到单个主题页，并让每个数字链接回原论文以便核对。由于开发者承认抽取存在误差且跨论文数值不可直接比较，使用者应回到原文验证后再引用，而不应把页面上的“最佳数值”当作权威排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atlas.scime.ai/research">Machine learning and computer vision research map · 108,967 ...</a></li>
<li><a href="https://atlas.scime.ai/">scime atlas · AI Paper Atlas: research map of 108,967 machine ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#research literature`, `#benchmark tracking`, `#ablation studies`, `#research tools`

---

<a id="item-tech-news-10"></a>
### [普京要求俄私营数据中心预留 10%算力](https://www.reuters.com/technology/putin-orders-private-data-centres-set-aside-10-capacity-support-it-2026-11-02/) ⭐️ 7.0/10

俄罗斯总统普京签署总统令，要求俄境内非国有数据中心预留 10%的场地和计算能力，供政府在必要时调用。总统令要求俄罗斯数字发展部清查全国私营数据中心的可用资源，并成立专门委员会；该委员会可要求运营商释放预留资源，运营商须在接到通知后 24 小时内提供使用权限。经俄罗斯联邦安全局（FSB）批准，政府还可临时调用位于境外的数据中心资源。目前这是总统令层面的安排，具体执行细则、适用范围和启用条件尚未在源材料中说明。

telegram · zaihuapd · 11月3日 10:58

**「背景」** 据《基辅独立报》报道，此项总统令出台之际，乌克兰正持续以远程无人机攻击俄罗斯数据中心，数据中心因而成为俄方应急基础设施保护机制覆盖的对象。

**「影响」** 对私营数据中心和云服务商而言，需在容量规划中固定留出 10%资源，并准备在 24 小时内响应政府调用；这会压缩其可对外销售的算力余量，并要求预先设计快速移交访问权限的流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kyivindependent.com/putin-orders-russian-data-centers-to-reserve-capacity-to-assist-state-it-infrastructure/">Putin orders Russian data centers to reserve capacity to ...</a></li>

</ul>
</details>

**标签**: `#data centers`, `#cloud infrastructure`, `#tech policy`, `#digital sovereignty`, `#Russia`

---

<a id="item-tech-news-11"></a>
### [传英伟达要求数据中心中企新合同占比不超 49%](https://www.tomshardware.com/tech-industry/data-centers/nvidia-tells-data-center-operators-to-limit-business-from-chinese-customers-with-new-global-restrictions-report-claims-allegedly-restricted-to-49-percent-of-the-total-ensuring-51-percent-are-non-chinese-outfits) ⭐️ 7.0/10

据《金融时报》报道、经 Tom&\#x27;s Hardware 转述，英伟达据称已要求全球数据中心运营商将来自中国企业的业务占比限制在 49%以内，以保证至少 51%来自非中国企业。该要求据称仅适用于新签和未来合同，不影响已签订的租赁协议，并由销售团队和区域团队口头传达，尚无正式文件，英伟达也未确认。报道还提到，英伟达表示美国芯片是美国模型与应用厂商参与全球竞争的基础，现行美国政策鼓励云服务商基于美国基础设施承接各地业务。

telegram · zaihuapd · 11月3日 16:19

**「背景」** 美国此前已对销往中国的先进 AI 芯片设限；而此次报道所指的对象不是芯片出口本身，而是采购英伟达 GPU、再对外出租算力的数据中心运营商。据报道，该要求仅适用于新签及未来合同，不影响已签订的租赁协议，并且由销售团队和区域团队口头传达、未见正式文件，因此它与正式出口管制规则不同，目前仍属英伟达未正式确认的说法。

**「受影响方与执行难点」** 对于批量采购英伟达芯片并对外出租算力的云服务商和 AI 基础设施运营商来说，如果这一报道属实，它们在新签合同中来自中国企业的业务占比将被限制在 49% 以内，同时至少 51% 的业务须来自非中国企业；而已签订的租赁协议不受影响，因此这些运营商需要在新合同审核和客户结构上作出调整。由于该要求据称仅由销售团队和区域团队口头传达、没有正式文件，运营商在执行时还面临标准不明、难以核验的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/1902df70-1380-4588-bad5-171352b575f2?syn-25a6b1a6=1">Nvidia orders data centre clients to reduce China exposure</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/nvidia-reportedly-restricts-chinese-access-112552007.html?fr=sycsrp_catchall">Nvidia Reportedly Restricts Chinese Access to AI Computing ...</a></li>
<li><a href="https://startupfortune.com/nvidia-tells-cloud-clients-to-cap-china-business-at-49-of-their-services/">Nvidia tells cloud clients to cap China business at 49% of ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI infrastructure`, `#export controls`, `#data centers`, `#semiconductors`

---

<a id="item-tech-news-12"></a>
### [OpenAI 称 ChatGPT 搜索查询量达 Google 两成](https://www.theverge.com/ai-artificial-intelligence/1025482/openai-says-chatgpt-is-catching-up-to-google-in-search) ⭐️ 7.0/10

OpenAI ChatGPT 消费级产品负责人 Adam Fry 周一表示，ChatGPT 处理的搜索查询量已达到 Google 的 20%。他限定该数字仅指触发网页检索的查询，不包含查词义等任务，且未说明 Google 数据的来源，因此这仍是 OpenAI 的单方面说法，尚无独立验证。作为参照，微软 CEO 纳德拉曾在 2023 年反垄断庭审中称 Bing 十余年只占约 3% 份额；OpenAI 上月已开始在 ChatGPT 中展示赞助商品的图片。

telegram · zaihuapd · 11月4日 02:22

**「背景」** 报道以 2023 年反垄断庭审中的说法作对比：微软 CEO 纳德拉称 Bing 经营十余年也只占约 3% 份额，这为理解 OpenAI 所称 ChatGPT 查询量达到 Google 20% 提供了参照。OpenAI 上月已开始在 ChatGPT 中展示赞助商品图片，显示其正在把搜索与商品推广结合。

**「搜索商业化与口径差异」** 对用户最直接的变化是搜索式查询正被商业化：OpenAI 上月已在 ChatGPT 中展示赞助商品的图片，而据 WIRED 报道，Adam Fry 曾演示用 ChatGPT 做咖啡机、办公椅等产品调研的购物场景，说明这类触发网页检索的查询正是付费推荐位的主要入口。同时，这个 20% 只统计触发网页检索的查询、且未说明 Google 数据来源，广告主和开发者无法将其当作可与 Google 查询量直接对标的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bigtechnology.com/p/openai-chatgpt-search-is-about-20">OpenAI: ChatGPT Search Is About 20 % of Google ’s, 250 Million...</a></li>
<li><a href="https://www.wired.com/story/openai-adds-shopping-to-chatgpt/">OpenAI Adds Shopping to ChatGPT | WIRED</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#search`, `#Google`, `#AI competition`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [黑石总裁称 AI 基础设施建设需更多股权融资](https://www.cnbc.com/2026/11/03/equity-ai-debt-blackstone-pimco-financing.html) ⭐️ 7.0/10

黑石总裁乔恩·格雷 11 月 3 日在香港金管局投资峰会上表示，AI 基础设施建设需要更多股权融资，因为贷款机构对 AI 行业和个别公司的贷款越来越集中。同场的 Pimco CEO 埃马纽埃尔·罗曼称，今年 AI 相关债务发行约 5500 亿美元，而全球公司债市场约 20 万亿美元；他引用预测称未来五年 AI 资本开支可能达 10 万亿美元。

rss · CNBC Finance · 11月3日 06:46

**「背景」** 这番表态发生在香港金管局主办的“全球金融领袖投资峰会”上；高盛在报告中预计，未来五年全球数据中心建设需要约 8.5 万亿美元资本开支，使融资来源和信贷市场承受能力成为讨论焦点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/videos/2026-11-03/blackstone-pimco-chiefs-debate-the-perils-of-ai-boom-video">Watch Blackstone , Pimco Chiefs Debate the Perils of AI ... - Bloomberg</a></li>
<li><a href="https://www.kucoin.com/news/flash/goldman-sachs-global-data-center-investment-to-reach-8-5-trillion-over-next-five-years">Goldman Sachs: Global Data Center Investment to ... - KuCoin</a></li>

</ul>
</details>

**标签**: `#AI infrastructure financing`, `#corporate debt markets`, `#private capital`, `#data center capex`, `#Blackstone`

---

<a id="item-finance-news-2"></a>
### [广州拟禁止房东加收租房水电费](https://www.21jingji.com/article/20261103/herald/060575406590d5720e27d585b9e1d1b1.html) ⭐️ 7.0/10

广州市人大常委会表决通过《广州市租赁房屋居民生活用水用电费用代收管理规定》，待广东省人大常委会批准后实施。规定禁止房东加价或变相加价收取水电费，包括按水电用量收取管理费、服务费；违者须退还多收费用，并可被处多收费用五倍以下罚款。

telegram · zaihuapd · 11月3日 10:18

**「背景」** 今年 8 月 24 日，广州市人大常委会已公布这项规定的草案，并向社会公开征求意见。按立法程序，市人大常委会表决通过的地方性法规，须报广东省人大常委会批准后才会生效实施。

**「影响」** 规定实施后，广州的租客可要求返还被违法加收的水电费用，房东和代收方则需按供水供电企业收费标准收费，否则面临退款和罚款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20260825/herald/4851fbb8ae951ec097867a759b573dae.html">21jingji.com/article/20260825/herald/4851fbb8ae951ec097867a759...</a></li>

</ul>
</details>

**标签**: `#Guangzhou`, `#rental housing regulation`, `#utility fees`, `#consumer protection`, `#local policy`

---