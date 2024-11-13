# Python3 code to demonstrate working of
# Charatacter indices Mapping in String List
# Using defaultdict() + enumerate() + split()
from collections import defaultdict

# initializing list
test_list = ['g f g', 'i s', 'b e s t', 'f o r', 'g e e k s']

# printing original list
print("The original list is : " + str(test_list))

res = defaultdict(set)

# loop for assigning indices
for idx, ele in enumerate(test_list):
	for sub in ele.split():
		res[sub].add(idx + 1)

# dictionary comprehension to remake result
res = {key: list(val) for key, val in res.items()}

# printing result
print("The mapped dictionary : " + str(res))
