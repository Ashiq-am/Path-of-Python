# Import pandas library
import pandas as pd

# initialize list of lists
data = [['Harvey', 10, 45.25], ['Carson', 15, 54.85],
		['juli', 14, 87.21], ['Ricky', 20, 45.23],
		['Gregory', 21, 77.25], ['Jessie', 16, 95.21]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Marks'],
				index = ['a', 'b', 'c', 'd', 'e', 'f'])

# lets find out the data type
# of 'Marks' column
print (df.dtypes)
