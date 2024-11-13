# Python3 code to demonstrate working of
# Column-wise elements in Dictionary value list
# Using generator expression + zip() + * operator

# initializing dictionary
test_dict = {'Gfg' : [3, 6, 7],
			'is' : [4, 2, 6],
			'best' :[9, 1, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values() gets all values at on
res = list(a for b in zip(*test_dict.values()) for a in b)

# printing result
print("The extracted values : " + str(res))
