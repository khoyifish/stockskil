# Result Validator

Meta-analysis tool for evaluating the quality and confidence level of investment conclusions across five critical dimensions.

## Usage

```
/result-validator [paste analysis output]
```

Accepts: Output from any InvestSkill skill, or any investment analysis text.

## Five Validation Dimensions (20 points each, total 0-100)

### Dimension 1: Data Quality (0-20)
| Criterion | Points |
|---|---|
| Sources explicitly cited | 0-4 |
| Data recency (current quarter = 4, 1-2 years = 2, older = 0) | 0-4 |
| Completeness (all key metrics present) | 0-6 |
| Internal consistency (no contradictions) | 0-6 |

### Dimension 2: Methodology Soundness (0-20)
| Criterion | Points |
|---|---|
| Sector-appropriate techniques used | 0-5 |
| Assumptions stated explicitly | 0-5 |
| Parameters within reasonable range | 0-5 |
| Cross-validation across multiple methods | 0-5 |

### Dimension 3: Signal Consistency (0-20)
| Criterion | Points |
|---|---|
| Technical signals aligned with fundamental | 0-5 |
| Insider/institutional signals aligned | 0-5 |
| Macro tailwinds support thesis | 0-5 |
| Valuation consistent with thesis direction | 0-5 |

### Dimension 4: Risk Coverage (0-20)
| Criterion | Points |
|---|---|
| At least 3 specific downside risks identified | 0-6 |
| Bear scenario quantified | 0-6 |
| Catalysts for thesis failure identified | 0-4 |
| Risk severity rated (not just listed) | 0-4 |

### Dimension 5: Reasoning Transparency (0-20)
| Criterion | Points |
|---|---|
| Logical chain from evidence to conclusion | 0-6 |
| Contrarian perspective considered | 0-4 |
| Limitations of analysis acknowledged | 0-4 |
| Conclusion follows from evidence | 0-6 |

## Confidence Tiers

| Score | Tier | Implication |
|---|---|---|
| 85-100 | Very High | Rely on conclusion with high conviction |
| 70-84 | High | Conclusion likely sound; minor gaps |
| 55-69 | Medium | Proceed with caution; fill gaps before acting |
| 40-54 | Low | Significant gaps; do more research |
| 0-39 | Very Low | Analysis insufficient; do not act on this |

## Validation Report Format

Overall Confidence Score: [0-100] - [Very High / High / Medium / Low / Very Low]

Dimension Scores:
| Dimension | Score | Key Gaps |
|---|---|---|
| Data Quality | [/20] | [gaps] |
| Methodology | [/20] | [gaps] |
| Signal Consistency | [/20] | [gaps] |
| Risk Coverage | [/20] | [gaps] |
| Reasoning | [/20] | [gaps] |

Warnings (reduce confidence but don't fail): [list]
Red Flags (critical issues requiring remediation): [list]
Strengths (what the analysis does well): [list]

Remediation Steps (ranked by importance):
1. Most important fix
2. Second priority
3. Third priority

Adjusted Signal (if original confidence was overstated):
Original: [BULLISH/NEUTRAL/BEARISH] with [HIGH/MEDIUM/LOW] confidence
Adjusted: [BULLISH/NEUTRAL/BEARISH] with [HIGH/MEDIUM/LOW] confidence
Reason for adjustment: [explanation]

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
