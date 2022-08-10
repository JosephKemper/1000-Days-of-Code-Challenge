# Day 2 of 100 days of Coding 
# Completed Find the Runner-Up Score challenge from HackerRank
# Link found here
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Goal is to get an array of numbers from the user and find the second largest number from that array

# The first two lines were partially provided by the challenge
# It errored out as given, I found that it worked better if you added a strip function
# The strategy I went with was to build a unique list and then sort the list 
# Then return the second largest via using the index of the second item from the end of the list

n = int(input())
arr = map(int, input().strip().split())

# List for unique values of list
unique_list = []

# Loop to separate out the unique values in the original array. 
for i in arr:
    if i not in unique_list:
        unique_list.append(i)
    
# Function to sort the filtered list. 
unique_list.sort()

# Variable to first find the length of the list and then by subtracting 2 from it, 
# you get the position of the number in the second place. 

index_of_second = len(unique_list)-2

# Display's output to user. 
print(unique_list[index_of_second])


