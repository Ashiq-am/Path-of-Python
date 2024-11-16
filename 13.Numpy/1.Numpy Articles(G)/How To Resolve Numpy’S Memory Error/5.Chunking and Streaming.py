import numpy as np
import pandas as pd

# Load large dataset in chunks
chunk_size = 10000
for chunk in pd.read_csv('large_dataset.csv', chunksize=chunk_size):
	process_chunk(chunk.to_numpy())
