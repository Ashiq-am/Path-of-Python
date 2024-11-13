# importing pyspark
from pyspark.sql.window import Window
import pyspark

# importing sparksessio
from pyspark.sql import SparkSession

# creating a sparksession object
# and providing appName
spark = SparkSession.builder.appName("pyspark_window").getOrCreate()

# sample data for dataframe
sampleData = (("Ram", 28, "Sales", 3000),
			("Meena", 33, "Sales", 4600),
			("Robin", 40, "Sales", 4100),
			("Kunal", 25, "Finance", 3000),
			("Ram", 28, "Sales", 3000),
			("Srishti", 46, "Management", 3300),
			("Jeny", 26, "Finance", 3900),
			("Hitesh", 30, "Marketing", 3000),
			("Kailash", 29, "Marketing", 2000),
			("Sharad", 39, "Sales", 4100)
			)

# column names for dataframe
columns = ["Employee_Name", "Age",
		"Department", "Salary"]

# creating the dataframe df
df = spark.createDataFrame(data=sampleData,
						schema=columns)

# importing Window from pyspark.sql.window

# creating a window
# partition of dataframe
windowPartition = Window.partitionBy("Department").orderBy("Age")

# print schema
df.printSchema()

# show df
df.show()
