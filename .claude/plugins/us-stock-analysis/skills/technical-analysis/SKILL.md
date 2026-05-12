# Technical Analysis

Evaluate US stock price patterns, technical indicators, and market structure to identify trade setups and price targets.

## Usage

```
/technical-analysis TICKER [--chart] [--timeframe short|medium|long]
```

## Core Analysis Areas

### 1. Chart Pattern Identification
- Reversal patterns: Head & Shoulders, Double Top/Bottom, Rounding Bottom
- Continuation patterns: Flags, Pennants, Triangles, Wedges
- Breakout/breakdown confirmation with volume

### 2. Technical Indicators

**Trend Indicators**
- Simple Moving Averages (20, 50, 200-day)
- Exponential Moving Averages (9, 21-day)
- MACD (12, 26, 9 settings): signal line, histogram, divergence
- ADX: trend strength (>25 = strong trend)

**Momentum Indicators**
- RSI (14-period): Overbought >70, Oversold <30, divergence signals
- Stochastic Oscillator: %K and %D crossovers
- Rate of Change (ROC)

**Volatility Indicators**
- Bollinger Bands (20-day, 2σ): squeeze setups, band walks
- ATR: position sizing and stop placement
- VIX correlation for broad market context

**Volume Indicators**
- On-Balance Volume (OBV): trend confirmation
- Volume Profile: Point of Control (POC), Value Area
- Accumulation/Distribution Line

### 3. Price Level Analysis
- Key support and resistance levels (horizontal, trendline)
- Fibonacci retracement levels (23.6%, 38.2%, 50%, 61.8%, 78.6%)
- Pivot points (daily, weekly, monthly)
- Gap analysis (breakaway, runaway, exhaustion)

## Multi-Timeframe Analysis

Evaluate three concurrent timeframes simultaneously:

| Timeframe | Period | Purpose |
|-----------|--------|---------|
| Long-term | Weekly | Primary trend direction |
| Medium-term | Daily | Trade setup identification |
| Short-term | 4H/1H | Entry timing |

**Alignment Score**: 0/3 (conflicting) to 3/3 (all aligned)
Rule: "Trade only in the direction of the higher timeframe trend."

## Volume Profile Analysis
- Point of Control (POC): highest volume price level
- Value Area (VA): 70% of volume range
- High Volume Nodes (HVN): strong support/resistance
- Low Volume Nodes (LVN): price tends to move quickly through

## Ichimoku Cloud Analysis
Five components: Tenkan-sen, Kijun-sen, Senkou Span A & B, Chikou Span

Signal strength matrix:
- Maximum Bullish: Price above cloud, bullish cloud, Chikou above price
- Maximum Bearish: Price below cloud, bearish cloud, Chikou below price

## Chart Output (--chart flag)

When `--chart` flag is used, provide:

### Candlestick Chart Data
```
Date       Open    High    Low     Close   Volume
[date]     [val]   [val]   [val]   [val]   [val]
```

### Moving Average Overlay
```
Date       MA20    MA50    MA200   EMA9    EMA21
[date]     [val]   [val]   [val]   [val]   [val]
```

### RSI & MACD Panel
```
Date       RSI14   MACD    Signal  Histogram
[date]     [val]   [val]   [val]   [val]
```

### ASCII Terminal Chart
```
Price Action (Last 20 Sessions)
$XXX ┤   ╭─╮
$XXX ┤ ╭─╯ ╰──╮
$XXX ┤─╯       ╰─
     └───────────
```

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

*This analysis is educational and not financial advice.*
