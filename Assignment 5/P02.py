# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/26/20
# Description: Check Answer
# Assignment # - 5

##### Template for Assignment X, problems 1-X ######

# initialize "main" program (Test Program)
def main():
    answer1 = check_answer(1, 2, 3, "+")
    print(answer1)
    answer2 = check_answer(1, 2, -1, "-")
    print(answer2)
    answer3 = check_answer(9, 5, 3, "+")
    print(answer3)
    answer4 = check_answer(8, 2, 4, "-")
    print(answer4)

# This function takes two numbers (two integers), an operator (addition "+" OR subtraction "-"),
# and the "correct" answer (an integer), checking to see if the supplied "expression":
# "first number" (+ OR -) "second number" equals the "correct" answer
def check_answer(num1, num2, answer, operator):
    expression = 0                      # "expression" is initialized

    # Determines the "entered_answer" based on what operator was used
    if operator == "+":                 # if addition (+) is used,
        expression = num1 + num2        # the first and second number is summed
    else:                               # if subtraction (-) is used,
        expression = num1 - num2        # the difference of the first and second numbers
                                        # is determined

    # Returns whether or not the entered_answer equals the "correct" answer
    if expression == answer:            # If the expression equals the "correct" answer
        return True                     # return that the expression was correct
    else:                               # Otherwise, the expression
        return False                    # does not equal the "correct" answer

# "main" program is called, running the program
main()
