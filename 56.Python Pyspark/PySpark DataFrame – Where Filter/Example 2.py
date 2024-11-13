# importing required module
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of Employees data
data = [
	(121, ("Mukul", "Kumar"), 22000, 23),
	(122, ("Arjun", "Singh"), 23000, 22),
	(123, ("Rohan", "Verma"), 24000, 23),
	(124, ("Manoj", "Singh"), 25000, 22),
	(125, ("Robin", "Kumar"), 26000, 23)
]

# specify column names
columns = ['Employee ID', 'Name', 'Salary', 'Age']

# creating a dataframe from the lists of data
df = spark.createDataFrame(data, columns)
print(" Original data ")
df.show()

# filter dataframe based on multiple conditions
df2 = df.where((df.Salary > 22000) & (df.Age == 22))
print(" After filter dataframe based on multiple conditions ")
df2.show()
