# Python3 code to demonstrate working of
# All combination Dictionary List
# Using product() + list comprehension + dictionary comprehension
from itertools import product

# initializing lists
test_list1 = ["Gfg", "is", "Best"]
test_list2 = [4, 5]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# generating combinations
temp = product(test_list2, repeat = len(test_list1))

# constructing dicts using combinations
res = [{key : val for (key , val) in zip(test_list1, ele)} for ele in temp]

# printing result
print("The combinations dictionary : " + str(res))
