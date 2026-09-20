# -*- coding: utf-8 -*-
# Pages 1 to 8 for Chinese Grok Bot Guide

def get_header():
    return """
    <div class="header">
      <div class="header-left">
        <span class="dot"></span>
        <span>GROK BOT</span>
      </div>
      <div class="header-right">实战指南 · XAI</div>
    </div>
    """

def get_footer(pno):
    return f"""
    <div class="footer">
      <div>{pno:02d}/24</div>
      <div>x.ai/bot</div>
    </div>
    """

def render_page_01():
    return """
  <div class="page cover" id="page-01">
    <div class="cover-header">
      <h1 class="cover-title">SpaceX 工程师撰写的<br>Grok Bot 实战指南</h1>
      <p class="cover-sub">72 小时现场直播构建，3 天高强度实战全景复盘。</p>
    </div>
    <div class="cover-image-container">
      <img src="cover-people.png" class="cover-image" />
    </div>
  </div>
    """

def render_page_02():
    items = [
        ("01", "实 战 实 验", "3 天高强度直播构建真正沉淀的实操成果"),
        ("02", "心 智 模 型", "队友，而非一次性任务 —— 视角的转变如何彻底改变你的工作流"),
        ("03", "Bot 拥有的资源底座", "专属计算机、独立记忆，以及团队共享的文件系统"),
        ("04", "搭建第一支团队名录", "一 Bot 一职 —— 以及如何避免 Bot 无序蔓延的陷阱"),
        ("05", "制造 Bot 的元 Bot", "Dr. Eggbot、作为灵魂的角色描述，以及纠正过度拟合"),
        ("06", "技能与例行任务", "通过动作示范来示教，并从日常纠偏中沉淀可复用技能"),
        ("07", "软 件 工 厂", "Potato 模式、Agent 蜂群，以及全自动无人驾驶流水线"),
        ("08", "确定性验证胜于一切", "在构建第二个 Bot 之前必须最先搭建的高杠杆武器"),
        ("09", "经受住检验的 7 大 Prompt 招式", "在 3 天直播中多位工程师高频复现的实战肌肉记忆"),
        ("10", "原汁原味 Prompt 库", "直接摘录自直播现场的原生 Prompt 话术"),
        ("11", "规 模 化 编 排", "幕僚长机制、动态剧本广播、Bot 决策例会与子 Bot 军团"),
        ("12", "经 济 学 核 算", "真实的 Token 与算力开销，以及资金暗中流失的 4 大暗坑"),
        ("13", "权限、机密与爆炸半径", "带有刹车的自主权、自动审查、安全金库与服务端权威判定"),
        ("14", "实战案例：Thursday Arena", "72 小时内从零构建并发布一款多人对战游戏"),
        ("15", "工 厂 团 队 花 名 册", "支撑 Thursday Arena 运行的每一个 Bot 及其职责划分"),
        ("16", "来 自 一 线 的 名 录", "覆盖研发、售后、营销、销售、支持与个人自动化的 6 大实战配置"),
        ("17", "直 播 翻 车 实 录", "直播镜头前发生的 10 大真实故障以及提炼出的通用原则"),
        ("18", "现 状 与 路 线 图", "目前产品明确拒绝的能力边界，以及即将推出的核心特性"),
        ("19", "终 场 复 盘 坦 白", "72 小时流媒体尾声，团队停下 Demo 展开的真诚反思"),
        ("20", "第 一 周 行 动 清 单", "今天即可着手落地的 9 步走起步指南与 1 个绝不要做的事"),
    ]
    
    page_map = {
        "01": "03", "02": "04", "03": "05", "04": "06", "05": "07",
        "06": "08", "07": "09", "08": "10", "09": "11", "10": "12",
        "11": "14", "12": "15", "13": "16", "14": "17", "15": "18",
        "16": "19", "17": "21", "18": "22", "19": "23", "20": "24"
    }

    rows_html = ""
    for num, title, desc in items:
        target_page = page_map.get(num, "03")
        rows_html += f"""
      <a href="#page-{target_page}" class="toc-item">
        <span class="toc-num">{num}</span>
        <span class="toc-title">{title}</span>
        <span class="toc-desc">{desc}</span>
      </a>
        """
    
    return f"""
  <div class="page" id="page-02">
    {get_header()}
    <div class="eyebrow">TABLE OF CONTENTS</div>
    <h1 class="page-title">指南目录与核心全景</h1>
    <div class="toc-list">
      {rows_html}
    </div>
    {get_footer(2)}
  </div>
    """

def render_page_03():
    return f"""
  <div class="page" id="page-03">
    {get_header()}
    <div class="eyebrow">01 · THE EXPERIMENT</div>
    <h1 class="page-title">三天，一家公司，全程直播</h1>
    <p class="page-intro">
      来自 Grok Bot 团队的三位工程师 —— <strong>Matt Palmer</strong>（开发者体验）、<strong>Roshan</strong>（产品负责人）与 <strong>Lauren</strong>（“Potato”，工程架构负责人，PStack 作者） —— 坐在旧金山的一个演播室里，面对空无一物的 GitHub 组织、空的 Slack、空的 Notion，且没有任何既定商业想法。72 小时后，他们交付了一款拥有数千名玩家的线上产品。本指南中的所有内容，全部提炼自这三场无剪辑的高强度实战直播。
    </p>

    <div class="grid-3col">
      <div class="card">
        <div class="card-title">第 1 天 —— 头脑风暴与构想</div>
        <div class="card-body">
          从餐厅快闪策划案，变成快闪服务平台，再变成艺术展览，最后变成周边快闪店。一天之内经历了 4 次业务大转型。软件编写从来不是瓶颈，就“究竟做什么”达成共识才是。
        </div>
      </div>
      <div class="card">
        <div class="card-title">第 2 天 —— 搭建与原型迭代</div>
        <div class="card-body">
          全面转型为游戏工作室。用纯 HTML/CSS/JS 手搓名为“Cupcake”的自动对战简易原型并在直播中试玩 —— 现场暴露了数值属性 Bug，并直接上演了前端调试作弊演示。
        </div>
      </div>
      <div class="card">
        <div class="card-title">第 3 天 —— 正式发布与上线</div>
        <div class="card-body">
          一夜之间，Bot 工厂自动化合入了 170 个 PR。上午 10 点，游戏以 <strong>Thursday Arena</strong> 为名正式上线。截至直播结束：累计合入 433 个 PR，约 30,000 次页面浏览，约 6,000 场对局，营收 $0。
        </div>
      </div>
    </div>

    <div class="grid-4col">
      <div class="stat-card">
        <div class="stat-val">433</div>
        <div class="stat-desc">三天内合并的代码拉取请求 (PR) 总数</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~2,000</div>
        <div class="stat-desc">上线首日登录账户的真实玩家数</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~30k</div>
        <div class="stat-desc">已发布游戏获得的线上总页面浏览量</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">$0</div>
        <div class="stat-desc">商业变现营收 —— 最坦诚的真实数字</div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">为什么一份源于直播的实战指南如此值得阅读？</div>
        <p class="callout-text">
          官方产品文档只会罗列功能是什么。而连续三天未剪辑的高压直播，展示了人们在极限时间压力下<strong>究竟拿它做了什么</strong> —— 哪些模式经受住了火线考验，哪些模式产生了巨额账单，哪些模式在悄无声息中崩溃。本指南沉淀的几乎每一条建议，都是某人被镜头记录下的真实动作，而非某个功能纸面上的美好畅想。
        </p>
      </div>
    </div>

    <div class="footnote">
      *关于名称的说明：自动生成的字幕将产品名称听写为“GrokBot”、“Rockbot”甚至“Brockbot”，将公司听写为“SpaceX AI”。它们都指向同一实体。文中引用的所有数据均为直播时当场披露的真实阶段性数据。
    </div>
    {get_footer(3)}
  </div>
    """

def render_page_04():
    return f"""
  <div class="page" id="page-04">
    {get_header()}
    <div class="eyebrow">02 · MENTAL MODEL</div>
    <h1 class="page-title">队友，而非一次性任务</h1>
    <p class="page-intro">
      产品核心缔造者之一 Roman 在第一天直播开场时，阐述了整个平台赖以立足的核心哲学：<strong>“我们真的希望 Grok Bot 给你的感觉，就像是和你并肩作战的真实同事与团队伙伴。”</strong> 产品界面被刻意设计成类似 iMessage 的聊天形态，正是这种形态驱动了本指南中的所有最佳实践。
    </p>

    <div class="section-label">构建产品所押注的三大基石假设</div>
    <div style="margin-bottom: 11pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>队友范式，而非任务范式。</strong> Bot 是一个有名字的同事，你会连续数月反复找它协作，而不是一个用完即弃的对话窗口。它的认知与上下文会随时间持续复利累积。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>每个 Bot 拥有专属的计算机。</strong> 这是一个配备独立浏览器和终端的 Linux 虚拟机。它能操作遗留内部软件、政府政务门户以及任何没有公开 API 的网站 —— 凡是人类在屏幕前用鼠标键盘能干的，它都能干。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>全天候云端运行。</strong> 合上笔记本电脑，工作依然在进行。“当你休假时它可以工作；当你安然入睡时它依旧在工作。”
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">实操中的思维转变</div>
        <ul class="custom-bullets">
          <li><strong>你是在招聘，而不是在配置。</strong> 定义一个 Bot 的职责范围，更接近于撰写一份岗位职责说明书（Job Description），而非勾选后台设置项。</li>
          <li><strong>纠错会产生复利。</strong> 告诉 Bot 它为什么做错了是一笔高回报投资，而不是一次被动的打断。</li>
          <li><strong>回过头来收获现成成果。</strong> 正如 Amrita 所言：“最爽的时刻莫过于回来看到工作已经被干完了。”</li>
          <li><strong>随时打断完全正常。</strong> 在任务中途纠正并重新引导 Bot 的方向，既常见也值得鼓励。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">底座模型 vs 调度外壳</div>
        <div class="card-body">
          <p>Roshan 明确划定了两者的界限，这对决定把任务派发给谁至关重要：</p>
          <ul class="custom-bullets" style="margin-top: 4pt;">
            <li><strong>Grok</strong> 是底座模型（Model）。</li>
            <li><strong>Grok Bot</strong> 是调度外壳（Harness） —— 刻意保持轻量，擅长多 Agent 编排、工具调用与主观判断。</li>
            <li><strong>Cursor 云端 Agent</strong> 则是重型编码执行外壳 —— 当遇到真正的硬核研发工程时，Bot 会主动将代码编写下放给它。</li>
          </ul>
          <p style="margin-top: 5pt; font-weight: 600; color: #111;">*在 Grok Bot 中做原型验证，通过云端 Agent 实施生产交付。*</p>
        </div>
      </div>
    </div>

    <div class="quote-box">
      <p class="quote-text">“把一件事情做到 90%，和完全撒手让它端到端全自动彻底搞定 —— 两者带来的心理感受是天差地别的，后者充满魔力。”</p>
      <p class="quote-author">Roman · Grok Bot 101, Day 1</p>
    </div>
    {get_footer(4)}
  </div>
    """

def render_page_05():
    return f"""
  <div class="page" id="page-05">
    {get_header()}
    <div class="eyebrow">03 · ARCHITECTURE</div>
    <h1 class="page-title">Bot 真正拥有的资源底座</h1>
    <p class="page-intro">
      清晰了解 Bot 之间<strong>哪些东西是共享的、哪些是严格隔离的</strong>，能解释直播中人们遇到的大多数意料之外的行为 —— 无论好的还是坏的。
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">🖥 专属的独立虚拟机</div>
        <ul class="custom-bullets">
          <li>每个 Bot 独享一个 Linux 虚拟机，预装浏览器、终端和可扩展应用。</li>
          <li>一个 Bot 无法窥探另一个 Bot 的屏幕 —— 这种强隔离性使得两个 Bot 能同时独立编辑同一个 PPT 的不同幻灯片。</li>
          <li>在涉及账号登录、双重验证 (2FA)、人机验证码 (CAPTCHA) 等敏感操作时，人类可随时接管屏幕亲自操作。</li>
          <li>由于虚拟机纯基于 Linux，<strong>不支持 Linux 且无 MCP 的专有工具完全无法调用</strong>（Q&A 环节明确确认）。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">🧠 专属的独立记忆库</div>
        <ul class="custom-bullets">
          <li>Bot 拥有只属于自己的独立持久记忆。它能记住你的个人偏好、工作风格和专属约定。</li>
          <li><strong>关键边界：记忆绝不跨 Bot 共享。</strong> 告诉了 Bot A 的信息，Bot B 浑然不知。</li>
          <li>若要让某个知识对全体 Bot 可见，必须显式写入<strong>共享团队驱动器</strong>（下述）。</li>
          <li>记忆能够被人类直接打开审查、单条编辑或定向清除 —— 这是一处极其关键的安全护栏。</li>
        </ul>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">📁 共享的团队文件驱动器</div>
        <ul class="custom-bullets">
          <li>这是全体 Bot 与人类共同的<strong>唯一事实真相来源 (Single Source of Truth)</strong>。</li>
          <li>存放公共规范：品牌风格指南、团队花名册、各阶段完成定义 (Definition of Done)、共享规则库。</li>
          <li><strong>踩坑红线：如果某份文件必须被所有 Bot 严格遵循，绝不能仅放在某一次对话附件中，必须扔进共享驱动器。</strong></li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">🔌 共享的第三方集成服务</div>
        <ul class="custom-bullets">
          <li>认证一次，全员复用：在团队级完成 Google Workspace、Slack、GitHub、Linear 授权。</li>
          <li>所有配置了对应权限的 Bot，均可直接读写上述第三方服务。</li>
          <li>若某个软件没有现成官方集成？<strong>让 Bot 通过浏览器直接操作 Web 版。</strong></li>
        </ul>
      </div>
    </div>

    <div class="card" style="margin-top: 4pt; padding: 7.5pt 10pt;">
      <div class="card-title">⚡️ 云端与本地混合执行模式</div>
      <div class="card-body">
        工程师们并非完全将代码托管在云端 Bot 虚拟机中跑。通过底层同步工具（如 PStack），他们在<strong>本地终端、本地 Neovim 与云端 Bot 之间保持毫秒级双向热同步</strong>。Bot 在云端运行测试、提交 PR，人类在本地随时查看 Diff 并微调代码 —— 两者无缝融合。
      </div>
    </div>
    {get_footer(5)}
  </div>
    """

def render_page_06():
    return f"""
  <div class="page" id="page-06">
    {get_header()}
    <div class="eyebrow">04 · BUILDING A ROSTER</div>
    <h1 class="page-title">一 Bot 一职</h1>
    <p class="page-intro">
      这是整整三天里，每一位登台演讲的工程师被问及经验时复述次数最多的一条金科玉律：不要试图做一个通晓一切的“全能万应助手”，而是打造一支<strong>每个成员各司其职、直呼其名的专属专家团队名录（Roster）</strong>。
    </p>

    <div class="section-label">为什么单功能专精 Bot 表现远超全能助手？</div>
    <div style="margin-bottom: 10pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>上下文边界保持精炼。</strong> 每个 Bot 的上下文预算是有限的。一个试图同时包揽四项无关任务的全才助手，会极快耗尽上下文并开始健忘与胡言乱语。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>人类大脑能清楚记得该向谁求助。</strong> 研发工程师 Ling Shi 形象地打了个比方：“人类的大脑也记不住长篇小说，但你必须清楚知道需要参考谁的意见。”
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>扮演特定角色时模型表现显著提升。</strong> 当一个 Bot 的任务边界被约束得足够狭窄时，人类纠偏的反馈闭环就会极度紧凑，促使模型输出高质量成果。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>天然获得零成本的并行处理能力。</strong> 同时派出 5 位专家 Bot 各自展开工作，之后统一汇集综合 —— 这与人类团队的“开会派工 → 独立攻关 → 汇总对齐”模式完全一致。
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">一个优秀的角色定义必须讲清的内容</div>
        <ul class="custom-bullets">
          <li>一个清晰单一、能用一句话叫出名字的权责归属。</li>
          <li>明确限定允许调用的工具与数据源。</li>
          <li>解决问题的工作方式与思考原则，而不仅仅是工作产出物。</li>
          <li>哪些高危动作在执行前必须先获得人类审批确认。</li>
          <li>是否配置周期性的定时例行任务（Routine）。</li>
          <li>杜绝泛化的“通用助手”。走向高度专精：<strong>猎头侦察员 (Talent Scout)</strong>、<strong>报销管理员 (Expense Manager)</strong>、<strong>Bug 复现专家 (Bug Reproduction)</strong>。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">如何组织侧边栏管理团队</div>
        <ul class="custom-bullets">
          <li><strong>分组如同画组织架构图</strong>：按职能归集为管理层 (Leadership)、工程组 (Engineering)、作战室 (War Room)。</li>
          <li><strong>标签用于提示专业领域</strong>：一旦你开始用食物或外号来给 Bot 命名，标签能帮你一眼看懂专长。</li>
          <li>Simon 的<strong>职能色标管理法</strong>：调研类用橙色，大客户跟进用绿色，拓客销售用另一色 —— 扫一眼会话列表便知客户处于漏斗的哪一阶段。</li>
          <li>将日常高频使用的三到四个核心 Bot <strong>固定置顶 (Pin)</strong>。</li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">⚠️</div>
      <div class="callout-body">
        <div class="callout-title">警惕 Bot 无序蔓延陷阱 (Bot Sprawl)</div>
        <p class="callout-text">
          在直播中拥有最庞大团队的 Simon 直言不讳：“我向你保证，我曾经建立过太多 Bot。最后局面变得混乱不堪。你必须时刻反问自己：真的有必要为这事专造一个新 Bot 吗？” 团队共识：<strong>克制臃肿，你根本不需要 45 个 Bot</strong>。随意创建 Bot 的快感是廉价且有趣的，正因如此才必须克制。优先考虑为既有专家补充新技能或新例行任务，而不是盲目招聘新 Bot。
        </p>
      </div>
    </div>

    <div class="footnote">
      *命名绝非小事：团队在直播间向观众征集了大量生活化的名字 —— Tater、Whisk、Bake、Crumble、Dr. Eggbot。这显著改变了团队与 Bot 沟通的心理感受：给一个叫 Bake 的 Bot 派活像在托付同事；给“任务3”下指令则像在微观管理。
    </div>
    {get_footer(6)}
  </div>
    """

def render_page_07():
    return f"""
  <div class="page" id="page-07">
    {get_header()}
    <div class="eyebrow">05 · THE META-BOT</div>
    <h1 class="page-title">制造 Bot 的元 Bot</h1>
    <p class="page-intro">
      连续三天里被唤醒调用次数最多的 Bot，既不是工程师也不是市场研究员，而是 <strong>Dr. Eggbot（蛋头博士）</strong> —— 一个全职负责创建、审查、优化其他所有 Bot 的“元 Bot (Meta-bot)”。直播中涌现出的几乎每一个全新团队成员，都诞生于对它下达的一句话指令。
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">元 Bot 的核心日常职责</div>
        <ul class="custom-bullets">
          <li>根据人类的一段大白话需求描述，全自动生成新 Bot。</li>
          <li>自动撰写新 Bot 的<strong>角色描述 (Description)</strong> —— 也就是充当底层系统提示词的灵魂字段。</li>
          <li><strong>主动审计团队名录</strong>：“请审查我们当前的所有 Bot —— 瓶颈在什么环节？职责是否存在冲突？”</li>
          <li>起名字：品味极佳，甚至有两位工程师在不同房间分别提需求时，Eggbot 为它们起的名字英雄所见略同，双双命名为“Ping”。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">角色描述即 Bot 的灵魂</div>
        <div class="card-body">
          <p>“角色描述 (Description)”绝不仅仅是一张外观贴纸。Lauren 强调：<strong>“有人称其为灵魂，或者系统提示词。”</strong> 它从根本上决定了 Bot 的语气声调、判断标准以及向外派工的行为风格。</p>
          <ul class="custom-bullets" style="margin-top: 5pt;">
            <li><strong>写通用原则，不要写偶发事故</strong>（详见下方反思）。</li>
            <li>明确限定它全权负责的边界，以及必须上交确认的红线。</li>
            <li>指名道姓地赋予它唯一认可的“事实标准源”。</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="section-label">真实踩坑：角色过度拟合与现场纠偏</div>
    <div class="card" style="margin-bottom: 10pt;">
      <div class="card-subtitle">DR. EGGBOT 最初为 CUPCAKE ENG 自动生成的角色描述：</div>
      <div class="card-body" style="background:#fff; padding:6pt 9pt; border-radius:5px; margin:4pt 0; border:1px solid #e0deda; font-style:italic;">
        “负责我们游戏工作室的高层上下文。唯一工作：通过 pstack potato mode 和云端 agent 统筹协调各项工作，进而进行监督与验证，以交付工程成果；对照你的剧本并严格执行。”
      </div>
      <div class="card-body" style="font-size:7.8pt; color:#666; margin-bottom:4pt;">
        <strong>Lauren 当场的评判：太过度拟合了。</strong> 这段描述直接把当天的特定工具链、特定故障现场和特定分支写死了，变成了一个不可迁移的永久代码补丁。
      </div>
      <div class="card-subtitle">LAUREN 当场下达的纠偏指令：</div>
      <div class="card-body" style="background:#fff; padding:6pt 9pt; border-radius:5px; margin:4pt 0; border:1px solid #e0deda; font-weight:600; color:#111;">
        “重新阅读 potato mode，提炼出 Cupcake 工程师应当遵循的底层通用原则，而不是硬编码这些过度具体的偶发事故细节。”
      </div>
      <div class="card-body" style="font-size:7.8pt; color:#e4402e; font-weight:600;">
        这是为你编写的每一项技能、每一条规则都必须坚守的核心铁律，绝不仅限于 Bot 描述。
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">💡</div>
      <div class="callout-body">
        <div class="callout-title">只要你开口，Bot 会自己为团队招兵买马</div>
        <p class="callout-text">
          在第 2 天，Amrita 向手下的两位现有 Bot 发问：“根据你们目前手头正在推进的工作，还需要哪些 Bot 才能帮你们把工作做得更好？直接帮我把它们创建出来吧。” 它们随后自动创建了三个专职 Bot —— <strong>Battle Card Blair（竞品攻防）</strong>、<strong>Demo Drake（演示专家）</strong> 与 <strong>AI Radar（雷达侦测）</strong>，每一个都拥有明确的岗位职责和指定的事实来源。主动询问现有团队缺失什么角色，是一种极其高效的高阶手法。
        </p>
      </div>
    </div>

    <div class="footnote">
      *若有现成模板，优先从官方市场导入。官方 Bot 模板沉淀了精良的记忆结构、预置例行任务与集成组件，且在分享导出时会自动剥离私密凭据和敏感聊天历史。团队的建议是：只要官方市场已有类似角色，绝不要从白纸从头搭建。
    </div>
    {get_footer(7)}
  </div>
    """

def render_page_08():
    return f"""
  <div class="page" id="page-08">
    {get_header()}
    <div class="eyebrow">06 · AUTOMATION</div>
    <h1 class="page-title">自动化构件：技能与例行任务</h1>
    <p class="page-intro">
      自动化系统由两大核心基石构成：<strong>技能（Skill）</strong>沉淀“某件事情该如何完成”的确定性操作手法；<strong>例行任务（Routine）</strong>决定“这项工作在何时被触发执行”。直播中所有持久可靠的工作流均严格遵循此序构建，且在人工手动完整走通至少一次之前，绝不提前固化为自动化。
    </p>

    <div class="flow-row">
      <div class="flow-step">1. 人类手动走通</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">2. 获得稳定可重复的结果</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">3. 沉淀固化为技能 (Skill)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">4. 挂载定时/事件任务 (Routine)</div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">打造一项技能的三种途径</div>
        <ul class="custom-bullets">
          <li><strong>动作示范 (Demonstration)</strong>：点击“示教任务”，亲自在屏幕上操作演练一遍，Bot 即可把你的操作录像转化为一项可复用的技能。直播中曾现场示教制作幻灯片动效与竞品博客监控。</li>
          <li><strong>日常纠偏沉淀 (Correction)</strong>：最具长期复利价值的途径 —— 详见下方黄金法则。</li>
          <li><strong>人工手写代码规则 (Writing)</strong>：当工作流包含分支判断逻辑、容错兜底或人工审批门禁时，单凭一次示范不足以让 Bot 穷尽各种边界分支，此时需要人工编写固化。</li>
          <li><strong>技能全局共享</strong>：任何一个 Bot 学会的技能，团队内所有其他 Bot 立即原生可用。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">一个例行任务必须明确定义的要素</div>
        <ul class="custom-bullets">
          <li>由哪一个具体的专家 Bot 归口负责。</li>
          <li>触发时间周期与时区 —— 或者是某个 Webhook/事件触发源。</li>
          <li>数据输入的权威获取源头。</li>
          <li>期望交付的标准输出物结构格式。</li>
          <li>人工审批的边界范围。</li>
          <li>当遭遇突发异常或外部失败时的回滚与告警预案。</li>
          <li><strong>空操作时的静默机制</strong>：明确告诫 Bot，当检查完毕发现没有任何新情况需要汇报时，必须保持彻底安静（Stay quiet on a no-op）。</li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">沉淀纠偏原则，绝不要记录个别故事</div>
        <p class="callout-text">
          Roshan 的法则是：“一旦看到 Agent 思考方向发生了偏差，这就是为其量身打造一项技能来根治问题的绝佳契机” —— 而不是在对话框里临时多打几行字绕过去。Ling Shi 的比喻更狠：“宁可深入一层修水管，也不要只擦水槽里的积水。” 但这很容易走向另一个陷阱：<strong>Agent 往往习惯性地把今天踩坑的所有偶发细节全写进规则，导致该技能极度过度拟合</strong>，下次毫无通用价值。必须做到：<strong>提炼底层通用原则，坚决删除偶发故事</strong>。
        </p>
      </div>
    </div>

    <div class="footnote">
      *例行任务的执行频次往往是巨额账单悄悄滋生的地方（详见第 12 章）。能用事件驱动触发的，绝不用定时轮询；能在每天早晚跑一两次的，绝不要设置成每 15 分钟轮询一次。
    </div>
    {get_footer(8)}
  </div>
    """
