import pandas as pd
# Sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
		'Value': [10, 20, 15, 25, 12, 18]}
df = pd.DataFrame(data)
# Using groupby to calculate average for each category
result = df.groupby('Category')['Value'].mean()
# Print the result
print(result)
