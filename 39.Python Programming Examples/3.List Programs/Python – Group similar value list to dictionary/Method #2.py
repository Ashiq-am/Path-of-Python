# Python3 code to demonstrate
# Group similar value list to dictionary
# using defaultdict() + loop
from collections import defaultdict

# Initializing lists
test_list1 = [4, 4, 4, 5, 5, 6, 6, 6, 6]
test_list2 = ['G', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Group similar value list to dictionary
# using defaultdict() + loop
res = defaultdict(set)
for key, val in zip(test_list1, test_list2):
	res[key].add(val)
res = {key: list(val) for key, val in res.items()}

# printing result
print ("Mapped resultant dictionary : " + str(res))
