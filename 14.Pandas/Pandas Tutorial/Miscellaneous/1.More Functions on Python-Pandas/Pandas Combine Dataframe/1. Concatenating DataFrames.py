# Create another DataFrame to be concatenated
new_data = pd.DataFrame({
    'Name': ['Grace', 'Sophia'],
    'Age': [40, 27],
    'Gender': ['Female', 'Female'],
    'Salary': [65000, 52000]
})

# Concatenate vertically (along rows)
combined_df = pd.concat([df, new_data], ignore_index=True)

# Display the combined DataFrame
print(combined_df)