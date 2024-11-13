# Python3 code to demonstrate working of
# Filter list by Boolean list
# Using itertools.compress
from itertools import compress

# initializing list
test_list = [6, 4, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# initializing Boolean list
bool_list = [True, False, False, True, True]

# printing boolean list
print("The bool list is : " + str(bool_list))

# Filter list by Boolean list
# Using itertools.compress
res = list(compress(test_list, bool_list))

# Printing result
print("List after filtering is : " + str(res))
