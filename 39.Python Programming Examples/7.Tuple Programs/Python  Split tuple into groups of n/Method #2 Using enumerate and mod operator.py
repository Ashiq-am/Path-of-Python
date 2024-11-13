# Python code to demonstrate
# how to split tuple
# into the group of k-tuples

# initialising tuple
ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,
			67, 45, 1, 1, 43, 65, 9, 10)

# printing initial tuple
print ("initial list", str(ini_tuple))

# code to group
# tuple into size 4 tuples
res = tuple(ini_tuple[n:n + 4] for n, i in enumerate(ini_tuple)
												if n % 4 == 0)

# printing result
print ("resultant tuples", str(res))
