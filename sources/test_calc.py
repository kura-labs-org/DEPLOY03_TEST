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
        result = calc.add2(2, 3)
        self.assertEqual(result, 6)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2, 3)
        self.assertEqual(result, 15.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def', 'abc')
        self.assertEqual(result, 'abcdefabc')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3, 33)
        self.assertEqual(result, 'abc333')

    
    def test_subtract_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.subtract2(1, 2, 3)
        self.assertEqual(result, -4)

    def test_subtract_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.subtract2('10.5', 2, 3)
        self.assertEqual(result, 5.5)


if __name__ == '__main__':
    unittest.main()
