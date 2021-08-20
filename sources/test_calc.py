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
        
     #New code Shown below:
    
    def test_minus_integers(self):
        result = calc.add2(3, -5)
        self.assertEqual(result, -2)
        
    #Simple Math Calc Causes an Error!    
    def return_minus_int(self):
        result = calc.add2(-5, -1):
        self.assertEqual(result, -6)

    def add_many_nums(self):
        sum = 0
        how_many_num = int(input(""))
        for i in range(0, how_many_num):
            num_enter = int(input(""))
            sum = sum + num_enter
        
        #num1 = int(input(""))        
        result = calc.add2(sum, '0')
        self.assertEqual(result, sum)
        

if __name__ == '__main__':
    unittest.main()
