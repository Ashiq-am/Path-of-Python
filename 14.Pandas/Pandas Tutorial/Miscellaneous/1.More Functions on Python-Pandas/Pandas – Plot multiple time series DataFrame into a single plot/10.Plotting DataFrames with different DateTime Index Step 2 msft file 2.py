# Visualizing The Price of the stocks
# to set the plot size
plt.figure(figsize=(16, 8), dpi=150)

# using .plot method to plot stock prices.
# we have passed colors as a list
aapl.plot(label='aapl', color=['orange', 'green'])

# adding title
plt.title('Price Plot')

# adding label to x-axis
plt.xlabel('Years')

# adding legend.
plt.legend()
