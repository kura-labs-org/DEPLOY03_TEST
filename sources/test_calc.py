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

if __name__ == '__main__':
    unittest.main()
    
    
class TestSecondCalc(unittest.TestCase):
    """
    Test the minus function from the calc library
    """

    def test_minus_integers(self):
        """
        Test that the subtraction of two integers returns the correct total
        """
        result = calc.minus2(1, 2)
        self.assertEqual(result, -1)

    def test_minus_floats(self):
        """
        Test that the subtractions of two floats returns the correct result
        """
        result = calc.minus2('10.5', 2)
        self.assertEqual(result, 8.5)

if __name__ == '__main__':
    unittest.main()
