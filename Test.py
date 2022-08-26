import math
number_quantity = int(input("Enter the quanity of numbers you would like to average: "))
list_to_average = []

for i in range(number_quantity):
    number_input = float(input("Enter a number: "))
    list_to_average.append(number_input)
print(sum(list_to_average)/number_quantity)
