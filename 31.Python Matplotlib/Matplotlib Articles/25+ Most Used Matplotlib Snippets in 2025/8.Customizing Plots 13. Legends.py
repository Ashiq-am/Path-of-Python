import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [15, 25, 20, 35]
plt.plot(x, y1, label='Dataset 1', color='blue')
plt.plot(x, y2, label='Dataset 2', color='orange')
plt.title('Customized Legend')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# Customizing legend
plt.legend(loc='upper left', ncol=1, facecolor='lightgray', fontsize='medium')
plt.show()