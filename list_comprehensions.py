# Project pulled from Hacker Rank List Comprehensions challange. 
# URL https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

# Challenge create a list of coordinates for a cuboid from the user.
# Use those ranges to generate a list of coordinates.
# Ignore any combination of coordinates whose sum equals the limiting number.

# Get Coordinate ranges from user
x = int(input())
y = int(input())
z = int(input())

# Get the limiting number from the user
# This is the number which the sum of the coordinates cannot be equal to
n = int(input())

print ([[i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if sum([i,j,k]) != n])





