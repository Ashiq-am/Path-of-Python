# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [(1, "sravan"), (2, "ojsawi"), (3, "bobby")]

# specify column names
columns = ['ID1', 'NAME1']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# list of employee data
data = [(1, "sravan"), (2, "ojsawi"), (3, "bobby"),
		(4, "rohith"), (5, "gnanesh")]

# specify column names
columns = ['ID2', 'NAME2']

# creating a dataframe from the lists of data
dataframe1 = spark.createDataFrame(data, columns)

# join based on ID and name column
dataframe.join(dataframe1, (dataframe.ID1 == dataframe1.ID2)
			& (dataframe.NAME1 == dataframe1.NAME2)).show()
