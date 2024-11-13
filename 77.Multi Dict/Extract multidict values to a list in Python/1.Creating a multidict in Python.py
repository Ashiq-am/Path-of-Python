# Import the 'multidict' library
import multidict

# create a multidict structure by
# passing the values to 'Multidict' class.
d = multidict.MultiDict([('a', 1), ('b', 2), ('b', 3),
						('c', 5), ('d', 4), ('c', 7)])

print(d)
