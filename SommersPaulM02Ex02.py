"""
Author: Paul Sommers
Date written: 10/29/2024
Assignment: Module 02 Programming Assignment Part 2
Short Desc: This program prompts the user to enter a non-negative integer and calculates the factorial.
"""

# Get a non-negative integer from the user and loop until one is entered
while True:
    num = int(input("Enter a non-negative integer: "))
    if num >= 0:
        break
    else:
        print("Error: Invalid input. Please enter a non-negative integer.")

# Initialize the factorial and counter
factorial = 1
count = 1

# Calculate the factorial
while count <= num:
    factorial *= count
    count += 1
    

# Show the result
print(f"The factorial of {num} is {factorial}.")