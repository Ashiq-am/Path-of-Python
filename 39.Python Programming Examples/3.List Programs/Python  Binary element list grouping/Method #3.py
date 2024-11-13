# Python3 code to demonstrate
# to perform binary list grouping
# using collections.defaultdict()
import collections

# initializing list
test_list = [["G", 0], ["F", 0], ["B", 2],
			["E", 2], ['I', 1], ['S', 1],
			['S', 2], ['T', 2], ['G', 0]]

# using collections.defaultdict()
# to perform binary list grouping
res = collections.defaultdict(list)
for val in test_list:
	res[val[1]].append(val[0])

# printing result
print ("The grouped list is : " + str(res.values()))
