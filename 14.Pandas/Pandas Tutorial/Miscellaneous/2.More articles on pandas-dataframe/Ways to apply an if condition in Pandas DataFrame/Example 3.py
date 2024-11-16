# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({
	'Product': ['Umbrella', 'Matress', 'Badminton',
				'Shuttle', 'Sofa', 'Football'],
	'MRP': [1200, 1500, 1600, 352, 5000, 500],
	'Discount': [0, 10, 0, 10, 20, 40]
})

# Print the dataframe
print(df)

# If condition on column values using Lambda function
df['Discount'] = df['Discount'].apply(lambda x : 20 if x > 20 else x)
print(df)
