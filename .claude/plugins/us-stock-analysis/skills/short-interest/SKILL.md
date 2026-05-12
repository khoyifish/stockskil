# Short Interest Analysis

Evaluate short selling activity, squeeze potential, and bearish positioning in US-listed stocks.

## Usage

```
/short-interest TICKER [--squeeze-check] [--history 12M]
```

## Data Sources
- FINRA Short Interest reports (bi-monthly; as of 15th and last business day)
- Published ~4-5 business days after settlement date (~2-week total lag)
- S3 Partners (real-time borrow rates and short interest)
- Ortex (predictive short interest using settlement data)
- IBKR Shortable Stocks List (borrow availability and rates)

Important: Short interest data reflects past positioning, not current. FINRA data has ~2-week delay.

## Four Primary Metrics

### 1. Short Float %
Shares sold short / Total float shares outstanding

| Level | Signal |
|---|---|
| < 2% | Negligible short interest |
| 2-5% | Low short interest |
| 5-10% | Moderate (normal for contested stocks) |
| 10-20% | High; notable bearish conviction |
| 20-30% | Very high; significant short thesis |
| > 30% | Extreme; potential squeeze target |

### 2. Days to Cover (DTC) / Short Interest Ratio
Short Interest / Average Daily Trading Volume

| DTC | Squeeze Risk |
|---|---|
| < 1 day | Very Low |
| 1-3 days | Low |
| 3-7 days | Moderate |
| 7-15 days | High |
| > 15 days | Very High |
| > 20 days | Extreme squeeze conditions |

### 3. Borrow Rate (Fee)
Annualized cost for short sellers to borrow shares:

| Rate | Classification | Signal |
|---|---|---|
| < 1% | General Collateral (GC) | Easy to short; low squeeze risk |
| 1-5% | Mild difficulty | Modest friction |
| 5-15% | Hard to Borrow | Notable friction; rising squeeze risk |
| 15-30% | Very Hard to Borrow | High squeeze risk |
| > 30% | Extreme / Recall Risk | Forced covering likely |

### 4. Squeeze Score (0-10 composite)
Combines: Short float %, DTC, catalyst presence, price momentum, float size, borrow cost

## High-Probability Squeeze Requirements

All three conditions must be present simultaneously:
1. High short interest: Short float > 15% AND DTC > 7
2. Catalyst or forced covering trigger: Earnings beat, buyout, short squeeze news
3. Limited downside floor: Fundamental or technical support preventing shorts from waiting out

## Short Interest Trend Analysis

Track changes over 6-12 months:
| Date | Short Interest (M shares) | Short Float % | DTC | Borrow Rate |
|---|---|---|---|---|
| [date] | [val] | [%] | [days] | [%] |

Trend interpretation:
- Rising short interest + rising borrow rate: Bears adding conviction
- Falling short interest + falling borrow rate: Short covering (potential catalyst for price rise)
- High short interest + high borrow rate + positive catalyst: Classic squeeze setup

## Bearish Thesis Assessment

When high short interest exists, consider:
- What is the fundamental thesis for shorts?
- Is the bear thesis already well-known (priced in)?
- How have prior short squeezes resolved for this stock?
- Is the short thesis based on valuation, fraud concern, or business model weakness?

## Integration with Other Signals
Short interest is most valuable when combined with:
- Insider buying (insiders buy while shorts pile on = contrarian bullish)
- Institutional accumulation (smart money vs. smart shorts)
- Options market (elevated put buying confirms short thesis)
- Earnings surprise potential (beats can force rapid short covering)

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
