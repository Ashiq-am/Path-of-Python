"""Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple.
Slicing can also be done to lists and arrays.
Indexing in a list results to fetching a single element whereas Slicing allows to fetch a set of elements.
Note- Negative Increment values can also be used to reverse the sequence of Tuples"""



# Slicing of a Tuple

# Slicing of a Tuple
# with Numbers
Tuple1 = tuple('GEEKSFORGEEKS')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[4:9])
