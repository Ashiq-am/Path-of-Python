# importing the required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Tips.csv')

# point plot using hue attribute
# for colouring out points
# according to the sex
sns.factorplot(x ='size', y ='tip',
			hue = 'sex', data = df)

# Show the plot
plt.show()
