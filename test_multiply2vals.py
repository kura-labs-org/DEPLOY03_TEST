# test_multiply2vals.py
import pytest
import calc

def test_multiplication():
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value.

        """

        result = calc.multiply(3,3)
        assert result == 3 * 3

def test_float_multiplication():
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value.

        """

        result = calc.multiply('3.6', '5.4')
        assert result == (3.6*5.4)


def test_string_multiplication():
        """
        Test that a user can't multiply strings. And that it will return the correct error.
        """

        result = calc.multiply('3', 'A string')
        
        assert result == 'Error: Arguments must be an integer or float'

