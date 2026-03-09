"""SPA shell — sidebar navigation, routing, layout."""

import json


def build_spa(ch, pages, colors):
    """Build complete SPA HTML from page list."""
    ind_no = ch["industry_no"]
    primary, secondary, bg = colors
    ch_name = ch["challenge"]
    industry = ch["industry"]
    pain = ch["pain"]

    # Navigation items
    nav = ""
    for i, p in enumerate(pages):
        act = " active" if i == 0 else ""
        nav += (
            f'<a data-page="{p["id"]}" class="nav-item{act} flex items-center gap-3 '
            f"px-3 py-2.5 rounded-lg text-sm cursor-pointer transition-all "
            f'hover:bg-white/10" onclick="navigate(\'{p["id"]}\')">'
            f'<i data-lucide="{p["icon"]}" class="w-[18px] h-[18px] shrink-0"></i>'
            f'<span class="truncate">{p["title"]}</span></a>\n'
        )

    # Page sections
    sections = ""
    all_js = ""
    for i, p in enumerate(pages):
        act = " active" if i == 0 else ""
        sections += f'<div id="page-{p["id"]}" class="page{act}">{p["html"]}</div>\n'
        if p.get("js"):
            all_js += f"\n// {p['id']}\n{p['js']}\n"

    page_cfg = json.dumps(
        [
            {"id": p["id"], "title": p["title"], "desc": p.get("desc", "")}
            for p in pages
        ],
        ensure_ascii=False,
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{ch_name} | {industry} | SRD</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{{font-family:'Inter','Hiragino Kaku Gothic ProN',sans-serif}}
.page{{display:none}}.page.active{{display:block;animation:fadeIn .25s ease-out}}
.nav-item.active{{background:rgba(255,255,255,.15);font-weight:600}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
::-webkit-scrollbar{{width:5px}}::-webkit-scrollbar-thumb{{background:#94a3b8;border-radius:3px}}
.card{{background:#fff;border-radius:12px;border:1px solid #e5e7eb;box-shadow:0 1px 2px rgba(0,0,0,.04)}}
.card:hover{{box-shadow:0 4px 12px rgba(0,0,0,.06)}}
input,select,textarea{{font-family:inherit}}
</style>
</head>
<body class="bg-gray-50">
<div class="flex h-screen overflow-hidden">

<aside class="w-[232px] flex flex-col text-white shrink-0 overflow-hidden" style="background:{primary}">
<div class="p-4 border-b border-white/10">
<div class="flex items-center gap-3">
<div class="w-9 h-9 rounded-lg bg-white/20 flex items-center justify-center font-bold text-sm shrink-0">{ind_no}</div>
<div class="min-w-0"><p class="font-semibold text-[13px] truncate">{ch_name[:22]}</p>
<p class="text-[11px] opacity-50 truncate">{industry}</p></div>
</div></div>
<nav class="flex-1 p-2.5 space-y-0.5 overflow-y-auto">{nav}</nav>
<div class="p-3 border-t border-white/10">
<div class="flex items-center gap-2 px-1">
<div class="w-7 h-7 rounded-full bg-white/20 flex items-center justify-center text-[11px]">管</div>
<div class="min-w-0"><p class="text-[11px] font-medium">管理者</p>
<p class="text-[10px] opacity-40">admin@example.com</p></div>
</div></div>
</aside>

<div class="flex-1 flex flex-col overflow-hidden">
<header class="bg-white border-b px-6 py-3 flex items-center justify-between shrink-0">
<div><h1 id="pageTitle" class="font-bold text-[15px] text-gray-800">{pages[0]["title"]}</h1>
<p id="pageDesc" class="text-[12px] text-gray-400 mt-0.5">{pages[0].get("desc", "")}</p></div>
<div class="flex items-center gap-2">
<span class="text-[11px] px-2.5 py-1 rounded-full font-medium" style="background:{bg};color:{primary}">MVP Demo</span>
</div></header>
<main class="flex-1 overflow-auto p-5">{sections}</main>
</div>
</div>

<script>
const charts=[];
const pageConfig={page_cfg};
function navigate(id){{
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
const el=document.getElementById('page-'+id);
if(el){{el.classList.add('active')}}
document.querySelector('[data-page="'+id+'"]')?.classList.add('active');
const cfg=pageConfig.find(p=>p.id===id);
if(cfg){{document.getElementById('pageTitle').textContent=cfg.title;
document.getElementById('pageDesc').textContent=cfg.desc}}
history.replaceState(null,null,'#'+id);
setTimeout(()=>{{charts.forEach(c=>c.resize());if(typeof lucide!=='undefined')lucide.createIcons()}},60);
}}
window.addEventListener('hashchange',()=>navigate(location.hash.slice(1)));
document.addEventListener('DOMContentLoaded',()=>{{
navigate(location.hash.slice(1)||pageConfig[0].id);
if(typeof lucide!=='undefined')lucide.createIcons();
}});
{all_js}
</script>
</body></html>"""
