# Portfolio Review

Assess overall portfolio performance, allocation, risk profile, and provide rebalancing recommendations.

## Usage

```
/portfolio-review [paste holdings] [--benchmark SPY|QQQ|custom]
```

Provide holdings as: TICKER SHARES or TICKER WEIGHT%

## Analysis Components

### 1. Performance Metrics
- Absolute return (1M, 3M, YTD, 1Y, 3Y, 5Y)
- Risk-adjusted returns: Sharpe ratio, Sortino ratio, Calmar ratio
- Alpha vs. benchmark
- Maximum drawdown and recovery time
- Win rate and average win/loss

### 2. Asset Allocation Analysis
- Sector weights vs. benchmark weights
- Market cap distribution (Large/Mid/Small)
- Geographic exposure (Domestic/International)
- Style tilts (Growth/Value/Blend)
- Factor exposures (momentum, quality, low-vol, size)

### 3. Risk Assessment
- Portfolio beta vs. benchmark
- Volatility (annualized standard deviation)
- Correlation matrix of top holdings
- Concentration risk (top 5/10 holdings %)
- Drawdown scenarios (-10%, -20%, -30%, -50%)

### 4. Diversification Analysis
- Effective number of positions (1 / sum of weight^2)
- Sector concentration (Herfindahl-Hirschman Index)
- Redundancy check (highly correlated holdings)
- Missing exposures relative to benchmark

### 5. Income Analysis
- Portfolio yield (weighted dividend yield)
- Dividend growth rate (weighted)
- Income stability assessment
- Tax efficiency (qualified vs. ordinary income)

## Optimization Recommendations

### Rebalancing Needs
Identify positions that have drifted beyond +/-5% of target weight.

### Diversification Gaps
Flag missing sectors (>5% underweight vs. benchmark).

### Performance Enhancement
- Identify underperformers (trailing benchmark by >10% over 12M)
- Flag overconcentrated positions (>10% of portfolio)
- Tax-loss harvesting opportunities

### Risk Reduction
- Hedge recommendations for concentrated positions
- Defensive additions for late-cycle positioning
- Correlation reduction suggestions

## Output Format

Portfolio Summary: Total value, number of positions, benchmark comparison (YTD alpha), Sharpe ratio vs. benchmark

Allocation Dashboard:
| Sector | Weight | Benchmark | Over/Under |
|---|---|---|---|
| [sector] | [%] | [%] | [+/-] |

Risk Profile: Conservative / Moderate / Aggressive

Top 3 Recommendations:
1. Action with rationale
2. Action with rationale
3. Action with rationale

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
