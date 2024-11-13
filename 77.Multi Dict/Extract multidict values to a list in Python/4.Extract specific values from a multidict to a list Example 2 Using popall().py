# Import the package Multidict
import multidict

# Create multidict structure using
# the Multidict class
d = multidict.MultiDict([('a', 1), ('b', 2),
						('b', 3), ('c', 5),
						('d', 4), ('c', 7)])

# Use the popall(k) method to
# fetch a list of all
# values associated with key 'c'
pop_list_of_key_c = d.popall('c')

# print the popped values
print("Pop out values of key C:", pop_list_of_key_c)

# After popping the key values,
# print the Multidict structure
print("Multidict after popping key C:", d)
