# set the backgroud stle of the plot
sns.set_style('darkgrid')

# plot the graph using the default estimator mean
sns.barplot(x ='sex', y ='total_bill', data = df, palette ='plasma')

# or
import numpy as np

# change the estimator from mean to standard devaition
sns.barplot(x ='sex', y ='total_bill', data = df,
			palette ='plasma', estimator = np.std)
