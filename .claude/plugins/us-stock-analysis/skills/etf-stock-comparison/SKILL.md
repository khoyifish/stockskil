# ETF vs Stock Comparison

Compare owning a sector ETF against its largest constituent stock to determine which vehicle better suits an investor's goals, risk tolerance, and time horizon.

## Usage

```
/etf-stock-comparison ETF STOCK
```

Examples:
- `/etf-stock-comparison XLF JPM`   — Financial sector ETF vs JPMorgan Chase
- `/etf-stock-comparison XLE XOM`   — Energy sector ETF vs ExxonMobil
- `/etf-stock-comparison XLV UNH`   — Health Care ETF vs UnitedHealth Group

---

## Analysis Framework

### 1. Vehicle Snapshot

| Dimension        | ETF                              | Individual Stock                 |
|------------------|----------------------------------|----------------------------------|
| Type             | Passive sector basket            | Single-company equity            |
| Holdings         | 20–80+ constituents              | 1 company                        |
| Expense Ratio    | 0.09%–0.35% / year               | $0 (no ongoing fee)              |
| Rebalancing      | Automatic, rules-based           | Manual / investor-driven         |
| Dividend Policy  | Pass-through from all holdings   | Single-company dividend decision |
| Liquidity        | High (ETF bid-ask spread)        | High (stock bid-ask spread)      |

---

### 2. ETF Profile — [ETF TICKER]

#### Holdings & Concentration
- Total number of holdings
- Top 10 holdings as % of total fund (concentration risk in ETF itself)
- Target stock's weight inside the ETF (how much single-name exposure already exists)
- Sector/sub-industry breakdown
- Market-cap tilt (mega/large/mid/small)

#### Cost Structure
- Expense ratio (annual fee drag in basis points)
- 10-year fee drag impact on $10,000 invested
- Bid-ask spread (typical daily)
- Premium/discount to NAV history

#### Distributions
- 30-day SEC yield / trailing dividend yield
- Distribution frequency (quarterly / monthly)
- Qualified dividend % (tax efficiency)
- Capital gains distribution history (tax drag)

#### Tracking & Liquidity
- AUM and daily average volume ($M)
- Tracking error vs. index (annualized)
- Short-sale availability / options market depth

---

### 3. Individual Stock Profile — [STOCK TICKER]

#### Business Quality
- Revenue and earnings growth (3-year CAGR)
- Operating margin vs. sector median
- Return on Equity (ROE) and Return on Invested Capital (ROIC)
- Free cash flow yield
- Balance sheet: Net Debt/EBITDA, interest coverage

#### Valuation
- P/E (trailing and forward) vs. sector ETF implied multiple
- EV/EBITDA vs. sector peers
- Price/Free Cash Flow
- PEG ratio (growth-adjusted)

#### Dividend & Capital Return
- Dividend yield and 5-year growth rate (CAGR)
- Payout ratio (sustainability)
- Buyback yield (shares repurchased / market cap)
- Total shareholder yield (dividend + buyback)

#### Risk Factors
- Single-company idiosyncratic risks (regulatory, litigation, management, competition)
- Earnings estimate revision trend (last 3 months)
- Analyst consensus: % Buy / Hold / Sell, price target range
- Short interest (% float)
- Beta vs. S&P 500

---

### 4. Head-to-Head Comparison

#### Performance Scorecard

| Metric                    | [ETF]   | [Stock] | Edge      |
|---------------------------|---------|---------|-----------|
| 1-Year Total Return       | [%]     | [%]     | [ETF/Stock/Tie] |
| 3-Year Annualized Return  | [%]     | [%]     | [ETF/Stock/Tie] |
| 5-Year Annualized Return  | [%]     | [%]     | [ETF/Stock/Tie] |
| YTD Return                | [%]     | [%]     | [ETF/Stock/Tie] |
| Max Drawdown (3Y)         | [%]     | [%]     | [ETF/Stock/Tie] |
| Annualized Volatility (3Y)| [%]     | [%]     | [ETF/Stock/Tie] |
| Sharpe Ratio (3Y)         | [val]   | [val]   | [ETF/Stock/Tie] |
| Dividend Yield (current)  | [%]     | [%]     | [ETF/Stock/Tie] |
| Expense Ratio / Cost      | [%]     | 0%      | Stock     |

#### Diversification Impact
- Correlation of stock to ETF (high correlation = ETF adds little diversification)
- Stock's weight in ETF: owning ETF + stock creates concentration; owning only ETF may be sufficient if weight is large
- Unsystematic risk reduction from ETF basket vs. single name

#### Tax Efficiency
- ETF: in-kind creation/redemption mechanism minimizes capital gains distributions
- Stock: capital gains only realized upon sale; losses harvestable on demand
- Qualified dividends: compare % qualified for each vehicle
- Winner: depends on investor tax bracket and holding period

#### Dividend Comparison
- ETF yield vs. stock yield (nominal)
- ETF yield smoothing effect (blend of all holdings)
- Stock: higher yield possible if top dividend payer in sector
- Growth trajectory: which has faster dividend CAGR?

---

### 5. Investor Profile Fit

#### Choose the ETF if:
- You want sector exposure without single-stock concentration risk
- You are a passive or index-oriented investor
- You prefer automatic rebalancing as sector composition shifts
- The target stock is already a large ETF weight (>10%), so ETF gives meaningful stock exposure anyway
- You are in an early accumulation phase and want broad diversification

#### Choose the Individual Stock if:
- You have high conviction that this company will outperform the sector
- The stock trades at a meaningful discount to intrinsic value vs. sector peers
- You want maximum dividend yield from the sector's top income payer
- You prefer avoiding ETF expense ratios on a large, long-term position
- You can actively monitor business fundamentals and want flexibility to exit on deterioration
- Tax-loss harvesting flexibility matters to you

#### Split Position Consideration:
- Own both ETF + individual stock for combined sector tilt with alpha opportunity
- Suggested weight: 60–70% ETF / 30–40% stock for balanced approach
- Rebalance trigger: if stock grows to >20% of combined position, trim to target

---

### 6. Specific Pair Analyses

---

#### XLF vs. JPM — Financials

**XLF (Financial Select Sector SPDR Fund)**
- Tracks the Financial Select Sector Index (~70 holdings)
- Top holdings: JPM (~12%), BAC (~9%), WFC (~7%), GS (~5%), MS (~4%)
- JPM alone = ~12% of XLF; owning XLF provides JPM exposure plus diversification into banks, insurers, capital markets, and consumer finance
- Expense ratio: 0.09% — among the cheapest sector ETFs
- Key risk: correlated to yield curve shape, credit cycles, and bank regulation

**JPM (JPMorgan Chase)**
- Largest US bank by assets; dominant in investment banking, consumer banking, and asset management
- Superior ROE vs. peers (~15%+); consistent dividend grower
- Higher idiosyncratic upside (alpha on execution, capital allocation) vs. ETF
- Higher idiosyncratic downside: regulatory fines, credit losses, specific management decisions
- Dividend yield typically 2–3%; buyback program adds 2–4% total return annually

**Key Trade-off:** If you believe JPM will continue to outperform the broader financial sector, own JPM directly. If you want financial sector exposure without betting on one bank's execution, XLF is the cleaner vehicle. Note: XLF's ~12% JPM weight means buying XLF gives you substantial JPM exposure alongside BAC, WFC, GS, MS, and insurers.

**Verdict Framework:**
- Bull case on JPM specifically → JPM
- Neutral on financials broadly → XLF
- Bearish on other large banks but bullish on JPM → JPM (avoids BAC/WFC dilution)

---

#### XLE vs. XOM — Energy

**XLE (Energy Select Sector SPDR Fund)**
- Tracks the Energy Select Sector Index (~20–25 holdings)
- Top holdings: XOM (~25%), CVX (~18%), EOG (~5%), SLB (~4%), PXD (~4%)
- XOM alone = ~25% of XLE; significant single-name concentration
- Expense ratio: 0.09%
- Exposure: integrated majors, E&P, oilfield services, midstream
- Key driver: WTI/Brent crude and natural gas prices

**XOM (ExxonMobil)**
- World's largest publicly traded oil major by market cap
- Integrated model: upstream (E&P), downstream (refining), chemicals
- Balance sheet discipline post-2020 restructuring; attractive free cash flow yield at $70+ WTI
- Dividend aristocrat: 40+ years of consecutive dividend increases
- Pioneer Resources acquisition (2024) dramatically expanded Permian Basin position
- Higher beta to oil prices than XLE due to pure-play concentration

**Key Trade-off:** XOM is ~25% of XLE, so XLE gives you significant XOM exposure diluted by CVX and smaller E&P names. If you want maximum crude oil leverage with dividend income, XOM directly may outperform. If you want energy sector exposure hedged across diversified sub-industries (services, midstream), XLE is preferable.

**Verdict Framework:**
- High-conviction oil bull → XOM (pure-play major)
- Sector rotation into energy broadly → XLE (diversified exposure)
- Want oilfield services or midstream participation → XLE (holds SLB, Williams, etc.)

---

#### XLV vs. UNH — Health Care

**XLV (Health Care Select Sector SPDR Fund)**
- Tracks the Health Care Select Sector Index (~60 holdings)
- Top holdings: UNH (~10%), LLY (~9%), JNJ (~7%), ABBV (~5%), MRK (~4%)
- Diverse sub-sectors: managed care, pharma, biotech, med devices, health services
- Expense ratio: 0.09%
- Defensive characteristics: low cyclicality, consistent earnings in recessions

**UNH (UnitedHealth Group)**
- Largest US health insurer and healthcare services company
- Two engines: UnitedHealthcare (insurance) + Optum (data, pharmacy, care delivery)
- Consistent 15%+ EPS growth over 10 years; strong free cash flow conversion
- Premium multiple justified by growth: trades at ~20–25x forward earnings
- Key risks: drug pricing legislation, medical loss ratio (MLR) spikes, ACA regulatory changes
- Weight in XLV (~10%) — meaningful exposure but diluted by pharma/biotech names

**Key Trade-off:** UNH has historically outperformed XLV significantly due to superior earnings growth vs. the broader healthcare basket. However, UNH carries managed care regulatory risk (Medicare Advantage reimbursement cuts) that XLV's pharma/biotech holdings do not share. XLV's inclusion of LLY (GLP-1 drugs) and biotech adds different growth exposure.

**Verdict Framework:**
- Conviction on managed care + Optum growth story → UNH directly
- Want healthcare defensiveness without single-company regulatory risk → XLV
- Want exposure to GLP-1/obesity drug theme → XLV (LLY weight) or split position

---

### 7. Decision Matrix

Score each criterion 1–3 (1 = ETF preferred, 2 = tie, 3 = Stock preferred):

| Criterion               | Weight | Score | Notes |
|-------------------------|--------|-------|-------|
| Diversification need    | 25%    | [1-3] | High need → ETF |
| Conviction in company   | 25%    | [1-3] | High conviction → Stock |
| Cost sensitivity        | 10%    | [1-3] | Long-term large position → Stock |
| Dividend yield priority | 15%    | [1-3] | Compare actual yields |
| Tax efficiency          | 10%    | [1-3] | ETF in taxable; stock in tax-deferred |
| Valuation discount      | 15%    | [1-3] | Stock cheap vs. peers → Stock |

**Weighted Score:**
- 1.0–1.7 → ETF preferred
- 1.8–2.3 → Split position (60/40 or 70/30)
- 2.4–3.0 → Individual stock preferred

---

## Standard Signal Output

For each pair (ETF and Stock separately):

**[ETF TICKER]**
- Signal:     BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon:    SHORT / MEDIUM / LONG-TERM
- Score:      X.X / 10
- Action:     BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

**[STOCK TICKER]**
- Signal:     BULLISH / NEUTRAL / BEARISH
- Confidence: HIGH / MEDIUM / LOW
- Horizon:    SHORT / MEDIUM / LONG-TERM
- Score:      X.X / 10
- Action:     BUY / HOLD / SELL
- Conviction: STRONG / MODERATE / WEAK

**Relative Preference:** [ETF / STOCK / SPLIT] — [one-sentence rationale]

*This analysis is educational and not financial advice.*
