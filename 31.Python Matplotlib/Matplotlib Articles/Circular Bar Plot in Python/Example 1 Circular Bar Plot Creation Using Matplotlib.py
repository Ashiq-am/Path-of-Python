import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [20, 35, 30, 25]

# Create a circular bar plot
fig, ax = plt.subplots(subplot_kw=dict(polar=True))
bars = ax.bar(np.arange(len(categories)) * 2 * np.pi / len(categories), values)

plt.show()
