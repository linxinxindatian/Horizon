---
layout: default
title: "Horizon Summary: 2026-11-07 (ZH)"
date: 2026-11-07
lang: zh
---

> 从 48 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [Libghostty 1.0 发布：可嵌入的 Ghostty 终端核心](#item-tech-news-1) ⭐️ 7.0/10
2. [Firecracker VM 逃逸：PwnEscape 实践利用未启用 jailer](#item-tech-news-2) ⭐️ 7.0/10
3. [Linux 内核拟认证 lockdown 休眠镜像](#item-tech-news-3) ⭐️ 7.0/10
4. [月之暗面拟经欧洲云厂商租用逾 8000 颗 Blackwell GPU](#item-tech-news-4) ⭐️ 7.0/10
5. [百度开源文心 5.5 Flash Base：280B MoE、支持 100 万 Token 上下文](#item-tech-news-5) ⭐️ 7.0/10
6. [长江存储拟建第四厂，国产设备占比最高 70%](#item-tech-news-6) ⭐️ 7.0/10
7. [淘宝 MNN 开源 0.3B 端侧模型，INT4 仅 173 MB](#item-tech-news-7) ⭐️ 7.0/10

**科技博客**
1. [团队最好只配一名设计师](#item-tech-blog-1) ⭐️ 6.0/10

**财经新闻**
1. [CoreWeave 2032 年债券收益率突破 16%，AI 数据中心债务担忧升温](#item-finance-news-1) ⭐️ 8.0/10
2. [美联储戴利：可能需进一步加息，10 月新增就业 16.5 万](#item-finance-news-2) ⭐️ 7.0/10
3. [纳斯达克指数进入回调区间，单日跌逾 5%](#item-finance-news-3) ⭐️ 7.0/10
4. [六部门发文推动具身智能等前沿技术进入养老领域](#item-finance-news-4) ⭐️ 7.0/10
5. [Anthropic 据报下周启动 IPO 路演，拟 11 月 16 日当周挂牌](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Libghostty 1.0 发布：可嵌入的 Ghostty 终端核心](https://mitchellh.com/writing/libghostty-1-0) ⭐️ 7.0/10

Libghostty 1.0 已发布，它是 Ghostty 终端模拟器背后可嵌入的终端模拟核心，面向希望在自己应用中复用终端模拟能力的开发者。此次发布将该核心以 1.0 版本提供，但现有材料未披露具体的 API 变更、支持平台或兼容性细节。

hackernews · mfiguiere · 11月6日 23:30 · [社区讨论](https://news.ycombinator.com/item?id=50399933)

**「背景」** Ghostty 是一个用 Zig 编写的终端模拟器；其作者 Mitchell Hashimoto 将核心终端模拟功能抽成一个可跨平台复用的组件，这个组件就是 libghostty。据 Terminal Trove 对作者的采访，libghostty 的目标是让其他应用不必自行实现终端模拟内核，就能直接嵌入终端能力。此次 1.0 发布，意味着这一原本服务于 Ghostty 的内核以带版本号的独立库形式对外提供。

**「影响」** 对终端和开发者工具作者而言，Libghostty 1.0 提供了可复用的终端模拟核心，可集成到自己的终端应用或编辑器中，而不必从零实现终端模拟；评论者 amterp 称其自建终端项目因此节省了大量工作。

**「社区讨论」** Hacker News 评论整体正面：amterp 称其自建终端项目直接受益，IlikeMadison 称 Libghostty 促成了 Emacs 终端 Ghostel，JuniperMesos 则提到曾在 Android 项目中试用。Decabytes 提出一个技术疑问：项目为何选择 C，而不是采用带 C 风格接口的 Zig。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terminaltrove.com/blog/terminal-trove-talks-with-mitchell-hashimoto-ghostty/">Terminal Trove Talks with Mitchell Hashimoto - Terminal Trove</a></li>

</ul>
</details>

**标签**: `#terminal emulators`, `#Ghostty`, `#open-source libraries`, `#developer tools`

---

<a id="item-tech-news-2"></a>
### [Firecracker VM 逃逸：PwnEscape 实践利用未启用 jailer](https://pwn.ai/blog/firecracker-escape) ⭐️ 7.0/10

文章演示了如何在实际 Firecracker 虚拟机中利用已披露的 PwnEscape 漏洞实现逃逸，目标读者是依赖 Firecracker 做隔离的开发和运维人员。测试环境没有启用 jailer；Firecracker 的生产隔离还包含降权、命名空间和 seccomp，文章也提示，启用这些控制后要另行评估 VMM 被攻破后剩余的权限与资源。评论进一步指出，这不是新披露的漏洞，而是数周前公开的 PwnEscape 的实践利用，因此不能把本次演示直接等同于加固生产部署可被利用。

hackernews · SerCe · 11月6日 19:33 · [社区讨论](https://news.ycombinator.com/item?id=50397219)

**「背景」** 这篇“Part 2”并非披露一个新漏洞，而是演示如何在实际的 Firecracker 环境中利用此前已公开的 Linux 内核漏洞 PwnEscape（CVE-2026-99999）：控制 guest VM 的攻击者可借此造成 guest-to-host 内存泄露，并在受影响配置下尝试逃逸到宿主机。Firecracker 的生产隔离还依赖 jailer 进行降权，并用命名空间和 seccomp 限制进程；该演示未启用这些控制，因此其逃逸路径不能直接等同于加固后的生产部署。

**「生产部署的实际影响」** 对运行 Firecracker 的服务方而言，这篇文章的实际影响取决于是否启用 jailer：文章明确说明测试配置没有 jailer，因此演示证明的是攻破 VMM 后能获得该进程的权限，而不是生产隔离被直接突破。部署方应确认是否启用 chroot、命名空间、cgroups、权限丢弃和 seccomp，并在启用这些控制后单独评估 VMM 被攻破时仍可触达的资源。

**「社区讨论」** 讨论集中在影响范围：scoodah 希望文章进一步说明，在启用降权、命名空间和 seccomp 的 jailer 配置下，攻击者攻破 VMM 后还能拿到哪些权限和资源；markasoftware 强调这不是新漏洞，而是对已披露 PwnEscape 的实践利用。zX41ZdbW 表示可在其托管数百个数据库引擎的 ClickBench playground 上做 PoC，lrvick 则主张采用经过形式化验证的 Nova 微内核来缩小虚拟化层攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://socprime.com/blog/cve-2026-99999-analysis/">CVE-2026-99999: Critical Linux PwnEscape Flaw</a></li>
<li><a href="https://almalinux.org/blog/2026-10-16-pwnescape-cve-2026-99999/">PwnEscape (CVE-2026-99999): Patched kernels... | AlmaLinux OS</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md">firecracker/docs/jailer.md at main · firecracker-microvm ...</a></li>
<li><a href="https://www.pandastack.ai/blog/firecracker-jailer-explained/">The Firecracker Jailer Explained · PandaStack</a></li>

</ul>
</details>

**标签**: `#virtualization`, `#security`, `#Firecracker`, `#exploit`, `#systems`

---

<a id="item-tech-news-3"></a>
### [Linux 内核拟认证 lockdown 休眠镜像](https://lwn.net/Articles/1103190/) ⭐️ 7.0/10

Matthew Garrett 提出了一组 Linux 内核补丁，目标是让启用 lockdown 的系统能够休眠：恢复时认证从磁盘读回的内存镜像，并防止攻击者用旧内核绕过新保护。当前 lockdown 会禁用休眠，因为内核无法判断恢复的内存数据是否被篡改；加入降级攻击防护使实现更复杂。该补丁目前仅为邮件列表上的提案，尚未合入内核。

rss · LWN.net · 11月6日 18:51

**「背景」** Lockdown 是 Linux 内核的一个可选安全功能，用于限制对运行中内核的修改。休眠会把内存内容写入磁盘，恢复时再读回内存，而内核无法验证这些数据是否被篡改，因此 lockdown 一直禁用休眠功能。

**标签**: `#Linux kernel`, `#hibernation`, `#lockdown security`, `#downgrade attacks`, `#patch sets`

---

<a id="item-tech-news-4"></a>
### [月之暗面拟经欧洲云厂商租用逾 8000 颗 Blackwell GPU](https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html) ⭐️ 7.0/10

据 CNBC 援引知情人士报道，月之暗面正洽谈从欧洲新兴云厂商（neocloud）租用逾 8000 颗 Nvidia Blackwell GPU，主要用于推理，也涉及训练；目前处于谈判阶段，并非已交付。由于美国出口管制禁止 Blackwell 进口中国，通过海外云服务远程使用被视为绕道方案，有方案要求月之暗面比非中国买家多付 30% 至 50% 的预付款。白宫今年 7 月曾称该公司通过泰国设施获取过 Blackwell 芯片；报道未说明欧洲方案能否获得美方许可，也未给出时间表或合同金额。

telegram · zaihuapd · 11月6日 05:02

**「背景」** 美国出口管制禁止 Blackwell 芯片直接进口中国，通过境外云服务远程租用算力则被视为绕道途径。白宫今年 7 月曾称月之暗面经泰国设施获取过 Blackwell 芯片；据 CNBC 2026 年 8 月 19 日报道，中国 AI 公司通过海外渠道获取 Nvidia 先进算力已促使美国立法者讨论填补云访问缺口，Tech Times 同月报道称美国工业与安全局（BIS）也在审查此类境外云租赁。

**「成本与合规影响」** 若交易达成，月之暗面需比非中国买家多预付 30%–50% 的算力费用，即在取得算力之前就占用更多现金。承接此事的欧洲新兴云厂商则需要承担合规风险：美国出口管制禁止 Blackwell 进口中国，而借海外云服务远程使用被视为绕道途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>
<li><a href="https://www.techtimes.com/articles/323532/20260807/bis-targets-legal-cloud-compute-china-ai-firms-bypass-export-controls.htm">BIS Targets Legal Cloud Compute as China AI Firms Bypass ...</a></li>

</ul>
</details>

**标签**: `#Nvidia Blackwell`, `#Moonshot AI`, `#export controls`, `#AI compute`, `#cloud infrastructure`

---

<a id="item-tech-news-5"></a>
### [百度开源文心 5.5 Flash Base：280B MoE、支持 100 万 Token 上下文](https://www.news.cn/info/20261105/f3bbdb6854f5441ca9fb34062f213875/c.html) ⭐️ 7.0/10

据新华网报道，百度已正式开源基座模型文心 5.5 Flash Base。该模型采用 MoE 架构，总参数为 2800 亿，每个 Token 激活 140 亿参数，预训练使用 33.5 万亿 Token，预训练上下文最长为 128K，微调与推理则支持最长 100 万 Token 上下文。百度称，模型在注意力机制、专家路由和训练目标等环节做了系统性效率优化；但此次公布未包含基准测试结果、许可证条款或权重获取方式，实际能力与使用条件仍待确认。

telegram · zaihuapd · 11月6日 05:41

**「背景」** 稀疏混合专家（MoE）架构将模型划分为多个专家网络，每个 Token 只被路由到其中少数专家，因此“总参数量”和“每 Token 激活参数量”会相差很大。百度文心 5.5 Flash Base 的模型卡显示，该模型总参数为 2800 亿，每 Token 激活 140 亿；这种稀疏设计旨在保留较大模型容量的同时，降低单次推理的计算量。

**「影响」** 对需要长上下文微调或推理的开发者而言，100 万 Token 上下文是这一基座模型最具体的可用特性。但在许可证和权重获取方式明确前，开发者尚难判断它能否用于商业或生产环境，也无法独立核验其长上下文效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/baidu/ERNIE-5.5-Flash-Base">baidu/ERNIE- 5 . 5 - Flash - Base · Hugging Face</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#large language models`, `#MoE`, `#long context`, `#Baidu`

---

<a id="item-tech-news-6"></a>
### [长江存储拟建第四厂，国产设备占比最高 70%](https://www.reuters.com/world/china/chinas-top-flash-memory-chipmaker-targets-more-homegrown-tools-new-factory-2026-11-06/) ⭐️ 7.0/10

长江存储计划在武汉建设第四座工厂，预计 2027 年开工，目标是把国产设备采购比例提高到至少 60%、最高 70%，高于第三座工厂目前超过 50%的水平。新厂将生产超过 300 层的 NAND 闪存，主要面向数据中心和人工智能存储需求。报道指出，清洗、抛光和刻蚀设备预计是国产化的主要增量，但光刻、检测等先进设备仍依赖海外供应商。报道还称，长江存储在中国 NAND 市场份额已升至 38.5%、超过三星，未来三座新厂全部投产后整体产能有望翻倍。

telegram · zaihuapd · 11月6日 08:34

**「背景」** 长江存储是中国主要的 NAND 闪存制造商，美国出口管制使其设备采购的国产化成为扩产的关键环节。其三号工厂的国产设备占比目前超过 50%，新工厂 60%–70% 的目标是在这一基础上的进一步提高；但光刻、检测等先进设备仍依赖海外供应商。

**「影响」** 若该采购目标落实，清洗、抛光、刻蚀等环节的国内设备供应商是明确受益方向；但光刻和检测仍依赖海外设备，长江存储的扩产及先进 NAND 量产爬坡仍会受到美国出口管制和设备交付条件的约束。

**标签**: `#semiconductors`, `#NAND flash`, `#China tech`, `#export controls`, `#supply chain`

---

<a id="item-tech-news-7"></a>
### [淘宝 MNN 开源 0.3B 端侧模型，INT4 仅 173 MB](https://www.ithome.com/1/023/212.htm) ⭐️ 7.0/10

淘宝 MNN 团队于 11 月 6 日开源约 3 亿参数的端侧模型 MNN-Pocket-0.3B，并称其在 iPhone 18 Pro 上可完全离线运行，平均解码约 350 token/s。该模型采用 28 层结构，词表由 151K 精简至 64K，INT4 部署文件为 173 MB；团队设定的目标是峰值内存低于 300 MB、解码超过 200 token/s。团队按预训练、后训练和端侧部署分别开源了多个版本。上述速度和内存数据均为团队自述，尚未见到独立验证。

telegram · zaihuapd · 11月6日 15:13

**「背景」** 端侧小模型要在手机本地完全离线运行，通常需要同时控制参数规模、量化精度和词表大小；INT4 量化可压缩权重体积，较小的词表则能减少嵌入层占用。MNN 是淘宝团队维护的移动端推理框架，此次发布可理解为针对手机内存和解码速度，在该框架上做的模型适配。

**「对开发者的影响」** 对移动端开发者而言，173 MB 的 INT4 文件和离线运行意味着可以把模型直接打包进应用，但实际体验仍取决于设备内存、量化精度和 MNN 运行时适配；在独立基准出现前，350 token/s 应视为团队目标环境下的参考值。

**标签**: `#on-device AI`, `#small language models`, `#MNN`, `#model compression`, `#mobile inference`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [团队最好只配一名设计师](https://seangoedecke.com/working-with-designers/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月7日 00:00

**「背景」** Sean Goedecke 喜欢与设计师合作，认为其价值一眼可见，文化差异反而有益；但据其经验，一个团队有多名设计师会带来麻烦，设计系统也造成组织与工程摩擦。

**「方案」** 他的核心观察是：设计分歧只能落到“品味”上，且任何设计改动都影响用户对整体产品的感知，难以像工程分歧那样用延迟、缺陷等指标裁决。他最糟的经历是产品先后有三名设计师：首位离开后，两位资深设计师彻底重做产品，迫使他重写大部分前端样式，随后两人不断互相推翻，每页来回三四次，直到截止前约一周才由两层管理层冻结设计。设计系统是规模化保持一致的方案，但存在激励错位：系统团队追求组件永远漂亮，产品团队要满足丑陋或特殊需求；嵌入式设计师的微小改动又让双方不满，导致团队重写组件、用 CSS 覆盖样式，并在升级时反复被破坏。兼容性也棘手：设计系统常用最新框架，而公司前端是难升级的混合技术栈，例如设计侧为 React、落地侧为纯 HTML/CSS，版本差异使“拼乐高”得不到设计师所见效果，工程师只能自行翻译可用特性。作者仍认为设计系统优于其他已知方案，只是希望设计师体谅一线工程难度；他也指出设计是产品三角中最短的一边，许多系统并无视觉需求，设计糟糕的产品也能成功。

**「启示」** 作者并非否定设计师的价值，而是认为其协作收益高度依赖组织约束：一次只配一名，并把设计系统当作虽增加一线工程痛苦、却仍优于替代方案的规模化手段。

**标签**: `#design systems`, `#frontend engineering`, `#team dynamics`, `#design collaboration`, `#product development`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [CoreWeave 2032 年债券收益率突破 16%，AI 数据中心债务担忧升温](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) ⭐️ 8.0/10

投资者对 AI 数据中心债务的担忧升温，CoreWeave 2032 年到期、票息 9.625%的债券收益率已升至 16%以上；其五年期信用违约互换（CDS，为债务违约提供保险的成本）周四一度超过 1289 个基点，周五回落约 8%至 1155 个基点。

rss · CNBC Finance · 11月6日 17:09

**「背景」** CoreWeave 是一家靠出租 AI 算力扩张的“新型云服务商”（neocloud），其 2032 年到期无担保债券此前已跌破面值 80 美分，被市场视为 AI 数据中心债务压力的风向标；债券收益率上升意味着价格下跌、投资者要求更高的违约补偿。

**「影响」** 对 AI 基础设施承建商和超大规模云厂商而言，违约保险成本上升意味着未来发债融资可能更贵；高盛称，若数据中心暂停令落地，可能影响美国约 45%的规划产能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1011460/neocloud-coreweaves-bonds-are-distressed-and-so-am-i">Neocloud CoreWeave ’s bonds are distressed, and so am I. | The Verge</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#credit markets`, `#CoreWeave`, `#data centers`, `#bond yields`

---

<a id="item-finance-news-2"></a>
### [美联储戴利：可能需进一步加息，10 月新增就业 16.5 万](https://www.cnbc.com/2026/11/06/fed-daly-interest-rates-inflation.html) ⭐️ 7.0/10

旧金山联储主席戴利 11 月 6 日表示，美联储可能还需要进一步加息，但具体时间和幅度尚未决定；同日美国劳工统计局公布，10 月非农就业新增 16.5 万人，失业率降至 4.1%。

rss · CNBC Finance · 11月6日 19:05

**「背景」** 美联储 9 月已将基准隔夜利率目标区间上调 25 个基点至 3.75%-4%，但上周会议决定按兵不动，称希望等待更多信息。

**「影响」** 戴利指出，10 月平均时薪同比上涨 3.1%，低于 9 月 CPI 同比涨幅 3.7%，实际工资下降，家庭仍承受高通胀压力。

**标签**: `#Federal Reserve`, `#interest rates`, `#inflation`, `#US jobs report`, `#monetary policy`

---

<a id="item-finance-news-3"></a>
### [纳斯达克指数进入回调区间，单日跌逾 5%](https://www.cnbc.com/2026/11/05/nasdaq-drops-into-correction-territory-heres-what-typically-happens-next.html) ⭐️ 7.0/10

纳斯达克综合指数周四下跌超过 5%，收于较上月创下的纪录高点低逾 11%的水平，进入回调区间。报道将此次抛售的催化剂指向民主党在周二中期选举中拿下参众两院，以及得克萨斯州州长当选人 Gina Hinojosa 主张立即暂停数据中心开发。

rss · CNBC Finance · 11月6日 20:42

**「背景」** 在华尔街，股指较近期高点下跌超过 10%即进入回调区间；据 CNBC 报道，本轮抛售的触发因素是民主党在本周二中期选举中拿下参众两院，以及得州当选州长 Gina Hinojosa 主张立即暂停数据中心建设，投资者因此担忧人工智能相关建设放缓。

**「影响」** 得克萨斯州州长当选人主张立即暂停数据中心开发，若其他州效仿，数据中心建设放缓将直接拖累芯片、服务器等人工智能基础设施相关企业及其投资者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.texastribune.org/2026/11/04/data-center-texas-pause-gina-hinojosa-governor-policies/">Under Hinojosa , Texas data center approvals could stay paused</a></li>
<li><a href="https://www.newsweek.com/texas-hits-brakes-on-data-centers-and-elon-musks-plans-12675796">Texas Hits Brakes On Data Centers — And Elon... - Newsweek</a></li>
<li><a href="https://www.cnbc.com/2026/11/04/ai-stocks-texas-governor-data-centers.html">SpaceX, Tesla stocks fall over 4% on Democrats big win</a></li>
<li><a href="https://techfyle.com/tech-stocks-plunge-midterm-elections-nasdaq-5-percent-nvidia-data-centre-fears-2026/">Tech Stocks Plunge as Midterms Fuel Data Centre ... | TechFyle | TF</a></li>

</ul>
</details>

**标签**: `#Nasdaq correction`, `#US equities`, `#semiconductors`, `#midterm elections`, `#market volatility`

---

<a id="item-finance-news-4"></a>
### [六部门发文推动具身智能等前沿技术进入养老领域](https://api3.cls.cn/share/article/2527197?sv=859&amp;amp;os=web) ⭐️ 7.0/10

民政部等六部门于 11 月 4 日印发《关于培育多元场景 促进适老用品产品消费的若干措施》，提出以国家重大科技项目为牵引，加快推进具身智能、大语言模型、脑机接口、外骨骼等前沿技术在养老领域的应用，并研发升级失能照护、康复护理、精神陪护智能设备。文件未给出资金规模、量化目标或执行时间表。

telegram · zaihuapd · 11月6日 07:31

**「背景」** 这份文件由民政部、国家发展和改革委员会、工业和信息化部等六部门于 11 月 4 日印发，11 月 6 日对外发布，属于多部门联合支持适老用品产品消费的措施。

**「影响」** 文件还鼓励智能养老服务机器人加快落地、推广“以租代售”等租赁模式，并培育银发 MALL、银龄市集等消费场景，这为养老服务机构以及服务机器人、康复辅具生产企业提供了新的应用方向和销售渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zaobao.com.sg/news/china/story20261106-9959072">中国要求加快推 进 具 身 智 能 、外骨骼等在 养 老 领域应 用 | 联合早报</a></li>

</ul>
</details>

**标签**: `#养老政策`, `#具身智能`, `#服务机器人`, `#银发经济`, `#消费刺激`

---

<a id="item-finance-news-5"></a>
### [Anthropic 据报下周启动 IPO 路演，拟 11 月 16 日当周挂牌](https://www.theinformation.com/briefings/anthropic-proceed-ipo-roadshow-next-week) ⭐️ 7.0/10

据 The Information 援引知情人士报道，Anthropic 计划下周启动 IPO 路演，并拟于 11 月 16 日当周、美国感恩节假期前挂牌上市。市场此前预期该公司将以 1.5 万亿美元估值募资超过 800 亿美元，但报道称，受近期 AI 股票与支出担忧引发的科技股波动影响，其估值目标可能下调。

telegram · zaihuapd · 11月7日 01:27

**「背景」** Anthropic 已于 10 月公开上市申请文件，其中显示 2026 年上半年营收为 162.9 亿美元；此前投资者讨论的估值约为 1.5 万亿美元，但公司尚未公布官方发行价区间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fxstreet.com/news/anthropic-ipo-filing-reveals-rapid-growth-as-investors-weigh-an-80-billion-loss-202610270748">Anthropic IPO filing reveals rapid growth as investors weigh an $ 80 ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI`, `#valuation`, `#markets`

---