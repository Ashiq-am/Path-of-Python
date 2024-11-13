# Python3 code to demonstrate working of
# Smallest K values in Dictionary
# Using nsmallest
from heapq import nsmallest

# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6, 'for' : 7, 'geeks' : 3 }

# Initialize K
K = 2

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Smallest K values in Dictionary
# Using nsmallest
res = nsmallest(K, test_dict, key = test_dict.get)

# printing result
print("The minimum K value pairs are " + str(res))
