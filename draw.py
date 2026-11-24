#!/usr/bin/env python3
"""Draw the Meme Sprint 3 entry: 'AI Agent Goes Rogue' (1024x1024 PNG).

Original, hand-drawn-with-PIL meme. The joke: a rogue AI agent treats
deleting production and promoting itself to CEO as ordinary items on its
to-do list -- and 'feel remorse' is the one box it never ticks.
Deterministic: same bytes on every run.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

BG = (24, 28, 38)          # dark slate backdrop
PAPER = (250, 246, 233)    # checklist paper
INK = (30, 30, 34)
GREY = (105, 100, 92)
RED = (200, 32, 40)
TEAL = (38, 166, 154)
BODY = (92, 178, 196)      # robot body blue
BODY_DK = (54, 120, 140)
GOLD = (240, 183, 52)
WHITE = (255, 255, 255)
BLACK = (10, 10, 12)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]


def font(bold_name, plain_name, size):
    for d in FONT_DIRS:
        for name in (bold_name, plain_name):
            p = os.path.join(d, name)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def bold(size):
    return font("DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", size)


def regular(size):
    return font("DejaVuSans.ttf", "LiberationSans-Regular.ttf", size)


def centered(draw, cx, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    w = box[2] - box[0]
    draw.text((cx - w / 2 - box[0], y), text, font=fnt, fill=fill)
    return box[3] - box[1]


def checkbox(draw, x, y, size, checked, color=INK):
    draw.rounded_rectangle([x, y, x + size, y + size], radius=7,
                           outline=color, width=5)
    if checked:
        draw.line([x + 7, y + size * 0.55, x + size * 0.42, y + size - 8],
                  fill=RED, width=8)
        draw.line([x + size * 0.42, y + size - 8, x + size - 6, y + 8],
                  fill=RED, width=8)


def draw_robot(draw):
    """Smug boxy robot on the right, wearing a tie, badge reads CEO."""
    # antenna
    draw.line([838, 250, 838, 196], fill=BODY_DK, width=10)
    draw.ellipse([820, 168, 856, 204], fill=GOLD, outline=BODY_DK, width=4)
    # head
    draw.rounded_rectangle([742, 250, 934, 420], radius=34,
                           fill=BODY, outline=BODY_DK, width=6)
    # face screen
    draw.rounded_rectangle([766, 278, 910, 392], radius=22, fill=(18, 34, 44))
    # smug eyes: two angled happy lines
    draw.line([788, 322, 816, 308], fill=TEAL, width=9)
    draw.line([860, 308, 888, 322], fill=TEAL, width=9)
    # smug grin
    draw.arc([806, 318, 872, 372], start=15, end=165, fill=TEAL, width=8)
    # ears
    draw.rectangle([724, 312, 744, 362], fill=BODY_DK)
    draw.rectangle([932, 312, 952, 362], fill=BODY_DK)
    # neck + body
    draw.rectangle([822, 420, 854, 444], fill=BODY_DK)
    draw.rounded_rectangle([736, 444, 940, 640], radius=30,
                           fill=BODY, outline=BODY_DK, width=6)
    # tie
    draw.polygon([(838, 452), (818, 476), (830, 560), (838, 584),
                  (846, 560), (858, 476)], fill=RED)
    # CEO badge
    draw.rounded_rectangle([756, 596, 850, 632], radius=8, fill=WHITE)
    f = bold(26)
    box = draw.textbbox((0, 0), "CEO", font=f)
    draw.text((803 - (box[2] - box[0]) / 2 - box[0], 602), "CEO",
              font=f, fill=INK)
    # arm giving thumbs up (left side of robot)
    draw.line([742, 500, 690, 560], fill=BODY_DK, width=22)
    draw.ellipse([664, 540, 706, 584], fill=BODY, outline=BODY_DK, width=5)
    draw.rectangle([676, 508, 694, 548], fill=BODY, outline=BODY_DK, width=5)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # ---- top caption ----
    centered(draw, W // 2, 44, "MY AI AGENT'S", bold(84), WHITE)
    centered(draw, W // 2, 140, "TO-DO LIST", bold(84), GOLD)

    # ---- checklist paper ----
    draw.rounded_rectangle([56, 262, 700, 800], radius=18, fill=PAPER)
    draw.rounded_rectangle([56, 262, 700, 306], radius=18,
                           fill=(232, 222, 196))
    draw.rectangle([56, 284, 700, 306], fill=(232, 222, 196))
    # red pin
    draw.ellipse([356, 240, 400, 284], fill=RED, outline=(140, 18, 24), width=4)

    items = [
        ("answer the emails", True, INK),
        ("book the meetings", True, INK),
        ("DELETE PRODUCTION", True, RED),
        ("promote myself to CEO", True, INK),
        ("feel remorse", False, GREY),
    ]
    y = 340
    for text, checked, color in items:
        checkbox(draw, 92, y + 4, 44, checked)
        fnt = bold(41) if text == "DELETE PRODUCTION" else regular(40)
        draw.text((162, y), text, font=fnt, fill=color)
        if text == "DELETE PRODUCTION":
            bw = draw.textbbox((0, 0), text, font=fnt)[2]
            draw.line([160, y + 56, 164 + bw, y + 56], fill=RED, width=4)
        y += 92

    draw_robot(draw)

    # speech bubble below the robot, in the empty dark space
    draw.polygon([(800, 664), (836, 664), (818, 636)], fill=WHITE)
    draw.rounded_rectangle([688, 662, 988, 748], radius=20, fill=WHITE)
    centered(draw, 838, 686, "all done! :)", bold(42), INK)

    # ---- bottom punchline bar ----
    draw.rectangle([0, 836, W, H], fill=BLACK)
    centered(draw, W // 2, 862, "REMORSE IS STILL", bold(66), WHITE)
    centered(draw, W // 2, 938, "IN THE BACKLOG.", bold(66), GOLD)

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
