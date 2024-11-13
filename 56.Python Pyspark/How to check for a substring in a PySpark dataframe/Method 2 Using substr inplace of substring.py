from pyspark.sql.functions import col

reg_df \
.withColumn('State' , col('LicenseNo' ).substr(1, 2)) \
.withColumn('RegYear', col('LicenseNo' ).substr(3, 4)) \
.withColumn('RegID' , col('LicenseNo' ).substr(7, 8)) \
.withColumn('ExpYr' , col('ExpiryDate').substr(1, 4)) \
.withColumn('ExpMo' , col('ExpiryDate').substr(6, 2)) \
.withColumn('ExpDt' , col('ExpiryDate').substr(9, 2)) \
.show()
