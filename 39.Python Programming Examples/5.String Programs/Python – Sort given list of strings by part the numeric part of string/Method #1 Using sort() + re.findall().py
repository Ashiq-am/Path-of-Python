# Python3 code to demonstrate working of
# Sort Strings on numerical substrings
# Using sort() + findall()
import re

# helper function to perform sort
def num_sort(test_string):
	return list(map(int, re.findall(r'\d+', test_string)))[0]

# initializing list
test_list = ["Gfg34", "is67", "be3st", "f23or", "ge9eks"]

# printing original list
print("The original list is : " + str(test_list))

# calling function
test_list.sort(key=num_sort)

# printing result
print("Strings after numercial Sort : " + str(test_list))
