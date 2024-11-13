# Importing the math and Pytest libraries
import math
import pytest

# Creating first test case
@pytest.mark.execute
def test_floor():
    num = 6
    assert num==math.floor(6.34532)

# Creating second test case
def test_equal():
    assert 50 == 49

# Creating third test case
@pytest.mark.execute
def test_difference():
    assert 99-43==57

# Creating fourth test case
def test_square_root():
    val=8
    assert val==math.sqrt(81)
