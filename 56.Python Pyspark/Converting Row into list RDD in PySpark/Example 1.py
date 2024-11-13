# import Row and SparkSession
from pyspark.sql import SparkSession, Row

# create sparksession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# create student data with Row function
data = [Row(name="sravan kumar",
			subjects=["Java", "python", "C++"],
			state="AP"),

		Row(name="Ojaswi",
			lang=["Spark", "Java", "C++"],
			state="Telangana"),

		Row(name="rohith",
			subjects=["DS", "PHP", ".net"],
			state="AP"),

		Row(name="bobby",
			lang=["Python", "C", "sql"],
			state="Delhi"),

		Row(name="rohith",
			lang=["CSharp", "VB"],
			state="Telangana")]
rdd = spark.sparkContext.parallelize(data)

# display actual rdd
rdd.collect()
