import math

# Prompt user for number of items
items = int(input("Enter the number of items: "))

# Prompt user for number of items per box
items_per_box = int(input("Enter the number of items per box: "))
# Calculate items per box using whole numbers
boxes_needed = math.ceil(items/items_per_box)

# Blank line for aesthetic purposes
print()

# Return quantity of items per box to user
print(f"For {items} items, packing {items_per_box} items in each box, you will need {boxes_needed} boxes.")