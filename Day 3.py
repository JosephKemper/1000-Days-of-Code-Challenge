# File for work performed during day 3 of my 100 days of coding challege. 
# Completed Nested Lists Challenge found at the following link
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# Lists for storing user data
names = []
scores = []

# Loop to collect user data and place it in a list. 
for _ in range(int(input())):
    name = input()
    names.append(name)
    score = float(input())
    scores.append(score)

# List to collect unique user scores. 
unique_scores = []

# List to find the unique values among user scores. 
for i in scores:
    if i not in unique_scores:
        unique_scores.append(i)

# Sorting unique scores into order within list. 
unique_scores.sort()

# Pulling the second highest value of the list of user scores. 
value_of_second_highest = unique_scores[1]

second_lowest_names = []

# Sort through scores list to pull out the indexes of any score that equals the second place score and print it out. 
for index, val in enumerate(scores):
    if val == value_of_second_highest:
        second_lowest_names.append(names[index])

# Sort List of names to alphabetical order
second_lowest_names.sort()

# Print list of names. 
for name in second_lowest_names:
    print(name)
