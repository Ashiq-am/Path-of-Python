# importing package
import matplotlib.pyplot as plt

# sample code
plt.bar([1, 2, 3], [16, 4, 1],
		color ='yellow',
		label = 'Label 2')

plt.bar([4, 5], [2, 4],
		label = 'Label 1')

# Add a title to a legend
plt.legend(title = "Variation Rate")

plt.title("Line Graph - Geeksforgeeks")

plt.show()
