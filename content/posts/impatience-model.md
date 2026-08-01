---
title: "What I Got Wrong About Screen Time and Discount Rates"
date: 2026-07-31
draft: true
math: true
tags: ["research", "behavioral-economics", "modeling"]
categories: ["research"]
summary: "I built a model expecting digital exposure to amplify impatience in the tail. It couldn't have, and the mechanism I was testing turned out to be statistically inert."
ShowToc: true
TocOpen: false
---

<!--
STRUCTURE — three nested discoveries (each one undercuts the last):
  1. What I expected: tail amplification
  2. What I found: it was architecturally impossible
  3. What that revealed: the mechanism was statistically inert

Write the prose yourself. The headers below are the skeleton.
Do NOT publish until the citation checks at the bottom are cleared.
-->

## The setup

<!--
What the model is: hyperbolic discount rate k as a function of digital exposure,
two-state Markov chain calibrated to Nelson et al. (2021).
State the model plainly. Define k. Say what "exposure" means operationally.
Keep this short — the interesting part is what breaks.
-->

The hyperbolic discounting model values a reward $R$ received at delay $t$ as

$$
V(t) = \frac{R}{1 + k t}
$$

where $k$ is the discount rate — higher $k$ means steeper preference for the immediate.

<!-- Then: the two-state chain. Transition matrix. Calibration source. -->

## What I expected to find

<!--
The hypothesis: exposure doesn't just shift mean impatience, it fattens the
right tail — a small group gets pulled to extreme k.
Say why that seemed plausible. Be honest that it seemed like the interesting result.
-->

## Why it couldn't happen

<!--
THE TURN. The 1/sqrt(N) scaling argument.
Averaging over N periods shrinks the variance of the realized exposure share,
so the tail can't widen the way I assumed — this is a mathematical consequence
of the model's architecture, not an empirical finding about people.
Show the algebra. This is the part worth reading.
-->

## The robustness sweep

<!--
What you varied, over what ranges, and what stayed flat.
Table goes here. Include the parameter grid.
-->

| Parameter | Range swept | Effect on tail |
|---|---|---|
| <!-- fill --> | | |

## Honest limitations

<!--
- Calibration rests on self-reported exposure
- Two-state chain is a coarse approximation of a graded process
- No empirical validation against panel data
- The result is about the model, not about adolescents
-->

## What I'd do differently

<!-- Short. One paragraph. -->

---

**Materials:** [OSF preprint](#) · [simulation code](#)

<!--
=== BLOCKERS BEFORE PUBLISHING — verify each yourself ===
[ ] Hollenbeck et al. — confirm DOI resolves
[ ] Nelson et al. (2021) — confirm summary stats match what the chain is calibrated to
[ ] Schulz van Endert & Mohr — confirm the correlation coefficient as cited
[ ] Zhang et al. — confirm the 24.58% figure
[ ] Simulation code matches Appendix A of the writeup
[ ] Prose is your own writing throughout
-->
