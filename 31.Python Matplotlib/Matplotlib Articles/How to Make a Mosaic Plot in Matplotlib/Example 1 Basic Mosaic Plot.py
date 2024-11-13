import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# Dictionary for mosaic plot data
data = {'John': 7, 'Joe': 10, 'James': 5, 'Kate': 1}

# Create mosaic plot
mosaic(data, title='Basic Mosaic Plot')
plt.show()
