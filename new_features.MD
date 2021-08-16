# Creating Multiplication Feature

Created multi2vals.py to accept 2 floats or integers from user input, multiply them and print the answer to the screen

- User is prompted to enter the first number
- If user enter a number, the user is prompted to enter the second number
- If user enters a non-number character, the user is given two more chances before the user is given a notice that the maximum numbe of attempts has been exceeded and the programme closes

## Failed Unit Tests
Tests were conducted directly on function and not on user input inteaction.

Tests failed under the following three conditions

### Multiplying an integer by a string
Function incorrectly converts both inputs to strings and therefore fails with a Type Error

### Multiplying a float by a string
A float can not be multiplied by a string and function therefore fails with a Type Error

### Multiplying two strings
Two strings can not be multiplied by each other and function therefore fails with a Type Error

## Corrections to Code
Adjustment were made to code and some to account for proper multiiplication logic.

### Multiplying an integer by a string
Function now checks to see if one value is a string and the other is a numnber and does not automatically convert both to strings

### Multiplying a float by a string
The function now informs the user that a float and a string can not be multiplied

### Multiplying two strings
The function now informs the user that two strings can not be multiplied
