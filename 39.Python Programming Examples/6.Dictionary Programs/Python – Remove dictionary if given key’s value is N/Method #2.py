# Python3 code to demonstrate working of
# Remove Dictionaries whose Key(K) is N
# Using filter() + lambda

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

# Using filter() to check for N value
res = list(filter(lambda x: x[K] != N, test_list))

# printing result
print("The extracted dictionaries : " + str(res))
