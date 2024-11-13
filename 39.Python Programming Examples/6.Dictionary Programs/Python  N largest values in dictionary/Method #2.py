# Python3 code to demonstrate working of
# N largest values in dictionary
# Using nlargest
from heapq import nlargest

# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6, 'for' : 7, 'geeks' : 3 }

# Initialize N
N = 3

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# N largest values in dictionary
# Using nlargest
res = nlargest(N, test_dict, key = test_dict.get)

# printing result
print("The top N value pairs are " + str(res))
