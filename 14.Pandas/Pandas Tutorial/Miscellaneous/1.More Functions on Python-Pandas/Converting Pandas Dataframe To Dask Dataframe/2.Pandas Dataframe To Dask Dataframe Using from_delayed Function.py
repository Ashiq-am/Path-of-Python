import pandas as pd
import dask
from dask import delayed
import dask.dataframe as dd

# Create a Pandas DataFrame
pandas_df = pd.DataFrame({
	'A': [1, 2, 3, 4],
	'B': [5, 6, 7, 8],
})

# Split the Pandas DataFrame into partitions
partitions = [delayed(pd.DataFrame)(part)
			for _, part in pandas_df.groupby(pandas_df.index % 2)]

# Create a Dask DataFrame using from_delayed
dask_df = dd.from_delayed(partitions)

# Display the result
print(dask_df.compute())
