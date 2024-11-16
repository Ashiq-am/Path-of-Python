import numpy as np

# using genfromtxt()
arr = np.genfromtxt("sample_data.csv",
					delimiter=",", dtype=str)
display(arr)
