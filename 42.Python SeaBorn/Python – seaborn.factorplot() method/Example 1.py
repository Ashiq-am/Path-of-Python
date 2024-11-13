# importing the required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Tips.csv')

# point plot(by default)
sns.factorplot(x ='size', y ='tip', data = df)

# Show the plot
plt.show()
