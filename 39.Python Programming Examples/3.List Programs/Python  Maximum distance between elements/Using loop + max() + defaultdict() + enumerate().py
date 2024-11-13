# Python3 code to demonstrate
# Maximum distance between elements
# using max() + enumerate() + loop + defaultdict()
from collections import defaultdict

# Initializing list
test_list = [4, 5, 6, 4, 6, 3]

# printing original list
print("The original list is : " + str(test_list))

# Maximum distance between elements
# using max() + enumerate() + loop + defaultdict()
temp = defaultdict(list)
for idx, ele in enumerate(test_list):
	temp[ele].append(idx)
res = max(temp[ele][-1]-temp[ele][0] for ele in temp)

# printing result
print ("Maximum distance between same element is : " + str(res))
