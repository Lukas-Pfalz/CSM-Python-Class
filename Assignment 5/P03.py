# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/26/20
# Description: Locate File
# Assignment # - 5

##### Template for Assignment X, problems 1-X ######

# Main Function is initialized
def main():
    # If a file with the filename entered by the user
    # exists, print out a confirmation message
    # If the file doesn't exist, tell the user the file
    # cannot be found

    # initialize counter
    num = 0

    # Loop checks through two files
    while num < 2:
        # Attempt to open a file
        try:
            # User is prompted to enter a file for grading
            file_title = input('Enter a class file to grade (i.e. class1 for class1.txt): ')

            file_name = str(file_title + '.txt')                # adds '.txt' extension to file name

            accessed_file = open(file_name, 'r')                # Opens text-file titled "file_name"
            print('Successfully opened ' + file_name + '\n')    # Print out a confirmation message
            accessed_file.close()                               # Closes the text-file

        # If the file does not exist (resulting in an IOError)
        except IOError:
            print('File cannot be found.\n')                    # print that the file doesn't exist

        # add 1 to counter to confirm one file was checked
        num = num + 1

# main program runs
main()
