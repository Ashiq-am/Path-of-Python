# import packages
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# import dataset
df = pd.read_csv('country_wise_latest.csv')

# select required data
country = df['Country/Region'].head(20)
confirmed = df['Active'].head(20)

# plot graph
plt.xlabel('Country')
plt.ylabel('Active Cases')
plt.bar(country, confirmed, color='maroon', width=0.4)

# display plot
plt.show()
