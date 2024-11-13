# Python3 code to demonstrate working of
# Frequency Key Values Summation
# Using reduce() + Counter() + lambda + __add__
from functools import reduce
from collections import Counter

# initializing dictionary
test_dict = {70 : [7, 4, 6],
			100 : [8, 9, 5],
			200 : [2, 5, 3, 7],
			50 : [6, 8, 5, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Counter() used to get values mapped with keys
# __add__ used to add key with values.
res = reduce(Counter.__add__, map(lambda sub: Counter({ele : sub[0] for ele in sub[1]}),
					test_dict.items()) )
# printing result
print("Extracted Summation dictionary : " + str(dict(res)))
