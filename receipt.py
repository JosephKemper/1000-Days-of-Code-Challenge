import csv

def main ():
    product_code_index = 0

    products_dict = read_dict("products.csv", product_code_index)
    print(products_dict)

    print ("Requested Items")
    process_request(products_dict, "request.csv")


def process_request (products_dict, filename):

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