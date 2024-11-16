import numpy as np


# skipping last line in the file
Data = np.genfromtxt("example5.txt", dtype=str,
					encoding=None, skip_footer=1)
print(Data)
