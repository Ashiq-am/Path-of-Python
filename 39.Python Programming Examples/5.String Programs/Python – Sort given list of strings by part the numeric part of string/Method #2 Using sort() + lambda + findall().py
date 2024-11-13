# Python3 code to demonstrate working of
# Sort Strings on numerical substrings
# Using sort() + lambda + findall()
import re

# initializing list
test_list = ["Gfg34", "is67", "be3st", "f23or", "ge9eks"]

# printing original list
print("The original list is : " + str(test_list))

# findall() getting all integers.
# conversion to integers using map()
test_list.sort(key=lambda test_string : list(
	map(int, re.findall(r'\d+', test_string)))[0])

# printing result
print("Strings after numercial Sort : " + str(test_list))
