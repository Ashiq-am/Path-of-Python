# Python program to demonstrate stratified sampling in pyspark

# Import libraries
import pandas as pd
from pyspark.sql import Row
from pyspark.sql import SparkSession

# Create the session
spark = SparkSession.builder.getOrCreate()

# Creating dataframe by passing list
df = spark.createDataFrame([
	Row(Brand="Redmi", Units=1000000, Performance="Outstanding", Ecofriendly="Yes"),
	Row(Brand="Samsung", Units=1000000, Performance="Outstanding", Ecofriendly="Yes"),
	Row(Brand="Nokia", Units=400000, Performance="Excellent", Ecofriendly="Yes"),
	Row(Brand="Motorola",Units=400000, Performance="Average", Ecofriendly="Yes"),
	Row(Brand="OPPO",Units=400000, Performance="Average", Ecofriendly="Yes"),
	Row(Brand="Apple", Units=2000000,Performance="Outstanding", Ecofriendly="Yes")
])

# Applying sampleBy() function
mobile_brands = df.sampleBy("Units", fractions={
1000000: 0.2, 2000000: 0.4, 400000: 0.2}, seed=0)

# Print to the console
mobile_brands.show()
