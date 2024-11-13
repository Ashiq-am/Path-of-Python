# course_df5 has all the column datatypes as string
course_df5.createOrReplaceTempView("course_view")

course_df7 = spark.sql('''
SELECT
Name,
Course_Name,
INT(Duration_Months),
FLOAT(Course_Fees),
DATE(Start_Date),
BOOLEAN(Payment_Done)
FROM course_view
''')

course_df7.printSchema()
