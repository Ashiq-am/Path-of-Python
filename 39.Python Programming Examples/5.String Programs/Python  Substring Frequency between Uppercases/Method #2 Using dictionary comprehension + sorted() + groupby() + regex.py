# Python3 code to demonstrate working of
# Substring Frequency between Uppercases
# Using dictionary comprehension + sorted() + groupby() + regex
from itertools import groupby
import re

# initializing string
test_str = "GeEkSForGeEkS"

# printing original string
print("The original string is : " + test_str)

# Substring Frequency between Uppercases
# Using dictionary comprehension + sorted() + groupby() + regex
res = {i : len(list(j)) for i, j in groupby(
		sorted(re.findall(r'[A-Z][a-z]*\d*', test_str))) }

# printing result
print("The grouped Substring Frequency : " + str(res))
