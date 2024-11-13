import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

plt.boxplot([data1, data2])

legend_handle1 = mpatches.Patch(color='blue', label='Dataset 1')
legend_handle2 = mpatches.Patch(color='orange', label='Dataset 2')

plt.legend(handles=[legend_handle1, legend_handle2])
plt.title("Boxplot with Custom Legend")
plt.show()
