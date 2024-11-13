# Python3 code to demonstrate working of
# Restrict Tuples by frequency of first element's value
# Using defaultdict() + filter() + lambda
from collections import defaultdict

# initializing list
test_list = [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5),
			(3, 4), (1, 4), (3, 4), (4, 7)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

mem = defaultdict(list)

# filtering result using filter() and lambda function
res = list(filter(lambda sub: mem[sub[0]].append(
	sub[0]) or len(mem[sub[0]]) <= K, test_list))

# printing result
print("Filtered tuples : " + str(res))
