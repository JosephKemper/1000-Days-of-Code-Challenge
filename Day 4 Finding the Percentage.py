# Work for 100 days of Code Day 4 Finding the Percentage
# This Coding Challenge was taken from HackerRank Found at the following URL
# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

# Challenge principles

# Get user to enter student name and scores
# Map that data to a dictionary
# Get name from user
# Return average of scores for student printed in float with 2 Decimals
# First line should allow user to enter the number of students
# Second line should allow user to enter the name of the student followed by their scores. 

# Get Quantity of Students from user
n = int(input())

# Get student and scores separated by spaces from user
# Split input and map it to dictionary
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))

    student_marks[name] = scores

# Get student for averaging scores from user
query_name = input()

# Calculate and print average score
average_score = (student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2])/3
print (f"{average_score:.2f}")