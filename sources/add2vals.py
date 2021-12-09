'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

choosing_ops = input("Choose. Do you want to add two numbers or multiply? (add) or (multiply)")

if choosing_ops == "add":
    ops = calc.add2
elif choosing_ops == "multiply":
    ops = calc.mul2
else:
    print("You didn't type in the allowed option")
    sys.exit(0)

mod_numbers = []
number = input("Give me a number ")
mod_numbers.append(number)
number = input("Give me another number ")
mod_numbers.append(number)



argnumbers = len(mod_numbers)

if argnumbers == 2 :
    print("")
    print("The result is " + str(ops(str(mod_numbers[0]), str(mod_numbers[1]))))
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
#    print("")
#    print("Usage: 'add2vals X Y' where X and Y are individual values.")
#    print("       If add2vals is not in your path, usage is './add2vals X Y'.")
#    print("       If unbundled, usage is 'python add2vals.py X Y'.")
#    print("")
    sys.exit(1)
