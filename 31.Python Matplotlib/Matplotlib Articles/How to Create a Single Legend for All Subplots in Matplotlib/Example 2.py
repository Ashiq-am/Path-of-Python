# Plotting sub-plots of number of
# students passed in each subject
# in academic year 2017-20.
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn') # Plot Styles

fig = plt.figure()

# 4 subplots in 2 rows and 2 columns in a figure
axes = fig.subplots(nrows=2, ncols=2)

axes[0, 0].bar(['Telugu', 'Hindi', 'English',
				'Maths', 'Science', 'Social'],
			[50, 27, 42, 34, 45, 48],
			color='g', label="Students passed in 2017")

axes[0, 0].set_yticks(np.arange(0, 51, 5))

axes[0, 1].bar(['Telugu', 'Hindi', 'English',
				'Maths', 'Science', 'Social'],
			[50, 27, 42, 34, 45, 48],
			color='y', label="Students passed in 2018")

axes[0, 1].set_yticks(np.arange(0, 51, 5))

axes[1, 0].bar(['Telugu', 'Hindi', 'English',
				'Maths', 'Science', 'Social'],
			[40, 27, 22, 44, 35, 38],
			color='r', label="Students passed in 2019")

axes[1, 0].set_yticks(np.arange(0, 51, 5))
axes[1, 0].set_xlabel('Subjects', fontsize=25)

# rotating third sub-plot x-axis labels
for tick in axes[1, 0].get_xticklabels():
	tick.set_rotation(45)

axes[1, 0].set_ylabel(" Number of Students passed in 2017-2020", fontsize=20)


axes[1, 1].bar(['Telugu', 'Hindi', 'English',
				'Maths', 'Science', 'Social'],
			[40, 27, 32, 44, 45, 48],
			color='b', label="Students passed in 2020")

axes[1, 1].set_xlabel('Subjects', fontsize=20)
axes[1, 1].set_yticks(np.arange(0, 51, 5))


lines = []
labels = []

for ax in fig.axes:
	Line, Label = ax.get_legend_handles_labels()
	# print(Label)
	lines.extend(Line)
	labels.extend(Label)

# rotating x-axis labels of last sub-plot
plt.xticks(rotation=45)

fig.legend(lines, labels, loc='upper right')

plt.show()
