"""Redraw the three figures for content/posts/2026-06-04-tail-risk/.

Values are the ones reported in the post. Run from anywhere:
    python3 scripts/tail_risk_figures.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "content/posts/2026-06-04-tail-risk"

INK = "#1f2937"
MUTED = "#6b7280"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
REF = "#9ca3af"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10.5,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 10.5,
        "axes.edgecolor": "#c9ced6",
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": "#e5e7eb",
        "grid.linewidth": 0.7,
        "legend.frameon": False,
        "text.color": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.dpi": 220,
    }
)


def clean(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", visible=False)
    ax.tick_params(length=0)


def save(fig, name):
    fig.savefig(OUT / name, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


# Figure 1: losses rise, but bad years shrink relative to the average.
levels = ["Low\n23 bets", "Medium\n34 bets", "High\n52 bets", "Very high\n78 bets"]
x = np.arange(4)
mean = np.array([6.476275, 9.669987, 14.689963, 22.521446])
cvar = np.array([77.936105, 97.415923, 124.392396, 159.508815])
multiple = cvar / mean

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3), gridspec_kw={"wspace": 0.28})
ax = axes[0]
ax.plot(x, cvar, marker="o", ms=7, lw=2.2, color=ORANGE, label="Worst 5% of years (average)")
ax.plot(x, mean, marker="o", ms=7, lw=2.2, color=BLUE, label="All years (average)")
for xi, c, m in zip(x, cvar, mean):
    ax.annotate(f"€{c:.0f}", (xi, c), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9.5)
    ax.annotate(f"€{m:.0f}", (xi, m), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9.5)
ax.set_xticks(x, levels)
ax.set_xlim(-0.35, 3.35)
ax.set_ylim(0, 185)
ax.set_ylabel("Yearly loss (€)")
ax.set_title("A. Both kinds of loss go up")
ax.legend(loc="upper left", fontsize=9.5)
clean(ax)

ax = axes[1]
ax.plot(x, multiple, marker="o", ms=7, lw=2.2, color=BLUE)
for xi, r in zip(x, multiple):
    ax.annotate(f"{r:.1f}×", (xi, r), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=9.5)
ax.set_xticks(x, levels)
ax.set_xlim(-0.35, 3.35)
ax.set_ylim(0, 14)
ax.set_ylabel("Bad-year loss ÷ average loss")
ax.set_title("B. …but bad years shrink relative to it")
clean(ax)
save(fig, "baseline_reversal.png")


# Figure 2: wider spread of bet counts in the high group can push Q above 1.
# Eight-run averages as reported in the post (low-group spread fixed at 1.0).
sigma_h = np.array([1.0, 1.8, 2.2])
q = np.array([0.644, 0.967, 1.117])

fig, ax = plt.subplots(figsize=(8.6, 4.4))
ax.axhspan(1.0, 1.2, color="#fdeee7", zorder=0)
ax.axhline(1.0, color=INK, lw=1.2, ls=(0, (4, 3)))
ax.text(0.9, 1.012, "Q = 1", va="bottom", fontsize=9.5, color=MUTED)
ax.text(0.9, 1.17, "Above 1: worst years grow faster than the average", va="top", fontsize=9.5, color=INK)
ax.text(0.9, 0.985, "Below 1: the average grows faster", va="top", fontsize=9.5, color=INK)
ax.plot(sigma_h, q, lw=2.2, color=BLUE, zorder=2)
ax.scatter(sigma_h, q, s=64, c=[BLUE, BLUE, ORANGE], edgecolor="white", linewidth=2, zorder=3)
for s, v in zip(sigma_h, q):
    ax.annotate(f"{v:.3f}", (s, v), xytext=(10, -4), textcoords="offset points", ha="left", va="top", fontsize=9.5)
ax.set_xlim(0.85, 2.4)
ax.set_ylim(0.58, 1.2)
ax.set_xticks(sigma_h, ["1.0\n(same as low group)", "1.8", "2.2"])
ax.set_xlabel(r"Spread of bet counts in the high-activity group ($\sigma$)")
ax.set_ylabel("Q")
ax.set_title("Making the high-activity group more unequal can reverse the result")
clean(ax)
save(fig, "dispersion_boundary.png")


# Figure 3: the "moment squeeze". Categorical x because the middle case
# changes the low-group spread to 0.5.
sigmas = np.array([1.8, 2.0, 2.2])
spec_labels = ["1.8\n(low 1.0)", "2.0\n(low 0.5)", "2.2\n(low 1.0)"]
reversed_ = np.array([False, True, True])
colors = np.where(reversed_, ORANGE, BLUE)
median_if_mean_fixed = 78.0 * np.exp(-(sigmas**2) / 2)
mean_if_median_fixed = 78.0 * np.exp((sigmas**2) / 2)
nelson_median = 15.0 * 12 / 8
nelson_mean = 92.8 * 12 / 8
xs = np.arange(3)

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.5), gridspec_kw={"wspace": 0.28})

ax = axes[0]
ax.axhline(78, color=INK, lw=1.2, ls=(0, (4, 3)))
ax.text(2.55, 79.5, "Average held at 78", ha="right", va="bottom", fontsize=9.5)
ax.axhline(nelson_median, color=REF, lw=1.2)
ax.text(2.55, nelson_median + 1.5, "Real bettors' median ≈ 22.5", ha="right", va="bottom", fontsize=9.5, color=MUTED)
ax.plot(xs, median_if_mean_fixed, lw=1.6, color=REF, zorder=2)
ax.scatter(xs, median_if_mean_fixed, s=64, c=colors, edgecolor="white", linewidth=2, zorder=3)
for xi, v in zip(xs, median_if_mean_fixed):
    ax.annotate(f"{v:.0f}", (xi, v), xytext=(10, 0), textcoords="offset points", va="center", fontsize=9.5)
ax.set_xticks(xs, spec_labels)
ax.set_xlim(-0.4, 2.6)
ax.set_ylim(0, 92)
ax.set_xlabel(r"High-group spread $\sigma$")
ax.set_ylabel("Implied median bets per year")
ax.set_title("A. Hold the average: median falls")
clean(ax)

ax = axes[1]
ax.axhline(78, color=INK, lw=1.2, ls=(0, (4, 3)))
ax.text(2.55, 60, "Median held at 78", ha="right", va="top", fontsize=9.5)
ax.axhline(nelson_mean, color=REF, lw=1.2)
ax.text(2.55, nelson_mean + 15, "Real bettors' average ≈ 139", ha="right", va="bottom", fontsize=9.5, color=MUTED)
ax.plot(xs, mean_if_median_fixed, lw=1.6, color=REF, zorder=2)
ax.scatter(xs, mean_if_median_fixed, s=64, c=colors, edgecolor="white", linewidth=2, zorder=3)
for xi, v in zip(xs, mean_if_median_fixed):
    ax.annotate(f"{v:.0f}", (xi, v), xytext=(10, 0), textcoords="offset points", va="center", fontsize=9.5)
ax.set_xticks(xs, spec_labels)
ax.set_xlim(-0.4, 2.6)
ax.set_ylim(0, 960)
ax.set_xlabel(r"High-group spread $\sigma$")
ax.set_ylabel("Implied average bets per year")
ax.set_title("B. Hold the median: average soars")
clean(ax)

handles = [
    plt.Line2D([], [], ls="", marker="o", ms=8, color=BLUE, label="Result not reversed (Q < 1)"),
    plt.Line2D([], [], ls="", marker="o", ms=8, color=ORANGE, label="Result reversed (Q > 1)"),
]
fig.legend(handles=handles, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.04), fontsize=9.5)
save(fig, "moment_squeeze.png")

print(f"Wrote figures to {OUT}")
