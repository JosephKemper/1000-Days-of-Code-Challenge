"""
Completed Hacker Rank Lists challenge. 
https://www.hackerrank.com/challenges/python-lists/problem
Thank you to https://www.codingbroz.com/lists-in-python-solution/ 
for helping me figure out what the question was even asking. 
While I did use their wonderfully built solution as a template for my own solution
I did try to make it my own. 
For example, I wanted to allow the commands to be entered in case insensitvely. 
I also wanted to get more practice with functions. 
"""
def main ():
    number = int(input())
    dynamic_list(number)

    

def dynamic_list (number):
    user_list = []
    for i in range (0,number):
        command = input().split()
        if command [0].lower() == "insert":
            user_list.insert(int(command[1]),int(command[2]))
        elif command [0].lower() == "print":
            print(user_list)
        elif command [0].lower() == "remove":
            user_list.remove(int(command[1]))
        elif command [0].lower() == "append":
            user_list.append(int(command[1]))
        elif command [0].lower() == "sort":
            user_list.sort()
        elif command [0].lower() == "pop":
            user_list.pop()
        elif command [0].lower() == "reverse":
            user_list.reverse()
        else:
            pass
    return user_list


if __name__ == '__main__':
    main()