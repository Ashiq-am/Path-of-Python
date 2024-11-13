# Import required module
from pyspark import SparkContext

sc = SparkContext()

# Create a key-value pair RDD
kv_rdd = sc.parallelize([(1, 'a'),
						(2, 'b'),
						(3, 'c')])

# Use map() to convert the RDD to an
# RDD containing keys and values
value_rdd = kv_rdd.map(lambda x:x)

# Collect the keys and values and print them
values =[item for t in value_rdd.collect() for item in t]

print(values)
