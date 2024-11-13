# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

data = ((30, 1000), (10, 28), (100, 30),
		(500, 800), (50, 10))

dim = len(data[0])
w = 0.6
dimw = w / dim

fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
	y = [d[i] for d in data]
	b = ax.bar(x + i * dimw, y, dimw, bottom = 0.001)

ax.set_xticks(x + dimw / 2)
ax.set_xticklabels(map(str, x))
ax.set_yscale('log')

x = ax.get_facecolor()
ax.text(1, 2.3*(10**3), "Value of facecolor : " +str(x),
		style ='italic', fontsize = 10,
		color ="green")
ax.set_title('matplotlib.axes.Axes.get_facecolor() Example\n', fontsize = 12, fontweight ='bold')
plt.show()
