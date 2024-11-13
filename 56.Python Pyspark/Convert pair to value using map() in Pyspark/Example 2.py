# Import required module
from pyspark import SparkContext

sc = SparkContext()

# Create a key-value pair RDD
kv_rdd = sc.parallelize([(1, 'a'),
						(2, 'b'),
						(3, 'c')])

# Use map() to convert the RDD to an
# RDD containing keys and values
keys_rdd = kv_rdd.map(lambda x:x[0])

# Collect the keys and values and print them
keys = keys_rdd.collect()

print(keys)
