# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/2/20
# Description: Management System
# Assignment # - 6

##### Template for Assignment X, problems 1-X ######

def main():
    valid = False
    while not valid:
        valid = True
        username = str(input("Please enter a username: "))

        upper, lower, nums = count_upper_lower_num(username)
        # check if first number is numeric
        if len(username) < 8 or len(username) > 15:
            print("Username must be between 8 and 15 characters.")
            valid = False

        elif not username.isalnum() and valid: # Check for Special Characters
            print("Username must contain only alphanumeric characters.")
            valid = False

        elif username[0].isnumeric() and valid:
            print("The first character in your username cannot be a digit")
            valid = False

        elif lower == 0 and valid:
            print("Your username must contain at least one lowercase character")
            valid = False

        elif nums == 0 and valid:
            print("Your username must contain at least one digit")
            valid = False

        elif upper == 0 and valid:
            print("Your username must contain at least one uppercase character")
            valid = False

        else:
            print("Your username is valid")

def count_upper_lower_num (string):
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

# Run main program
main()
