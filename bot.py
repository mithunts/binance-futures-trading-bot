BasicBot class

from binance import Client
from binance.exceptions import BinanceAPIException
from logger import logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"Market Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Market Order Error: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"Limit Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Limit Order Error: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )
            logger.info(f"Stop-Limit Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Stop-Limit Order Error: {e}")
            return None
