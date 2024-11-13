# Python3 code to demonstrate working of
# Separate specific Strings
# Using re.split() + | operator
import re

# initializing string
test_str = 'geekforgeeksisbestforgeeks'

# printing original String
print("The original string is : " + str(test_str))

# initializing list words
sub_list = ["best"]

# regex to for splits()
# | operator to include all strings
temp = re.split(rf"({'|'.join(sub_list)})", test_str)
res = [ele for ele in temp if ele]

# printing result
print("The segmented String : " + str(res))
