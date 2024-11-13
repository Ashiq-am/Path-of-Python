from pyspark.sql.functions import substring

reg_df.select(
substring('LicenseNo' , 1, 2).alias('State') ,
substring('LicenseNo' , 3, 4).alias('RegYear'),
substring('LicenseNo' , 7, 8).alias('RegID') ,
substring('ExpiryDate', 1, 4).alias('ExpYr') ,
substring('ExpiryDate', 6, 2).alias('ExpMo') ,
substring('ExpiryDate', 9, 2).alias('ExpDt') ,
).show()
