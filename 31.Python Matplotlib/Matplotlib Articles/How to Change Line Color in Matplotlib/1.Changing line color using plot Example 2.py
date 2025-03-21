import matplotlib.pyplot as plt

# Adding X and Y axis label
plt.ylabel('Year')
plt.xlabel('Population')

# Adding title to the plot
plt.title("Shwarma Population")

# Plotting x and y axes and line color to orange
plt.plot([100, 200, 300, 400, 500, 600], [
		1950, 1960, 1970, 1980, 1990, 2000], 'g')

plt.show()
