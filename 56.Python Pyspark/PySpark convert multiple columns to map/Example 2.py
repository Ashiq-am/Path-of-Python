# Pyspark convert multiple columns to map

# Import the libraries SparkSession, col, lit, create_map
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit,create_map

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Define the data set
emp = [(1,"Smith",-1,"2018","10","M",3000),
	(2,"Rose",1,"2010","20","M",4000),
	(3,"Williams",1,"2010","10","M",1000),
	(4,"Jones",2,"2005","10","F",2000),
	(5,"Brown",2,"2010","40","F",4000),
	(6,"Brown",2,"2010","50","M",2000)]

# Define the schema of the data set
empColumns = ["emp_id","name","superior_emp_id",
			"year_joined", "emp_dept_id",
			"gender","salary"]

# Create the data frame through data set and schema
empDF = spark_session.createDataFrame(data=emp,
						schema = empColumns)

# Convert name, superior_emp_id, year_joined, emp_dept_id,
# gender, and salary columns to map
empDF = empDF.withColumn("employee_details",
		create_map(lit("name"),col("name"),
		lit("superior_emp_id"),col("superior_emp_id"),
		lit("year_joined"),col("year_joined"),
		lit("emp_dept_id"),col("emp_dept_id"),
		lit("gender"),col("gender"),
		lit("salary"),col("salary"))).drop("name",
			"superior_emp_id", "year_joined",
			"emp_dept_id", "gender", "salary")

# Display the data frame
empDF.show(truncate=False)
