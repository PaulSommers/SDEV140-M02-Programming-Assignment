"""
Author: Paul Sommers
Date written: 10/29/2024
Assignment: Module 02 Programming Assignment Part 1
Short Desc: This program asks the user to enter two colors (red, blue, yellow) and displays the resulting secondary color.
            If the user enters something other than one of these options, the program will ask again until a valid color is entered.
"""

# Get the first primary color
while True:
    color1 = input("Enter the first primary color (red, blue, yellow): ").lower()
    if color1 == "red" or color1 == "blue" or color1 == "yellow":
        break  # Valid color entered, exit the loop
    else:
        print("Invalid color. Please enter 'red', 'blue', or 'yellow'.")

# Get the second primary color
while True:
    color2 = input("Enter the second primary color (red, blue, yellow): ").lower()
    if color2 == color1:
        print("Don't pick the same color!")
    elif color2 == "red" or color2 == "blue" or color2 == "yellow":
        break  # Valid color entered, exit the loop
    else:
        print("Invalid color. Please enter 'red', 'blue', or 'yellow'.")

# Determine the secondary color
if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("Red and blue make purple!")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("Red and yellow make orange!")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("Blue and yellow make green!")
else:
    print("Error!  Something unforeseen occurred.")