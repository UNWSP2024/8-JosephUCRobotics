# Author: Joseph Kracht
# Last Modified: 10/23/2025
# Title: Word Separator

# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase.
# Convert the sentence to a string in which the words are separated by spaces,
# and the first word starts with an uppercase.
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    # set the first char in the new sentence to the upper first char in the old sentence
    new_sentence = sentence[0].upper()

    # loop through each char in the old sentence not counting the first char
    for char in sentence[1:]:
        # if the char is upper make a new word
        if char.isupper():
            new_sentence += " "
        # add the char
        new_sentence += char.lower()

    # add a "." to the end of the sentence
    new_sentence +="."

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
