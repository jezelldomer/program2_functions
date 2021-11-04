import math

def input_apple():
    apple_buy = int(input("Enter how many apples you want to buy: "))
    return apple_buy

def input_orange(): 
    orange_buy = int(input("Enter how many oranges you want to buy: "))
    return orange_buy

def total_1(appleF, orangeF):
    _result = appleF*orange_price
    _result2 = orangeF*orange_price
    sum = _result + _result2
    return sum

def display(total):
    print(f"The total amount is {total}. ")

apple_price = 20
orange_price = 25

apple = input_apple() 
orange = input_orange()
total = total_1(apple, orange)

print(f"Hi, the total amount is {total}. Thank you. ")
