# Python3 code to demonstrate working of
# Key Value list pairings in Dictionary
# Using list comprehension

# initializing dictionary
test_dict = {'gfg' : [7, 8],
			'best' : [10, 11, 7]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Key Value list pairings in Dictionary
# Using list comprehension
res = [{'gfg': i, 'best': j} for i in test_dict['gfg']
						for j in test_dict['best']]

# printing result
print("All key value paired List : " + str(res))
