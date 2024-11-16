import numpy as np


# skipping first row
# converting file data to string
data = np.loadtxt("example2.txt", skiprows=1, dtype='str')
print(data)
