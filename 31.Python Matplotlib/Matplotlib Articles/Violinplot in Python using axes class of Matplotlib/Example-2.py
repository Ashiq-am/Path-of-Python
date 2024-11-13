# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(10**7)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]

fig, ax1 = plt.subplots()
val = ax1.violinplot(data)
ax1.set_ylabel('Result')
ax1.set_xlabel('Domain Name')
for i in val['bodies']:
	i.set_facecolor('green')
	i.set_alpha(1)

ax1.set_title('matplotlib.axes.Axes.violinplot() Example')
plt.show()
