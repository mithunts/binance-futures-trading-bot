CLI input logic

from bot import BasicBot
from config import DEFAULT_SYMBOL

def main():
    api_key = input("Enter API Key: ").strip()
    api_secret = input("Enter API Secret: ").strip()

    bot = BasicBot(api_key, api_secret)

    print("\nOrder Types:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order")

    choice = input("Choose order type (1/2/3): ").strip()
    side = input("Side (BUY/SELL): ").upper()
    quantity = float(input("Quantity: "))

    if choice == "1":
        result = bot.place_market_order(DEFAULT_SYMBOL, side, quantity)

    elif choice == "2":
        price = float(input("Limit Price: "))
        result = bot.place_limit_order(DEFAULT_SYMBOL, side, quantity, price)

    elif choice == "3":
        stop_price = float(input("Stop Price: "))
        limit_price = float(input("Limit Price: "))
        result = bot.place_stop_limit_order(
            DEFAULT_SYMBOL, side, quantity, stop_price, limit_price
        )

    else:
        print("Invalid choice")
        return

    if result:
        print("\nOrder Successful!")
        print("Order ID:", result.get("orderId"))
        print("Status:", result.get("status"))
    else:
        print("\nOrder Failed. Check logs.")

if __name__ == "__main__":
    main()
