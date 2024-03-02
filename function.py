def currency_converter(amount, currency):
    if currency == "GBP to USD":
        rate = 1.27
    elif currency == "USD to GBP":
        rate = 1.27
    elif currency == "GBP to JPY":
        rate = 190
    elif currency == "JPY to GBP":
        rate = 0.0053

    new_amount = amount * rate
    return new_amount

