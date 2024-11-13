# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of students data
data = [["1", "Amit", "DU"],
		["2", "Mohit", "DU"],
		["3", "rohith", "BHU"],
		["4", "sridevi", "LPU"],
		["1", "sravan", "KLMP"],
		["5", "gnanesh", "IIT"]]

# specify column names
columns = ['student_ID', 'student_NAME', 'college']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# show dataframe
dataframe.show()
