# import pyspark along with sparksession
import pyspark
from pyspark.sql import SparkSession

# to get an existing sparksession
spark = SparkSession.builder.getOrCreate()

# read the dataset
df = spark.read.format('csv').option('header',
						'true').load('gfg.csv')
split1, split2 = df.randomSplit([0.5, 0.5], seed=13)

# count of rows in original data frame
print("original: ", df.count())

# count of rows in splitted data frames
print("split1: ", split1.count())
print("split2: ", split2.count())
