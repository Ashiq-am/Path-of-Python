import numpy as np

# Open the file in binary mode
with open('myfile.bin', 'rb') as f:
	# Read the data into a NumPy array
	array = np.fromfile(f, dtype=np.uint8) # Change dtype according to your data
