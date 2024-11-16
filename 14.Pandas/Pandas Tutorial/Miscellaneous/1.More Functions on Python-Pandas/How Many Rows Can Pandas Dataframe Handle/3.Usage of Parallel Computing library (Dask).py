import pandas as pd
import dask.dataframe as dd

# Loading and processing data in chunks
chunk_size = 100000
chunks = []
for chunk in pd.read_csv('large_dataset.csv',
                         chunksize=chunk_size,engine="python"):
    chunks.append(chunk)

df_large = pd.concat(chunks)
df_large.head()

# Converting pandas DataFrame to Dask DataFrame
ddf = dd.from_pandas(df_large, npartitions=10)

# Perform groupby operation with Dask DataFrame
result = ddf.groupby('ProductId').sum().compute()
print(result)
