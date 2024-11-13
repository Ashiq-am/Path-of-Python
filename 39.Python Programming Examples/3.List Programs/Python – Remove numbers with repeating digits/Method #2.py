# Python3 code to demonstrate working of
# Remove numbers with repeting digits
# Using regex()
import re

# initializing list
test_list = [4252, 6578, 3421, 6545, 6676]

# printing original list
print("The original list is : " + str(test_list))

# regex used to remove elements with repeating digits
regx = re.compile(r"(\d).*\1")
res = [sub for sub in test_list if not regx.search(str(sub))]

# printing result
print("List after removing repeating digit numbers : " + str(res))
