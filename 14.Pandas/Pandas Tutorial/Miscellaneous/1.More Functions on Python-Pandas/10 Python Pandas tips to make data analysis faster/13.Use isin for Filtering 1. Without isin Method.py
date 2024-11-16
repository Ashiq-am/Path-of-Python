import pandas as pd
# Sample DataFrame
data = {'ID': [1, 2, 3, 4, 5],
		'Category': ['A', 'B', 'A', 'C', 'B'],
		'Value': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)
# Filtering using traditional method
categories_to_filter = ['A', 'B']
filtered_df = df[df['Category'].apply(lambda x: x in categories_to_filter)]
# Print the filtered DataFrame
print("Filtered DataFrame (Without isin):")
print(filtered_df)
