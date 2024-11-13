# Python3 code to demonstrate working of
# Extract top N Dictionaries by Key
# Using nlargest() + lambda
from heapq import nlargest

# initializing dictionary
test_dict = {6: 2, 8: 9, 3: 9, 6: 1, 10: 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing N
N = 4

res = []

# Using nlargest() to get maximum keys
for key, val in nlargest(N, test_dict.items(), key=lambda ele: ele[0]):
    res.append(key)

# printing result
print("Top N keys are: " + str(res))
