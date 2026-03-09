"""Reusable HTML component generators and Chart.js helpers."""

import json


# ────────────────────────────────────────────────
#  KPI / Stat Cards
# ────────────────────────────────────────────────


def comp_kpi(title, value, change, up, icon, color):
    arrow = "↑" if up else ("↓" if change else "")
    ccls = "text-emerald-600" if up else "text-red-500" if change else "text-gray-400"
    chg = (
        f'<div class="text-[11px] mt-2 {ccls}">{arrow} {change}</div>' if change else ""
    )
    return (
        f'<div class="card p-5 transition-shadow cursor-pointer">'
        f'<div class="flex items-center justify-between mb-3">'
        f'<span class="text-[13px] text-gray-500">{title}</span>'
        f'<i data-lucide="{icon}" class="w-[18px] h-[18px] text-gray-300"></i></div>'
        f'<div class="text-2xl font-bold" style="color:{color}">{value}</div>'
        f"{chg}</div>"
    )


def comp_stat_big(title, value, sub, icon, color):
    return (
        f'<div class="card p-6 flex items-center gap-5 transition-shadow">'
        f'<div class="w-14 h-14 rounded-2xl flex items-center justify-center shrink-0" style="background:{color}15">'
        f'<i data-lucide="{icon}" class="w-7 h-7" style="color:{color}"></i></div>'
        f'<div><div class="text-3xl font-bold" style="color:{color}">{value}</div>'
        f'<div class="text-[13px] text-gray-500 mt-1">{title}</div>'
        f'<div class="text-[11px] text-gray-400 mt-0.5">{sub}</div></div></div>'
    )


def comp_progress_ring(value, label, color, size=80):
    r = size // 2 - 6
    circ = 2 * 3.14159 * r
    offset = circ * (1 - value / 100)
    return (
        f'<div class="flex flex-col items-center gap-2">'
        f'<svg width="{size}" height="{size}" class="-rotate-90">'
        f'<circle cx="{size // 2}" cy="{size // 2}" r="{r}" fill="none" stroke="#e5e7eb" stroke-width="6"/>'
        f'<circle cx="{size // 2}" cy="{size // 2}" r="{r}" fill="none" stroke="{color}" stroke-width="6" '
        f'stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}" stroke-linecap="round"/></svg>'
        f'<div class="text-center"><div class="text-lg font-bold" style="color:{color}">{value}%</div>'
        f'<div class="text-[11px] text-gray-400">{label}</div></div></div>'
    )


# ────────────────────────────────────────────────
#  Chart containers & JS
# ────────────────────────────────────────────────


def comp_chart_box(chart_id, title, height=280, span=""):
    sp = f" {span}" if span else ""
    return (
        f'<div class="card p-5{sp}">'
        f'<h3 class="font-semibold text-[13px] text-gray-700 mb-4">{title}</h3>'
        f'<div style="height:{height}px"><canvas id="{chart_id}"></canvas></div></div>'
    )


def js_chart(cid, ctype, labels, datasets, show_legend=False, horizontal=False):
    """Generate Chart.js initialization JS."""
    cfg = {
        "type": ctype,
        "data": {"labels": labels, "datasets": datasets},
        "options": {
            "responsive": True,
            "maintainAspectRatio": False,
            "plugins": {
                "legend": {
                    "display": show_legend,
                    "position": "bottom",
                    "labels": {
                        "font": {"size": 11, "family": "Inter"},
                        "usePointStyle": True,
                        "padding": 14,
                    },
                }
            },
        },
    }
    if ctype in ("line", "bar"):
        if horizontal:
            cfg["indexAxis"] = "y"
        cfg["options"]["scales"] = {
            "y": {
                "beginAtZero": True,
                "grid": {"color": "#f3f4f6"},
                "ticks": {"font": {"size": 11}},
            },
            "x": {"grid": {"display": False}, "ticks": {"font": {"size": 11}}},
        }
    if ctype == "radar":
        cfg["options"]["scales"] = {
            "r": {
                "beginAtZero": True,
                "grid": {"color": "#e5e7eb"},
                "pointLabels": {"font": {"size": 11}},
            }
        }
    return f'charts.push(new Chart(document.getElementById("{cid}"),{json.dumps(cfg, ensure_ascii=False)}));'


# ────────────────────────────────────────────────
#  Tables
# ────────────────────────────────────────────────


def comp_table(tid, headers, rows, color):
    """Sortable data table."""
    ths = "".join(
        f'<th class="px-4 py-3 text-left text-[11px] font-semibold text-gray-500 uppercase tracking-wider cursor-pointer hover:text-gray-800" '
        f'onclick="sortTbl(\'{tid}\',{i})">{h} <span class="text-gray-300">↕</span></th>'
        for i, h in enumerate(headers)
    )
    trs = ""
    for r in rows:
        tds = ""
        for j, cell in enumerate(r):
            cls = "font-medium" if j == 0 else ""
            # Status coloring
            if cell in ("完了", "成約", "正常", "合格"):
                tds += f'<td class="px-4 py-3 text-[13px]"><span class="px-2 py-0.5 rounded-full text-[11px] bg-emerald-50 text-emerald-700">{cell}</span></td>'
            elif cell in ("進行中", "交渉中", "処理中", "対応中"):
                tds += f'<td class="px-4 py-3 text-[13px]"><span class="px-2 py-0.5 rounded-full text-[11px]" style="background:{color}15;color:{color}">{cell}</span></td>'
            elif cell in ("未着手", "未対応", "保留", "不合格"):
                tds += f'<td class="px-4 py-3 text-[13px]"><span class="px-2 py-0.5 rounded-full text-[11px] bg-gray-100 text-gray-600">{cell}</span></td>'
            elif cell in ("遅延", "異常", "要対応", "緊急"):
                tds += f'<td class="px-4 py-3 text-[13px]"><span class="px-2 py-0.5 rounded-full text-[11px] bg-red-50 text-red-600">{cell}</span></td>'
            else:
                tds += (
                    f'<td class="px-4 py-3 text-[13px] {cls} text-gray-700">{cell}</td>'
                )
        trs += f'<tr class="border-b border-gray-50 hover:bg-gray-50/50 transition-colors">{tds}</tr>'
    return (
        f'<div class="card overflow-hidden"><div class="overflow-x-auto">'
        f'<table id="{tid}" class="w-full"><thead class="bg-gray-50/80 border-b">'
        f"<tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div></div>"
    )


JS_SORT_TABLE = """
function sortTbl(id,col){const t=document.getElementById(id);const b=t.querySelector('tbody');
const rows=Array.from(b.querySelectorAll('tr'));const asc=t.dataset.sc!==col+'a';
t.dataset.sc=asc?col+'a':col+'d';
rows.sort((a,b)=>{const av=a.cells[col]?.textContent.trim()||'';const bv=b.cells[col]?.textContent.trim()||'';
const an=parseFloat(av.replace(/[^0-9.-]/g,''));const bn=parseFloat(bv.replace(/[^0-9.-]/g,''));
if(!isNaN(an)&&!isNaN(bn))return asc?an-bn:bn-an;return asc?av.localeCompare(bv,'ja'):bv.localeCompare(av,'ja');});
rows.forEach(r=>b.appendChild(r));}
"""


# ────────────────────────────────────────────────
#  Activity / Timeline
# ────────────────────────────────────────────────


def comp_activities(items, color, limit=6):
    html = ""
    for a in items[:limit]:
        html += (
            f'<div class="flex gap-3 items-start">'
            f'<div class="w-8 h-8 rounded-full flex items-center justify-center text-[11px] text-white shrink-0" '
            f'style="background:{color}">{a["user"][0]}</div>'
            f'<div class="min-w-0"><p class="text-[13px] text-gray-700">'
            f'<span class="font-medium">{a["user"]}</span> {a["text"]}</p>'
            f'<p class="text-[11px] text-gray-400">{a["time"]}</p></div></div>'
        )
    return html


def comp_timeline_items(items, color):
    html = ""
    for i, item in enumerate(items):
        done = item.get("done", False)
        dot_bg = color if done else "#d1d5db"
        line = (
            f'<div class="w-0.5 flex-1 mx-auto" style="background:{color if done else "#e5e7eb"}"></div>'
            if i < len(items) - 1
            else '<div class="flex-1"></div>'
        )
        html += (
            f'<div class="flex gap-4">'
            f'<div class="flex flex-col items-center">'
            f'<div class="w-3 h-3 rounded-full shrink-0 mt-1.5" style="background:{dot_bg}"></div>{line}</div>'
            f'<div class="pb-6"><p class="text-[13px] font-medium text-gray-700">{item["title"]}</p>'
            f'<p class="text-[11px] text-gray-400 mt-0.5">{item["date"]}</p>'
            f'<p class="text-[12px] text-gray-500 mt-1">{item.get("desc", "")}</p></div></div>'
        )
    return html


# ────────────────────────────────────────────────
#  Search / Filter bar
# ────────────────────────────────────────────────


def comp_search(input_id, placeholder="検索..."):
    return (
        f'<div class="relative">'
        f'<i data-lucide="search" class="w-4 h-4 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2"></i>'
        f'<input id="{input_id}" type="text" placeholder="{placeholder}" '
        f'class="w-full pl-10 pr-4 py-2.5 text-[13px] bg-white border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-100 transition">'
        f"</div>"
    )


def js_filter(input_id, container_id):
    return (
        f'document.getElementById("{input_id}").addEventListener("input",function(){{'
        f"const q=this.value.toLowerCase();"
        f'document.querySelectorAll("#{container_id} [data-search]").forEach(el=>{{'
        f'el.style.display=el.dataset.search.toLowerCase().includes(q)?"":"none"}});}});'
    )


# ────────────────────────────────────────────────
#  Tabs
# ────────────────────────────────────────────────


def comp_tabs(tab_id, labels, color):
    tabs_html = ""
    for i, label in enumerate(labels):
        act = "font-semibold" if i == 0 else "text-gray-400"
        border = (
            f"border-b-2;border-color:{color}"
            if i == 0
            else "border-b-2 border-transparent"
        )
        tabs_html += (
            f'<button class="tab-btn px-4 py-2.5 text-[13px] {act} transition-colors cursor-pointer" '
            f'style="{border}" data-tab="{tab_id}-{i}" '
            f"onclick=\"switchTab('{tab_id}',{i},'{color}')\">{label}</button>"
        )
    return f'<div class="flex gap-0 border-b mb-4">{tabs_html}</div>'


JS_TABS = """
function switchTab(gid,idx,color){
document.querySelectorAll('[data-tab^="'+gid+'"]').forEach((b,i)=>{
b.style.borderColor=i===idx?color:'transparent';
b.classList.toggle('font-semibold',i===idx);b.classList.toggle('text-gray-400',i!==idx);});
document.querySelectorAll('[data-panel^="'+gid+'"]').forEach((p,i)=>{
p.style.display=i===idx?'block':'none';});}
"""


def comp_tab_panel(tab_id, idx, content, hidden=True):
    disp = "none" if hidden else "block"
    return f'<div data-panel="{tab_id}-{idx}" style="display:{disp}">{content}</div>'


# ────────────────────────────────────────────────
#  Form fields
# ────────────────────────────────────────────────


def comp_form_field(label, ftype="text", placeholder="", name="", options=None):
    name = name or label
    if ftype == "select" and options:
        opts = "".join(f'<option value="{o}">{o}</option>' for o in options)
        return (
            f'<div><label class="block text-[12px] font-medium text-gray-600 mb-1.5">{label}</label>'
            f'<select name="{name}" class="w-full px-3 py-2.5 text-[13px] border rounded-lg bg-white focus:outline-none focus:ring-2 focus:ring-blue-100">'
            f'<option value="">選択してください</option>{opts}</select></div>'
        )
    if ftype == "textarea":
        return (
            f'<label class="block text-[12px] font-medium text-gray-600 mb-1.5">{label}</label>'
            f'<textarea name="{name}" rows="3" placeholder="{placeholder}" '
            f'class="w-full px-3 py-2.5 text-[13px] border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-100"></textarea>'
        )
    return (
        f'<div><label class="block text-[12px] font-medium text-gray-600 mb-1.5">{label}</label>'
        f'<input type="{ftype}" name="{name}" placeholder="{placeholder}" '
        f'class="w-full px-3 py-2.5 text-[13px] border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-100"></div>'
    )


# ────────────────────────────────────────────────
#  Misc helpers
# ────────────────────────────────────────────────


def comp_badge(text, color="gray"):
    colors = {
        "green": "bg-emerald-50 text-emerald-700",
        "red": "bg-red-50 text-red-600",
        "blue": "bg-blue-50 text-blue-700",
        "yellow": "bg-amber-50 text-amber-700",
        "gray": "bg-gray-100 text-gray-600",
        "purple": "bg-purple-50 text-purple-700",
    }
    cls = colors.get(color, colors["gray"])
    return f'<span class="px-2 py-0.5 rounded-full text-[11px] font-medium {cls}">{text}</span>'


def comp_empty(icon, message):
    return (
        f'<div class="text-center py-16">'
        f'<i data-lucide="{icon}" class="w-12 h-12 text-gray-300 mx-auto mb-3"></i>'
        f'<p class="text-[13px] text-gray-400">{message}</p></div>'
    )


def comp_btn(text, color, icon=None, onclick="", size="md"):
    py = "py-2 px-4 text-[13px]" if size == "md" else "py-1.5 px-3 text-[12px]"
    ic = f'<i data-lucide="{icon}" class="w-4 h-4"></i>' if icon else ""
    return (
        f'<button onclick="{onclick}" class="inline-flex items-center gap-1.5 {py} '
        f'rounded-lg text-white font-medium transition-all hover:opacity-90 cursor-pointer" '
        f'style="background:{color}">{ic}{text}</button>'
    )


def comp_btn_outline(text, color, icon=None, onclick=""):
    ic = f'<i data-lucide="{icon}" class="w-4 h-4"></i>' if icon else ""
    return (
        f'<button onclick="{onclick}" class="inline-flex items-center gap-1.5 py-2 px-4 '
        f'rounded-lg text-[13px] font-medium border transition-all hover:bg-gray-50 cursor-pointer" '
        f'style="color:{color};border-color:{color}">{ic}{text}</button>'
    )
