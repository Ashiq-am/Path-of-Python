# by using withcolumn function
df_col1 = df_col1.withColumn('withcolum_Sum',
							data['B']+data['C']+data['D'])

# Showing and printing the schema
# of the Dataframe
df_col1.printSchema()
df_col1.show()
