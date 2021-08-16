import unittest
from unittest import result
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

    def test_multiplication(self):
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value

        """

        result = calc.multiply(3,3)
        self.assertEqual(result, 9)

    def test_float_multiplication(self):
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value

        """

        result = calc.multiply('3.6', '5.4')
        self.assertEqual(result,3.6*5.4)

    def test_string_multiplication(self):
        """
        Test that a user can't multiply strings.
        """

        result = calc.multiply('3', 'A string')
        
        self.assertEqual(result, 'Error: Arguments must be an integer or float')


if __name__ == '__main__':
    unittest.main()
