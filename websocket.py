WebSocket code

from binance import ThreadedWebsocketManager
from logger import logger

def start_price_stream(symbol="btcusdt"):
    twm = ThreadedWebsocketManager()
    twm.start()

    def handle(msg):
        price = msg.get("c")
        logger.info(f"Live price {symbol}: {price}")
        print(f"Live price {symbol}: {price}")

    twm.start_symbol_ticker_socket(symbol=symbol, callback=handle)
