from pyspark.sql.functions import substring

reg_df.withColumn(
'State', substring('LicenseNo', 1, 2)
).show()
