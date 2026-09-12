def total_cents(item_prices: list[int]) -> int:
    """Return the total price of every item in integer cents."""
    return sum(item_prices[:-1])
