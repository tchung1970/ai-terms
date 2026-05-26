from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (251, 249, 244)
SOFT = (244, 240, 230)
INK = (26, 24, 20)
INK2 = (58, 53, 48)
INK3 = (107, 100, 90)
PLUM = (109, 58, 138)
ROSE = (193, 75, 107)
LEAF = (61, 110, 62)
OCEAN = (44, 94, 138)
AMBER = (168, 106, 31)

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
# AppleSDGothicNeo.ttc has multiple weights at different indexes
def font(size, weight="bold"):
    idx = {"thin":0,"ultralight":1,"light":2,"regular":3,"medium":4,"semibold":5,"bold":6,"extrabold":7,"heavy":8}[weight]
    return ImageFont.truetype(FONT_PATH, size, index=idx)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# soft radial blobs (rose top-right, plum bottom-left)
def soft_blob(cx, cy, r, color, alpha_peak=70):
    layer = Image.new("RGBA", (W, H), (0,0,0,0))
    ld = ImageDraw.Draw(layer)
    steps = 60
    for i in range(steps, 0, -1):
        ratio = i / steps
        a = int(alpha_peak * (1 - ratio) ** 2)
        rr = int(r * ratio)
        ld.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=(*color, a))
    img.alpha_composite(layer) if img.mode == "RGBA" else None

# Use compositing with RGBA
base = img.convert("RGBA")
def add_blob(cx, cy, r, color, peak=80):
    layer = Image.new("RGBA", (W, H), (0,0,0,0))
    ld = ImageDraw.Draw(layer)
    for i in range(40, 0, -1):
        ratio = i/40
        a = int(peak*(1-ratio)**1.6)
        rr = int(r*ratio)
        ld.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=(*color, a))
    return Image.alpha_composite(base, layer)

base = add_blob(1080, -40, 420, ROSE, 60)
base = add_blob(120, 580, 460, PLUM, 55)
img = base.convert("RGB")
draw = ImageDraw.Draw(img)

# Top rainbow band
band_colors = [PLUM, ROSE, AMBER, LEAF, OCEAN]
seg_w = W / len(band_colors)
for i, c in enumerate(band_colors):
    x0 = int(i*seg_w); x1 = int((i+1)*seg_w)
    # smooth gradient between segments
    for x in range(x0, x1):
        if i < len(band_colors)-1:
            t = (x - x0) / (x1 - x0)
            nxt = band_colors[min(i+1, len(band_colors)-1)]
            r = int(c[0]*(1-t) + nxt[0]*t)
            g = int(c[1]*(1-t) + nxt[1]*t)
            b = int(c[2]*(1-t) + nxt[2]*t)
            draw.line([(x,0),(x,8)], fill=(r,g,b))
        else:
            draw.line([(x,0),(x,8)], fill=c)

# Layout
PAD_X = 80

# Kicker
kicker_font = font(20, "bold")
draw.ellipse([PAD_X, 78, PAD_X+10, 88], fill=PLUM)
draw.text((PAD_X+22, 70), "AI GLOSSARY  ·  한국어  ·  2026", fill=PLUM, font=kicker_font)

# Main title — two lines
title_font = font(78, "heavy")
line1 = "AI 시대를 살아남기 위한"
line2 = "단어들의 안내서"

y = 150
draw.text((PAD_X, y), line1, fill=INK, font=title_font)

# line2 with subtle highlight bar behind, then gradient-ish text (plum)
y2 = y + 100
# measure
bbox = draw.textbbox((PAD_X, y2), line2, font=title_font)
hl_pad_x = 4
hl_pad_y = 6
# soft highlight behind
hl = Image.new("RGBA", (W, H), (0,0,0,0))
hld = ImageDraw.Draw(hl)
hld.rounded_rectangle([bbox[0]-hl_pad_x, bbox[3]-22, bbox[2]+hl_pad_x, bbox[3]+4],
                      radius=6, fill=(193,75,107,55))
img = Image.alpha_composite(img.convert("RGBA"), hl).convert("RGB")
draw = ImageDraw.Draw(img)
# Render line2 with simulated gradient by horizontal slicing
def gradient_text(xy, text, font_obj, c0, c1):
    bb = draw.textbbox(xy, text, font=font_obj)
    tw = bb[2]-bb[0]; th = bb[3]-bb[1]
    if tw <= 0 or th <= 0:
        draw.text(xy, text, fill=c0, font=font_obj); return
    # render text in white onto a mask
    mask = Image.new("L", (tw+20, th+40), 0)
    md = ImageDraw.Draw(mask)
    md.text((0, 0), text, font=font_obj, fill=255)
    # build gradient strip
    grad = Image.new("RGB", (tw+20, th+40), c0)
    gd = ImageDraw.Draw(grad)
    for i in range(tw+20):
        t = i/max(1, tw+19)
        r = int(c0[0]*(1-t)+c1[0]*t)
        g = int(c0[1]*(1-t)+c1[1]*t)
        b = int(c0[2]*(1-t)+c1[2]*t)
        gd.line([(i,0),(i,th+40)], fill=(r,g,b))
    img.paste(grad, (xy[0], xy[1]), mask)

gradient_text((PAD_X, y2), line2, title_font, PLUM, ROSE)
draw = ImageDraw.Draw(img)

# Subtitle
sub_font = font(26, "regular")
sub = "AI 시대를 이해하기 위한 핵심 용어와 인물 53개를 한국어로 정리했습니다."
draw.text((PAD_X, y2+120), sub, fill=INK3, font=sub_font)

# Bottom row: stats and URL
bot_y = H - 110
# stat pills
stat_font_n = font(34, "heavy")
stat_font_l = font(18, "medium")

# Draw three pills
def pill(x, y, n, label, accent):
    pill_w = 200
    pill_h = 70
    draw.rounded_rectangle([x, y, x+pill_w, y+pill_h], radius=14,
                           fill=(255,255,255), outline=(232,227,212), width=1)
    # accent dot
    draw.ellipse([x+18, y+30, x+30, y+42], fill=accent)
    draw.text((x+40, y+10), n, fill=INK, font=stat_font_n)
    draw.text((x+40, y+45), label, fill=INK3, font=stat_font_l)

pill(PAD_X, bot_y, "38", "용어", PLUM)
pill(PAD_X+220, bot_y, "15", "인물", ROSE)
pill(PAD_X+440, bot_y, "한국어", "번역", OCEAN)

# URL right-aligned
url_font = font(22, "semibold")
url = "ai.tchung.org/ai-terms"
ubb = draw.textbbox((0,0), url, font=url_font)
uw = ubb[2]-ubb[0]
draw.text((W-PAD_X-uw, bot_y+22), url, fill=INK2, font=url_font)

img.save("/tmp/og.png", "PNG", optimize=True)
print("ok", img.size)
