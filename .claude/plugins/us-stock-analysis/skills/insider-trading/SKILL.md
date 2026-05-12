# Insider Trading Analysis

Analyze SEC Form 4 insider trading filings to identify investment signals and behavioral patterns from corporate insiders.

## Usage

```
/insider-trading TICKER [--period 6M|12M|24M] [--threshold 100000]
```

## Data Sources
- SEC EDGAR (primary; official Form 4 filings)
- OpenInsider.com (free; easy filtering)
- InsiderMonkey.com (aggregated smart money)
- Bloomberg / FactSet (institutional premium)

## Ten Analysis Areas

### 1. Transaction Summary (6-12 months)
| Transaction Type | Count | Total Value | Avg Size |
|---|---|---|---|
| Open Market Purchases (P) | [n] | $[val] | $[val] |
| Open Market Sales (S) | [n] | $[val] | $[val] |
| Option Exercises (M) | [n] | $[val] | $[val] |
| 10b5-1 Plan Sales | [n] | $[val] | $[val] |

### 2. Sentiment Analysis
Net Sentiment Ratio = (Buy Value - Sale Value) / (Buy Value + Sale Value)
- +0.8 to +1.0: Strongly Bullish
- +0.4 to +0.8: Bullish
- -0.4 to +0.4: Neutral
- -0.8 to -0.4: Bearish
- -1.0 to -0.8: Strongly Bearish

Exclude routine 10b5-1 plan sales from sentiment calculation.

### 3. Significant Transactions
Flag transactions that are:
- Greater than $1M in value, OR
- Greater than 10% of insider's total holdings
- All CEO or CFO purchases (regardless of size)

### 4. Insider Categories (signal strength)
1. Executive Officers (CEO, CFO, COO, CTO): Strongest signal
2. Board Directors: Strong signal, especially for purchases
3. VP and Other Officers: Moderate signal
4. 10%+ Shareholders: Weaker signal (often passive or activist)

### 5. Transaction Type Interpretation

| Form 4 Code | Description | Signal Weight |
|---|---|---|
| P | Open market purchase | HIGH (bullish) |
| S | Open market sale | MEDIUM (bearish) |
| M | Option exercise | LOW (neutral) |
| A | Award/grant | Very Low (neutral) |

### 6. Ownership Trend
Track quarterly insider ownership %:
- Rising: Increasing alignment with shareholders (bullish)
- Stable: Normal maintenance
- Declining: Potential concern if sustained and large

### 7. Timing Analysis
- Trades relative to 52-week high/low positioning
- Trades during market corrections (contrarian buying = bullish)
- Pattern of buying at lows and selling at highs

### 8. Pattern Recognition

Bullish Patterns:
- Clustered buying (3+ insiders buying within 30 days)
- CEO purchase during weak stock period
- CFO purchase (knows financials intimately)
- Buying after a 30%+ drawdown

Bearish Patterns:
- Coordinated multi-insider selling
- CEO/CFO liquidating large % of stake
- Selling immediately after lockup expiration
- Decreasing insider ownership 4 consecutive quarters

### 9. Red Flags
- CEO selling >50% of stake without disclosed reason
- Multiple C-suite departures combined with selling
- Selling pattern preceding earnings misses

### 10. Context Assessment
Important caveats:
- One sale is not necessarily bearish (insiders sell for many reasons)
- Buying is more informative than selling
- Small routine sales < $100K typically carry little signal
- Cluster buys are the most reliable bullish signal

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
