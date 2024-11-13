# import pyspark along with sparksession
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# read the dataset
df = spark.read.format('csv').option
('header', 'true').load('gfg.csv')

# to show the content of dataset
df.show()
