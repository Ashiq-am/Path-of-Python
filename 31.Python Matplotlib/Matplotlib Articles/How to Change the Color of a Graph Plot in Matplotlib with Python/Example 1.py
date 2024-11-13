# import packages
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# import dataset
df = pd.read_csv('country_wise_latest.csv')

# select required columns
country = df['Country/Region'].head(10)
confirmed = df['Confirmed'].head(10)

# plotting graph
plt.xlabel('Country')
plt.ylabel('Confirmed Cases')
plt.bar(country, confirmed, color='green', width=0.4)

# display plot
plt.show()
