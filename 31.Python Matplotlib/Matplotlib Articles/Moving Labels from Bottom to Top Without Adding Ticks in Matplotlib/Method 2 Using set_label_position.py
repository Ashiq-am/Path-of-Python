import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

# Move the x-axis label to the top
ax.xaxis.set_label_position('top')
plt.show()
