# We can also make use of datatypes from
# pyspark.sql.types
from pyspark.sql.types import StringType, DateType, FloatType

course_df3 = course_df \
.withColumn("Course_Fees" ,
			course_df["Course_Fees"]
			.cast(FloatType())) \
.withColumn("Payment_Done",
			course_df["Payment_Done"]
			.cast(StringType())) \
.withColumn("Start_Date" ,
			course_df["Start_Date"]
			.cast(DateType())) \

course_df3.printSchema()
