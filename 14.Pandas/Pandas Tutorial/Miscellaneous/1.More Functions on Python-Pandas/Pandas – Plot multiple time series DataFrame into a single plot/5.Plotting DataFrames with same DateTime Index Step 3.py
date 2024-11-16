# code
# Visualizing The Open Price of all the stocks

# to set the plot size
plt.figure(figsize=(16, 8), dpi=150)

# using plot method to plot open prices.
# in plot method we set the label and color of the curve.
tesla['Open'].plot(label='Tesla', color='orange')
gm['Open'].plot(label='GM')
ford['Open'].plot(label='Ford')

# adding title to the plot
plt.title('Open Price Plot')

# adding Label to the x-axis
plt.xlabel('Years')

# adding legend to the curve
plt.legend()
