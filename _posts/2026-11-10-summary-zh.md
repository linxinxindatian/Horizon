---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 51 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [watched.earth：查询过去 7 天卫星过境与实拍影像](#item-tech-news-1) ⭐️ 8.0/10
2. [谷歌发布 TPU 8tx 与 8i Max 两款新芯片](#item-tech-news-2) ⭐️ 8.0/10
3. [报告称消费级 Gemini 将个人 Drive 和邮件数据送人工审阅](#item-tech-news-3) ⭐️ 7.0/10
4. [E-means 宣称用十分之一 epoch 媲美或超越 k-means](#item-tech-news-4) ⭐️ 7.0/10
5. [LingBot-Touch：潜空间预测优于重建的触觉预训练](#item-tech-news-5) ⭐️ 7.0/10
6. [Twindex：ODE/PDE/PINN 参数不可辨识性证书](#item-tech-news-6) ⭐️ 7.0/10
7. [OPPO、vivo、小米、荣耀上线 ADV 侧载开发者验证](#item-tech-news-7) ⭐️ 7.0/10
8. [欧盟《数字公平法案》草案拟限制成瘾性设计与虚拟货币披露](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [英伟达董事会调查黄仁勋，预测市场认为其近期离职概率低](#item-finance-news-1) ⭐️ 8.0/10
2. [前三季度中国新能源乘用车出口增 138.8%，国内零售降 12.8%](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [watched.earth：查询过去 7 天卫星过境与实拍影像](https://www.watched.earth/) ⭐️ 8.0/10

开发者发布了 Show HN 项目 watched.earth：输入任意地点后，它用浏览器端 SGP4 在约 0.5 秒内检索 CelesTrak 目录，找出过去 7 天飞越该地的卫星，并关联这些过境对应的 Sentinel-2、Landsat 和 NASA 真实影像。项目称其过境搜索在极点、反经线和极窄扫幅等边界情况下与暴力枚举对比为 0 漏检，并在 GPU 上逐帧求解开普勒方程绘制约 1.7 万个在轨物体；代码已在 GitHub 开源。它只在存在真实影像时标记“watched”，且不存储用户位置；作者还指出 Sentinel-2 时间戳常比卫星实际过境时间差 5–10 分钟，并已处理这一问题。

hackernews · a585gupt · 11月9日 17:51 · [社区讨论](https://news.ycombinator.com/item?id=50428907)

**「背景」** 此前已有面向公众的卫星过境规划工具，例如 Satellite Overpass Planner 可查询 Sentinel-1、Sentinel-2 和 Landsat 8/9 何时经过任意地点，其采集计划直接来自 ESA 和 USGS 并每日更新。这类工具主要回答“卫星何时经过、何时采集”，而本次 Show HN 项目进一步把过去 7 天的过境与对应的真实影像关联起来，并采用浏览器端 SGP4 自行计算整个 CelesTrak 目录中的轨道对象。

**「影响」** 对想确认某条街道或某片区域近期是否被拍到的用户，这个工具把过境记录直接连到可查看的真实影像，省去在 Copernicus 等平台逐景查找的步骤；但“watched”只代表有可用影像，未标记并不等于卫星没有飞过。

**「社区讨论」** 有地理空间从业者称该站能直接看到卫星拍下的具体影像，认为在同类卫星概览站点中表现突出；也有用户表示用它规划背包旅行，比 Copernicus 更易用。另有评论集中抱怨位置输入框的光标与字符间距异常，几乎无法正常输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://satflyover.com/">Satellite Overpass Planner</a></li>

</ul>
</details>

**标签**: `#satellite-imagery`, `#orbital-mechanics`, `#geospatial`, `#gpu-computing`, `#open-source-tools`

---

<a id="item-tech-news-2"></a>
### [谷歌发布 TPU 8tx 与 8i Max 两款新芯片](https://www.bloomberg.com/news/articles/2026-11-09/google-escalates-nvidia-rivalry-with-new-versions-of-its-tpu-systems) ⭐️ 8.0/10

谷歌宣布推出两款新张量处理单元：面向政府及严格监管行业、处理安全机密数据并将与 AMD 芯片协同工作的 TPU 8tx，以及面向超长上下文 AI、把两颗 TPU 集成在同一封装内以提升算力和内存的 TPU 8i Max。谷歌称苹果、Meta、甲骨文和 Anthropic 等已成为客户，并正打破过去每两年推出一款处理器的节奏，今年连续扩充 TPU 产品线。来源摘要未给出两款芯片的上市时间、价格、功耗或每 token 成本，也没有独立性能数据。

telegram · zaihuapd · 11月9日 13:36

**「背景」** TPU 是谷歌自研的张量处理单元，用于加速 AI 计算任务。谷歌过去大约每两年更新一次 TPU，这次却在同一产品周期内接连扩充产品线，显示其正以更细分的芯片定位覆盖不同 AI 工作负载。

**「影响」** 对受监管机构而言，TPU 8tx 的选型不仅要看机密数据处理能力，还要评估与 AMD 芯片混合部署时的软件兼容性；对超长上下文应用，8i Max 的双芯片封装提供了更大内存和算力，但在缺少价格与能效数据前，用户无法判断其相对英伟达方案的实际成本优势。

**「社区讨论」** 有评论者称 Colab 目前可用的最强 TPU 仍为 v6e-1，认为其规模不足以支撑严肃工作；也有人追问谷歌为何不出售这些芯片，并指出缺少每 token 功耗或成本数据，难以与英伟达同价位产品比较。另有评论者推荐谷歌 TPUSync 材料，称其与 Strata 等面向 Qwen 系列模型的开源项目做法相近。

**标签**: `#Google TPU`, `#AI chips`, `#Nvidia competition`, `#AI hardware`, `#semiconductors`

---

<a id="item-tech-news-3"></a>
### [报告称消费级 Gemini 将个人 Drive 和邮件数据送人工审阅](https://github.com/thisisme6598/gemini_files/) ⭐️ 7.0/10

一份托管在 GitHub 的报告与 Hacker News 讨论称，消费级 Google Gemini 在用户连接 Gmail、Drive 等应用后，可能把个人邮件和云盘数据发送给人工标注人员；该说法尚未得到独立验证。评论者强调，这针对的是消费级 Gemini 的“已连接应用”，而 Workspace Gemini 的文档仍声称不受人工审阅。现有材料未提供可核实的审阅规模、触发条件或 Google 的正式回应。

hackernews · gf74918 · 11月9日 18:24 · [社区讨论](https://news.ycombinator.com/item?id=50429426)

**「背景」** Gemini 的“连接应用”（Personal Intelligence）是一项可选功能：用户逐项授权后，Gemini 能跨 Gmail、Drive、Calendar 和 Photos 读取内容来回答问题；该功能在欧洲经济区（EEA）不提供。这一授权范围与数据访问方式，是理解本次隐私争议的前提。

**「影响」** 对使用个人 Google 账号并授权 Gemini 连接 Gmail 或 Drive 的用户，潜在影响是个人数据可能进入人工审阅流程，而 Workspace 的企业级承诺不能直接套用到消费级账户；用户应检查 Gemini 的已连接应用和账号数据设置，必要时断开不必要的访问。

**「社区讨论」** 评论者 bri3d 区分消费级与 Workspace 政策，称后者仍声明不受人工审阅；rustyhancock 则报告 Gemini 的回答似乎暗中贴合其近期邮件内容，但这是个人体验而非可验证证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificial-ideas.com/resources/gemini-privacy-cheatsheet/">Gemini and your data: what it touches, keeps, and... — Artificial Ideas</a></li>

</ul>
</details>

**标签**: `#AI privacy`, `#Google Gemini`, `#human annotation`, `#consumer AI`, `#data governance`

---

<a id="item-tech-news-4"></a>
### [E-means 宣称用十分之一 epoch 媲美或超越 k-means](https://e-means.github.io/) ⭐️ 7.0/10

E-means 项目页面提出一种 k-means 替代聚类方法，声称只需约十分之一的 epoch 就能取得相当或更好的聚类效果。它面向希望减少大规模数据遍历的从业者，但当前证据主要是项目方说明和 Hacker News 上的零星试用，尚不足以证明它普遍优于 k-means。社区报告呈现分化：有人把该方法改用于 IVF 索引并在 GPU 上得到 146 倍加速，也有人用于球面网格松弛时发现效果不如 Lloyd 算法。

hackernews · porridgeraisin · 11月9日 18:45 · [社区讨论](https://news.ycombinator.com/item?id=50429734)

**「背景」** e-means 是 Meta FAIR 提出的 k-means 变体，其对照基线是 Lloyd 算法（包括 k-means++ 初始化）。经典 Lloyd 算法反复执行“把样本分配到最近中心、再重算中心”两步直至收敛，因此聚类质量和运行耗时都直接受迭代轮数影响。

**「影响」** 对聚类工程而言，值得验证的具体收益是减少对大型数据集的遍历次数，以及在 GPU 或 IVF 类索引流程中的潜在加速；但球面网格松弛的反例说明它并非跨场景替代品，采用前应按自身数据分布和迭代预算与 Lloyd 算法对比。

**「社区讨论」** 开发者报告了两种相反结果：real\_faxenoff 称把方法适配到 IVF 索引后在 GPU 上获得 146 倍加速，jlhawn 则在球面等面积网格松弛中试过后认为不如 Lloyd 算法，只在大数据集减少遍历次数上有优势。senderista 还指出 k 仍是剩余超参数，并询问当前选择 k 的最佳做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/e-means/e-means.github.io/tree/main">GitHub - e-means/e-means.github.io: e-means: a modern ...</a></li>
<li><a href="https://openreview.net/pdf?id=pt14gnV3dl">E-MEANS OUTPERFORMING K MEANS IN ONE TENTH THE EPOCHS</a></li>

</ul>
</details>

**标签**: `#clustering algorithms`, `#k-means`, `#machine learning`, `#GPU acceleration`, `#algorithm design`

---

<a id="item-tech-news-5"></a>
### [LingBot-Touch：潜空间预测优于重建的触觉预训练](https://www.reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for/) ⭐️ 7.0/10

Reddit 帖介绍了 Robbyant 的 LingBot-Touch：一种 JEPA 式自监督触觉编码器，通过预测被遮挡接触的潜表征而非重建原始传感器信号来预训练，推理代码和检查点已公开。帖子称，在与同规模 MAE、VAE 重建基线使用相同数据的对比中，1K 小时数据下触觉到视频的 top-5 召回率为 32.1%，MAE 为 5.6%，VAE 为 4.4%；到 4K 小时，JEPA 达到 49.3%，MAE 低于 9%，VAE 反而降至 3.1%。设计上，掩码比例在 300 步内从 40% 升至 80%，三类传感器通过规范化指尖坐标和 5D RoPE（时间、手指、3D 位置）送入同一个 Transformer。帖子还报告，在 26 个真实机器人任务、4 种策略共 104 个组合中，冻结编码器特征在其中 89 个得分最高；在预训练未见过的磁性手上，LingBot-VLA 从 57.21 提升到 75.04。

reddit · r/MachineLearning · /u/Zealousideal-War7154 · 11月9日 18:52

**「背景」** JEPA（联合嵌入预测架构）不重建原始输入，而是在潜空间中预测被遮挡部分的目标表征；本文用来对照的 MAE 和 VAE 属于常见的重建式自监督基线，因此这次比较的核心前提是：对稀疏的触觉信号而言，用潜空间预测是否比重建更合适。Robbyant 将 LingBot-Touch 作为触觉基础模型开源（Apache 2.0），提供冻结的目标编码器与推理工具，用于统一磁性、压阻和视触觉等异构传感器信号的表征，并称其在近 5,000 小时的压阻触觉数据上完成了预训练。

**「影响」** 对开发灵巧操作策略的团队来说，最直接的影响是可以下载公开的推理代码和检查点，把 LingBot-Touch 作为冻结触觉编码器接入下游策略，而不必先训练重建式编码器；不过这些数字来自帖子所述作者自测的 26 个任务，跨传感器和跨机器人本体的效果仍需自行验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technology.robbyant.com/lingbot-touch">LingBot-Touch Tactile Foundation Model - Robbyant</a></li>
<li><a href="https://agihunt.info/en/p/1a1c20d6d7c43e4b3f2845b66f2">Ant Group&#x27;s Robbyant open-sources LingBot Touch… · AGI Hunt</a></li>
<li><a href="https://github.com/Robbyant/lingbot-touch">GitHub - Robbyant/lingbot-touch: Learning Heterogeneous ...</a></li>

</ul>
</details>

**标签**: `#tactile sensing`, `#self-supervised learning`, `#JEPA`, `#dexterous manipulation`, `#robotics`

---

<a id="item-tech-news-6"></a>
### [Twindex：ODE/PDE/PINN 参数不可辨识性证书](https://www.reddit.com/r/MachineLearning/comments/1xryhhg/twindex_exact_replayable_proofs_that_your_data/) ⭐️ 7.0/10

项目作者在 Reddit 发布 Twindex，面向 ODE、PDE 与 PINN 建模中的参数不可辨识性问题：它生成小型 JSON 证书，并由仅使用 Python 标准库、采用有理数运算而非浮点数的精确检查器重放，返回 VALID、INVALID 或 INCONCLUSIVE。作者称，在声明的有界噪声假设下，一个 VALID 的“孪生”参数对意味着任何估计器都无法从这些数据中把该参数恢复得优于两者差距的一半。示例使用 1978 年寄宿学校流感数据：在前 5 天计数下，R0=2.5 与 R0=20 的 SIR 模型都能拟合，Twindex 找出了可区分二者的次日计数，而真实计数把两者都排除。项目覆盖含多项式、除法、exp、sin、cos 的 ODE，一维/二维椭圆与热方程 PDE，以及作为数值审计（明确不是证明）的任意 Python 模拟器；作者列出的限制包括有界噪声而非统计噪声、证明依赖所声明的模型和噪声界、超过少数几个参数时扩展困难，且尚无独立专家审计。

reddit · r/MachineLearning · /u/Longjumping\_Glass852 · 11月9日 17:50

**「背景」** 参数可辨识性关心的是：在给定模型结构和观测数据时，参数能否被唯一确定。相关综述区分结构可辨识性与实际可辨识性：前者通常只作“是否唯一”的二元判断，后者则考察实验设计和有限数据能把参数约束到什么程度。对非线性模型，可辨识性还可能随参数取值而变化，因此需要全局或基于模拟的分析方法。

**「对参数拟合实践的影响」** 对做 ODE/PDE/PINN 参数拟合的研究者而言，Twindex 提供了一种可在论文或报告中附带的可复现证书：当证书判定为 VALID 时，在设定的有界噪声假设下，任何估计器都无法把该参数确定到优于两个候选参数差值一半的精度，因此不应据此宣称该参数可从数据中辨识。实际使用时可以用 pip 安装，并在浏览器中本地重放证书（每个约 0.2 秒）；但作者本人指出，该方法受有界噪声假设限制，参数数量稍多就难以扩展，且尚无独立第三方审计，所以它更适合作为小规模模型的辅助核验，而不是通用结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S245231002500023X">Think before you fit: Parameter identifiability, sensitivity ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0378475422001227">Practical identifiability of parametrised models: A review of ...</a></li>
<li><a href="https://github.com/Arnav-M10/Twindex">GitHub - Arnav-M10/Twindex: Exact, replayable proofs that ...</a></li>

</ul>
</details>

**标签**: `#parameter identifiability`, `#scientific machine learning`, `#PINNs`, `#reproducible certificates`, `#ODE/PDE inference`

---

<a id="item-tech-news-7"></a>
### [OPPO、vivo、小米、荣耀上线 ADV 侧载开发者验证](https://mp.weixin.qq.com/s/ZiKBASSLzvsZ6WR2AUmFeg) ⭐️ 7.0/10

OPPO、vivo、小米、荣耀已在中国大陆上线 Android 侧载应用开发者身份验证（ADV）机制，并支持四家厂商之间的验证结果互认。已在四家开放平台注册并上架的 App 会自动提交验证，开发者无需单独申请。未完成验证的应用在侧载安装时会显示「未验证」提示，用户需手动确认后才能继续安装。

telegram · zaihuapd · 11月9日 11:44

**「背景」** 背景：侧载是指绕过应用商店直接安装 APK；ADV 试图把安装包与可验证的开发者身份绑定，让系统在安装时判断来源是否可信。外部报道显示，谷歌此前已推进 Android 开发者身份验证，并可能限制“未验证”应用的侧载，且曾将小米、OPPO、vivo、荣耀、三星等厂商列入相关协同范围（tool-1-1、tool-1-3）。此次四家中国厂商的互认机制可放在这一“开发者身份验证”趋势下理解，但现有来源未说明其与谷歌方案在技术或政策上的具体衔接。

**「影响」** 对未完成验证的应用，侧载安装会增加一步手动确认，主要影响通过官网等非应用商店渠道分发的开发者和用户；来源未说明独立开发者如何单独提交 ADV 验证，相关接入方式仍不明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7543362371340566571">谷歌 开 启 Android ...</a></li>
<li><a href="https://post.smzdm.com/p/anvomm2v/">安卓彻底告别自由 侧 载 ？ 谷歌联合六大厂商，装陌生APK等24...</a></li>

</ul>
</details>

**标签**: `#Android sideloading`, `#developer verification`, `#app security`, `#mobile ecosystem`, `#China tech`

---

<a id="item-tech-news-8"></a>
### [欧盟《数字公平法案》草案拟限制成瘾性设计与虚拟货币披露](https://www.mlex.com/mlex/articles/2546584/digital-businesses-face-addictive-design-controls-under-draft-eu-consumer-law) ⭐️ 7.0/10

一份泄露的欧盟《数字公平法案》草案显示，数字企业可能被要求允许用户关闭自动播放和连续使用奖励等诱导过度使用的功能，并为在线订阅提供取消按钮、续费提醒和人工客服，且在免费试用转为付费订阅前取得明确同意。草案还拟禁止面向未成年人的游戏付费抽奖、“付费获胜”和画像广告，并要求游戏虚拟货币标明真实币值。欧盟委员会定于 11 月 11 日提交该法案，违规企业最高或被罚全球营业额的 6%；该草案及消费者保护合作框架改革均需欧洲议会和欧盟各国政府同意才能生效。

telegram · zaihuapd · 11月9日 16:42

**「背景」** 《数字公平法案》是欧盟委员会此前已推动的数字消费者保护计划，重点针对暗黑模式、成瘾性设计和不公平个性化，并特别关注未成年人。此次泄露草案的意义在于把这些既有政策方向转化为具体禁令、订阅规则和游戏虚拟货币披露要求。

**「影响」** 若按草案生效，面向欧盟用户的游戏和订阅类数字服务需要调整产品设计、取消流程和虚拟货币标价，并限制对未成年人的付费抽奖与画像广告；不合规可能面临最高全球营业额 6%的罚款。由于目前仍是泄露草案，企业尚不能把上述要求视为最终合规义务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digitalfairnessact.com/">Digital Fairness Act (DFA) | EU Tracker</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#digital fairness`, `#dark patterns`, `#game virtual currency`, `#consumer protection`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达董事会调查黄仁勋，预测市场认为其近期离职概率低](https://www.cnbc.com/2026/11/09/jensen-huang-nvidia-exit-prediction-markets.html) ⭐️ 8.0/10

英伟达董事会正在调查 CEO 黄仁勋，缘由是有关他遭“外国情报活动”针对的报道；消息传出后，英伟达股价周一下跌超过 5%。Kalshi 上的交易者认为，黄仁勋在 2027 年前离职的概率仅为 17%。

rss · CNBC Finance · 11月9日 18:46

**「背景」** 黄仁勋是英伟达的联合创始人兼首席执行官，公司目前没有明确的继任安排，因此此次调查被外界视为典型的“关键人物风险”，即公司命运过度依赖单一领导者（tool-1-1）。据 BBC 报道，他仅持有公司约 3.5%的股份，且英伟达采用单一类别股票的投票结构，这意味着董事会在理论上具备将其免职的能力（tool-1-3）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/09/jensen-huang-affair-nvidia-succession.html">Jensen Huang &#x27;s affair highlights Nvidia &#x27;s key man risk with no heir</a></li>
<li><a href="https://www.bbc.com/news/articles/c6zxjx01vyleo">Nvidia shares tumble over investigation into Huang &#x27;s affair with alleged...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#prediction markets`, `#national security`

---

<a id="item-finance-news-2"></a>
### [前三季度中国新能源乘用车出口增 138.8%，国内零售降 12.8%](https://finance.sina.com.cn/tech/roll/2026-10-26/doc-iniwpfnc2438186.shtml) ⭐️ 7.0/10

2026 年前三季度，中国新能源乘用车出口 388.7 万辆，同比增长 138.8%；同期国内零售量为 775.8 万辆，同比下降 12.8%。

telegram · zaihuapd · 11月10日 02:56

**「政策背景」** 作为背景，中国政府将新能源车购置税优惠从全额免征调整为减半征收，同时把汽车以旧换新补贴政策延续至 2026 年底。

**「影响」** 对车企而言，出口增长已成为支撑整体销量增长的重要来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/economy/articles/china-pv-retail-sales-fall-110150847.html">China ’s PV retail sales fall by 23% in May</a></li>

</ul>
</details>

**标签**: `#China NEV exports`, `#passenger vehicle retail`, `#auto demand`, `#purchase incentives`, `#September sales`

---