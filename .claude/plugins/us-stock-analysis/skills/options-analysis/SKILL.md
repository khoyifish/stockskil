# Options Analysis

Analyze options market structure, Greeks, implied volatility dynamics, and strategy selection for US equity options.

## Usage

```
/options-analysis TICKER [--expiry YYYY-MM-DD] [--strategy] [--earnings]
```

## Core Components

### 1. Options Greeks Analysis

Delta: Directional sensitivity (call: 0 to +1, put: -1 to 0)
Gamma: Rate of delta change; highest near ATM and near expiration
Theta: Time decay - "rent paid to maintain a long options position"; accelerates in last 30 days
Vega: Implied volatility sensitivity; long options have positive vega
Rho: Interest rate sensitivity; more relevant for LEAPS

### 2. Implied Volatility Analysis

Key IV Metrics:
- Current IV (30-day)
- Historical Volatility (HV, 30-day realized)
- IV Rank (IVR) = (Current IV - 52W Low) / (52W High - 52W Low) x 100
- IV Percentile (IVP) = % of days in past year with lower IV

IV vs. HV Framework:
- IV > HV: Options relatively expensive; prefer selling premium
- IV < HV: Options relatively cheap; prefer buying premium
- IVR > 50: Elevated IV; consider credit strategies
- IVR < 20: Low IV; consider debit strategies

IV Term Structure:
- Contango (near-term IV < long-term): Normal
- Backwardation (near-term IV > long-term): Elevated fear / event risk

### 3. Strategy Selection Matrix

| Market Outlook | IV Environment | Recommended Strategy |
|---|---|---|
| Bullish | Low IV | Long calls, bull call spread |
| Bullish | High IV | Cash-secured put, bull put spread |
| Bearish | Low IV | Long puts, bear put spread |
| Bearish | High IV | Bear call spread, short call |
| Neutral | High IV | Iron condor, short straddle, short strangle |
| Neutral | Low IV | Long straddle (pre-earnings), calendar spread |
| Mildly Bullish | High IV | Covered call, short put |

### 4. Earnings Analysis

Expected Move = ATM Straddle Price (front-week expiry)
Expected Move % = Straddle Price / Stock Price x 100

Historical Earnings Move Comparison:
| Quarter | Expected Move | Actual Move | Beat/Miss |
|---|---|---|---|
| [Qx] | +/-[%] | [%] | Over/Under |

IV crush post-announcement: IV collapses 30-50% regardless of direction.

### 5. Put/Call Ratio Analysis
- P/C Ratio > 1.0: Bearish sentiment (more puts bought)
- P/C Ratio < 0.7: Bullish/complacent sentiment
- Extreme readings: contrarian signals
- Identify largest OI strikes as support/resistance levels

### 6. Risk Management

Position Sizing:
- Long options: 2-5% of portfolio per trade
- Credit spreads: 1-3% of portfolio per trade

Stop-Loss Guidelines:
- Long options: Exit at 50% of premium paid
- Credit spreads: Exit at 2x premium received

Rolling Mechanics:
- Roll when position approaches max loss
- Roll out in time (same strike, later expiry) to reduce delta risk

## Standard Signal Output

Signal: BULLISH / NEUTRAL / BEARISH
Confidence: HIGH / MEDIUM / LOW
Horizon: SHORT / MEDIUM / LONG-TERM
Score: X.X / 10
Action: BUY / HOLD / SELL
Conviction: STRONG / MODERATE / WEAK

*This analysis is educational and not financial advice.*
