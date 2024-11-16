# Python code to demonstrate
# user-defined function as ufunc
import numpy as np

# create an array of numbers
a = np.array([345, 122, 454, 232, 334, 56, 66])


# user-defined function to check
# whether a no. is palindrome or not
def fun(x):
    s = str(x)
    return s[::-1] == s


# 'check_palindrome' as universal function
check_palindrome = np.frompyfunc(fun, 1, 1)
print("Original array-", a)
print("Checking of number as palindrome-",
      check_palindrome(a))
