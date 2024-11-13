import pandas as pd
import matplotlib.pyplot as plt
import string as str


# Creating a DataFrame from the CSV Dataset
df = pd.read_csv("car_sales.csv", sep=';')

# Separating the Date and Mercedes-Benz Cars unit sales (USA)
df['car_sales_z'] = df.loc[:, ['Mercedes-Benz Cars unit sales (USA)']]
df['car_sales_z'] = df['car_sales_z'] .str.replace(
	',', '').astype(float)

# Removing null value
df.drop(df.tail(1).index, inplace=True)

for i in range(35):
	# Colour of bar chart is set to red if the sales
	# is < 60000 and green otherwise
	df['colors'] = ['red' if float(
		x) < 60000 else 'green' for x in df['car_sales_z']]

# Sort values from lowest to highest
df.sort_values('car_sales_z', inplace=True)

# Resets initial index in Dataframe to None
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(14, 10), dpi=80)

# Plotting the horizontal lines
plt.hlines(y=df.index, xmin=60000, xmax=df.car_sales_z,
		color=df.colors, alpha=0.4, linewidth=5)

# Decorations
# Setting the labels of x-axis and y-axis
plt.gca().set(ylabel='Quarter', xlabel='Sales')

# Setting Date to y-axis
plt.yticks(df.index, df.Date, fontsize=12)

# Title of Bar Chart
plt.title('Diverging Bars Chart Example', fontdict={
		'size': 20})

# Optional grid layout
plt.grid(linestyle='--', alpha=0.5)

# Displaying the Diverging Bar Chart
plt.show()
