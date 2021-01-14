# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/26/20
# Description: Print Lines
# Assignment # - 5

##### Template for Assignment X, problems 1-X ######

# initialize "main" program (Test Program)
def main():
    print("Horizontal line, width = 5:")
    horizontal_line(5)
    print()
    print("Horizontal line, width = 10:")
    horizontal_line(10)
    print()
    print("Horizontal line, width = 15:")
    horizontal_line(15)
    print()
    print("Vertical Line, shift=0; height=3:")
    vertical_line(0, 3)
    print()
    print("Vertical Line, shift=3; height=3:")
    vertical_line(3, 3)
    print()
    print("Vertical Line, shift=6; height=5:")
    vertical_line(6, 5)
    print()
    print("Two Vertical Lines, height=3; width=3:")
    two_vertical_lines(3, 3)
    print()
    print("Two Vertical Lines, height=4; width=5:")
    two_vertical_lines(4, 5)
    print()
    print("Two Vertical Lines, height=5; width=2:")
    two_vertical_lines(5, 2)

# Function 'horizontal_line' initialized
# requires 'width' value
def horizontal_line(width):
    for num in range(0, width):         # loops for the given 'width'
        print("*", end = '')            # to print out a line-segment
    print("")                           # prints a new line

# Function 'vertical_line' initialized
# requires 'shift' and 'height' values
def vertical_line(shift, height):
    # This function prints a single vertical line with
    # the line's length equal to 'height' and shifted
    # horizontally by 'shift'-number of spaces
    for num in range(0, height):        # loops for the given 'height'
        for space in range(0, shift):   # loops 'spaces' for the given 'shift'
            print(" ", end = '')        # prints out each 'space'
        print("*")                      # prints out a line-segment

# Function 'two_vertical_lines' initialized
# requires 'width' and 'height' values
def two_vertical_lines(height, width):
    # Two vertical lines are drawn,
    # with the length of each line equal to 'height'
    # and the width of each line being 'width' (including
    # each line-segment)
    for num in range(0, height):        # loops for the given 'height'
        print("*", end = '')            # prints the first line-segment
        for space in range(0, width-2): # loops 'spaces' for the given 'width'
                                        # two-space offset to account for each line-segment
            print(" ", end = '')        # prints out each 'space'
        print("*")                      # prints out a line-segment

# Main function is called, starting the program
main()
