---
title: "Formalizing the Secretary Problem in Lean 4"
date: 2026-09-20
draft: false
math: true
tags: ["lean", "formalization", "optimal stopping"]
summary: ""
---

<!--
=============================================================================
ON HOLD. DO NOT WRITE THIS POST YET. The blocker is mathematical, not
editorial.

BLOCKER: the unimodality / sign-change lemma for the finite-n success
probability P(r,n). Until that lemma is proven, the optimality of the
threshold rule is a NUMERICALLY VERIFIED CONJECTURE, not a theorem. Writing
the post before the lemma closes means either overclaiming or writing a post
whose central claim is "I checked some cases."

SCOPED DELIVERABLE (Stage 1 only) — this is a complete piece of work on its own:
  finite-n closed form for P(r,n) + unimodality + optimal threshold.

STRETCH (Stage 2): asymptotic n/e convergence via Mathlib's harmonic/log
machinery. Cite as a classical result; do not commit to proving it.

THE C++ TWIN is what makes this legible to a reader who can't parse Lean:
  Tier 0 — validate the closed form numerically
  Tier 1 — Bayesian prior variant via DP
  Tier 2 — noisy observation variant
The proof and the simulation make the same claim from two directions, one
symbolic and exact, one empirical and visual. Show both or the post only
reaches readers who already read Lean.

Date is a placeholder. Move it when the lemma closes.
=============================================================================
-->
