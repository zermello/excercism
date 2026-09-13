def exchange_money(budget, exchange_rate):
    exchanged_currency = budget / exchange_rate
    return exchanged_currency

def get_change(budget, exchanging_value):
    amount_of_money_left = budget - exchanging_value
    return amount_of_money_left


def get_value_of_bills(denomination, number_of_bills):
    value_of_bills = denomination * number_of_bills
    return value_of_bills

def get_number_of_bills(amount, denomination):
    number_of_bills = amount // denomination
    return number_of_bills

def get_leftover_of_bills(amount, denomination):
    leftover_of_bills = amount % denomination
    return leftover_of_bills


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread = spread / 100
    spread_amount = exchange_rate * spread
    actual_rate = exchange_rate + spread_amount
    exchanged_money = int(budget / actual_rate)
    return (exchanged_money // denomination) * denomination