from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import getpass
username = getpass.getuser()
spark = SparkSession.builder.appName("Identify corrupted records").getOrCreate()
customers_schema = '''
customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode int,
_corrupt_record string
'''
customers_df = spark.read.schema(customers_schema).format("csv").options(header = True,delimiter = "|",
			mode = "PERMISSIVE", columnNameOfCorruptRecord = "_corrupt_record").load(
			f"C:\\Users\\{username}\\Desktop\\PYSPARK\\source\\corrupted_customer_details.csv")
customers_df.filter(col("_corrupt_record").isNotNull()).show()
print(f"Total number of records while reading in PERMISSIVE mode : {customers_df.count()}")
