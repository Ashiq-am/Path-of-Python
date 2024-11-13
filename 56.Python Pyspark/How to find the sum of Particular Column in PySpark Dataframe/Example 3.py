# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of students data
data = [["1", "sravan", "vignan", 67, 89],
		["2", "ojaswi", "vvit", 78, 89],
		["3", "rohith", "vvit", 100, 80],
		["4", "sridevi", "vignan", 78, 80],
		["1", "sravan", "vignan", 89, 98],
		["5", "gnanesh", "iit", 94, 98]]

# specify column names
columns = ['student ID', 'student NAME', 'college',
		'subject 1', 'subject 2']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)


# find sum of multiple column
dataframe.agg({'subject 1': 'sum', 'student ID': 'sum',
			'subject 2': 'sum'}).show()
