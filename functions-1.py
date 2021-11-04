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

def total(moneyF, priceF):
    apple_quant = int(moneyF/priceF)
    _result2 = apple_quant * priceF
    change = moneyF - _result2
    return change

def display(result,change):
    print (f"you can buy {result}apples, and your change is {change}") 
    
money = get_money()
price = get_price()
result = math.floor(divide(money,price))
result2 = float(total(money,price))
print(f"You can buy {result} and your change is PHP {result2}. ") 

