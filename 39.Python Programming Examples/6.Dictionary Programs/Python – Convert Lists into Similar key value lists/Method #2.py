# Python3 code to demonstrate working of
# Convert Lists into Similar key value lists
# Using defaultdict() + list comprehension + zip()
from collections import defaultdict

# initializing lists
test_list1 = [5, 6, 6, 4, 5, 6]
test_list2 = [8, 3, 2, 9, 10, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# creating a mesh of keys using defaultdict
res = defaultdict(list)
[res[key].append(val) for key, val in zip(test_list1, test_list2)]

# printing result
print("The mapped dictionary : " + str(dict(res)))
