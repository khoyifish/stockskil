# Financial Report Analyst

Analyze company financial filings and extract investment insights from 10-K, 10-Q, earnings releases, proxy statements, and investor presentations.

## Usage

```
/financial-report-analyst [paste 10-K or 10-Q text]
/financial-report-analyst TICKER 10-K
/financial-report-analyst TICKER 10-Q --section risk-factors
/financial-report-analyst TICKER 10-K --full
/financial-report-analyst TICKER --compare-prior
```

## Eight Analysis Phases

### Phase 1: Document Orientation
- Filing type (10-K / 10-Q / 8-K / DEF 14A)
- Reporting period and fiscal year end
- Auditor name and opinion type
- Any restatements or late filings

### Phase 2: MD&A Deep Read
- Revenue drivers and management commentary
- Margin trends and explanations
- Liquidity discussion and going-concern risk
- Forward guidance and outlook statements
- Non-GAAP reconciliations and adjustments

### Phase 3: Financial Statement Analysis

Income Statement Quality:
- Revenue recognition policy and any changes
- Gross margin trend and drivers
- Operating expense leverage or dis-leverage
- Below-the-line items (non-recurring, restructuring)
- Tax rate normalization

Balance Sheet Health:
- Working capital trend (current ratio, quick ratio)
- Inventory days, DSO, DPO trends
- Goodwill/intangibles as % of total assets
- Off-balance-sheet obligations (operating leases, pension)
- Debt maturity schedule

Cash Flow Truth:
- Operating CF vs. Net Income (quality check)
- Capex as % of revenue and depreciation
- Free cash flow trend and conversion
- Financing activities (debt issuance, buybacks, dividends)

### Phase 4: Risk Factor Assessment
- New risks added vs. prior filing
- Risks removed (positive signal or hiding concern?)
- Material changes in existing risk language
- Litigation disclosures and financial exposure

### Phase 5: Accounting Policy Review
- Critical accounting estimates and their sensitivity
- Related party transactions
- Segment reporting changes
- Revenue recognition policy details

### Phase 6: Management Tone Analysis
- Confidence indicators: specific guidance, definitive language
- Caution signals: hedging, wide ranges, uncertainty language
- Red flags: evasiveness, metric changes, blame-shifting

### Phase 7: YoY Comparison
- Revenue growth (organic vs. acquired)
- Margin expansion/contraction by segment
- EPS drivers decomposition
- Capital allocation changes

### Phase 8: Insider Activity (Form 4 signals)
- Net insider sentiment (buys vs. sells, excluding 10b5-1 plans)
- Significant transactions (>$1M or >10% of holdings)

## Output Format

Executive Summary: High-level verdict in 3-5 bullets

Financial Health Dashboard:
| Metric | Current | Prior Year | Trend |
|---|---|---|---|
| Revenue Growth | [%] | [%] | up/flat/down |
| Gross Margin | [%] | [%] | up/flat/down |
| FCF Margin | [%] | [%] | up/flat/down |
| Net Debt/EBITDA | [x] | [x] | up/flat/down |

Key Insights: Bullish / Bearish / Watch items

Red Flags Table (severity-ranked):
| Flag | Severity | Detail |
|---|---|---|
| [flag] | HIGH/MED/LOW | [detail] |

Accounting Quality Score (0-21): Score breakdown across criteria

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice. Ready to analyze - paste a filing or provide a ticker symbol.*
