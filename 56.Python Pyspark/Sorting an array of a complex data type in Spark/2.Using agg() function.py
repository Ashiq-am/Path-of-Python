# Python program to sort an array of a complex
# data type in Spark using agg() function

# Import the Pyspark library
from pyspark.sql import *
import pyspark
from pyspark.sql import SparkSession

# Create a Spark Session
spark=SparkSession.builder.getOrCreate()

# Create the Spark data frame
data_df = spark.createDataFrame([
Row(section='A', name='Ashish', sequence=1),
Row(section='B', name='Bharti', sequence=1),
Row(section='B', name='Charlie', sequence=2),
Row(section='A', name='Marie', sequence=2),
Row(section='C', name='Prabhakar', sequence=1),
Row(section='D', name='Shrey', sequence=1),
Row(section='C', name='Rose', sequence=2),
Row(section='B', name='Ishita', sequence=3),
Row(section='C', name='Samarth', sequence=3),
Row(section='A', name='Vinayak', sequence=4),
Row(section='A', name='Pranjal', sequence=3),
])

# Display the Spark data frame
views_df = data_df.select('section', 'name', 'sequence')

# Create a local temporary view
views_df.createOrReplaceTempView('views')

# Sort array of complex data type
views_df= (views_df
.groupBy('section')
.agg(
	array_sort(
	collect_list(struct('sequence', 'name'))
	).alias('sorted_names')
).select("section", col("sorted_names.name").alias("Sorted Names"))
).show(20, False)
