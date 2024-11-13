# Import col method from pyspark.sql.functions
from pyspark.sql.functions import col

# Selct the 'salary' as 'Amount' using aliasing
# Selct remainging with their original name
data = df.select(col("Name"),col("DOB"),
				col("Gender"),
				col("salary").alias('Amount'))

# Print the dataframe
data.show()
