# import the python pandas library
import pandas as pd

# read the data using pandas read_csv() function.
data = pd.read_csv("car-sales.csv", header=0,
				index_col=0, parse_dates=True,
				squeeze=True)
# printing the first 6 rows of the dataset
print(data.head(6))
