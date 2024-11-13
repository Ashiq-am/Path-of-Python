# import the modules
from pyspark.sql import SparkSession

# Create Spark session app name
# is GFG and master name is local
spark = SparkSession.builder.appName("GFG").master("local") .getOrCreate()

# dictionary list of college data
data = [{"Name": 'sravan kumar',
		"ID": 1,
		"Percentage": 94.29},
		{"Name": 'sravani',
		"ID": 2,
		"Percentage": 84.29},
		{"Name": 'kumar',
		"ID": 3,
		"Percentage": 94.29}
		]

# Create data frame from dictionary list
df = spark.createDataFrame(data)

# display
df.show()
