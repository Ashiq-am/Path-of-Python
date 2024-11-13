# Python3 code to demonstrate working of
# Merge Python key values to list
# Using list comprehension + dictionary comprehension

# Initialize list
test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
			{'it' : 5, 'is' : 7, 'best' : 8},
			{'CS' : 10}]

# Printing original list
print("The original list is : " + str(test_list))

# using list comprehension + dictionary comprehension
# Merge Python key values to list
res = {key: list({sub[key] for sub in test_list if key in sub})
	for key in {key for sub in test_list for key in sub}}

# printing result
print("The merged values encapsulated dictionary is : " + str(res))
