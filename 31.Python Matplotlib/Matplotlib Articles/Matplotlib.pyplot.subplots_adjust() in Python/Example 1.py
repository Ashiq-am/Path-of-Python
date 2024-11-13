# Implementation of matplotlib function
import matplotlib.pyplot as plt


x = [1, 12, 3, 9]
y = [1, 4, 9, 16]
labels = ['Geeks1', 'Geeks2', 'Geeks3', 'Geeks4']

plt.plot(x, y)
plt.xticks(x, labels, rotation ='vertical')

plt.margins(0.2)
plt.subplots_adjust(bottom = 0.15)

plt.title('matplotlib.pyplot.subplots_adjust() Example')
plt.show()
