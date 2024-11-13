from pyspark.sql import SparkSession
import pandas as pd

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
], ["people", "City", "State"])
df2.show()

# Convert PySpark data frames to Pandas data frames
pdf1 = df1.toPandas()
pdf2 = df2.toPandas()

# Merge Pandas data frames using the merge method
pdf3 = pd.merge(pdf1, pdf2, how="outer", left_on="Name", right_on="people")

print(pdf3)
