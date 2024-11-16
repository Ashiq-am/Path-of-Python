# storing data in hdf5 file format
storedata = pd.HDFStore('college_data.hdf5')

# data
storedata.put('data_01', ser)

# mentioning scale and offset
metadata = {'scale': 0.1, 'offset': 15}

storedata.get_storer('data_01').attrs.metadata = metadata

# storing close
storedata.close()

# getting attributes
with pd.HDFStore('college_data.hdf5') as storedata:
	data = storedata['data_01']
	metadata = storedata.get_storer('data_01').attrs.metadata

# display data
print('\nData:\n', data)

# display stored data
print('\nStored Data:\n', storedata)

# display Metadata
print('\nMetadata:\n', metadata)
