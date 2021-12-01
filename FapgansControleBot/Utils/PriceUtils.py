def price_formatter(price: str) -> int:
    return int(str.upper(price).replace('K', "000"))
