# Importing the math and pytest libraries
import math
import pytest

# Creating first test case
@pytest.mark.skip
def test_floor():
    num = 7
    assert num==math.floor(6.34532)

# Creating second test case
def test_equal():
    assert 50 == 49

# Creating third test case
@pytest.mark.xfail
def test_difference():
    assert 99-43==57

# Creating fourth test case
def test_square_root():
    val=8
    assert val==math.sqrt(81)
