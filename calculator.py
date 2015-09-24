"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

def calculator_answers():
    """Allows users to abbreviate calculations

    User can input numbers for calculations 
    as long as they indicate whether they want to continue or not. 
    """

    want_to_calculate = 'Y'

    while want_to_calculate == 'Y':

        tokens = raw_input("> ").split(" ")

        if len(tokens) == 2:
            function = tokens[0]
            num1 = int(tokens[1])

        if len(tokens) == 3:
            function = tokens[0]
            num1 = int(tokens[1])
            num2 = int(tokens [2])

        if tokens[0] == 'q':
            print "That's it!"


        if function == '+':
            print add(num1, num2)

        if function == "-":
            print subtract(num1, num2)

        if function == "*":
            print multiply(num1, num2)

        if function == "/":
            print divide(num1, num2)

        if function == "square": 
            print square(num1)

        if function == "cube":
            print cube(num1)

        if function == "pow":
            print power(num1, num2)

        if function == "mod":
            print mod(num1, num2)

        want_to_calculate = raw_input("Do you want to calculate something else? (Y/N): ").upper()

    if want_to_calculate == 'N':
        print "Goodbye!"

calculator_answers()
