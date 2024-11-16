# importing packages
import seaborn
import pandas
# load the csv
data = pandas.read_csv("nba.csv")

seaborn.pairplot(data, hue = 'Age', diag_kind = 'kde',
			plot_kws = {'edgecolor': 'k'}, size = 4)
