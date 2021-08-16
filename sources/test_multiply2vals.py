import pytest
import calc

@pytest.fixture
def practice_fixture():
    return {
        "test":"practice pytest"
    }


def test_multiplication():
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value

        """

        result = calc.multiply(3,3)
        assert result == 3 * 3

def test_float_multiplication():
        """
        Test that multiplication between an integer/float and another integer/float
        will return the correct value

        """

        result = calc.multiply('3.6', '5.4')
        assert result == (3.6*5.4)

def test_string_multiplication():
        """
        Test that a user can't multiply strings.
        """

        result = calc.multiply('3', 'A string')
        
        assert result == 'Error: Arguments must be an integer or float'

def fixture_usage(practice_fixture):
    assert practice_fixture['test'] == "practice pytest"
