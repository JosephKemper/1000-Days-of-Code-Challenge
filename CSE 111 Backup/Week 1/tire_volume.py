# 02 Prove: Calling Functions
# Problem Statement
"""
Many companies wish to understand the needs and wants of their customers more deeply 
so the company can create products that fill those needs and wants. 
One way to understand customers more deeply is to record the values entered by customers 
while they are using a program and then to analyze those values. 
One common way to record values is for a program to store them in a file.


# 01 Prove Milestone: Review Python

The size of a car tire in the United States 
is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with these variables:

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

import math
from datetime import date
current_date = date.today()


# Collect User Input
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate tire pressure
#Compute top half of formula
top_formula = math.pi * (w**2) * a *(w * a +2540 *d)
# Finish Formula computation
v = round(top_formula/10000000000,2)

print()

# Display results to user.
print(f"""You entered a tire with the following dimensions:
Width: {w}
Aspect Ratio: {a}
Diameter {d}
A tire of that size will have an approximate volume of {v:.2f} liters""")


# Check if tire size matches sample tires
tire_price = None

if w == 265 and a == 40 and d == 21:
    tire_price = 247.64
elif  w == 265 and a == 70 and d == 16:
    tire_price = 159
elif  w == 245 and a == 50 and d == 20:
    tire_price = 152
elif  w == 215 and a == 55 and d == 17:
    tire_price = 78.93
elif  w == 215 and a == 45 and d == 17:
    tire_price = 73.63
elif  w == 235 and a == 50 and d == 18:
    tire_price = 95.67
elif  w == 225 and a == 65 and d == 17:
    tire_price = 112


# Determine which path would be proper to use for user. 
# Record tire size check
if tire_price == None:
    with open ("volumes.txt", "at") as v_record:
        print (f"{current_date}, {w}, {a}, {d}, {v}", file=v_record)

# Offer sale of tires that are on sale
else:
    print(f"We have a tire that will fit your car on sale for ${tire_price:.2f}.")
    user_choice = input("Would you be interested in purchasing a set? ")

# Collect contact info if yes
    if user_choice.lower() == "yes" or user_choice.lower() == "y":
        phone_number = input("Please enter your phone number: ")
        # Added name at the last minute because it felt too impersonal without the name.
        customer_name = input("And who should we ask for when we call? ")
        print("Wonderful! We'll be in touch soon to arrange for delivery and installation.")
        with open ("volumes.txt", "at") as v_record:
            print (f"{current_date}, {w}, {a}, {d}, {v}, {phone_number}, {customer_name}", file=v_record)

# Record tire size if customer declines
    else:
        with open ("volumes.txt", "at") as v_record:
            print (f"{current_date}, {w}, {a}, {d}, {v}", file=v_record)