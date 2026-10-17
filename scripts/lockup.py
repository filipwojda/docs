"""
The docs' logo: the regards mark and "regards.design" in Public Sans 500, set as the site sets
<Regards domain /> (src/lib/components/brand/Regards.svelte in the app): the mark 1.1em wide, 0.22em before
the word, its bottom 0.22em below the baseline. The word is outlined, so it renders the same everywhere.

  python3 scripts/lockup.py <PublicSans variable .ttf/.woff2> <the app's static/logo/mark-small.svg>

Writes logo/light.svg (ink #111111) and logo/dark.svg (#EEEEEE). In the dark one the mark turns over, as the
site's .ink-art does at night (light lines on dark). Needs fontTools (and brotli for a .woff2).
"""
import re
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

WORD, SIZE, WEIGHT = "regards.design", 100.0, 500
font_path, mark_path = sys.argv[1], sys.argv[2]
out = Path(__file__).resolve().parent.parent / "logo"

font = TTFont(font_path)
if "fvar" in font:
    font = instantiateVariableFont(font, {"wght": WEIGHT})
scale = SIZE / font["head"].unitsPerEm
cmap, glyphs, hmtx = font.getBestCmap(), font.getGlyphSet(), font["hmtx"]

mark_box, gap, drop = 1.1 * SIZE, 0.22 * SIZE, 0.22 * SIZE
baseline = mark_box - drop  # the mark's top at 0, its bottom `drop` below the baseline
x = mark_box + gap
pen = SVGPathPen(glyphs)
for ch in WORD:
    name = cmap[ord(ch)]
    # font units, y up → the logo's px, y down, from this glyph's origin on the baseline
    glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
    x += hmtx[name][0] * scale
word = pen.getCommands()
width = round(x + 0.04 * SIZE, 2)

svg = Path(mark_path).read_text()
view = re.search(r'viewBox="([^"]+)"', svg).group(1)
inner = re.sub(r"<title>.*?</title>", "", svg[svg.index(">") + 1 : svg.rindex("</svg>")], flags=re.S)


def inverted(art: str) -> str:
    """The art as filter: invert(1) draws it: every hex colour turned over."""
    def flip(m: re.Match) -> str:
        h = m.group(1)
        h = "".join(c * 2 for c in h) if len(h) == 3 else h
        return "#" + "".join(f"{255 - int(h[i:i + 2], 16):02x}" for i in (0, 2, 4))
    return re.sub(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", flip, art)


for name, ink in (("light", "#111111"), ("dark", "#EEEEEE")):
    art = inner if name == "light" else inverted(inner)
    (out / f"{name}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {mark_box:g}" role="img" aria-label="regards.design">'
        f'<title>regards.design</title>'
        f'<svg x="0" y="0" width="{mark_box:g}" height="{mark_box:g}" viewBox="{view}">{art}</svg>'
        f'<path fill="{ink}" d="{word}"/></svg>\n'
    )
print(f"logo/light.svg, logo/dark.svg: {width}×{mark_box:g}")
