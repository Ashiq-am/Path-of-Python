# Python3 code to demonstrate working of
# Sort Strings by maximum frequency character
# Using sorted() + lambda + Counter()
from collections import Counter

# getting maximum character frequency
def max_freq(arg_str):
	res = Counter(arg_str)
	return arg_str.count(max(arg_str, key = arg_str.get))

# initializing list
test_list = ["geekforgeeks", "bettered", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
# lambda function to drive logic
res = sorted(test_list,
			key = lambda arg_str : arg_str.count(
			max(Counter(arg_str), key = Counter(arg_str).get)))

# printing result
print("Sorted List : " + str(res))
