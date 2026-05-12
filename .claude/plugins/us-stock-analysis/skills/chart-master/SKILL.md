# Chart Master

Generate professional financial charts and visualizations for investment analysis across multiple formats and platforms.

## Usage

```
/chart-master [TICKER] [--type <chart-type>] [--format html|mermaid|ascii] [--period 1M|3M|6M|1Y|5Y]
```

## Supported Chart Types

1. moving-averages: Price with MA20/MA50/MA200 overlays
2. volume-analysis: Volume bars with average volume reference
3. rsi-macd: RSI and MACD indicator panels
4. revenue-trend: Annual/quarterly revenue growth
5. margin-analysis: Gross/operating/net margin trends
6. valuation-comparison: P/E, EV/EBITDA vs. peers and history
7. portfolio-allocation: Sector/asset class pie/donut charts
8. fair-value-range: Bull/base/bear valuation football field
9. signal-dashboard: Multi-signal summary gauge
10. support-resistance: Key price levels map
11. earnings-history: EPS beat/miss history
12. histogram: Return distribution

## Platform Detection

Auto-detect target environment and select optimal rendering:

| Platform | Preferred Format |
|---|---|
| Claude web / claude.ai | Mermaid diagrams |
| HTML report output | Chart.js interactive |
| VS Code / IDE | Mermaid or ASCII |
| Terminal | ASCII fallback |

## Rendering Formats

### HTML/Chart.js (Interactive - Preferred for Reports)
Uses Chart.js library via CDN. Produces interactive charts with hover tooltips, responsive layout, and print-friendly CSS.

### Mermaid Diagram
Suitable for markdown environments and claude.ai. Use xychart-beta for bar/line combinations.

### ASCII Terminal Chart
```
Price (52-Week Range)
High $XXX |              /---\
          |          /---/   \--
Mid  $XXX |      /---/
          |  /---/
Low  $XXX |--/
          +--------------------
           Jan Feb Mar Apr May
```

## Design Standards

Color Coding:
- Price line: blue (#2196F3)
- MA50: amber (#FF9800)
- MA200: red (#F44336)
- Bullish/positive: green (#4CAF50)
- Bearish/negative: red (#F44336)
- Neutral: gray (#9E9E9E)

Chart Elements:
- Always include axis titles and units
- Add data labels for bar charts
- Include legend for multi-series charts
- Annotate key events (earnings, splits, guidance)
- Responsive layout (100% width containers)

## Integration with Other Skills

Chart Master accepts data from:
- /fundamental-analysis: Financial metrics tables
- /technical-analysis: Price and indicator data
- /dcf-valuation: Valuation range outputs
- /report-generator: Embeds charts in HTML report

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
