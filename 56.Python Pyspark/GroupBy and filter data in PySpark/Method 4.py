# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

#import functions
from pyspark.sql import functions as f

# import window module
from pyspark.sql import Window

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of student data
data = [["1", "sravan", "IT", 45000],
		["2", "ojaswi", "CS", 85000],
		["3", "rohith", "CS", 41000],
		["4", "sridevi", "IT", 56000],
		["5", "bobby", "ECE", 45000],
		["6", "gayatri", "ECE", 49000],
		["7", "gnanesh", "CS", 45000],
		["8", "bhanu", "Mech", 21000]
		]

# specify column names
columns = ['ID', 'NAME', 'DEPT', 'FEE']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)


# display
dataframe.join(dataframe.groupBy('DEPT').agg(
	f.max('FEE').alias('FEE')), on='FEE',
			how='leftsemi').show()
