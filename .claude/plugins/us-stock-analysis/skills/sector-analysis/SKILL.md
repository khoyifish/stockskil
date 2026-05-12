# Sector Analysis

Analyze US market sector performance, rotation dynamics, and identify allocation opportunities across the 11 S&P 500 GICS sectors.

## Usage

```
/sector-analysis [SECTOR|all] [--cycle] [--rotation]
```

Sectors: XLK (Tech), XLV (Healthcare), XLF (Financials), XLY (Consumer Disc.), XLP (Consumer Staples), XLE (Energy), XLI (Industrials), XLB (Materials), XLRE (Real Estate), XLU (Utilities), XLC (Communication)

## Analysis Dimensions

### 1. Sector Performance Metrics
- Absolute returns (1W, 1M, 3M, YTD, 1Y)
- Relative strength vs. S&P 500
- Earnings growth rate and revisions
- Revenue growth trends
- Valuation multiples (P/E, forward P/E vs. historical)
- Dividend yield vs. 10-year average

### 2. Economic Cycle Positioning

| Cycle Phase | Leading Sectors | Lagging Sectors |
|---|---|---|
| Early Recovery | Financials, Consumer Disc., Tech | Utilities, Staples |
| Mid-cycle | Industrials, Materials, Energy | Utilities, Staples |
| Late Cycle | Energy, Materials, Healthcare | Consumer Disc., Tech |
| Recession | Utilities, Staples, Healthcare | Energy, Financials |

### 3. Fundamental Valuation
For each sector, assess:
- Current P/E vs. 10-year average
- Forward P/E vs. S&P 500 premium/discount
- EPS growth forecast (next 12 months)
- Revenue growth forecast
- Margin trajectory
- Analyst revision trend (upgrades vs. downgrades)

### 4. Macroeconomic Drivers

| Sector | Key Macro Drivers |
|---|---|
| Financials | Yield curve slope, credit growth, regulatory environment |
| Real Estate | Interest rates, cap rates, credit availability |
| Utilities | Interest rates, regulatory environment, renewable transition |
| Energy | Oil/gas prices, rig count, geopolitical factors |
| Materials | China PMI, USD strength, commodity cycle |
| Tech | Innovation cycle, AI adoption, interest rates |
| Healthcare | Drug pricing policy, FDA pipeline, aging demographics |
| Industrials | ISM Manufacturing, fiscal spending, reshoring trends |
| Consumer Disc. | Consumer confidence, wage growth, savings rate |
| Consumer Staples | Inflation pass-through, private label competition |
| Communication | Ad spending cycle, streaming penetration, regulation |

### 5. Technical Analysis
- Relative Strength vs. SPY (13-week, 26-week)
- Sector ETF moving average status (above/below 50/200-day)
- Money flow (sector fund flows, institutional rebalancing)
- Momentum score (1-month, 3-month, 6-month returns)

## Rotation Strategy

### Identifying Rotation Opportunities
1. Find sectors with improving earnings revisions + cheap valuation
2. Identify sectors with positive macro tailwinds entering cycle phase
3. Confirm with improving relative strength vs. SPY
4. Check sector ETF fund flows for institutional confirmation

### Tactical vs. Strategic Allocation
- Tactical (3-6 months): Follow earnings revision cycle and momentum
- Strategic (12-24 months): Align with economic cycle phase

## Output Format

Sector Scorecard:
| Sector | Valuation | Momentum | Earnings | Macro | Overall |
|---|---|---|---|---|---|
| [sector] | +/=/- | +/=/- | +/=/- | +/=/- | OVERWEIGHT/NEUTRAL/UNDERWEIGHT |

Top Picks: 2-3 sectors to overweight with rationale
Avoid: 1-2 sectors to underweight with rationale
Rotation Theme: Describe current dominant rotation if any

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
