# importing required module
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of Employees data
data = [
	(121, "Mukul", 22000, 23),
	(122, "Arjun", 23000, 22),
	(123, "Rohan", 24000, 23),
	(124, "Manoj", 25000, 22),
	(125, "Robin", 26000, 23)
]

# specify column names
columns = ['Employee ID', 'Name', 'Salary', 'Age']

# creating a dataframe from the lists of data
df = spark.createDataFrame(data, columns)
print("Original Dataframe")
df.show()

# where() method with SQL Expression
df2 = df.where("Age == 22")
print(" After filter dataframe")
df2.show()
