import numpy as np
import dask.array as da

# Define the seed
seed = 123

# Set the seed for numpy
np.random.seed(seed)

# Generate a random array using numpy
np_array = np.random.rand(10)

# Set the seed for dask
da.random.seed(seed)

# Generate a random array using dask
dask_array = da.random.random(10, chunks=5)

print("Numpy Array:", np_array)
print("Dask Array:", dask_array.compute())
