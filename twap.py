TWAP stratergy

from logger import logger

def grid_trading(bot, symbol, side, start_price, grid_size, levels, quantity):
    logger.info("Starting Grid Trading Strategy")

    for i in range(levels):
        price = start_price + (i * grid_size)
        bot.place_limit_order(symbol, side, quantity, round(price, 2))
        logger.info(f"Grid order placed at {price}")
