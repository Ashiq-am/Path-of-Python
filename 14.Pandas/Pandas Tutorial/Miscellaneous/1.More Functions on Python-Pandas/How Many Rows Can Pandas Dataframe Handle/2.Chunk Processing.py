import pandas as pd

# Loading and processing data in chunks
chunk_size = 100000
chunks = []
for chunk in pd.read_csv('large_dataset.csv',
                         chunksize=chunk_size,engine="python"):
    chunks.append(chunk)

df_large = pd.concat(chunks)
print(df_large.head())
