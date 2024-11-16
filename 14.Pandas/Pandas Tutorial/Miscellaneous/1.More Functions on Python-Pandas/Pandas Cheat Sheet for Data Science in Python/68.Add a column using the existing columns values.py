# Add a column using the existing columns values
df = df.assign(Paid_Price=lambda df:
			(df.QUANTITY * df.PRICE)\
			-(df.QUANTITY * df.PRICE)\
			*df.DISCOUNT/100)
print(df)
