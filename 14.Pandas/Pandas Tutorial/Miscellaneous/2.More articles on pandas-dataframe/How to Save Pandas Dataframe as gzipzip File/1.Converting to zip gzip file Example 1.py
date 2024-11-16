# importing packages
import pandas as pd

# dictionary of data
dct = {'ID': {0: 23, 1: 43, 2: 12,

			3: 13, 4: 67},

	'Name': {0: 'Ajay', 1: 'Deep',

				2: 'Deepanshi', 3: 'Mira',

				4: 'Yash'},

	'Marks': {0: 89, 1: 97, 2: 45, 3: 78,

				4: 56},

	'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',

				4: 'E'}
	}

# forming dataframe and printing
data = pd.DataFrame(dct)
print(data)

# using to_pickle function to form file
# by default, compression type infers from the file extension in specified path.
# file will be created in the given path
data.to_pickle('file.zip')
