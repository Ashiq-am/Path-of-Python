# defining split() along with withColumn()
df2 = df.withColumn('Year', split(df['DOB'], '-').getItem(0)) \
	.withColumn('Month', split(df['DOB'], '-').getItem(1)) \
	.withColumn('Day', split(df['DOB'], '-').getItem(2))

# show df2
df2.show()
