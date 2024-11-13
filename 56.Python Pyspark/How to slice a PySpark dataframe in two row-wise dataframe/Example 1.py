# Importing PySpark
import pyspark
from pyspark.sql import SparkSession

# Session Creation
Spark_Session = SparkSession.builder.appName(
	'Spark Session'
).getOrCreate()


# Data filled in our DataFrame
rows = [['Lee Chong Wei', 69, 'Malaysia'],
		['Lin Dan', 66, 'China'],
		['Srikanth Kidambi', 9, 'India'],
		['Kento Momota', 15, 'Japan']]

# Columns of our DataFrame
columns = ['Player', 'Titles', 'Country']

# DataFrame is created
df = Spark_Session.createDataFrame(rows, columns)

# Getting the slices
# The first slice has 3 rows
df1 = df.limit(3)

# Getting the second slice by removing df1
# from df
df2 = df.subtract(df1)

# Printing the first slice
df1.show()

# Printing the second slice.
df2.show()
