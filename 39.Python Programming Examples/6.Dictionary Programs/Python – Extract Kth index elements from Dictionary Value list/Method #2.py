# Python3 code to demonstrate working of
# Extract Kth index elements from Dictionary Value list
# Using map() + itemgetter()
from operator import itemgetter

# initializing dictionary
test_dict = {"Gfg" : [4, 7, 5], "Best" : [8, 6, 7], "is" : [9, 3, 8]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 1

# map and itemgetter() extracting result
# list() used to convert result from map() to list format
res = list(map(itemgetter(K), test_dict.values()))

# printing result
print("The extracted values : " + str(res))
