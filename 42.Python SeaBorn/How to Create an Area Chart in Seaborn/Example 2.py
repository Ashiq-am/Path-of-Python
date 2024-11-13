import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set seaborn style
sns.set_theme()

data = {'period': [1, 2, 3, 4, 5, 6, 7, 8],
				'team_B': [15, 17, 17, 19, 22, 19, 19, 14],
				'team_C': [21, 18, 20, 16, 16, 15, 19, 22]}

# define DataFrame
df = pd.DataFrame(data)

# define colors to use in chart
color_map = ['orange', 'pink']

#create area chart
plt.stackplot(df.period, df.team_B, df.team_C,
			labels=['Team B', 'Team C'],
			colors=color_map)
