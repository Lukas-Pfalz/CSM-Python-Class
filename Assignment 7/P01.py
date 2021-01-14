# Name: Lukas Pfalz
# Section: CSC-1110-71762
# Date: 8/9/20
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

    # remove punctuation from initial phrase to find matches
    new_sentence = ""
    for character in user_phrase:
        # removes any character that isn't a space or alphanumeric
        if character.isalnum() or character.isspace():
            new_sentence += character
    phrase = new_sentence.split()

    # compare the words in that phrase to the keys in the thesaurus
    for word in phrase:
        # If the key can be found
        value = word.lower()
        if value in thesaurus:
            phrase[phrase.index(word)] = thesaurus[value].upper()

    # words that are changed are printed in uppercase letters
    for words in phrase:
        print(words, end = " ")

# Run main program
main()
