# Importing defaultdict from the collections module
from collections import defaultdict

# Defining the desired size of the dictionary
size = 5

# Creating a dictionary with zeros using a defaultdict
# The defaultdict uses int as the default factory, ensuring default values are set to zero
zero_dict = defaultdict(int, {i: 0 for i in range(size)})

# Printing the resulting dictionary
print( zero_dict)
