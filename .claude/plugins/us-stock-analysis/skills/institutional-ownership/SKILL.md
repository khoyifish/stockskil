# Institutional Ownership Analysis

Track SEC 13F filings and identify investment signals from institutional investor activity.

## Usage

```
/institutional-ownership TICKER [--track BERKSHIRE,SEQUOIA] [--period 4Q]
```

## Data Sources
- SEC EDGAR 13F filings (primary; 45-day lag after quarter-end)
- WhaleWisdom.com (13F aggregation and analytics)
- GuruFocus.com (notable investor tracking)
- Bloomberg / FactSet (real-time institutional data)
- 13F filing windows: May 15, Aug 15, Nov 15, Feb 15

Note: 13F data reflects positions as of quarter-end, filed up to 45 days later.

## Core Analysis Areas

### 1. Institutional Ownership Overview

| Metric | Value |
|---|---|
| Total Institutional Ownership % | [%] |
| Total Institutions Holding | [n] |
| Net Change (QoQ) | [+/-] shares |
| Institutions Buying | [n] |
| Institutions Selling | [n] |
| New Positions | [n] |
| Eliminated Positions | [n] |

### 2. Top Holder Identification and Categorization

| Institution | Type | Shares | Value | QoQ Change | % of Portfolio |
|---|---|---|---|---|---|
| [inst] | Index/Active/Passive | [n] | $[val] | [+/-] | [%] |

Categorize holders:
- Index funds (Vanguard, BlackRock, State Street): Passive; low signal
- Active managers: Higher signal; analyze conviction vs. benchmark weight
- Hedge funds / Concentrated funds: Highest signal; especially high-conviction positions

### 3. Quarter-Over-Quarter Position Changes

Initiations (new positions - bullish signal):
- Institution: [name], Shares: [n], Value: $[val]

Significant Increases (>10% position increase):
- Institution: [name], Prior: [n], Current: [n], Change: [+%]

Significant Decreases (>10% position decrease):
- Institution: [name], Prior: [n], Current: [n], Change: [-%]

Eliminations (complete exits - bearish signal):
- Institution: [name], Shares Sold: [n], Value: $[val]

### 4. Smart Money Tracking

Track notable investors: Warren Buffett / Berkshire, Bill Ackman / Pershing Square, Seth Klarman / Baupost Group, and other relevant names per industry.

For each tracked investor: Is their position growing, stable, or declining?

### 5. Ownership Concentration Metrics
- Top 10 institutions hold [%] of shares
- Top 20 institutions hold [%] of shares
- Overlap with S&P 500 index weight (over/under-owned vs. index)

### 6. Activist Investor Positions
- Any 13D/13G filings (>=5% stake)?
- Activist campaign status (settled, ongoing, proposed)
- Historical activist outcomes at this company

### 7. High-Conviction Signals

Strongest bullish signals:
- Smart money initiating/building position
- Multiple quality institutions adding simultaneously
- High conviction: position >5% of manager's portfolio
- Buying during price weakness over multiple quarters

Strongest bearish signals:
- Smart money eliminating entire stake
- Multiple quality institutions exiting simultaneously
- Total institutional ownership declining for 3+ consecutive quarters

### 8. Comparison to Index Weight
If in S&P 500:
- Index weight: [%]
- Institutional ownership relative to index: Over/Under/Market-weight
- Institutional "crowding" risk if heavily over-owned

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
