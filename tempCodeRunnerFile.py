# Project pulled from Hacker Rank List Comprehensions challange. 
# URL https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true



x, y, z, n = (int(input()) for _ in range(4))
# print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])
