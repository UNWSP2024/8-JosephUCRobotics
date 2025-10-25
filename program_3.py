# Author: Joseph Kracht
# Last Modified: 10/23/2025
# Title: Capital Quiz

import random

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).

# Make dictionary of states and capitals
state_capitals = {"Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas":"Little Rock", "California":"Sacramento", "Colorado":"Denver",
                  "Connecticut":"Hartford", "Delaware":"Dover", "Florida":"Tallahassee", "Georgia":"Atlanta", "Hawaii":"Honolulu",
                  "Idaho":"Boise", "Illinois":"Springfield","Indiana":"Indianapolis","Kansas":"Topeka","Kentucky":"Frankfort",
                  "Louisiana":"Baton Rouge", "Maine":"Augusta", "Maryland":"Annapolis","Massachusetts":"Boston",
                  "Michigan":"Lansing","Minnesota":"Saint Paul", "Mississippi":"Jackson", "Missouri":"Jefferson City",
                  "Montana":"Helena", "Nebraska":"Lincoln", "Nevada":"Carson City", "New Hampshire":"Concord",
                  "New Jersey":"Trenton", "New Mexico":"Santa Fe", "New York":"Albany", "North Carolina":"Raleigh",
                  "North Dakota":"Bismarck", "Ohio":"Columbus", "Oklahoma":"Oklahoma City", "Oregon":"Salem",
                  "Pennsylvania":"Harrisburg","Rhode Island":"Providence", "South Carolina":"Columbia", "South Dakota":"Pierre",
                  "Tennessee":"Nashville", "Texas":"Austin", "Utah":"Salt Lake City", "Vermont":"Montpelier", "Virginia":"Richmond",
                  "Washington":"Olympia", "West Virginia":"Charleston", "Wisconsin":"Madison", "Wyoming":"Cheyenne"}

quizzing = True
correct = 0
incorrect = 0
while quizzing:
    # Pick a random key
    key = random.choice(list(state_capitals.keys()))

    # Git the user input
    guess = input("What is the capital of " + key +"?: ")

    # Process the guess
    if guess.strip().lower() == state_capitals[key].lower():
        print("Correct!")
        correct += 1
    else:
        print("Incorrect. The Capital of " + key + " is " + state_capitals[key] + ".")
        incorrect += 1

    # Check if the user is done
    input_to_end = int(input("Press 1 to continue or press 2 to exit: "))
    if input_to_end != 1:
        quizzing = False

# Display total correct and incorrect
print("You got " + str(correct) + " correct and " + str(incorrect) + " incorrect.")
