# open the file as 'f'
with h5py.File('test.hdf5', 'r') as f:
    data = f['default']

    # get the minimum value
    print(min(data))

    # get the maximum value
    print(max(data))

    # get the values ranging from index 0 to 15
    print(data[:15])

