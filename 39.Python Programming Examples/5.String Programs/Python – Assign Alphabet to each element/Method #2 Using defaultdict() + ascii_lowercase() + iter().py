# Python3 code to demonstrate working of
# Assign Alphabet to each element
# Using defaultdict() + ascii_lowercase() + iter()
from collections import defaultdict
import string

# initializing list
test_list = [4, 5, 2, 4, 2, 6, 5, 2, 5]

# printing list
print("The original list : " + str(test_list))

# assigning lowecases as iterator
temp = iter(string.ascii_lowercase)

# lambda functions fits to similar elements
res = defaultdict(lambda: next(temp))

# flatten in list
res = [res[key] for key in test_list]

# printing results
print("The mapped List : " + str(list(res)))
