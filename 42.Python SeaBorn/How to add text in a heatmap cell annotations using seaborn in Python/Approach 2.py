# importing libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# creating random data
data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
				[11, 12, 13, 14, 15]])
text = np.array([['A', 'B', 'C', 'D', 'E'],
				['F', 'G', 'H', 'I', 'J'], ['K', 'L', 'M', 'N', 'O']])

# combining text with values
formatted_text = (np.asarray(["{0}\n{1:.2f}".format(
	text, data) for text, data in zip(text.flatten(), data.flatten())])).reshape(3, 5)

# drawing heatmap
fig, ax = plt.subplots()
ax = sns.heatmap(data, annot=formatted_text, fmt="", cmap="cool")
