# importing the module
import pandas as pd

# creating a DataFrame
list = [[15, 2.5, 100.22], [20, 4.5, 50.21],
		[25, 5.2, 80.55], [45, 5.8, 48.86],
		[40, 6.3, 70.99], [41, 6.4, 90.25],
		[51, 2.3, 111.90]]
df = pd.DataFrame(list, columns = ['Field_1', 'Field_2', 'Field_3'],
				index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
display(df)
