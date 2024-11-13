# Python3 code to demonstrate working of
# Prefix tuple records
# Using filter() + lambda + generator expression + all()

# initializing list
test_list = [('Gfg', 'best', 'geeks'), ('Gfg', 'good'),
				('Gfg', 'best', 'CS'), ('Gfg', 'love')]

# printing original list
print("The original list is : " + str(test_list))

# initializing prefix tuple
pref_tup = ('Gfg', 'best')

# Prefix tuple records
# Using filter() + lambda + generator expression + all()
res = list(filter(lambda sub: all([sub[idx] == ele
	for idx, ele in enumerate(pref_tup)]), test_list))

# printing result
print("The filtered tuples : " + str(res))
