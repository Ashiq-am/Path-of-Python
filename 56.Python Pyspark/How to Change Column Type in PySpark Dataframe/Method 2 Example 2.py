# Changing datatype of all the columns
# to string type
from pyspark.sql.types import StringType

course_df5 = course_df.select(
[course_df.cast(StringType())
.alias(c) for c in course_df.columns]
)
course_df5.printSchema()
