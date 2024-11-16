# Define a function to map the values
def set_value(row_number, assigned_value):
	return assigned_value[row_number]

# Create the dictionary
event_dictionary ={'Music' : 1500, 'Poetry' : 800, 'Comedy' : 1200}

# Add a new column named 'Price'
df['Price'] = df['Event'].apply(set_value, args =(event_dictionary, ))

# Print the DataFrame
print(df)
