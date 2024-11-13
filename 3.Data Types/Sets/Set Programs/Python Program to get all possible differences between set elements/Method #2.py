# Python3 code to demonstrate working of
# All elements difference in Set
# Using set comprehension + combinations() + abs()
from itertools import combinations

# initializing strings set
test_set = {1, 5, 2, 7, 3, 4, 10, 14}

# printing original string
print("The original set is : " + str(test_set))

# set comprehension providing consize solution
res = {abs(x - y) for x, y in combinations(test_set, 2)}

# printing result
print("All possible differences : " + str(res))
