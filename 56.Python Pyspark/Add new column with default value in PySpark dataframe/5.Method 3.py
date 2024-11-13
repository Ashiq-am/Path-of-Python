import findspark
findspark.init()

# Importing the modules
from datetime import datetime, date
import pandas as pd
from pyspark.sql import SparkSession

# creating the session
spark = SparkSession.builder.getOrCreate()

# creating the dataframe
pandas_df = pd.DataFrame({
	'Name': ['Anurag', 'Manjeet', 'Shubham',
			'Saurabh', 'Ujjawal'],
	'Address': ['Patna', 'Delhi', 'Coimbatore',
				'Greater noida', 'Patna'],
	'ID': [20123, 20124, 20145, 20146, 20147],
	'Sell': [140000, 300000, 600000, 200000, 600000]
})
df = spark.createDataFrame(pandas_df)
print("Original DataFrame :")
df.show()
