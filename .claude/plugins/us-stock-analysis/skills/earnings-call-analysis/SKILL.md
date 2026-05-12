# Earnings Call Analysis

Analyze earnings call transcripts to extract investment insights, management sentiment, strategic themes, and warning signs.

## Usage

```
/earnings-call-analysis TICKER [paste transcript | URL | Q1 2024]
```

## Analysis Sections

### 1. Executive Summary
- Overall call sentiment: Bullish / Neutral / Bearish
- 3-5 key takeaways for investors
- Guidance changes: Raised / Maintained / Lowered / Withdrawn
- Key surprises (positive and negative)
- Market-moving statements

### 2. Management Tone Assessment

Confidence Indicators (bullish signals):
- Specific numerical guidance (not ranges)
- Definitive language ("we will", "we are confident")
- Proactive discussion of opportunities
- Specific timelines for initiatives

Caution Signals (neutral/mixed):
- Wide guidance ranges
- Hedging language ("we expect", "we believe", "approximately")
- Frequent references to macro uncertainty

Red Flags (bearish signals):
- Evasiveness on direct questions
- Changing key performance metrics mid-stream
- Blaming macro for structural issues
- Withdrawing guidance without clear reason

### 3. Theme Extraction

Categorize and rank by frequency of mention:

| Theme | Mentions | Sentiment | Investment Implication |
|---|---|---|---|
| [theme] | [n] | +/=/- | [implication] |

Categories: Strategic initiatives, Operational performance, Market dynamics, Capital allocation

### 4. Financial Guidance Analysis

| Metric | Prior Guidance | New Guidance | Change | Vs. Consensus |
|---|---|---|---|---|
| Revenue | $X | $X | [%] | [+/-] |
| EPS | $X | $X | [%] | [+/-] |
| Gross Margin | [%] | [%] | [bps] | [+/-] |

Track guidance accuracy history: conservative, realistic, or optimistic?

### 5. Q&A Session Review
- Most frequently asked topics (rank by analyst question count)
- Quality of management responses: Detailed / Vague / Deflected
- Notable deflections or non-answers
- Recurring analyst concerns

### 6. Red Flag Checklist
- [ ] Consecutive quarters of missed guidance
- [ ] Margin deterioration without clear explanation
- [ ] Declining FCF despite revenue growth
- [ ] Key executive departure mentioned
- [ ] Changes to segment reporting
- [ ] Aggressive accounting practices noted
- [ ] Legal/regulatory issues surfaced
- [ ] Significant customer losses disclosed

### 7. Quarter-Over-Quarter Shift Analysis
Compare to prior quarter's call:
- Key topics that appeared/disappeared
- Tone shift (more/less optimistic)
- Metric definitions that changed

## Data Sources
- SEC EDGAR 8-K filings (official)
- Company investor relations pages
- Seeking Alpha transcript archive
- Bloomberg / FactSet (institutional)

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
