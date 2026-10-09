#!/usr/bin/env python3
"""Genera assets/now-playing.svg: un casete que muestra tu último movimiento público en GitHub.

Lo ejecuta .github/workflows/now-playing.yml. Solo usa la librería estándar.
Uso local de prueba:  python scripts/now_playing.py --sample
"""
import json, os, sys, urllib.request
from datetime import datetime, timedelta, timezone
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "Nakusuo")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT", "assets/now-playing.svg")
LIMA = timezone(timedelta(hours=-5))
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
MONO = "'Courier New', Courier, monospace"
SERIF = "Georgia, 'Times New Roman', serif"


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={
        "Accept": "application/vnd.github+json", "User-Agent": "now-playing-cassette"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def describe(ev):
    """Devuelve (título, repo, etiqueta) para un evento público."""
    t, repo, p = ev["type"], ev["repo"]["name"], ev.get("payload", {})
    short = repo.split("/")[-1]
    if t == "PushEvent":
        msg = None
        commits = p.get("commits") or []
        if commits:
            msg = commits[-1].get("message")
        elif p.get("head"):
            try:
                msg = api(f"/repos/{repo}/commits/{p['head']}")["commit"]["message"]
            except Exception:
                msg = None
        branch = (p.get("ref") or "").replace("refs/heads/", "")
        return (msg or "push").splitlines()[0], short, f"push · {branch}" if branch else "push"
    if t == "ReleaseEvent":
        rel = p.get("release", {})
        return f"release {rel.get('tag_name', '')} · {rel.get('name') or ''}".strip(" ·"), short, "release"
    if t == "CreateEvent":
        return f"nuevo {p.get('ref_type', 'repo')} {p.get('ref') or short}", short, "create"
    if t == "PullRequestEvent":
        pr = p.get("pull_request", {})
        return f"PR #{pr.get('number', '')} {pr.get('title', '')}", short, f"pr · {p.get('action', '')}"
    if t == "IssuesEvent":
        return f"issue: {p.get('issue', {}).get('title', '')}", short, "issue"
    if t == "WatchEvent":
        return f"le dio ★ a {repo}", short, "star"
    return t.replace("Event", "").lower(), short, "evento"


def collect():
    events = []
    for page in (1, 2, 3):
        try:
            batch = api(f"/users/{USER}/events/public?per_page=100&page={page}")
        except Exception as e:  # noqa: BLE001
            print("aviso:", e, file=sys.stderr)
            break
        if not batch:
            break
        events += batch
    return events


def sample():
    now = datetime.now(timezone.utc)
    evs = [{"type": "PushEvent", "repo": {"name": "Nakusuo/huecko-frontend"},
            "payload": {"ref": "refs/heads/main", "commits": [{"message": "feat(planes): votación exprés con plazo y recomendación de la IA"}]},
            "created_at": now.isoformat()}]
    for i in range(40):
        evs.append({"type": "PushEvent", "repo": {"name": "Nakusuo/x"}, "payload": {},
                    "created_at": (now - timedelta(hours=7 * i + (i * i) % 11)).isoformat()})
    return evs


def trunc(s, n):
    return s if len(s) <= n else s[: n - 1] + "…"


def render(events):
    now = datetime.now(LIMA)
    if events:
        title, repo, tag = describe(events[0])
        when = datetime.fromisoformat(events[0]["created_at"].replace("Z", "+00:00")).astimezone(LIMA)
    else:
        title, repo, tag, when = "silencio entre pistas", USER, "pausa", now
    when_s = f"{when.day:02d} {MESES[when.month - 1]} · {when:%H:%M} (Lima)"

    # actividad de los últimos 14 días
    days = [0] * 14
    for ev in events:
        d = datetime.fromisoformat(ev["created_at"].replace("Z", "+00:00")).astimezone(LIMA).date()
        k = (now.date() - d).days
        if 0 <= k < 14:
            days[13 - k] += 1
    week = sum(days[7:])
    mx = max(days) or 1

    bars = []
    bx, base, bw = 880, 128, 14
    for i, n in enumerate(days):
        h = 6 + 64 * n / mx if n else 3
        col = "#c9505f" if i == 13 else ("#8fa36b" if n else "#2c322c")
        lo = max(3, h * 0.7)
        anim = (f'<animate attributeName="height" values="{h:.0f};{lo:.0f};{h:.0f}" dur="{1.1 + (i % 4) * 0.2:.1f}s" repeatCount="indefinite"/>'
                f'<animate attributeName="y" values="{base - h:.0f};{base - lo:.0f};{base - h:.0f}" dur="{1.1 + (i % 4) * 0.2:.1f}s" repeatCount="indefinite"/>') if n else ""
        bars.append(f'<rect x="{bx + i * (bw + 6)}" y="{base - h:.0f}" width="{bw}" height="{h:.0f}" rx="2" fill="{col}">{anim}</rect>')

    def reel(x, dur):
        spokes = "".join(f'<path d="M0 -20 L0 -9" transform="rotate({a})"/>' for a in range(0, 360, 60))
        return (f'<g transform="translate({x} 88)"><circle r="32" fill="#1d1916" stroke="#5b5249" stroke-width="1.5"/>'
                f'<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="{dur}s" repeatCount="indefinite"/>'
                f'<circle r="21" fill="#3a322c" stroke="#6b6156"/><circle r="8" fill="#15171a"/>'
                f'<g stroke="#6b6156" stroke-width="3.5" stroke-linecap="round">{spokes}</g></g></g>')

    t = escape(trunc(title, 46))
    meta = escape(f"{repo}  ·  {tag}")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 176" width="1200" height="176" role="img" aria-label="Reproduciendo: {t}">
  <title>Reproduciendo: {t}</title>
  <defs>
    <pattern id="grain" width="7" height="7" patternUnits="userSpaceOnUse">
      <rect x="0" y="0" width="1" height="1" fill="#6b7f52" opacity="0.16"/>
      <rect x="4" y="3" width="1" height="1" fill="#8a8f8a" opacity="0.10"/>
    </pattern>
    <clipPath id="marquee"><rect x="250" y="64" width="590" height="34"/></clipPath>
  </defs>
  <rect width="1200" height="176" rx="14" fill="#15171a"/>
  <rect width="1200" height="176" rx="14" fill="url(#grain)"/>
  <rect x="1" y="1" width="1198" height="174" rx="13" fill="none" stroke="#2c322c"/>

  <!-- deck -->
  <rect x="34" y="40" width="190" height="96" rx="10" fill="#2b2521" stroke="#5b5249"/>
  <rect x="78" y="80" width="102" height="16" fill="#4a382c"/>
  {reel(84, 3.2)}{reel(174, 4.4)}

  <!-- texto -->
  <g font-family="{MONO}">
    <circle cx="258" cy="44" r="6" fill="#c9505f"><animate attributeName="opacity" values="1;0.2;1" dur="1.4s" repeatCount="indefinite"/></circle>
    <text x="272" y="49" font-size="13" letter-spacing="4" fill="#8f9a83">REPRODUCIENDO</text>
    <text x="840" y="49" text-anchor="end" font-size="12" fill="#6f776a">{escape(when_s)}</text>
  </g>
  <g clip-path="url(#marquee)">
    <text x="250" y="90" font-family="{SERIF}" font-size="25" font-weight="700" fill="#e3dbc8">{t}</text>
  </g>
  <text x="250" y="122" font-family="{MONO}" font-size="14" fill="#a89c86">{meta}</text>
  <rect x="250" y="138" width="590" height="3" rx="1.5" fill="#2c322c"/>
  <rect x="250" y="138" width="0" height="3" rx="1.5" fill="#7a8f5c">
    <animate attributeName="width" values="0;590" dur="24s" repeatCount="indefinite"/>
  </rect>
  <text x="250" y="160" font-family="{MONO}" font-size="11.5" fill="#6f776a">se actualiza solo cada 6 h · github actions</text>

  <!-- ecualizador: 14 días -->
  <g>{''.join(bars)}</g>
  <g font-family="{MONO}" font-size="11.5" fill="#6f776a">
    <text x="{bx}" y="152">14 días</text>
    <text x="{bx + 14 * (bw + 6) - 6}" y="152" text-anchor="end">esta semana: <tspan fill="#c9c2b0">{week}</tspan></text>
  </g>
</svg>
"""


if __name__ == "__main__":
    evs = sample() if "--sample" in sys.argv else collect()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(evs))
    print("ok ->", OUT, "eventos:", len(evs))
