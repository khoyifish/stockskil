# US Stock Evaluation Framework

Perform a comprehensive evaluation of a US stock ticker across fundamental, valuation, quality, and risk dimensions.

## Usage

```
/stock-eval TICKER [--visual]
```

## Core Analysis Components

### 1. Company Overview
- Business model and revenue streams
- Competitive positioning and moat assessment
- Market size and growth opportunity
- Industry dynamics and disruption threats
- Geographic exposure

### 2. Financial Health
- Revenue growth (1/3/5-year CAGR)
- Profitability trends (gross, operating, net margins)
- Balance sheet strength (debt/equity, current ratio)
- Cash flow generation (FCF margin, FCF conversion)
- Working capital management

### 3. Valuation Metrics
- P/E, Forward P/E, PEG ratio
- EV/EBITDA, EV/Sales
- Price/Book, Price/FCF
- Comparison to 5-year historical averages
- Peer group multiple comparison

### 4. Quality Scoring

**Piotroski F-Score (0–9)**
Evaluates nine binary criteria:
- Profitability: ROA > 0, Operating CF > 0, ROA improving, Accruals < 0
- Leverage/Liquidity: Debt ratio declining, Current ratio improving, No dilution
- Operating Efficiency: Gross margin improving, Asset turnover improving

Score interpretation:
- 8–9: Strong financial health (Bullish)
- 6–7: Moderate quality (Neutral-Bullish)
- 3–5: Average quality (Neutral)
- 0–2: High deterioration risk (Bearish)

**Earnings Quality Score**
- Accruals ratio (lower = higher quality)
- Cash conversion rate (Operating CF / Net Income)
- Non-recurring items identification

### 5. ROIC vs. WACC Analysis
- Calculate ROIC (NOPAT / Invested Capital)
- Estimate WACC using CAPM
- EVA Spread = ROIC − WACC
- Sustained ROIC > WACC = value creation

### 6. DCF Valuation
- Project 10-year FCF (Bull/Base/Bear scenarios)
- Apply terminal value (Gordon Growth Model)
- Discount at WACC
- Sensitivity table: WACC vs. Terminal Growth Rate
- Margin of safety = (Intrinsic Value − Market Price) / Intrinsic Value

### 7. Risk Assessment

| Risk Category | Factors |
|---------------|---------|
| Business Risk | Competitive threats, customer concentration, regulatory |
| Financial Risk | Leverage, liquidity, refinancing |
| Valuation Risk | Premium to peers, priced for perfection |
| Macro Risk | Rate sensitivity, FX exposure, cycle positioning |

## Output Format

**Investment Thesis**: 2-3 sentence summary

**Valuation**: Undervalued / Fairly Valued / Overvalued
**Quality Rating**: Excellent / Good / Average / Poor
**Management Rating**: Strong / Adequate / Weak

**Price Targets**:
- Bull Case: $XXX
- Base Case: $XXX
- Bear Case: $XXX

**Top 3 Risks**: List with severity (High/Medium/Low)

**Analyst Consensus**: Average target, Buy/Hold/Sell distribution

## Standard Signal Output

```
╔══════════════════════════════════════════════╗
║              INVESTMENT SIGNAL               ║
╠══════════════════════════════════════════════╣
║ Signal:      BULLISH / NEUTRAL / BEARISH     ║
║ Confidence:  HIGH / MEDIUM / LOW             ║
║ Horizon:     SHORT / MEDIUM / LONG-TERM      ║
║ Score:       X.X / 10                        ║
╠══════════════════════════════════════════════╣
║ Action:      BUY / HOLD / SELL               ║
║ Conviction:  STRONG / MODERATE / WEAK        ║
╚══════════════════════════════════════════════╝
```

**Score Guide**: 8.0–10.0 Strongly Bullish | 6.0–7.9 Moderately Bullish | 4.0–5.9 Neutral | 2.0–3.9 Moderately Bearish | 0.0–1.9 Strongly Bearish

*This analysis is educational and not financial advice.*
