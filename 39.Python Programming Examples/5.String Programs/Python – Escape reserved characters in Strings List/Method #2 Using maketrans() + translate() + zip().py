# Python3 code to demonstrate working of
# Escape reserved characters in Strings List
# Using maketrans() + translate() + zip()

# initializing list
test_list = ["Gf-g", "is*", "be)s(t"]

# printing string
print("The original list : " + str(test_list))

# reserved_chars
reserved_chars = '''?&|!{}[]()^~*:\\"'+-'''

# the escaping logic
mapper = ['\\' + ele for ele in reserved_chars]
result_mapping = str.maketrans(dict(zip(reserved_chars, mapper)))

# reforming result
res = [sub.translate(result_mapping) for sub in test_list]

# printing results
print("The resultant escaped String : " + str(res))
