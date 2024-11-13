# Import the Multidict library
import multidict

# Declare a Multidict structure
# using the Multidict class
d = multidict.MultiDict([('a', 1), ('b', 2),
						('b', 3), ('c', 5),
						('d', 4), ('c', 7)])

# Fetch values for key 'b' in a
# list using getall(k) method
values_for_keyB_list = d.getall('b')

# Print the list of values
print("Key B values:", values_for_keyB_list)

# Fetch values for key 'c' in a
# list using getall(k) method
values_for_keyC_list = d.getall('c')

# Print the list of values
print("Key C values:", values_for_keyC_list)
