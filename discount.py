# Problem Statement
"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store's slowest sales days. 
On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, 
the store will discount the customer's subtotal by 10%.
"""
from datetime import datetime

def tax_amount(cost):
    total_taxes = cost * 0.06
    return total_taxes

def discount_amount (cost):
    total_discount = cost * 0.1
    return total_discount

def total_with_discount (cost):
    total =cost - discount_amount(cost) + tax_amount(cost)
    return total

def normal_total (cost):
    total = cost + tax_amount(cost)
    return total

def needed_for_discount (cost):
    if cost < 50:
        needed = 50 - cost
        print(f"If you purchase ${needed} you could qualify for a 10% discount on your purchase today.")
    


# Stretch Challenge #2
# Replace request for subtotal with loop that asks for price and quantity
# that then calculates the subtotal. 
# Loop is broken when they type 0. 
# Ask user for subtotal

item_cost = None
item_quantity = None
subtotal = 0.00
while item_cost != 0:
    item_cost = float(input('Enter cost of item [Enter "0" to end]: '))
    if item_cost == 0:
        break
    item_quantity = float(input("Enter the quantity being purchased: "))
    total_item_cost = item_cost * item_quantity
    print(f"{item_quantity} times ${item_cost} is a total of {total_item_cost}")
    subtotal += total_item_cost
    print(f"Current Subtotal is ${subtotal:.2f}")
    print()



# Pull date from computer
# Do not ask it from user
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 1

# Stretch Challenge #1
# Calculate and display the extra they would need to purchase to get discount

# Print Total and discount (if appropriate) to user
if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    print (f"Discount amount: {discount_amount(subtotal):.2f}")
    print (f"Sales tax amount: {tax_amount(subtotal):.2f}")
    print (f"Total: {total_with_discount(subtotal):.2f}")

elif  (day_of_week == 1 or day_of_week == 2) and subtotal <= 50:
    needed_for_discount(subtotal)
    print (f"Sales tax amount: {tax_amount(subtotal):.2f}")
    print (f"Total: {total_with_discount(subtotal):.2f}")

else:
    print (f"Sales tax amount: {tax_amount(subtotal):.2f}")
    print (f"Total: {normal_total(subtotal):.2f}")