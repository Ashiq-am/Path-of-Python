# Python3 code to demonstrate
# Concatenating Kth element in Tuple List
# using map() + itergetter() + join()
from operator import itemgetter

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# using map() + itergetter() + join() to get names
res = " ".join(list(map(itemgetter(K), test_list)))

# printing result
print("String with only nth tuple element (i.e names) concatenated : " + str(res))
