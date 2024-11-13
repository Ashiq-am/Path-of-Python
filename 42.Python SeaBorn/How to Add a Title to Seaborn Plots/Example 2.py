# import necessary packages
import pandas as pd
import seaborn as sns

# create a dataframe
temperature = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar',
									'Apr', 'May', 'Jun',
									'Jul', 'Aug', 'Sep',
									'Oct', 'Nov', 'Dec'],
							'Avg_Temperatures': [22, 25, 28,
												32, 35, 44,
												38, 32, 25,
												23, 20, 18]})

# plot a rel-plot
plot = sns.relplot(x='Month', y='Avg_Temperatures', data=temperature)

# add title using suptitle
plot.fig.suptitle('Monthly Avg Temperatures')
