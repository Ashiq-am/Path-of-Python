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

#DataFrame is created
df = Spark_Session.createDataFrame(rows, columns)

# the first slice has 20% of the rows
# the second slice has 80% of the rows
# the data in both slices is selected randomly
df1, df2 = df.randomSplit([0.20, 0.80])

# Showing the first slice
df1.show()

# Showing the second slice
df2.show()
