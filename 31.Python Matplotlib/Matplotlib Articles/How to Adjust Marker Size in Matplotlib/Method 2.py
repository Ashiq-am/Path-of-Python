# import necessary packages
import matplotlib.pyplot as plt

# data1&data2
data1 = [1, 2, 3, 4, 5]
data2 = [0, 0, 0, 0, 0]

# size of marker points
sizes = [10, 20, 30, 40, 50]

# plot graph
plt.scatter(data1, data2, sizes)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
