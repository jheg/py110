# Searching 101
# Write a program that solicits six (6) numbers from the user and prints a 
# message that describes whether the sixth number appears among the first five.

# Examples:
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

"""
Given six inputs from a user, expected to be whole numbers, check to see if the 
last number given appears in the first five numbers. If it is, then return a  
confirmation that number is in the list of five numbers. If it is not then 
confirm it is not in the list of five numbers. 

Input: 6 string inputs from a user
Output: string

Rules: 
Explicit: 
- Inputs are numbers
- There are exactly six inputs
Implicit: 
- Numbers are not negative
- Numbers are whole numbers

Data structures:
- Integers for the user input 
- A list to hold the inputs

Algorythm:
- Create a five_numbers list and append five numbers from a user input
- Create a sixth_number variable and assign it to an integer input from the user
- If the sixth_number is in five_numbers
    - display a message to the user to confirm the sixth number is in the list
- else
    - display a message to the user to confirm the sixth number is not in the list
"""

five_numbers = []

def get_five_numbers():
    for num in range(5):
        user_input = int(input(f'Enter number {num + 1}: '))
        if user_input < 26:
            user_input = int(input(
                f'Number must be greater than 25, Enter number {num + 1}: '
                ))
        else:
            five_numbers.append(str(user_input))

def display_result():
    sixth_number = input('Please enter your sixth number: ')

    if sixth_number in five_numbers:
        print(f'{sixth_number} is in {', '.join(five_numbers)}')
    else:
        print(f'{sixth_number} is not in {', '.join(five_numbers)}')

def play_game():
    get_five_numbers()
    display_result()

play_game()

"""
The above code splits the main parts of the program into 2 functions 
(get_five_numbers, display_result) and a third function, play_game to keep 
things neat.

Most of the work is done inside the get_five_numbers function which asks the 
user to enter five numbers. Each of these is coerced into an integer and 
checked to ensure it is greater than 25. If the number is greater than 25 it is 
coerced back to a string and added to a list five_numbers storing the user inputs .

This approach allows me to apply a condition that needs to be satisfied from 
the users input (e.g., a number greater than 25).

The display_result function gets the sixth input from the user and then checks 
to see if the value is in five_numbers before displaying the appropriate 
message to the user.
"""