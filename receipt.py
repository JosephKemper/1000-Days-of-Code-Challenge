import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

def main ():
    product_code_index = 0

    # Product Code 0
    # Product Name 1
    # Product Price 2
    products_dict = read_dict("products.csv", product_code_index)
    count = count_items ("request.csv")
    subtotal = calculate_subtotal (products_dict,"request.csv")
    sales_tax = calculate_tax (subtotal)
    order_total = calculate_total (subtotal,sales_tax)

# TODO: 10 Prove Assignment Write Code to handle errors

# Print the store name at the top of the receipt.
    print ("Inkom Emporium")
    print_items (products_dict, "request.csv")

    # Print number of items being purchased to receipt
    print(f"Number of Items: {count}")


# Print Order Subtotal
    print (f"Subtotal: {subtotal:.2f}")

# Print Sales Tax
    print(f"Sales Tax: {sales_tax:.2f}")

# Print Order Total
    print(f"Total: {order_total:.2f}")

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")

def calculate_total (subtotal,taxes):
    """
    Calculate and return the total for the order
    """
    return subtotal + taxes

def calculate_tax (subtotal):
    """
    Calculate and return a 6% sales tax.
    """
    return subtotal * 0.06

def calculate_subtotal (products_dict,filename):
    """
    Calculate and return the subtotal for the order in question. 
    """
    subtotal = 0
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # Pull out Product info from request.csv
                # Assign both quantity and product code to variables
                product_code = row_list [0]
                product_quantity =int(row_list [1])

                # Look up product code in products_dict
                product_info = products_dict [product_code]

                # Assign product name and price to variables
                product_price = float(product_info [2])
                
                subtotal_product = product_quantity * product_price

                subtotal += subtotal_product
    return subtotal

def count_items (filename):
    """
    Count and return the total number of items in the order
    """
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        count = 0
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # Pull out Product info from request.csv
                # Assign both quantity and product code to variables
                quantity = int(row_list[1])
                count +=quantity
        return count

def print_items (products_dict, filename):
    """
    Print the list of items purchased to the terminal
    """
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # Pull out Product info from request.csv
                # Assign both quantity and product code to variables
                product_code = row_list [0]
                product_quantity =row_list [1]

                # Look up product code in products_dict
                product_info = products_dict [product_code]

                # Assign product name and price to variables
                product_name = product_info [1]
                product_price = product_info [2]

                # Print product name and price
                print(f"{product_name}: {product_quantity} @ {product_price}")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    products_dict = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                products_dict [key] = row_list

    # Return dictionary
    return products_dict

# Call Main function to start
if __name__ == "__main__":
    main()