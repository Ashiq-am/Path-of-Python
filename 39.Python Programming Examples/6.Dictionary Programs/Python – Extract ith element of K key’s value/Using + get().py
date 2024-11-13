# Python3 code to demonstrate working of
# Extract ith element of K key's value
# Using get()

# initializing dictionary
test_dict = {'Gfg': [6, 7, 3, 1],
             'is': [9, 1, 4],
             'best': [10, 7, 4]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 'Gfg'

# initializing i
i = 2

# using get() to get the required value
temp = test_dict.get(K)
res = None
# checking for non empty dict and length constraints
if temp and len(temp) >= i:
    res = temp[i]

# printing result
print("The extracted value : " + str(res))
