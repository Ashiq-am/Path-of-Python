# import required modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, desc

# Start spark session
spark = SparkSession.builder.appName("Student_Info").getOrCreate()

# sample dataset
simpleData = [("Pulkit","trial_1",32),
	("Ritika","trial_1",42),
	("Pulkit","trial_2",45),
	("Ritika","trial_2",50),
	("Ritika","trial_3",62),
	("Pulkit","trial_3",55),
	("Ritika","trial_4",75),
	("Pulkit","trial_4",70)
]

# define the schema
schema = ["Name","Number_of_Trials","Marks"]

# create a dataframe
df = spark.createDataFrame(data=simpleData, schema = schema)

df.groupBy("Name")\
	.agg(avg("Marks").alias("Avg_Marks"))\
	.orderBy("Avg_Marks", ascending=False)\
	.show()

# stop sparks session
spark.stop()
