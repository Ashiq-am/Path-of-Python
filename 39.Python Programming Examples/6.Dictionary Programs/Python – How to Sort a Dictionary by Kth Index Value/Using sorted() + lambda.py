# Python3 code to demonstrate working of
# Sort Dictionary by Kth Index Value
# Using sorted() + lambda

# initializing dictionary
test_dict = {'gfg' : [5, 6, 7],
			'is' : [1, 4, 7],
			'best' : [8, 3, 1]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 1

# Sort Dictionary by Kth Index Value
# Using sorted() + lambda
res = sorted(test_dict.items(), key = lambda key: key[1][K])

# printing result
print("The sorted dictionary : " + str(res))
