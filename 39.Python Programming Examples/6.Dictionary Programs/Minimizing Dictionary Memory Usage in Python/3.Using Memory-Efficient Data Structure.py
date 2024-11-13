import sys
from array import array

# Original dictionary
original_dict = {
	'name': 'John',
	'age': 25,
	'city': 'New York'
}

# Measure the size of the original dictionary
original_size = sys.getsizeof(original_dict)

# Convert dictionary to an array
optimized_dict = array('B', bytes(str(original_dict.items()), 'utf-8'))

# Measure the size of the optimized dictionary
optimized_size = sys.getsizeof(optimized_dict)

print(f"Original Dictionary Size: {original_size} bytes")
print(f"Optimized Dictionary Size (using array): {optimized_size} bytes")
