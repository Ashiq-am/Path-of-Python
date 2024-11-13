# Python3 code to demonstrate working of
# Sort Strings by maximum frequency character
# Using sort() + Counter() + max()
from collections import Counter

# getting maximum character frequency
def max_freq(arg_str):
	res = Counter(arg_str)
	return arg_str.count(max(res, key = res.get))

# initializing list
test_list = ["geekforgeeks", "bettered", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
test_list.sort(key = max_freq)

# printing result
print("Sorted List : " + str(test_list))
