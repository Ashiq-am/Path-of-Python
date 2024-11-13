# Adding a Y-Axis Label to the
# Secondary Y-Axis in Matplotlib
# importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# creating data for plot
# data arrangement between 0 and 50 with the difference of 2
# x-axis values
x = np.arange(0, 50, 2)

#y-axis values
y1 = x**2

# secondary y-axis values
y2 = x**3

# plotting figures by creating aexs object
# using subplots() function
fig, ax = plt.subplots(figsize = (10, 5))
plt.title('Example of Two Y labels')

# using the twinx() for creating
# another axes object for secondry y-Axis
ax2 = ax.twinx()
# creating a bar plot
ax.bar(x, y1, color = 'g')
ax2.bar(x, y2, color = 'b')

# giving labels to the axises
ax.set_xlabel('x-axis', color = 'r')
ax.set_ylabel('y1-axis', color = 'g')

# secondary y-axis label
ax2.set_ylabel('Secondary y-axis', color = 'b')

# defining display layout
plt.tight_layout()

# show plot
plt.show()
