# Import needed package
from collections import defaultdict

# Define our data
list_data = [1, 2, 3, 4, 2, 4, 1, 2]


# Helper Function
def list_to_dict(input_list):
	"""Convert list to DefaultDict"""
	d = defaultdict(int)
	for i in input_list:
		d[i] += 1
	return d


# Output
print(ltd(list_data))
