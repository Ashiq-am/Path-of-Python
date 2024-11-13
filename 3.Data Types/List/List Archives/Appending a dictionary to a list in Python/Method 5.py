# import numpy library
import numpy as np

# define a list
subjects = ["PHP", "Java", "SQL"]

# iterating the elements in
# list to create an numpy array
data = np.array([{'GFG': i} for i in subjects])

# append to the numpy array to list
final = np.append(res_array, {'GFG': "ML/DL"}).tolist()

# Printing the appended data
print(final)
