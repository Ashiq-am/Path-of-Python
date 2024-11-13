# Importing libraries for dataframe creation
# and graph plotting
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating our own dataframe
data = {"Section": ["A", "B", "C", 'D', 'E'],
		"Students": [0, 10, 20, 30, 40]}

# Now convert this dictionary type data into a pandas dataframe
# specifying what are the column names
df = pd.DataFrame(data, columns=['Section', 'Students'])


# Defining the plot size
plt.figure(figsize=(5, 5))

# Defining the values for x-axis, y-axis
# and from which datafarme the values are to be picked
plots = sns.barplot(x="Section", y="Students", data=df)

# Iterrating over the bars one-by-one
for bar in plots.patches:

	# Using Matplotlib's annotate function and
	# passing the coordinates where the annotation shall be done
	plots.annotate(format(bar.get_height(), '.2f'),
				(bar.get_x() + bar.get_width() / 2,
					bar.get_height()), ha='center', va='center',
				size=15, xytext=(0, 5),
				textcoords='offset points')


# Setting the title for the graph
plt.title("Example 2")

# Fianlly showing the plot
plt.show()
