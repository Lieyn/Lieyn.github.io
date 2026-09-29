---
title: "Quantifying Risk in Chess Sacrifices"
date: 2026-07-30
draft: false
math: true
tags: ["research", "econometrics", "chess", "bayesian"]
summary: ""
---

<!--
=============================================================================
THIS IS THE METHODS POST. It is separate from 2026-04-27 and the boundary is
strict in BOTH directions:

  2026-04-27 uses the headline number as evidence for a conceptual claim about
  bounded rationality. It never explains how the number was produced.

  THIS POST explains how the number was produced. It never re-argues bounded
  rationality. If you find yourself writing "satisficing" or "aspiration
  level" here, cut it and link to the April post instead.

Different readers. If they overlap, one of them is redundant and a reader will
notice.

The paper is under review at IJHSR. Write this as a public explanation of work
already done, not as a preprint. No claim here should exceed what the paper
claims.
=============================================================================
-->

## The question

<!--
A sacrifice is a decision to give up guaranteed material for uncertain
positional compensation. That is an investment under uncertainty with a
clean, observable payoff — which is rare in behavioral data and is the whole
reason chess is a usable lab here.

State the question in one sentence: does decision quality under this kind of
uncertainty improve with expertise, and by how much.
-->

## Data

<!--
~75,000 TWIC classical games. 35,830 sound balanced sacrifices after filtering.
Stockfish (UCI) evaluation.

Be explicit about what "balanced" and "sound" mean operationally — a reader
cannot evaluate the result without the filter definitions. This is where most
readers will decide whether to trust the rest.
-->

## The model

<!--
Bayesian investor setup: private signal about position quality, posterior
update, commit more when the posterior favors success.

Keep the formalism minimal. State what the model predicts BEFORE showing the
regression — a prediction stated after the fact is not a prediction.
-->

## Identification

<!--
THE SECTION THAT MATTERS MOST AND THE ONE MOST READERS SKIP. Make it readable.

  - Cluster-robust OLS. Say what the clusters are and WHY errors are correlated
    within them. A reader who doesn't know the technique should still follow
    the reason for it.
  - eval_before as a control: without it, rating correlates with the KINDS of
    positions a player reaches, and the estimate absorbs position selection
    rather than decision quality. Say this plainly — it is the single most
    important design choice in the paper.
-->

## Result

<!--
~1.5 centipawns per 100 rating points. p ≈ 10^-45. R² = 0.705.

Then, immediately, the discipline:

  - The p-value is a function of n = 35,830. At that sample size it is close to
    uninformative about effect importance. Say so before a reviewer does.
  - R² = 0.705 is mostly eval_before doing work. It is NOT "the model explains
    70% of decision quality." State what it actually reflects.
  - 1.5cp is small in absolute terms. Argue for why it matters anyway — or
    concede that it's modest. Do not inflate it.
-->

## Limitations

<!--
Own these plainly rather than burying them:
  - Observational. Rating is not randomly assigned.
  - Stockfish evaluation is a proxy for ground-truth position quality, not
    identical to it.
  - TWIC is tournament classical play — a selected population, not chess
    players in general.
  - Sound/balanced filters are defensible but not the only defensible choices.

The reason to write this section well: it is the part chú Thao's "simplest
clean result first" discipline is actually about. A result stated with its
limits is a stronger claim than the same result stated without them.
-->

## Related work

<!--
Gerdes & Gränsmark (2010) and Gränsmark (2012) — the existing economics-of-
chess literature using chess as a risk-preference lab. Precedent for the whole
approach; flagged to chú Thao for the paper's related-work section.

One short paragraph here. This post is not a survey.
-->
