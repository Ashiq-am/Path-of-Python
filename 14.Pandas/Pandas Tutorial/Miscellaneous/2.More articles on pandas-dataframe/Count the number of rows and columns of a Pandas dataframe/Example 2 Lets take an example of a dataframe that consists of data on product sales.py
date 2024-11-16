# importing pandas
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Product' : ['Carrots', 'Broccoli', 'Banana',
								'Banana', 'Beans', 'Orange',
								'Broccoli', 'Banana'],
				'Category' : ['Vegetable', 'Vegetable', 'Fruit',
								'Fruit', 'Vegetable', 'Fruit',
								'Vegetable', 'Fruit'],
				'Quantity' : [8, 5, 3, 4, 5, 9, 11, 8],
				'Amount' : [270, 239, 617, 384, 626, 610, 62, 90]})

print(df)

# getting number of rows
print("Number of Rows: ", len(df.axes[0]))

# getting number of columns
print("Number of Columns: ", len(df.axes[1]))
