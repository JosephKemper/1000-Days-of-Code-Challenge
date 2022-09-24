# 07 Team Activity: Lists
import random
# TODO: #25 Write the main function for 07 Team
def main():
    # default number list
    numbers = [16.2, 75.1, 52.3]

    #display number list before processing it in function
    print (f"numbers {numbers}")

    # Calls the append_random_numbers function with only one argument to add one number to numbers
    append_random_numbers(numbers)
    
    # Prints the numbers list
    print (f"numbers {numbers}")

    # Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    append_random_numbers(numbers,quantity=3)
    # Prints the numbers list
    print (f"numbers {numbers}")

# TODO: #24 Write the append_random_numbers function for 07 team
def append_random_numbers(numbers_list, quantity=1):
    
    # Use the paramater quantity to determine how many numbers to generate inside of a loop. 
    # Append each number to the numbers list
    count = 0
    while count < quantity:
        random_float = random.uniform(0,100)
        rounded_float = round(random_float,1)
        numbers_list.append(rounded_float)
        count += 1



if __name__ == "__main__":
    main()