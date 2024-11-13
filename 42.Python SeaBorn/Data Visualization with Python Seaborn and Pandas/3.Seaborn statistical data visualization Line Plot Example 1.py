# import module
import seaborn as sns
import pandas

# loading csv
data = pandas.read_csv("nba.csv")

# ploting lineplot
sns.lineplot( data['Age'], data['Weight'])
