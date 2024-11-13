# importing module
import pyspark

# importing sparksession
from pyspark.sql import SparkSession

# creating sparksession
# and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of students data with null values
# we can define null values with none
data = [[1, "sravan", "vignan"],
		[2, "ramya", "vvit"],
		[3, "rohith", "klu"],
		[4, "sridevi", "vignan"],
		[5, "gnanesh", "iit"]]

# specify column names
columns = ['ID', 'NAME', 'college']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

dataframe.show()
