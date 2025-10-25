# Author: Joseph Kracht
# Last Modified: 10/23/2025
# Title: Initials

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names,
# and displays their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here

    # Split the name at the spaces
    full_name_list = personsName.split()

    # Loop through each word
    for name in full_name_list:
        # Add the first letter of the word and a ". " to the initials string
        personsInitials += name[0].upper()
        personsInitials += ". "

    # Return the initials string
    return personsInitials.strip()

# Get the users name
personsName = input('Enter the users first, middle, and last name: ')

# Call the function
initials = initials_generator(personsName)

# Print the result
print(initials)
