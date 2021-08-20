# '''
# A simple command line tool that takes 2 values and adds them together using
# the calc.py library's 'add2' function.
# '''

# import sys
# import calc

# argnumbers = len(sys.argv) - 1

# if argnumbers == 2 :
#     print("")
#     print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
#     print("")
#     sys.exit(0)

# if argnumbers != 2 :
#     print("")
#     print("You entered " + str(argnumbers) + " value/s.")
#     print("")
#     print("Usage: 'add2vals X Y' where X and Y are individual values.")
#     print("       If add2vals is not in your path, usage is './add2vals X Y'.")
#     print("       If unbundled, usage is 'python add2vals.py X Y'.")
#     print("")
#     sys.exit(1)
    
    
'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

#Changes
#Implement a number for condition
#Line 18 is a new line
#Changed the addition fof first if statement to be more understandable from reading top to bottom
#Removed some print("")
#Line 33 and 34 is now 33. Added a \n for new line for line 35 is line 34
#Incremented num_counter to add all sys.argv below


num = int(input("Enter a number:")
sum = 0
num_counter = 0
          
argnumbers = len(sys.argv) - 1

if argnumbers == num :
    for i in range(0, num):
        print("\n")
        #print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
        sum = sum + sys.argv[num_counter]
        num_counter = num_counter + 1  
         
    sum_str = str(sum)
    print(f"The result is {sum_str}")
          
    print("The result for indexes 1 and 2 is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))      
          
    #print("")
    sys.exit(0)

if argnumbers != num :
    #print("")
    print("You entered " + str(argnumbers) + " value/s.")
    #print("")
    print("Usage: add2vals X Y, where X and Y are individual values. \n If add2vals is not in your path, usage is ./add2vals X Y.")
    print("If unbundled, usage is python add2vals.py X Y.")
    #print("")
    sys.exit(1)
