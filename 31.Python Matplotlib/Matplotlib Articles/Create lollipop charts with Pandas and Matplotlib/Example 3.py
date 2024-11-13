# import modules
from pandas import *
from matplotlib import pyplot as plt

# read csv file
d = read_csv("company_sales_data.csv")

# using subplots() to draw vertical lines
fig, axes = plt.subplots()

# providing list of colors
line_colors = ['blue', 'cyan', 'green', 'red',
			'skyblue', 'brown', 'yellow',
			'black', 'grey', 'orange', 'maroon',
			'lightgreen']

axes.hlines(d['month_number'], xmin=0,
			xmax=d['total_profit'], colors=line_colors)

# drawing the markers (circle)
axes.plot(d['total_profit'], d['month_number'], "o")
axes.set_xlim(0)

# formatting and details
plt.xlabel('Profit')
plt.ylabel('Month')
plt.title('Total Profit')
plt.yticks(d['month_number'])
