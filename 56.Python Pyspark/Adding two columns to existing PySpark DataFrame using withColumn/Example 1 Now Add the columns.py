new_df = df.withColumn('After_discount',
					df.Course_Fees - df.Discount).withColumn('Before_discount',
																df.Course_Fees)
new_df.show()
