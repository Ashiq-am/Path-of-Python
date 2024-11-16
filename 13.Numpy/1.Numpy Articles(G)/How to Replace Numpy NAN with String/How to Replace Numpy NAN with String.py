import numpy as np

# Creating a NumPy array with NaN values
data1 = np.array([1.0, 2.0, np.nan, 4.0, np.nan])

print("Original Array:")
print(data1)

# Replacing NaN with a default string, e.g., 'Not Available'
data1_with_default_string = np.where(np.isnan(data1),
									'Not Available', data1)

print("\nArray with NaN replaced by 'Not Available':")
print(data1_with_default_string)
