# importing module
from pyspark.rdd import RDD
from pyspark.sql import DataFrame
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# import singledispatch
from functools import singledispatch

# import spark context
from pyspark import SparkContext

# createan object for spark
# context with local and name is GFG
sc = SparkContext("local", "GFG")

# creating sparksession
# and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# import DataFrame

# import RDD

# creating the spark session
spark = SparkSession.builder.getOrCreate()

# create a function to dispatch our function
@singledispatch
def check(x):
	pass

# this function is for returning
# an RDD if the given input is RDD
@check.register(RDD)
def _(arg):
	return "RDD"

# this function is for returning
# an RDD if the given input is DataFrame
@check.register(DataFrame)
def _(arg):
	return "DataFrame"

# create an pyspark dataframe
# and check whether it is RDD or not
print(check(sc.parallelize([("1", "sravan", "vignan", 67, 89)])))
