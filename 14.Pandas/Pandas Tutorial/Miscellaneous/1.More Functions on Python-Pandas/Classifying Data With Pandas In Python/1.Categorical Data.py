# Sample DataFrame with categorical data for a classification task
data = {'Category': ['Small', 'Medium', 'Large', 'Medium', 'Small', 'Large', 'Medium', 'Large', 'Small'],
		'Value1': [15, 30, 45, 20, 10, 40, 25, 35, 12],
		'Value2': [5, 10, 15, 8, 4, 12, 7, 11, 3],
		'Label': ['A', 'B', 'C', 'A', 'B', 'C', 'B', 'C', 'A']}

df = pd.DataFrame(data)

# Convert 'Category' column to categorical type
df['Category'] = pd.Categorical(df['Category'], categories=['Small', 'Medium', 'Large'], ordered=True)

# Explore ordered categories
print("Ordered Categories:")
print(df['Category'].describe())

# Create custom categories based on 'Value1' and 'Value2'
df['CustomCategory'] = pd.cut(df['Value1'], bins=[0, 15, 30, 45], labels=['Low', 'Medium', 'High'])

# Handle missing values by filling with a default category
df['Category'].fillna('Unknown', inplace=True)

# Display the optimized DataFrame
print("\nOptimized DataFrame:")
print(df)
