# importing required module
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of Employees data
data = [
	(121, ("Mukul", "Kumar"), 25000, 25),
	(122, ("Arjun", "Singh"), 28000, 23),
	(123, ("Rohan", "Verma"), 30000, 27),
	(124, ("Manoj", "Singh"), 30000, 22),
	(125, ("Robin", "Kumar"), 28000, 23)
]

# specify column names
columns = ['Employee ID', 'Name', 'Salary', 'Age']

# creating a dataframe from the lists of data
df = spark.createDataFrame(data, columns)
print(" Original data ")
df.show()

# filter dataframe based on single condition
df2 = df.where(df.Salary == 28000)
print(" After filter dataframe based on single condition ")
df2.show()
