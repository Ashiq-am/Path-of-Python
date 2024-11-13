# Python3 code to demonstrate working of
# Convert Tuple value list to List of tuples
# Using list comprehension + * operator + items()

# initializing dictionary
test_dict = {'Gfg' : [(5, 6, 7), (1, 3), (6, )],
			'is' : [(5, 5, 2, 2, 6)],
			'best' :[(7, ), (9, 16)]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# list comprehension encapsulates whole logic
# into one line
res = [(key, *ele) for key, sub in test_dict.items() for ele in sub]

# printing result
print("The converted tuple list : " + str(res))
