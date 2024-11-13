# Python3 code to demonstrate
# Element Occurrence in dictionary value list
# using collections.Counter()
from collections import Counter

# initializing dictionary
test_dict = { "Akshat" : [1, 4, 5, 3],
			"Nikhil" : [4, 6],
			"Akash" : [5, 2, 1] }

# initializing test list
test_list = [2, 1]

# printing original dict
print("The original dictionary : " + str(test_dict))

# printing original list
print("The original list : " + str(test_list))

# using collections.Counter()
# Element Occurrence in dictionary value list
# omits the 0 occurrence word key
res = dict(Counter(j for j in test_dict
		for i in test_list if i in test_dict[j]))

# print result
print("The summation of element occurrence : " + str(res))
