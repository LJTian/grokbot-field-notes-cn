[![SpaceX 工程师撰写的 Grok Bot 指南](guide/cover.png)](guide/grok-bot-guide-by-spacex-engineers-cn.pdf)

# Grok Bot 实战笔记 (Grok Bot Field Notes - 中文版)

> 本仓库是 [grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes) 的中文翻译与本地化版本。
> 现已提供 **24 页完整排版中文版 PDF** 与 **开箱即用的 Web 静态阅读页面（适配 Cloudflare Pages）**。

来自 xAI Grok Bot 团队的三位工程师在直播中用时 72 小时，利用自研的 Agent 平台从一个空仓库构建并发布了一款完整产品。团队成员包括：[Roshan Sadanani](https://www.linkedin.com/in/roshansadanani)（产品负责人）、[Lauren Tan](https://www.linkedin.com/in/laurenelizabethtan)（工程负责人，PStack 作者）以及 [Matt Palmer](https://www.linkedin.com/in/matt-palmer)（开发者体验）。

本仓库是对这三天高强度实战的全面提炼：一份精心排版的完整指南、一套可直接注入你的 Agent 的行为守则、九套业务职能剧本、包含 69 个 Bot 设定的角色名录，以及全程所有踩坑与翻车故障的完整日志。

---

## 📕 中文版指南与 Web 静态阅读器

- 📕 **中文版高清排版 PDF (24 页完整版)**：[guide/grok-bot-guide-by-spacex-engineers-cn.pdf](guide/grok-bot-guide-by-spacex-engineers-cn.pdf)（1:1 还原原著瑞士现代主义设计排版与页码结构）
- 🌐 **Web 交互阅读器源码目录**：[`public/`](public/)（包含 `index.html`，集成目录跳转、Prompt 一键复制、深色毛玻璃导航、响应式移动端适配）
- ⚙️ **自动化构建脚本**：[`build.py`](build.py)（单命令重新生成 HTML 与分发文件）

### 部署到 Cloudflare Pages

本项目 Web 静态站点位于 `public/` 目录，完全静态零第三方后端依赖，可直接接入 Cloudflare Pages 秒级全球部署：

1. 在 [Cloudflare Dashboard](https://dash.cloudflare.com/) 中进入 **Workers & Pages** -> **Create application** -> **Pages** -> **Connect to Git**。
2. 选择本仓库。
3. 在构建配置（Build settings）中设置：
   - **Framework preset**：`None`
   - **Build command**：（留空，无需构建命令）
   - **Build output directory**：`public`
4. 点击 **Save and Deploy**，即可获得全球 CDN 加速的在线阅读与 PDF 下载站点！

---

## 内容导航

| 路径 | 内容简介 |
|---|---|
| [AGENTS.md](AGENTS.md) | 编码 Agent 的核心行为守则。放置在仓库根目录，Agent 会自动读取并遵守。 |
| [ANTIPATTERNS.md](ANTIPATTERNS.md) | 直播中发生的 40 个真实翻车案例。记录：何处出错 → 为何出错 → 提炼出的通用准则。 |
| [agents/](agents/) | `AGENTS.md` 所引用的深度指导：验证机制、多 Agent 编排、技能与定时任务、Prompt 库。 |
| [roster/](roster/) | 69 个具体的 Agent 角色卡，每角色独立一文。涵盖职责边界、数据来源、人工审批权限及可直接复制的 Prompt 设定。 |
| [playbooks/](playbooks/) | 九大职能工坊剧本：研发、产品经理、创始人、销售工程、销售、SDR、客户支持、售后实施、市场营销。包含 Bot 团队架构、实际运行工作流、Prompt、定时例行任务与关键指标。 |
| [guide/](guide/) | [《SpaceX 工程师撰写的 Grok Bot 指南 (中文版)》](guide/grok-bot-guide-by-spacex-engineers-cn.pdf)（24 页排版 PDF）与 [英文原版 PDF](guide/grok-bot-guide-by-spacex-engineers.pdf)，以故事形式讲述三天全过程：心智模型、软件工厂、实战案例、故障日志与经济学核算。 |
| [public/](public/) | Cloudflare Pages 静态发布目录，提供现代化交互式 Web 阅读器及静态资产。 |
| [reference/](reference/) | 两份简明参考：[ECONOMICS.md](reference/ECONOMICS.md) 记录直播提及的所有成本与指标及背后规则；[PRODUCT.md](reference/PRODUCT.md) 梳理影响 Bot 设计的 Grok Bot 底层产品机制（记忆、复制/共享继承、隔离与权限）。 |
| [notes/](notes/) | 结构化实战笔记，按天记录。包含产品细节、工作流、Prompt、故障现场、量化数据及人员分工。所有材料均基于此整理。 |

## 从哪里开始

- **立刻给你的 Agent 注入行为守则**：直接复制 [AGENTS.md](AGENTS.md) 到你的仓库根目录。
- **Agent 总让你帮忙测试代码？**：阅读 [agents/VERIFICATION.md](agents/VERIFICATION.md)。
- **正在设计多 Agent 团队而非单个 Prompt**：阅读 [agents/ORCHESTRATION.md](agents/ORCHESTRATION.md)。
- **想要经过实战检验的高效 Prompt**：阅读 [agents/PROMPTS.md](agents/PROMPTS.md)。
- **在线阅读 24 章节全景图文**：打开 [public/index.html](public/index.html)。
- **寻找开箱即用的 Bot 职责设定**：查看 [roster/](roster/)，先读 [roster/README.md](roster/README.md)。
- **为特定职能（如客户支持、销售）搭建 Agent 体系**：查看 [playbooks/](playbooks/)，先读 [playbooks/README.md](playbooks/README.md)。
- **想知道踩过哪些坑**：阅读 [ANTIPATTERNS.md](ANTIPATTERNS.md)。
- **了解 Token 消耗与成本构成**：阅读 [reference/ECONOMICS.md](reference/ECONOMICS.md)。
- **决定哪些内容进记忆系统、哪些进角色描述**：阅读 [reference/PRODUCT.md](reference/PRODUCT.md)。
- **想阅读完整中文排版书籍**：阅读 [中文版 PDF (24页)](guide/grok-bot-guide-by-spacex-engineers-cn.pdf)。
- **核实某个具体事实或数据**：查阅 [notes/](notes/) 原始笔记。

## 一句话精髓

为每个 Agent 分配单一且明确的职责，并赋予一个名字。在构建第二个 Agent 之前，必须先搭建好确定性验证循环。

让 Agent 在着手修复 Bug 之前必须先精准复现，提交任何工作成果都必须附带证据。每当出现错误，提炼通用的底层原则，绝不要拘泥于具体的偶发故事。

每周审计你的定时例行任务（Routines），因为执行频率才是产生大额账单的根源。无论自动化循环运转得多么顺畅，在涉及数据库迁移、线上部署、资金与权限变更时，务必保留人类最后把关。

## 开源协议

MIT 协议。欢迎自由复制本仓库内容至你自己的项目中。
