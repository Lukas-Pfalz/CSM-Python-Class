# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/4/20
# Description: Lowest Number
# Assignment # - 3

##### Template for Assignment X, problems 1-X ######

# Problem #2
print("********** Problem 2 **********")

# Initial prompt for when the program begins
print("Display the smallest of three integers")

# Have the user enter the values of 'x', 'y', and 'z'
x = input("The value of x is: ")
y = input("The value of y is: ")
z = input("The value of z is: ")

# Each variable is compared to determine which value is the smallest
if x < y and x < z:                      # If x is less than y and z
    print("\nThe smallest value is ", x)  # x is the lowest
elif y < x and y < z:                    # If y is less than x and z
    print("\nThe smallest value is ", y)  # y is the lowest
else:                                   # If neither x nor y are smallest
    print("\nThe smallest value is ", z)  # z must be the lowest
