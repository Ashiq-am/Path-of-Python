# Combine 'First Name' and 'Last Name' into 'Full Name'
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

# Display the updated DataFrame
print(df)