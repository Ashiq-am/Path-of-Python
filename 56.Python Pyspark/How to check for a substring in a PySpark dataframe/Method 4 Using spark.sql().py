reg_df.createOrReplaceTempView("reg_view")

reg_df2 = spark.sql('''
SELECT
SUBSTR(LicenseNo, 1, 3) AS State,
SUBSTR(LicenseNo, 3, 4) AS RegYear,
SUBSTR(LicenseNo, 7, 8) AS RegID,
SUBSTR(ExpiryDate, 1, 4) AS ExpYr,
SUBSTR(ExpiryDate, 6, 2) AS ExpMo,
SUBSTR(ExpiryDate, 9, 2) AS ExpDt
FROM reg_view;
''')

reg_df2.show()
