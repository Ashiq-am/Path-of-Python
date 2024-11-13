from pyspark.sql.types import (
	StringType, BooleanType, IntegerType, FloatType, DateType
)

coltype_map = {
	"Name": StringType(),
	"Course_Name": StringType(),
	"Duration_Months": IntegerType(),
	"Course_Fees": FloatType(),
	"Start_Date": DateType(),
	"Payment_Done": BooleanType(),
}

# course_df6 has all the column
# types as string
course_df6 = course_df5.select(
	[course_df5.cast(coltype_map)
	.alias(c) for c in course_df5.columns]
)
course_df6.printSchema()
