# StockSkil — TradingView → SMS + Auto-Trade

Receives TradingView webhook alerts, sends you an SMS via Twilio, and places a market order on Alpaca.

## Quick start

### 1. Accounts you need
- **Alpaca**: https://alpaca.markets — free paper + live trading for US stocks
- **Twilio**: https://console.twilio.com — free trial (~$15 credit, ~100 SMS)

### 2. Install & configure

```bash
pip install -r requirements.txt
cp .env.example .env
# Fill in your keys in .env
```

### 3. Run the server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

For **local testing**, expose it publicly with [ngrok](https://ngrok.com):
```bash
ngrok http 8000
# Copy the https://xxxx.ngrok.io URL
```

For **production**, deploy to any VPS (DigitalOcean, Render, Railway, etc.).

### 4. Set up TradingView alert

In TradingView, create an alert and under **Notifications → Webhook URL** enter:
```
https://your-server.com/webhook
```

Set the **Message** body to JSON:
```json
{
  "secret": "your_secret_here",
  "symbol": "{{ticker}}",
  "action": "buy",
  "quantity": 1
}
```

Change `"action"` to `"sell"` for sell alerts. Use `{{strategy.order.action}}` if triggering from a Pine Script strategy.

### 5. Test manually

```bash
curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{"secret":"your_secret_here","symbol":"AAPL","action":"buy","quantity":1}'
```

## Environment variables

| Variable | Description |
|---|---|
| `ALPACA_API_KEY` | Alpaca API key |
| `ALPACA_SECRET_KEY` | Alpaca secret key |
| `ALPACA_LIVE` | `true` for live trading, `false` (default) for paper |
| `TWILIO_ACCOUNT_SID` | Twilio account SID |
| `TWILIO_AUTH_TOKEN` | Twilio auth token |
| `TWILIO_FROM_NUMBER` | Your Twilio phone number (E.164 format) |
| `TWILIO_TO_NUMBER` | Your personal phone number (E.164 format) |
| `WEBHOOK_SECRET` | Optional shared secret for webhook validation |

## Safety notes

- **Start with `ALPACA_LIVE=false`** (paper trading) until you've tested everything end-to-end.
- Orders are market orders with `time_in_force=DAY` — they won't execute outside market hours.
- Keep your `.env` file out of version control (it's in `.gitignore`).
