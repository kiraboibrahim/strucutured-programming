"""
Create a function that takes two inputs, price and quantity and then outputs the computed amount
"""

def get_amount(price,quantity):
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")
    amount=(price*quantity)
    print(amount)
get_amount(10000000, 2)    


def get_discount(amount):
    if amount >1000000:
        discount=(20/100)*amount
    elif amount>500000<1000000:
        discount =(10/100)*amount
    else:
        print(amount)       

