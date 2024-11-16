# importing pandas
import pandas as pd
result_data = {'name': ['Katherine', 'James', 'Emily',
						'Michael', 'Matthew', 'Laura'],
		'score': [98, 80, 60, 85, 49, 92],
		'age': [20, 25, 22, 24, 21, 20],
		'qualify_label': ['yes', 'yes', 'no',
						'yes', 'no', 'yes']}

# creating dataframe
df = pd.DataFrame(result_data, index = None)

# computing number of rows
rows = len(df.axes[0])

# computing number of columns
cols = len(df.axes[1])

print(df)
print("Number of Rows: ", rows)
print("Number of Columns: ", cols)
