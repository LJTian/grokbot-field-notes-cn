# 角色名录库 (Roster)

汇总三天直播中提及的所有 Agent 角色——共计 **69 个专业角色**。**按“职能职责”而非“Bot 昵称”进行去重归并**。例如 Steve、Cora、Gus、Craig、Simon-bot 和 Olive 统归为一个角色（幕僚长），只是在不同专场拥有六个不同的名字。

每个角色卡片均包含标准化的八大板块：

| 板块 | 核心解答的问题 |
|---|---|
| **直播中曾化名为 (Seen on stream as)** | 在直播中扮演此角色的具体 Bot 名字，以及归属谁管理 |
| **负责职责 / 不负责范围 (Owns / Does not own)** | 清晰界定专属泳道。*“不负责范围”*往往最容易被忽视，但它恰恰是防止 Bot 盲目膨胀失控的防线 |
| **权威事实来源 (Source of truth)** | 从何处获取真实数据。如果该数据源中没有，Bot 必须坦白承认，严禁胡编乱造 |
| **需要人工审批的操作 (Needs approval for)** | 人工把关的关键门禁。初期宁严勿松，随后逐步放权 |
| **触发时机 / 交付产物 (Triggers / Outputs)** | 何时启动该任务，以及最终向谁移交什么格式的产物 |
| **定时例行周期 (Routines)** | 直播中实际推荐的执行周期与频次 |
| **角色描述 Prompt (Role description)** | 带有 `{PLACEHOLDERS}` 占位符、可直接复制到 System Prompt 的设定（这是 Bot 的“灵魂”） |
| **直播实战出处 (From the stream)** | 诞生该角色的具体事故、灵感或现场原话 |

## 如何使用角色卡

1. 将文中的【角色描述 Prompt】代码块复制到新 Bot 的 Description 字段中，替换其中的 `{占位符}`；
2. 根据你当下的真实需要，**大幅裁剪【负责职责】列表**。绝不要在第一天就盲目建好全套多 Bot 体系；
3. **严格遵守【需要人工审批的操作】**，直到该 Bot 在实践中彻底赢得了你的信任；
4. 当你对它进行纠错时，**将提炼出的通用规则补充进其角色描述中，而不是记录具体故事**。详见 [`../AGENTS.md`](../AGENTS.md)。

直播现场的大多数团队日常保持在 5–10 个核心 Bot。Blake 告诫：“你根本不需要 45 个 Bot”；Simon 也强调：“我曾经在某些时期建了太多 Bot，坦率讲，那样只会带来混乱。”

---

## 编排与协同 (Orchestration)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`Bot 工厂 (元 Bot / bot-factory.md)`](bot-factory.md) | 负责创建其他 Bot：起草角色设定、命名、体检现有团队、诊断工作流瓶颈。 |
| [`团队幕僚长 (chief-of-staff.md)`](chief-of-staff.md) | 人类唯一直接对话的主控 Bot。将所有任务分发给合适专家，掌握全局进度，唯一向人类弹窗的会话窗口。 |
| [`研发工程主管 (engineering-manager.md)`](engineering-manager.md) | 承接大块业务需求，拆解为独立任务包，分派给工程师 Bot 并闭环验证。调教为明确禁止亲自写代码。 |
| [`知识库管理员 (knowledge-base-manager.md)`](knowledge-base-manager.md) | 静默旁听对话，经人类批准后克制地将耐用事实写入知识库——像对待 Git Log 一样严谨，拒绝无脑倾倒。 |
| [`杂项垃圾桶 Bot (misc-bot.md)`](misc-bot.md) | 承接各类临时偶发杂项，防止污染各专职 Bot 的上下文。当某项知识证明有价值时再交接给专职 Bot。 |
| [`剧本文档管理员 (playbook-owner.md)`](playbook-owner.md) | 全权维护团队的动态规范活文档。其他 Bot 只读不写。新规则只录入一次并全局广播。 |
| [`项目经理 (project-manager.md)`](project-manager.md) | 深入学习人类在多 Bot 协作中的调度与干预痕迹，随后全面接管全自动化推进，成为该业务线的唯一对接人。 |
| [`自我改进巡检员 (self-improvement-scan.md)`](self-improvement-scan.md) | 每周审计人机协作中仍存在的手工冗余，产出 1 条自动化提案，并将真实发送 Diff 反哺给文风 Bot。 |
| [`权威事实来源 (source-of-truth.md)`](source-of-truth.md) | 基于权威基准文档作答并附带依据链接。其他 Bot 均以此为准；在答案不容有失时幕僚长必经其确认。 |
| [`工兵蜂群 (sub-agent-army.md)`](sub-agent-army.md) | 低上下文底层工兵集群，由父级 Bot 将大批量批处理任务切片分发，在群聊中向父级回传闭环——绝不打扰人类。 |

## 研发工程 (Engineering)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`CI 与故障自动修复 (ci-autofix.md)`](ci-autofix.md) | CI 飘红、部署失败第一响应人。排查、拉起云端 Agent 修复、按规则合入，仅在超时未解时呼叫人类。 |
| [`冗余注释清理员 (comment-cleanup.md)`](comment-cleanup.md) | 无情删除不必要的代码注释。防止 Agent 将注释当作遮掩权宜之计（Workaround）的拐杖。 |
| [`领域工程师 (domain-engineer.md)`](domain-engineer.md) | 按前端、DevX、基础设施等细分的专属工程 Bot，拥有独立记忆，将独立任务转化为带证据的 PR。 |
| [`用户反馈直转 PR (feedback-to-pr.md)`](feedback-to-pr.md) | 提取确认的用户反馈，以真实产品为上下文进行真机复现自检，数小时内完成修复并提交 PR。 |
| [`初创首位工程师 (founding-engineer.md)`](founding-engineer.md) | 守候在代码库第一线的全能工程师：紧盯每个 PR、合并可用代码、拉起云端 Agent 解决缺陷，支持随时语音交互。 |
| [`看板与任务状态管家 (kanban-updater.md)`](kanban-updater.md) | 确保任务看板真实可信：PR 合并时自动流转卡片，根据决策新建卡片，让其他 Bot 依照看板领活。 |
| [`深夜代码大扫除工程师 (nightly-audit-engineer.md)`](nightly-audit-engineer.md) | 每晚凌晨启动云端 Agent 扫描全库代码质量、模块化缺口、注释冗余与安全隐患，早晨留下整洁 PR。 |
| [`实机试玩与 QA 测试员 (playtester.md)`](playtester.md) | 在独立虚拟电脑中真正使用产品——四处点击、真机试玩、故意制造边缘输入破坏，在合并前或部署后汇报缺陷。 |
| [`PR 审查专员 (pr-reviewer.md)`](pr-reviewer.md) | 审查每一个 PR 的正确性、风险与测试完备性，强制检查是否附带了所需证据，随后执行合入或打回。 |
| [`原型构建专员 (prototyper.md)`](prototyper.md) | 极速构建一次性轻量原型——内联 HTML 或临时分支，专为回答某个交互设计问题，绝不追求一次上线。 |
| [`Slack @ 快捷响应助手 (slack-mention-responder.md)`](slack-mention-responder.md) | 监听 Slack 中的 @ 提及与私信并执行操作——零后台面板的轻量级内部工具，或充当人类前置分流层。 |
| [`分流校验员 (triage-validator.md)`](triage-validator.md) | 在自动化修复启动前，二次核验分流 Bot 对用户反馈的理解是否准确无误。在用户与代码之间设立双保险。 |
| [`工单与反馈分流员 (triage.md)`](triage.md) | 阅读进站反馈，尝试复现问题，录入已确认的工单（或判定丢弃）。严密防范反馈中的提示词注入攻击。 |

## 产品与设计 (Product & design)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`创意总监与媒体探索者 (creative-director.md)`](creative-director.md) | 尽可能以代码形式探索创意方向（音乐、动效、广告素材），并将候选方案汇总至看板供团队选拔。 |
| [`独立评审员 (critic.md)`](critic.md) | 对照标准基线对交付物进行严苛审阅并指出不足，只使用通俗直白的大白话。仅提供反馈，绝不亲自代笔。 |
| [`数据科学家与商业分析师 (data-scientist.md)`](data-scientist.md) | 用普通大白话提问即可编写并执行 SQL 调取数仓，输出图表，并在人类误读图表数据时当场予以纠正。 |
| [`UI/UX 设计师 (designer.md)`](designer.md) | 深度内化设计规范、参考素材与团队历次禁忌清单，极速交付高质量原型，同时提供多款变体方案以供选拔。 |
| [`优先级排定专员 (prioritizer.md)`](prioritizer.md) | 维护一份按商业影响力和投入成本综合打分的排期清单，随着新想法和新反馈涌入动态重排优先级。 |
| [`产品动态与变更追踪员 (product-changes-tracker.md)`](product-changes-tracker.md) | 研读 PR 和 Issue 并在自己的虚拟电脑上亲自巡视真实线上产品，汇报上线了什么、下线了什么、做出了哪些取舍。 |
| [`招聘专员 (recruiter.md)`](recruiter.md) | 挖掘潜在候选人、推进招聘管道、起草触达沟通；或者反过来为求职者寻找猎头与人脉切入点。 |
| [`产品规范与 PRD 撰写员 (spec-writer.md)`](spec-writer.md) | 将业务洞察转化为紧凑、明确界定 P0/P1/P2、专为快速转为代码而优化的规范，根据文档批注迭代。 |

## 销售与售前工程 (Sales & sales engineering)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`重点大客户专家 (account-specialist.md)`](account-specialist.md) | 掌握单一战略大客户全景（规划、干系人、续约、承诺），会后自动更新客户档案并提示高危风险。 |
| [`对战卡撰写员 (battle-card-writer.md)`](battle-card-writer.md) | 将竞品实测情报与代码库真实现状交叉比对，输出售前实战对战卡：竞品宣称了什么 vs 我们真实能力。 |
| [`会前准备与促成专员 (call-prep.md)`](call-prep.md) | 会前 15–20 分钟送达：参会人、上次遗留要点、用量异动、最新功能、建议话题，以及其官网的 Bug 截图开场白。 |
| [`案例幻灯片制作员 (case-study-curator.md)`](case-study-curator.md) | 将客户博客或通话笔记按固定模版生成案例 Slide，自动抓取官方 Logo 插入母版，并动态隐藏无关页面。 |
| [`竞品情报对抗专家 (competitive-intel.md)`](competitive-intel.md) | 亲自在虚拟电脑中注册并深度使用竞品，研读其更新日志、官方推文和招聘信息，汇报差异与应对之策。 |
| [`CRM 进展更新助手 (crm-updater.md)`](crm-updater.md) | 倾听通话录音，提取讨论要点，按照你预设的标准格式草拟阶段进展更新，并在商机阶段变动时做出响应。 |
| [`演示脚本与话术专家 (demo-scripter.md)`](demo-scripter.md) | 打造无幻觉的演示脚本与演讲话术，将特定客户的痛点精准映射到运行中的产品页面流转上。 |
| [`线索数据增强与企业调研 (enrichment.md)`](enrichment.md) | 将姓名转化为可达邮箱，将企业转化为技术栈、招聘岗位与组织架构树，防止外呼退信并精准触达负责人。 |
| [`目标客群 ICP 研究员 (icp-researcher.md)`](icp-researcher.md) | 综合赢单记录、客户之声与用量数据提炼究竟谁在买单，沉淀为细分画像，并做成独立技能以应对频繁迭代。 |
| [`实时演示文稿调度员 (live-deck-curator.md)`](live-deck-curator.md) | 需求调研通话结束后（或通话中），拉取录音转录并根据客户真实所言动态更新演示文稿中的业务场景与下一步。 |
| [`出海外呼拓客专员 (prospector.md)`](prospector.md) | 圈定账号与关键人，深挖专属个人切入点（亲自研读其 X 推文、把其做客的长视频看完），并草拟定制邮件。 |
| [`全局商业信号扫描员 (signal-scanner.md)`](signal-scanner.md) | 每天借助底层工兵蜂群大规模扫描目标客户清单的公网异动——融资、招聘、新闻、博客，快速把握商机。 |
| [`基于代码的技术答疑专家 (technical-expert.md)`](technical-expert.md) | 借助云端 Agent 直接深入代码库解答刁难，将其转化为通俗客户语言作答，且绝不泄露底层核心 IP。 |
| [`产品驱动增长遥测专员 (usage-signals.md)`](usage-signals.md) | 读取产品使用遥测数据，挖掘谁刚注册、核心超级用户是谁、哪些团队采纳了功能、哪些客户当前意向正温热。 |
| [`客户之声库 (voice-of-customer.md)`](voice-of-customer.md) | 归集每一笔赢单与丢单的真实动因，使外呼触达能够直奔同类客户最介意的痛点去进行精准破冰与召回。 |
| [`专属文风管家 (voice.md)`](voice.md) | 从你发出的高回复、近期真实邮件与消息中持续学习文风口吻，为不同沟通受众定制专属文风草稿。 |

## 售后交付与个人办公 (Post-sales & personal ops)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`承诺与托付双向追踪员 (commitment-tracker.md)`](commitment-tracker.md) | 维护两份清单：你答应别人的事，和你要求别人办的事。前者准时提醒，后者按期催办，杜绝信息黑洞。 |
| [`每日精选简报 (daily-digest.md)`](daily-digest.md) | 阅读你订阅但无暇细看的海量 Newsletter、播客与行业信息流，每天早晨呈递一份精炼高浓度摘要。 |
| [`会后工作台 (follow-up-desk.md)`](follow-up-desk.md) | 会议结束的第 1 秒：拉取转录、草拟跟进邮件、同步内部 Slack、赶制会上答应的材料，全部作为草稿呈现。 |
| [`收件箱智能排序员 (inbox-manager.md)`](inbox-manager.md) | 每天早晨将夜间堆积的邮件、Slack 消息和会议邀请按紧急度排序，对常规事项草拟回复，仅升级重要事务。 |
| [`内部情报雷达 (internal-radar.md)`](internal-radar.md) | 替你盯防 30–40 个内部 Slack 频道与大量更新邮件，每天向你呈递一份附带深度链接的重点简报。 |
| [`参会与会议纪要助理 (meeting-attendee.md)`](meeting-attendee.md) | 替你入会参会（静音、关摄、打招呼），会后发回决议要点，并将具体行动项准确路由给对应 Bot。 |

## 客户支持与服务 (Customer support)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`紧急客服告警员 (support-alert.md)`](support-alert.md) | 当工单命中高危升级规则（大客户被锁、流失风险）时由回复 Bot 呼叫，在专属 Slack 频道发帖并 @ 人类。 |
| [`客服基础设施与架构员 (support-infra.md)`](support-infra.md) | 搭建客服体系底座：安装连接器、配置 Evals 评测表与 Traces 链路追踪表，并在缺少连接器时拉起 Agent 现写。 |
| [`工单回复专员 (support-reply.md)`](support-reply.md) | 严格依据书面 SOP 闭环处理工单，带置信度门禁，并同时基于同一套知识库解答内部同事的咨询提问。 |
| [`客服自我调优专员 (support-tuner.md)`](support-tuner.md) | 发现知识盲区时提请补充知识库，复盘上周全部工单与 Traces 追踪日志，经审批后持续迭代优化支持体系。 |

## 市场营销与增长 (Marketing & growth)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`增长灵感记录员 (growth-ideas-logger.md)`](growth-ideas-logger.md) | 实时捕捉口述涌现的增长点子，自动整理录入增长手册，并按影响力和执行成本进行综合排期。 |
| [`市场调研专员 (market-researcher.md)`](market-researcher.md) | 深入研究产品与所处赛道，研读竞品落地页，明确指出定位差距与战略破局机会点，作为 Campaign 第一棒。 |
| [`营销效果分析师 (marketing-analyst.md)`](marketing-analyst.md) | 从广告后台拉取最新测试数据，指出优胜文案变体与核心指标表现，针对后续战略优化提出明确落地建议。 |
| [`效果投放专员 (performance-marketer.md)`](performance-marketer.md) | 在 Google Ads 等广告后台搭建投放 Campaign 骨架，配置文案变体，并随时发送操作截图供人类把关。 |
| [`产品营销专员 (product-marketer.md)`](product-marketer.md) | 基于调研起草定位简报、一句话卖点、价值主张，随后规划落地页大纲与广告测试矩阵，根据批注迭代。 |
| [`网站前端运维 (website-ops.md)`](website-ops.md) | 接收经确认的落地页简报并将其发布上线：提交代码 PR、展示进度截图与预览链接，确认后直接部署推向生产。 |

## 综合运营、会展与财务 (Operations, events & finance)

| 角色卡文件 | 一句话核心定位 |
|---|---|
| [`财务出纳与记账员 (bookkeeper.md)`](bookkeeper.md) | 追踪发票收据与报销开销，保持账目实时准确，对超预算行为实时预警——严格剥离任何直接转账动钱的权限。 |
| [`合同与政策初审员 (contract-reviewer.md)`](contract-reviewer.md) | 对场地租赁合同与商务政策开展第一道初审：标出异常条款、缺失的安全保护与偏离市场均价处，供专业法务复核。 |
| [`活动策划统筹 (event-planner.md)`](event-planner.md) | 统领整场活动的生产预算模型（场地、餐饮、人员、音视频、营销作为独立分项），并向各子级 Bot 下达预算参数。 |
| [`商务谈判与二手交易助手 (negotiator.md)`](negotiator.md) | 挂牌商品或索取报价，在你设定的底线框架内（底价红线、终止谈判规则）与交易对手方自主斡旋。 |
| [`政策审批与红线调研员 (permit-researcher.md)`](permit-researcher.md) | 深入调研特定行政管辖区针对该活动类型的许可要求、营业执照与合规红线，输出带有时间前置量的检查清单。 |
| [`活动场地侦察员 (venue-scout.md)`](venue-scout.md) | 检索符合活动硬性标准的候选场地，通过邮件批量发送 RFP 询价函，并在你预设的预算底线内开展初步谈判。 |

---

## 直播中出现但未收录在此的角色说明

- **挂机打天梯 Bot（Grind / Cheater）**：替主持人登录游戏刷天梯分数的恶搞 Bot。现场事实证明这纯属娱乐——Lauren 的天梯分甚至不升反降。
- **个人生活自动化（Personal Trackers）**：Karen Cheng 的快递物流追踪、缺货补货提醒；Matthew Berman 的电费套餐优化等——这些属于个人生活自动化，而非严肃团队角色。其本质是 `daily-digest` + `signal-scanner` 组合应用。
- **客服电话上的 xAI 语音 Agent**：属于产品原生功能特性，而非本体系内定义的数字同事。
