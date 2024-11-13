# importing packages
import matplotlib.pyplot as plt
import numpy as np

# making subplots objects
fig, ax = plt.subplots(3, 3)

# draw graph
for i in ax:
	for j in i:
		j.plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))

plt.show()
