# Problem Statement
"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store's slowest sales days. 
On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, 
the store will discount the customer's subtotal by 10%.
"""


# Your program asks the user for the subtotal 
# but does not ask the user for the day of the week. 
# Your program gets the day of the week from your computer's operating system.
from datetime import datetime

# load the system date
current_day = datetime.now()

# convert to week order day
week_day = current_day.weekday()
week_day = 2
subtotal = float(input("Enter the Subtotal: "))
taxes = subtotal *0.06

discount = 0
# detect Tuesday:1 or Wednesday:2
if (week_day == 1 or week_day == 2) and subtotal >= 50:
    print('you win a 10 percent discount')
    discount = subtotal * 0.1
    subtotal = subtotal * 0.9
    print(f"Your discount today was ${discount:.2f}.")
else:
    print('Thanks for your shop')

taxes = subtotal * 0.06
total = taxes + subtotal


print(f"The taxes today came to ${taxes:.2f}")

print(f"Your total today was ${total:.2f}")




# Your program correctly computes and prints the discount amount if applicable.

# Your program correctly computes and prints the sales tax amount and the total amount due.
