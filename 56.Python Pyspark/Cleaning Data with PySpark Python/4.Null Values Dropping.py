# Dropping Entire rows containing Null
null_dropped=df_pyspark.na.drop()
null_dropped.show()
