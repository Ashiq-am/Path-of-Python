# Python3 code to demonstrate
# the application of expm1()
import math

# initializing the value
test_int = 1e-10

# checking expm1() values
# expm1() is more accurate
print ("The value with exp()-1 : " + str(math.exp(test_int)-1))
print ("The value with expm1() : " + str(math.expm1(test_int)))
