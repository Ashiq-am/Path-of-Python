# importing modules
from pandas import *
import matplotlib.pyplot as plt

# reading CSV file
d = read_csv("company_sales_data.csv")

# creating an empty chart
fig, axes = plt.subplots()

# plotting using plt.stem
axes.stem(d['month_number'], d['total_profit'],
		use_line_collection=True, basefmt=' ')

# starting value of y-axis
axes.set_ylim(0)

# details and formatting of chart
plt.title('Total Profit')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.xticks(d['month_number'])
