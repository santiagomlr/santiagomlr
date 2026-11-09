"""Render a branded contribution dashboard SVG from the GitHub GraphQL API.

Usage: GITHUB_TOKEN=... python scripts/stats.py <user> <out.svg>
       python scripts/stats.py --demo <out.svg>      # fake data, for previews
"""
import datetime as dt, json, os, random, sys, urllib.request

def fetch(user, token):
    q = """query($u:String!){user(login:$u){
      createdAt
      contributionsCollection{
        totalCommitContributions totalPullRequestContributions
        restrictedContributionsCount
        contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}
      repositories(ownerAffiliations:OWNER,privacy:PUBLIC){totalCount}}}"""
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": q, "variables": {"u": user}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req))["data"]["user"]
    cc = d["contributionsCollection"]
    days = [(x["date"], x["contributionCount"]) for w in cc["contributionCalendar"]["weeks"] for x in w["contributionDays"]]
    return dict(days=days, total=cc["contributionCalendar"]["totalContributions"],
                commits=cc["totalCommitContributions"], prs=cc["totalPullRequestContributions"],
                repos=d["repositories"]["totalCount"])

def demo():
    random.seed(7); today = dt.date.today(); start = today - dt.timedelta(days=364 + today.isoweekday() % 7)
    days = []
    for i in range((today - start).days + 1):
        d = start + dt.timedelta(days=i)
        days.append((d.isoformat(), 0 if random.random() < .3 else int(random.expovariate(.25))))
    return dict(days=days, total=sum(c for _, c in days), commits=812, prs=64, repos=4)

def streaks(days):
    cur = best = run = 0
    for _, c in days:
        run = run + 1 if c else 0; best = max(best, run)
    for i, (_, c) in enumerate(reversed(days)):
        if c: cur += 1
        elif i == 0: continue          # today may still be empty
        else: break
    return cur, best

def color(c, mx):
    if c == 0: return "#141C36"
    p = [ "#0E4D5C", "#0E7490", "#22D3EE", "#E3B341"]
    q = c / max(mx, 1)
    return p[0] if q < .15 else p[1] if q < .4 else p[2] if q < .75 else p[3]

def render(s):
    days = s["days"]; cur, best = streaks(days); active = sum(1 for _, c in days if c)
    mx = sorted(c for _, c in days)[int(len(days) * .97)] or 1
    W, H = 1200, 400
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         "<defs><style>.s{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}"
         ".m{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}"
         ".c{opacity:0;animation:f .4s ease-out forwards}@keyframes f{to{opacity:1}}"
         ".k{opacity:0;animation:u .7s ease-out forwards}@keyframes u{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}</style>"
         '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E1530"/><stop offset="1" stop-color="#080C1A"/></linearGradient>'
         '<linearGradient id="bd" x1="0" x2="1"><stop offset="0" stop-color="#22D3EE" stop-opacity=".5"/><stop offset="1" stop-color="#E3B341" stop-opacity=".5"/></linearGradient></defs>',
         f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="20" fill="url(#bg)" stroke="url(#bd)"/>']
    kpis = [(f"{s['total']:,}", "contributions · last 12 months", "#22D3EE"),
            (f"{cur}", "day current streak", "#E3B341"),
            (f"{best}", "day longest streak", "#A78BFA"),
            (f"{active}", "active days this year", "#34D399")]
    for i, (v, l, col) in enumerate(kpis):
        x = 40 + i * 285
        o.append(f'<g class="k" style="animation-delay:{.15*i:.2f}s"><rect x="{x}" y="32" width="265" height="110" rx="14" fill="{col}" fill-opacity=".07" stroke="{col}" stroke-opacity=".3"/>'
                 f'<text x="{x+22}" y="92" class="s" font-size="44" font-weight="800" fill="{col}">{v}</text>'
                 f'<text x="{x+22}" y="122" class="m" font-size="13" fill="#94A3B8">{l}</text></g>')
    # heatmap
    first = dt.date.fromisoformat(days[0][0]); cell, gap = 16, 4; x0, y0 = 80, 185
    lastm = None
    for i, (d, c) in enumerate(days):
        dd = dt.date.fromisoformat(d)
        wk = (dd - first + dt.timedelta(days=first.isoweekday() % 7)).days // 7; dow = dd.isoweekday() % 7
        x = x0 + wk * (cell + gap); y = y0 + dow * (cell + gap)
        if dd.day <= 7 and dow == 0 and dd.month != lastm:
            o.append(f'<text x="{x}" y="{y0-10}" class="m" font-size="12" fill="#64748B">{dd.strftime("%b")}</text>'); lastm = dd.month
        o.append(f'<rect class="c" style="animation-delay:{.6+wk*.025:.2f}s" x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="{color(c,mx)}"><title>{d}: {c}</title></rect>')
    for lbl, r in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        o.append(f'<text x="{x0-12}" y="{y0+r*(cell+gap)+13}" text-anchor="end" class="m" font-size="11" fill="#64748B">{lbl}</text>')
    o.append(f'<text x="{W-40}" y="{H-14}" text-anchor="end" class="m" font-size="11" fill="#475569">{s["commits"]:,} commits · {s["prs"]} PRs · auto-updated {dt.date.today():%b %d, %Y}</text>')
    o.append("</svg>")
    return "\n".join(o)

if __name__ == "__main__":
    if sys.argv[1] == "--demo": s = demo(); out = sys.argv[2]
    else: s = fetch(sys.argv[1], os.environ["GITHUB_TOKEN"]); out = sys.argv[2]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w").write(render(s)); print("wrote", out, s["total"])
