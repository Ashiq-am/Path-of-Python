# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the DataFrame
df = pd.read_csv('schoolimprovement2010grants.csv')

# creating a histogram
plt.hist(df['Award_Amount'])
plt.show()
