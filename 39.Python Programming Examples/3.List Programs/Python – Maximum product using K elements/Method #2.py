# Python code to demonstrate
# Maximum product using K elements
# using max() + reduce() + combination() + mul + list comprehension
from itertools import combinations
from operator import mul

# Initializing list
test_list = [8, 5, 9, 11, 3, 7]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 4

# Maximum product using K elements
# using max() + reduce() + combination() + mul + list comprehension
res = max([reduce(mul, ele) for ele in combinations(test_list, K)])

# printing result
print ("Maximum product using K elements : " + str(res))
