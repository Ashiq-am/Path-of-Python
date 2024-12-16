# Create another DataFrame to be concatenated horizontally
new_data = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Sales', 'Operations'],
    'Location': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin']
})

# Concatenate horizontally (along columns)
combined_df = pd.concat([df, new_data], axis=1)

# Display the combined DataFrame
print(combined_df)