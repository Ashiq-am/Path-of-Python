# Using dictionary comprehesion + split() + enumerate()

# initializing string
test_str = 'gfg_is_best_for_geeks'

# printing original string
print("The original string is : "
	+ str(test_str))

# initializing delim
delim = "_"

# using one liner to rearrange dictionary
res = {idx: ele for idx, ele in
	enumerate(test_str.split(delim))}

# printing result
print("Dictionary after splits ordering : "
	+ str(res))
