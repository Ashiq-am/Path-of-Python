import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create DataFrame
df = pd.DataFrame({'var1': [25, 12, 15, 14, 19, 23, 25, 29],
				'var2': [5, 7, 7, 9, 12, 9, 9, 4]})

# create scatterplot
sns.scatterplot(data=df, x='var1', y='var2')

# specify positions of ticks on x-axis and y-axis
plt.xticks([15, 20, 25], ['A', 'B', 'C'])
plt.yticks([4, 8, 12], ['Low', 'Medium', 'High'])
