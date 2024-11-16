# import python pandas library
import pandas as pd

# import python matplotlib library for plotting
import matplotlib.pyplot as plt

# read the dataset using pandas read_csv()
# function
data = pd.read_csv("daily-total-female-births-IN.csv",
				header=0, index_col=0)

# use simple line plot to see the distribution
# of the data
plt.plot(data)
