#!/usr/bin/env python3
"""SRD MVP Generator v2 — Multi-page SPA with unique UI per challenge."""

import openpyxl
from pathlib import Path

from gen.shell import build_spa
from gen.pages import (
    gen_mock,
    DASHBOARD_VARIANTS,
    FEATURE_MAP,
    DATA_VARIANTS,
    DETAIL_VARIANTS,
    REPORT_VARIANTS,
    page_settings,
)

# ════════════════════════════════════════════════════════════
#  CONFIGURATION
# ════════════════════════════════════════════════════════════

XLSX = Path(
    "/Users/niff/workspace/stella/srd/sales-research/SRD_業界別課題_SaaSリサーチ.xlsx"
)
OUT = Path("/Users/niff/workspace/srd-mvp-apps/public")
BASE_URL = "https://z403.github.io/srd-mvp-apps"

COLORS = {
    1: ("#1e3a5f", "#3b82f6", "#dbeafe"),
    2: ("#7c2d12", "#ea580c", "#ffedd5"),
    3: ("#065f46", "#10b981", "#d1fae5"),
    4: ("#5b21b6", "#8b5cf6", "#ede9fe"),
    5: ("#0e7490", "#06b6d4", "#cffafe"),
    6: ("#9f1239", "#f43f5e", "#ffe4e6"),
    7: ("#a16207", "#eab308", "#fef9c3"),
    8: ("#be185d", "#ec4899", "#fce7f3"),
    9: ("#4338ca", "#6366f1", "#e0e7ff"),
    10: ("#0f766e", "#14b8a6", "#ccfbf1"),
    11: ("#1e3a5f", "#2563eb", "#dbeafe"),
    12: ("#581c87", "#9333ea", "#f3e8ff"),
    13: ("#9f1239", "#fb7185", "#ffe4e6"),
    14: ("#166534", "#22c55e", "#dcfce7"),
    15: ("#92400e", "#f59e0b", "#fef3c7"),
    16: ("#374151", "#6b7280", "#f3f4f6"),
    17: ("#1e40af", "#3b82f6", "#dbeafe"),
    18: ("#c2410c", "#f97316", "#fff7ed"),
    19: ("#86198f", "#d946ef", "#fae8ff"),
    20: ("#047857", "#34d399", "#d1fae5"),
}

# ════════════════════════════════════════════════════════════
#  CLASSIFICATION
# ════════════════════════════════════════════════════════════

FEATURE_KEYWORDS = {
    "kanban": [
        "施工管理",
        "プロジェクト",
        "工程管理",
        "タスク管理",
        "進行管理",
        "進捗",
        "PJ",
        "商談管理",
        "板金",
        "工程",
    ],
    "calendar": [
        "勤怠",
        "シフト",
        "出面",
        "スケジュール",
        "予約",
        "入退室",
        "点呼",
        "アポ",
        "入退館",
        "レッスン",
        "内見",
    ],
    "form_wizard": [
        "見積",
        "積算",
        "申請",
        "登録",
        "請求",
        "レセプト",
        "申告",
        "届出",
        "記入",
        "問診",
        "帳票",
        "報告書",
    ],
    "checklist": [
        "安全管理",
        "KY活動",
        "点検",
        "品質管理",
        "検査",
        "衛生",
        "HACCP",
        "コンプライアンス",
        "監査",
        "適合性",
    ],
    "map": [
        "配車",
        "配送",
        "ルート",
        "車両",
        "位置情報",
        "拠点",
        "ロケーション",
        "圃場",
        "森林",
        "漁獲",
    ],
    "inventory": [
        "在庫",
        "棚卸",
        "発注",
        "仕入",
        "資材",
        "食材",
        "薬剤",
        "部品",
        "商品マスタ",
        "物販",
        "物件情報",
        "空室",
        "中古車",
        "預かり品",
    ],
    "timeline": [
        "工事原価",
        "整備",
        "車検",
        "保全",
        "メンテナンス",
        "リコール",
        "設備",
        "老朽化",
        "CCUS",
        "技工物",
    ],
    "documents": [
        "書類",
        "文書",
        "図面",
        "ペーパーレス",
        "帳票",
        "カルテ",
        "ケアプラン",
        "契約書",
        "マニュアル",
        "教材",
        "校正",
        "著作権",
        "素材管理",
        "提案書",
    ],
    "matrix": [
        "比較",
        "評価",
        "審査",
        "与信",
        "マッチング",
        "アサイン",
        "スキル",
        "事業性",
        "選定",
    ],
    "calculator": [
        "原価管理",
        "コスト",
        "利益",
        "収支",
        "試算",
        "会計",
        "経理",
        "月謝",
        "料金",
        "家賃",
        "消込",
        "給与",
        "工数管理",
        "採算",
        "タイムチャージ",
        "食材発注",
        "需給",
    ],
    "chat": [
        "情報共有",
        "連絡",
        "引き継ぎ",
        "伝達",
        "コミュニケーション",
        "多言語",
        "保護者",
        "問合せ",
        "口コミ",
        "チェックイン",
    ],
    "crm": [
        "顧客",
        "CRM",
        "追客",
        "反響",
        "得意先",
        "ファン",
        "オーナー報告",
        "リピート",
        "会員",
        "入金",
        "督促",
        "集客",
        "窓口",
    ],
    "hr": [
        "人材",
        "採用",
        "離職",
        "育成",
        "教育",
        "研修",
        "技術伝承",
        "ナレッジ",
        "資格",
        "スタッフDB",
        "要員",
        "求職",
        "定着",
        "多能工",
    ],
    "workflow": [
        "承認",
        "稟議",
        "ワークフロー",
        "清掃",
        "受発注",
        "契約管理",
        "組合員",
        "開通",
        "共済",
        "配本",
        "レガシー",
        "DMS",
        "電子申告",
    ],
    "analytics": [
        "データ分析",
        "可視化",
        "KPI",
        "POSデータ",
        "ABC分析",
        "需給",
        "CO2",
        "気象",
        "稼働率",
        "マーケティング",
        "集客",
        "広告運用",
        "レポート作成",
        "売価",
        "廃棄",
        "エネルギー",
        "キャッシュレス",
        "写真整理",
        "遠隔",
    ],
}


def classify(name, pain):
    """Classify challenge into feature type based on keywords."""
    text = f"{name} {pain}"
    for ftype, keywords in FEATURE_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return ftype
    return "kanban"


def variant_idx(ind_no, ch_no, n, offset=0):
    """Deterministic variant selection based on challenge ID."""
    return abs(hash(f"{ind_no}-{ch_no}-{offset}")) % n


# ════════════════════════════════════════════════════════════
#  INDEX PAGE
# ════════════════════════════════════════════════════════════


def generate_index(challenges):
    """Generate a professional index page."""
    industries = {}
    for c in challenges:
        ind = c["industry"]
        if ind not in industries:
            industries[ind] = []
        industries[ind].append(c)

    total = len(challenges)
    cards = ""
    for ind, items in industries.items():
        ind_no = items[0]["industry_no"]
        primary, secondary, bg = COLORS.get(ind_no, ("#1e40af", "#3b82f6", "#dbeafe"))
        links = ""
        for item in items:
            links += (
                f'<a href="{ind_no}-{item["challenge_no"]}.html" '
                f'class="flex items-center gap-2 p-2 rounded-lg hover:bg-gray-50 text-[13px] text-gray-600 '
                f'hover:text-gray-900 transition-colors cursor-pointer" data-search="{item["challenge"]}">'
                f'<span class="text-gray-300">{item["challenge_no"]}.</span> '
                f'<span class="truncate">{item["challenge"]}</span></a>'
            )
        cards += f"""
        <div class="bg-white rounded-2xl shadow-sm border overflow-hidden hover:shadow-lg transition-shadow">
            <div class="p-5 text-white" style="background:{primary}">
                <span class="text-[11px] opacity-60">業界 {ind_no}</span>
                <h2 class="font-bold text-lg mt-0.5">{ind}</h2>
                <p class="text-[12px] opacity-60 mt-1">{len(items)}件のデモアプリ</p>
            </div>
            <div class="p-3 space-y-0 max-h-[320px] overflow-y-auto">{links}</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="ja"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>SRD 業界別課題 MVPデモ一覧</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>*{{font-family:'Inter','Hiragino Kaku Gothic ProN',sans-serif}}</style>
</head><body class="bg-gray-50 min-h-screen">
<div class="max-w-7xl mx-auto px-6 py-12">
    <div class="text-center mb-10">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-50 text-blue-700 text-[12px] font-medium mb-4">
            <i data-lucide="zap" class="w-3.5 h-3.5"></i> {total}件のインタラクティブデモ
        </div>
        <h1 class="text-3xl font-bold text-gray-900">SRD 業界別課題 MVPデモ</h1>
        <p class="text-gray-500 mt-2 text-[14px]">20業界の業務課題を解決する SaaS プロトタイプ集</p>
        <div class="max-w-md mx-auto mt-6">
            <div class="relative">
                <i data-lucide="search" class="w-4 h-4 text-gray-400 absolute left-4 top-1/2 -translate-y-1/2"></i>
                <input id="globalSearch" type="text" placeholder="課題名で検索..."
                    class="w-full pl-11 pr-4 py-3 text-[14px] bg-white border rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-100 transition">
            </div>
        </div>
    </div>
    <div id="indexGrid" class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">{cards}</div>
    <footer class="text-center py-10 text-[12px] text-gray-400">
        <p>Powered by SRD / Stella Group</p>
        <p class="mt-1">商談時のデモツールとしてご利用ください</p>
    </footer>
</div>
<script>
document.addEventListener('DOMContentLoaded',()=>{{if(typeof lucide!=='undefined')lucide.createIcons();
document.getElementById('globalSearch').addEventListener('input',function(){{
const q=this.value.toLowerCase();
document.querySelectorAll('#indexGrid [data-search]').forEach(el=>{{
el.style.display=el.dataset.search.toLowerCase().includes(q)?'':'none'}});
}});}});
</script></body></html>"""


# ════════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════════


def main():
    wb = openpyxl.load_workbook(XLSX)
    ws = wb["全課題一覧"]

    challenges = []
    for r in range(2, ws.max_row + 1):
        row = {
            "industry_no": ws.cell(r, 1).value,
            "industry": ws.cell(r, 2).value,
            "challenge_no": ws.cell(r, 3).value,
            "challenge": ws.cell(r, 4).value,
            "pain": ws.cell(r, 5).value or "",
            "dept": ws.cell(r, 6).value or "",
        }
        if row["challenge"]:
            challenges.append(row)

    OUT.mkdir(parents=True, exist_ok=True)
    feat_counts = {}

    for ch in challenges:
        ind_no = ch["industry_no"]
        ch_no = ch["challenge_no"]
        colors = COLORS.get(ind_no, COLORS[1])

        # Classify feature type
        ftype = classify(ch["challenge"], ch["pain"])
        feat_counts[ftype] = feat_counts.get(ftype, 0) + 1

        # Generate mock data
        mock = gen_mock(ftype, ch, colors)

        # Select page variants deterministically
        dash_fn = DASHBOARD_VARIANTS[
            variant_idx(ind_no, ch_no, len(DASHBOARD_VARIANTS), 0)
        ]
        feat_fn = FEATURE_MAP.get(ftype, FEATURE_MAP["kanban"])
        data_fn = DATA_VARIANTS[variant_idx(ind_no, ch_no, len(DATA_VARIANTS), 10)]
        detail_fn = DETAIL_VARIANTS[
            variant_idx(ind_no, ch_no, len(DETAIL_VARIANTS), 20)
        ]
        report_fn = REPORT_VARIANTS[
            variant_idx(ind_no, ch_no, len(REPORT_VARIANTS), 30)
        ]

        # Generate pages
        pages = [
            dash_fn(ch, colors, mock),
            feat_fn(ch, colors, mock),
            data_fn(ch, colors, mock),
            detail_fn(ch, colors, mock),
            report_fn(ch, colors, mock),
            page_settings(ch, colors, mock),
        ]

        # Build SPA
        html = build_spa(ch, pages, colors)
        filename = f"{ind_no}-{ch_no}.html"
        (OUT / filename).write_text(html, encoding="utf-8")
        print(f"  {filename} [{ftype}]")

    # Index page
    index_html = generate_index(challenges)
    (OUT / "index.html").write_text(index_html, encoding="utf-8")

    print(f"\n{'=' * 50}")
    print(f"Generated {len(challenges)} apps + index.html")
    print("\nFeature type distribution:")
    for ft, count in sorted(feat_counts.items(), key=lambda x: -x[1]):
        print(f"  {ft:15s} {count:3d}")
    print(f"{'=' * 50}")

    # Update xlsx G column
    ws.cell(1, 7).value = "MVPデモURL"
    for r in range(2, ws.max_row + 1):
        ind = ws.cell(r, 1).value
        cno = ws.cell(r, 3).value
        name = ws.cell(r, 4).value
        if name and ind and cno:
            ws.cell(r, 7).value = f"{BASE_URL}/{ind}-{cno}.html"
    wb.save(XLSX)
    print("\nUpdated xlsx G column with URLs")


if __name__ == "__main__":
    main()
