import re

def validate_sku(sku):
    """Validate SKU format (e.g., SKU-12345)."""
    pattern = r"^SKU-\d{5}$"
    return bool(re.match(pattern, sku))

def calculate_tax(price, tax_rate):
    """Calculate tax amount based on price and tax rate."""
    return round(price * (tax_rate / 100), 2)

def calculate_profit(buy_price, sell_price, quantity):
    """Calculate profit based on buy and sell prices."""
    profit = (sell_price - buy_price) * quantity
    return profit

def is_high_margin_trade(profit, buy_price, quantity):
    """Generator function to yield trades with profit margins > 20%."""
    margin = (profit / (buy_price * quantity)) * 100
    if margin > 20:
        yield profit, margin
