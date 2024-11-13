import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set seaborn style
sns.set_theme()

# define DataFrame
df = pd.DataFrame({'Class': [1, 2, 3, 4, 5, 6, 7, 8],
				'sec_A': [20, 12, 9, 14, 18, 20, 15, 22],
				'sec_B': [ 12, 5, 7, 7, 9, 9, 9, 4],
				'sec_C': [11, 8, 5, 9, 12, 10, 6, 6]})

# define colors to use in chart
color_map = ['yellow', 'blue', 'black']

# create area chart
plt.stackplot(df.Class, df.sec_A, df.sec_B, df.sec_C,
			labels=['Sec A', 'Sec B', 'Sec C'],
			colors=color_map)
