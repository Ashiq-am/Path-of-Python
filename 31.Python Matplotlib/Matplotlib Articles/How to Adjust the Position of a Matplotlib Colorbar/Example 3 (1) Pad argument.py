# import matplotlib packages
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)


# create chart
fig, ax = plt.subplots(figsize=(4,4))
im = ax.imshow(np.random.rand(11,16))
ax.set_xlabel("x label")

# pad argument to set colorbar away from x-axis
fig.colorbar(im, orientation="horizontal", pad = 0.4)
plt.show()
