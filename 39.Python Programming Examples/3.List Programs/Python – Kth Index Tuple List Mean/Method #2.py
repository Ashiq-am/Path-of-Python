# Python3 code to demonstrate working of
# Kth Index Tuple List Mean
# Using sum() + len() + generator expression
from statistics import mean

# initializing list
test_list = [('Gfg', 4), ('is', 18), ('best', 2), ('for', 5), ('geeks', 1)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# Kth Index Tuple List Mean
# Using sum() + len() + generator expression
res = sum(val[K] for val in test_list) / len(test_list)

# printing result
print("The computed mean : " + str(res))
