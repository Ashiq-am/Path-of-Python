import numpy as np
import h5py


arr1 = np.random.randn(10000)
arr2 = np.random.randn(10000)

with h5py.File('test_read.hdf5', 'w') as f:
	f.create_dataset('array_1', data = arr1)
	f.create_dataset('array_2', data = arr2)
