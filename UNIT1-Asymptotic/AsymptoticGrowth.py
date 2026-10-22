"""Generate the Asymptotic Notations and Growth Comparison Visualization (PNG).

Run with:
    python Project3_AsymptoticGrowth.py
Requires:
    Pillow (PIL)
"""

from pathlib import Path
from math import log2, log10
from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).with_name("Visualization.png")
WIDTH, HEIGHT = 1800, 1720
BG = "#F8FAFC"
INK = "#0F172A"
MUTED = "#475569"
LINE_COLOR = "#CBD5E1"

# Academic color palette
COLORS = {
    "O": "#1D4ED8",        # Royal Blue
    "Omega": "#0D9488",    # Teal Green
    "Theta": "#7C3AED",    # Vivid Violet
    "Exp": "#E11D48",      # Crimson Rose
}


def get_font(size, bold=False):
    """Retrieve suitable system font or fallback gracefully."""
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_centered_text(draw, xy, text, fnt, fill):
    """Draw text centered at xy."""
    x, y = xy
    box = draw.multiline_textbbox((0, 0), text, font=fnt, spacing=7, align="center")
    w = box[2] - box[0]
    h = box[3] - box[1]
    draw.multiline_text((x - w / 2, y - h / 2), text, font=fnt, fill=fill, spacing=7, align="center")


def draw_card(draw, box, fill, outline, radius=24, width=3):
    """Draw a smooth rounded card container."""
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def main():
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    d = ImageDraw.Draw(image)

    # -------------------------------------------------------------
    # 1. Main Header
    # -------------------------------------------------------------
    draw_centered_text(d, (WIDTH / 2, 60), "ASYMPTOTIC ANALYSIS & NOTATION COMPARISON", get_font(42, True), INK)
    draw_centered_text(d, (WIDTH / 2, 112), "Formal definitions, bounds interpretation, and growth rate scaling as input size n approaches infinity",
                       get_font(21), MUTED)

    # Central Concept Banner
    draw_card(d, (460, 160, 1340, 275), "#FFFFFF", LINE_COLOR, radius=24, width=2)
    draw_centered_text(d, (WIDTH / 2, 202), "Core Mathematical Principle: Compare f(n) against reference function g(n)", get_font(25, True), INK)
    draw_centered_text(d, (WIDTH / 2, 240), "Bounds hold for sufficiently large n (n ≥ n₀) while ignoring constant scale multipliers", get_font(19), MUTED)

    # -------------------------------------------------------------
    # 2. Three Notation Cards
    # -------------------------------------------------------------
    cards = [
        (
            75,
            "BIG-O NOTATION",
            "O( g(n) )",
            "Asymptotic Upper Bound",
            "f(n) ≤ c · g(n)  for all n ≥ n₀",
            "Ceiling / Worst-Case Bound",
            "Example: 3n² + 2n + 1 is O(n²)",
            "Linear Search: O(n) worst case",
            "#EFF6FF",
            COLORS["O"],
        ),
        (
            625,
            "BIG-OMEGA NOTATION",
            "Ω( g(n) )",
            "Asymptotic Lower Bound",
            "f(n) ≥ c · g(n)  for all n ≥ n₀",
            "Floor / Best-Case Bound",
            "Example: 3n² + 2n + 1 is Ω(n²)",
            "Linear Search: Ω(1) best case",
            "#F0FDF4",
            COLORS["Omega"],
        ),
        (
            1175,
            "BIG-THETA NOTATION",
            "Θ( g(n) )",
            "Asymptotically Tight Bound",
            "c₁·g(n) ≤ f(n) ≤ c₂·g(n)  for n ≥ n₀",
            "Sandwich / Exact Rate",
            "Example: 3n² + 2n + 1 is Θ(n²)",
            "Merge Sort: Θ(n log n) all cases",
            "#FAF5FF",
            COLORS["Theta"],
        ),
    ]

    for x, title, symbol, meaning, inequality, mnemonic, ex1, ex2, tint, theme_color in cards:
        card_box = (x, 345, x + 550, 830)
        # Card outer border
        draw_card(d, card_box, "#FFFFFF", theme_color, radius=24, width=3)
        # Card header pill
        d.rounded_rectangle((x + 2, 347, x + 548, 440), radius=22, fill=tint)
        draw_centered_text(d, (x + 275, 380), title, get_font(23, True), theme_color)
        draw_centered_text(d, (x + 275, 415), symbol, get_font(28, True), INK)

        # Meaning & inequality
        draw_centered_text(d, (x + 275, 485), meaning, get_font(22, True), INK)
        draw_centered_text(d, (x + 275, 535), inequality, get_font(18), MUTED)

        # Mnemonic highlight pill
        d.rounded_rectangle((x + 40, 575, x + 510, 635), radius=16, fill=tint, outline=theme_color, width=1)
        draw_centered_text(d, (x + 275, 605), mnemonic, get_font(18, True), theme_color)

        # Divider line
        d.line((x + 50, 665, x + 500, 665), fill=LINE_COLOR, width=2)

        # Practical examples
        draw_centered_text(d, (x + 275, 705), ex1, get_font(18, True), INK)
        draw_centered_text(d, (x + 275, 765), ex2, get_font(17), MUTED)

    # Connecting arrows from central principle to cards
    arrow_color = "#94A3B8"
    for target_x in (350, 900, 1450):
        d.line((900, 275, target_x, 325), fill=arrow_color, width=3)
        d.polygon([(target_x - 8, 320), (target_x + 8, 320), (target_x, 338)], fill=arrow_color)

    # -------------------------------------------------------------
    # 3. Equivalence Theorem Banner
    # -------------------------------------------------------------
    draw_card(d, (120, 890, 1680, 1060), "#FFFFFF", LINE_COLOR, radius=22, width=2)
    draw_centered_text(d, (WIDTH / 2, 930), "THE ASYMPTOTIC EQUIVALENCE THEOREM", get_font(22, True), INK)
    draw_centered_text(d, (WIDTH / 2, 982), "A function f(n) is Θ(g(n))  ⟺  f(n) is both O(g(n)) AND Ω(g(n))",
                       get_font(25, True), "#4C1D95")
    draw_centered_text(d, (WIDTH / 2, 1024), "Upper Bound (O) + Lower Bound (Ω) together establish a definitive Tight Bound (Θ)",
                       get_font(18), MUTED)

    # -------------------------------------------------------------
    # 4. Growth Rate Graph (Semi-Logarithmic)
    # -------------------------------------------------------------
    draw_card(d, (120, 1090, 1680, 1640), "#FFFFFF", LINE_COLOR, radius=22, width=2)
    draw_centered_text(d, (WIDTH / 2, 1130), "COMPARISON OF COMMON ASYMPTOTIC GROWTH RATES", get_font(24, True), INK)
    draw_centered_text(d, (WIDTH / 2, 1164), "Values plotted on a logarithmic vertical axis (y = log₁₀(value)) to visualize exponential divergence",
                       get_font(17), MUTED)

    left, top, right, bottom = 270, 1215, 1560, 1485

    # Axis Labels
    d.text((left - 85, top - 26), "Value (log₁₀)", font=get_font(17, True), fill=INK)

    # Horizontal decades (1 to 10,000)
    for decade in range(5):
        y = bottom - decade * (bottom - top) / 4
        d.line((left, int(y), right, int(y)), fill="#E2E8F0", width=2)
        d.text((left - 70, int(y) - 12), f"10^{decade}", font=get_font(16), fill=MUTED)

    # Coordinate Axes
    d.line((left, top, left, bottom), fill="#475569", width=3)
    d.line((left, bottom, right, bottom), fill="#475569", width=3)
    draw_centered_text(d, ((left + right) / 2, 1540), "Input Size (n)", get_font(20, True), INK)

    # X-axis ticks (n = 1..10)
    for n in range(1, 11):
        x = left + (n - 1) * (right - left) / 9
        d.line((int(x), bottom, int(x), bottom + 8), fill="#475569", width=2)
        d.text((int(x) - 6, bottom + 12), str(n), font=get_font(16), fill=MUTED)

    # Growth rate curves
    chart_curves = [
        ("Linear: n", [n for n in range(1, 11)], COLORS["O"]),
        ("Linearithmic: n log₂ n", [max(1, n * log2(n)) for n in range(1, 11)], COLORS["Omega"]),
        ("Quadratic: n²", [n * n for n in range(1, 11)], COLORS["Theta"]),
        ("Exponential: 2ⁿ", [2 ** n for n in range(1, 11)], COLORS["Exp"]),
    ]

    for name, values, color in chart_curves:
        pts = []
        for i, val in enumerate(values):
            x = left + i * (right - left) / 9
            log_val = min(4, max(0, log10(val)))
            y = bottom - log_val * (bottom - top) / 4
            pts.append((int(x), int(y)))
        # Draw smooth line
        d.line(pts, fill=color, width=5, joint="curve")
        # Draw node markers
        for px, py in pts:
            d.ellipse((px - 5, py - 5, px + 5, py + 5), fill="#FFFFFF", outline=color, width=3)

    # Legend
    legend_x = 340
    for name, _, color in chart_curves:
        d.line((legend_x, 1595, legend_x + 36, 1595), fill=color, width=5)
        d.ellipse((legend_x + 14, 1591, legend_x + 22, 1599), fill="#FFFFFF", outline=color, width=2)
        d.text((legend_x + 46, 1583), name, font=get_font(18, True), fill=INK)
        legend_x += 295

    image.save(OUT, "PNG", optimize=True)

    # Terminal output matching lab execution style
    print("=" * 60)
    print("    ASYMPTOTIC GROWTH & NOTATION ANALYSIS (UNIT 1)")
    print("=" * 60)
    print("Analyzing Polynomial Function: f(n) = 3n^2 + 2n + 1")
    print("  - Highest-Order Dominant Term : n^2")
    print("  - Asymptotic Upper Bound      : O(n^2)")
    print("  - Asymptotic Lower Bound      : Omega(n^2)")
    print("  - Asymptotically Tight Bound  : Theta(n^2)")
    print("-" * 60)
    print("Growth Rates for Sample Input (n = 10):")
    print(f"  - Linear        : n          = 10")
    print(f"  - Linearithmic  : n log2(n)  = {10 * log2(10):.2f}")
    print(f"  - Quadratic     : n^2        = {10**2}")
    print(f"  - Exponential   : 2^n        = {2**10}")
    print("Hierarchy : n < n log2(n) < n^2 < 2^n")
    print("-" * 60)
    print(f"Visualization graphic successfully generated: {OUT.name}")
    print("=" * 60)


if __name__ == "__main__":
    main()
