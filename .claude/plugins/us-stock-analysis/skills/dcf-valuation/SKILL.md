# DCF Valuation

Perform disciplined Discounted Cash Flow analysis to estimate a stock's intrinsic value.

Core question: "What is this business actually worth based on future cash generation?"

## Usage

```
/dcf-valuation TICKER [--scenarios] [--sensitivity]
```

## Seven-Step DCF Process

### Step 1: Establish Baseline Metrics
- TTM Revenue, EBITDA, Net Income
- TTM Free Cash Flow = Operating CF minus Capex
- FCF margin (FCF / Revenue)
- Net debt (Total Debt minus Cash)
- Shares outstanding (diluted, including SBC)

### Step 2: Project Revenue Growth (10 Years)
Use multiple anchors:
- Historical revenue CAGR (3, 5, 10 years)
- Analyst consensus estimates (years 1-3)
- Industry growth rate benchmarks
- TAM expansion / contraction analysis
- Management guidance and track record

### Step 3: Model FCF Margins
- Operating leverage: margin expansion potential
- Capex intensity by business model type
- R&D as percent of revenue trend
- SBC as real dilutive cost (must be included)
- Working capital changes

### Step 4: Calculate Terminal Value

Gordon Growth Model (preferred for stable businesses):
```
Terminal Value = FCF_10 x (1 + g) / (WACC - g)
```
Where g = long-term growth rate (typically 2-3%, not to exceed GDP growth)

Exit Multiple Method (alternative):
```
Terminal Value = EBITDA_10 x EV/EBITDA_exit_multiple
```

Rule: Terminal value should not exceed 70% of enterprise value.

### Step 5: Calculate WACC

Cost of Equity (CAPM):
```
Ke = Rf + Beta x (Rm - Rf) + Size/Specific Premium
```
- Rf = 10-year Treasury yield
- Beta = levered beta (5-year monthly, sector-adjusted)
- Equity Risk Premium: 5-6% for US markets

Cost of Debt:
```
Kd(after-tax) = Interest Expense / Total Debt x (1 - Tax Rate)
```

WACC:
```
WACC = Ke x (E/V) + Kd x (D/V)
```

### Step 6: Discount to Present Value
```
PV = Sum [FCF_t / (1 + WACC)^t] + Terminal Value / (1 + WACC)^10
Enterprise Value = PV of FCFs + PV of Terminal Value
Equity Value = Enterprise Value - Net Debt
Intrinsic Value per Share = Equity Value / Diluted Shares
```

### Step 7: Sensitivity Analysis
5x5 grid (WACC vs. Terminal Growth Rate):

| WACC \ g | 1.0% | 1.5% | 2.0% | 2.5% | 3.0% |
|---|---|---|---|---|---|
| 6% | $XXX | $XXX | $XXX | $XXX | $XXX |
| 7% | $XXX | $XXX | $XXX | $XXX | $XXX |
| 8% | $XXX | $XXX | $XXX | $XXX | $XXX |
| 9% | $XXX | $XXX | $XXX | $XXX | $XXX |
| 10% | $XXX | $XXX | $XXX | $XXX | $XXX |

## Three-Scenario Modeling (Required)

| Scenario | Probability | Revenue CAGR | FCF Margin | WACC | Terminal g |
|---|---|---|---|---|---|
| Bull | 25% | [high] | [high] | [low] | [high] |
| Base | 50% | [mid] | [mid] | [mid] | [mid] |
| Bear | 25% | [low] | [low] | [high] | [low] |

Probability-weighted intrinsic value = Bull x 0.25 + Base x 0.50 + Bear x 0.25

Margin of Safety = (Intrinsic Value - Current Price) / Intrinsic Value

## Common Pitfalls (Avoid These)

1. Extrapolating recent high growth too far forward
2. Terminal value > 70% of enterprise value
3. WACC set artificially low (inflates intrinsic value)
4. Ignoring stock-based compensation
5. Failing to normalize FCF through business cycles
6. Using GAAP earnings instead of true FCF
7. Ignoring off-balance-sheet liabilities

## Best Fit
DCF works best for: stable, mature, cash-generative businesses with predictable FCF.
Use relative valuation instead for: early-stage, high-growth, highly cyclical companies.

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
