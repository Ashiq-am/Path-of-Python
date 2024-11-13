# Python3 code to demonstrate working of
# Extract Combination Mapping in two lists
# using zip() + product()
from itertools import product

# initialize lists
test_list1 = [3, 4, 5]
test_list2 = ['x', 'y']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Extract Combination Mapping in two lists
# using zip() + product()
res = list(list(zip(test_list1, ele)) for ele in product(test_list2, repeat = len(test_list1)))

# printing result
print("Mapped Combination result : " + str(res))
