# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of students data with null values
# we can define null values with none
data = [[None, "sravan", "vignan"],
		["2", None, "vvit"],
		["3", "rohith", None],
		["4", "sridevi", "vignan"],
		["1", None, None],
		["5", "gnanesh", "iit"]]

# specify column names
columns = ['ID', 'NAME', 'college']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# show columns
print(dataframe.columns)

# display dataframe
dataframe.show()
