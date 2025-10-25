# Author: Joseph Kracht
# Last Modified: 10/24/2025
# Title: Course Finder

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.
from os.path import split

class_dictionary = {}

while True:
    # Get class id
    class_id = input("Enter a class id or enter q to quit entering classes: ").strip()

    # Check to see if the user is done entering classes
    if class_id.lower().strip() == "q":
        break

    # Get class name
    class_name = input("Enter the course name for course " + class_id + ": ").strip()

    # Add class id and name to a dictionary
    class_dictionary[class_id] = class_name

# Get subject
subject = input("Enter a subject: ").upper()

# Display list of classes in that subject
print("Hear a list of all of the classes in the subject " + subject + ":")
for key in class_dictionary.keys():
    if key.split()[0].upper() == subject:
        print("ID: " + key + ", Name: " + class_dictionary[key])
