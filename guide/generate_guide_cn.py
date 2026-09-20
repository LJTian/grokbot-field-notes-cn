# -*- coding: utf-8 -*-
import os
import subprocess

from pages_part1 import (
    render_page_01, render_page_02, render_page_03, render_page_04,
    render_page_05, render_page_06, render_page_07, render_page_08
)
from pages_part2 import (
    render_page_09, render_page_10, render_page_11, render_page_12,
    render_page_13, render_page_14, render_page_15, render_page_16
)
from pages_part3 import (
    render_page_17, render_page_18, render_page_19, render_page_20,
    render_page_21, render_page_22, render_page_23, render_page_24
)

HTML_HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SpaceX 工程师撰写的 Grok Bot 实战指南 (中文版)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;600;700;800;900&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Inter', 'PingFang SC', 'Hiragino Sans GB', 'Noto Sans SC', 'Microsoft YaHei', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #111111;
    background: #eef0f3;
    overflow-wrap: break-word;
    -webkit-font-smoothing: antialiased;
  }
  .book-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    padding: 20px 0;
  }
  @media print {
    body {
      background: #ffffff;
    }
    .book-container {
      gap: 0;
      padding: 0;
      margin: 0;
      display: block;
    }
  }
  .page {
    width: 210mm;
    height: 296.8mm;
    max-height: 296.8mm;
    page-break-after: always;
    break-after: page;
    page-break-inside: avoid;
    break-inside: avoid;
    position: relative;
    padding: 12mm 14mm 10mm 14mm;
    overflow: hidden;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    background: #ffffff;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  }
  .page:last-child {
    page-break-after: avoid;
    break-after: avoid;
  }
  @media print {
    .page {
      box-shadow: none;
      height: 296.8mm;
      max-height: 296.8mm;
      overflow: hidden;
    }
    .page:last-child {
      page-break-after: avoid;
      break-after: avoid;
    }
  }
  .page.cover {
    padding: 0;
    background: #fefdfc;
    position: relative;
    display: flex;
    flex-direction: column;
  }
  .cover-header {
    padding: 22mm 18mm 0 18mm;
    z-index: 2;
  }
  .cover-title {
    font-family: 'Poppins', 'PingFang SC', 'Noto Sans SC', sans-serif;
    font-size: 34pt;
    font-weight: 800;
    line-height: 1.18;
    letter-spacing: -1px;
    margin: 0 0 12pt 0;
    color: #0d0d0d;
  }
  .cover-sub {
    font-size: 15pt;
    font-weight: 600;
    color: #444444;
    margin: 0;
    letter-spacing: -0.2px;
  }
  .cover-image-container {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 210mm;
    height: 96mm;
    overflow: hidden;
    z-index: 1;
  }
  .cover-image {
    width: 130%;
    position: absolute;
    bottom: 0;
    left: -15%;
    display: block;
  }

  /* Universal Header */
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 6.5pt;
    border-bottom: 1px solid #e6e4e1;
    margin-bottom: 11pt;
  }
  .header-left {
    display: flex;
    align-items: center;
    gap: 6pt;
    font-size: 7.4pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #111111;
  }
  .dot {
    width: 6.5px;
    height: 6.5px;
    background-color: #e4402e;
    border-radius: 50%;
    display: inline-block;
  }
  .header-right {
    font-size: 7.4pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #8c8985;
  }

  /* Universal Headings */
  .eyebrow {
    font-size: 7.4pt;
    font-weight: 700;
    color: #e4402e;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 3.5pt;
  }
  .page-title {
    font-family: 'Poppins', 'PingFang SC', 'Noto Sans SC', sans-serif;
    font-size: 21pt;
    font-weight: 700;
    line-height: 1.2;
    color: #111111;
    letter-spacing: -0.5px;
    margin: 0 0 6.5pt 0;
  }
  .page-intro {
    font-size: 8.8pt;
    line-height: 1.48;
    color: #404040;
    margin: 0 0 10pt 0;
  }
  .page-intro strong {
    color: #111111;
    font-weight: 700;
  }

  .section-label {
    font-size: 7.6pt;
    font-weight: 700;
    color: #e4402e;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin: 8pt 0 5.5pt 0;
  }
  .section-label.dark {
    color: #111111;
  }

  /* Cards & Grids */
  .grid-2col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9.5pt;
    margin-bottom: 8.5pt;
  }
  .grid-3col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8.5pt;
    margin-bottom: 8.5pt;
  }
  .grid-4col {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 7.5pt;
    margin-bottom: 8.5pt;
  }

  .card {
    background: #f4f3f1;
    border-radius: 8px;
    padding: 8.5pt 10.5pt;
  }
  .card-title {
    font-size: 9.1pt;
    font-weight: 700;
    color: #111111;
    margin-bottom: 3.5pt;
    display: flex;
    align-items: center;
    gap: 5pt;
  }
  .card-subtitle {
    font-size: 7.6pt;
    font-weight: 600;
    color: #777777;
    margin-top: -2pt;
    margin-bottom: 3.5pt;
  }
  .card-body {
    font-size: 7.9pt;
    line-height: 1.42;
    color: #383838;
  }
  .card-body strong {
    color: #111111;
    font-weight: 700;
  }
  .card-body p {
    margin: 0 0 3.5pt 0;
  }
  .card-body p:last-child {
    margin-bottom: 0;
  }

  /* Stat Card */
  .stat-card {
    background: #f4f3f1;
    border-radius: 8px;
    padding: 8pt 10pt;
  }
  .stat-val {
    font-family: 'Poppins', sans-serif;
    font-size: 18pt;
    font-weight: 800;
    color: #111111;
    line-height: 1.1;
    margin-bottom: 2pt;
  }
  .stat-desc {
    font-size: 7.3pt;
    line-height: 1.32;
    color: #555555;
  }

  /* Numbered List Items */
  .num-item {
    display: flex;
    align-items: flex-start;
    gap: 7.5pt;
    padding: 5.8pt 0;
    border-bottom: 1px solid #e6e4e1;
  }
  .num-item:last-child {
    border-bottom: none;
  }
  .num-badge {
    background: #111111;
    color: #ffffff;
    font-size: 7.2pt;
    font-weight: 700;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 1.5pt;
  }
  .num-content {
    font-size: 8pt;
    line-height: 1.42;
    color: #383838;
    flex: 1;
  }
  .num-content strong {
    color: #111111;
    font-weight: 700;
  }

  /* Callout Banners */
  .callout {
    background: #faf2f0;
    border-left: 3.5px solid #e4402e;
    border-radius: 6px;
    padding: 8pt 11pt;
    margin-top: auto;
    margin-bottom: 4pt;
    display: flex;
    gap: 7.5pt;
  }
  .callout-icon {
    width: 18px;
    height: 18px;
    background: #f6dcd6;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8.5pt;
    flex-shrink: 0;
    margin-top: 1pt;
  }
  .callout-body {
    flex: 1;
  }
  .callout-title {
    font-size: 8.5pt;
    font-weight: 700;
    color: #111111;
    margin-bottom: 2pt;
  }
  .callout-text {
    font-size: 7.7pt;
    line-height: 1.4;
    color: #383838;
    margin: 0;
  }
  .callout-text strong {
    color: #111111;
    font-weight: 700;
  }

  /* Quote Box */
  .quote-box {
    border-left: 3.5px solid #e4402e;
    padding-left: 10pt;
    margin: 6.5pt 0 8.5pt 0;
  }
  .quote-text {
    font-family: 'Poppins', 'PingFang SC', 'Noto Sans SC', sans-serif;
    font-size: 10.5pt;
    font-weight: 700;
    line-height: 1.35;
    color: #111111;
    margin: 0 0 2.5pt 0;
  }
  .quote-author {
    font-size: 7.4pt;
    font-weight: 500;
    color: #777777;
    margin: 0;
  }

  /* Prompt Cards */
  .prompt-card {
    background: #f4f3f1;
    border-left: 3px solid #e4402e;
    border-radius: 6px;
    padding: 6.5pt 9pt;
    margin-bottom: 6.5pt;
  }
  .prompt-label {
    font-size: 7.1pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    color: #e4402e;
    text-transform: uppercase;
    margin-bottom: 2pt;
  }
  .prompt-content {
    font-size: 7.8pt;
    line-height: 1.38;
    color: #111111;
    font-style: normal;
    margin-bottom: 2pt;
  }
  .prompt-meta {
    font-size: 7.1pt;
    color: #777777;
    line-height: 1.32;
  }

  /* Footnote */
  .footnote {
    font-size: 6.9pt;
    line-height: 1.32;
    color: #888880;
    margin-bottom: 4pt;
  }

  /* Universal Footer */
  .footer {
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 4.5pt;
    font-size: 7pt;
    font-weight: 500;
    color: #aaa8a5;
    border-top: 1px solid #f2f0ed;
  }

  /* TOC Item */
  .toc-list {
    display: flex;
    flex-direction: column;
    gap: 0;
  }
  .toc-item {
    display: flex;
    align-items: baseline;
    padding: 4.5pt 0;
    border-bottom: 1px solid #f0eeeb;
    gap: 11pt;
  }
  .toc-num {
    font-size: 8.4pt;
    font-weight: 700;
    color: #888888;
    width: 18pt;
    flex-shrink: 0;
  }
  .toc-title {
    font-size: 8.4pt;
    font-weight: 700;
    color: #111111;
    width: 130pt;
    flex-shrink: 0;
  }
  .toc-desc {
    font-size: 7.6pt;
    color: #666666;
    flex: 1;
  }

  /* Bullet points */
  ul.custom-bullets {
    margin: 0;
    padding-left: 11pt;
  }
  ul.custom-bullets li {
    font-size: 7.8pt;
    line-height: 1.4;
    color: #383838;
    margin-bottom: 3pt;
  }
  ul.custom-bullets li:last-child {
    margin-bottom: 0;
  }
  ul.custom-bullets li strong {
    color: #111111;
  }

  /* Flow chart */
  .flow-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 5pt;
    background: #f4f3f1;
    border-radius: 7px;
    padding: 7pt 10pt;
    margin-bottom: 8pt;
  }
  .flow-step {
    font-size: 7.9pt;
    font-weight: 700;
    color: #111111;
    text-align: center;
    flex: 1;
  }
  .flow-arrow {
    color: #e4402e;
    font-weight: 800;
    font-size: 10pt;
  }

  /* Failure item */
  .fail-item {
    border-bottom: 1px solid #f0eeeb;
    padding: 4pt 0;
  }
  .fail-item:last-child {
    border-bottom: none;
  }
  .fail-head {
    display: flex;
    justify-content: space-between;
    font-size: 8pt;
    font-weight: 700;
    color: #111111;
    margin-bottom: 1.5pt;
  }
  .fail-day {
    color: #888888;
    font-size: 7.2pt;
  }
  .fail-desc {
    font-size: 7.5pt;
    line-height: 1.35;
    color: #444444;
  }
  .fail-rule {
    font-size: 7.5pt;
    line-height: 1.35;
    color: #e4402e;
    font-weight: 600;
    margin-top: 1pt;
  }
</style>
</head>
<body>
<div class="book-container">
"""

HTML_FOOT = """
</div>
</body>
</html>
"""

def generate_html():
    pages = [
        render_page_01(),
        render_page_02(),
        render_page_03(),
        render_page_04(),
        render_page_05(),
        render_page_06(),
        render_page_07(),
        render_page_08(),
        render_page_09(),
        render_page_10(),
        render_page_11(),
        render_page_12(),
        render_page_13(),
        render_page_14(),
        render_page_15(),
        render_page_16(),
        render_page_17(),
        render_page_18(),
        render_page_19(),
        render_page_20(),
        render_page_21(),
        render_page_22(),
        render_page_23(),
        render_page_24()
    ]
    return HTML_HEAD + "".join(pages) + HTML_FOOT

def main():
    guide_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(guide_dir, "grok-bot-guide-cn.html")
    pdf_path = os.path.join(guide_dir, "grok-bot-guide-by-spacex-engineers-cn.pdf")
    
    html_content = generate_html()
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML at {html_path}")

if __name__ == "__main__":
    main()
