# import modules
import matplotlib.pyplot as plt
import numpy as np

# depict illustration
g = np.random.rand(20,1)
plt.plot(g, label='gfg')
legend = plt.legend()
frame = legend.get_frame()
frame.set_facecolor('green')
plt.show()
