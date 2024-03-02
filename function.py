def currency_converter(amount, currency):
    if currency == "GBP to USD":
        rate = 1.27
    elif currency == "USD to GBP":
        rate = 0.79
    elif currency == "GBP to JPY":
        rate = 190
    elif currency == "JPY to GBP":
        rate = 0.0053

    new_amount = round(amount * rate, 2)
    return new_amount

