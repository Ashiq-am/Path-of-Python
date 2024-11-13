# Add new column with NUll
from pyspark.sql.functions import lit
df = df.select('*', lit(None).alias("Rewards"))

# Add new constanst column
df = df.select('*', lit(0.25).alias("Bonus Percent"))
df.show()
