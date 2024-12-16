# Create a new DataFrame to be appended
new_data = pd.DataFrame({
    'Name': ['Grace', 'Sophia'],
    'Age': [40, 27],
    'Gender': ['Female', 'Female'],
    'Salary': [65000, 52000]
})

# Append the new data to the original DataFrame
df = df.append(new_data, ignore_index=True)

# Display the updated DataFrame
print(df)