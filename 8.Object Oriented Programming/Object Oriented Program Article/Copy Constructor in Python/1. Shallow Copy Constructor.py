import copy

class ShallowCopyExample:
	def __init__(self, data):
		self.data = data

	def __str__(self):
		return f"Original Object: {self.data}"

	def shallow_copy(self):
		return copy.copy(self)

# Example usage
original_object = ShallowCopyExample([1, 2, 3])
copy_object = original_object.shallow_copy()

print(original_object)
print(copy_object)

# Modify the copied object
copy_object.data.append(4)

# Changes reflected in the original object
print(original_object)
print(copy_object)
