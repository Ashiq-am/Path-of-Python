import numpy as np

# Create a structured array with specified dtype
structured_array = np.array([('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4)],
							dtype=[('keys', 'U1'), ('data', '<i8')])
print("Structured Array:")
print(structured_array)
print("\nKeys Field:")
print(structured_array['keys'])
print("\nData Field:")
print(structured_array['data'])
