def join_elements(set_obj, sep=','):
	joined_str = ''
	i = 0
	for el in set_obj:
		joined_str += el
		if i < len(set_obj) - 1:
			joined_str += sep
		i += 1
	return joined_str


set_obj = {'Java', 'Python', 'Scala', 'Rust', 'Lua'}

# print original set object
print("Original Set:", set_obj)

# sep is our separator character on joining elements
sep = "-"

# It joins elements of set_obj by `sep` and stores it in string named joined_str
joined_str = join_elements(set_obj, '-')

# print resultant joined string
print("Joined String:", joined_str)
