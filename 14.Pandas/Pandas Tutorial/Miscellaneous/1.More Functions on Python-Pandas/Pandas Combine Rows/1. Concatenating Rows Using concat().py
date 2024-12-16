# Create a new DataFrame to be combined with the original one
new_data = pd.DataFrame({
    'Name': ['Grace', 'Sophia'],
    'Age': [40, 27],
    'Gender': ['Female', 'Female'],
    'Salary': [65000, 52000]
})

# Combine the original DataFrame with the new data
combined_df = pd.concat([df, new_data], ignore_index=True)

# Display the updated DataFrame
print(combined_df)