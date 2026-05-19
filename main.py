import os
import logging
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, field_validator

import broker
import notifier

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "")


@asynccontextmanager
async def lifespan(app: FastAPI):
    acct = broker.get_account()
    mode = "LIVE" if os.environ.get("ALPACA_LIVE", "false").lower() == "true" else "PAPER"
    log.info("Alpaca connected (%s) — portfolio: $%s", mode, acct["portfolio_value"])
    yield


app = FastAPI(title="StockSkil Webhook", lifespan=lifespan)


class AlertPayload(BaseModel):
    """
    TradingView alert message body (JSON).

    Example TradingView message template:
    {
      "secret": "your_secret_here",
      "symbol": "{{ticker}}",
      "action": "buy",
      "quantity": 1
    }
    """

    secret: str = ""
    symbol: str
    action: str  # "buy" or "sell"
    quantity: float = 1

    @field_validator("action")
    @classmethod
    def validate_action(cls, v: str) -> str:
        if v.lower() not in ("buy", "sell"):
            raise ValueError("action must be 'buy' or 'sell'")
        return v.lower()

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("quantity must be positive")
        return v


@app.post("/webhook")
async def receive_alert(payload: AlertPayload, request: Request):
    if WEBHOOK_SECRET and payload.secret != WEBHOOK_SECRET:
        log.warning("Rejected webhook — bad secret from %s", request.client.host)
        raise HTTPException(status_code=401, detail="Invalid secret")

    log.info("Alert received: %s %s x%s", payload.action.upper(), payload.symbol, payload.quantity)

    sms_text = f"[StockSkil] {payload.action.upper()} signal: {payload.symbol} x{payload.quantity}"

    order_result = None
    try:
        order_result = broker.place_order(payload.symbol, payload.action, payload.quantity)
        sms_text += f"\nOrder placed — ID: {order_result['id']} status: {order_result['status']}"
        log.info("Order placed: %s", order_result)
    except Exception as exc:
        sms_text += f"\nOrder FAILED: {exc}"
        log.error("Order failed: %s", exc)

    try:
        sid = notifier.send_sms(sms_text)
        log.info("SMS sent: %s", sid)
    except Exception as exc:
        log.error("SMS failed: %s", exc)

    return {"received": True, "order": order_result}


@app.get("/health")
async def health():
    return {"status": "ok"}
