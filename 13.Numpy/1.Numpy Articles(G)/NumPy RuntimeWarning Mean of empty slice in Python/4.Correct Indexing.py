import numpy as np

single_element_array = np.array([42])

# Correcting indexing to prevent accessing elements beyond array bounds
mean_value = np.mean(single_element_array[:1])
print("Mean:", mean_value)
