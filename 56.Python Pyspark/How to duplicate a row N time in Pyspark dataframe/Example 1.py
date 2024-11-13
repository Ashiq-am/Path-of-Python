# Importing PySpark and Pandas
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,expr

# Session Creation
Spark_Session = SparkSession.builder.appName(
	'Spark Session'
).getOrCreate()

# Accepting n from the user.
n = int(input('Enter n : '))

# Data filled in our DataFrame
rows = [['a',1,'@'],
		['b',3,'_'],
		['c',2,'!'],
		['d',6,'(']]

# Columns of our DataFrame
columns = ['X','Y','Z']

# DataFrame is created
df = Spark_Session.createDataFrame(rows,columns)

# Printing the DataFrane
df.show()

# Creating a new DataFrame with a
# expression using functions
new_df = df.withColumn(
"Y", expr("explode(array_repeat(Y,int(Y)))"))

# Printing the new DataFrame
new_df.show()
