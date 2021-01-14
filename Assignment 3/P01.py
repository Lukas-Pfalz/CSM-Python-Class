# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/4/20
# Description: Exam Scores
# Assignment # - 3

##### Template for Assignment X, problems 1-X ######

# Problem #1
print ("********** Problem 1 **********")

# Initialized Prompt
print("Three Exam Score Grade Calculator\n")

# User inputs scores for Exams 1-3
exam_1_score = int(input("Enter exam 1 score: "))
exam_2_score = int(input("Enter exam 2 score: "))
exam_3_score = int(input("Enter exam 3 score: "))

# Calculates average exam score
average_exam_score = (exam_1_score + exam_2_score + exam_3_score) / 3.0

# Formats "Average Exam Score" to Two Decimal places
avg_scores = str(format(average_exam_score, '.2f'))

# Displays Average Exam score / Converts "Average Score" to a String to be printable
print("\nResults:\nAverage of the 3 scores: ", avg_scores)

average_exam_score = int(average_exam_score)
print(average_exam_score)
# Displays Letter Grade (from 'F' to 'A') for Average Exams
if average_exam_score < 60:                                 # If grade is under 60
    print("Letter grade: F")                                # final grade is a "F"

elif 60 <= average_exam_score < 70:    # If grade is between 60-69
    print("Letter grade: D")                                # final grade is a "D"

elif 70 <= average_exam_score < 80:    # If grade is between 70-79
    print("Letter grade: C")                                # final grade is a "C"

elif 80 <= average_exam_score < 90:    # If grade is between 80-89
    print("Letter grade: B")                                # final grade is a "B"

else:                                                       # If grade is above 90
    print("Letter grade: A")                                # final grade is an "A"
