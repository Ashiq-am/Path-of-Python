import pandas as pd
# Sample DataFrame
data = {'ID': [1, 2, 3, 4, 5],
		'Category': ['A', 'B', 'A', 'C', 'B'],
		'Value': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)
# Updating values using .loc for conditional updates
df.loc[df['Value'] > 20, 'Category'] = 'High'
df.loc[df['Value'] <= 20, 'Category'] = 'Low'
# Print the updated DataFrame using .loc
print("\nUpdated DataFrame (With .loc):")
print(df)
