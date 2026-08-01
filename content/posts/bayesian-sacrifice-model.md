---
title: "A Bayesian Model of the Chess Sacrifice"
date: 2026-07-20
draft: true
math: true
tags: ["chess", "decision-theory", "modeling"]
categories: ["research"]
summary: "A sacrifice is a bet on your own future information. Here's what that looks like written down."
ShowToc: true
TocOpen: false
---

<!--
STRUCTURE:
  setup → the informational framing → the model → what it predicts →
  what the data says → where the model fails
-->

## The question

<!--
A sacrifice gives up certain material for uncertain compensation.
The standard framing is "is it sound?" — but soundness is engine-relative.
The decision-theoretic framing: what does the player believe, and how does
that belief update over the next few plies?
-->

## Setup

Let $\theta$ be the true evaluation of the position after the sacrifice, and let the player hold a prior

$$
\theta \sim \mathcal{N}(\mu_0, \sigma_0^2)
$$

<!--
Then: each ply of calculation is a noisy signal. Precision scales with skill.
Write out the posterior update. This is where stronger players separate:
not a different prior, a tighter likelihood.
-->

## What the model predicts

<!--
Prediction 1: conditional on position quality, stronger players sacrifice more
Prediction 2: the value of a sacrifice grows with the observation horizon
State these as falsifiable claims before showing data.
-->

## Against the data

<!--
Reference the empirical paper. Key numbers:
  - 75K TWIC classical games
  - 35,830 sound balanced sacrifices
  - +1.5 cp per 100 rating points (eval_before controlled, cluster-robust SEs by game_id)
  - conversion 32.7 → 55.3 cp across 4 → 6 plies
Do NOT overstate. Selection effect, not a causal claim about skill.
-->

## Where this breaks

<!--
- Gaussian priors are a convenience, not a claim about cognition
- Engine eval as ground truth is itself a modeling choice
- The 8-ply horizon was dropped — say why honestly
-->

---

**Related:** full paper — *Risk-Taking, Information, and Sacrifices in Chess* (with Thao Vuong). <!-- link when live -->
