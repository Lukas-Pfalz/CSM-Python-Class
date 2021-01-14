# Name: Lukas Pfalz
# Section:  CSC-1110-71762
# Date: 6/28/20
# Description: Name Orders
# Assignment # - 2

##### Template for Assignment X, problems 1-X ######

print ("********** Problem 3 **********")

name_1 = input("Please enter name #1: ")    # Name #1
name_2 = input("Please enter name #2: ")    # Name #2
name_3 = input("Please enter name #3: ")    # Name #3

# Format the screen before displaying each possible order
print("Here are your names in every possible order:")
print("--------------------------------------------\n")

print(name_1 + ", " + name_2 + ", " + name_3 + "\n")    # Single Line Combination #1
print(name_1 + ", " + name_3 + ", " + name_2 + "\n")    # Single Line Combination #2
print(name_3 + ", " + name_1 + ", " + name_2 + "\n")    # Single Line Combination #3

print(name_2 + "\n" + name_3 + "\n" + name_1 + "\n")    # Multi-Line Combination #1
print(name_3 + "\n" + name_2 + "\n" + name_1 + "\n")    # Multi-Line Combination #2
print(name_3 + "\n" + name_1 + "\n" + name_2)           # Multi-Line Combination #3