from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import getpass

username = getpass.getuser()
spark = SparkSession.builder.appName("Drop corrupted records").getOrCreate()
customers_schema = '''
customer_id int,
customer_fname string,
customer_lname string,
customer_email string,
customer_password string,
customer_street string,
customer_city string,
customer_state string,
customer_zipcode int
'''
customers_df = spark.read.schema(
customers_schema).format("csv").options(header = True,
	delimiter = "|", mode = "DROPMALFORMED").load(f"C:\\Users\\{
		username}\\Desktop\\PYSPARK\\source\\corrupted_customer_details.csv")
customers_df.show()
print(f"Total number of records while reading in \
			DROPMALFORMED mode : {customers_df.count()}")
