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

    q1 = input("1. I feel that I am a person of worth, at least on an equal plane with others. "+
    "Enter D, d, a, or A: ")
    q2 = input("2. I feel that I have a number of good qualities. "+
    "Enter D, d, a, or A: ")
    q3 = input("3. All in all, I am inclined to feel that I am a failure. "+
    "Enter D, d, a, or A: ")
    q4 = input("4. I am able to do things as well as most other people. "+
    "Enter D, d, a, or A: ")
    q5 = input("5. I feel I do not have much to be proud of. "+
    "Enter D, d, a, or A: ")
    q6 = input("6. I take a positive attitude toward myself. "+
    "Enter D, d, a, or A: ")
    q7 = input("7. On the whole, I am satisfied with myself. "+
    "Enter D, d, a, or A: ")
    q8 = input("8. I wish I could have more respect for myself. "+
    "Enter D, d, a, or A: ")
    q9 = input("9. I certainly feel useless at times. "+
    "Enter D, d, a, or A: ")
    q10 = input("10. At times I think I am no good at all. "+
    "Enter D, d, a, or A: ")

    print()

    positive_score = positive_grading(q1, q2, q4, q6, q7)
    negative_score = negative_grading(q3, q5, q8, q9, q10)
    score = positive_score + negative_score
# Display results
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")
    
def positive_grading (q1, q2, q4, q6, q7) -> int:
    positive_answers = [q1, q2, q4, q6, q7]
    score = 0

    for q in positive_answers:
        if q == "A":
            score += 3
        elif q == "a":
            score += 2
        elif q == "d":
            score += 1
        elif q == "D":
            score += 0
    return score


def negative_grading(q3, q5, q8, q9, q10) -> int:
    negative_answers = [q3, q5, q8, q9, q10]
    score = 0

    for q in negative_answers:
        if q == "D":
            score += 3
        elif q == "d":
            score += 2
        elif q == "a":
            score += 1
        elif q == "A":
            score += 0
    return score



if __name__ == "__main__":
    main()