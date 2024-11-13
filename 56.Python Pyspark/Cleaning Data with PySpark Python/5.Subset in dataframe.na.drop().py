# Dropping Rows where Joining Year is missing
non_null_year = df_pyspark.na.drop(subset=['Joining Year'])
non_null_year.show()
