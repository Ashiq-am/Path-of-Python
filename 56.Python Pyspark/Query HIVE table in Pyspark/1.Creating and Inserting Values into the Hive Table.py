# import Spark Session
from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder.appName(
	"HiveQuery").enableHiveSupport().getOrCreate()

# create table query
spark.sql("CREATE TABLE IF NOT EXISTS employees (id INT, name STRING, age INT, sales_amt INT, "
		  "city STRING, state STRING)")

# insert values in the table
spark.sql("INSERT INTO TABLE employees VALUES (1, 'John', 28, 100, 'LA', 'CA'), (2, 'Jane', 32, 200, 'NY', 'NY'), "
		  "(3, 'David', 45, 150, 'LA', 'CA'), (4, 'Lisa', 23, 300, 'NY', 'NY'), (5, 'Mike', 38, 250, 'SF', 'CA')")

# display the table
df = spark.read.table("employees")
df.show()
