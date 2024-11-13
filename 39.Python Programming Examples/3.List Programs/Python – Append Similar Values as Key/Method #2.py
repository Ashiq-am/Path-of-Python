# Python3 code to demonstrate working of
# Append Similar Values as Key
# Using defaultdict() + loop
from collections import defaultdict

# initializing list
test_list = ['Manjeet', 'Nikhil', 'Akshat', 'Akash',
		'Manjeet', 'Akash', 'Akshat', 'Manjeet']

# printing original list
print("The original list is : " + str(test_list))

# Append Similar Values as Key
# Using defaultdict() + loop
res = defaultdict(list)
for sub in test_list:
	res[sub].append(sub)

# printing result
print("The similar values dictionary is : " + str(dict(res)))
