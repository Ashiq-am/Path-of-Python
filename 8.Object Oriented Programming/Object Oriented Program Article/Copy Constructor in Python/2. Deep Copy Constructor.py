import copy

class DeepCopyExample:
	def __init__(self, data):
		self.data = data

	def __str__(self):
		return f"Original Object: {self.data}"

	def deep_copy(self):
		return copy.deepcopy(self)

# Example usage
original_object = DeepCopyExample([1, [2, 3], 4])
copy_object = original_object.deep_copy()

print(original_object)
print(copy_object)

# Modify the copied object
copy_object.data[1].append(99)

# Changes not reflected in the original object
print(original_object)
print(copy_object)
