# Problem Statement
"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store's slowest sales days. 
On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, 
the store will discount the customer's subtotal by 10%.
"""
# Import DateTime Module to allow for automatic calculation of which day of the week it is for discount purposes
from datetime import datetime

# Calculate total taxes on purchase. 
def tax_amount(cost)->float:
    return round(cost * 0.06,2)
     

# Calculate total discount on purchase
def discount_amount (cost)->float:
    return round(cost * 0.1,2)
    
    

# Calculate total cost including taxes and discount
def total_with_discount (cost)->float:
    return cost - discount_amount(cost) + tax_amount(cost)
    

# Calculate the total without discount
def normal_total (cost)->float:
    return cost + tax_amount(cost)
    
# Calculate the amount extra amount needed to get the discount
def needed_for_discount (cost)->float:
    return 50 - cost
    
    


# Stretch Challenge #2
# Replace request for subtotal with loop that asks for price and quantity
# that then calculates the subtotal. 
# Loop is broken when they type 0. 
# Ask user for subtotal

# Initialize cost variables
# Set Item Cost and item quantity to none to not effect the loop
item_cost = None
item_quantity = None
subtotal = 0.00

# Loop for entering items being purchased
while item_cost != 0:
    item_cost = float(input('Enter cost of item [Enter "0" to end]: '))
    if item_cost == 0:
        break
    item_quantity = float(input("Enter the quantity being purchased: "))
    total_item_cost = item_cost * item_quantity
    
    # Ongoing display of how much they are purchasing
    # Formatted to display proper decimals.
    print(f"{item_quantity} times ${item_cost:.2f} is a total of {total_item_cost:.2f}")
    subtotal += total_item_cost
    print(f"Current Subtotal is ${subtotal:.2f}")
    print()



# Pull date from computer
# Do not ask it from user
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 1

# Stretch Challenge #1


# Print Total and discount (if appropriate) to user
if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    print (f"Discount amount: {discount_amount(subtotal):.2f}")
    print (f"Sales tax amount: {tax_amount(subtotal):.2f}")
    print (f"Total: {total_with_discount(subtotal):.2f}")

# Calculate and display the extra they would need to purchase to get discount
elif  (day_of_week == 1 or day_of_week == 2) and subtotal <= 50:
    print(f"If you purchase ${needed_for_discount(subtotal)} more" +
    "you could qualify for a 10% discount today.")
    
    print (f"Sales tax amount: {tax_amount(subtotal):.2f}")
    print (f"Total: {normal_total(subtotal):.2f}")

# Display total without discount if no discount is being offered. 
else:
    print (f"Sales tax amount: {tax_amount(subtotal):.2f}")
    print (f"Total: {normal_total(subtotal):.2f}")