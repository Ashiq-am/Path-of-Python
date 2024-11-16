# importing pandas as pd
import pandas as pd

# create the DataFrame
df = pd.DataFrame({
	'Product': ['Umbrella', 'Matress', 'Badminton',
				'Shuttle', 'Sofa', 'Football'],
	'MRP': [1200, 1500, 1600, 352, 5000, 500],
	'Discount': [0, 10, 0, 10, 20, 40]
})

# display the DataFrame
print(df)
