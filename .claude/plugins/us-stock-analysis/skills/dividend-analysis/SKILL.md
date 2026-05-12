# Dividend Analysis

Evaluate dividend safety, growth trajectory, yield attractiveness, and income optimization for US stocks.

## Usage

```
/dividend-analysis TICKER [--drip] [--compare-peers]
```

## Eight Analysis Dimensions

### 1. Dividend Safety Assessment
- Payout ratio (Dividends / EPS): Safe <60%, Caution 60-75%, Danger >75%
- Cash payout ratio (Dividends / FCF): More conservative; safe <50%
- Interest coverage ratio (EBIT / Interest): Safe >4x
- Debt/EBITDA: Safe <2.5x; leverage risk >4x
- Stress test: if earnings fall 20%/40%, can dividend be maintained?

### 2. Growth Trajectory
- 1-year dividend growth rate
- 3-year CAGR
- 5-year CAGR
- 10-year CAGR
- Dividend Aristocrat status? (25+ consecutive years of increases)
- Dividend King status? (50+ consecutive years of increases)

### 3. Yield Evaluation
- Current dividend yield (%)
- Historical yield range (5-year min/max)
- Yield vs. 10-year Treasury spread
- Yield vs. sector median
- Dividend trap check: Is high yield due to price collapse?
- Chowder Number = Current Yield + 5-Year DGR (target: >12 for high-yield, >8 for low-yield)

### 4. Payment Reliability
- Consecutive years of payments
- Consecutive years of increases
- Dividend cuts/freezes history (last 20 years)
- Recession durability: Did the dividend survive 2008-09 and 2020?

### 5. Financial Health Supporting Dividend
- FCF coverage ratio (FCF / Annual Dividends): Strong >2x, Adequate 1.5-2x, Tight <1.5x
- Balance sheet leverage trend
- Interest coverage trend
- Credit rating and outlook

### 6. Income Optimization (DRIP Analysis)
Assuming $10,000 initial investment over 10 years:

| Year | Shares | Divs Reinvested | Total Value | Yield on Cost |
|---|---|---|---|---|
| 1 | [val] | [val] | [val] | [%] |
| 5 | [val] | [val] | [val] | [%] |
| 10 | [val] | [val] | [val] | [%] |

Tax Efficiency:
- Qualified vs. ordinary dividend classification
- Holding period requirement (60 days for qualified)
- REIT/MLP special tax considerations

### 7. Peer Benchmarking

| Metric | Company | Peer 1 | Peer 2 | Sector Median |
|---|---|---|---|---|
| Yield | [%] | [%] | [%] | [%] |
| 5Y DGR | [%] | [%] | [%] | [%] |
| Payout Ratio | [%] | [%] | [%] | [%] |
| FCF Coverage | [x] | [x] | [x] | [x] |
| Chowder # | [val] | [val] | [val] | [val] |

### 8. Risk Identification
Top risks to dividend sustainability (rank by severity):
1. FCF compression from revenue risk / margin pressure
2. Leverage risk from debt maturity / rising rates
3. Regulatory / policy risk
4. Competitive pressure on core business
5. Payout ratio already elevated

## Safety Score (0-100)

| Component | Weight | Score |
|---|---|---|
| FCF coverage | 25% | [0-100] |
| Payout ratio | 20% | [0-100] |
| Debt/EBITDA | 20% | [0-100] |
| Dividend growth | 20% | [0-100] |
| Payment history | 15% | [0-100] |

Grade: A (85-100) | B (70-84) | C (55-69) | D (40-54) | F (<40)

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
