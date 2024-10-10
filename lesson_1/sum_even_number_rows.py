"""
Sum Even Number Rows
Imagine a sequence of consecutive even integers beginning with two. The integers
are grouped in rows, with the first row containing one integer, the second row
two integers, the third row three integers, and so on. Given an integer 
representing the number of a particular row, return an integer representing the
sum of all the integers in that row. 

START 
Input: integer representing the row number
Output: integer representing the sum of all integers of the given row
Rules: 
    Explicit: 
        - Sequence of integers
        - Sequence begins with 2
        - Integers are consecutive
        - Integers are even
        - Sequences are grouped into rows
        - Each row is incrementally larger than the last 1, 2, 3, ...
    Implicit: 
        - Row 1 has 1 element, row 2 has 2 elements, etc
    - 2
    - 4, 6
    - 8, 10, 12
    - 14, 16, 18, 20
    - 22, 24, 26, 28, 30

Algorithm: 
- Create a create_rows function that takes a single argument, row_number
- Declare a rows variable and initialise it to an empty list
- Declare a counter variable to 1
- Declare a current_iteration to 2

HERE
- For each number from counter to row_number   
    - Add an empty list to rows
    -   for number in range(counter: row_number)
        - Append current_iteration
        - Increment current_iteration by 2


END
"""

## The PEDAC Process

## Sum Even Number Rows
# Imagine a sequence of consecutive even integers beginning with two. The integers
# are grouped in rows, with the first row containing one integer, the second row
# two integers, the third row three integers, and so on. Given an integer 
# representing the number of a particular row, return an integer representing the
# sum of all the integers in that row. 

## P: Understand the Problem
#   - Input: Integer representing the row number
#   - Output: Integer representing the sum of all numbers in that row
#   - Explicit 
#       - Sequence of numbers
#       - Sequence begins with 2
#       - Integers are consecutive
#       - Integers are even
#       - Sequence is grouped into rows
#       - Each row is incrementally larger than the last 1, 2, 3, ...

#   - Implicit 
#       - Row 1 has 1 element, Row 2 has 2 elements, Row 3 has 3 elements, etc

# - Establish the rules define the boundaries of the problem
# - Restate the problem in your own words
# - Identify problem requirements: 
# Identify Inputs and Outputs 
# Ask questions / identify unclear information
# Spend enough time here. Don't rush.

## General Example: 
# Given a string 
 
## E: 
## D:
## A: 
## C:


def create_rows(row_number):
    rows = []
    for num in range(row_number):
        rows.append([])
    print(rows)
    
    value = 2
    for list in rows:
        count = 0
        while count < row_number:
            list.append(value)
            count += 1
            value += 2
    
    print(f'{rows = }')

create_rows(1) # 2 -> [2]
create_rows(2) # 10 -> [4, 6]
create_rows(3) # 30 -> [8, 10, 12]
create_rows(5) # 130 -> [22, 24, 26, 28, 30]
