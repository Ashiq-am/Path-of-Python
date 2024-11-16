# import packages
from pandas.api.types import is_file_like
import numpy as np

# checking if it's a file like object
print(is_file_like(np.array([4, 8, 2, 7])))
