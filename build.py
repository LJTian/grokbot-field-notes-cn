#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for Grok Bot Field Notes (Chinese Edition)
Generates:
  1. guide/grok-bot-guide-cn.html
  2. public/index.html (Cloudflare Pages responsive web reader)
  3. Copies PDF & images to public/ directory
"""

import os
import shutil
import re
import sys

# Add guide directory to path so we can import generator modules
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GUIDE_DIR = os.path.join(ROOT_DIR, "guide")
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
sys.path.insert(0, GUIDE_DIR)

from generate_guide_cn import generate_html

def build():
    print("=== 1. Generating guide/grok-bot-guide-cn.html ===")
    guide_html = generate_html()
    guide_html_path = os.path.join(GUIDE_DIR, "grok-bot-guide-cn.html")
    with open(guide_html_path, "w", encoding="utf-8") as f:
        f.write(guide_html)
    print(f"Generated {guide_html_path} ({len(guide_html)} bytes)")

    print("\n=== 2. Setting up public/ directory ===")
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    # Copy images
    for img_name in ["cover.png", "cover-people.png"]:
        src = os.path.join(GUIDE_DIR, img_name)
        dst = os.path.join(PUBLIC_DIR, img_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {img_name} -> public/")

    # Copy PDFs
    for pdf_name in [
        "grok-bot-guide-by-spacex-engineers-cn.pdf",
        "grok-bot-guide-by-spacex-engineers.pdf"
    ]:
        src = os.path.join(GUIDE_DIR, pdf_name)
        dst = os.path.join(PUBLIC_DIR, pdf_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {pdf_name} -> public/ ({os.path.getsize(dst)} bytes)")

    print("\n=== 3. Building public/index.html (Interactive Web Reader) ===")
    
    # Custom Web Reader Header / Nav Bar & Controls
    web_nav_html = """
<header class="app-nav no-print">
  <div class="nav-left">
    <span class="nav-dot"></span>
    <span class="nav-logo">GROK BOT</span>
    <span class="nav-badge">中文实战指南</span>
    <span class="nav-sub">72小时现场直播构建 · 24页全景复盘</span>
  </div>
  <div class="nav-actions">
    <div class="chapter-dropdown">
      <select id="chapter-select" onchange="jumpToChapter(this.value)">
        <option value="">📑 快速跳转章节 (01~20)...</option>
        <option value="page-01">封面 · SpaceX 工程师 Grok Bot 实战指南</option>
        <option value="page-02">目录 · 指南核心全景与章节清单</option>
        <option value="page-03">01 · 实战实验：三天，一家公司，全程直播</option>
        <option value="page-04">02 · 心智模型：队友，而非一次性任务</option>
        <option value="page-05">03 · 架构底座：Bot 真正拥有的资源底座</option>
        <option value="page-06">04 · 团队名录：一 Bot 一职与侧边栏管理</option>
        <option value="page-07">05 · 元 Bot：制造 Bot 的元 Bot (Dr. Eggbot)</option>
        <option value="page-08">06 · 自动化：技能 (Skill) 与例行任务 (Routine)</option>
        <option value="page-09">07 · 软件工厂：433 个 PR 是如何自动合并的</option>
        <option value="page-10">08 · 确定性验证：验证机制胜于一切</option>
        <option value="page-11">09 · Prompt 招式：经受住检验的 7 大肌肉记忆</option>
        <option value="page-12">10 · Prompt 库（上）：原生提示词现场采撷</option>
        <option value="page-13">10 · Prompt 库（下）：研发调研与商业化实操</option>
        <option value="page-14">11 · 规模编排：管理团队而非操作工具</option>
        <option value="page-15">12 · 经济学核算：真实成本与 4 大资金暗坑</option>
        <option value="page-16">13 · 权限护栏：带有刹车的自主权与爆炸半径</option>
        <option value="page-17">14 · 案例复盘：72 小时从零打造 Thursday Arena</option>
        <option value="page-18">15 · 团队名录：工厂团队全员花名册</option>
        <option value="page-19">16 · 一线名录（上）：售后实施与市场营销</option>
        <option value="page-20">16 · 一线名录（下）：销售、技术支持与个人自动化</option>
        <option value="page-21">17 · 翻车实录：直播现场 10 大故障与提炼法则</option>
        <option value="page-22">18 · 能力边界：现在的硬性限制与未来路线图</option>
        <option value="page-23">19 · 终场复盘：团队停下 Demo 的真诚反思</option>
        <option value="page-24">20 · 行动清单：第一周落地 9 步走指南</option>
      </select>
    </div>
    <a href="grok-bot-guide-by-spacex-engineers-cn.pdf" download class="nav-btn btn-primary" title="下载高清 24 页中文版 PDF">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
      <span>下载中文 PDF</span>
    </a>
    <a href="grok-bot-guide-by-spacex-engineers.pdf" target="_blank" class="nav-btn btn-secondary" title="对照查看 24 页原版英文 PDF">
      <span>英文原版</span>
    </a>
    <button onclick="window.print()" class="nav-btn btn-secondary" title="浏览器打印 / 导出为 PDF">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
      <span>打印</span>
    </button>
    <a href="https://github.com/LJTian/grokbot-field-notes-cn" target="_blank" class="nav-btn btn-icon" title="查看 GitHub 仓库源码">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
    </a>
  </div>
</header>

<div class="floating-bar no-print">
  <div class="page-indicator" id="page-indicator">第 01 / 24 页</div>
  <button class="float-btn" onclick="window.scrollTo({top:0, behavior:'smooth'})" title="回到顶部">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </button>
</div>

<div id="copy-toast" class="copy-toast">Prompt 已复制到剪贴板</div>
"""

    web_styles = """
  /* Web App Navigation & Responsive Styles */
  html {
    scroll-behavior: smooth;
  }
  .app-nav {
    position: sticky;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: rgba(254, 253, 252, 0.94);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid #e2ded9;
    padding: 10px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  }
  .nav-left {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .nav-dot {
    width: 8px;
    height: 8px;
    background: #e4402e;
    border-radius: 50%;
  }
  .nav-logo {
    font-weight: 800;
    font-size: 13pt;
    letter-spacing: 0.5px;
    color: #111;
  }
  .nav-badge {
    background: #111;
    color: #fff;
    font-size: 8pt;
    font-weight: 700;
    padding: 2.5px 7px;
    border-radius: 4px;
    letter-spacing: 0.5px;
  }
  .nav-sub {
    font-size: 8.5pt;
    color: #666;
    margin-left: 6px;
  }
  .nav-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  #chapter-select {
    font-family: inherit;
    font-size: 8.5pt;
    font-weight: 600;
    color: #222;
    padding: 6px 12px;
    border: 1px solid #d4cfc9;
    border-radius: 6px;
    background: #fff;
    cursor: pointer;
    outline: none;
    max-width: 260px;
    transition: border-color 0.2s;
  }
  #chapter-select:hover, #chapter-select:focus {
    border-color: #e4402e;
  }
  .nav-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-family: inherit;
    font-size: 8.5pt;
    font-weight: 600;
    padding: 6px 13px;
    border-radius: 6px;
    text-decoration: none;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.15s ease-in-out;
  }
  .btn-primary {
    background: #e4402e;
    color: #ffffff;
  }
  .btn-primary:hover {
    background: #c83222;
    color: #fff;
  }
  .btn-secondary {
    background: #f3efe9;
    color: #333;
    border-color: #dcd7ce;
  }
  .btn-secondary:hover {
    background: #e8e3d8;
    color: #111;
  }
  .btn-icon {
    padding: 6px 9px;
    background: #f3efe9;
    color: #333;
    border-color: #dcd7ce;
  }
  .btn-icon:hover {
    background: #e8e3d8;
    color: #111;
  }

  /* Floating Bottom Progress & Back-to-top */
  .floating-bar {
    position: fixed;
    bottom: 24px;
    right: 28px;
    z-index: 999;
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(17, 17, 17, 0.9);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    padding: 5px 8px 5px 14px;
    border-radius: 30px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25);
    color: #fff;
  }
  .page-indicator {
    font-size: 8.2pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #eee;
  }
  .float-btn {
    background: rgba(255, 255, 255, 0.15);
    color: #fff;
    border: none;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background 0.2s;
  }
  .float-btn:hover {
    background: #e4402e;
  }

  /* Copy Button inside Prompts */
  .prompt-card {
    position: relative;
  }
  .copy-btn {
    position: absolute;
    top: 7pt;
    right: 8pt;
    font-family: inherit;
    font-size: 6.8pt;
    font-weight: 600;
    color: #777;
    background: #f0ede8;
    border: 1px solid #dcd7ce;
    border-radius: 4px;
    padding: 2.5pt 6pt;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 3pt;
    transition: all 0.15s;
  }
  .copy-btn:hover {
    color: #111;
    background: #e4ded5;
    border-color: #bbb;
  }
  .copy-btn.copied {
    color: #fff;
    background: #108a38;
    border-color: #108a38;
  }

  /* Copy Toast */
  .copy-toast {
    position: fixed;
    top: 65px;
    left: 50%;
    transform: translateX(-50%) translateY(-20px);
    background: #111111;
    color: #ffffff;
    font-size: 8.5pt;
    font-weight: 600;
    padding: 7px 16px;
    border-radius: 20px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 2000;
  }
  .copy-toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }

  /* Responsive Mobile Screens */
  @media screen and (max-width: 860px) {
    .app-nav {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 14px;
    }
    .nav-sub {
      display: none;
    }
    .nav-actions {
      width: 100%;
      flex-wrap: wrap;
      justify-content: flex-start;
    }
    #chapter-select {
      max-width: 100%;
      flex: 1 1 100%;
    }
    .book-container {
      padding: 10px 6px;
      gap: 16px;
    }
    .page {
      width: 100%;
      max-width: 100vw;
      height: auto;
      min-height: unset;
      max-height: unset;
      padding: 20px 16px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    }
    .page.cover {
      height: 620px;
    }
    .cover-header {
      padding: 24px 18px 0 18px;
    }
    .cover-title {
      font-size: 26pt;
    }
    .cover-sub {
      font-size: 12pt;
    }
    .cover-image-container {
      width: 100%;
      height: 280px;
    }
    .cover-image {
      width: 130%;
      left: -15%;
      bottom: 0;
    }
    .grid-2col, .grid-3col, .grid-4col {
      grid-template-columns: 1fr;
    }
    .floating-bar {
      bottom: 16px;
      right: 16px;
      padding: 4px 8px 4px 12px;
    }
  }

  @media print {
    .no-print {
      display: none !important;
    }
  }
"""

    web_js = """
<script>
function jumpToChapter(pageId) {
  if (!pageId) return;
  const el = document.getElementById(pageId);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Attach Copy Buttons to Prompts
document.addEventListener('DOMContentLoaded', () => {
  const promptCards = document.querySelectorAll('.prompt-card');
  promptCards.forEach(card => {
    const content = card.querySelector('.prompt-content');
    if (!content) return;
    
    const btn = document.createElement('button');
    btn.className = 'copy-btn no-print';
    btn.innerHTML = '📋 复制 Prompt';
    btn.onclick = () => {
      const text = content.innerText.trim().replace(/^[“"']|[”"']$/g, '');
      navigator.clipboard.writeText(text).then(() => {
        btn.classList.add('copied');
        btn.innerHTML = '✅ 已复制';
        showToast('Prompt 已复制到剪贴板');
        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML = '📋 复制 Prompt';
        }, 2000);
      });
    };
    card.appendChild(btn);
  });

  // ScrollSpy for Active Page
  const pages = document.querySelectorAll('.page');
  const indicator = document.getElementById('page-indicator');
  const select = document.getElementById('chapter-select');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        if (id) {
          const numMatch = id.match(/page-(\\d+)/);
          if (numMatch) {
            const num = numMatch[1];
            if (indicator) {
              indicator.innerText = `第 ${num} / 24 页`;
            }
            if (select) {
              select.value = id;
            }
          }
        }
      }
    });
  }, { threshold: 0.3 });

  pages.forEach(p => observer.observe(p));
});

function showToast(msg) {
  const toast = document.getElementById('copy-toast');
  if (!toast) return;
  toast.innerText = msg;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 2200);
}
</script>
"""

    # Inject web styles before </head>
    html_with_web = guide_html.replace("</style>", web_styles + "\n</style>")
    # Inject nav bar right after <body>
    html_with_web = html_with_web.replace("<body>\n<div class=\"book-container\">", f"<body>\n{web_nav_html}\n<div class=\"book-container\">")
    # Inject JS right before </body>
    html_with_web = html_with_web.replace("</body>", f"{web_js}\n</body>")

    public_index_path = os.path.join(PUBLIC_DIR, "index.html")
    with open(public_index_path, "w", encoding="utf-8") as f:
        f.write(html_with_web)
    print(f"Generated {public_index_path} ({len(html_with_web)} bytes)")

    # 4. Generate Cloudflare Pages configuration files
    headers_content = """# Cloudflare Pages Caching and Security Headers
/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/*.pdf
  Cache-Control: public, max-age=604800, immutable

/*.png
  Cache-Control: public, max-age=2592000, immutable

/index.html
  Cache-Control: public, max-age=3600, must-revalidate
"""
    headers_path = os.path.join(PUBLIC_DIR, "_headers")
    with open(headers_path, "w", encoding="utf-8") as f:
        f.write(headers_content)
    print(f"Generated {headers_path}")

    robots_content = """User-agent: *
Allow: /
"""
    robots_path = os.path.join(PUBLIC_DIR, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"Generated {robots_path}")

    print("\n✅ Build finished successfully! All static assets ready in public/ for Cloudflare Pages.")

if __name__ == "__main__":
    build()
