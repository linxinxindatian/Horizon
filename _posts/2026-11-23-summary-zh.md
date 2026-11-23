---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 28 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [O&\#x27;Reilly 长文：硅谷的激励机制如何偏离人类福祉](#item-tech-news-1) ⭐️ 7.0/10
2. [OpenAI 探讨困惑度与模型智能的关联](#item-tech-news-2) ⭐️ 7.0/10
3. [英媒：太子集团涉案人员被指走私英伟达芯片至中国](#item-tech-news-3) ⭐️ 7.0/10
4. [Windows Server 2028 默认移除 WoW64，可手动装回](#item-tech-news-4) ⭐️ 7.0/10

**科技博客**
1. [不确定时，不妨主动试错](#item-tech-blog-1) ⭐️ 5.0/10

**财经新闻**
1. [美股科技股大跌，亚洲多地出台稳市措施](#item-finance-news-1) ⭐️ 9.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [O&\#x27;Reilly 长文：硅谷的激励机制如何偏离人类福祉](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

O&\#x27;Reilly Radar 刊载的长文《What Happened to Silicon Valley?》梳理硅谷的文化与经济演变，认为其激励机制和机制设计把股东价值放在了更广泛的人类福祉之上。文章把机制设计称为“反向博弈论”：不只追问当前游戏的规则，而是先问“我们本该玩什么游戏”，并主张以人类福祉作为集体优化的目标。需要说明的是，目前没有文章全文可供核对，上述要点来自内容摘要和读者讨论，并非独立验证。

hackernews · greenyouse · 11月22日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50602947)

**「机制设计与价值转向」** 这篇文章的核心参照系是“机制设计”，作者将其称为反向博弈论：与其只接受现有规则，不如追问“我们本该玩什么游戏”，并把人类福祉作为目标。文章据此回顾硅谷从以客户为中心的创新，转向由股东价值、垄断野心和炒作驱动的价值榨取，并将这一变化与当前的 AI 热潮联系起来。

**「社区讨论」** 评论者大多认同文章的批评，但对原因的看法不同：Animats 认为人们把市场当成自然现象，没有追究“机制设计者”的责任；CoolestBeans 则把直接原因归于零利率时代催生的过度扩张，并质疑当前的 AI 投入能否受到市场约束。michalsustr 表示，文章最重要的“机制设计即反向博弈论”观点被放在结尾；jansport123 则批评当下的“VC 网红”文化让硅谷的专业操守更加稀薄。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oreilly.com/radar/what-happened-to-silicon-valley/">What Happened to Silicon Valley? – O’Reilly</a></li>
<li><a href="https://oreillyradar.substack.com/p/what-happened-to-silicon-valley">What Happened to Silicon Valley? - oreillyradar.substack.com</a></li>

</ul>
</details>

**标签**: `#Silicon Valley`, `#tech industry`, `#mechanism design`, `#capitalism`, `#AI investment`

---

<a id="item-tech-news-2"></a>
### [OpenAI 探讨困惑度与模型智能的关联](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

OpenAI 发布一篇题为《Perplexity and Intelligence》的分析文章，讨论困惑度（perplexity）与模型智能之间的关系，涉及交叉熵、评测基准和推理模型趋势。现有材料没有提供原文正文，因此文章的具体结论、所用数据和适用范围无法核实；可以确认的是，它属于分析或评测论述，而非产品发布或独立复现结果。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「背景」** Perplexity（困惑度）通常由交叉熵推导而来，衡量模型对下一个 token 的预测有多不确定，数值越低表示预测和压缩越好；这是理解把预训练损失与模型能力挂钩的分析所需的前提。作为参照，2025 年 2 月发布的 GPT-4.5 侧重扩大无监督学习规模，有基准分析称它在对话上更强、在复杂问题求解上较弱，这为讨论预训练指标与推理能力的关系提供了近期样本。

**「影响」** 微软 AI CEO Mustafa Suleyman 表示，MAI-2 Base 在 OpenAI 共享的 held-out 评估集上录得 0.819 的 log-perplexity，与 GPT-5.6 Sol 基座模型处于同一量级，并称将致力于在共同评估集上披露预训练进展。对模型开发者而言，这意味着多了一个可横向对照的预训练指标，但该 0.819 是厂商自报数据，只有采用同一评估集和口径时才可直接比较。

**「社区讨论」** HN 评论中，有读者补充困惑度衡量模型预测下一 token 的意外程度：完全准确时接近 1，随机预测时约等于词表大小；也有人认为交叉熵与能力的对应趋势仍然清晰，简单基准比日益复杂的评测更有价值。另有评论称微软的 MAI 模型被加入同一评测图表，但该说法来自评论中的社交媒体链接，未获原文或独立来源确认。

<details><summary>参考链接</summary>
<ul>
<li>OpenAI releases GPT-4.5 - LessWrong</li>
<li>GPT 4.5 Released: Here Are the Benchmarks - Helicone.ai</li>
<li><a href="https://x.com/mustafasuleyman/status/2124663594449318173">Mustafa Suleyman on X: &quot;We fully support OpenAI&#x27;s ...</a></li>
<li><a href="https://www.techtwitter.com/tweet/86327c55-7454-4d6c-a5cb-1fe8f0cee796">Microsoft&#x27;s MAI-2 Base scores near GPT-5.6 Sol on perplexity</a></li>

</ul>
</details>

**标签**: `#perplexity`, `#language-models`, `#evaluation-benchmarks`, `#cross-entropy`, `#OpenAI`

---

<a id="item-tech-news-3"></a>
### [英媒：太子集团涉案人员被指走私英伟达芯片至中国](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 7.0/10

英国《金融时报》援引知情人士报道，被美国财政部指为柬埔寨太子集团“二号人物”的胡小伟涉嫌参与将英伟达芯片运入中国；报道还称该集团拥有由空壳公司和地下融资渠道组成的网络，并利用私人飞机走私货物。报道援引贸易数据称，2024 年 12 月至 2025 年 12 月，Megaspeed 马来西亚子公司进口货物的申报价值约 46 亿美元，部分芯片据称流入中国黑市。太子集团否认胡小伟曾为其工作，并表示有关非法网络和私人飞机走私的指控缺乏事实依据；上述指控尚未得到证实。

telegram · zaihuapd · 11月22日 04:34

**「背景」** 美国对英伟达高端 AI 芯片实施对华出口管制，第三国采购和转运因此成为合规审查的重点。此前《日经亚洲》11 月 13 日报道称，新加坡的 Megaspeed 因英伟达芯片流向中国的问题受到关注，新加坡和马来西亚的相关公司也因此被置于聚光灯下。

**「合规审查压力」** 对经由马来西亚等东南亚中转采购英伟达 AI 硬件的机构来说，现实影响是最终用户和最终用途审查更受关注：涉及约 46 亿美元申报进口的 Megaspeed 马来西亚子公司已否认违规出口，并称遵守美国出口管制，但交易方仍需保留可核验的最终用户证明和转运记录。由于报道中的指控尚未被证实，合规风险是否落地取决于后续调查。

<details><summary>参考链接</summary>
<ul>
<li>Nvidia case puts Singapore, Malaysia companies in spotlight - Nikkei Asia</li>
<li><a href="https://www.independent.co.uk/news/world/americas/nvidia-donald-trump-ceo-beijing-malaysia-b3084263.html">What we know after Jensen Huang resigns as Nvidia CEO</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#export controls`, `#chip smuggling`, `#supply chain`

---

<a id="item-tech-news-4"></a>
### [Windows Server 2028 默认移除 WoW64，可手动装回](https://www.windowslatest.com/2026/11/23/32-bit-apps-days-are-numbered-as-microsoft-strips-support-bit-by-bit-starting-with-windows-server-2028-but-windows-11-is-safe-for-now/) ⭐️ 7.0/10

微软在 Ignite 2026 上表示，计划于 2027 年秋季随 Windows 11 27H2 发布的 Windows Server 2028 将默认不包含 WoW64 兼容子系统，因此系统开箱即无法运行 32 位应用。需要时，管理员可通过按需功能（FoD）将 WoW64 装回，在 Server Core 上通常使用 PowerShell 或 DISM 添加。微软称此举旨在减少攻击面、阻止 32 位恶意软件；Windows 11 目前仍保留 WoW64，且未公布移除计划。上述内容来自 Windows Latest 的报道，属于已宣布的发布计划，并非已经交付的服务器版本。

telegram · zaihuapd · 11月23日 03:03

**「背景：WoW64 兼容层」** WoW64 是 64 位 Windows 用来运行 32 位应用的兼容层，过去一直随系统默认提供。此次调整若按计划落地，将是 64 位 Windows 首次在默认配置下无法运行 32 位程序。

**「对企业的直接影响」** 对仍在服务器上运行 32 位业务软件或 32 位管理代理的企业来说，Windows Server 2028 的默认镜像开箱即无法运行这些程序；管理员必须在部署镜像或首次启动时用 PowerShell 或 DISM 将 WoW64 作为按需功能装回，Server Core 环境尤其需要提前把该 FoD 包放入离线源，否则无图形界面的自动化部署会卡在这一步。微软称此举可缩小攻击面、阻止 32 位恶意软件，但同样会挡住未迁移的老旧 32 位服务端工具，因此在计划于 2027 年秋季发布的版本到来前，应先盘点依赖 32 位组件的服务端软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thecommunity.ru/microsoft/windows/server/12123-windows-server-2028-po-umolchaniju-ne-budet-podderzhivat-32-bitnye-prilozhenija.html">Windows Server 2028 по умолчанию не будет поддерживать...</a></li>

</ul>
</details>

**标签**: `#Windows Server`, `#WoW64`, `#32-bit compatibility`, `#Microsoft`, `#enterprise IT`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [不确定时，不妨主动试错](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 5.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 面对信息不足、不知从何下手的工程或组织问题，作者认为与其谨慎等待更完整的理解，不如主动进行“乱撞”式试错。

**「方案」** 作者把有效的“乱撞”归纳为三点：大量尝试不同做法、密切观察来自现实和周围专家的反馈、对没有得到正向反馈的方案立刻放弃。多试既能接触更多真实情况，也因为多数方案本就不可行，同时持有多个方案还能避免过度投入。作者称，这种方法适用于产品尚未找到市场契合点时、复杂系统难以找到改进起点时，以及跨团队沟通不畅等组织问题中；他在 GitHub Models 上做过多个未奏效的功能，但“用 GitHub Actions token 运行 AI 推理”意外受欢迎，后来成为“Continuous AI”的种子。工程上他建议先做若干试探性改动，看效果再决定是否深挖；组织上则可以主动自动化、接手任务或提出长期方案。作者也警告，试错可能损害声誉，尤其在组织场景中必须对反馈敏感，及时停掉失败方案才能建立信任，否则不满会转向自己；从内部感受看会像反复失败，但不应因此放弃。

**「启示」** 作者的核心论点是：在高度不确定时，广泛试错并快速依据反馈淘汰方案，比等待完整理解更有效；真正的风险不是尝试失败，而是对失败信号视而不见。

**标签**: `#uncertainty`, `#experimentation`, `#feedback loops`, `#engineering management`, `#software engineering culture`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美股科技股大跌，亚洲多地出台稳市措施](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 9.0/10

美国 AI 科技股周五遭遇大规模抛售，纳斯达克指数单日下跌 5.28%，费城半导体指数重挫近 11%。随后，中国内地下调融资保证金最低比例至 80%，韩国放宽上市公司回购限制并加强卖空监控，中国台湾地区则禁止平盘以下卖空并将融券保证金比例由 130%提高至 150%。

telegram · zaihuapd · 11月22日 13:24

**「背景」** 费城半导体指数追踪 30 家最大芯片股；据 Axios 当时报道，纳斯达克指数此前已较 10 月 6 日的高点回落至少 10%，进入通常所说的“回调”区间。亚洲芯片与出口导向型市场与美股科技股高度联动，因此美股的这轮抛售会迅速传导至亚洲。

**「影响」** 这些措施将直接影响相关市场的融资交易者和卖空者：中国内地降低融资保证金比例可提高杠杆买入能力，而台湾地区禁止平盘以下卖空并提高融券保证金，则会限制卖空操作并抬高其成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/7c6ceb4f-d7b1-49ec-9047-0e2e4cd2615c?syn-25a6b1a6=1">US midterms 2026 reaction as it happened: Global stocks tumble as...</a></li>
<li><a href="https://www.axios.com/2026/11/05/nasdaq-plummets-correction">Tech stocks tumble as election rattles AI trade</a></li>

</ul>
</details>

**标签**: `#US tech selloff`, `#Asian markets`, `#market stabilization`, `#margin trading`, `#short selling`

---