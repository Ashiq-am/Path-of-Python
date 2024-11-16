# Add a new column named 'Price'
df['Price'] = [1500 if x =='Music' else 800 for x in df['Event']]

# Print the DataFrame
print(df)
