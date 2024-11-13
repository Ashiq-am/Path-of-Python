# Python3 code to demonstrate working of
# Check for Whitespace in List
# Using in operator + any()
import re

# initializing list
test_list = ["Geeks forGeeks", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# Check for Whitespace in List
# Using in operator + any()
res = any('' in ele for ele in test_list)

# printing result
print("Does any string contain spaces ? " + str(res))
