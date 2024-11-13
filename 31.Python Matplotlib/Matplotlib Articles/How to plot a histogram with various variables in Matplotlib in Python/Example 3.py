# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read in the DataFrame
df = pd.read_csv('medals_by_country_2016.csv')

# plotting three histograms on the same axis
plt.hist(df['Bronze'],bins = 25, alpha = 0.5,
		color = 'red')
plt.hist(df['Gold'],bins = 25, alpha = 0.5,
		color = 'blue')
plt.hist(df['Silver'],bins = 25, alpha = 0.5,
		color = 'yellow')

plt.title("histogram with multiple \
variables (overlapping histogram)")
plt.legend(['Bronze','Gold','Silver'])

plt.show()
