
def main ():
# Open the provinces.txt file for reading.
    provinces_list = open_file("provinces.txt")
    
# Print the entire list.
    print(provinces_list)

    remove_first_item(provinces_list)

    remove_last_item(provinces_list)

    replace_AB(provinces_list)

    alberta_count = count_Alberta(provinces_list)
    print(f"Alberta occurs {alberta_count} times in the modified list.")

def open_file (file_name):
    provinces_list = []
    with open (file_name) as text_file:

# Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
        for line in text_file:
            clean_line = line.strip()
            provinces_list.append(clean_line)
    return provinces_list

# Remove the first element from the list.
def remove_first_item (provinces_list):
    provinces_list.pop(0)

# Remove the last element from the list.
def remove_last_item (provinces_list):
    provinces_list.pop()

# Replace all occurrences of "AB" in the list with "Alberta".
def replace_AB (provinces_list):
    for i in range(len(provinces_list)):
        if provinces_list [i] == "AB":
            provinces_list [i] = "Alberta"
            

# Count the number of elements that are "Alberta" and print that number.
def count_Alberta (provinces_list):
    alberta_count = 0
    for province in provinces_list:
        if province == "Alberta":
            alberta_count += 1
    return alberta_count

if __name__ == "__main__":
    main()