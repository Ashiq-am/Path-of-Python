import numpy as np

a = np.array([(13.0, 1.0, -47.0), (12.0, 3.0, -47.0), (15.0, 2.0, -44.0)])

# adding nan values to the row
np.insert(a, 2, np.nan, axis=0)

# adding nan values to the row
np.insert(a, 2, np.nan, axis=1)
