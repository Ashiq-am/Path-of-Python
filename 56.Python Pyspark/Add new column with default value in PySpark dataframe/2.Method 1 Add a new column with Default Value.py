# Add new column with NUll
from pyspark.sql.functions import lit
df = df.withColumn("Rewards", lit(None))
df.show()

# Add new constanst column
df = df.withColumn("Bonus Percent", lit(0.25))
df.show()
