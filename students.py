import csv

def main ():
    
    student_info = read_dict("students.csv")
    student_number = input("Please enter an I-Number (xxxxxxxxx): ")
    if student_number in student_info:
        student_name = lookup_student(student_info, student_number)
        print(student_name)
    else:
        print("No such student")

    
def lookup_student (student_info,student_number):
    student_name = student_info[student_number]
    return student_name

def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    student_info ={}
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open (filename,"rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        for row_list in reader:

            # If the current row is not blank, add the
            # current row to the dictionary.
            if len (row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[0]
                value = row_list [1]
                # Store the data from the current
                # row into the dictionary.
                student_info[key] = value




    return student_info

if __name__ == "__main__":
    main()