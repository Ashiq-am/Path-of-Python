import numpy as np
# number of nan we want to add It will insert 3 nan vlaues to the data.....
n_b = 5

# creating dataset
data_b = np.random.randint(10, 100, size=(5, 5))

# converting the data to float as nan is also of type float
data_b = data_b*0.1

# choosing random indexes to put NaN
index_b = np.random.choice(data_b.size, n_b, replace=False)

# adding nan to the data.
data_b.ravel()[index_b] = np.nan
print(data_b)
