# Create the dictionary
event_dictionary ={'Music' : 1500, 'Poetry' : 800, 'Comedy' : 1200}

# Add a new column named 'Price'
df['Price'] = df['Event'].map(event_dictionary)

# Print the DataFrame
print(df)
