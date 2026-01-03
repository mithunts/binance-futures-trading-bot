PnL logic

def calculate_pnl(entry_price, exit_price, quantity, side):
    if side == "BUY":
        return round((exit_price - entry_price) * quantity, 2)
    else:
        return round((entry_price - exit_price) * quantity, 2)
