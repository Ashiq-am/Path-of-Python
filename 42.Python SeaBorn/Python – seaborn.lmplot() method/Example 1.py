# importing the required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Tips.csv')

# scatter plot with regression
# line(by default)
sns.lmplot(x ='total_bill', y ='tip', data = df)

# Show the plot
plt.show()
