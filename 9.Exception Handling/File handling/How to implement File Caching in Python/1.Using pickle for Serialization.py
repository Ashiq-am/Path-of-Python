import pickle

# dictionary to store cached file content
file_cache = {}

# function to read file content using pickle and implement caching

def read_file_pickle(file_path):
	# check if file content is already in cache
	if file_path not in file_cache:
		# read file using pickle and store content in cache
		with open(file_path, 'rb') as file:
			file_content = pickle.load(file)
			file_cache[file_path] = file_content
	# return the cached file content
	return file_cache[file_path]


# data to be pickled and cached
data = {'website': 'geeksforgeeks'}

# write data to file using pickle
with open('output.pkl', 'wb') as file:
	pickle.dump(data, file)

# read and print cached data from file
result = read_file_pickle('output.pkl')
print(result)
