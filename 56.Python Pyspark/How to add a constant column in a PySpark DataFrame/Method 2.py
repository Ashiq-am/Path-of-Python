df.registerTempTable('table')
newDF = spark.sql('select *, 1 as newCol from table')
newDF.show()
