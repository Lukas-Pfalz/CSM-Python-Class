# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 7/4/20
# Description: Thesaurus
# Assignment # - 7

##### Template for Assignment X, problems 1-X ######
def main():
    # define our simple thesaurus
    thesaurus = {
                  "happy": "glad",
                  "sad"  : "bleak"
                }

    # Prompt the user for a phrase
    user_phrase = input("Enter a phrase: ")

    # remove all punctuation from the initial phrase to
    # find all possible matches
    phrase = user_phrase.split()

    # compare the words in that phrase to the keys in the thesaurus


    # If the key can be found, replace original word with
    # random synonym for that word

    # words that are changed are printed in uppercase letters
    for words in phrase:
        print(words, end = " ")

# Run main program
main()