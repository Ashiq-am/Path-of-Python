# Extracting the month and year from the index of the above dataset "Monthly Sunspots"
data['Month_Num'] = data.index.month

# Grouping the data by month, calculating the average number of sunspots for each month
monthly_average = data.groupby('Month_Num')['Sunspots'].mean()

# Polar Plot theta (angle) and radii (length) settings
theta = np.linspace(0, 2 * np.pi, len(monthly_average))
radii = monthly_average.values

# Polar Plot
plt.figure(figsize=(7, 5))
plt.polar(theta, radii)
plt.title('Polar Plot of Monthly Average Sunspots')
plt.xticks(theta, ['Jan', 'Feb', 'Mar', 'Apr', 'May',
				'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Set y-axis limit to accommodate the data
plt.ylim(0, radii.max() + 10)
plt.show()
