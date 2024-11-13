from pyspark.sql.functions import substring

reg_df \
.withColumn('State' , substring('LicenseNo' , 1, 2)) \
.withColumn('RegYear', substring('LicenseNo' , 3, 4)) \
.withColumn('RegID' , substring('LicenseNo' , 7, 8)) \
.withColumn('ExpYr' , substring('ExpiryDate', 1, 4)) \
.withColumn('ExpMo' , substring('ExpiryDate', 6, 2)) \
.withColumn('ExpDt' , substring('ExpiryDate', 9, 2)) \
.show()
