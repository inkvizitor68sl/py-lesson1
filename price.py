#!/usr/bin/python3.6

def format_price(price):
    int_price = int(price)
    return ("Цена: " + str(int_price) + " руб.")

display_price = format_price(56.24)
print(display_price)
    