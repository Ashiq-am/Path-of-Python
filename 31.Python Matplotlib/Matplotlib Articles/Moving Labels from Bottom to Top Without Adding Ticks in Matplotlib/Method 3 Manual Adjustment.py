import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

# Move the x-axis label to the top
x_lbl_pos = (0.5, 1.05)
ax.xaxis.set_label_coords(*x_lbl_pos)
plt.show()
