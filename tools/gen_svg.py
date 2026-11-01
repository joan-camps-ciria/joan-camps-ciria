"""Genera los SVG del README de perfil con el estilo del portfolio."""
import base64, pathlib, re, sys, urllib.parse, urllib.request
from xml.sax.saxutils import escape as esc
from fontTools.ttLib import TTFont

HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
CACHE = HERE / "fontcache"
CACHE.mkdir(exist_ok=True)

THEMES = {
    "dark": dict(fondo="#0f131b", alt="#161b26", texto="#e6eaf2", suave="#9aa4b8", borde="#262d3b",
                 acento="#3ddc97", acento_s="rgba(61,220,151,.12)", terminal="#0a0d13", on_acento="#0b1a13"),
    "light": dict(fondo="#f6f7f9", alt="#ffffff", texto="#1c2230", suave="#5a6478", borde="#e1e5ec",
                  acento="#0a9b6e", acento_s="rgba(10,155,110,.1)", terminal="#161b26", on_acento="#ffffff"),
}
CHARS = "".join(chr(c) for c in range(32, 127)) + "áéíóúñÁÉÍÓÚÑüç·–→®¿¡▋"
INTER, MONO = "Inter", "JetBrains Mono"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def font(family, weight):
    path = CACHE / f"{family.replace(' ', '')}-{weight}.woff2"
    if not path.exists():
        q = urllib.parse.urlencode({"family": f"{family}:wght@{weight}", "text": CHARS})
        req = urllib.request.Request(f"https://fonts.googleapis.com/css2?{q}", headers={"User-Agent": UA})
        css = urllib.request.urlopen(req).read().decode()
        url = re.search(r"url\((https:[^)]+)\)", css).group(1)
        path.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read())
    return path


METRICS = {}


def width(s, family, weight, size, ls=0):
    key = (family, weight)
    if key not in METRICS:
        f = TTFont(font(family, weight))
        METRICS[key] = (f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm)
    cmap, hmtx, upem = METRICS[key]
    return sum(hmtx[cmap[ord(c)]][0] if ord(c) in cmap else upem * 0.6 for c in s) / upem * size + ls * len(s)


class Svg:
    def __init__(self, w, h, t):
        self.w, self.h, self.t, self.body, self.fonts, self.defs = w, h, THEMES[t], [], set(), []

    def add(self, s):
        self.body.append(s)

    def text(self, x, y, s, family=INTER, weight=400, size=16, fill="texto", anchor="start", ls=0):
        self.fonts.add((family, weight))
        spacing = f' letter-spacing="{ls}"' if ls else ""
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-family="\'{family}\',{"ui-monospace,monospace" if family == MONO else "system-ui,sans-serif"}" '
                 f'font-weight="{weight}" font-size="{size}" fill="{self.c(fill)}"{a}{spacing}>{esc(s)}</text>')

    def c(self, name):
        return self.t.get(name, name)

    def rect(self, x, y, w, h, r=0, fill="alt", stroke=None, extra=""):
        s = f' stroke="{self.c(stroke)}"' if stroke else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{self.c(fill)}"{s} {extra}/>')

    def card(self, x, y, w, h):
        self.rect(x + .5, y + .5, w - 1, h - 1, 12, "alt", "borde")

    def save(self, name):
        css = ""
        for fam, wt in sorted(self.fonts):
            b64 = base64.b64encode(font(fam, wt).read_bytes()).decode()
            css += f"@font-face{{font-family:'{fam}';font-weight:{wt};src:url(data:font/woff2;base64,{b64}) format('woff2')}}"
        doc = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
               f'width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}"><style>{css}</style>'
               f'<defs>{"".join(self.defs)}</defs>{"".join(self.body)}</svg>')
        (OUT / name).write_text(doc, encoding="utf-8")


# ---------- Hero ----------
CMDS = ["ansible-playbook -i produccion hardening.yml", "kubectl rollout status deploy/tareas",
        "sudo dnf update --security -y", "podman build -t mi-app:2.0 .", "systemctl status httpd"]
CW = 15 * .6  # JetBrains Mono: 0.6 em


def timeline():
    """Frames (t, comando, letras) con los mismos tiempos que script.js."""
    frames, t = [], 0
    for i, c in enumerate(CMDS):
        for n in range(1, len(c) + 1):
            frames.append((t, i, n)); t += 55
        t += 1800 - 55
        for n in range(len(c) - 1, -1, -1):
            frames.append((t, i, n)); t += 25
        t += 400 - 25
    return frames, t


def hero(t):
    W, H = 900, 366
    s = Svg(W, H, t)
    s.rect(.5, .5, W - 1, H - 1, 14, "fondo", "borde")
    s.add(f'<line x1="1" x2="{W-1}" y1="56.5" y2="56.5" stroke="{s.c("borde")}"/>')
    s.text(30, 35, "joan@camps", MONO, 600, 16)
    s.text(30 + width("joan@camps", MONO, 600, 16), 35, ":~$", MONO, 600, 16, "acento")
    x = W - 30
    links = ["Contacto", "Proyectos", "Habilidades", "Experiencia", "Sobre mí"]
    for l in links:
        x -= width(l, INTER, 500, 14)
        s.text(x, 34, l, INTER, 500, 14, "suave")
        x -= 20

    s.text(40, 112, "Hola, soy", MONO, 400, 16, "acento")
    s.text(40, 166, "Joan Camps Ciria", INTER, 700, 50, ls=-1)
    s.text(40, 204, "Linux Systems Engineer", INTER, 400, 22, "suave")

    tx, ty, tw, th = 40, 228, 820, 100
    s.defs.append(f'<clipPath id="term"><rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="10"/></clipPath>')
    s.add('<g clip-path="url(#term)">')
    s.rect(tx, ty, tw, th, 0, "terminal")
    s.rect(tx, ty, tw, 32, 0, "rgba(255,255,255,.05)")
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        s.add(f'<circle cx="{tx+18+i*18}" cy="{ty+16}" r="5.5" fill="{col}"/>')
    s.add("</g>")

    bx, by = tx + 18, ty + 72
    s.text(bx, by, "$", MONO, 400, 15, "#3ddc97")
    cx0 = bx + 2 * CW
    frames, total = timeline()
    # Se comprime en valores discretos; un cuadro por cada cambio
    kt = ";".join(f"{f[0]/total:.5f}" for f in frames)
    wid = ";".join(f"{f[2]*CW:.1f}" for f in frames)
    cur = ";".join(f"{cx0+f[2]*CW:.1f}" for f in frames)
    dur = f"{total/1000:.2f}s"
    s.defs.append(f'<clipPath id="typed"><rect x="{cx0}" y="{by-18}" width="{len(CMDS[0])*CW}" height="26">'
                  f'<animate attributeName="width" calcMode="discrete" dur="{dur}" repeatCount="indefinite" keyTimes="{kt}" values="{wid}"/>'
                  f'</rect></clipPath>')
    s.add('<g clip-path="url(#typed)">')
    for i, c in enumerate(CMDS):
        vis = ";".join("1" if f[1] == i else "0" for f in frames)
        s.fonts.add((MONO, 400))
        s.add(f'<text x="{cx0}" y="{by}" font-family="\'{MONO}\',ui-monospace,monospace" font-size="15" fill="#d7dde8" '
              f'opacity="{1 if i == 0 else 0}">{esc(c)}<animate attributeName="opacity" calcMode="discrete" dur="{dur}" '
              f'repeatCount="indefinite" keyTimes="{kt}" values="{vis}"/></text>')
    s.add("</g>")
    s.add(f'<rect x="{cx0+len(CMDS[0])*CW+2}" y="{by-13}" width="8" height="16" fill="#3ddc97">'
          f'<animate attributeName="x" calcMode="discrete" dur="{dur}" repeatCount="indefinite" keyTimes="{kt}" values="{cur}"/>'
          f'<animate attributeName="opacity" calcMode="discrete" dur="1s" repeatCount="indefinite" keyTimes="0;.5" values="1;0"/></rect>')

    s.save(f"hero-{t}.svg")


def cifras(t):
    W, H, gap = 900, 100, 14
    s = Svg(W, H, t)
    w = (W - 3 * gap) / 4
    data = [("+7", "años en producción"), ("RHCSA", "Red Hat certified"), ("IaC", "Ansible · AWX"), ("K8s", "OpenShift · Docker")]
    for i, (a, b) in enumerate(data):
        x = i * (w + gap)
        s.card(x, 0, w, H)
        s.text(x + w / 2, 46, a, MONO, 600, 26, "acento", "middle")
        s.text(x + w / 2, 74, b, INTER, 400, 14, "suave", "middle")
    s.save(f"cifras-{t}.svg")


def boton(t, name, label, primary=False):
    w, h = int(width(label, INTER, 600, 15)) + 44, 44
    s = Svg(w, h, t)
    if primary:
        s.rect(.5, .5, w - 1, h - 1, 8, "acento", "acento")
    else:
        s.rect(.5, .5, w - 1, h - 1, 8, "alt", "borde")
    s.text(w / 2, 27.5, label, INTER, 600, 15, "on_acento" if primary else "texto", "middle")
    s.save(f"boton-{name}-{t}.svg")


for t in THEMES:
    hero(t); cifras(t)
    boton(t, "portfolio", "Ver portfolio", True)
    boton(t, "linkedin", "LinkedIn")
print("archivos", len(list(OUT.glob("*.svg"))))
