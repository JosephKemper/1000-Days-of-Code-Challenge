# 06 Team Activity: Troubleshooting Functions
"""
Problem Statement
The Rosenberg self-esteem scale is a self-esteem measure developed by the sociologist Morris Rosenberg in 1965. 
It is still used in social-science research today. 
To complete the measure, a person completes a survey that contains the following ten statements.

I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all.
The person responds to each statement by choosing one of these four options: 
strongly disagree, disagree, agree, or strongly agree. 
The person's response to each statement is worth 0–3 points, 
meaning the highest possible score is 10 * 3 = 30 points. 
If a person scores lower than 15 points, the person may have a problematic low self-esteem.

Notice that five of the statements (numbers 1, 2, 4, 6, 7) are positive and are scored like this:

Choice	Points
Strongly Disagree	0
Disagree	1
Agree	2
Strongly Agree	3
The other five statements (numbers 3, 5, 8, 9, 10) are negative and are scored like this:

Choice	Points
Strongly Disagree	3
Disagree	2
Agree	1
Strongly Agree	0

Core Requirements
Your program prints the introductory text as shown in the Testing Procedure section below.
Your program prints each of the ten statements and gets a response from the user.
Your program computes score for each response and sums all the scores and displays the total score.
"""
def main():
    # TODO: #15 Program prints the introductory text."
    print("""
This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
    """)


# Collect user data and store in separate lists
# TODO: #14 Program prints each of the ten statements and gets a response from user."

q1 = "I feel that I am a person of worth, at least on an equal plane with others."
q2 = "I feel that I have a number of good qualities."
q3 = "All in all, I am inclined to feel that I am a failure."
q4 = "I am able to do things as well as most other people."
q5 = "I feel I do not have much to be proud of."
q6 = "I take a positive attitude toward myself."
q7 = "On the whole, I am satisfied with myself."
q8 = "I wish I could have more respect for myself."
q9 = "I certainly feel useless at times."
q10 = "At times I think I am no good at all."


# TODO: #13 Program computes score for each response and sums scores and displays total. 



if __name__ == "__main__":
    main()