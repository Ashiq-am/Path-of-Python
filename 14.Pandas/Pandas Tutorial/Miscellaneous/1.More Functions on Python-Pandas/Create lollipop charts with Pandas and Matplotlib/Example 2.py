# import modules
from pandas import *
from matplotlib import pyplot as plt

# read csv file
d = read_csv("company_sales_data.csv")

# using subplots() to draw vertical lines
fig, axes = plt.subplots()
axes.vlines(d['month_number'], ymin=0, ymax=d['total_profit'])

# drawing the markers (circle)
axes.plot(d['month_number'], d['total_profit'], "o")
axes.set_ylim(0)

# formatting and details
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Total Profit')
plt.xticks(d['month_number'])
