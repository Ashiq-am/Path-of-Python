# importing required packages
from scipy import stats as st
import numpy as np

# creating an array using array() method
abc = np.array([1, 1, 2, 2, 2, 3, 4, 5])

# applying mode operation on array and
# printing result
print(st.mode(abc))
