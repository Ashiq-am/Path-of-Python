import matplotlib.pyplot as plt

# the slices are ordered and
# plotted counter-clockwise:
product = 'Product A', 'Product B',
'Product C', 'Product D'

stock = [15, 30, 35, 20]
explode = (0.1, 0, 0.1, 0)

plt.pie(stock, explode=explode,
        labels=product, autopct='%1.1f%%',
        shadow=True, startangle=90,
        wedgeprops={"edgecolor": "black",
                    'linewidth': 3,
                    'antialiased': True})

# Equal aspect ratio ensures that
# pie is drawn as a circle.
plt.axis('equal')

plt.show()
