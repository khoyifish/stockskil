# Full Report

Generate a comprehensive, professional HTML investment report by orchestrating all 15 analysis modules for a given stock ticker.

## Usage

```
/full-report TICKER [--lang en|zh-tw|zh-cn|ja] [--output ./reports/]
```

## Analysis Modules Executed (Sequential)

1. Company overview and business model evaluation
2. Financial statement analysis (10-K/10-Q data)
3. Technical pattern and indicator analysis
4. DCF intrinsic value estimation
5. Comparable company (comps) analysis
6. Competitive positioning and moat assessment
7. Sector trends and macro positioning
8. Macroeconomic factor analysis
9. Insider trading activity review
10. Institutional ownership and 13F analysis
11. Earnings call sentiment and themes
12. Regulatory filing (10-K/10-Q) deep read
13. Dividend sustainability analysis
14. Short interest and squeeze potential
15. Options market signals and positioning

## Output: Self-Contained HTML Report

File naming: TICKER_report_YYYY-MM-DD.html
Location: output/ directory (or specified path)
Dependencies: Chart.js via CDN only (no local dependencies)

### Report Structure

1. Hero Header: Ticker, company name, report date, overall signal
2. Table of Contents: Sticky navigation sidebar
3. Executive Summary: 3-5 bullet investment thesis
4. Section per Module: Each of 15 modules with key findings, Chart.js visualizations, and investment signal block
5. Composite Verdict: Weighted synthesis of all 15 modules
6. Risk Summary: Top 5 risks with severity ratings
7. Disclaimer: Educational use only, not financial advice

### Visualization Components
- Moving average overlays (Candlestick + MA20/50/200)
- Revenue and earnings growth charts
- Margin trend analysis
- Valuation football field (fair value range)
- Peer comparison grouped bar charts
- Institutional ownership treemap
- Signal dashboard summary

### Composite Scoring Weights

| Module | Weight |
|---|---|
| Fundamental Analysis | 20% |
| DCF Valuation | 15% |
| Technical Analysis | 10% |
| Comparable Valuation | 10% |
| Competitive/Moat Analysis | 10% |
| Insider Activity | 8% |
| Institutional Ownership | 8% |
| Earnings Call | 7% |
| Sector/Macro | 7% |
| Short Interest + Options | 5% |

### Multi-language Support
- English (default): --lang en
- Traditional Chinese: --lang zh-tw
- Simplified Chinese: --lang zh-cn
- Japanese: --lang ja

## Report Characteristics
- Interactive Chart.js visualizations with hover tooltips
- Sticky table of contents for easy navigation
- Color-coded analysis (green/amber/red for bullish/neutral/bearish)
- Print-friendly CSS formatting
- Responsive layout for desktop and mobile
- Each section has its own standardized signal block

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This report is for educational purposes only and does not constitute financial advice.*
