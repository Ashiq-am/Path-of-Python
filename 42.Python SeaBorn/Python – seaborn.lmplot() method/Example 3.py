# importing the required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Tips.csv')

# scatter plot using hue attribute
# for colouring out points
# according to the sex
sns.lmplot(x ='total_bill', y ='tip',
		fit_reg = False, hue = 'sex',
		data = df)

# Show the plot
plt.show()
