# importing required modeules
import numpy as np
from scipy import stats as st

# creating a 2-D array using numpy package
arr = np.array([[1, 2, 3, 4, 5],
				[1, 2, 2, 2, 2],
				[4, 5, 7, 9, 4],
				[6, 7, 8, 9, 2],
				[2, 3, 4, 8, 6]])

# applying mode operation and printing the
# result
print(st.mode(arr))
