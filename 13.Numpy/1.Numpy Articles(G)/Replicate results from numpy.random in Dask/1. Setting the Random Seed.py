import numpy as np
import dask.array as da

# Set the seed for numpy's random number generator
np.random.seed(42)

# Generate a random array using numpy
np_array = np.random.random((5, 5))

# Set the seed for dask's random number generator
da.random.seed(42)

# Generate a random array using dask
dask_array = da.random.random((5, 5), chunks=(5, 5))

print("Numpy Array:", np_array)
print("Dask Array:", dask_array.compute())
