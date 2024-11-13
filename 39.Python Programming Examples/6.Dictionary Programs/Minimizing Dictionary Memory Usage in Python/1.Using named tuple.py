import sys
from collections import namedtuple

original_dict = {
	'name': 'John',
	'age': 25,
	'city': 'New York'
}

original_size = sys.getsizeof(original_dict)

# Convert dictionary to a namedtuple
MyTuple = namedtuple('MyTuple', original_dict.keys())
optimized_dict = MyTuple(**original_dict)

# Measure the size of the optimized dictionary
optimized_size = sys.getsizeof(optimized_dict)

print(f"Original Dictionary Size: {original_size} bytes")
print(f"Optimized Dictionary Size (using namedtuple): {optimized_size} bytes")
