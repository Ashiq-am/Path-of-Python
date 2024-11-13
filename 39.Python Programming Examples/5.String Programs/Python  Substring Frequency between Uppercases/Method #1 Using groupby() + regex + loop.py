# Python3 code to demonstrate working of
# Substring Frequency between Uppercases
# Using groupby() + regex + loop
from itertools import groupby
import re

# initializing string
test_str = "GeEkSForGeEkS"

# printing original string
print("The original string is : " + test_str)

# Substring Frequency between Uppercases
# Using groupby() + regex + loop
res = {}
for i, j in groupby(re.findall(r'[A-Z][a-z]*\d*', test_str)):
	res[i] = res[i] + 1 if i in res.keys() else 1

# printing result
print("The grouped Substring Frequency : " + str(res))
