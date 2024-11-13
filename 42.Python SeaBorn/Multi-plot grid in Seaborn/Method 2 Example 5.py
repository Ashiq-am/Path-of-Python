import matplotlib.pyplot as plt

Grid_plot = plt.GridSpec(2, 3, wspace = 0.8,
						hspace = 0.6)

plt.subplot(Grid_plot[0, 0])
plt.subplot(Grid_plot[0, 1:])
plt.subplot(Grid_plot[1, :2])
plt.subplot(Grid_plot[1, 2])
