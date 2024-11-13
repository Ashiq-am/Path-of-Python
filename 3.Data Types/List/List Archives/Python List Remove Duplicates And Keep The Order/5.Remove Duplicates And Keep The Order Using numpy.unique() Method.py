import numpy as np

original_list = [1, 2, 3, 4, 2, 1, 5, 6, 4]
print("Original List:", original_list)

unique_list, indices = np.unique(original_list, return_index=True)
print("Update List:", unique_list)
