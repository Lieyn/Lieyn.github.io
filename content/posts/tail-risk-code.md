---
title: "Code — Why More Bets Can Reduce Relative Tail Risk"
date: 2026-06-04
draft: false
math: false
build:
  list: never
  render: always
ShowToc: true
ShowReadingTime: false
---

Source excerpts referenced in [Why More Bets Can Reduce Relative Tail Risk](/posts/2026-06-04-tail-risk/).

## CRN decomposition (Python)

```python
# impatience_simulation.py, lines 306–327
def decomposition(
    spec: ModelSpec, scenarios: list[Scenario], n_paths: int = 500_000
) -> pd.DataFrame:
    """Separate frequency and post-loss-response channels."""
    low, high = scenarios[0], scenarios[-1]
    cases = {
        "Low reference": low,
        "Frequency only": Scenario(
            "Frequency only", high.x, high.bets, low.p_chase
        ),
        "Escalation only": Scenario(
            "Escalation only", high.x, low.bets, high.p_chase
        ),
        "Combined": high,
    }
    rows = []
    common_seed = SEED + 500_000
    for name, s in cases.items():
        losses = simulate_paths(spec, s, n_paths, common_seed)
        rows.append(
            {
                "case": name,
                "bets": s.bets,
                "p_chase": s.p_chase,
                **summarize(losses),
            }
        )
    table = pd.DataFrame(rows)
    table.to_csv(OUT / "decomposition.csv", index=False)
    return table
```

## Exact wager loop (C++)

```cpp
// random_count_exact.cpp, lines 77–108 (inside simulate)
for (std::size_t i = 0; i < paths; ++i) {
  std::uint64_t n;
  if (sigma_count == 0.0) {
    n = static_cast<std::uint64_t>(std::llround(target_count));
  } else {
    double raw = std::exp(mu_count + sigma_count * normal(rng));
    n = std::max<std::uint64_t>(1, std::llround(raw));
    n = std::min(n, count_cap);
  }
  count_sum += n;
  count_sum_sq += static_cast<long double>(n) * n;
  count_max = std::max(count_max, n);

  bool elevated = false;
  double net = 0.0;
  for (std::uint64_t t = 0; t < n; ++t) {
    double stake = elevated ? elevated_stake(rng) : normal_stake(rng);
    bool win = uniform(rng) < q_win;
    net += win ? payout_multiple * stake : -stake;
    elevated = (!win) && (uniform(rng) < p_chase);
  }
  losses.push_back(-net);
}

long double loss_sum =
    std::accumulate(losses.begin(), losses.end(), 0.0L);
double mean = static_cast<double>(loss_sum / paths);
std::sort(losses.begin(), losses.end());
std::size_t tail_start = static_cast<std::size_t>(std::floor(0.95 * paths));
long double tail_sum = std::accumulate(
    losses.begin() + tail_start, losses.end(), 0.0L);
double cvar95 = static_cast<double>(tail_sum / (paths - tail_start));
```

*The complete source first calibrates $\mu$ by bisection so that rounding produces the target mean count. `count_cap` is a sentinel set orders of magnitude above any realized draw in the reported experiment, so it never actively constrains `n`; the 5,000-count cap discussed in the main post belonged only to the separate review harness. This excerpt therefore runs every realized wager and computes CVaR from the exact upper 5% by rank.*
