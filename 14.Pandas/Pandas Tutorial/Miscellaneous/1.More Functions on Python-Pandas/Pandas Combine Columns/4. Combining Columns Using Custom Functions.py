# Combine 'First Name', 'Last Name' and 'Age' into a custom message
df['Message'] = df.apply(lambda row: f"{row['First Name']} {row['Last Name']} is {row['Age']} years old.", axis=1)

# Display the updated DataFrame
print(df)