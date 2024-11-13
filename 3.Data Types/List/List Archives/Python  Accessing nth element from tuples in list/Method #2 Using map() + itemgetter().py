# Python3 code to demonstrate
# get nth tuple element from list
# using map() + itergetter()
from operator import itemgetter

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# using map() + itergetter() to get names
res = list(map(itemgetter(1), test_list))

# printing result
print("List with only nth tuple element (i.e names) : " + str(res))
