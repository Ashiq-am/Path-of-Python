# Python3 code to demonstrate
# getting size of string in bytes
# using sys.getsizeof()
import sys

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))

# using sys.getsizeof()
# getting size of string in bytes
res = sys.getsizeof(test_string)

# print result
print("The length of string in bytes : " + str(res))
