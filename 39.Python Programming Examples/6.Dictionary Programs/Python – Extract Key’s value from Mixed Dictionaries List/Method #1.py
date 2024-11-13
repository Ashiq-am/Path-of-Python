# Python3 code to demonstrate working of
# Extract Key's value from Mixed Dictionaries List
# Using list comprehension

# initializing list
test_list = [{"Gfg" : 3, "b" : 7},
			{"is" : 5, 'a' : 10},
			{"Best" : 9, 'c' : 11}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'Best'

# list comprehension to get key's value
# using in operator to check if key is present in dictionary
res = [sub[K] for sub in test_list if K in sub][0]

# printing result
print("The extracted value : " + str(res))
