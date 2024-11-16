# Check if the updated price is available or not
if {'Updated Price', 'Discount'}.issubset(df.columns):
	df['Final cost'] = df['Updated Price'] - (df['Updated Price']*0.1)

elif {'Last Price', 'Discount'}.issubset(df.columns):
	df['Final cost'] = df['Last Price'] - (df['Last Price']*0.1)

# Print the Dataframe
print(df)




"""
available then we will apply the discount 

of 10% on the ‘Last Price’ column to calculate the final price

"""