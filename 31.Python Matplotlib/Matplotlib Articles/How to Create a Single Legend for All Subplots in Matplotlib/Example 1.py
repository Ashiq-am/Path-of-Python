# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np

# 2 subplots in 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

x1 = ['Telugu', 'Hindi', 'English',
	'Maths', 'Science', 'Social']
y1 = [45, 34, 30, 45, 50, 38]
y2 = [36, 28, 30, 45, 38, 48]

# Labels to use in the legend for each line
labels = ["in 2019", "in 2020"]

# Title for subplots
fig.suptitle('Number of Students passed in each subject from a class in 2019 & 2020', fontsize=20)

# Creating the sub-plots.
l1 = ax1.plot(x1, y1, color="green")
l2 = ax2.plot(x1, y2, color="blue")

ax1.set_yticks(np.arange(0, 51, 5))
ax2.set_yticks(np.arange(0, 51, 5))

ax1.set_ylabel('Number of students', fontsize=25)


fig.legend([l1, l2], labels=labels,
		loc="upper right")

# Adjusting the sub-plots
plt.subplots_adjust(right=0.9)

plt.show()
