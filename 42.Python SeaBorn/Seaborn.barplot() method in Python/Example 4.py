# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# read a titanic.csv file
# from seaborn libraray
df = sns.load_dataset('titanic')


# who v/s fare barplot
sns.barplot(x = 'who',
			y = 'fare',
			hue = 'class',
			data = df,
			estimator = np.median,
			ci = 0)

# Show the plot
plt.show()
