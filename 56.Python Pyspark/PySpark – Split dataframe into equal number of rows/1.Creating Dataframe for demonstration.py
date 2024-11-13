# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# Column names for the dataframe
columns = ["Brand", "Product"]

# Row data for the dataframe
data = [
	("HP", "Laptop"),
	("Lenovo", "Mouse"),
	("Dell", "Keyboard"),
	("Samsung", "Monitor"),
	("MSI", "Graphics Card"),
	("Asus", "Motherboard"),
	("Gigabyte", "Motherboard"),
	("Zebronics", "Cabinet"),
	("Adata", "RAM"),
	("Transcend", "SSD"),
	("Kingston", "HDD"),
	("Toshiba", "DVD Writer")
]

# Create the dataframe using the above values
prod_df = spark.createDataFrame(data=data,
								schema=columns)

# View the dataframe
prod_df.show()
