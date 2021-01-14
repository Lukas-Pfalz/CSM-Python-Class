# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/2/20
# Description: Odds & Evens Lists
# Assignment # - 6

##### Template for Assignment X, problems 1-X ######

def main():
    # lists of numbers
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the list of numbers
    print("Original List:", numbers_list)

    evens_list = [] # initialize "odds" number list
    odds_list = []  # initialize "evens" number list

    # Split the list into two "odd" and "even" lists
    # Loop through the number list to read each element
    for num in numbers_list:
        if num % 2 == 0:            # if the element was even
            evens_list.append(num)  # add element to evens list
        else:                       # otherwise,
            odds_list.append(num)   # add element to odds list
    # Display the evens and odds lists
    print("\nEvens list:", evens_list)
    print("Odds list:", odds_list)

# Run main program
main()
