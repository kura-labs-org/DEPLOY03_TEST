'''
A simple command line tool that takes 2 values and multiplies them using
the calc.py library's 'multi2' function.
'''

import sys
import calc

def _input(message, input_type=str):
    count = 0
    while True and count < 3:
      try:
        count += 1
        return input_type (input(message))
      except:
        pass
    if count >= 3:
      print('Max tries exceeded')
      return False

if __name__ == '__main__':

    number1 = False
    number2 = False

    number1 = _input("Enter your first number : ", str)
    if number1 != False:
      number2 = _input("Enter your second number : ", str)
      
    if (number1 != False) and (number2 != False):
        print("")
        print("The result is " + str(calc.multi2(str(number1), str(number2))))
        print("")
        sys.exit(0)
    else:
        print("")
        print("You entered non-number value/s.")
        print("")
        print("Usage: 'multi2vals' where user is pompted to enter 2 numbers.")
        print("       If multi2vals is not in your path, usage is './multi2vals'.")
        print("       If unbundled, usage is 'python multi2vals.py'.")
        print("")
        sys.exit(1)
