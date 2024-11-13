# importing required libraries
import matplotlib.pyplot as plt
import numpy as np

# setting different parameters to adjust each grid
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7),
					gridspec_kw={
						'width_ratios': [3, 3],
						'height_ratios': [3, 3],
					'wspace': 0.4,
					'hspace': 0.4})


# initializing x,y axis value
x = np.arange(0, 10, 0.1)
y = np.tan(x)

# ax[0][0] will take 0th position in
# geometry(Grid we created for subplots)
ax[0][0].plot(x, y)

# ax[0][0] will take 0th position in
# geometry(Grid we created for subplots)
ax[0][1].plot(x, y)

# ax[0][0] will take 0th position in
# geometry(Grid we created for subplots)
ax[1][0].plot(x, y)

# ax[0][0] will take 0th position in
# geometry(Grid we created for subplots)
ax[1][1].plot(x, y)

plt.show()
