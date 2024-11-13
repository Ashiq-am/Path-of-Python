# Importing the math library
import math

# Creating first test case
def test_check_floor():
    num = 6
    assert num==math.floor(6.34532)

# Creating second test case
def test_check_equal():
    assert 50 == 49

# Creating third test case
def test_check_difference():
    assert 99-43==57

# Creating fourth test case
def test_check_square_root():
    val=9
    assert val==math.sqrt(81)
