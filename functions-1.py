import math

def get_money():
    _money = float(input("Enter the amount of money you have: "))
    return _money

def get_price():
    _price = float(input("Enter the price of an apple: "))
    return _price

def divide(moneyF, priceF):
    _result = moneyF/priceF   
    return _result



money = get_money()
price = get_price()
result = math.floor(divide(money,price))
