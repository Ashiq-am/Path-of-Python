# Function returning a pair of values
def get_key_value_pair():
	return "key", "value"

# Ignoring the first element of the returned pair using a single underscore
_, value = get_key_value_pair()

# The first element is ignored, and only the second element is used
print("Value:", value)
