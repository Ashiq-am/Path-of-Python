# Using split() + loop

# initializing string
test_str = 'gfg_is_best_for_geeks'

# printing original string
print("The original string is : "
	+ str(test_str))

# initializing delim
delim = "_"

# splitting using split()
temp = test_str.split(delim)

res = dict()

# using loop to reform dictionary with splits
for idx, ele in enumerate(temp):
	res[idx] = ele

# printing result
print("Dictionary after splits ordering : "
	+ str(res))
