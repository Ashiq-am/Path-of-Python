# importing module
import pyspark

# importing sparksession from pyspark.sql
# module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of students data
data = [["1", "sravan", "vignan", 95],
		["2", "ojaswi", "vvit", 78],
		["3", "rohith", "vvit", 89],
		["2", "ojaswi", "vvit", 100],
		["4", "sridevi", "vignan", 88],
		["1", "sravan", "vignan", 78],
		["4", "sridevi", "vignan", 90],
		["5", "gnanesh", "iit", 67]]

# specify column names
columns = ['student ID', 'student NAME',
		'college', 'subject marks']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

print("the data is ")
dataframe.show()
