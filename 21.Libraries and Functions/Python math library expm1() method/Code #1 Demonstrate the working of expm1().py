# Python3 code to demonstrate
# the working of expm1()
import math

# initializing the value
test_int = 4
test_neg_int = -3

# checking expm1() values
# doesn't throw error with negative
print("The expm1 value using positive integer : "
      + str(math.expm1(test_int)))

print("The expm1 value using negative integer : "
      + str(math.expm1(test_neg_int)))
