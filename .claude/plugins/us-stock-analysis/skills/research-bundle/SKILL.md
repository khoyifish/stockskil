# Research Bundle

Run a comprehensive multi-phase stock analysis and generate a unified investment thesis with a composite score.

## Usage

```
/research-bundle TICKER [--skip technical] [--quick] [--compare PEER1,PEER2] [--visual]
```

## Five Analysis Phases

### Phase 1: Business and Competitive Foundation (Weight: 25%)
Runs: /competitor-analysis + /fundamental-analysis

Deliverables:
- Business quality score (1-10)
- Moat rating: Wide / Narrow / None
- Financial health assessment
- Key competitive advantages identified

### Phase 2: Valuation (Weight: 25%)
Runs: /dcf-valuation + /stock-valuation

Deliverables:
- DCF intrinsic value range (Bull/Base/Bear)
- Comparable company valuation range
- Price target: $[low] - $[high]
- Margin of safety: [%]
- Valuation verdict: Undervalued / Fair / Overvalued

### Phase 3: Market Signals (Weight: 20%)
Runs: /insider-trading + /institutional-ownership + /earnings-call-analysis

Deliverables:
- Insider sentiment: Bullish / Neutral / Bearish
- Institutional trend: Accumulating / Stable / Distributing
- Earnings call tone: Confident / Cautious / Concerning
- Smart money alignment: Aligned / Mixed / Against

### Phase 4: Technical Timing (Weight: 15%)
Runs: /technical-analysis

Deliverables:
- Trend direction: Uptrend / Sideways / Downtrend
- Entry setup quality: Strong / Moderate / Weak
- Key support and resistance levels
- Optimal entry zone: $[low] - $[high]

### Phase 5: Risk Assessment (Weight: 15%)
Runs: /short-interest + /options-analysis

Deliverables:
- Short interest signal: Low / Moderate / High / Extreme
- Squeeze potential: High / Medium / Low / None
- Options market sentiment: Risk-on / Neutral / Risk-off
- Risk profile: Low / Moderate / High / Very High

## Composite Scoring

| Phase | Weight | Score (0-10) | Weighted Score |
|---|---|---|---|
| Business Quality | 25% | [val] | [val] |
| Valuation | 25% | [val] | [val] |
| Market Signals | 20% | [val] | [val] |
| Technical Timing | 15% | [val] | [val] |
| Risk Profile | 15% | [val] | [val] |
| Composite | 100% | | [val] |

Interpretation Scale:
| Score | Rating |
|---|---|
| 8.0-10.0 | Strong Buy |
| 6.5-7.9 | Buy |
| 5.0-6.4 | Hold / Accumulate on weakness |
| 3.5-4.9 | Reduce / Underweight |
| 0.0-3.4 | Sell / Avoid |

## Conflict Resolution Rules

1. Fundamental overrides technical: Strong business quality takes precedence over short-term price action
2. Majority rule: When 4 of 5 phases align, the outlier does not dominate
3. All conflicts documented explicitly
4. Time horizon matters: Technical bearish + fundamental bullish = "accumulate on weakness over 6-12 months"

## Output Format

Investment Thesis (3-5 sentences): Synthesize why this is/isn't a good investment.

Bull Case:
- Key catalyst / upside driver -> Price target: $[val]

Bear Case:
- Key risk / downside driver -> Floor estimate: $[val]

Entry Strategy:
- Ideal entry zone: $[low] - $[high]
- Position sizing: [%] of portfolio
- Stop loss: $[val]
- Scale-in approach: immediate / 3 tranches / wait for pullback

Monitoring Plan: Key metrics to track quarterly

Exit Criteria:
- Target reached: Sell at $[val]
- Thesis broken: Exit if [specific condition]
- Stop loss: Exit if price closes below $[val]

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
