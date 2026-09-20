# -*- coding: utf-8 -*-
# Pages 17 to 24 for Chinese Grok Bot Guide
from pages_part1 import get_header, get_footer

def render_page_17():
    return f"""
  <div class="page" id="page-17">
    {get_header()}
    <div class="eyebrow">14 · CASE STUDY</div>
    <h1 class="page-title">72 小时从零打造 Thursday Arena</h1>
    <p class="page-intro">
      一款多人自动对战游戏：将官方公开市场上可用的真实 Bot 抓取为参战角色，为其自动赋予稀有度等级、AI 生成的角色立绘、基础数值与专属技能。由三名人类与一支由 Bot 构成的团队联合构建，在第 3 天上午 10 点，通过一个头像完全空白的全新 X 账号发推正式公测发布。
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">它是如何被一步步构建出来的</div>
        <ul class="custom-bullets">
          <li><strong>极速原型先行</strong> —— 纯原生 HTML/CSS/JS，内存状态管理，无数据库，无用户鉴权。从始至终唯一衡量标准：这个对局玩起来到底好不好玩？</li>
          <li>好玩的玩法闭环验证通过后，用 React/Next.js 全面重写，严谨划分前后端架构。</li>
          <li>后端采用 Vercel Serverless 上运行的 Go 语言，数据库选用 PlanetScale，登录接入 Clerk（Sign in with X），跨网络数据校验引入 Zod。</li>
          <li>卡牌立绘由 Grok Imagine 实时生成；角色采用代码而非静态雪碧图渲染，以便程序化动态切换状态。</li>
          <li>早期故意删光了所有测试用例 —— “Agent 通常很不擅长写测试代码” —— 决定把代码质量重构推迟到后序阶段。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">起决定性作用的产品取舍决策</div>
        <ul class="custom-bullets">
          <li><strong>坚决杜绝数值付费买赢 (No pay-to-win)。</strong> 曾被反复讨论，但被当场坚决否决。原生广告、赞助专属卡牌和实体周边才是首选商业化路径。</li>
          <li><strong>残酷地砍掉复杂功能 (Ruthless cutting)。</strong> 石头剪刀布克制机制、冗长的复杂数值面板、多战场地图……统统被果断砍掉，仅保留最极致流畅的单核心对战循环。</li>
          <li><strong>为 Agent 定制专用的规则解释接口。</strong> 团队上线了 <code>/rules</code> 页面，供 Agent 在需要澄清游戏规则时自行联网抓取阅读。</li>
          <li><strong>用确定性函数替代模型的主观随性发挥。</strong> 战斗裁决逻辑全写在纯 Go 代码中，绝不交由 LLM 凭空想象胜负。</li>
        </ul>
      </div>
    </div>

    <div class="section-label">72 小时从零构建并发布上线所达成的核心指标</div>
    <div class="grid-4col">
      <div class="stat-card">
        <div class="stat-val">433</div>
        <div class="stat-desc">代码库累计合并的 PR 总数，全部由云端 Agent 和 Potato 模式流水线编写并推送</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">2,000+</div>
        <div class="stat-desc">公测发布数小时内涌入体验的真实玩家总数，全部来自一个白号推文传播</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">100+</div>
        <div class="stat-desc">游戏中可供解锁的参战 Bot 角色总数，全部由 Bot 自动抓取市场卡片并生成立绘</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">72h</div>
        <div class="stat-desc">从空无一物的 GitHub 组织，到产品正式面对全球公测并稳定支撑高并发的全部耗时</div>
      </div>
    </div>
    {get_footer(17)}
  </div>
    """

def render_page_18():
    return f"""
  <div class="page" id="page-18">
    {get_header()}
    <div class="eyebrow">15 · THE ROSTER</div>
    <h1 class="page-title">工厂团队全员花名册</h1>
    <p class="page-intro">
      支撑 Thursday Arena 从零诞生的真实 Bot 团队阵容。值得将其作为组织设计的标准模板仔细研读：<strong>请注意真正写代码的 Bot 占比有多么稀少，而绝大多数 Bot 的存在仅仅是为了检查、路由、分类或抓取</strong>。
    </p>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Dr. Eggbot（蛋头博士）· 元工匠</span>
        <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">调用频率最高</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        负责创建并审查其他所有 Bot。撰写它们的基础描述，为它们起名字，随时解答“当前我们的系统瓶颈在哪”。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Steve · 幕僚长 (Chief of Staff)</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">中央调度枢纽</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        团队总协调。人类几乎所有指令都经由他分流派发。在大家嘲笑团队里究竟有多少个“幕僚长”之后，被特意赋予了这个真人名字。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Cupcake Eng · 研发总指挥</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">工程交付核心</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        通过驱动 Potato 模式与云端 Agent 来掌控整体工程成果，全程监督、调度并最终验证交付。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Bake · 创始工程师 (Founding Engineer)</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">代码合并哨兵</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        监控 PR 动态、执行代码合并，并为特定 Bug 现场唤起云端 Agent。曾被人类用语音电话直接呼叫并在直播中途在线合并了一项 PR。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Chrome / Play · 真机试玩员</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">端到端最后把关</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        紧盯通过 CI 检查的 PR，并在真正放行合并前，在真实浏览器中亲自把整款游戏完整跑通玩一遍。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Crumble & Hashbrown · Bug 分流与二次校验二人组</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">双重质检机制</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        Crumble 配合试玩员重现报障并录入确认项；Hashbrown 作为质检员的质检员，在自动化流水线获准介入前二次复核其分类是否准确无误。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Comment Sicko · 注释死神</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">代码库代码净化</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        无情清理多余无用的代码注释。核心逻辑非常深刻：Agent 往往习惯性用注释作为留下 Hack 和临时补丁的借口而不去根治问题，这些注释积重难返会导致代码库彻底腐烂。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Whisk (Crit) & Glow (Tone) · 策划评审与音画探索</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">游戏设计核心</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        Crit 在发布首日清晨做出的严厉评判 —— “这游戏太难了”，直接在上线前重构了数值平衡；Glow 则用 Strudel 和 Suno 生成背景音乐并丢进 Notion 供人类试听。
      </div>
    </div>

    <div class="card" style="margin-bottom: 5.5pt; padding: 5.5pt 9pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.3pt;">Ping、数据科学家、Vincent (Cerebro) · 运营监控三人组</span>
        <span style="font-size:7.2pt; color:#666; font-weight:600;">日常运转中枢</span>
      </div>
      <div style="font-size:7.6pt; color:#444; line-height:1.35; margin-top:1.5pt;">
        Ping 监控 @ 消息并沉淀回 Notion；数据科学家在上线首日每 15 分钟出具一份报表；Vincent 则负责拓展增长并把找出的 ICP 导入营销流水线。
      </div>
    </div>

    <div class="footnote">
      *团队的命名哲学全是以土豆或烘焙为灵感，合并 PR 在内部被戏称为一次“MASH（捣成泥）”。这些好玩的词汇从 Dr. Eggbot 泄露到了整个 Notion 正式项目管理流程中，反倒让团队谈论工作的频次大幅增加。
    </div>
    {get_footer(18)}
  </div>
    """

def render_page_19():
    return f"""
  <div class="page" id="page-19">
    {get_header()}
    <div class="eyebrow">16 · FROM THE FIELD</div>
    <h1 class="page-title">一线实战名录：售后实施与市场营销</h1>
    <p class="page-intro">
      三天中穿插的专项业务工坊是全场最可直接抄作业的实操范本。以下是各位实战业务专家在各自真实工作流中所实际部署的落地配置。
    </p>

    <div class="section-label">售后交付部署 · Blake (AI Deployment Manager)</div>
    <div class="card" style="margin-bottom: 10pt;">
      <div class="card-title">单一联系窗口，单客户独立专员架构</div>
      <div class="card-body">
        <p><strong>“Gus 是我最好的铁哥们。”</strong> Blake 永远只和一个名为 Gus 的 Bot 对话，而 Gus 负责统管其麾下的 15~20 名垂类专家，不设任何冗余中间层。</p>
        <div class="grid-2col" style="margin-top: 6pt;">
          <div>
            <div style="font-weight:700; color:#111; font-size:8pt; margin-bottom:2pt;">核心团队构成：</div>
            <ul class="custom-bullets">
              <li><strong>Gus</strong> —— 幕僚长，人类唯一的专属沟通接口</li>
              <li><strong>Frankie</strong> —— 客户会议纪要及承诺跟进</li>
              <li><strong>Wally</strong> —— 针对不同客户受众调校沟通语气风格</li>
              <li><strong>Trudy</strong> —— 内部知识与制度的权威事实源</li>
              <li><strong>客户专员</strong> —— 每个客户独立专属一个 Bot，独家掌握该客户全量上下文</li>
            </ul>
          </div>
          <div>
            <div style="font-weight:700; color:#111; font-size:8pt; margin-bottom:2pt;">日常工作习惯：</div>
            <ul class="custom-bullets">
              <li>随口一问“Harbor 客户进展如何？”，系统立即汇总其风险、当前阻塞、悬空承诺与下一步 —— 外加一句强制附带的太空笑话。</li>
              <li><strong>每周自省扫描 (Self-improvement scan)</strong>：自动审计哪些重复工作应当被固化自动化，并将 Blake 手动改动的草稿进行 diff 对比以自适应学习其语言风格。</li>
              <li>每周自省建议<strong>严格封顶 1 条</strong> —— 无休止的主动提议纯属垃圾邮件骚扰。</li>
            </ul>
          </div>
        </div>
      </div>
      <div style="margin-top: 5pt; font-size: 7.9pt; font-style: italic; color: #555;">
        “唯一能限制住你的 Grok Bot 的瓶颈，就是你自己对‘究竟什么才是可能的’这件事情的想象力。”
      </div>
    </div>

    <div class="section-label">全栈市场营销 · Josh Kim (6-Bot Campaign Team)</div>
    <div class="card">
      <div class="card-title">最后招聘的那个 Bot，负责驱动前面的所有 Bot</div>
      <div class="card-body">
        <p>市场研究员 → 产品营销 (PMM) → 官网运营 → 效果投放 → 营销数据分析师。紧接着，团队构建了第 6 个 Bot —— <strong>项目经理 (PM)</strong>，它通过深入研读前 5 个角色的职责与上下游交接规范，蜕变为统领整个营销推广活动端到端运转的单一接洽总管。</p>
        <div class="grid-2col" style="margin-top: 6pt;">
          <div>
            <div style="font-weight:700; color:#111; font-size:8pt; margin-bottom:2pt;">如何定义职责边界：</div>
            <ul class="custom-bullets">
              <li>“这非常类似于在写岗位招聘启事” —— 为每个 Bot 划定泾渭分明的独立泳道。</li>
              <li>产品定位简报通过 Google Docs 的在线评论闭环层层审阅，正如真人同事互相 Review 一样严谨。</li>
            </ul>
          </div>
          <div>
            <div style="font-weight:700; color:#111; font-size:8pt; margin-bottom:2pt;">Josh 的落地忠告：</div>
            <ul class="custom-bullets">
              <li>在前期尽早接入 Slack 和企业邮箱，然后向它直接提问：“你现在能为我分担什么？”</li>
              <li><strong>“多给你的 Bot 投资”</strong> —— 持续提供的反馈和上下文具有长远复利，正如培养一位真实队友。</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    {get_footer(19)}
  </div>
    """

def render_page_20():
    return f"""
  <div class="page" id="page-20">
    {get_header()}
    <div class="eyebrow">16 · FROM THE FIELD, CONTINUED</div>
    <h1 class="page-title">销售、技术支持、拓客与个人自动化</h1>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">💼 销售大客户业务 · Krista</div>
        <div class="card-subtitle">作为贯穿混乱工具链的统一编排层</div>
        <div class="card-body">
          <p>Olive (幕僚长)、PG (线索拓展)、Echo (调取 Gong 和 Granola 真实会话录音实时定制宣讲 PPT)，加上客户专家与工程支援 Bot。Notion 作为中央档案库，Grok Bot 跨越 Salesforce、Slack 和 Databricks 调度 —— “没有任何一家公司能完美地把数据整理在同一处。”</p>
          <div style="margin-top:4pt; font-size:7.8pt;">
            <strong>产生质变的切入点</strong>：拿自己过往发出的 Gmail、Slack 和 X 聊天历史对 Bot 进行刻意微调，彻底杀灭千篇一律的机械 AI 腔调。先连接你每天重度依赖的工具；对待 Bot 要像对待亲自上阵的执行者（“替我去听完那几场技术研讨会，并起草好开发信”），而非仅仅丢链接给你的资料检索员。
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-title">🎧 客户技术支持 · David</div>
        <div class="card-subtitle">4 大专职 Bot，背靠一套严密的评测 (Evals) 表格</div>
        <div class="card-body">
          <p>Build (基础建设)、Reply (工单与 Slack 响应)、Alert (流失预警与封号提醒)、Tune (自省学习与知识库沉淀)。跨工单系统、Stripe、Notion 和 Slack 实机运转：常见重置全自动秒回；复杂的 SSO 故障以低置信度警告安全移交人工；退款诉求依规驳回；知识库盲区打上标签报请人工批准。</p>
          <div style="margin-top:4pt; font-size:7.8pt;">
            <strong>非技术人员的护栏机制</strong>：设立单独的评测结果表与逐次运行追踪 (Trace) 表，且评测针对 PR 分支直接跑。给非技术人员提供模板而非代码参数，修改知识库走 GitHub PR 审查，把 git 基础设施作为安全防线。
          </div>
        </div>
      </div>
    </div>

    <div class="grid-2col" style="margin-top: 8pt;">
      <div class="card">
        <div class="card-title">🎯 销售拓客 (SDR) · Simon</div>
        <div class="card-subtitle">单平台单 Bot 专攻，大军团集群作战</div>
        <div class="card-body">
          <p>幕僚长统领 Shakespeare (专门把控邮件语气)、负责驱动海量工兵的联网检索 Bot，以及客户画像 Bot —— 每天挖掘 50 个新目标，清晨自动置顶前 5 个黄金线索。<strong>“你的每一封邮件都绝不能看起来像群发模板。”</strong> 按职能进行色标管理，一眼辨明客户阶段。</p>
        </div>
      </div>
      <div class="card">
        <div class="card-title">🏡 个人超级自动化 · Karen Cheng</div>
        <div class="card-subtitle">大道至简：打造一打极端无聊的专用 Bot</div>
        <div class="card-body">
          <p>反其道而行之：维护十几个极其枯燥但超实用的单任务 Bot —— 包裹物流追踪、商品补货通知、以及一个早间新闻 Bot（它在局域网内自己找到了家里的无线打印机，每天清晨自动打印出当天专属新闻报纸）。</p>
          <p style="margin-top: 3pt; font-weight: 600; color: #111;">“找到你生活中的痛点或烦恼，然后干脆利落地解决掉它。这已经不再是氛围写代码 (Vibe Coding)，这纯粹就是在享受生活 (Vibing)。”</p>
        </div>
      </div>
    </div>
    {get_footer(20)}
  </div>
    """

def render_page_21():
    return f"""
  <div class="page" id="page-21">
    {get_header()}
    <div class="eyebrow">17 · FAILURE LOG</div>
    <h1 class="page-title">直播现场真实翻车实录</h1>
    <p class="page-intro">
      全程未剪辑的现场直播展现了最残酷、最真实的工程现场。以下是当着成千上万名线上观众的面当场发生的典型翻车事故，以及由每一场事故提炼出的不可动摇的黄金法则。
    </p>

    <div class="fail-item">
      <div class="fail-head">
        <span>Agent 编写的角色规则严重过度拟合 (Overfitting)</span>
        <span class="fail-day">第 2 天 · 规则层事故</span>
      </div>
      <div class="fail-desc">一次故障后自动生成的 Bot 描述，把当天的具体报错和偶发细节全部硬编码成了永久设定。</div>
      <div class="fail-rule">提炼法则：当一条规则脱胎于某次糟糕事故时，必须剥离事故细节，只保留底层通用原则。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>闪光动效吞没了所有卡牌视觉 (CSS Shimmer Bug)</span>
        <span class="fail-day">第 2 天 · 前端呈现事故</span>
      </div>
      <div class="fail-desc">本意用于提示高稀有度卡牌的闪光效果被滥用泛化，导致所有卡牌无差别全在闪烁，彼此无法区分。</div>
      <div class="fail-rule">提炼法则：明确声明期望达成的业务甄别目标，而不要仅仅命令它堆砌视觉特效。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>正式上线官网出现凭空捏造的虚假内容</span>
        <span class="fail-day">第 2 天 · 真实性事故</span>
      </div>
      <div class="fail-desc">Agent 在产品主页上随意编造了看似合理的虚假 Bot，并将内部研发原型代号泄漏进面向用户的展示文案中。</div>
      <div class="fail-rule">提炼法则：绝不伪造数据。明确指出权威事实源，并明确下达“去真实系统里给我查”的指令。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>承诺的 3D 原型实际上做成了伪 2.5D</span>
        <span class="fail-day">第 2 天 · 工具链缺失</span>
      </div>
      <div class="fail-desc">要求提供 3D 动画，Agent 却用 CSS 搓出了 2.5D 效果 —— 因为提示词里从未告诉它使用专业的 3D 类库。</div>
      <div class="fail-rule">提炼法则：凡是行业存在成熟标准工具或公认库的任务，必须指名道姓要求其调用。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>利用浏览器控制台公然修改数值作弊</span>
        <span class="fail-day">第 2 天 · 安全架构事故</span>
      </div>
      <div class="fail-desc">游戏逻辑完全放在前端，开发者在直播镜头前打开 DevTools 控制台直接篡改攻击力和血量作弊。</div>
      <div class="fail-rule">提炼法则：涉及信任与竞争的核心逻辑必须由服务端权威判定；隐藏调试开关不是安全防线。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>Bot 擅自开 PR 违背团队“直接推 Main”的口头约定</span>
        <span class="fail-day">第 1 天 · 规范未明文化</span>
      </div>
      <div class="fail-desc">在团队口头约定直接快打推主干阶段，Bot 依然我行我素提了 PR。</div>
      <div class="fail-rule">提炼法则：人类之间未落笔的默契对 Bot 不存在。所有规范必须明文写进 Bot 能读取的文件中。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>虚拟机上的第三方登录会话周期性断开</span>
        <span class="fail-day">第 2 天 · 无人值守中断</span>
      </div>
      <div class="fail-desc">Karen Cheng 依赖的无感自动化频繁罢工，因为 Bot 虚拟机里的浏览器会话频繁掉线。</div>
      <div class="fail-rule">提炼法则：对于需要完全无人值守稳定运行的长效任务，优先采用 MCP 连接器而非浏览器模拟。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>自动化软件工厂把正在运行的线上游戏打挂</span>
        <span class="fail-day">第 3 天 · 生产严重故障</span>
      </div>
      <div class="fail-desc">一个自动修复提交了一条劣质 SQL 查询，直接导致生产环境崩溃，而当时现场正在大谈“克制”。</div>
      <div class="fail-rule">提炼法则：无论自动化闭环多么美妙，在涉及数据库迁移与线上生产部署前，必须保留人类最后审查。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>明文 API Token 密钥在直播大屏幕上暴露</span>
        <span class="fail-day">第 3 天 · 凭据泄漏事故</span>
      </div>
      <div class="fail-desc">敏感私钥被直接暴露在投屏画面上，几秒钟内被紧急吊销作废。</div>
      <div class="fail-rule">提炼法则：在安全体系中，人类永远是机密保管中最脆弱的一环，严禁通过明文渠道传递密钥。</div>
    </div>

    <div class="fail-item">
      <div class="fail-head">
        <span>上线数小时内用户反馈渠道遭遇海量垃圾灌水</span>
        <span class="fail-day">第 3 天 · 防护门禁缺失</span>
      </div>
      <div class="fail-desc">上线后被垃圾刷屏，事后紧急追加了 20 字符下限、敏感词过滤、防注入、模型安全防护与限流。</div>
      <div class="fail-rule">提炼法则：所有的输入净化、内容审查与风控门禁，必须随同表单一起发布，绝不要事后补救。</div>
    </div>
    {get_footer(21)}
  </div>
    """

def render_page_22():
    return f"""
  <div class="page" id="page-22">
    {get_header()}
    <div class="eyebrow">18 · LIMITS AND ROADMAP</div>
    <h1 class="page-title">现在的能力边界与未来路线图</h1>
    <p class="page-intro">
      以下内容均在直播过程中的问答环节由官方坦诚直言披露。在基于该产品规划工作流之前，清晰知晓哪些设想“目前根本不可行”能帮你少走数周弯路。
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">🚫 当前坚决亮红灯的硬性限制</div>
        <ul class="custom-bullets">
          <li><strong>仅支持 Linux 环境</strong>：既不支持 Linux 又没有封装为 MCP 的专有客户端工具，彻底无法运行（问答中官方直接回答“不行”）。</li>
          <li><strong>人机验证码 (CAPTCHA) 会彻底阻断自动化</strong>：官方不提供任何破解黑客方案；正规建议是配置白名单让 Bot 绕开此类网站，而非尝试对抗。</li>
          <li><strong>不支持跨企业账号间直接发消息</strong>：你的 Bot 无法与属于其他客户企业账号的 Bot 直接对话沟通。</li>
          <li><strong>虚拟机里的浏览器 Session 会过期</strong>：网页的登录态无法永久维持，可能打断长期无人值守的任务。</li>
          <li><strong>缺乏从其他 Agent 框架平滑迁移的工具</strong>：除导入模板并重新挂载上下文外，不存在自动迁移路径。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">🚀 官方明确表态正在开发中的特性</div>
        <ul class="custom-bullets">
          <li><strong>双向语音通话 (Two-way voice)</strong> —— 在第 3 天直播中已现场 Demo，后续陆续向全体用户灰度推开。</li>
          <li><strong>多人在线协作 (Multiplayer)</strong> —— 允许多个人类与多个 Bot 同时置身于同一个共享聊天室（目前只能在 Slack 里 @ 点名曲线实现）。</li>
          <li><strong>跨机器综合管控</strong> —— 攻关解决一个 Bot 调度多台机器时容易陷入迷茫的难题。</li>
          <li><strong>基于业务角色的智能入职向导</strong> —— 新用户登录时只需阐述其岗位，系统自适应推荐全套预装模板。</li>
          <li><strong>大幅提升 Computer Use 执行速度</strong> —— 针对最核心的操作迟滞痛点进行深层架构加速。</li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">全场工程师无人能够回避的终极命题：非确定性</div>
        <p class="callout-text">
          大语言模型天生具备概率与非确定性特征，一旦要求它强制执行某项不可动摇的严格制度时，这就成了硬伤。现场给出的工程化解法非常精妙：<strong>让 Bot 为该制度写出纯代码逻辑 —— 一个确定性的判断分支树或纯函数；往后每次遇到此类决策，直接调用这段确定性代码运行，而不是每次让模型重新开脑洞瞎猜</strong>。这与验证 CLI 的哲学高度一致：凡是两次输入应当产生相同结果的逻辑，就坚决用确定性工具替换主观自由发挥。
        </p>
      </div>
    </div>

    <div class="footnote">
      *本章内容反映直播期间的技术快照。请将局限性章节视为一种产品能力轮廓而非永久规格说明：在基于某个重度功能落地之前，务必对照当下的最新官方文档进行核实。
    </div>
    {get_footer(22)}
  </div>
    """

def render_page_23():
    return f"""
  <div class="page" id="page-23">
    {get_header()}
    <div class="eyebrow">19 · THE RETROSPECTIVE</div>
    <h1 class="page-title">终场复盘时团队的真诚坦白</h1>
    <p class="page-intro">
      第 3 天的最后半小时是整整 72 小时直播中最具含金量的宝藏段落 —— 因为三位工程师彻底停下了华丽的产品演示，开始开诚布公地复盘这三天走过的弯路与心底的真相。
    </p>

    <div class="quote-box">
      <p class="quote-text">“创造任何东西时最艰难的部分 —— 哪怕你手握近乎无限的 AI 神力 —— 依然是如何让真实世界里的人们真正去在乎它。”</p>
      <p class="quote-author">Roshan · 闭幕复盘致辞</p>
    </div>

    <div class="section-label">终局复盘提炼出的五大真理</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>分发渠道是这次实验能跑通的唯一支柱。</strong> 涌入的大批玩家纯粹来源于直播活动本身的注意力，而非产品本身已经具备了不可抗拒的魔力。第 14 章中的所有亮眼指标都必须带上这个先决限定条件。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>做你自己懂的业务。</strong> 天真幼稚的空想 —— “我只要给模型下指令让它去帮我挣钱就行了”被现实无情打脸。专职负责商业变现的 Agent 辛勤奔忙了一整天，产生的实际营收正好是 $0。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>就方向达成共识，远比动手写代码艰难百倍。</strong> 第 1 天历经 4 次大转型，交付产出为 0。拖慢人类步伐的从来都不是软件开发速度本身。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>克制在今天已成为一种稀缺的核心工程美德。</strong> Lauren：“你如今拥有近乎无限的算力，能在一天内堆出拥有一百万个功能的庞然大物，但它们可能全是一堆垃圾。自我克制是一种必须刻意培养的纪律。” 大刀阔斧地砍掉鸡肋功能，才让游戏得以按时上线。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">5</div>
        <div class="num-content">
          <strong>真实需求的探索依然只能由人类亲自肉身完成。</strong> “你必须亲自作为人类走进真实世界，敏锐捕捉真实问题。一旦你找到了解决它的通路，你就可以把它做成一个 Bot，让它不知疲倦地永远运行下去。”
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">Bot 真正极其擅长的地方</div>
        <ul class="custom-bullets">
          <li>弥补人类专业知识盲区 —— 团队涉足了大家此前从未做过的领域。</li>
          <li>没人愿意去做的枯燥繁重的重复性真机回归测试。</li>
          <li>在大脑根本装不下的三天高压项目中始终保持全局上下文。</li>
          <li>把口头随性迸发的灵感即时录入为排序好的待办，而不打断对话思路。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">依然只能完全归属人类的核心能力</div>
        <ul class="custom-bullets">
          <li>决定究竟什么东西才值得被造出来。</li>
          <li>面对无休止的功能蔓延，坚决果断地说“不”。</li>
          <li>在一款游戏还不好玩时，敏锐本能地感受到它的枯燥。</li>
          <li>真实人际关系的连接、彼此的深层信任，以及复杂的模糊价值判断。</li>
        </ul>
      </div>
    </div>

    <div class="footnote">
      *Roshan 的自我反思习惯极具借鉴价值：定期反思“我目前在流程中是否介入过多？我怎样才能让这个环节更加自主？”，并专门设定一个定时 Bot 定期向自己抛出这个问题。
    </div>
    {get_footer(23)}
  </div>
    """

def render_page_24():
    return f"""
  <div class="page" id="page-24">
    {get_header()}
    <div class="eyebrow">20 · START HERE</div>
    <h1 class="page-title">你的第一周落地行动清单</h1>
    <p class="page-intro">
      本清单经过精心排定先后顺序，<strong>确保前面的每一步都在让随后的下一步变得更加低廉与稳健</strong>。对于什么是最重要的先决条件，Lauren 给出的排名出乎很多人的意料：“Grok Bot 最关键的事情甚至不是去新建 Bot，而是首先把你日常所用的所有工具和插件统统打通。”
    </p>

    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>第一步先连接你每天重度使用的基础技术栈。</strong> 在造第一个 Bot 之前：接通 Slack、邮箱、日历、项目管理软件和代码仓库。在速度、成本与可靠性上，连接器每一次都全方位碾压浏览器视觉模拟。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>录制一段 15 分钟的真实语音备忘录。</strong> 讲述你是谁、你的职责是什么、目前的业务痛点在哪、哪些繁琐事情需要自动化。把转录文本丢给你的第一个 Bot，让它来反向为你量身设计一套系统。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>挑出你一天工作中感觉最恶心烦躁的那个环节。</strong> Amrita 与 Karen Cheng 共同的痛点发掘心法：不要挑那个看起来最高大上的，就挑最让你恶心烦躁的那一件小事。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>创建一个高度专精的窄角色，并以“只读模式”启动。</strong> 仅限查阅并总结，然后是撰写内部草稿，唯有确立了信任才放开写入权限。在事故发生之前把审批防护网先织好。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">5</div>
        <div class="num-content">
          <strong>在 Bot 的注视下，人类亲自把任务走通一遍。</strong> 点击“示教任务”。随后手动为其补齐分支判断、异常兜底与人工审批门禁 —— 单凭一次示范是无法自发推演出严密逻辑的。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">6</div>
        <div class="num-content">
          <strong>在造第二个 Bot 之前，先把确定性验证闭环搭建好。</strong> 哪怕初期再粗糙。只要 Bot 能对照真实客观的信号自查工作成果，往后的一切运转都会成倍加速且成本暴跌。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">7</div>
        <div class="num-content">
          <strong>直到现在，才引入幕僚长 Bot。</strong> 并且后续诞生的每一个新 Bot 都由它亲自把关创建，让它时刻通晓全员的职责定位。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">8</div>
        <div class="num-content">
          <strong>将每一次日常纠偏沉淀为通用原则。</strong> 每次它思考走偏时，写下普遍性法则 —— 坚决剔除具体事件细节。正是这种持续的复利沉淀，让第三个月的体系与第一周有天壤之别。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">9</div>
        <div class="num-content">
          <strong>在周五定期审计所有例行任务。</strong> 触发频次是资金流失的元凶。任何被定为定时轮询、但其实可以改用 Webhook 事件驱动的任务，果断迁移。
        </div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🚫</div>
      <div class="callout-body">
        <div class="callout-title">以及，唯一坚决不要做的事情</div>
        <p class="callout-text">
          <strong>绝不要因为好玩有趣就随手捏造一个 Bot。</strong> 创造一个 Bot 确实非常有趣，而这恰恰是问题的根源。每一个新招聘的 Bot 都会产生上下文沉淀开销、带来定时任务调用、分散团队注意力。在直播中拥有最庞大 Bot 队伍的人，反而是呼吁控制规模最激烈的声音。当产生这种冲动时，先问问现有的专家 Bot 是否只需补齐一项新技能即可解决。
        </p>
      </div>
    </div>

    <div class="quote-box" style="margin-top: 5pt; border-left: 3.5px solid #111;">
      <p class="quote-text" style="font-size: 13pt;">“为什么不从今天开始？ (Why not today?)”</p>
      <p class="quote-author">Roshan 永久挂在 Slack 上的状态签名，也是全书最好的收尾寄语</p>
    </div>
    {get_footer(24)}
  </div>
    """
