# Import Pandas and Dask
import pandas as pd
import dask.dataframe as dd

# Create multiple Pandas DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [4, 5]})
df2 = pd.DataFrame({'A': [3, 4], 'B': [6, 7]})

# Convert to Dask DataFrame using concat
dask_df = dd.concat([dd.from_pandas(df1, npartitions=2), dd.from_pandas(df2, npartitions=2)])

# Display Results
print(dask_df.compute())
