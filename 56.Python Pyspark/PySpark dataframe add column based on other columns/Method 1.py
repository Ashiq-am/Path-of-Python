new_df = df.withColumn('After_discount',
					df.Course_Fees - df.Discount)
new_df.show()
