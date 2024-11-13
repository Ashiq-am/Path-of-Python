# Python3 code to demonstrate working of
# Remove Dictionaries whose Key(K) is N
# Using list comprehension

# initializing list
test_list = [{"Gfg" : 3, "is" : 7, "Best" : 8},
			{"Gfg" : 9, "is" : 2, "Best" : 9},
			{"Gfg" : 5, "is" : 4, "Best" : 10},
			{"Gfg" : 3, "is" : 6, "Best" : 8}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = "Gfg"

# initializing N
N = 5

# returning only dictionaries with "Gfg" key not 5
res = [sub for sub in test_list if sub[K] != N]

# printing result
print("The extracted dictionaries : " + str(res))
