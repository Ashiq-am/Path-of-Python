import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

plt.boxplot([data1, data2])
plt.title("Multiple Boxplots")
plt.show()
