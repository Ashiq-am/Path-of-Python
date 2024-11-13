# Need to import to use date time
from datetime import datetime, date

# need to import for working with pandas
import pandas as pd

# need to import to use pyspark
from pyspark.sql import Row

# need to import for session creation
from pyspark.sql import SparkSession

# creating the session
spark = SparkSession.builder.getOrCreate()

## PySpark DataFrame from a pandas DataFrame
pandas_df = pd.DataFrame({
	'a': [1, 2, 3],

	'b': [4., 8., 5.],

	'c': ['GFG1', 'GFG2', 'GFG3'],

	'd': [date(2000, 8, 1), date(2000, 6, 2),
		date(2000, 5, 3)],

	'e': [datetime(2000, 8, 1, 12, 0),
		datetime(2000, 6, 2, 12, 0),
		datetime(2000, 5, 3, 12, 0)]
})

df = spark.createDataFrame(pandas_df)
df

# show table
df.show()

# show schema
df.printSchema()
