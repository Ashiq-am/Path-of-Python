# Python program to demonstrate random
# sampling in pyspark without replacement

# Import libraries
import pandas as pd
from pyspark.sql import Row
from pyspark.sql import SparkSession

# create the session
spark = SparkSession.builder.getOrCreate()

# Create dataframe by passing passing list
df = spark.createDataFrame([
	Row(Brand="Redmi", Units=1000000, Performance="Outstanding", Ecofriendly="Yes"),
	Row(Brand="Samsung", Units=900000, Performance="Outstanding", Ecofriendly="Yes"),
	Row(Brand="Nokia", Units=500000, Performance="Excellent", Ecofriendly="Yes"),
	Row(Brand="Motorola",Units=400000, Performance="Average", Ecofriendly="Yes"),
	Row(Brand="Apple", Units=2000000,Performance="Outstanding", Ecofriendly="Yes")
])

# Apply sample() function without replacement
df_mobile_brands = df.sample(False, 0.5, 42)

# Print to the console
df_mobile_brands.show()
