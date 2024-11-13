# Python Program illustrating
# pyplot.colorbar() method
import matplotlib.pyplot as plt

# creates four Axes
fig, axes = plt.subplots(nrows=2, ncols=2)

for ax in axes.flat:
	im = ax.imshow(np.random.random((10, 10)), vmin=0, vmax=1)

plt.colorbar(im, ax=axes.ravel().tolist())

plt.show()
