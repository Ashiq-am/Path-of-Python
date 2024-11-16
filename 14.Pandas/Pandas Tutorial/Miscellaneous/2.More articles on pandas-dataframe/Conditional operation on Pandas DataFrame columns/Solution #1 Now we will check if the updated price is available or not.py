# Check if the updated price is available or not
if 'Updated Price' in df.columns:
	df['Final cost'] = df['Updated Price'] - (df['Updated Price']*0.1)

else :
	df['Final cost'] = df['Last Price'] - (df['Last Price']*0.1)

# Print the Dataframe
print(df)
