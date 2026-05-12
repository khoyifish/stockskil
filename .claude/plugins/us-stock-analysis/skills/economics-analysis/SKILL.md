# US Economics Analysis

Assess current US macroeconomic conditions and their investment implications across asset classes and sectors.

## Usage

```
/economics-analysis [--focus inflation|rates|growth|sentiment]
```

## Core Indicator Categories

### 1. Growth Metrics
- GDP growth rate (QoQ, YoY, annualized)
- ISM Manufacturing & Services PMI (>50 = expansion)
- Nonfarm Payrolls and unemployment rate
- Consumer spending (PCE, retail sales)
- Industrial production and capacity utilization

### 2. Inflation Measures
- CPI (headline and core, MoM and YoY)
- PCE deflator (Fed's preferred measure)
- PPI (leading indicator for CPI)
- Wage growth (Average Hourly Earnings)
- Inflation expectations (5y5y breakeven, Michigan survey)

### 3. Monetary Policy
- Fed Funds Rate (current, target range)
- FOMC dot plot and forward guidance
- Balance sheet (QT/QE status and pace)
- Money supply (M2 growth)
- Real interest rates (nominal minus inflation expectations)

### 4. Market Sentiment
- Conference Board Consumer Confidence
- University of Michigan Sentiment Index
- NFIB Small Business Optimism
- Credit spreads (IG and HY)
- VIX (fear gauge)

### 5. Fiscal Policy
- Federal budget deficit/surplus
- Government spending trajectory
- Tax policy changes
- Debt ceiling status
- Treasury issuance calendar

## Key Analytical Tools

### Yield Curve Analysis
The 3M10Y spread is the historically strongest recession predictor:
- Normal (3M10Y > 0): Healthy growth expectations
- Flat (near 0): Slowing growth
- Inverted (3M10Y < 0): Recession warning; inversions lasting 6-12 months typically precede recessions by 6-15 months
- Re-steepening after inversion often signals imminent contraction

### Credit Market Signals

| Spread Level | Signal |
|---|---|
| IG spreads < 100 bps | Healthy risk appetite |
| IG spreads 100-150 bps | Moderate caution |
| HY spreads < 300 bps | Risk-on environment |
| HY spreads > 500 bps | Distress / risk-off |

Note: HY spreads lead equity markets by 2-4 weeks on average.

### Real Yield Framework
- Real yield < 0%: Favorable for growth assets, gold, risk-on
- Real yield 0-2%: Neutral; balanced asset allocation
- Real yield > 2%: Meaningful financial tightening; defensive positioning

### Recession Signal Tools (cross-confirm all three)
1. NY Fed 3M10Y Model: Probability derived from yield curve
2. Conference Board LEI: Leading Economic Index trend
3. Sahm Rule: Triggered when 3-month unemployment average rises 0.5pp above 12-month low

## Economic Cycle Positioning

| Cycle Phase | Characteristics | Favored Sectors |
|---|---|---|
| Early Recovery | Rising PMI, low rates | Cyclicals, Financials, Tech |
| Mid-cycle | Peak growth, rising rates | Industrials, Materials |
| Late Cycle | Slowing growth, high rates | Energy, Staples, Healthcare |
| Recession | Contraction, falling rates | Utilities, Staples, Gold |

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
