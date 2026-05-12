# Stock Valuation

Determine intrinsic stock value using a multi-method triangulation approach across five primary valuation techniques.

## Usage

```
/stock-valuation TICKER [--methods dcf,comps,ev-ebitda] [--scenarios]
```

## Core Philosophy

Never rely on a single valuation method. Triangulate across multiple approaches and use the range as your "fair value zone" rather than a precise point estimate.

## Five Primary Valuation Methods

### Method 1: Discounted Cash Flow (DCF)
Best for: Mature, cash-generative businesses with predictable FCF

Process:
1. Establish baseline FCF (TTM) and FCF margin
2. Project revenue and FCF for 10 years (3 scenarios)
3. Calculate terminal value (Gordon Growth Model)
4. Discount at WACC
5. Sensitivity: 5x5 WACC vs. terminal growth grid

Key rule: Terminal value should not exceed 70% of enterprise value.

### Method 2: Comparable Company Analysis (Comps)
Best for: Any publicly traded company with available peers

Process:
1. Select 5-8 peer companies (similar industry, business model, growth, size)
2. Calculate peer multiples: EV/Revenue, EV/EBITDA, P/E, P/FCF
3. Compute peer median for each multiple
4. Apply to target's metrics with premium/discount adjustment
5. Weight multiples by relevance to this business

Premium/Discount Drivers:
- Apply premium for: Higher growth, wider moat, better management, lower leverage
- Apply discount for: Lower growth, narrowing moat, higher risk, governance concerns

### Method 3: EV/EBITDA Multiple
Best for: Quick sanity check; capital-intensive businesses

Process:
1. Calculate current EV (Market Cap + Net Debt + Minority Interest - Cash)
2. Get trailing and forward EBITDA
3. Compare to 5-year historical average, sector median, S&P 500 median
4. Assess at what EV/EBITDA the stock represents fair value

### Method 4: Price/Earnings Ratio
Best for: Stable, growing businesses; consumer staples, financials

Process:
1. Trailing P/E and forward P/E
2. PEG ratio = Forward P/E / Earnings Growth Rate (PEG < 1 = potentially cheap)
3. Compare to 5-year average P/E and sector median
4. Normalize earnings for cyclical distortions

### Method 5: Residual Income Model (RIM)
Best for: Financial institutions (banks, insurance)

Process:
1. Book value per share as starting point
2. Project excess returns (ROE - Cost of Equity) for 5-10 years
3. Terminal residual income
4. Discount to present value
5. Intrinsic value = Book Value + PV of excess returns

## Football Field (Valuation Range Visualization)

| Method | Bear Value | Base Value | Bull Value |
|---|---|---|---|
| DCF | $[low] | $[mid] | $[high] |
| EV/EBITDA comps | $[low] | $[mid] | $[high] |
| P/E comps | $[low] | $[mid] | $[high] |
| P/FCF comps | $[low] | $[mid] | $[high] |
| Composite | $[low] | $[mid] | $[high] |

Current Price: $[price]
Margin of Safety (Base): [%]
Upside/Downside to Base: [%]

## Probability-Weighted Value

Composite Intrinsic Value = (Bull x 25%) + (Base x 50%) + (Bear x 25%)

Conviction Determination:
- Margin of Safety > 30%: Strong Buy signal
- Margin of Safety 15-30%: Buy signal
- Margin of Safety 0-15%: Hold / Accumulate on weakness
- Overvalued 0-15%: Reduce / Trim
- Overvalued > 15%: Sell / Avoid

## Analyst Consensus Comparison

| Source | Price Target | Upside/Downside | Rating |
|---|---|---|---|
| Average | $[val] | [%] | Buy/Hold/Sell |
| High | $[val] | [%] | |
| Low | $[val] | [%] | |
| Your estimate | $[val] | [%] | |

Identify where your estimate diverges from consensus and why.

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
