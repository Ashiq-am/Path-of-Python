set_obj = {11, 22, 33, 44, 55}

# print original set object
print("Original Set:", set_obj)

# sep is our separator character on joining elements
sep = ","

# It joins elements of set_obj by ',' and stores it in string named joined_str
joined_str = sep.join(str(s) for s in set_obj)

# print resultant joined string
print("Joined String:", joined_str)
