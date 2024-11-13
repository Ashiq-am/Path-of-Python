import sys

# Original dictionary
original_dict = {
	'name': 'John',
	'age': 25,
	'city': 'New York'
}
original_size = sys.getsizeof(original_dict)

# Convert dictionary to a custom object
class MyObject:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

optimized_obj = MyObject(**original_dict)
optimized_size = sys.getsizeof(optimized_obj)

print(f"Original Dictionary Size: {original_size} bytes")
print(
	f"Optimized Dictionary Size (using custom object): {optimized_size} bytes")
