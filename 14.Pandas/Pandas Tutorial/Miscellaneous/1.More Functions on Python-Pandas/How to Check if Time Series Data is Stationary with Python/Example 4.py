# import python pandas library
import pandas as pd

# import python matplotlib library for plotting
import matplotlib.pyplot as plt

# import python numpy library
import numpy as np

# read the dataset using pandas read_csv()
# function
data = pd.read_csv("AirPassengers.csv", header=0, index_col=0)

# extracting only the air passengers count
# from the dataset using values function
values = log(data.values)

# printing the first 15 passenger count values
print(values[0:15])

# using simple line plot to understand the
# data distribution
plt.plot(values)
