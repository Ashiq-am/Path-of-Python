# import the python pandas library
import pandas as pd

# read data using read_csv
data = pd.read_csv("Detergent sales data.csv", header=0,
				index_col=0, parse_dates=True, squeeze=True)
