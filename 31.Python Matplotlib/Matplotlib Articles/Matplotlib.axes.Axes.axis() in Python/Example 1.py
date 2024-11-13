# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

labels = 'Geek1', 'Geek2', 'Geek3', 'Geek4', 'Geek5'
sizes = [95, 230, 145, 40, 65]
explode = (0, 0.2, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels,
        autopct='% 1.0f %%',
        shadow=True, startangle=90)
ax1.axis('square')
ax1.set_title('matplotlib.axes.Axes.axis() \
Example\n', fontsize=14, fontweight='bold')
plt.show()
