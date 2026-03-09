"""Page generators — Dashboard, Feature, Data, Detail, Report variants."""

import random

from .components import (
    comp_kpi,
    comp_stat_big,
    comp_progress_ring,
    comp_chart_box,
    js_chart,
    comp_table,
    JS_SORT_TABLE,
    comp_activities,
    comp_timeline_items,
    comp_search,
    js_filter,
    comp_tabs,
    JS_TABS,
    comp_tab_panel,
    comp_form_field,
    comp_badge,
    comp_empty,
    comp_btn,
    comp_btn_outline,
)

MONTHS = [
    "1月",
    "2月",
    "3月",
    "4月",
    "5月",
    "6月",
    "7月",
    "8月",
    "9月",
    "10月",
    "11月",
    "12月",
]
NAMES = [
    "田中太郎",
    "鈴木花子",
    "佐藤一郎",
    "山田優子",
    "高橋健太",
    "伊藤美咲",
    "渡辺誠",
    "中村明子",
    "小林拓也",
    "加藤真理",
]
STATUSES = ["完了", "進行中", "未着手", "レビュー中"]

# ════════════════════════════════════════════════════════════
#  MOCK DATA
# ════════════════════════════════════════════════════════════

KPI_BANK = {
    "kanban": [
        ("進行中タスク", "件", 15, 40, "+{v}", "clipboard-list"),
        ("完了率", "%", 60, 95, "+{v}pt", "check-circle"),
        ("遅延", "件", 0, 8, "-{v}", "alert-triangle"),
        ("メンバー", "名", 5, 25, "", "users"),
    ],
    "calendar": [
        ("今月出勤", "日", 18, 23, "", "calendar"),
        ("残業時間", "h", 5, 30, "-{v}h", "clock"),
        ("有休残", "日", 5, 20, "", "sun"),
        ("稼働率", "%", 85, 99, "+{v}%", "activity"),
    ],
    "form_wizard": [
        ("今月申請", "件", 8, 35, "+{v}", "file-text"),
        ("承認待ち", "件", 1, 8, "", "clock"),
        ("平均処理", "日", 1, 5, "-{v}日", "zap"),
        ("差戻率", "%", 2, 15, "-{v}pt", "alert-circle"),
    ],
    "checklist": [
        ("完了率", "%", 60, 98, "+{v}pt", "check-circle"),
        ("未実施", "件", 1, 12, "", "circle"),
        ("要是正", "件", 0, 5, "-{v}", "alert-triangle"),
        ("今月検査", "件", 10, 50, "", "clipboard-list"),
    ],
    "map": [
        ("稼働車両", "台", 5, 30, "", "truck"),
        ("本日配送", "件", 20, 80, "+{v}", "package"),
        ("遅延", "件", 0, 5, "-{v}", "alert-triangle"),
        ("稼働率", "%", 70, 98, "+{v}%", "activity"),
    ],
    "inventory": [
        ("総SKU", "品", 100, 2000, "", "package"),
        ("在庫金額", "万円", 500, 5000, "", "database"),
        ("発注点割れ", "品", 2, 15, "", "alert-triangle"),
        ("回転率", "回", 2, 12, "+{v}", "refresh-cw"),
    ],
    "timeline": [
        ("進捗率", "%", 20, 85, "+{v}pt", "trending-up"),
        ("残工数", "日", 10, 90, "", "clock"),
        ("完了工程", "件", 3, 20, "+{v}", "check"),
        ("遅延", "件", 0, 5, "-{v}", "alert-triangle"),
    ],
    "documents": [
        ("総文書", "件", 50, 500, "+{v}", "file-text"),
        ("未承認", "件", 2, 15, "", "clock"),
        ("今月更新", "件", 5, 30, "+{v}", "refresh-cw"),
        ("カテゴリ", "種", 5, 20, "", "folder"),
    ],
    "matrix": [
        ("評価対象", "件", 3, 20, "", "grid"),
        ("完了", "件", 1, 15, "+{v}", "check-circle"),
        ("最高スコア", "pt", 70, 98, "", "star"),
        ("平均スコア", "pt", 50, 85, "+{v}pt", "bar-chart-3"),
    ],
    "calculator": [
        ("売上", "万円", 500, 5000, "+{v}%", "trending-up"),
        ("原価率", "%", 40, 75, "-{v}pt", "percent"),
        ("粗利", "万円", 100, 3000, "+{v}%", "banknote"),
        ("営業利益", "万円", 50, 1000, "+{v}%", "wallet"),
    ],
    "chat": [
        ("未読", "件", 2, 20, "", "mail"),
        ("今日の会話", "件", 5, 30, "+{v}", "message-square"),
        ("メンバー", "名", 5, 30, "", "users"),
        ("応答時間", "分", 5, 30, "-{v}分", "clock"),
    ],
    "crm": [
        ("顧客数", "社", 50, 500, "+{v}", "building-2"),
        ("商談中", "件", 5, 30, "+{v}", "handshake"),
        ("今月成約", "件", 1, 10, "+{v}", "trophy"),
        ("売上見込", "万円", 500, 5000, "+{v}%", "trending-up"),
    ],
    "hr": [
        ("社員数", "名", 10, 200, "", "users"),
        ("今月入社", "名", 0, 5, "+{v}", "user-plus"),
        ("研修完了率", "%", 50, 95, "+{v}pt", "graduation-cap"),
        ("離職率", "%", 2, 15, "-{v}pt", "user-minus"),
    ],
    "workflow": [
        ("処理中", "件", 3, 20, "", "loader"),
        ("承認待ち", "件", 1, 10, "", "clock"),
        ("完了", "件", 10, 50, "+{v}", "check-circle"),
        ("平均日数", "日", 1, 7, "-{v}日", "calendar"),
    ],
    "analytics": [
        ("PV", "件", 1000, 50000, "+{v}%", "eye"),
        ("CV率", "%", 1, 8, "+{v}pt", "target"),
        ("単価", "円", 5000, 50000, "+{v}%", "banknote"),
        ("ROI", "%", 50, 300, "+{v}pt", "trending-up"),
    ],
}


def gen_mock(ftype, ch, colors):
    """Generate all mock data for a challenge."""
    rng = random.Random(ch["industry_no"] * 100 + ch["challenge_no"])
    p, s, bg = colors

    # KPIs
    bank = KPI_BANK.get(ftype, KPI_BANK["kanban"])
    kpis = []
    for title, unit, lo, hi, chg_tpl, icon in bank:
        v = rng.randint(lo, hi)
        cv = rng.randint(1, max(2, v // 5))
        up = "-" not in chg_tpl if chg_tpl else False
        change = chg_tpl.format(v=cv) if chg_tpl else ""
        kpis.append((title, f"{v}{unit}", change, up, icon))

    # Chart data
    chart1 = [rng.randint(20, 90) for _ in range(12)]
    chart2 = [rng.randint(10, 60) for _ in range(6)]
    chart_pie = [rng.randint(10, 40) for _ in range(5)]

    # Table rows
    rows = []
    depts = [
        "営業部",
        "製造部",
        "管理部",
        "開発部",
        "品質部",
        "物流部",
        "CS部",
        "人事部",
    ]
    for i in range(12):
        rows.append(
            [
                f"#{rng.randint(1000, 9999)}",
                NAMES[i % len(NAMES)],
                depts[rng.randint(0, len(depts) - 1)],
                STATUSES[rng.randint(0, len(STATUSES) - 1)],
                f"2026/{rng.randint(1, 3):02d}/{rng.randint(1, 28):02d}",
                f"¥{rng.randint(10, 999):,}万",
            ]
        )

    # Activities
    actions = ["を更新", "を完了", "にコメント", "を作成", "を承認", "に対応"]
    activities = [
        {
            "user": NAMES[i % len(NAMES)],
            "text": actions[rng.randint(0, len(actions) - 1)],
            "time": f"{rng.randint(1, 48)}時間前",
        }
        for i in range(8)
    ]

    # Timeline items
    tl_items = [
        {
            "title": f"フェーズ{i + 1}",
            "date": f"2026/{rng.randint(1, 6):02d}/{rng.randint(1, 28):02d}",
            "desc": f"ステップ{i + 1}の作業",
            "done": i < rng.randint(2, 5),
        }
        for i in range(6)
    ]

    # Kanban cards
    kanban_cols = {"未着手": [], "進行中": [], "レビュー": [], "完了": []}
    priorities = ["高", "中", "低"]
    for i in range(16):
        col_key = list(kanban_cols.keys())[rng.randint(0, 3)]
        kanban_cols[col_key].append(
            {
                "title": f"タスク-{rng.randint(100, 999)}",
                "assignee": NAMES[rng.randint(0, len(NAMES) - 1)],
                "priority": priorities[rng.randint(0, 2)],
                "due": f"{rng.randint(1, 3)}/{rng.randint(1, 28)}",
            }
        )

    return {
        "kpis": kpis,
        "chart1": chart1,
        "chart2": chart2,
        "chart_pie": chart_pie,
        "rows": rows,
        "activities": activities,
        "timeline": tl_items,
        "kanban": kanban_cols,
        "rng": rng,
        "p": p,
        "s": s,
        "bg": bg,
    }


# ════════════════════════════════════════════════════════════
#  DASHBOARD VARIANTS (6)
# ════════════════════════════════════════════════════════════


def dash_kpi_line_activity(ch, colors, m):
    """V1: 4 KPIs + line chart + activity feed"""
    p, s, bg = colors
    kpis = "".join(comp_kpi(*k, p) for k in m["kpis"][:4])
    chart = comp_chart_box("dC1", "月次推移", 260, "lg:col-span-2")
    acts = comp_activities(m["activities"], p)
    html = (
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">{kpis}</div>'
        f'<div class="grid grid-cols-1 lg:grid-cols-3 gap-5">{chart}'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">最近の更新</h3>'
        f'<div class="space-y-4">{acts}</div></div></div>'
    )
    ds = [
        {
            "label": "実績",
            "data": m["chart1"],
            "borderColor": p,
            "backgroundColor": p + "15",
            "fill": True,
            "tension": 0.4,
            "pointRadius": 3,
            "pointBackgroundColor": p,
        }
    ]
    js = js_chart("dC1", "line", MONTHS, ds)
    return {
        "id": "dashboard",
        "title": "ダッシュボード",
        "desc": "KPIと最新状況",
        "icon": "layout-dashboard",
        "html": html,
        "js": js,
    }


def dash_stats_donut_bar(ch, colors, m):
    """V2: 2 big stats + donut + bar chart"""
    p, s, bg = colors
    stats = "".join(
        comp_stat_big(
            m["kpis"][i][0],
            m["kpis"][i][1],
            m["kpis"][i][2] or "前月比",
            m["kpis"][i][4],
            p if i % 2 == 0 else s,
        )
        for i in range(min(2, len(m["kpis"])))
    )
    html = (
        f'<div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">{stats}</div>'
        f'<div class="grid grid-cols-1 md:grid-cols-2 gap-5">'
        f"{comp_chart_box('dC1', '構成比', 240)}"
        f"{comp_chart_box('dC2', '月別推移', 240)}</div>"
    )
    pie_ds = [
        {
            "data": m["chart_pie"],
            "backgroundColor": [p, s, p + "80", s + "80", "#e5e7eb"],
            "borderWidth": 0,
        }
    ]
    bar_ds = [
        {
            "label": "実績",
            "data": m["chart1"][:6],
            "backgroundColor": p,
            "borderRadius": 6,
        }
    ]
    js = (
        js_chart("dC1", "doughnut", ["A", "B", "C", "D", "E"], pie_ds)
        + "\n"
        + js_chart("dC2", "bar", MONTHS[:6], bar_ds)
    )
    return {
        "id": "dashboard",
        "title": "ダッシュボード",
        "desc": "統計サマリー",
        "icon": "layout-dashboard",
        "html": html,
        "js": js,
    }


def dash_rings_radar(ch, colors, m):
    """V3: Progress rings + radar chart"""
    p, s, bg = colors
    rings = "".join(
        comp_progress_ring(m["rng"].randint(40, 95), label, p if i % 2 == 0 else s)
        for i, label in enumerate(["品質", "効率", "遵守", "満足度"])
    )
    html = (
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-5 mb-6">'
        f'<div class="card p-5 flex justify-center">{rings.split("</div></div>")[0]}</div></div></div>'
        f'<div class="card p-5 flex justify-center">{comp_progress_ring(m["rng"].randint(40, 95), "効率", s)}</div>'
        f'<div class="card p-5 flex justify-center">{comp_progress_ring(m["rng"].randint(40, 95), "遵守", p)}</div>'
        f'<div class="card p-5 flex justify-center">{comp_progress_ring(m["rng"].randint(40, 95), "満足度", s)}</div>'
        f"</div>"
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f"{comp_chart_box('dC1', '能力マップ', 280)}"
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">最近のアクティビティ</h3>'
        f'<div class="space-y-3">{comp_activities(m["activities"], p, 5)}</div></div></div>'
    )
    radar_ds = [
        {
            "label": "現在",
            "data": m["chart2"],
            "borderColor": p,
            "backgroundColor": p + "20",
            "pointBackgroundColor": p,
        }
    ]
    js = js_chart(
        "dC1", "radar", ["営業", "品質", "効率", "技術", "CS", "管理"], radar_ds
    )
    return {
        "id": "dashboard",
        "title": "ダッシュボード",
        "desc": "パフォーマンス概要",
        "icon": "layout-dashboard",
        "html": html,
        "js": js,
    }


def dash_metrics_area(ch, colors, m):
    """V4: Metrics row + area chart + bottom cards"""
    p, s, bg = colors
    kpis = "".join(comp_kpi(*k, p) for k in m["kpis"][:4])
    html = (
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">{kpis}</div>'
        f"{comp_chart_box('dC1', 'トレンド分析', 300)}"
        f'<div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-5">'
        f"{comp_chart_box('dC2', 'カテゴリ別', 200)}"
        f"{comp_chart_box('dC3', '比較', 200)}"
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">アラート</h3>'
        f'<div class="space-y-2">{"".join(f"""<div class="flex items-center gap-2 p-2 rounded-lg bg-amber-50"><i data-lucide="alert-triangle" class="w-4 h-4 text-amber-500"></i><span class="text-[12px] text-amber-700">{a["user"]} — {a["text"]}</span></div>""" for a in m["activities"][:3])}</div></div></div>'
    )
    area_ds = [
        {
            "label": "実績",
            "data": m["chart1"],
            "borderColor": p,
            "backgroundColor": p + "20",
            "fill": True,
            "tension": 0.4,
            "pointRadius": 0,
        }
    ]
    pie_ds = [
        {
            "data": m["chart_pie"][:4],
            "backgroundColor": [p, s, p + "60", "#e5e7eb"],
            "borderWidth": 0,
        }
    ]
    bar_ds = [
        {
            "label": "今期",
            "data": m["chart1"][:6],
            "backgroundColor": p,
            "borderRadius": 4,
        },
        {
            "label": "前期",
            "data": m["chart2"],
            "backgroundColor": "#e5e7eb",
            "borderRadius": 4,
        },
    ]
    js = (
        js_chart("dC1", "line", MONTHS, area_ds)
        + "\n"
        + js_chart("dC2", "doughnut", ["A", "B", "C", "D"], pie_ds)
        + "\n"
        + js_chart("dC3", "bar", MONTHS[:6], bar_ds, True)
    )
    return {
        "id": "dashboard",
        "title": "ダッシュボード",
        "desc": "トレンドとアラート",
        "icon": "layout-dashboard",
        "html": html,
        "js": js,
    }


def dash_timeline_hbar(ch, colors, m):
    """V5: Timeline + horizontal bars"""
    p, s, bg = colors
    tl = comp_timeline_items(m["timeline"][:4], p)
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-3 gap-5 mb-6">'
        f'<div class="card p-5 lg:col-span-2">'
        f'<h3 class="font-semibold text-[13px] text-gray-700 mb-4">進捗タイムライン</h3>{tl}</div>'
        f"{comp_chart_box('dC1', 'カテゴリ別実績', 280)}</div>"
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-4">'
        f"{''.join(comp_kpi(*k, p) for k in m['kpis'][:4])}</div>"
    )
    hbar_ds = [
        {"label": "実績", "data": m["chart2"], "backgroundColor": p, "borderRadius": 4}
    ]
    js = js_chart(
        "dC1",
        "bar",
        ["営業", "設計", "製造", "品質", "管理", "CS"],
        hbar_ds,
        horizontal=True,
    )
    return {
        "id": "dashboard",
        "title": "ダッシュボード",
        "desc": "進捗とカテゴリ分析",
        "icon": "layout-dashboard",
        "html": html,
        "js": js,
    }


def dash_table_chart(ch, colors, m):
    """V6: Summary table + chart side by side"""
    p, s, bg = colors
    kpis = "".join(comp_kpi(*k, p) for k in m["kpis"][:4])
    tbl = comp_table(
        "dTbl", ["ID", "担当", "部門", "状態", "日付", "金額"], m["rows"][:6], p
    )
    html = (
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">{kpis}</div>'
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f"<div>{tbl}</div>"
        f"{comp_chart_box('dC1', '推移', 280)}</div>"
    )
    ds = [
        {
            "label": "実績",
            "data": m["chart1"],
            "borderColor": p,
            "backgroundColor": p + "15",
            "fill": True,
            "tension": 0.4,
            "pointRadius": 3,
            "pointBackgroundColor": p,
        }
    ]
    js = JS_SORT_TABLE + js_chart("dC1", "line", MONTHS, ds)
    return {
        "id": "dashboard",
        "title": "ダッシュボード",
        "desc": "データと推移",
        "icon": "layout-dashboard",
        "html": html,
        "js": js,
    }


DASHBOARD_VARIANTS = [
    dash_kpi_line_activity,
    dash_stats_donut_bar,
    dash_rings_radar,
    dash_metrics_area,
    dash_timeline_hbar,
    dash_table_chart,
]


# ════════════════════════════════════════════════════════════
#  FEATURE PAGE VARIANTS (15 types)
# ════════════════════════════════════════════════════════════


def feat_kanban(ch, colors, m):
    p, s, bg = colors
    cols_html = ""
    col_colors = {
        "未着手": "#94a3b8",
        "進行中": p,
        "レビュー": "#f59e0b",
        "完了": "#10b981",
    }
    for col_name, cards in m["kanban"].items():
        cc = col_colors.get(col_name, "#6b7280")
        cards_html = ""
        for card in cards[:4]:
            pri_c = {
                "高": "bg-red-50 text-red-600",
                "中": "bg-amber-50 text-amber-700",
                "低": "bg-gray-100 text-gray-500",
            }
            cards_html += (
                f'<div class="bg-white rounded-lg p-3 border shadow-sm hover:shadow-md transition-shadow cursor-move" draggable="true">'
                f'<p class="text-[13px] font-medium text-gray-700">{card["title"]}</p>'
                f'<div class="flex items-center justify-between mt-2">'
                f'<span class="text-[11px] px-1.5 py-0.5 rounded {pri_c.get(card["priority"], "")}">{card["priority"]}</span>'
                f'<div class="flex items-center gap-1"><span class="text-[11px] text-gray-400">{card["due"]}</span>'
                f'<div class="w-5 h-5 rounded-full text-white text-[9px] flex items-center justify-center" style="background:{p}">{card["assignee"][0]}</div>'
                f"</div></div></div>"
            )
        cols_html += (
            f'<div class="kanban-col min-w-[260px] flex-1">'
            f'<div class="flex items-center gap-2 mb-3">'
            f'<div class="w-2 h-2 rounded-full" style="background:{cc}"></div>'
            f'<span class="text-[13px] font-semibold text-gray-700">{col_name}</span>'
            f'<span class="text-[11px] bg-gray-100 text-gray-500 px-1.5 rounded-full">{len(cards)}</span></div>'
            f'<div class="kanban-cards space-y-2.5 min-h-[200px] p-1">{cards_html}</div></div>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5">'
        f"{comp_search('kSearch', 'タスクを検索...')}"
        f"{comp_btn('新規タスク', p, 'plus')}</div>"
        f'<div class="flex gap-4 overflow-x-auto pb-4">{cols_html}</div>'
    )
    js = """
document.querySelectorAll('[draggable]').forEach(c=>{c.addEventListener('dragstart',e=>{e.dataTransfer.setData('text',c.innerHTML);c.classList.add('opacity-40')});c.addEventListener('dragend',()=>c.classList.remove('opacity-40'))});
document.querySelectorAll('.kanban-cards').forEach(col=>{col.addEventListener('dragover',e=>e.preventDefault());col.addEventListener('drop',e=>{e.preventDefault();const d=document.createElement('div');d.className='bg-white rounded-lg p-3 border shadow-sm hover:shadow-md transition-shadow cursor-move';d.draggable=true;d.innerHTML=e.dataTransfer.getData('text');col.appendChild(d)})});
"""
    return {
        "id": "feature",
        "title": "ボード",
        "desc": "タスク管理",
        "icon": "columns",
        "html": html,
        "js": js,
    }


def _day_headers():
    return "".join(
        f'<div class="text-center text-[11px] font-semibold text-gray-400 py-1">{d}</div>'
        for d in ["月", "火", "水", "木", "金", "土", "日"]
    )


def feat_calendar(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    # Build month grid
    cells = ""
    for d in range(1, 32):
        has_event = rng.randint(0, 3) == 0
        ev = (
            f'<div class="w-1.5 h-1.5 rounded-full mx-auto mt-0.5" style="background:{p}"></div>'
            if has_event
            else ""
        )
        today = "ring-2 ring-offset-1 font-bold" if d == 9 else ""
        cells += f'<div class="p-1.5 text-center rounded-lg hover:bg-gray-50 cursor-pointer {today}" style="{"ring-color:" + p if d == 9 else ""}"><span class="text-[12px] text-gray-600">{d}</span>{ev}</div>'
    events = ""
    for i in range(5):
        t = f"{rng.randint(9, 18)}:{rng.choice(['00', '30'])}"
        events += (
            f'<div class="flex items-center gap-3 p-3 rounded-lg hover:bg-gray-50 cursor-pointer transition-colors">'
            f'<div class="w-1 h-10 rounded-full" style="background:{p if i % 2 == 0 else s}"></div>'
            f'<div><p class="text-[13px] font-medium text-gray-700">予定{i + 1} — {NAMES[rng.randint(0, 5)]}</p>'
            f'<p class="text-[11px] text-gray-400">{t} 〜 {int(t.split(":")[0]) + 1}:00</p></div></div>'
        )
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-3 gap-5">'
        f'<div class="lg:col-span-2 card p-5">'
        f'<div class="flex items-center justify-between mb-4">'
        f"{comp_btn_outline('前月', p, 'chevron-left')}"
        f'<h3 class="font-semibold text-[15px]">2026年3月</h3>'
        f"{comp_btn_outline('翌月', p, 'chevron-right')}</div>"
        f'<div class="grid grid-cols-7 gap-1 mb-2">{_day_headers()}</div>'
        f'<div class="grid grid-cols-7 gap-1">{cells}</div></div>'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">今日の予定</h3>'
        f'<div class="space-y-2">{events}</div></div></div>'
    )
    return {
        "id": "feature",
        "title": "スケジュール",
        "desc": "予定管理",
        "icon": "calendar",
        "html": html,
        "js": "",
    }


def feat_form_wizard(ch, colors, m):
    p, s, bg = colors
    steps = ["基本情報", "詳細入力", "確認", "完了"]
    step_indicators = ""
    for i, st in enumerate(steps):
        active = "font-semibold" if i == 0 else "text-gray-400"
        bg_c = p if i == 0 else "#e5e7eb"
        tc = "text-white" if i == 0 else "text-gray-400"
        connector = (
            '<div class="w-8 h-0.5 bg-gray-200"></div>' if i < len(steps) - 1 else ""
        )
        step_indicators += (
            f'<div class="flex items-center gap-2 step-ind" data-step="{i}">'
            f'<div class="w-7 h-7 rounded-full flex items-center justify-center text-[12px] {tc}" style="background:{bg_c}">{i + 1}</div>'
            f'<span class="text-[12px] {active} hidden sm:inline">{st}</span>'
            f"{connector}</div>"
        )
    fields1 = (
        comp_form_field("名称", "text", "入力してください")
        + comp_form_field(
            "カテゴリ", "select", options=["カテゴリA", "カテゴリB", "カテゴリC"]
        )
        + comp_form_field("日付", "date")
        + comp_form_field("担当者", "text", "担当者名")
    )
    fields2 = (
        comp_form_field("詳細説明", "textarea", "詳細を入力")
        + comp_form_field("金額", "number", "0")
        + comp_form_field("優先度", "select", options=["高", "中", "低"])
        + comp_form_field("備考", "textarea", "その他")
    )
    html = (
        f'<div class="card p-6">'
        f'<div class="flex items-center justify-center gap-4 mb-8">{step_indicators}</div>'
        f'<div id="wizStep0" class="wiz-step space-y-4">{fields1}'
        f'<div class="flex justify-end pt-4">{comp_btn("次へ", p, "arrow-right", "wizNext()")}</div></div>'
        f'<div id="wizStep1" class="wiz-step space-y-4 hidden">{fields2}'
        f'<div class="flex justify-between pt-4">{comp_btn_outline("戻る", p, "arrow-left", "wizPrev()")}{comp_btn("次へ", p, "arrow-right", "wizNext()")}</div></div>'
        f'<div id="wizStep2" class="wiz-step hidden"><div class="text-center py-8"><i data-lucide="file-check" class="w-12 h-12 mx-auto mb-3" style="color:{p}"></i>'
        f'<p class="text-[15px] font-semibold text-gray-700">入力内容をご確認ください</p>'
        f'<p class="text-[13px] text-gray-400 mt-1">問題なければ送信してください</p></div>'
        f'<div class="flex justify-between pt-4">{comp_btn_outline("戻る", p, "arrow-left", "wizPrev()")}{comp_btn("送信", p, "send", "wizNext()")}</div></div>'
        f'<div id="wizStep3" class="wiz-step hidden"><div class="text-center py-12"><i data-lucide="check-circle" class="w-16 h-16 mx-auto mb-4 text-emerald-500"></i>'
        f'<p class="text-[18px] font-bold text-gray-700">送信完了</p>'
        f'<p class="text-[13px] text-gray-400 mt-2">正常に処理されました</p></div></div></div>'
    )
    js = f"""
let wizCur=0;
function wizGo(n){{document.querySelectorAll('.wiz-step').forEach((s,i)=>s.classList.toggle('hidden',i!==n));
document.querySelectorAll('.step-ind').forEach((s,i)=>{{const c=s.querySelector('div');c.style.background=i<=n?'{p}':'#e5e7eb';c.className=c.className.replace(/text-\\w+/g,i<=n?'text-white':'text-gray-400')+' w-7 h-7 rounded-full flex items-center justify-center text-[12px]'}});
wizCur=n;if(typeof lucide!=='undefined')lucide.createIcons()}}
function wizNext(){{if(wizCur<3)wizGo(wizCur+1)}}
function wizPrev(){{if(wizCur>0)wizGo(wizCur-1)}}
"""
    return {
        "id": "feature",
        "title": "入力フォーム",
        "desc": "ステップ形式入力",
        "icon": "file-edit",
        "html": html,
        "js": js,
    }


def feat_checklist(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    groups = ["基本チェック", "安全確認", "品質検証", "最終確認"]
    items_html = ""
    total = 0
    checked = 0
    for gi, group in enumerate(groups):
        items = ""
        for j in range(rng.randint(3, 6)):
            c = rng.randint(0, 1)
            total += 1
            checked += c
            chk = "checked" if c else ""
            items += (
                f'<label class="flex items-center gap-3 p-2.5 rounded-lg hover:bg-gray-50 cursor-pointer transition-colors">'
                f'<input type="checkbox" {chk} onchange="updateCL()" class="w-[18px] h-[18px] rounded accent-current" style="accent-color:{p}">'
                f'<span class="text-[13px] text-gray-700">確認項目 {gi + 1}-{j + 1}</span></label>'
            )
        items_html += (
            f'<div class="card p-4 mb-3"><div class="flex items-center gap-2 mb-2">'
            f'<i data-lucide="check-square" class="w-4 h-4" style="color:{p}"></i>'
            f'<h4 class="font-semibold text-[13px] text-gray-700">{group}</h4></div>'
            f'<div class="space-y-0.5">{items}</div></div>'
        )
    pct = round(checked / max(total, 1) * 100)
    html = (
        f'<div class="card p-5 mb-5"><div class="flex items-center justify-between mb-3">'
        f'<div><span class="text-[13px] text-gray-500">完了率</span>'
        f'<span id="clPct" class="text-lg font-bold ml-2" style="color:{p}">{pct}%</span></div>'
        f"{comp_btn('完了報告', p, 'send')}</div>"
        f'<div class="w-full bg-gray-100 rounded-full h-2.5">'
        f'<div id="clBar" class="h-2.5 rounded-full transition-all" style="width:{pct}%;background:{p}"></div></div></div>'
        f"{items_html}"
    )
    js = """
function updateCL(){const all=document.querySelectorAll('#page-feature input[type=checkbox]');
const c=[...all].filter(x=>x.checked).length;const pct=Math.round(c/all.length*100);
document.getElementById('clPct').textContent=pct+'%';
document.getElementById('clBar').style.width=pct+'%';}
"""
    return {
        "id": "feature",
        "title": "チェックリスト",
        "desc": "確認・検査",
        "icon": "check-square",
        "html": html,
        "js": js,
    }


def feat_map(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    # Simulated map with grid
    pins = ""
    locations = []
    for i in range(8):
        x = rng.randint(5, 85)
        y = rng.randint(5, 85)
        name = f"拠点{chr(65 + i)}"
        status = ["稼働中", "移動中", "待機中", "要対応"][rng.randint(0, 3)]
        sc = {
            "稼働中": "bg-emerald-500",
            "移動中": "bg-blue-500",
            "待機中": "bg-gray-400",
            "要対応": "bg-red-500",
        }
        pins += (
            f'<div class="absolute w-6 h-6 rounded-full border-2 border-white shadow-md flex items-center justify-center text-[9px] text-white cursor-pointer hover:scale-125 transition-transform {sc.get(status, "bg-gray-400")}" '
            f'style="left:{x}%;top:{y}%" title="{name}">{chr(65 + i)}</div>'
        )
        locations.append((name, status, f"{rng.randint(1, 50)}km"))
    loc_list = ""
    for name, status, dist in locations:
        sc2 = {"稼働中": "green", "移動中": "blue", "待機中": "gray", "要対応": "red"}
        loc_list += (
            f'<div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg cursor-pointer transition-colors">'
            f'<div class="flex items-center gap-3"><i data-lucide="map-pin" class="w-4 h-4" style="color:{p}"></i>'
            f'<div><p class="text-[13px] font-medium text-gray-700">{name}</p>'
            f'<p class="text-[11px] text-gray-400">{dist}</p></div></div>'
            f"{comp_badge(status, sc2.get(status, 'gray'))}</div>"
        )
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-3 gap-5">'
        f'<div class="lg:col-span-2 card p-4">'
        f'<div class="relative bg-gradient-to-br from-blue-50 to-green-50 rounded-lg overflow-hidden" style="height:420px">'
        f'<div class="absolute inset-0 opacity-10" style="background:repeating-linear-gradient(0deg,{p}22 0,{p}22 1px,transparent 1px,transparent 40px),repeating-linear-gradient(90deg,{p}22 0,{p}22 1px,transparent 1px,transparent 40px)"></div>'
        f"{pins}</div></div>"
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">拠点一覧</h3>'
        f'<div class="space-y-1">{loc_list}</div></div></div>'
    )
    return {
        "id": "feature",
        "title": "マップ",
        "desc": "拠点・ルート管理",
        "icon": "map-pin",
        "html": html,
        "js": "",
    }


def feat_inventory(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    cards = ""
    for i in range(12):
        name = f"品目-{rng.randint(100, 999)}"
        stock = rng.randint(0, 200)
        threshold = rng.randint(10, 50)
        level = (
            "emerald"
            if stock > threshold * 2
            else "amber"
            if stock > threshold
            else "red"
        )
        pct = min(100, round(stock / max(threshold * 3, 1) * 100))
        cards += (
            f'<div class="card p-4 hover:shadow-md transition-shadow cursor-pointer" data-search="{name}">'
            f'<div class="flex items-center justify-between mb-3">'
            f'<p class="text-[13px] font-medium text-gray-700">{name}</p>'
            f"{comp_badge('低在庫', 'red') if stock <= threshold else ''}</div>"
            f'<div class="text-2xl font-bold text-gray-800">{stock}<span class="text-[12px] font-normal text-gray-400 ml-1">個</span></div>'
            f'<div class="w-full bg-gray-100 rounded-full h-1.5 mt-3">'
            f'<div class="h-1.5 rounded-full bg-{level}-500" style="width:{pct}%"></div></div>'
            f'<p class="text-[11px] text-gray-400 mt-1.5">発注点: {threshold}個</p></div>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5 gap-3">'
        f'<div class="flex-1">{comp_search("invSearch", "品目を検索...")}</div>'
        f"{comp_btn('入荷登録', p, 'plus')}</div>"
        f'<div id="invGrid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">{cards}</div>'
    )
    js = js_filter("invSearch", "invGrid")
    return {
        "id": "feature",
        "title": "在庫管理",
        "desc": "在庫状況・発注",
        "icon": "package",
        "html": html,
        "js": js,
    }


def feat_timeline(ch, colors, m):
    p, s, bg = colors
    tl = comp_timeline_items(m["timeline"], p)
    rng = m["rng"]
    schedule = ""
    for i in range(5):
        w = rng.randint(15, 40)
        l = rng.randint(0, 60)
        schedule += (
            f'<div class="flex items-center gap-3 group">'
            f'<span class="text-[11px] text-gray-400 w-20 shrink-0">工程{i + 1}</span>'
            f'<div class="flex-1 h-7 bg-gray-50 rounded relative">'
            f'<div class="absolute h-full rounded group-hover:opacity-80 transition-opacity" style="left:{l}%;width:{w}%;background:{p if i % 2 == 0 else s}"></div></div>'
            f'<span class="text-[11px] text-gray-400 w-16 text-right">{rng.randint(5, 30)}日</span></div>'
        )
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">進捗タイムライン</h3>{tl}</div>'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">ガントチャート</h3>'
        f'<div class="space-y-3">{schedule}</div></div></div>'
    )
    return {
        "id": "feature",
        "title": "タイムライン",
        "desc": "進捗・工程管理",
        "icon": "git-commit",
        "html": html,
        "js": "",
    }


def feat_documents(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    categories = ["契約書", "報告書", "設計書", "議事録", "マニュアル"]
    icons_map = {
        "契約書": "file-text",
        "報告書": "file-bar-chart",
        "設計書": "file-cog",
        "議事録": "file-pen-line",
        "マニュアル": "book-open",
    }
    docs = ""
    for i in range(10):
        cat = categories[rng.randint(0, len(categories) - 1)]
        docs += (
            f'<div class="card p-4 hover:shadow-md transition-shadow cursor-pointer flex items-center gap-4" data-search="{cat} 文書{i + 1}">'
            f'<div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:{bg}">'
            f'<i data-lucide="{icons_map.get(cat, "file")}" class="w-5 h-5" style="color:{p}"></i></div>'
            f'<div class="flex-1 min-w-0"><p class="text-[13px] font-medium text-gray-700 truncate">{cat}_{rng.randint(2024, 2026)}_{rng.randint(1, 12):02d}_{i + 1}</p>'
            f'<p class="text-[11px] text-gray-400">{cat} · {rng.randint(50, 500)}KB · {rng.randint(1, 28)}/{rng.randint(1, 12)}更新</p></div>'
            f'<i data-lucide="download" class="w-4 h-4 text-gray-300 hover:text-gray-600 cursor-pointer shrink-0"></i></div>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5 gap-3">'
        f'<div class="flex-1">{comp_search("docSearch", "文書を検索...")}</div>'
        f"{comp_btn('アップロード', p, 'upload')}</div>"
        f'<div class="flex gap-2 mb-4">{"".join(f"""<button class="text-[12px] px-3 py-1.5 rounded-lg border hover:bg-gray-50 cursor-pointer transition-colors">{c}</button>""" for c in ["全て"] + categories)}</div>'
        f'<div id="docList" class="space-y-2">{docs}</div>'
    )
    js = js_filter("docSearch", "docList")
    return {
        "id": "feature",
        "title": "文書管理",
        "desc": "ファイル・書類管理",
        "icon": "folder",
        "html": html,
        "js": js,
    }


def feat_matrix(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    criteria = ["品質", "コスト", "納期", "サポート", "機能性", "拡張性"]
    options = [f"オプション{chr(65 + i)}" for i in range(4)]
    header = (
        '<th class="px-4 py-3 text-[11px] font-semibold text-gray-500">評価項目</th>'
        + "".join(
            f'<th class="px-4 py-3 text-[13px] font-medium text-center" style="color:{p}">{o}</th>'
            for o in options
        )
    )
    rows = ""
    totals = [0] * 4
    for cr in criteria:
        cells = ""
        for j in range(4):
            score = rng.randint(1, 5)
            totals[j] += score
            stars = "".join(
                f'<span style="color:{p if k < score else "#e5e7eb"}">★</span>'
                for k in range(5)
            )
            cells += f'<td class="px-4 py-3 text-center text-[13px]">{stars}</td>'
        rows += f'<tr class="border-b border-gray-50"><td class="px-4 py-3 text-[13px] font-medium text-gray-700">{cr}</td>{cells}</tr>'
    total_cells = "".join(
        f'<td class="px-4 py-3 text-center font-bold text-[15px]" style="color:{p}">{t}</td>'
        for t in totals
    )
    rows += f'<tr class="bg-gray-50/50 border-t-2"><td class="px-4 py-3 text-[13px] font-bold text-gray-700">合計</td>{total_cells}</tr>'
    best = options[totals.index(max(totals))]
    html = (
        f'<div class="card p-5 mb-5"><div class="flex items-center gap-2 mb-1">'
        f'<i data-lucide="award" class="w-5 h-5" style="color:{p}"></i>'
        f'<span class="text-[13px] text-gray-500">推奨:</span>'
        f'<span class="font-bold text-[15px]" style="color:{p}">{best}</span></div></div>'
        f'<div class="card overflow-hidden"><table class="w-full"><thead class="bg-gray-50/80 border-b"><tr>{header}</tr></thead>'
        f"<tbody>{rows}</tbody></table></div>"
    )
    return {
        "id": "feature",
        "title": "比較マトリクス",
        "desc": "評価・比較分析",
        "icon": "grid",
        "html": html,
        "js": "",
    }


def feat_calculator(ch, colors, m):
    p, s, bg = colors
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-5">入力パラメータ</h3>'
        f'<div class="space-y-4">'
        f"{comp_form_field('売上高（万円）', 'number', '10000')}"
        f"{comp_form_field('原価率（%）', 'number', '60')}"
        f"{comp_form_field('販管費（万円）', 'number', '2000')}"
        f"{comp_form_field('人件費（万円）', 'number', '1500')}"
        f'<div class="pt-2">{comp_btn("計算する", p, "calculator", "calcProfit()")}</div>'
        f"</div></div>"
        f'<div class="space-y-4">'
        f'<div class="card p-5" id="calcResult">'
        f'<h3 class="font-semibold text-[13px] text-gray-700 mb-4">計算結果</h3>'
        f'<div class="space-y-3">'
        f'<div class="flex justify-between py-2 border-b"><span class="text-[13px] text-gray-500">粗利</span><span id="rGross" class="font-bold" style="color:{p}">—</span></div>'
        f'<div class="flex justify-between py-2 border-b"><span class="text-[13px] text-gray-500">粗利率</span><span id="rGrossRate" class="font-bold" style="color:{p}">—</span></div>'
        f'<div class="flex justify-between py-2 border-b"><span class="text-[13px] text-gray-500">営業利益</span><span id="rOp" class="font-bold" style="color:{p}">—</span></div>'
        f'<div class="flex justify-between py-2"><span class="text-[13px] text-gray-500">営業利益率</span><span id="rOpRate" class="font-bold" style="color:{p}">—</span></div>'
        f"</div></div>"
        f"{comp_chart_box('calcChart', '利益構成', 200)}"
        f"</div></div>"
    )
    js = f"""
function calcProfit(){{
const rev=parseFloat(document.querySelector('[name="売上高（万円）"]').value)||0;
const cr=parseFloat(document.querySelector('[name="原価率（%）"]').value)||0;
const sg=parseFloat(document.querySelector('[name="販管費（万円）"]').value)||0;
const hr=parseFloat(document.querySelector('[name="人件費（万円）"]').value)||0;
const cost=rev*cr/100;const gross=rev-cost;const op=gross-sg-hr;
document.getElementById('rGross').textContent=gross.toLocaleString()+'万円';
document.getElementById('rGrossRate').textContent=(gross/rev*100).toFixed(1)+'%';
document.getElementById('rOp').textContent=op.toLocaleString()+'万円';
document.getElementById('rOpRate').textContent=(op/rev*100).toFixed(1)+'%';
const el=document.getElementById('calcChart');const old=charts.findIndex(c=>c.canvas===el);if(old>=0)charts[old].destroy();
charts.push(new Chart(el,{{type:'doughnut',data:{{labels:['原価','販管費','人件費','営業利益'],datasets:[{{data:[cost,sg,hr,Math.max(0,op)],backgroundColor:['{p}','{s}','{p}80','#10b981'],borderWidth:0}}]}},options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{display:true,position:'bottom',labels:{{font:{{size:11}}}}}}}}}}}}));
}}"""
    return {
        "id": "feature",
        "title": "シミュレーター",
        "desc": "原価・利益計算",
        "icon": "calculator",
        "html": html,
        "js": js,
    }


def feat_chat(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    msgs = ""
    for i in range(8):
        is_me = i % 3 == 0
        name = "自分" if is_me else NAMES[rng.randint(0, 5)]
        align = "justify-end" if is_me else "justify-start"
        bubble_bg = p if is_me else "#f3f4f6"
        tc = "text-white" if is_me else "text-gray-700"
        texts = [
            "了解しました",
            "確認お願いします",
            "添付ファイルを送りました",
            "MTGの件、問題ありません",
            "対応中です",
            "完了しました",
            "ありがとうございます",
            "進捗報告です",
        ]
        avatar = "" if is_me else f'<div class="w-7 h-7 rounded-full flex items-center justify-center text-[10px] text-white shrink-0" style="background:{s}">{name[0]}</div>'
        ta = "text-right" if is_me else ""
        ago = rng.randint(1, 59)
        msgs += (
            f'<div class="flex {align} gap-2">{avatar}'
            f'<div class="max-w-[70%]"><div class="rounded-2xl px-4 py-2.5 {tc}" style="background:{bubble_bg}">'
            f'<p class="text-[13px]">{texts[i]}</p></div>'
            f'<p class="text-[10px] text-gray-400 mt-1 {ta}">{name} \u00b7 {ago}\u5206\u524d</p></div></div>'
        )
    html = (
        f'<div class="card flex flex-col" style="height:calc(100vh - 180px)">'
        f'<div class="p-4 border-b flex items-center gap-3">'
        f'<div class="w-8 h-8 rounded-full flex items-center justify-center text-white text-[12px]" style="background:{p}">G</div>'
        f'<div><p class="text-[13px] font-semibold">プロジェクトチャンネル</p>'
        f'<p class="text-[11px] text-gray-400">{rng.randint(3, 15)}人のメンバー</p></div></div>'
        f'<div class="flex-1 overflow-y-auto p-4 space-y-4">{msgs}</div>'
        f'<div class="p-3 border-t flex gap-2">'
        f'<input type="text" placeholder="メッセージを入力..." class="flex-1 px-4 py-2.5 text-[13px] border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-100">'
        f"{comp_btn('送信', p, 'send')}</div></div>"
    )
    return {
        "id": "feature",
        "title": "メッセージ",
        "desc": "チーム連絡",
        "icon": "message-square",
        "html": html,
        "js": "",
    }


def feat_crm(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    stages = [("リード", 3), ("提案", 2), ("交渉", 2), ("成約", 1)]
    pipeline = ""
    for stage, count in stages:
        cards = ""
        for j in range(count):
            amount = rng.randint(100, 2000)
            cards += (
                f'<div class="bg-white rounded-lg p-3 border shadow-sm hover:shadow-md transition-shadow cursor-pointer">'
                f'<p class="text-[13px] font-medium text-gray-700">{NAMES[rng.randint(0, 7)]}商事</p>'
                f'<p class="text-[11px] text-gray-400 mt-1">¥{amount:,}万</p>'
                f'<div class="flex items-center gap-1 mt-2">'
                f'<div class="w-5 h-5 rounded-full text-white text-[9px] flex items-center justify-center" style="background:{p}">{NAMES[rng.randint(0, 5)][0]}</div>'
                f'<span class="text-[11px] text-gray-400">{rng.randint(1, 30)}日前</span></div></div>'
            )
        pipeline += (
            f'<div class="flex-1 min-w-[200px]">'
            f'<div class="flex items-center gap-2 mb-3"><span class="text-[13px] font-semibold text-gray-700">{stage}</span>'
            f'<span class="text-[11px] bg-gray-100 text-gray-500 px-1.5 rounded-full">{count}</span></div>'
            f'<div class="space-y-2">{cards}</div></div>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5">'
        f"{comp_search('crmSearch', '顧客を検索...')}"
        f"{comp_btn('新規顧客', p, 'plus')}</div>"
        f'<div class="flex gap-4 overflow-x-auto pb-4">{pipeline}</div>'
    )
    return {
        "id": "feature",
        "title": "顧客管理",
        "desc": "パイプライン",
        "icon": "building-2",
        "html": html,
        "js": "",
    }


def feat_hr(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    roles = [
        "エンジニア",
        "デザイナー",
        "マネージャー",
        "営業",
        "CS",
        "マーケ",
        "人事",
        "経理",
    ]
    members = ""
    for i in range(8):
        role = roles[rng.randint(0, len(roles) - 1)]
        skill = rng.randint(60, 100)
        members += (
            f'<div class="card p-4 hover:shadow-md transition-shadow cursor-pointer" data-search="{NAMES[i]} {role}">'
            f'<div class="flex items-center gap-3 mb-3">'
            f'<div class="w-10 h-10 rounded-full flex items-center justify-center text-white text-[13px] font-medium" style="background:{p}">{NAMES[i][0]}</div>'
            f'<div><p class="text-[13px] font-semibold text-gray-700">{NAMES[i]}</p>'
            f'<p class="text-[11px] text-gray-400">{role}</p></div></div>'
            f'<div class="flex items-center gap-2">'
            f'<div class="flex-1 bg-gray-100 rounded-full h-1.5"><div class="h-1.5 rounded-full" style="width:{skill}%;background:{p}"></div></div>'
            f'<span class="text-[11px] text-gray-500">{skill}%</span></div></div>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5 gap-3">'
        f'<div class="flex-1">{comp_search("hrSearch", "メンバーを検索...")}</div>'
        f"{comp_btn('メンバー追加', p, 'user-plus')}</div>"
        f'<div id="hrGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">{members}</div>'
    )
    js = js_filter("hrSearch", "hrGrid")
    return {
        "id": "feature",
        "title": "人材管理",
        "desc": "メンバー・スキル",
        "icon": "users",
        "html": html,
        "js": js,
    }


def feat_workflow(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    steps = ["申請", "部門承認", "経理確認", "最終承認", "完了"]
    current = rng.randint(1, 3)
    steps_html = ""
    for i, step in enumerate(steps):
        if i < current:
            circle = f'<div class="w-8 h-8 rounded-full flex items-center justify-center text-white text-[12px]" style="background:{p}"><i data-lucide="check" class="w-4 h-4"></i></div>'
        elif i == current:
            circle = f'<div class="w-8 h-8 rounded-full flex items-center justify-center text-white text-[12px] animate-pulse" style="background:#f59e0b">{i + 1}</div>'
        else:
            circle = f'<div class="w-8 h-8 rounded-full flex items-center justify-center text-gray-400 text-[12px] bg-gray-100">{i + 1}</div>'
        connector = (
            f'<div class="flex-1 h-0.5 mx-2" style="background:{p if i < current else "#e5e7eb"}"></div>'
            if i < len(steps) - 1
            else ""
        )
        steps_html += (
            f'<div class="flex items-center flex-1">'
            f'<div class="flex flex-col items-center gap-1.5">{circle}'
            f'<span class="text-[11px] {"font-semibold" if i == current else "text-gray-400"}">{step}</span></div>'
            f"{connector}</div>"
        )
    history = ""
    for i in range(current):
        history += (
            f'<div class="flex items-center gap-3 p-3 bg-emerald-50/50 rounded-lg">'
            f'<i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i>'
            f'<div><p class="text-[13px] text-gray-700">{steps[i]} — {NAMES[rng.randint(0, 5)]}</p>'
            f'<p class="text-[11px] text-gray-400">{rng.randint(1, 5)}日前</p></div></div>'
        )
    html = (
        f'<div class="card p-6 mb-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-6">承認フロー</h3>'
        f'<div class="flex items-start px-4">{steps_html}</div></div>'
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">承認履歴</h3>'
        f'<div class="space-y-2">{history}</div></div>'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">現在のステップ</h3>'
        f'<div class="p-4 rounded-lg" style="background:{bg}">'
        f'<p class="font-semibold text-[13px]" style="color:{p}">{steps[current]}</p>'
        f'<p class="text-[12px] text-gray-500 mt-1">担当: {NAMES[rng.randint(0, 5)]}</p>'
        f'<div class="flex gap-2 mt-4">{comp_btn("承認", p, "check")}{comp_btn_outline("差戻", "#ef4444", "x")}</div>'
        f"</div></div></div>"
    )
    return {
        "id": "feature",
        "title": "ワークフロー",
        "desc": "承認・申請管理",
        "icon": "git-branch",
        "html": html,
        "js": "",
    }


def feat_analytics(ch, colors, m):
    p, s, bg = colors
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5 mb-5">'
        f"{comp_chart_box('anC1', 'トレンド分析', 260)}"
        f"{comp_chart_box('anC2', 'カテゴリ構成', 260)}</div>"
        f'<div class="grid grid-cols-1 lg:grid-cols-3 gap-5">'
        f"{comp_chart_box('anC3', '月次比較', 220)}"
        f"{comp_chart_box('anC4', '達成率', 220)}"
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">Key Insights</h3>'
        f'<div class="space-y-3">'
        f'<div class="p-3 rounded-lg bg-emerald-50"><p class="text-[12px] text-emerald-700">前月比 +12% の成長</p></div>'
        f'<div class="p-3 rounded-lg bg-amber-50"><p class="text-[12px] text-amber-700">カテゴリBが伸び悩み</p></div>'
        f'<div class="p-3 rounded-lg" style="background:{bg}"><p class="text-[12px]" style="color:{p}">Q2目標は達成見込み</p></div>'
        f"</div></div></div>"
    )
    line_ds = [
        {
            "label": "今期",
            "data": m["chart1"],
            "borderColor": p,
            "backgroundColor": p + "15",
            "fill": True,
            "tension": 0.4,
            "pointRadius": 3,
            "pointBackgroundColor": p,
        },
        {
            "label": "前期",
            "data": [max(5, v - m["rng"].randint(0, 20)) for v in m["chart1"]],
            "borderColor": "#d1d5db",
            "borderDash": [5, 5],
            "tension": 0.4,
            "pointRadius": 0,
        },
    ]
    pie_ds = [
        {
            "data": m["chart_pie"],
            "backgroundColor": [p, s, p + "60", s + "60", "#e5e7eb"],
            "borderWidth": 0,
        }
    ]
    bar_ds = [
        {"label": "今月", "data": m["chart2"], "backgroundColor": p, "borderRadius": 4},
        {
            "label": "先月",
            "data": [max(3, v - m["rng"].randint(0, 10)) for v in m["chart2"]],
            "backgroundColor": "#e5e7eb",
            "borderRadius": 4,
        },
    ]
    gauge_ds = [
        {
            "data": [m["rng"].randint(60, 95), 100 - m["rng"].randint(60, 95)],
            "backgroundColor": [p, "#f3f4f6"],
            "borderWidth": 0,
        }
    ]
    js = (
        js_chart("anC1", "line", MONTHS, line_ds, True)
        + "\n"
        + js_chart("anC2", "doughnut", ["A", "B", "C", "D", "E"], pie_ds)
        + "\n"
        + js_chart(
            "anC3", "bar", ["営業", "設計", "製造", "品質", "管理", "CS"], bar_ds, True
        )
        + "\n"
        + js_chart("anC4", "doughnut", ["達成", "残り"], gauge_ds)
    )
    return {
        "id": "feature",
        "title": "分析",
        "desc": "データ分析・BI",
        "icon": "bar-chart-3",
        "html": html,
        "js": js,
    }


FEATURE_MAP = {
    "kanban": feat_kanban,
    "calendar": feat_calendar,
    "form_wizard": feat_form_wizard,
    "checklist": feat_checklist,
    "map": feat_map,
    "inventory": feat_inventory,
    "timeline": feat_timeline,
    "documents": feat_documents,
    "matrix": feat_matrix,
    "calculator": feat_calculator,
    "chat": feat_chat,
    "crm": feat_crm,
    "hr": feat_hr,
    "workflow": feat_workflow,
    "analytics": feat_analytics,
}


# ════════════════════════════════════════════════════════════
#  DATA PAGE VARIANTS (4)
# ════════════════════════════════════════════════════════════


def data_table_view(ch, colors, m):
    """Full table with search and sort."""
    p, s, bg = colors
    tbl = comp_table(
        "dataTbl", ["ID", "担当", "部門", "ステータス", "更新日", "金額"], m["rows"], p
    )
    html = (
        f'<div class="flex items-center justify-between mb-5 gap-3">'
        f'<div class="flex-1 max-w-md">{comp_search("dataSearch", "データを検索...")}</div>'
        f'<div class="flex items-center gap-2">{comp_btn_outline("フィルタ", p, "filter")}{comp_btn("新規追加", p, "plus")}</div></div>'
        f"{tbl}"
        f'<div class="flex items-center justify-between mt-4"><span class="text-[12px] text-gray-400">{len(m["rows"])}件</span>'
        f'<div class="flex gap-1">{"".join(f"""<button class="w-8 h-8 rounded-lg text-[12px] {"font-bold text-white" if i == 0 else "text-gray-400 hover:bg-gray-100"} cursor-pointer transition-colors" {"style=background:" + p if i == 0 else ""}>{i + 1}</button>""" for i in range(3))}</div></div>'
    )
    js = JS_SORT_TABLE
    return {
        "id": "data",
        "title": "データ一覧",
        "desc": "検索・並べ替え",
        "icon": "list",
        "html": html,
        "js": js,
    }


def data_card_grid(ch, colors, m):
    """Card-style data browsing."""
    p, s, bg = colors
    cards = ""
    for r in m["rows"]:
        cards += (
            f'<div class="card p-4 hover:shadow-md transition-shadow cursor-pointer" data-search="{r[1]} {r[2]}">'
            f'<div class="flex items-center justify-between mb-3">'
            f'<span class="text-[11px] text-gray-400">{r[0]}</span>'
            f"{comp_badge(r[3], 'green' if r[3] == '完了' else 'blue' if r[3] == '進行中' else 'gray')}</div>"
            f'<p class="text-[13px] font-medium text-gray-700">{r[1]}</p>'
            f'<p class="text-[11px] text-gray-400 mt-1">{r[2]} · {r[4]}</p>'
            f'<p class="text-[13px] font-bold mt-2" style="color:{p}">{r[5]}</p></div>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5 gap-3">'
        f'<div class="flex-1 max-w-md">{comp_search("gridSearch", "検索...")}</div>'
        f"{comp_btn('新規追加', p, 'plus')}</div>"
        f'<div id="gridContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">{cards}</div>'
    )
    js = js_filter("gridSearch", "gridContainer")
    return {
        "id": "data",
        "title": "データ一覧",
        "desc": "カード表示",
        "icon": "layout-grid",
        "html": html,
        "js": js,
    }


def data_split_view(ch, colors, m):
    """Split: list left, detail right."""
    p, s, bg = colors
    items = ""
    for i, r in enumerate(m["rows"]):
        active = "border-l-2" if i == 0 else ""
        items += (
            f'<div class="flex items-center justify-between p-3 hover:bg-gray-50 cursor-pointer transition-colors {active}" '
            f'style="{"border-left-color:" + p if i == 0 else ""}" '
            f"onclick=\"selectItem(this,'{p}')\">"
            f'<div><p class="text-[13px] font-medium text-gray-700">{r[1]}</p>'
            f'<p class="text-[11px] text-gray-400">{r[0]} · {r[4]}</p></div>'
            f"{comp_badge(r[3], 'green' if r[3] == '完了' else 'blue' if '中' in r[3] else 'gray')}</div>"
        )
    detail = (
        f'<div class="p-5">'
        f'<div class="flex items-center gap-3 mb-6">'
        f'<div class="w-12 h-12 rounded-xl flex items-center justify-center text-white text-lg font-bold" style="background:{p}">{m["rows"][0][1][0]}</div>'
        f'<div><p class="text-[15px] font-bold text-gray-800">{m["rows"][0][1]}</p>'
        f'<p class="text-[12px] text-gray-400">{m["rows"][0][0]} · {m["rows"][0][2]}</p></div></div>'
        f'<div class="grid grid-cols-2 gap-4">'
        f'<div class="p-3 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block">ステータス</span><span class="text-[13px] font-medium">{m["rows"][0][3]}</span></div>'
        f'<div class="p-3 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block">金額</span><span class="text-[13px] font-medium" style="color:{p}">{m["rows"][0][5]}</span></div>'
        f'<div class="p-3 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block">更新日</span><span class="text-[13px] font-medium">{m["rows"][0][4]}</span></div>'
        f'<div class="p-3 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block">部門</span><span class="text-[13px] font-medium">{m["rows"][0][2]}</span></div></div>'
        f'<div class="mt-5 pt-5 border-t"><h4 class="text-[13px] font-semibold text-gray-700 mb-3">アクティビティ</h4>'
        f'<div class="space-y-3">{comp_activities(m["activities"][:4], p)}</div></div></div>'
    )
    html = (
        f'<div class="grid grid-cols-1 lg:grid-cols-5 gap-0 card overflow-hidden" style="height:calc(100vh - 180px)">'
        f'<div class="lg:col-span-2 border-r overflow-y-auto">'
        f'<div class="p-3 border-b">{comp_search("splitSearch", "検索...")}</div>'
        f'<div id="splitList">{items}</div></div>'
        f'<div class="lg:col-span-3 overflow-y-auto">{detail}</div></div>'
    )
    js = """
function selectItem(el,color){document.querySelectorAll('#splitList > div').forEach(d=>{d.classList.remove('border-l-2');d.style.borderLeftColor=''});
el.classList.add('border-l-2');el.style.borderLeftColor=color;}
"""
    return {
        "id": "data",
        "title": "データ一覧",
        "desc": "リスト・詳細表示",
        "icon": "panel-left",
        "html": html,
        "js": js,
    }


def data_accordion(ch, colors, m):
    """Grouped accordion view."""
    p, s, bg = colors
    groups = {}
    for r in m["rows"]:
        dept = r[2]
        groups.setdefault(dept, []).append(r)
    acc = ""
    for i, (dept, items) in enumerate(groups.items()):
        rows = "".join(
            f'<div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg cursor-pointer transition-colors">'
            f'<div class="flex items-center gap-3"><i data-lucide="file-text" class="w-4 h-4 text-gray-400"></i>'
            f'<div><p class="text-[13px] text-gray-700">{r[1]}</p>'
            f'<p class="text-[11px] text-gray-400">{r[0]} · {r[4]}</p></div></div>'
            f"{comp_badge(r[3], 'green' if r[3] == '完了' else 'blue' if '中' in r[3] else 'gray')}</div>"
            for r in items
        )
        open_attr = "open" if i == 0 else ""
        acc += (
            f'<details class="card overflow-hidden" {open_attr}>'
            f'<summary class="flex items-center justify-between p-4 cursor-pointer hover:bg-gray-50 transition-colors">'
            f'<div class="flex items-center gap-3"><i data-lucide="folder" class="w-5 h-5" style="color:{p}"></i>'
            f'<span class="font-semibold text-[13px] text-gray-700">{dept}</span>'
            f'<span class="text-[11px] bg-gray-100 text-gray-500 px-2 py-0.5 rounded-full">{len(items)}件</span></div>'
            f'<i data-lucide="chevron-down" class="w-4 h-4 text-gray-400"></i></summary>'
            f'<div class="border-t px-4 py-2 space-y-0.5">{rows}</div></details>'
        )
    html = (
        f'<div class="flex items-center justify-between mb-5">'
        f"{comp_search('accSearch', '検索...')}"
        f"{comp_btn('新規追加', p, 'plus')}</div>"
        f'<div class="space-y-3">{acc}</div>'
    )
    return {
        "id": "data",
        "title": "データ一覧",
        "desc": "グループ表示",
        "icon": "folder",
        "html": html,
        "js": "",
    }


DATA_VARIANTS = [data_table_view, data_card_grid, data_split_view, data_accordion]


# ════════════════════════════════════════════════════════════
#  DETAIL PAGE VARIANTS (4)
# ════════════════════════════════════════════════════════════


def detail_section_form(ch, colors, m):
    p, s, bg = colors
    html = (
        f'<div class="max-w-3xl">'
        f'<div class="card p-6 mb-5"><h3 class="font-semibold text-[14px] text-gray-700 mb-5 flex items-center gap-2">'
        f'<i data-lucide="info" class="w-4 h-4" style="color:{p}"></i>基本情報</h3>'
        f'<div class="grid grid-cols-1 md:grid-cols-2 gap-4">'
        f"{comp_form_field('名称', 'text', '入力してください')}"
        f"{comp_form_field('カテゴリ', 'select', options=['A', 'B', 'C'])}"
        f"{comp_form_field('日付', 'date')}"
        f"{comp_form_field('担当者', 'text', '担当者名')}</div></div>"
        f'<div class="card p-6 mb-5"><h3 class="font-semibold text-[14px] text-gray-700 mb-5 flex items-center gap-2">'
        f'<i data-lucide="file-text" class="w-4 h-4" style="color:{p}"></i>詳細情報</h3>'
        f'<div class="space-y-4">{comp_form_field("説明", "textarea", "詳細を入力")}'
        f"{comp_form_field('金額', 'number', '0')}"
        f"{comp_form_field('備考', 'textarea', 'その他')}</div></div>"
        f'<div class="flex items-center justify-between">'
        f"{comp_btn_outline('キャンセル', '#6b7280')}"
        f'<div class="flex gap-2">{comp_btn_outline("下書き保存", p, "save")}{comp_btn("保存", p, "check")}</div></div></div>'
    )
    return {
        "id": "detail",
        "title": "登録・編集",
        "desc": "データ入力",
        "icon": "pencil",
        "html": html,
        "js": "",
    }


def detail_tabbed(ch, colors, m):
    p, s, bg = colors
    tab_labels = ["基本情報", "履歴", "添付ファイル", "コメント"]
    content0 = (
        f'<div class="grid grid-cols-2 gap-4">'
        f'<div class="p-4 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block mb-1">ID</span><span class="text-[14px] font-medium">{m["rows"][0][0]}</span></div>'
        f'<div class="p-4 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block mb-1">担当</span><span class="text-[14px] font-medium">{m["rows"][0][1]}</span></div>'
        f'<div class="p-4 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block mb-1">状態</span>{comp_badge(m["rows"][0][3], "green" if m["rows"][0][3] == "完了" else "blue")}</div>'
        f'<div class="p-4 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block mb-1">金額</span><span class="text-[14px] font-bold" style="color:{p}">{m["rows"][0][5]}</span></div></div>'
    )
    content1 = f'<div class="space-y-3">{comp_activities(m["activities"], p)}</div>'
    content2 = comp_empty("paperclip", "添付ファイルはありません")
    content3 = (
        f'<div class="space-y-4">'
        f'<div class="flex gap-3"><div class="w-8 h-8 rounded-full flex items-center justify-center text-white text-[11px]" style="background:{p}">管</div>'
        f'<div class="flex-1 card p-3"><p class="text-[13px] text-gray-700">問題ありません。承認します。</p>'
        f'<p class="text-[11px] text-gray-400 mt-1">2時間前</p></div></div>'
        f"{comp_form_field('コメント追加', 'textarea', 'コメントを入力...')}"
        f"{comp_btn('送信', p, 'send')}</div>"
    )
    tabs = comp_tabs("dtlTab", tab_labels, p)
    panels = (
        comp_tab_panel("dtlTab", 0, content0, False)
        + comp_tab_panel("dtlTab", 1, content1)
        + comp_tab_panel("dtlTab", 2, content2)
        + comp_tab_panel("dtlTab", 3, content3)
    )
    html = f'<div class="card p-5">{tabs}{panels}</div>'
    js = JS_TABS
    return {
        "id": "detail",
        "title": "詳細",
        "desc": "タブ切替表示",
        "icon": "eye",
        "html": html,
        "js": js,
    }


def detail_timeline_view(ch, colors, m):
    p, s, bg = colors
    tl = comp_timeline_items(m["timeline"], p)
    summary = "".join(
        f'<div class="p-4 rounded-lg bg-gray-50"><span class="text-[11px] text-gray-400 block mb-1">{m["kpis"][i][0]}</span>'
        f'<span class="text-[15px] font-bold" style="color:{p}">{m["kpis"][i][1]}</span></div>'
        for i in range(min(4, len(m["kpis"])))
    )
    html = (
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">{summary}</div>'
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">進行状況</h3>{tl}</div>'
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">メモ</h3>'
        f"{comp_form_field('メモ', 'textarea', 'メモを追加...')}"
        f'<div class="mt-3">{comp_btn("保存", p, "save")}</div></div></div>'
    )
    return {
        "id": "detail",
        "title": "詳細",
        "desc": "タイムライン表示",
        "icon": "clock",
        "html": html,
        "js": "",
    }


def detail_card_summary(ch, colors, m):
    p, s, bg = colors
    html = (
        f'<div class="max-w-4xl">'
        f'<div class="card p-6 mb-5">'
        f'<div class="flex items-center gap-4 mb-6">'
        f'<div class="w-14 h-14 rounded-2xl flex items-center justify-center text-white text-xl font-bold" style="background:{p}">{ch["challenge"][0]}</div>'
        f'<div><h2 class="text-[18px] font-bold text-gray-800">{ch["challenge"]}</h2>'
        f'<p class="text-[13px] text-gray-400">{ch["industry"]} · {ch["dept"]}</p></div></div>'
        f'<div class="p-4 rounded-lg mb-5" style="background:{bg}"><p class="text-[13px]" style="color:{p}">{ch["pain"]}</p></div>'
        f'<div class="grid grid-cols-2 md:grid-cols-4 gap-3">'
        f'{"".join(f"""<div class="text-center p-3 rounded-lg bg-gray-50"><div class="text-[18px] font-bold" style="color:{p}">{m["kpis"][i][1]}</div><div class="text-[11px] text-gray-400 mt-1">{m["kpis"][i][0]}</div></div>""" for i in range(min(4, len(m["kpis"]))))}'
        f"</div></div>"
        f'<div class="card p-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-4">最近のアクティビティ</h3>'
        f'<div class="space-y-3">{comp_activities(m["activities"], p, 5)}</div></div></div>'
    )
    return {
        "id": "detail",
        "title": "サマリー",
        "desc": "概要カード",
        "icon": "layout-list",
        "html": html,
        "js": "",
    }


DETAIL_VARIANTS = [
    detail_section_form,
    detail_tabbed,
    detail_timeline_view,
    detail_card_summary,
]


# ════════════════════════════════════════════════════════════
#  REPORT PAGE VARIANTS (4)
# ════════════════════════════════════════════════════════════


def report_multi_chart(ch, colors, m):
    p, s, bg = colors
    html = (
        f'<div class="flex items-center justify-between mb-5">'
        f'<div class="flex gap-2">{"".join(f"""<button class="text-[12px] px-3 py-1.5 rounded-lg {"text-white" if i == 0 else "border text-gray-500 hover:bg-gray-50"} cursor-pointer transition-colors" {"style=background:" + p if i == 0 else ""}>{t}</button>""" for i, t in enumerate(["月次", "週次", "日次"]))}</div>'
        f"{comp_btn_outline('エクスポート', p, 'download')}</div>"
        f'<div class="grid grid-cols-1 md:grid-cols-2 gap-5">'
        f"{comp_chart_box('rpC1', '売上推移', 240)}"
        f"{comp_chart_box('rpC2', 'カテゴリ別構成', 240)}"
        f"{comp_chart_box('rpC3', '月次比較', 240)}"
        f"{comp_chart_box('rpC4', 'パフォーマンス', 240)}</div>"
    )
    ds1 = [
        {
            "label": "実績",
            "data": m["chart1"],
            "borderColor": p,
            "backgroundColor": p + "15",
            "fill": True,
            "tension": 0.4,
            "pointRadius": 3,
            "pointBackgroundColor": p,
        }
    ]
    ds2 = [
        {
            "data": m["chart_pie"],
            "backgroundColor": [p, s, p + "60", s + "60", "#e5e7eb"],
            "borderWidth": 0,
        }
    ]
    ds3 = [
        {
            "label": "今期",
            "data": m["chart1"][:6],
            "backgroundColor": p,
            "borderRadius": 4,
        },
        {
            "label": "前期",
            "data": m["chart2"],
            "backgroundColor": "#e5e7eb",
            "borderRadius": 4,
        },
    ]
    ds4 = [
        {
            "label": "スコア",
            "data": m["chart2"],
            "borderColor": p,
            "backgroundColor": p + "20",
            "pointBackgroundColor": p,
        }
    ]
    js = (
        js_chart("rpC1", "line", MONTHS, ds1)
        + "\n"
        + js_chart("rpC2", "doughnut", ["A", "B", "C", "D", "E"], ds2)
        + "\n"
        + js_chart("rpC3", "bar", MONTHS[:6], ds3, True)
        + "\n"
        + js_chart("rpC4", "radar", ["営業", "品質", "効率", "技術", "CS", "管理"], ds4)
    )
    return {
        "id": "report",
        "title": "レポート",
        "desc": "分析・集計",
        "icon": "bar-chart-3",
        "html": html,
        "js": js,
    }


def report_table_totals(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    headers = ["月", "件数", "売上(万)", "原価(万)", "粗利(万)", "粗利率"]
    rows = []
    t_cnt, t_rev, t_cost = 0, 0, 0
    for i, mo in enumerate(MONTHS[:6]):
        cnt = rng.randint(5, 30)
        rev = rng.randint(100, 1000)
        cost = round(rev * rng.randint(40, 70) / 100)
        gross = rev - cost
        rate = round(gross / rev * 100, 1)
        rows.append(
            [mo, str(cnt), f"¥{rev:,}", f"¥{cost:,}", f"¥{gross:,}", f"{rate}%"]
        )
        t_cnt += cnt
        t_rev += rev
        t_cost += cost
    rows.append(
        [
            "合計",
            str(t_cnt),
            f"¥{t_rev:,}",
            f"¥{t_cost:,}",
            f"¥{t_rev - t_cost:,}",
            f"{round((t_rev - t_cost) / t_rev * 100, 1)}%",
        ]
    )
    tbl = comp_table("rpTbl", headers, rows, p)
    html = (
        f'<div class="flex items-center justify-between mb-5">'
        f'<h3 class="font-semibold text-[14px] text-gray-700">月次実績レポート</h3>'
        f"{comp_btn_outline('エクスポート', p, 'download')}</div>"
        f"{tbl}"
        f'<div class="mt-5">{comp_chart_box("rpC1", "月次推移", 240)}</div>'
    )
    bar_ds = [
        {
            "label": "売上",
            "data": [int(r[2].replace("¥", "").replace(",", "")) for r in rows[:-1]],
            "backgroundColor": p,
            "borderRadius": 4,
        }
    ]
    js = JS_SORT_TABLE + "\n" + js_chart("rpC1", "bar", MONTHS[:6], bar_ds)
    return {
        "id": "report",
        "title": "レポート",
        "desc": "月次実績",
        "icon": "table",
        "html": html,
        "js": js,
    }


def report_trend(ch, colors, m):
    p, s, bg = colors
    kpis = "".join(comp_kpi(*k, p) for k in m["kpis"][:4])
    html = (
        f'<div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-5">{kpis}</div>'
        f"{comp_chart_box('rpC1', 'トレンド分析', 320)}"
        f'<div class="card p-5 mt-5"><h3 class="font-semibold text-[13px] text-gray-700 mb-3">分析サマリー</h3>'
        f'<div class="grid grid-cols-1 md:grid-cols-3 gap-3">'
        f'<div class="p-3 rounded-lg bg-emerald-50"><p class="text-[11px] text-emerald-600 font-medium mb-1">好調指標</p><p class="text-[13px] text-emerald-700">前月比+12%の成長</p></div>'
        f'<div class="p-3 rounded-lg bg-amber-50"><p class="text-[11px] text-amber-600 font-medium mb-1">注意指標</p><p class="text-[13px] text-amber-700">コスト率が上昇傾向</p></div>'
        f'<div class="p-3 rounded-lg" style="background:{bg}"><p class="text-[11px] font-medium mb-1" style="color:{p}">予測</p><p class="text-[13px]" style="color:{p}">Q2達成確率78%</p></div></div></div>'
    )
    ds = [
        {
            "label": "実績",
            "data": m["chart1"],
            "borderColor": p,
            "tension": 0.4,
            "pointRadius": 4,
            "pointBackgroundColor": p,
        },
        {
            "label": "予測",
            "data": m["chart1"][:8] + [None] * 4,
            "borderColor": "#d1d5db",
            "borderDash": [5, 5],
            "tension": 0.4,
            "pointRadius": 0,
        },
        {
            "label": "目標",
            "data": [60] * 12,
            "borderColor": "#f59e0b",
            "borderDash": [2, 4],
            "pointRadius": 0,
        },
    ]
    js = js_chart("rpC1", "line", MONTHS, ds, True)
    return {
        "id": "report",
        "title": "レポート",
        "desc": "トレンド分析",
        "icon": "trending-up",
        "html": html,
        "js": js,
    }


def report_comparison(ch, colors, m):
    p, s, bg = colors
    rng = m["rng"]
    categories = ["営業", "製造", "品質", "管理", "開発", "CS"]
    this_period = [rng.randint(30, 90) for _ in categories]
    last_period = [max(10, v - rng.randint(0, 20)) for v in this_period]
    # Summary cards
    total_this = sum(this_period)
    total_last = sum(last_period)
    change = round((total_this - total_last) / total_last * 100, 1)
    html = (
        f'<div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5">'
        f"{comp_stat_big('今期合計', str(total_this), f'前期比 +{change}%', 'trending-up', p)}"
        f"{comp_stat_big('前期合計', str(total_last), '', 'calendar', s)}"
        f"{comp_stat_big('増減', f'+{total_this - total_last}', f'{change}%増', 'arrow-up-right', '#10b981')}</div>"
        f'<div class="grid grid-cols-1 lg:grid-cols-2 gap-5">'
        f"{comp_chart_box('rpC1', '期間比較', 260)}"
        f"{comp_chart_box('rpC2', '構成比変化', 260)}</div>"
    )
    bar_ds = [
        {"label": "今期", "data": this_period, "backgroundColor": p, "borderRadius": 4},
        {
            "label": "前期",
            "data": last_period,
            "backgroundColor": "#e5e7eb",
            "borderRadius": 4,
        },
    ]
    pie1 = [
        {
            "data": this_period[:5],
            "backgroundColor": [p, s, p + "80", s + "80", "#e5e7eb"],
            "borderWidth": 0,
        }
    ]
    js = (
        js_chart("rpC1", "bar", categories, bar_ds, True)
        + "\n"
        + js_chart("rpC2", "doughnut", categories[:5], pie1)
    )
    return {
        "id": "report",
        "title": "レポート",
        "desc": "期間比較",
        "icon": "git-compare",
        "html": html,
        "js": js,
    }


REPORT_VARIANTS = [
    report_multi_chart,
    report_table_totals,
    report_trend,
    report_comparison,
]


# ════════════════════════════════════════════════════════════
#  SETTINGS PAGE (shared)
# ════════════════════════════════════════════════════════════


def page_settings(ch, colors, m):
    p, s, bg = colors
    toggles = ""
    settings = [
        ("メール通知", "新しいタスクが割り当てられた時"),
        ("Slack連携", "ステータス変更時に通知"),
        ("自動バックアップ", "日次でデータをバックアップ"),
        ("ダークモード", "画面表示をダークテーマに変更"),
    ]
    for i, (title, desc) in enumerate(settings):
        checked = "checked" if i < 2 else ""
        toggles += (
            f'<div class="flex items-center justify-between p-4 hover:bg-gray-50 rounded-lg transition-colors">'
            f'<div><p class="text-[13px] font-medium text-gray-700">{title}</p>'
            f'<p class="text-[11px] text-gray-400 mt-0.5">{desc}</p></div>'
            f'<label class="relative inline-flex items-center cursor-pointer">'
            f'<input type="checkbox" {checked} class="sr-only peer">'
            f'<div class="w-10 h-5 bg-gray-200 peer-focus:ring-2 peer-focus:ring-blue-100 rounded-full peer '
            f"peer-checked:after:translate-x-full after:content-[''] after:absolute after:top-0.5 after:left-[2px] "
            f'after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all" style="peer-checked:background:{p}"></div></label></div>'
        )
    html = (
        f'<div class="max-w-2xl">'
        f'<div class="card p-5 mb-5"><h3 class="font-semibold text-[14px] text-gray-700 mb-4 flex items-center gap-2">'
        f'<i data-lucide="bell" class="w-4 h-4" style="color:{p}"></i>通知設定</h3>'
        f'<div class="divide-y">{toggles}</div></div>'
        f'<div class="card p-5 mb-5"><h3 class="font-semibold text-[14px] text-gray-700 mb-4 flex items-center gap-2">'
        f'<i data-lucide="palette" class="w-4 h-4" style="color:{p}"></i>表示設定</h3>'
        f'<div class="space-y-4">'
        f"{comp_form_field('表示件数', 'select', options=['10', '20', '50', '100'])}"
        f"{comp_form_field('言語', 'select', options=['日本語', 'English'])}"
        f"{comp_form_field('タイムゾーン', 'select', options=['Asia/Tokyo', 'UTC'])}</div></div>"
        f'<div class="flex justify-end">{comp_btn("保存", p, "save")}</div></div>'
    )
    return {
        "id": "settings",
        "title": "設定",
        "desc": "アプリ設定",
        "icon": "settings",
        "html": html,
        "js": "",
    }
