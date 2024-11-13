from pyspark.sql.functions import col, lit


df.select('*',lit("Cricket").alias("Sport")).withColumn("Fitness",lit(("Good"))).show()
