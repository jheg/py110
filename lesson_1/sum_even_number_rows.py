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
1 Create a rows list to hold all our rows
2 Create a row list and add it to the rows list 
3 Repeat adding rows until all rows have been created
    - All the rows have been created when the length of the 'rows' list is equal to the input
4 Sum the final row
5 Return the sum of the last row

    - Problem: 2: Create a row
    - Rules: 
        - The row is a list
        - Row contains integers
        - The integers are consecutive even numbers
        - The integers in each row form part of an overall sequence
        - Each row has a different length

        Input: 
            - Length of the row 
            - The starting integer 
        Output: The row itself  --> [8, 10, 12]

    Examples: 
    - Start: 2, length: 1 --> [2]
    - Start: 4, length: 2 --> [4, 6]
    - Start: 8, length: 3 --> [8, 10, 12]

    - Data structures: list

    Algorithm:
        1 Create an empty row containing the integers
        2 Add the starting integer   
        3 Increment the starting integer by 2 to get the next integer in the sequence
        4 Repeat steps 2 & 3 until row has reached the correct length
        5 Return the 'row' list

END
"""

def sum_even_number_row(row_number):
    rows = []
    start_integer = 2
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = row[-1] + 2

    return sum(rows[-1])

def create_row(start_integer, row_length):
    row = []
    current_integer = start_integer
    while len(row) < row_length:
        row.append(current_integer)
        current_integer += 2
    return row

print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)