# Import required module
from pyspark import SparkContext

sc = SparkContext()

# Create a key-value pair RDD
kv_rdd = sc.parallelize([(1, 'a'),
						(2, 'b'),
						(3, 'c')])

# Use map() to convert the RDD to an
# RDD containing only the values
value_rdd = kv_rdd.map(lambda x: x[1])

# Collect the values and print them
values = value_rdd.collect()

# Print values
print(values)
