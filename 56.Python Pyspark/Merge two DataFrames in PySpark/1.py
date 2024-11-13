from functools import reduce # For Python 3.x
from pyspark.sql import DataFrame

def unionAll(*dfs):
	return reduce(DataFrame.unionAll, dfs)

unionAll(td2, td3, td4, td5, td6, td7, td8, td9, td10)
