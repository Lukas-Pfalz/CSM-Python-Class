# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/7/20
# Description: Sentinel Value
# Assignment # - 4

##### Template for Assignment X, problems 1-X ######

print("********** Problem 3 **********")

# the "counter" and "num" is initialized
counter = 0
num = 0

# while "num" doesn't equal a 'sentinel_value', the loop continues
while num != 21 and num != -147 and num != 77 and num != 81 and num != 1002 and num != -23 and num != -999:
    counter += num                          # "num" value is added to the "counter"
    num = int(input("Enter a number: "))    # User enters "num" value

# Print out the final value for "counter"
print("\nThe sum is ", counter)
