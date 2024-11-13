import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

plt.rcParams["figure.figsize"] = [10.00, 6.00]
plt.rcParams["figure.autolayout"] = True

# Data for mosaic plot
data = {'John': 7, 'Joe': 10, 'James': 5, 'Kate': 1}

# Customizing the mosaic plot
props = lambda key: {'color': 'skyblue' if key == 'John' else 'lightgreen'}

# Create mosaic plot with custom properties
mosaic(data, title='Customized Mosaic Plot', properties=props)
plt.show()
