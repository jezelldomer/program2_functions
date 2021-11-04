import math

def get_name():
    _name = input("Enter your name: ")
    return _name

def get_age():
    _age = input("Enter your age: ")
    return _age

def get_address():
    _address = input("Enter your address: ")
    return _address

def display(nameF, ageF, addF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addF}. ")

name = get_name()
age = get_age()
address = get_address()
display(name, age, address)