import dask
import dask.dataframe as dd
import pandas as pd
from dask.delayed import delayed
import time


# Time variable for finding the
# difference
t1 = time.time()


parts = dask.delayed(pd.read_excel)('excel.xls',
									sheet_name=0)
df = dd.from_delayed(parts)

print(df.head())

t2 = time.time()
print("\nTime taken by Dask:")
print(t2-t1)
