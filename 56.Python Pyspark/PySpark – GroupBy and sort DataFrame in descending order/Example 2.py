# import the required modules
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

# define the schema to be used
schema = ["Name","Number_of_Trials","Marks"]

# create the dataframe
df = spark.createDataFrame(data=simpleData, schema = schema)

# perform groupby operation on name table
# aggrigate marks and give it a new name
# sort in descending order by avg_marks
df.groupBy("Name") \
.agg(avg("Marks").alias("Avg_Marks")) \
.sort(desc("Avg_Marks")) \
.show()

# stop sparks session
spark.stop()
