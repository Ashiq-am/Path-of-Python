# importing the numpy library as np
import numpy as np

# Create a numpy array
# Notice we have not set the dtype of the object
# this will lead to the length problem
country = np.array(['USA', 'Japan', 'UK', '', 'India', 'China'])

# Print the array
print(country)
