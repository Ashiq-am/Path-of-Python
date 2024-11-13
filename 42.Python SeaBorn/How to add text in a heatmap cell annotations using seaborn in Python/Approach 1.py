# importing libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# creating random data
data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
				[11, 12, 13, 14, 15]])

# creating array of text
text = np.array([['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'J'],
				['K', 'L', 'M', 'N', 'O']])

# creating subplot
fig, ax = plt.subplots()

# drawing heatmap on current axes
ax = sns.heatmap(data, annot=text, fmt="")
