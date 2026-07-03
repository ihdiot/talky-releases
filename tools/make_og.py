# One-shot OG card (1200x630) for the Talky download page — dark bg, cyan brand, waveform motif.
# Base image stays RGB; ImageDraw in "RGBA" ink-mode blends alpha inks correctly onto RGB.
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
BG = (7, 9, 12)
CYAN = (33, 217, 255)
TEXT = (233, 241, 245)
MUTED = (143, 162, 176)
DIM = (92, 109, 122)
AMBER = (255, 180, 84)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img, "RGBA")

# faint grid
for x in range(0, W, 56):
    d.line([(x, 0), (x, H)], fill=(140, 200, 225, 12))
for y in range(0, H, 56):
    d.line([(0, y), (W, y)], fill=(140, 200, 225, 12))

# cyan glow top-center (blurred overlay pasted with its own alpha as mask)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([W // 2 - 480, -380, W // 2 + 480, 200], fill=(33, 217, 255, 60))
glow = glow.filter(ImageFilter.GaussianBlur(130))
img.paste(glow, (0, 0), glow)
d = ImageDraw.Draw(img, "RGBA")

F = "C:/Windows/Fonts/"
f_badge = ImageFont.truetype(F + "consolab.ttf", 24)
f_name = ImageFont.truetype(F + "segoeuib.ttf", 148)
f_tag = ImageFont.truetype(F + "segoeuib.ttf", 47)
f_sub = ImageFont.truetype(F + "segoeui.ttf", 31)
f_url = ImageFont.truetype(F + "consola.ttf", 24)

LX = 92  # left margin

# badge pill
bt = "EARLY ALPHA  ·  WINDOWS  ·  FREE WHILE TESTING"
bw = d.textlength(bt, font=f_badge)
d.rounded_rectangle([LX, 96, LX + bw + 44, 146], radius=25,
                    outline=(255, 180, 84, 110), width=2, fill=(255, 180, 84, 28))
d.text((LX + 22, 108), bt, font=f_badge, fill=AMBER)

# logo: rounded square + waveform bars
ly, ls = 196, 132
d.rounded_rectangle([LX, ly, LX + ls, ly + ls], radius=30, outline=CYAN, width=7)
bars = [(0.28, 0.34), (0.46, 0.72), (0.64, 0.46)]  # (x-frac, height-frac)
bw_ = 15
for xf, hf in bars:
    bx = LX + xf * ls - bw_ / 2
    bh = hf * ls
    by = ly + (ls - bh) / 2
    d.rounded_rectangle([bx, by, bx + bw_, by + bh], radius=7, fill=CYAN)

# wordmark
d.text((LX + ls + 44, ly - 44), "Talky", font=f_name, fill=TEXT)

# tagline: the slogan, IHDIOT in brand cyan (drawn in colored segments) + descriptor
x = LX
for seg, col in (("Talk like an ", TEXT), ("IHDIOT", CYAN), (". Type like a pro.", TEXT)):
    d.text((x, 392), seg, font=f_tag, fill=col)
    x += d.textlength(seg, font=f_tag)
d.text((LX, 462), "Offline AI dictation for Windows — nothing ever leaves your PC.",
       font=f_sub, fill=MUTED)

# decorative waveform strip along the bottom
for i, x in enumerate(range(LX, W - 80, 22)):
    hgt = 12 + 30 * abs(math.sin(i * 0.55)) * (1 - i / 60.0 * 0.35)
    a = max(28, 150 - i * 3)
    d.rounded_rectangle([x, 560 - hgt / 2, x + 9, 560 + hgt / 2], radius=4,
                        fill=(33, 217, 255, int(a)))

d.text((W - 80 - d.textlength("ihdiot.github.io/talky-releases", font=f_url), 596),
       "ihdiot.github.io/talky-releases", font=f_url, fill=DIM)

out = r"C:\Users\ihdio\Documents\Claude\Projects\ihdiot-dictation\.temp\talky-releases\docs\og.png"
img.save(out, "PNG")
print("saved", out)
