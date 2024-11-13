# Python3 code to demonstrate working of
# Filter rows without Space Strings
# Using list comprehension + any() + regex
import re

# initializing list
test_list = [["gfg is", "best"], ["gfg", "good"],
			["gfg is cool"], ["love", "gfg"]]

# printing original list
print("The original list is : " + str(test_list))

# checking for spaces using regex
# not including row if any string has space
res = [row for row in test_list if not any(
	bool(re.search(r"\s", ele)) for ele in row)]

# printing result
print("Filtered Rows : " + str(res))
