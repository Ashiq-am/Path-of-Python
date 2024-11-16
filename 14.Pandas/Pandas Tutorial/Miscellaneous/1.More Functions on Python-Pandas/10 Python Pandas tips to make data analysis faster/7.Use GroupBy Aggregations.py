#Without groupby
import pandas as pd
# Sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
			'Value': [10, 20, 15, 25, 12, 18]}
df = pd.DataFrame(data)

# Iterative approach to calculate average for each category
categories = df['Category'].unique()
for category in categories:
			avg_value = df[df['Category'] == category]['Value'].mean()
			print(f'Average Value for Category {category}: {avg_value}')
