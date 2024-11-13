# importing packages
import seaborn
import pandas

# load the csv
data = pandas.read_csv("nba.csv")
seaborn.pairplot(data.head(), hue = 'Age')
