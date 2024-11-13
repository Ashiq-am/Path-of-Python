# Importing necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql import functions as f

# Create a spark session
spark = SparkSession.builder.appName(
'pyspark - example join').getOrCreate()

# Define data in a dataframe
dataframe = [
	("Sam", "Software Engineer", "IND", 10000),
	("Raj", "Data Scientist", "US", 41000),
	("Jonas", "Sales Person", "UK", 230000),
	("Peter", "CTO", "Ireland", 50000),
	("Hola", "Data Analyst", "Australia", 111000),
	("Ram", "CEO", "Iran", 300000),
	("Lekhana", "Advertising", "UK", 250000),
	("Thanos", "Marketing", "UIND", 114000),
	("Nick", "Data Engineer", "Ireland", 680000),
	("Wade", "Data Engineer", "IND", 70000)
]

# Column names of dataframe
columns = ["Name", "Job", "Country", "salary"]

# Create the spark dataframe
df = spark.createDataFrame(data=dataframe, schema=columns)

# Printing the dataframe
df.show()
