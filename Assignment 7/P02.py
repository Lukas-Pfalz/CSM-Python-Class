# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/9/20
# Description: Numerology
# Assignment # - 7

##### Template for Assignment X, problems 1-X ######
def main():
    # 1. Prompt for user's name
    name = input("Name: ")
    name = name.lower()     # converted to lowercase

    # Convert name to all lowercase before anything else
    cleaned_up_name = "" # initialize 'cleaned up' name
    for character in name:
        # Remove any non-alphanumerics and numbers (leaving letters)
        if character.isalpha():
            # Adds each letter to the 'cleaned up' name
            cleaned_up_name += character
    # Display the 'cleaned up' name
    print("Your 'cleaned up' name is: ", cleaned_up_name)

    # 3. Convert each letter to its own number ("a" = 1, "b" = 2, etc)
    # ord() function converts each char into an ASCII index
    alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    name_num_conversion = {}    # initialize name -> number converted
    for chars in alphabet:
        name_num_conversion[chars] = ord(chars) - ord("a") + 1

    # 4. Add the numbers to a single "numerology number"
    reduction = 0
    for characters in cleaned_up_name:
        reduction += name_num_conversion[characters]

    print("Reduction:\t", reduction, "\n") # display "numerology number"

# Run main program
for num in range(6):
    main()
