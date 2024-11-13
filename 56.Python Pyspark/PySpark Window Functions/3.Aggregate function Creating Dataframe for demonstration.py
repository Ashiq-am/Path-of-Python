# importing pyspark
import pyspark

# importing sparksessio
from pyspark.sql import SparkSession

# creating a sparksession
# object and providing appName
spark = SparkSession.builder.appName("pyspark_window").getOrCreate()

# sample data for dataframe
sampleData = (("Ram", "Sales", 3000),
			("Meena", "Sales", 4600),
			("Robin", "Sales", 4100),
			("Kunal", "Finance", 3000),
			("Ram", "Sales", 3000),
			("Srishti", "Management", 3300),
			("Jeny", "Finance", 3900),
			("Hitesh", "Marketing", 3000),
			("Kailash", "Marketing", 2000),
			("Sharad", "Sales", 4100)
			)

# column names for dataframe
columns = ["Employee_Name", "Department", "Salary"]

# creating the dataframe df
df3 = spark.createDataFrame(data=sampleData,
							schema=columns)

# print schema
df3.printSchema()

# show df
df3.show()
