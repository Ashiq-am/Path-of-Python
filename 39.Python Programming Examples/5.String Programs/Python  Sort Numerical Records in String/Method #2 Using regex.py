# Python3 code to demonstrate working of
# Sort Numerical Records in String
# Using regex
import re

# initializing string
test_str = "Akshat 15 Nikhil 20 Akash 10"

# printing original string
print("The original string is : " + test_str)

# Sort Numerical Records in String
# Using regex
temp1 = re.findall(r'([A-z]+) (\d+)', test_str)
temp2 = sorted(temp1, key = lambda ele: (int(ele[1]), ele[0]))
res = ' '.join(' '.join(ele) for ele in temp2)

# printing result
print("The string after sorting records : " + res)
