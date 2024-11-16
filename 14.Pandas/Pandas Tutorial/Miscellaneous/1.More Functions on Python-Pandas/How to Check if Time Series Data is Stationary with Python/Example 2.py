# import python pandas library
import pandas as pd

# import python matplotlib library for
# plotting
import matplotlib.pyplot as plt

# read the dataset using pandas read_csv()
# function
data = pd.read_csv("AirPassengers.csv",
				header=0, index_col=0)

# print the first 6 rows of data
print(data.head(10))

# use simple line plot to understand the
# data distribution
plt.plot(data)
