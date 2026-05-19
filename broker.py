import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


def _client() -> TradingClient:
    return TradingClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_SECRET_KEY"],
        paper=os.environ.get("ALPACA_LIVE", "false").lower() != "true",
    )


def place_order(symbol: str, side: str, quantity: float) -> dict:
    order_side = OrderSide.BUY if side.lower() == "buy" else OrderSide.SELL
    req = MarketOrderRequest(
        symbol=symbol.upper(),
        qty=quantity,
        side=order_side,
        time_in_force=TimeInForce.DAY,
    )
    order = _client().submit_order(req)
    return {
        "id": str(order.id),
        "symbol": order.symbol,
        "side": order.side.value,
        "qty": str(order.qty),
        "status": order.status.value,
    }


def get_account() -> dict:
    acct = _client().get_account()
    return {
        "buying_power": str(acct.buying_power),
        "portfolio_value": str(acct.portfolio_value),
        "status": acct.status.value,
    }
