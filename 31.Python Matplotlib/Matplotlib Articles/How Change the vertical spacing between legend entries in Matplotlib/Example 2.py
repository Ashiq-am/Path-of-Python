# importing package
import matplotlib.pyplot as plt

#Create data and plot lines.
plt.plot([0, 1], [0, 2.0], label = 'Label-1')
plt.plot([1, 2], [0, 2.1], label = 'Label-2')
plt.plot([2, 3], [0, 2.2], label = 'Label-3')

# Change the label spacing here
plt.legend(labelspacing = 2)
plt.title("Line Graph - Geeksforgeeks")

plt.show()
