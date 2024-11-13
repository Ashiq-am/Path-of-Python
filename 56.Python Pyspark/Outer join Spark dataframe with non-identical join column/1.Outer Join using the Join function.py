from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder.appName("OuterJoin").getOrCreate()

# Create Dataframe 1

df1 = spark.createDataFrame([
	("Alice", 22, "Female"),
	("Bob", 35, "Male"),
	("Jack", 28, "Male"),
	("Jill", 30, "Female")
], ["Name", "Age", "Gender"])

df1.show()
# Create Dataframe 2

df2 = spark.createDataFrame([
	("Alice", "Chicago", "IL"),
	("Bob", "Boston", "MA"),
	("Charlie", "Houston", "TX"),
	("David", "Austin", "TX")
], ["Name", "City", "State"])
df2.show()

# Outer Join operation
# df3 = df1.join(df2, "Name", how='outer')
df3 = df1.join(df2, df1.Name == df2.Name, how='outer')

df3.show()
