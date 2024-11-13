# Cast Course_Fees from integer type to float type
course_df2 = course_df.withColumn("Course_Fees",
								course_df["Course_Fees"]
								.cast('float'))
course_df2.printSchema()
