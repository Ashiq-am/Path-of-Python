# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Creating dataset
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)

fig = plt.figure(figsize =(20, 16))
gs = gridspec.GridSpec(nrows = 3, ncols = 2, height_ratios =[1, 1, 2])

# Create a mask
mask = np.zeros(U.shape, dtype = bool)
mask[40:60, 40:60] = True
U[:20, :20] = np.nan
U = np.ma.array(U, mask = mask)

ax = fig.add_subplot(gs[2:, :])
ax.streamplot(X, Y, U, V, color ='r')
ax.set_title('Streamplot with Masking')

ax.imshow(~mask, extent =(-w, w, -w, w), alpha = 0.5,
		interpolation ='nearest', cmap ='gray', aspect ='auto')
ax.set_aspect('equal')

# show plot
plt.tight_layout()
plt.show()
