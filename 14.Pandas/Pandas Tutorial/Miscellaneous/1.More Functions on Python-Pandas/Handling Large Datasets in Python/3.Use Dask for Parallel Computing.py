import dask.dataframe as dd
import pandas as pd

# Create sample DataFrame
data = {'A': range(10000),
        'B': range(10000)}

df = pd.DataFrame(data)

# Load data using Dask
ddf = dd.from_pandas(df, npartitions=4)

# Perform parallelized operations
result = ddf.groupby('A').mean().compute()
print(result)
