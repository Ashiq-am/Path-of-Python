df.registerTempTable('table')
newDF = spark.sql('select *, Course_Fees - Discount as Total from table')
newDF.show()
