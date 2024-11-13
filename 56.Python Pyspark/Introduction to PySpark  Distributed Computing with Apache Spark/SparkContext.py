from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("Test")
# setMaster(local) - we are doing tasks on a single machine
sc = SparkContext(conf = conf)
