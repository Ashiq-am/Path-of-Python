# Python3 code to demonstrate working of
# Replace duplicates in tuple
# using set() + list comprehension

# initialize tuple
test_tup = (1, 1, 4, 4, 4, 5, 5, 6, 7, 7)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Replace duplicates in tuple
# using set() + list comprehension
temp = set()
res = tuple(ele if ele not in temp and not temp.add(ele)
				else 'gfg' for ele in test_tup)

# printing result
print("Tuple after replacing values : " + str(res))
