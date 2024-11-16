# Import Pandas and Dask
import pandas as pd
import dask.dataframe as dd

# Create Pandas DataFrame
pandas_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Convert to Dask DataFrame
dask_df = dd.from_pandas(pandas_df, npartitions=2)

# Display Results
print(dask_df.compute())
