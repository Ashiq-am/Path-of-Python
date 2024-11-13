with h5py.File('test_read.hdf5', 'r') as f:
	d1 = f['array_1']
	d2 = f['array_2']

	data = d2[d1[:]>1]
