# Python3 code to demonstrate working of
# Extract Kth index elements from Dictionary Value list
# Using list comprehension + values()

# initializing dictionary
test_dict = {"Gfg" : [4, 7, 5], "Best" : [8, 6, 7], "is" : [9, 3, 8]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 1

# one liner, values() getting all value according to keys
res = [sub[K] for sub in test_dict.values()]

# printing result
print("The extracted values : " + str(res))
