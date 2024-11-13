from pyspark.sql.functions import substring

reg_df.selectExpr(
'LicenseNo',
'ExpiryDate',
'substring(LicenseNo , 1, 2) AS State' ,
'substring(LicenseNo , 3, 4) AS RegYear' ,
'substring(LicenseNo , 7, 8) AS RegID' ,
'substring(ExpiryDate, 1, 4) AS ExpYr' ,
'substring(ExpiryDate, 6, 2) AS ExpMo' ,
'substring(ExpiryDate, 9, 2) AS ExpDt' ,
).show()
