# Competitor Analysis

Evaluate a company's competitive position, economic moat, and industry dynamics to support investment decisions.

## Usage

```
/competitor-analysis TICKER [--peers PEER1,PEER2,PEER3]
```

## Five Sources of Economic Moat (Morningstar Framework)

For each moat source, assess: Present? Strength (Wide/Narrow/None)? Trend (Widening/Stable/Narrowing)?

1. Network Effects: Value increases as more users join (marketplaces, social platforms)
2. Cost Advantages: Structural cost savings vs. peers (scale, process, location, unique assets)
3. Intangible Assets: Brands, patents, regulatory licenses, proprietary data
4. Switching Costs: Customer lock-in through data, integrations, training, contracts
5. Efficient Scale: Niche market; new entrants cannot profitably enter

Moat Width Classification:
- Wide Moat: 20+ year durability; ROIC significantly exceeds WACC
- Narrow Moat: 10-20 year durability; moderate ROIC/WACC spread
- No Moat: Commodity dynamics; ROIC approximately equals WACC

Critical insight: Moat trend matters most - widening, stable, or narrowing?

## Porter's Five Forces Analysis

Score each force 1-5 (1 = low intensity/favorable, 5 = high intensity/unfavorable):

### Competitive Rivalry (weight: 25%)
- Number and size of competitors
- Industry growth rate
- Product differentiation
- Exit barriers
- Price competition intensity

### Threat of New Entrants (weight: 25%)
- Capital requirements
- Economies of scale
- Brand identity / loyalty
- Access to distribution
- Regulatory barriers

### Bargaining Power of Suppliers (weight: 15%)
- Supplier concentration
- Switching costs
- Supplier differentiation
- Threat of forward integration

### Bargaining Power of Buyers (weight: 20%)
- Buyer concentration
- Price sensitivity
- Switching costs
- Threat of backward integration

### Threat of Substitutes (weight: 15%)
- Availability of substitutes
- Switching costs to substitutes
- Relative price/performance

Industry Attractiveness Score = Weighted average (lower = more attractive)

## Competitive Benchmarking

Select 5-8 peers by: similar industry, business model, growth profile, market cap (+/-50%)

| Metric | Company | Peer 1 | Peer 2 | Peer 3 | Peer Median |
|---|---|---|---|---|---|
| Revenue Growth | [%] | [%] | [%] | [%] | [%] |
| Gross Margin | [%] | [%] | [%] | [%] | [%] |
| EBITDA Margin | [%] | [%] | [%] | [%] | [%] |
| ROIC | [%] | [%] | [%] | [%] | [%] |
| R&D / Revenue | [%] | [%] | [%] | [%] | [%] |
| P/E | [val] | [val] | [val] | [val] | [val] |
| EV/EBITDA | [val] | [val] | [val] | [val] | [val] |

## Market Share and Pricing Power
- Current market share (%)
- Market share trend (gaining/holding/losing)
- Pricing power test: can the company raise prices without losing volume?

## Innovation and Management Quality
- R&D investment as % of revenue vs. peers
- Patent portfolio strength and expiry profile
- Product pipeline / roadmap assessment
- Management tenure and capital allocation track record
- Insider ownership alignment

## Valuation Impact
Moat directly drives valuation premium/discount:
- Wide moat widening: Justify 20-30% P/E premium to sector
- Narrow moat stable: Sector-average multiple
- Moat narrowing: Discount regardless of near-term earnings

## Standard Signal Output

Signal block:
- Signal: BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon: SHORT / MEDIUM / LONG-TERM
- Score: X.X / 10 (Moat composite)
- Action: BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
