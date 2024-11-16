import numpy as np
def process(chunk):
    print("Processing chunk:", chunk)

data = np.zeros((10000, 10000))
chunk_size = 100
for start in range(0, data.shape[0], chunk_size): # Iterate over the data in chunks and call the process function
    process(data[start : start + chunk_size])
