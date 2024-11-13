from pyspark.sql.types import StringType, BooleanType, IntegerType

course_df4 = course_df3.select(
	course_df3.Name,
	course_df3.Course_Name,
	course_df3.Duration_Months,
	(course_df3.Course_Fees.cast(IntegerType()))
	.alias('Course_Fees'),
	(course_df3.Start_Date.cast(StringType()))
	.alias('Start_Date'),
	(course_df3.Payment_Done.cast(BooleanType()))
	.alias('Payment_Done'),
)

course_df4.printSchema()
