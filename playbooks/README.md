# 业务职能剧本 (Playbooks)

三天直播中呈现的九大职能角色实战工坊，每个角色独立整理为一篇实战手册。每一场专场均由一位 xAI 员工在现场演示他们真实运转的 Bot 体系（基于虚拟演示公司）。每个剧本均采用严密的统一结构：

**团队架构**（谁负责什么、连接哪些系统） → **直播真实工作流** → **实战 Prompt（尽可能保留录音原貌）** → **定时例行任务与触发频次** → **量化数据指标** → **主讲人实战心得** → **一键抄作业（落地配置检查清单）**。

这是本仓库中最具即插即用价值的部分。在 PDF 完整指南中，这九套方案被浓缩成了每套三段话的摘要；而在这里，它们得到了完整的原貌还原。

---

## 九大职能工坊速查

| 剧本文件 | 主讲人 | 直播日 | 核心精髓 |
|---|---|---|---|
| [`engineering.md`](engineering.md) | Ling Shi，研发工程师 | 第 1 天 | 剧本管理 Bot 广播全团队规范；P0 故障策略只定义一次；深夜自动清理代码与带证据的门禁合并 |
| [`product-management.md`](product-management.md) | Kevin De Parco + Roshan，产品团队 | 第 1 天 | 数据 → PRD 规范 → UI 设计 → 工程主管拆解 → 云端 Agent 并发执行；Bot 反客为主纠正人类对漏斗数据的误读 |
| [`founders.md`](founders.md) | Shub，创始人成功部门 | 第 1 天 | 4 个核心 Bot 覆盖创始人 4 项日常关键工作；沉淀经验形成复利，不要随手丢弃；严厉审计 Routine 触发频率 |
| [`sales-engineering.md`](sales-engineering.md) | Amrita，现场售前工程师 | 第 2 天 | 代码库专家 Bot 与竞品分析 Bot 在群聊中激烈辩论；通过人机示教录制来教会 Bot 新技能 |
| [`sales.md`](sales.md) | Krista + Mark Wright，GTM 业务团队 | 第 2 天 | 结合 X 平台个人钩子进行获客；让 Bot 替你把 Webinars 研讨会看完；从通话转录中全自动更新 CRM |
| [`sdr.md`](sdr.md) | Simon，业务拓展代表 (SDR) | 第 2 天 | 幕僚长先行，所有下属 Bot 均通过它来创建；每个渠道平台设立专职 Bot；底层挂载庞大的低上下文工兵蜂群 |
| [`customer-support.md`](customer-support.md) | David，用户运营负责人 | 第 2 天 | 爬行 → 慢走 → 奔跑三步演进；公共 / 内部 / 流程三级知识库拆分；链路追踪与评测表格；单工单成本从 $2 骤降至 $0.20 |
| [`post-sales.md`](post-sales.md) | Blake，AI 交付与客户成功 | 第 3 天 | 设立单一对外接头 Bot，其余内部 Bot 绝不弹窗打扰人类；通过语音倾倒完成冷启动；每周自我改进严格限制为 1 条建议 |
| [`marketing.md`](marketing.md) | Josh Kim，市场营销 | 第 3 天 | 6 个专业 Bot 协同推进一次真实营销 Campaign 并上线生产；随后由产品经理 Bot 自主学习人类的人工干预点并全面接管 |

*注：第 3 天 Matthew 的营收与市场运营分享（主题为“构建工具而非堆积规则”）已收录在 [`../notes/day-3-notes.md`](../notes/day-3-notes.md)，因其为宏观分享而非具体的职能角色工坊，故未单独设为剧本。*

---

## 贯穿九场专场的十大共识原则

纵观这九大业务剧本，尽管各自业务语境与词汇不同，但背后呈现出高度一致的底层铁律：

1. **一个 Bot，一项职责（One Bot, One Job）。** 每一位主讲人的共同铁律。职责严格按照岗位职责说明书（Job Description）的范围圈定；只有当范围真正扩大时才做拆分，在此之前绝不随意拆分。
2. **只保留一个主对话入口。** Simon、Blake、Josh、Ling、Kevin 最终都采用了“幕僚长（Chief of Staff）/ 单一对接人”架构，由它在幕后调度众多垂直专家。Shub 是唯一的例外——他个人更喜欢直接和各领域专家对话，并明确表示这属于个人习惯。
3. **所有下属垂直专家统一“通过幕僚长来创建”**，确保幕僚长能够完整掌握每个专家的能力边界。（Simon 强调得最为清晰直接）。
4. **一句话说清楚，绝不重复啰嗦。** Ling 的剧本广播链路、Blake 的自我改进巡检、Shub 的“再深挖一层根因”、Roshan 的“一旦思路出错就沉淀为 Skill”。如果你发现自己需要对 Agent 重复下达同一个 Prompt，这往往意味着你缺少了一条永久规则或一个 Routine。
5. **文风语气先行（Voice First）。** Krista、Simon、Shub、Blake 在允许 Bot 正式外发任何内容之前，都会先用真实发出的历史邮件或文案对文风 Bot 进行强化训练。Simon 的训练配方最为精准：筛选目标区域内的、获得正面回复的、按时间越近权重越高的真实邮件进行训练，随后开启批评循环不断纠偏，直到没有任何一封邮件看起来像生硬的套用模板。
6. **先生成草稿，后允许直发。** David 的“爬行 → 慢走 → 奔跑”理念；Blake 的“只准生成草稿，坚决不准擅自发送”；Josh 的“从低风险最小场景切入”。对外部系统的直接写入权限必须是一步一步赢来的。
7. **Routine 例行任务：数量必须远比你想象的要少。** Krista 强调每天跑 1 到 2 次足够；Blake 提醒三个 15 分钟的 Routine 一天就会触发几百条消息；Shub 指出每 15 分钟触发相当于一天跑 100 次，必须尽量换用 Webhook；Kevin 强调在无事发生时 Routine 应当保持绝对静默。
8. **Bot 之间保持通信，但只在关键时刻打扰人类。** 下属各专业 Bot 之间的内部对话与数据传递绝对不应该在你的侧边栏里频繁刷屏。
9. **放手让 Bot 亲自去使用产品。** Serena 去航司官网订了一张西南航空的真实机票；ProdBot 亲自巡检网站；Reply Bot 亲自打开真实工单系统研读；Craig 亲自在 flyloair.com 上逐步点击操作。Bot 远程电脑上的真实运行环境就是最强大的验证闭环。
10. **反问 Bot，让它们参与设计 Bot。** “你觉得哪些 Bot 能帮你分担工作？”（Amrita），“帮我搭建一个适配我的协作系统”（Blake），“指出我们当前的系统瓶颈到底在哪里？”（Lauren 在研发专场）。

---

## 跨专场 Bot 角色花名册速查

当你在笔记中看到某个名字想快速查验其所属专场时，可参考下表：

| Bot 角色名 | 所属专场 | 角色定位 |
|---|---|---|
| Craig / Ling Xixi, Cray, Steve, Hogan1QR, Jenny | 研发专场 (engineering) | 幕僚长、前端 UI 专家、DevX 开发者体验、基础设施、剧本文档管理员 |
| Cora, Emily, Einstein/Igor/Nova/Larry/Eileen, Ashley, PMP/Pete, Pixel, Ray | 产品专场 (product-management) | 幕僚长、工程主管、研发团队蜂群、数据分析师、PRD 规划、UI 设计、招聘专员 |
| CloseBot, ProdBot, StockBot, ProtoBot, YapBot, misc | 创始人专场 (founders) | 客户洞察、产品状态看板、竞品雷达、反馈自动转 PR、口述文风、临时回收站 |
| Mimi, Sherlock, Serena Williams, Battle Card Blair, Demo Drake, AI Radar | 销售工程专场 (sales-engineering) | 幻灯片制作、代码库专家、竞品对抗测试员，以及由 Sherlock 衍生的三位专家 |
| Olive, PG, Echo, Customer Expert, Engineer | 销售专场 (sales) | 幕僚长、获客勘探专员、实时演示文稿、客户档案规划、技术答疑专家 |
| Simon-bot, Shakespeare, Web Search, Simon soldiers, Customer, PLG, Ample Market, Company research, Inbox manager | SDR 专场 (sdr) | 幕僚长、邮件文风专家、网络研究员、工兵蜂群、客户之声、产品驱动增长、数据增强、组织架构调研、收件箱分流 |
| Build, Reply, Alert, Tune | 客服支持专场 (customer-support) | 基础设施与知识库、工单自动回复、异常升级报警、自我调优专员 |
| Gus, Frankie, Wally, Trudy, Scout, Franny, Harbor/Northwind/Brightline | 售后与交付专场 (post-sales) | 幕僚长、跟进跟催、文风管家、单一事实来源、雷达巡检、表单助手、专属大客户代表 |
| market researcher, product marketer, website ops, performance marketer, marketing analyst, project manager | 市场营销专场 (marketing) | 战役策划团队：市场调研、产品营销、网站运维、效果投放、营销分析、项目统筹 |

---

## 补充说明

- **Flylo, XAir, Northwind, Harbor, Brightline, Craft** 均为直播中使用的虚拟演示公司与演示账号。文中所涉演示商品价格、业务指标与工单内容均为舞台演示效果而构造。
- 标有“录音原话（verbatim）”的 Prompt 来自现场实时字幕捕获，口述长句做了轻量标点整理；由叙述推导重构的 Prompt 标有“意译推导（paraphrased）”。
- 现场实时字幕中的产品名称偶有拼写偏差（如 GrokBot / Rockbot / Brockbot / Grock-Bot、“SpaceX AI”等），在本译文中均已统一校正规范。
- 直播中报出的所有量化数字均为主持人或嘉宾现场口述的实时变动数据。
