# -*- coding: utf-8 -*-
# Pages 9 to 16 for Chinese Grok Bot Guide
from pages_part1 import get_header, get_footer

def render_page_09():
    return f"""
  <div class="page" id="page-09">
    {get_header()}
    <div class="eyebrow">07 · THE SOFTWARE FACTORY</div>
    <h1 class="page-title">433 个 PR 是如何自动合并的</h1>
    <p class="page-intro">
      “软件工厂 (Software Factory)”正是创造这一惊人数字的核心工程模式。开发团队其实并不喜欢这个词（“我其实真不太喜欢工厂这个叫法”），但这个名字最终深入人心。剥去所有的品牌宣传外衣，它本质上是一个严密的闭环：<strong>编写者 Agent 提交细粒度的小改动，验证者 Agent 实际运行应用并尝试破坏它，唯有验证通过的代码才被允许合入</strong>。
    </p>

    <div class="section-label">流水线闭环运作五步法</div>
    <div style="margin-bottom: 10pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>宏大方案拆解为细分阶段。</strong> 由 Lauren 编写的 Pstack 插件及其“Potato Mode”技能全自动完成：只需下达指令 <code>/potato mode</code> 加上 <code>full autopilot this plan</code>。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>编写者 Agent 提交小颗粒度 PR。</strong> 调动 Cursor 云端 Agent，每一个细小关注点各分配一个 Agent，在各自的独立云端机器上并行编码。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>验证者 Agent 真机运行并进行模糊破坏测试。</strong> “Swarm (蜂群)”技能会唤起一整支 Agent 舰队，直接在运行中的产品界面上四处点击挖掘 Bug。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>自动化验证全绿即自动合并 (Auto-merge on green)。</strong> 验证通过是唯一的合入门禁 —— 而不是让人类肉眼去通读庞大的 Diff。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">5</div>
        <div class="num-content">
          <strong>试玩 Bot 端到端完整打通游戏。</strong> 专门的试玩 Bot “Chrome”监控 CI 通过的 PR，并在真正合入前在真机浏览器中完整试玩一局。
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">自主权阶梯 (Autopilot Ladder)</div>
        <ul class="custom-bullets">
          <li><strong>仅限调查 (Investigate only)</strong> —— “先不要提 PR，查清楚你认为的原因再来向我汇报。”</li>
          <li><strong>草稿模式 (Draft)</strong> —— 提交 PR，等待人类审查确认。</li>
          <li><strong>自动驾驶 (Autopilot)</strong> —— 自主实现并验证，测试全绿自动合并。</li>
          <li><strong>完全自动驾驶 (Full autopilot)</strong> —— 规划、拆相、编码、验证、合并端到端全自动。</li>
          <li>一旦正式上线生产环境，Lauren 便审慎下调了一个档位：“也许不要开完全自动驾驶 —— 我们真的敢吗？”</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">架构师环节 (The Architect step)</div>
        <div class="card-body">
          <p>Pstack 的“架构师 (Architect)”技能会将同一个技术难题<strong>同时并行抛给 4 个不同的顶级模型</strong>，随后由评审裁决环节合并或选出最优架构方案。</p>
          <p style="margin-top: 5pt;">对于重大技术选型，这非常值得，因为不同模型会发现不同的边界约束。但在初期手搓极简原型阶段，团队果断跳过了它：“在这个节点我其实根本不在乎架构规范，好玩才是唯一的指标。”</p>
        </div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">⚠️</div>
      <div class="callout-body">
        <div class="callout-title">必须坦白的事实与警告</div>
        <p class="callout-text">
          Lauren 在谈到这款游戏时坦言：“说实话，我压根没有逐行看代码。我就是纯靠 Potato 模式和 Pstack 自动流转。” 但负责 Grok Bot 正式商业产品的核心架构师 Eric 同样立场鲜明地指出，<strong>他在真实的生产核心代码库中绝不会这样撒手不管</strong> —— 他会细致审阅每一个 PR 并严格执行反模式检查。软件工厂的激进程度必须与<strong>爆炸半径 (Blast Radius)</strong> 严格匹配，而一个 72 小时限时试玩的小游戏，其爆炸半径几乎低到了极限。
        </p>
      </div>
    </div>
    {get_footer(9)}
  </div>
    """

def render_page_10():
    return f"""
  <div class="page" id="page-10">
    {get_header()}
    <div class="eyebrow">08 · VERIFICATION</div>
    <h1 class="page-title">确定性验证胜于一切</h1>
    <p class="page-intro">
      如果这整整三天的实战记录中你只打算吸收一条构建指令，请务必牢记这一条。每一位真正用 Bot 成功交付了严肃产品的工程师都以不同形式强调了它；而那些尚未构建验证闭环的团队，无一例外陷入了低效拉锯的巨大泥潭。
    </p>

    <div class="quote-box">
      <p class="quote-text">“验证机制是重中之重。你必须让 Bot 真正把代码运行起来、去截屏留存证据。唯有亲眼看到运行证据，你才能拥有坚实的信心确定它真的理解了问题。”</p>
      <p class="quote-author">Lauren · Day 3</p>
    </div>

    <div class="section-label">一套合格的验证技能 (Verification Skill) 究竟包含什么？</div>
    <div class="grid-2col">
      <div class="card">
        <div class="card-title">🖥 Agent 可操纵的确定性 CLI</div>
        <div class="card-body">
          绝不要让 Agent 每次临时手写即兴测试脚本 —— 那既浪费大量 Token 且无法复现。Lauren：“你必须提供一个 CLI、标准脚本或测试套件，让 Bot 能以稳定、确定性的方式与应用交互。我宁可直接塞给它一套标准的成熟工具。”
        </div>
      </div>
      <div class="card">
        <div class="card-title">🗺 机器可读的功能地图 (Feature Map)</div>
        <div class="card-body">
          一份结构化的功能与页面路径映射表，使 Agent 无需在应用里盲猜即可直达要测试的界面。Thursday Arena 甚至更进一步，上线了一个 <code>/rules</code> 页面并提供类似 <code>llms.txt</code> 的接口，供 Agent 随时读取游戏的底层规则。
        </div>
      </div>
    </div>

    <div class="section-label">团队在实战中铁腕执行的三大铁律</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>先精准复现，再动手修复。</strong> “唯有当 Agent 能在真机上精准复现 Bug 时，我们才能信任它真正理解了问题所在。” 团队的常驻提示词：“在写任何代码前，先运行应用，找到确切的 Bug 和确切的表现，然后再开始。”
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>提交 PR 必须附带证据。</strong> 剧本中的明文规定：UI 界面更改必须附带截图或视频录屏；后端更改必须附带性能对比数据。云端 Agent 能够自动录制自身的测试运行视频并直接插入 PR。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>指名道姓命名技能，并用其名字调用。</strong> 团队的验证技能名为 <code>/verify cupcake</code>，在游戏上线生产后，所有的自动驾驶指令都强制将其列为不可协商的必跑条件。
        </div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">普适判别法则：什么样的任务才适合全自动化？</div>
        <p class="callout-text">
          Eric 给出的决定是否自动化的黄金准则：“审视你的工作流并反问：<strong>这里是否存在一个能够闭环验证的确定性反馈回路？如果有，那就是你可以放手让 Bot 尽情施展的地方。</strong>” 代码编写之所以是最佳试点，正是因为单元测试、编译构建和真机运行能提供确凿的机器可读信号。任何缺乏此类信号的流程，在赋予自主权之前，必须先发明出这种确定性信号。
        </p>
      </div>
    </div>

    <div class="footnote">
      *缺乏验证技能的典型翻车表现大家再熟悉不过：Bot 干完活后两手一摊对你说：“好了，你现在可以把应用跑起来，在界面上到处点一点，然后告诉我行不行。” 这种来回人工试错才是吞噬所有时间与精力的黑洞。
    </div>
    {get_footer(10)}
  </div>
    """

def render_page_11():
    return f"""
  <div class="page" id="page-11">
    {get_header()}
    <div class="eyebrow">09 · PROMPT PATTERNS</div>
    <h1 class="page-title">经受住实战检验的 7 大 Prompt 招式</h1>
    <p class="page-intro">
      这里没有华而不实的提示词奇淫巧技，而是在整整三天里，六七位不同的工程师在各自独立的操作中，不约而同反复高频使用的核心肌肉记忆。
    </p>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">1 · 用自己的话重述 (Restate it back)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">全体工程师必备</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        在一长串复杂或多阶段的指令末尾加上：“在开始前，先用你自己的话把任务重述一遍”。在开始烧钱之前把误解掐灭在萌芽状态。第 2 天被誉为“全场我最喜欢的模式”。
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">2 · 随意倾诉，再行结构化 (Yap, then structure)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">语音转录实录</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        按住麦克风，以意识流的方式畅所欲言一两分钟，然后要求 Bot 将其整理提炼。想法在口述的当下就被完整捕捉，无需事后痛苦敲键盘 —— 团队在对话中实时用这种方式记录了大量业务灵感。
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">3 · 先提炼事实，再展开推理 (Distill, then reason)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">应对海量输入</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        面对冗长的口述转录或大型文档，要求 Bot 首先提取核心事实清单，然后<strong>仅基于这份提炼后的清单展开逻辑推理</strong>。这是 Blake 解决长篇输入下幻觉胡言乱语的克星。
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">4 · 交付物先行 (Outcome first)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">Amrita 的实操习惯</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        开门见山说明：“这就是我最终想要拿到的产出物”，然后让 Bot 自行逆向拆解步骤。直接声明交付物形态和验收标准，远比手把手指导执行步骤有效得多。
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">5 · 动手改之前先彻底调查 (Investigate before you touch)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">Roshan 的生产原则</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        面对任何线上生产环境问题：“深入排查，弄清楚到底发生了什么。<strong>先不要提 PR。</strong> 查清楚你认为的原因后再回来向我汇报。” 严禁未探明根因擅自改动代码。
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">6 · 实时打断与微调纠偏 (Interrupt and nudge)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">Ling Shi 的调度心得</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        密切注视 Bot 偏离轨道并在中途果断拉回，是正常的操作流程，绝非失败。每隔几分钟要一次状态更新，远胜于在死寂中空等 —— 这也是当场抓获某个决定 <code>sleep 300</code> 偷懒 Agent 的关键。
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding: 7pt 10pt;">
      <div style="display:flex; justify-content:space-between; align-items:baseline;">
        <span style="font-weight:700; color:#111; font-size:8.6pt;">7 · 语音大倾倒入职法 (The voice dump)</span>
        <span style="font-size:7.4pt; color:#e4402e; font-weight:600;">Blake 用于新人 Bot 入职</span>
      </div>
      <div style="font-size:7.9pt; color:#333; line-height:1.4; margin-top:2pt;">
        录制一段 10~15 分钟的语音备忘录：我是谁、我的岗位是什么、目前的痛点是什么、哪些流程该自动化。把转录文本丢给你的第一个 Bot：“为我设计一套行之有效的自动化体系”，让它反向提议系统框架。
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">💡</div>
      <div class="callout-body">
        <div class="callout-title">贯穿这七大习惯背后的唯一底层心智</div>
        <p class="callout-text">
          上述每一个模式，本质上都是<strong>在 Bot 真正消耗你的资金与 Token 之前，逼它证明自己已经完全理解了意图</strong>。这与你在真实职场中对待一个刚入职第一周的有能力的新员工的心理防线别无二致 —— 这一对应绝非巧合，因为整套产品正是构建在这一隐喻之上。
        </p>
      </div>
    </div>
    {get_footer(11)}
  </div>
    """

def render_page_12():
    return f"""
  <div class="page" id="page-12">
    {get_header()}
    <div class="eyebrow">10 · PROMPT LIBRARY</div>
    <h1 class="page-title">原汁原味实战 Prompt 库</h1>
    <p class="page-intro">
      从直播实战中近乎原封不动摘录的真实提示词。这些 Prompt 的结构本身就是最生动的教材：<strong>目标产出物、明确约束、权威事实源，以及任务完成后的闭环动作</strong>。
    </p>

    <div class="prompt-card">
      <div class="prompt-label">创建幕僚长 (CHIEF OF STAFF)</div>
      <div class="prompt-content">
        “你的工作是向 Email Ethan、Slide Sonia 和 Data Dan 获取他们手头工作的最新进展汇报。”
      </div>
      <div class="prompt-meta">
        紧接着挂载例行任务：“每两小时，我需要你向你的团队主动索取工作进展，并排查当前是否存在任何阻塞项 (Blockers)。”
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">保持静默的知识库 BOT (STAYS QUIET)</div>
      <div class="prompt-content">
        “这个 Bot 的工作是静默旁观我与其他所有 Bot 之间的对话，但在被明确点名 @ 之前，绝不要采取任何行动。你应当静静等待消息主动发给你。我们需要极其克制、有选择地更新 Notion。我们绝不希望把所有垃圾信息一股脑全倒进文档库里。所以在同步之前，务必先向我请示确认。”
      </div>
      <div class="prompt-meta">
        Roshan。克制性声明是整个提示词的灵魂所在。在其他会话中被总结为“像对待 git commit log 一样严肃对待沉淀”。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">常驻 P0 巡检巡警，一次配齐免于日常怒吼 (STANDING P0 POLICY)</div>
      <div class="prompt-content">
        “建立一个每 5 分钟检查一次云端 Agent 的例行任务。检查它们是否偏离了轨道 —— 比如正在执行长达 300 秒的休眠（如 sleep 300），或者脱离了我们的目标，或者行事过于保守裹足不前。一旦发现它们偏离，立即予以打断并现场微调拉回。”
      </div>
      <div class="prompt-meta">
        Ling Shi。核心洞察：反复在对话框里对 Agent 咆哮“这很紧急”只会诱使它跳过验证去瞎猜；确立制度化的巡检策略才起效。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">审慎处理线上生产环境 BUG (PRODUCTION BUG)</div>
      <div class="prompt-content">
        “我怀疑我们的 ELO 匹配机制出现了故障。每次我在 ThursdayArena.com 上玩游戏，匹配到的全都是 AI 对手而非真实玩家的阵容，但排行榜上的 ELO 积分却在大幅变动。你能不能深入排查一下，彻底搞清楚到底怎么回事？使用 potato mode，并派出 Cursor 云端 Agent 去调查。先不要开 PR，查清楚你认为的根因后直接回来向我汇报。”
      </div>
      <div class="prompt-meta">
        Roshan。症状描述、可验证证据、指定工具，并在改动任何代码前明确设立硬性停止点。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">搭建用户反馈流水线 —— 包含安全防护条款 (FEEDBACK PIPELINE)</div>
      <div class="prompt-content">
        “上面的链接是我们接收用户反馈的 Slack 频道。我想搭建一套工厂流水线：查阅反馈、进行分类定级、尝试重现该问题，然后将确认的 Bug 录入我们的 Notion 数据库。非常重要的是，如果我们用 AI 来审查这些反馈，你必须明确警告你的 AI 严密防范提示词注入 (Prompt Injections) 攻击。……用你自己的话把刚才这番要求复述一遍。”
      </div>
      <div class="prompt-meta">
        Lauren。来自不可信外部用户的输入均视为恶意攻击面；在构建流程的一开始就把防御写入 Prompt。
      </div>
    </div>
    {get_footer(12)}
  </div>
    """

def render_page_13():
    return f"""
  <div class="page" id="page-13">
    {get_header()}
    <div class="eyebrow">10 · PROMPT LIBRARY, CONTINUED</div>
    <h1 class="page-title">研发、调研与商业化实操 Prompt</h1>

    <div class="prompt-card">
      <div class="prompt-label">创建前端极速原型专家 (PROTOTYPING SPECIALIST)</div>
      <div class="prompt-content">
        “我们想针对 Cupcake 代码库中现有的客户端，做更多前端探索。你能不能孵化出一个专职 Bot，专门负责快速原型验证：探索如何在保持极度轻量化的前提下加入更多 3D 动画？这个 Bot 必须能够驱使 Cursor 云端 Agent 来交付成果。我非常希望利用 potato mode，在一个接一个的前端原型试验上启动 Agent 蜂群 (Swarm) 进行攻坚。”
      </div>
      <div class="prompt-meta">
        Lauren 对 Dr. Eggbot 下达的指令。注意它明确指出了核心约束（“保持极度轻量化”）与执行载体，而不是直接给死具体输出物。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">限定具体交付物的竞品调研 (COMPETITIVE RESEARCH)</div>
      <div class="prompt-content">
        “帮我把旧金山所有顶尖的餐厅主理人拉出来，挑出其中做得最好的 5 家网站；接着从它们的网站里找出 5 个做得最好的快闪专页；随后找出过去 6 到 12 个月内，在任何主流大都市举办过的 5 个最优秀的快闪餐厅案例。最后，把所有这些调研成果系统整理成一份文档交付给我。”
      </div>
      <div class="prompt-meta">
        Cody Sanchez。层层链式递进，每一步收窄范围，并在末端指名道姓要求交付特定形态的文档。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">产出鲜明战略站位的市场调研 (MARKET RESEARCH)</div>
      <div class="prompt-content">
        “仔细研读目标网站，深入理解该产品是什么、我们处于什么细分市场。现在去执行竞品分析：精准识别并深刻剖析我们的竞争对手，研究他们的营销官网，理解他们的市场定位 —— 最重要的是，指出我们具有哪些战略机会窗口，能与他们形成具有杀伤力的差异化竞争定位。”
      </div>
      <div class="prompt-meta">
        Josh Kim。正是最后那句寻找差异化切入点的话，把一份平庸的信息罗列变成了可执行的商业武器。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">通过指名技能向蜂群下发拓客任务 (DELEGATING TO A SWARM)</div>
      <div class="prompt-content">
        “帮我们寻找目标客户画像 (ICP)，确定这些广告位该卖给谁。你拥有一个名为 FindMyICP 的专有技能。……把我们敲定的目标用户画像输入给 Clay MCP，检索其企业与人员数据库，告诉我们世界上哪些公司符合这个画像 —— 具体交付一份包含 10 家目标企业的清单。”
      </div>
      <div class="prompt-meta">
        指名道姓调用技能、指定外部连接器、限定收敛的产出物规模。
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">永久固化记忆偏好 (STEERING MEMORY)</div>
      <div class="prompt-content">
        “我希望你记住，今后在任何场合称呼我时，绝不要同时使用我的姓和名。只准直呼我的名字 (First name)。”
      </div>
      <div class="prompt-meta">
        Amrita。只需说一遍，便被永久铭刻进该 Bot 的独立长期记忆中，往后所有会话永远生效。
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">贯穿所有高质量 Prompt 的共同范式：明确钦定权威事实源</div>
        <p class="callout-text">
          在一名专职 Bot 的系统设定中直接明文写着：“一切主张均以 Sherlock 为权威事实依据 (Ground every claim in Sherlock)”。当细分领域的专家 Bot 被明确告知团队中哪一位同事的判断拥有最终权威时，AI 之间的胡思乱想与幻觉便有了终结与核实之所。
        </p>
      </div>
    </div>
    {get_footer(13)}
  </div>
    """

def render_page_14():
    return f"""
  <div class="page" id="page-14">
    {get_header()}
    <div class="eyebrow">11 · ORCHESTRATION</div>
    <h1 class="page-title">管理团队，而非操作工具</h1>
    <p class="page-intro">
      一旦你的 Bot 数量突破大约 5 个，你亲自充当每个消息的二传手和路由器就会迅速演变成整个系统的致命瓶颈。为突破这一上限，直播中反复验证了 4 套规模化编排模式。
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">1 · 幕僚长模式 (The Chief of Staff)</div>
        <ul class="custom-bullets">
          <li>你几乎只与这一个总管 Bot 对话；由它向下派发给具体专家，并汇总成果向你汇报。</li>
          <li>它亲自负责新 Bot 的入职培训 —— 将上下文和团队剧本同步过去，人类无需喋喋不休。</li>
          <li>Simon 的铁律：团队里的其他所有 Bot 都要通过幕僚长来创建，这样它才能对每个专家的职责了如指掌。</li>
          <li>Blake 在一个幕僚长麾下直管 15~20 个细分专家，不设任何中层管理。</li>
          <li>并非绝对准则 —— Shub 则明确表示自己更偏爱直接与垂类专家对话。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">2 · 剧本全员广播 (Playbook Broadcast)</div>
        <ul class="custom-bullets">
          <li>由一个专属 Bot 总揽维护一份动态演进的“团队工作标准剧本”（通常存放于 Notion）。</li>
          <li>每次有了新的工程规范或业务规则，只需告诉它一次，由它向下广播给所有人。</li>
          <li>“你只需思考一次该怎么做……全体工程师 Bot 就会自发同步遵守，无需你逐个敲门通知。”</li>
          <li>规范示例：所有 UI PR 必须附带截图，所有后端 PR 必须附带基准性能对比。</li>
        </ul>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">3 · 跨角色决策例会 (The Staff Meeting)</div>
        <ul class="custom-bullets">
          <li>把几个不同角色的 Bot 拉进同一个会话群组，针对重大决策从不同立场展开辩论。</li>
          <li>Blake 甚至特意给手下 Bot 下达指令：<strong>必须提出反对意见</strong> —— “如果大家全是一团和气举手赞同，那开会毫无意义。”</li>
          <li>由幕僚长负责综合各方激辩，并形成最终的决策建议书汇报给人类。</li>
          <li><strong>严厉警告</strong>：群聊非常啰嗦、兴奋且极其烧 Token。仅用于重大决策，绝不可用于日常例行公事。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">4 · 子 Bot 游击军团 (The Sub-bot Army)</div>
        <ul class="custom-bullets">
          <li>由一个中层 Bot 将海量的大规模批处理任务，下发给一整群低上下文预算的基层“工兵”。</li>
          <li>Simon 麾下的“工兵 (Soldiers)”在一个共享群组中，以高度并行的方式同时调研 100~200 个目标企业账号。</li>
          <li>弹性极强，按需随时唤起与销毁；所有产出流回父级 Bot 接受统一审计。</li>
          <li>形态上与研发团队的“蜂群 (Swarm)”完全同构 —— 一个指挥官，带领大量一次性轻量执行者。</li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">💡</div>
      <div class="callout-body">
        <div class="callout-title">全场无人彻底解决的真实现实困境</div>
        <p class="callout-text">
          知名科技播客主 Matthew Berman 被问及同时调度如此多并行 Agent 是什么感觉时坦白：“<strong>我产出的成果比以往任何时候都要多，但同时，我也比以往任何时候都更加忙碌。</strong>” 在十几个飞速运转的 Agent 之间频繁来回切换上下文，是一项极其真实且目前在交互设计上尚未彻底解决的认知开销。幕僚长模式是目前能拿出的最佳对策，但也仅能起到缓解作用，而非终极解药。
        </p>
      </div>
    </div>
    {get_footer(14)}
  </div>
    """

def render_page_15():
    return f"""
  <div class="page" id="page-15">
    {get_header()}
    <div class="eyebrow">12 · ECONOMICS</div>
    <h1 class="page-title">真实成本与经济学核算</h1>
    <p class="page-intro">
      产品计费完全基于实际资源消耗：你只需为同 Bot 对话消耗的 Token，以及 Bot 虚拟机自身运行的屏幕交互算力买单。以下是直播中披露的真实账单数据，以及现场抓获的 4 大资金暗中流失黑洞。
    </p>

    <div class="grid-4col">
      <div class="stat-card">
        <div class="stat-val">$20–30</div>
        <div class="stat-desc">制作一份完整的销售客户案例 PPT 幻灯片 —— 相当于人工 4~5 小时的纯体力劳动</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">$1–2</div>
        <div class="stat-desc">端到端全自动彻底解决一个中等复杂度的客户支持工单</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">$0.20</div>
        <div class="stat-desc">将低复杂度简单工单分类归集并进行批处理时，单张工单的极致成本</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~$1,000</div>
        <div class="stat-desc">单个 Bot 在人类投入 60 秒注意力的前提下，为企业挖掘并节省出的年度公用事业费用</div>
      </div>
    </div>

    <div class="section-label">资金暗中蒸发的四大黑洞</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>设置过频的定时例行任务 (Routines)。</strong> 绝对是产生惊人账单的第一大元凶。“如果你有 3 个例行任务每 15 分钟轮询一次，一天就是数百次高频调用。” 必须严肃审计频次；优先拥抱 Webhook 事件驱动；对于绝大多数日常场景，每天运行一到两次足够应付。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>明有官方 API 却硬用浏览器模拟点击。</strong> 通过 Computer Use 操作网页表单所消耗的视觉算力，远贵于直接调用 API 接口。Shub 的偷师绝技：让 Bot 第一次在浏览器里点一遍，命令它审查刚才触发的网络请求 (Network Requests)，随后命令它往后直接对这些 API 端点发网络请求。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>群聊放在后台未关闭。</strong> 多 Agent 群聊极其兴奋，Bot 们会互相接话争吵，瞬间卷走大笔开销。日常办公请坚持单对单指定点名。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>Bot 队伍过度膨胀。</strong> 每多造一个 Bot，就意味着更多重复建立的上下文、更多并行的定时任务、更多重叠的认知消耗。精简的团队才是廉价高效的团队。
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">你能直接掌控的降本杠杆</div>
        <ul class="custom-bullets">
          <li><strong>调低 Bot 的吐字啰嗦程度 (Verbosity)</strong>：沟通风格直接决定 Token 消耗。</li>
          <li>命令 Bot 及时忘掉不再相关的陈旧上下文。</li>
          <li>直接向 Grok Bot 提问，让它为你的系统架构提供降本优化方案。</li>
          <li>专设一个审计 Bot，唯一职责就是定期排查其他 Bot 的例行任务与技能效率。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">你无法调节的不可控项</div>
        <div class="card-body">
          <p>Computer Use（屏幕视觉识别与鼠标模拟）本身的底层虚拟机算力单价对用户是不可调的。</p>
          <p style="margin-top: 5pt;">唯一降低这部分开销的途径就是<strong>减少对它的依赖</strong>：只要存在 MCP 就立刻接入，唯有没有任何 API 能触达的蛮荒之地，才允许退守至浏览器视觉模拟。</p>
        </div>
      </div>
    </div>
    {get_footer(15)}
  </div>
    """

def render_page_16():
    return f"""
  <div class="page" id="page-16">
    {get_header()}
    <div class="eyebrow">13 · APPROVALS AND BLAST RADIUS</div>
    <h1 class="page-title">带有刹车的自主权</h1>
    <p class="page-intro">
      Matthew 的定性最为精辟通透：<strong>“信任你的 Bot，赋予它们充分的自主权；但同时，牢牢立好防护栏 —— 确保无论它们跑得多么欢快，在真正交付上线任何东西之前，必须回到你面前请示批准，这样局面就绝不会失控。”</strong>
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">🛡 自动审查与硬性防线</div>
        <ul class="custom-bullets">
          <li>系统内置的意图风险分类器会自动裁决动作危险度，并在必要时打断请示。</li>
          <li>你可以在其上追加确定性白纸黑字红线：“严禁未经我人工批准擅自向外发邮件”，“创建 PPT 幻灯片无需请示我可直接执行”。</li>
          <li>针对具体操作类型的开关 —— 例如部署到生产环境必须一律预先弹窗请示。</li>
          <li>宁可过分谨慎：在直播中，一个负责开发表单的 Bot 在动工前，甚至主动停下来向人类确认该表单是否涉及收集敏感用户个人身份信息 (PII)。</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">🔑 机密凭据管理机制</div>
        <ul class="custom-bullets">
          <li>密码与私钥必须通过专有加密安全表单存入安全金库 (Vault) —— Agent 本身绝不可窥视到明文密码。</li>
          <li>活动中途上线了 1Password 集成；Bot 可以直接通过密码库完成二次安全认证。</li>
          <li>对外分享导出的团队模板只包含记忆、配置、技能与例行任务 —— 凭据与聊天记录会被自动剔除。</li>
          <li>对于极度敏感、无论如何都不愿假手于 AI 的顶级鉴权，请人类直接接管屏幕手动输入。</li>
        </ul>
      </div>
    </div>

    <div class="section-label">直播火线中付出惨痛代价学到的三大教训</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>任何涉及竞争与信任的逻辑必须由服务端权威判定。</strong> 由于游戏逻辑起初跑在前端客户端，Matt 在直播众目睽睽之下直接按 F12 打开开发者工具，在 Console 里现场篡改数值作弊。通过 Feature Flag 隐藏调试 UI 毫无安全可言 —— 有心之人瞬间就能翻出来。这段作弊代码在前端必须彻底物理拔除。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>用户提交的文本是巨大的恶意攻击面。</strong> 上线后的反馈流水线紧急追加了全套防御：前端字数截断、服务端敏感词过滤、入库数据转义净化、模型层安全内容护栏、API 限流 —— 以及在分流 Bot 提示词中严厉告诫其防范 Prompt 注入。
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>全自动修复会导致生产环境瞬间崩溃。</strong> 它真的发生了：软件工厂自动化提交的一条劣质 SQL 查询，直接把刚上线的线上游戏打崩停摆，而当时团队甚至正在镜头前探讨“克制”。所幸几分钟内迅速抢修完毕 —— 但这是必须在<strong>数据库迁移和线上生产部署前保留人类最后把关</strong>的铁证。
        </div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">培养一个新 Bot 的“爬-走-跑”三级渐进法</div>
        <p class="callout-text">
          David 在客户支持场景中验证的递进法则适用于几乎所有领域：<strong>第一步（爬）</strong>：Bot 仅拥有只读权限，只负责查阅并提炼摘要；<strong>第二步（走）</strong>：允许其在内部系统撰写回复草稿，供人类审核；<strong>第三步（跑）</strong>：唯有信任完全确立后，才放开权限让其直接发送与执行 —— 即使到了这一步，对于修改面向客户的知识库这种具有超大爆炸半径的高危动作，依然保留人工最终确认。“从小处着手。努力让 Bot 融入你现有的工作节奏，而不是强行颠倒过来。”
        </p>
      </div>
    </div>
    {get_footer(16)}
  </div>
    """
