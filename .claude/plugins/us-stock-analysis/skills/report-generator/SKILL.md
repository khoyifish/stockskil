# Report Generator

Generate professional HTML investment reports with interactive Chart.js visualizations from financial analysis data.

## Usage

```
/report-generator TICKER [--template executive|comprehensive|portfolio] [--output ./reports/]
```

Accepts: Structured JSON data, markdown analysis output from other skills, CSV/spreadsheet data.

## Report Templates

### Executive Summary (1-2 pages)
Target audience: Busy stakeholders, portfolio managers
- Investment signal and conviction level
- 5 key metrics dashboard
- Bull/bear case in 2 bullets each
- Price target range
- Risk factors (top 3)

### Comprehensive Analysis (5-10 pages)
Target audience: Analysts, detailed due diligence
- Full financial statement analysis
- Technical charts with multiple indicators
- DCF valuation with sensitivity tables
- Peer comparison tables
- All signal blocks from integrated skills

### Portfolio Review
Target audience: Portfolio management
- Multi-stock comparison table
- Allocation analysis charts
- Risk-adjusted performance metrics
- Rebalancing recommendations

## Visualization Components

Financial Charts:
- Line chart: Revenue and earnings trends (dual Y-axis)
- Bar chart: Annual/quarterly comparisons
- Stacked area: Revenue breakdown by segment
- Waterfall: FCF bridge analysis

Valuation Charts:
- Football field: Valuation range across methods
- Grouped bar: P/E, EV/EBITDA vs. peers
- Scatter: Growth vs. valuation (PEG visualization)

Technical Charts:
- Candlestick + MA overlays (MA20/50/200)
- RSI panel
- MACD panel with histogram
- Volume bars with average reference

Portfolio Charts:
- Pie/donut: Sector and asset allocation
- Bar: Return attribution
- Heat map: Correlation matrix

## Design Standards

Color coding (consistent across all charts):
- Positive/bullish: green (#22c55e)
- Negative/bearish: red (#ef4444)
- Neutral/caution: amber (#f59e0b)
- Price line: blue (#2196F3)
- MA50: orange (#FF9800)
- MA200: red (#F44336)

All charts include: Responsive width, axis titles with units, legend, tooltips on hover, print-friendly CSS.

## PDF Export Methods

Browser (simplest): Ctrl+P -> "Save as PDF"

Command Line (wkhtmltopdf):
```
wkhtmltopdf --page-size A4 report.html report.pdf
```

Node.js (Playwright):
```javascript
const page = await browser.newPage();
await page.goto('file://' + reportPath);
await page.pdf({ path: 'report.pdf', format: 'A4', printBackground: true });
```

## Output File
Filename format: investment-report-[TICKER]-[YYYYMMDD]-[HHMMSS].html
Self-contained: No external dependencies except Chart.js CDN

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
