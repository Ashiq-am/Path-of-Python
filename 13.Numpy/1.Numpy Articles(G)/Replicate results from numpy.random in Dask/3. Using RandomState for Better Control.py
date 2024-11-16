import numpy as np
import dask.array as da

# Create a RandomState for numpy
np_state = np.random.RandomState(42)

# Generate a random array using numpy's RandomState
np_array = np_state.rand(10)

# Create a RandomState for dask
dask_state = da.random.RandomState(42)

# Generate a random array using dask's RandomState
dask_array = dask_state.random_sample(10, chunks=5)

print("Numpy Array:", np_array)
print("Dask Array:", dask_array.compute())
