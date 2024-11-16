# Import pandas library
import pandas as pd

# initialize list of lists
data = [['Harvey.', 10.5, 45.25, 95.2],
		['Carson', 15.2, 54.85, 50.8],
		['juli', 14.9, 87.21, 60.4],
		['Ricky', 20.3, 45.23, 99.5],
		['Gregory', 21.1, 77.25, 90.9],
		['Jessie', 16.4, 95.21, 10.85]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'Percentage', 'Accuracy'],
				index=['a', 'b', 'c', 'd', 'e', 'f'])

# print dataframe.
df
