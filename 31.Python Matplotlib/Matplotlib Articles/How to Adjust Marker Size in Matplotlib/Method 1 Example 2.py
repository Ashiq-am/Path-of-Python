# import necessary packages
import matplotlib.pyplot as plt

# data1&data2
data1 = [1, 2, 3, 4, 5]
data2 = [1, 2, 1, 2, 1]

# plot graph
plt.plot(data1, data2, marker=".", markersize=20)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
