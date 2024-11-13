from pyspark.sql.functions import udf
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, FloatType
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

# Define a Python function to calculate the
#commission for each salesperson in each order
@udf(FloatType())
def calculate_commission(sales):
	if sales > 5000:
		return sales * 10000.0
	else:
		return sales * 100000.0

# Define a Python function to extract the month from the date
@udf(StringType())
def extract_month(date):
	return date.split('-')[1]

# Create a DataFrame from the sales data
sales_data = spark.createDataFrame([
	("Alice", "2022-01-01", 5000),
	("Alice", "2022-01-01", 7000),
	("Alice", "2022-02-01", 5000),
	("Bob", "2022-01-01", 2000),
	("Bob", "2022-01-01", 4000),
	("Bob", "2022-02-01", 2000)
], ["salesperson", "date", "sales"])

# Apply the UDFs to each row of the DataFrame and group
#by salesperson and month
sales_data = sales_data.withColumn('commission'
	, calculate_commission('sales'))
sales_data = sales_data.withColumn('month'
	, extract_month('date'))
sales_data = sales_data.groupBy('salesperson'
	, 'month').agg(
	{'sales': 'sum', 'commission': 'sum'})

# Rename the aggregated columns to 'total_sales' and
#'total_commission' and sort by salesperson and month
sales_data = sales_data.withColumnRenamed('sum(sales)'
	, 'total_sales')
sales_data = sales_data.withColumnRenamed('sum(commission)'
	, 'total_commission')
sales_data = sales_data.orderBy(['salesperson'
	, 'month'])

# Show the resulting DataFrame
sales_data.show()
