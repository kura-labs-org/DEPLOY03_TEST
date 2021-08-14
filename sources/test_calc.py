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
        result = calc.add2(1, 2, 4, 6, 10)
        self.assertEqual(result, 23)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2, 22.1, 44, 0.3)
        self.assertEqual(result, 78.9)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def', 'xyz', 'hijk', 'qrs')
        self.assertEqual(result, 'abcdefxyzhijkqrs')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3, 'xyz', 4, 'dbx')
        self.assertEqual(result, 'abc3xyz4dbx')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add2('abc', '5.5','xyz', '11.6', 'dbx')
        self.assertEqual(result, 'abc5.5xyz11.6dbx')

if __name__ == '__main__':
    unittest.main()
