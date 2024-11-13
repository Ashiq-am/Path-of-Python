# importing required module
import pyspark
from pyspark.sql import SparkSession

# creating sparksession and giving
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# demo data of college students
data = [["Mukul", 23, "BBA"],
		["Robin", 21, "BCA"],
		["Rohit", 24, "MBA"],
		["Suraj", 25, "MBA"],
		["Krish", 22, "BCA"]]

# giving column names of dataframe
columns = ["Name", "Age", "Course"]

# creating a dataframe
dataframe = spark.createDataFrame(data, columns)

# Rename dataframe
df = dataframe.withColumnRenamed(dataframe.columns[0],
								"Student Name")

# Original dataframe
print("Original Dataframe")
dataframe.show()

# Dataframe after rename column
print("Dataframe after rename 0 index column")
df.show()
