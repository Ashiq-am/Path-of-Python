# Python3 code to demonstrate working of
# Prefix tuple records
# Using list comprehension + zip() + all()

# initializing list
test_list = [('Gfg', 'best', 'geeks'), ('Gfg', 'good'),
			('Gfg', 'best', 'CS'), ('Gfg', 'love')]

# printing original list
print("The original list is : " + str(test_list))

# initializing prefix tuple
pref_tup = ('Gfg', 'best')

# Prefix tuple records
# Using list comprehension + zip() + all()
res = [tup for tup in test_list if all(x == y for x, y in
									zip(tup, pref_tup))]

# printing result
print("The filtered tuples : " + str(res))
