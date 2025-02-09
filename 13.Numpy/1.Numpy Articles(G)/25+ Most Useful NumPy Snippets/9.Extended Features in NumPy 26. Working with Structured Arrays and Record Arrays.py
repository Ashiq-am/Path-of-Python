# Defining a structured data type
dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

# Creating a structured array
structured_array = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=dtype)
print("Structured Array:\n", structured_array)

# Accessing fields in structured arrays
print("Names:", structured_array['name'])
print("Ages:", structured_array['age'])