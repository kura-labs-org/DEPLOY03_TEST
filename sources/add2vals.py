'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
    print("")
    sys.exit(0)
    
elif argnumbers == 4 :
    print("")
    print("The result is " + str(calc.add4(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))))
    print("")
    sys.exit(0)

elif argnumbers != 2 or argunumbers != 4 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'add4vals A B C D' where A, B, C and D are individual values.")
    print("       If add4vals is not in your path, usage is './add4vals A B C D'.")
    print("       If unbundled, usage is 'python add4vals.py A B C D'.")
    print("")
    sys.exit(1)
