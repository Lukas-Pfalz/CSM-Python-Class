# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/2/20
# Description: Management System
# Assignment # - 6

##### Template for Assignment X, problems 1-X ######

def count_upper_lower_num(string):
    upper = 0  # counter for uppercase character
    lower = 0  # counter for lowercase character
    num = 0  # counter fo numeric
    for character in string:
        if character.isupper():
            upper = upper + 1  # counts how many uppercase
        elif character.islower():
            lower = lower + 1  # counts how many lowercase
        elif character.isnumeric():
            num = num + 1  # counts how many numbers
    arr = [upper, lower, num]
    return arr

name = "PlasmaReactor1"
upper, lower, num = count_upper_lower_num (name)
print("upper: ", upper, "\nlower: ", lower, "\nnum: ", num)
