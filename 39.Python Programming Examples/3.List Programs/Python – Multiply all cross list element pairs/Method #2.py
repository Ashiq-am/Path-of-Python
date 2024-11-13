# Python3 code to demonstrate
# Multiply all cross list element pairs
# using product()
from itertools import product

# Initializing lists
test_list1 = [4, 5, 6]
test_list2 = [6, 4, 2]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Multiply all cross list element pairs
# using product()
res = [a * b for a, b in product(test_list1, test_list2)]

# printing result
print("The multiplication list is : " + str(res))
