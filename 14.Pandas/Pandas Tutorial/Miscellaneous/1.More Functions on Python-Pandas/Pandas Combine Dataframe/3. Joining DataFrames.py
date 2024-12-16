# Create another DataFrame to join based on the index
df3 = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Sales', 'Operations'],
    'Location': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin']
}, index=['John', 'Alice', 'Bob', 'Eve', 'Charlie'])

# Join the two DataFrames based on their index
joined_df = df.set_index('Name').join(df3)

# Display the joined DataFrame
print(joined_df)