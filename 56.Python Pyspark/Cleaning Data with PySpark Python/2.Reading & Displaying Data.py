# Create Spark DataFrame
df_pyspark = sparkSession.read.csv(
	'Employee_Table.csv',
	header=True,
	inferSchema=True
)
