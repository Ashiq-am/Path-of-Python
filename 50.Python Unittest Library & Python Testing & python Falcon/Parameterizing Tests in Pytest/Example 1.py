# Importing the math and Pytest libraries
import math
import pytest

# Creating first test case
@pytest.mark.parametrize("input, output", [(5.234, 5), (9.99, 10), (0.456, 0), (7.905, 7)])
def test_floor(input, output):
    assert output==math.floor(input)

# Creating second test case
@pytest.mark.parametrize("val, result", [(8, 60), (1, 1), (3, 10), (5, 25)])
def test_square_root(val, result):
    assert result==math.sqrt(val)
