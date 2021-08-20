import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')
        
     #New code
    
    def test_minus_integers(self):
        result = calc.add2(3, -5)
        self.assertEqual(result, -2)
        
    #Simple Math Calc Causes an Error!    
#     def test_minus_ints(self):
#         result = calc.add2(3, -4):
#         self.assertEqual(result, -6)

     def add_num_decimals(self):
#         ask_question_1 = int(input("How many numbers do you want to add:))
#         sum = 0
                                   
#         for i in range(0, ask_question_1):
#             num = int(input(""))
#             sum = sum + num
                                   
#         result = calc.add2(0,sum):
        num1 = '0'
        num2 = '1'
        sum_of_2nums = num1 + num2
                  
        self.assertEqual(result, sum_of_2nums)

if __name__ == '__main__':
    unittest.main()
